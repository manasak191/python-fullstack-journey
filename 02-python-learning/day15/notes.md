# Assignment 2 - Launching an EC2 instance

1.AMI
    AMI stands for Amazon Machine Image. It is a template used to create an EC2 instance. It contains the operating system and other configuration required to launch the instance.

2.What is an EC2 instance type?"
    "An EC2 instance type defines the computing resources allocated to an EC2 instance, such as CPU, memory, networking, and other capabilities. Different instance families are designed for different workloads."

3.Key pair in EC2
    An EC2 key pair consists of a public key and a private key. AWS places the public key on the EC2 instance, while the private key is kept by the user and is used to securely authenticate when connecting to the instance, typically through SSH.

4. Linux server running in AWS.
              AWS
                  │
                 EC2
                  │
        ┌─────────┼─────────┐
        │         │         │
       AMI      Network    Storage
        │         │         │
     Linux      VPC       EBS
                  │
             Security Group
                  │
             Public IP
                  │
             SSH Access