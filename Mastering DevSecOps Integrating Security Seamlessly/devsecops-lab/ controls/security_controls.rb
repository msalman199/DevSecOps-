# Security Controls for DevSecOps Demo

control 'docker-security-1' do
  title 'Docker daemon configuration'
  desc 'Ensure Docker daemon is configured securely'
  impact 0.7
  
  describe file('/etc/docker/daemon.json') do
    it { should exist }
  end
  
  describe json('/etc/docker/daemon.json') do
    its(['log-driver']) { should eq 'json-file' }
  end
end

control 'system-security-1' do
  title 'System security configuration'
  desc 'Ensure system is configured with security best practices'
  impact 0.8
  
  describe file('/etc/passwd') do
    its('mode') { should cmp '0644' }
  end
  
  describe file('/etc/shadow') do
    its('mode') { should cmp '0640' }
  end
end

control 'network-security-1' do
  title 'Network security configuration'
  desc 'Ensure network is configured securely'
  impact 0.6
  
  describe port(22) do
    it { should be_listening }
  end
  
  describe iptables do
    it { should have_rule('-P INPUT DROP') }
  end
end

control 'application-security-1' do
  title 'Application security checks'
  desc 'Ensure application follows security best practices'
  impact 0.9
  
  describe file('/app/package.json') do
    it { should exist }
  end
  
  # Check for known vulnerable packages
  describe command('npm audit --json') do
    its('exit_status') { should eq 0 }
  end
end
