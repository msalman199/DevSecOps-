# Privacy Compliance Controls

title 'Privacy and Data Protection Controls'

control 'privacy-001' do
  impact 1.0
  title 'Data Encryption at Rest'
  desc 'Ensure sensitive data is encrypted when stored'
  
  describe file('/etc/ssl/certs') do
    it { should exist }
    it { should be_directory }
  end
  
  # Check if application uses HTTPS
  describe port(443) do
    it { should be_listening }
  end
end

control 'privacy-002' do
  impact 0.8
  title 'Password Storage Security'
  desc 'Ensure passwords are not stored in plain text'
  
  # Check application code for plain text passwords
  describe file('/home/ubuntu/devsecops-lab/src/app.py') do
    its('content') { should_not match(/password.*=.*['"][^'"\$]/) }
  end
end

control 'privacy-003' do
  impact 0.9
  title 'Session Security'
  desc 'Ensure secure session management'
  
  # Check for secure session configuration
  describe file('/home/ubuntu/devsecops-lab/src/app.py') do
    its('content') { should match(/secret_key/) }
  end
end

control 'privacy-004' do
  impact 0.7
  title 'Data Minimization'
  desc 'Ensure only necessary data is collected'
  
  # Check database schema for excessive data collection
  describe command('sqlite3 /home/ubuntu/devsecops-lab/src/users.db ".schema"') do
    its('stdout') { should_not match(/ssn|social_security|credit_card/) }
  end
end

control 'privacy-005' do
  impact 1.0
  title 'Access Logging'
  desc 'Ensure access to sensitive data is logged'
  
  describe file('/var/log/auth.log') do
    it { should exist }
    it { should be_readable }
  end
end
