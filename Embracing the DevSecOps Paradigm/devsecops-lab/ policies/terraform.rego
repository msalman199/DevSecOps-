package terraform

import rego.v1

# Deny if containers expose ports to 0.0.0.0
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    port := resource.values.ports[_]
    port.external != null
    msg := sprintf("Container '%s' exposes port %d to all interfaces", [resource.name, port.external])
}

# Deny if containers run as root
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    not resource.values.user
    msg := sprintf("Container '%s' runs as root user", [resource.name])
}

# Require environment specification
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    not has_environment_tag(resource)
    msg := sprintf("Container '%s' missing environment specification", [resource.name])
}

has_environment_tag(resource) if {
    env := resource.values.env[_]
    startswith(env, "ENVIRONMENT=")
}
