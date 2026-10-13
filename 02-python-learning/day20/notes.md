Assignment 4: Secure Bastion Host — Interview Notes
1. What is a Bastion Host?

A Bastion Host is a secure server used to access instances in a private network. In AWS, it is usually an EC2 instance in a public subnet that acts as a gateway to private servers.

Real-world example: A company allows administrators to access private application servers through a Bastion Host instead of exposing those servers directly to the internet.

2. What did you do in this assignment?

I created two EC2 instances in AWS:

Bastion Host: Deployed in a public subnet with a public IP address.

Private Server: Deployed in a private subnet without a public IP address.

I configured security groups to allow SSH access to the Bastion Host from my IP address and SSH access to the private server only from the Bastion Host. Then I connected to the private server through the Bastion Host using SSH.

3. Important interview questions

Q1. What is a VPC?

A Virtual Private Cloud (VPC) is an isolated virtual network in AWS where we launch and manage cloud resources.

Q2. What is the difference between public and private subnets?

A public subnet has a route to an Internet Gateway. A private subnet has no direct route to an Internet Gateway.

Q3. What is a security group?

A security group is a virtual firewall that controls inbound and outbound traffic for AWS resources.

Q4. What is an Internet Gateway?

An Internet Gateway allows communication between a VPC and the internet when routing, IP addressing, and security rules permit it.

Q5. What is SSH?

SSH stands for Secure Shell. It is used to securely connect to and manage remote servers, usually through port 22.

Q6. Why shouldn't we expose a private server directly to the internet?

To reduce unauthorized access and improve security by restricting direct internet exposure.

Q7. Why shouldn't we copy the private key to the Bastion Host?

Keeping the private key on our local computer reduces the risk of key theft if the Bastion Host is compromised.

Q8. What is the purpose of a route table?

A route table determines where network traffic should be directed, such as within a VPC or toward an Internet Gateway.

4. Project explanation for interviews
Writing

I completed an AWS project to create a secure Bastion Host for accessing a private EC2 instance. I launched two EC2 instances, configured public and private subnet routing, and created security groups to restrict SSH access. First, I connected to the Bastion Host from my computer, then accessed the private server through it using SSH without copying my private key to the Bastion Host. This project helped me understand VPCs, route tables, security groups, and secure access to private cloud resources.

Remember these six keywords: Bastion Host, VPC, public and private subnets, route tables, security groups, and SSH.