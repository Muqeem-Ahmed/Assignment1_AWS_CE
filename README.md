# Assignment1_AWS_CE: UniEvent Management System

## Overview
Scalable, fault-tolerant AWS platform fetching real-time event data via Open API with secure S3 media storage.

## Architecture
- **VPC**: Custom VPC; 2 Public (ALB) and 2 Private (App Servers) subnets.
- **Security**: IAM Roles for S3 access; Security Groups restricted to ALB traffic.
- **Availability**: Multi-AZ deployment with ALB and ASG for self-healing.
- **Connectivity**: NAT Gateway for private subnet API data fetching.
- **Storage**: S3 bucket `unievent-media-storage-giki` for event posters.

## API Justification
- **Ticketmaster Discovery API**: Provides structured JSON (Title, Date, Venue, Images) for automated event integration.

## User Data Script
Automates web server setup and deployment:

```bash
#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
echo "<h1>Welcome to UniEvent - Deployment Successful!</h1>" > /var/www/html/index.html
````

## Evidence Documentation

Detailed architectural evidence and project verification screenshots are located in: **app/screenshot/**

The folder contains:

  - **VPC Resource Map**: 2 public and 2 private subnet proof.
  - **Target Group Health**: Confirmation of "Healthy" status for all instances.
  - **Private Subnet Proof**: Verification that EC2 instances have no public IP addresses.
  - **S3 Objects**: Proof of successful media storage integration.
  - **Live Site**: Screenshot of the functional app via the Load Balancer.

## Live Application

To access the live production environment, use the following link:

**Link**: https://www.google.com/search?q=http://unievent-alb-1085333370.ap-southeast-2.elb.amazonaws.com/

**Instruction**: Copy and paste the URL into any web browser to view the deployed platform.

```
```
