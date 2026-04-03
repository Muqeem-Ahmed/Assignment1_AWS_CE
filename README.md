Assignment 1: UniEvent AWS ArchitectureCourse: CE 308/408 Cloud Computing 
Institution: Ghulam Ishaq Khan Institute 
Architecture Design VPC & Networking: Custom VPC with 2 Public Subnets (Load Balancer) and 2 Private Subnets (Application Servers).
Security: IAM Roles used for S3 access; Security Groups restrict EC2 traffic to only the Load Balancer.
Availability: Multi-AZ deployment with an Elastic Load Balancer (ELB) and Auto Scaling Group to handle instance failures.
Step-by-Step Setup GuideInfrastructure Provisioning:
    Create an S3 Bucket for event posters and media.
    Set up an IAM Role with S3FullAccess and attach it to your EC2 instance profile.
    API Key Integration:Obtain a public API key (e.g., Ticketmaster or Eventbrite).
    Update the main.py file with your API key and S3 bucket name.
    Application Launch:Launch an EC2 Auto Scaling Group in the Private Subnets.Paste the content of scripts/user_data.sh into the User Data field to automate deployment.
    Verification:Access the DNS name of your Elastic Load Balancer.The app will automatically fetch events, store posters in S3, and display them as "University Events".
