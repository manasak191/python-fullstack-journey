# day 14 of learning AWS concept

# IAM
# EC2 Instances
# Types of EC2 Instances 
    # General Purpose
    # Compute Optimized
    # Memory Optimized
    # GPU


1.AWS
    Amazon Web Services, is a cloud platform that provides services such as computing, storage, databases, networking, security and monitoring over the internet.

2.Region

    A region is a geographical area containing cloud infrastructure.

    For example:

    AWS Region
    ↓
    Multiple Availability Zones

    A company may deploy an application in a region closer to its customers.

    Real-world example

    If most customers are in India, a company may choose an AWS region serving India to reduce network latency.

3.Availability Zone — AZ

    An Availability Zone is an isolated location within an AWS Region.

    Think:

    Region
    │
    ├── AZ 1
    ├── AZ 2
    └── AZ 3

    Why?

    High availability.

    If one AZ has a problem, workloads can potentially continue in another AZ.

4.IAM - Identity and Access Management
    # IAM controls:
        Who can access what?

    # Understand:
        User
        Group
        Role
        Policy
        Permissions
        Root user
        Least privilege
        MFA- Multi Factor Autentication 
    
    # Root user
        The root user is the account's original, highest-level AWS identity.
    
    # group 
        An IAM group is a collection of IAM users to which permissions can be assigned collectively.

    # least privilege
        Give a user or service only the permissions required to perform its task.
        # Example:

            If an application only needs to read files from S3, don't give it permission to delete all S3 files.

5.AWS EC2 -Elastic Compute Cloud
    Amazon EC2 is a service that provides resizable virtual servers in the AWS cloud. It is commonly used to host applications and backend services.

    You built:

    Python FastAPI application

    we can deploy backend  the backend appliaction on EC2 Instance.

    AWS EC2

    Users:

    Browser
    ↓
    Internet
    ↓
    EC2
    ↓
    FastAPI

6.EC2 Instance Types
    Different applications have different resource requirements, so AWS provides different instance types optimized for Compute, Memory, Storage or GPU workloads.

    # For example:

        General purpose → balanced CPU + memory

        Compute optimized → more CPU

        Memory optimized → more RAM

        GPU → machine learning / graphics

7.Security Groups
    A security group is a virtual firewall that controls inbound and outbound traffic for AWS resources such as EC2 instances.

    # Port	Usage
        22	SSH
        80	HTTP
        443	HTTPS
        3306	MySQL
        5432	PostgreSQL
        8000	Common FastAPI development port

# Assignment 1 — What you completed
    AWS Account
        │
        └── IAM
            │
            ├── User
            │    └── developer1
            │
            └── Group
                │
                └── EC2-Practice-Users
                        │
                        └── AmazonEC2ReadOnlyAccess

