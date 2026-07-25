# Environment Configuration
project_name = "devsecops-lab"
environment  = "development"
aws_region   = "us-east-1"

# Network Configuration
vpc_cidr            = "10.0.0.0/16"
public_subnet_cidr  = "10.0.1.0/24"
private_subnet_cidr = "10.0.2.0/24"

# Instance Configuration
instance_type   = "t3.micro"
key_pair_name   = "lab-key-pair"
