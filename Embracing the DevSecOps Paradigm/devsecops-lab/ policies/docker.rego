package docker

import rego.v1

# Deny running containers as root
deny contains msg if {
    input.User == "root"
    msg := "Container should not run as root user"
}

# Deny containers without health checks
deny contains msg if {
    not input.Config.Healthcheck
    msg := "Container should have health check configured"
}

# Deny containers with privileged mode
deny contains msg if {
    input.HostConfig.Privileged == true
    msg := "Container should not run in privileged mode"
}
