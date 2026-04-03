#!/bin/bash
# Update and install dependencies
yum update -y
yum install python3 git -y
pip3 install flask requests boto3

# Clone the repository
cd /home/ec2-user
git clone https://github.com/Muqeem-Ahmed/Assignment1_AWS_CE.git
cd Assignment1_AWS_CE/app

# Set environment variables for S3
export BUCKET_NAME="your-unievent-s3-bucket"

# Run the application
python3 main.py