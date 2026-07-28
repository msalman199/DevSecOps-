import jenkins.model.*
import hudson.security.*
import hudson.util.Secret

def instance = Jenkins.getInstance()
def credentialsStore = instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0]

if (credentialsStore != null) {
    def credentials = credentialsStore.getCredentials()
    credentials.each { cred ->
        println "ID: ${cred.id}"
        println "Description: ${cred.description}"
        if (cred.hasProperty('username')) {
            println "Username: ${cred.username}"
        }
        if (cred.hasProperty('password')) {
            println "Password: ${Secret.toString(cred.password)}"
        }
        println "---"
    }
}
