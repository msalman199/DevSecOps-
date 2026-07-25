#!/bin/bash
yum update -y
yum install -y httpd

# Start and enable Apache
systemctl start httpd
systemctl enable httpd

# Create a simple web page
cat > /var/www/html/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>${project_name} - DevSecOps Lab</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .header { color: #2c3e50; }
        .info { background-color: #ecf0f1; padding: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1 class="header">Welcome to ${project_name}</h1>
    <div class="info">
        <h2>DevSecOps Infrastructure Lab</h2>
        <p>This server was deployed using Terraform Infrastructure as Code.</p>
        <p>Server deployed at: $(date)</p>
        <p>Hostname: $(hostname)</p>
    </div>
</body>
</html>
