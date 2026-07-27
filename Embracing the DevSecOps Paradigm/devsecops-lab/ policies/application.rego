package application

import rego.v1

# Deny if debug mode is enabled in production
deny contains msg if {
    input.environment == "production"
    input.debug == true
    msg := "Debug mode should not be enabled in production"
}

# Require HTTPS in production
deny contains msg if {
    input.environment == "production"
    input.protocol != "https"
    msg := "HTTPS must be used in production environment"
}
