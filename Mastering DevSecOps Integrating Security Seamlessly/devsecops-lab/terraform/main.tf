terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC Configuration
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "devsecops-vpc"
    Environment = var.environment
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "devsecops-igw"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true

  tags = {
    Name = "devsecops-public-subnet"
  }
}

# Security Group with intentional misconfigurations for demonstration
resource "aws_security_group" "web" {
  name_prefix = "devsecops-web-"
  vpc_id      = aws_vpc.main.id

  # Intentionally insecure - allows all traffic (for demonstration)
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devsecops-web-sg"
  }
}

# S3 Bucket with security issues for demonstration
resource "aws_s3_bucket" "app_data" {
  bucket = "devsecops-demo-bucket-${random_string.bucket_suffix.result}"

  tags = {
    Name        = "devsecops-app-data"
    Environment = var.environment
  }
}

# Intentionally insecure S3 bucket configuration
resource "aws_s3_bucket_public_access_block" "app_data" {
  bucket = aws_s3_bucket.app_data.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

data "aws_availability_zones" "available" {
  state = "available"
}
