# AWS EC2 Hands-on – Day 1

## 1. EC2 Instance Setup

Created an EC2 instance with:

* Amazon Linux AMI
* Small/free-tier eligible instance type
* Key pair: `aws-practice-key`
* VPC: Default VPC
* Public IP: Enabled
* Security Group: `python-practice-sg`
* SSH: TCP Port `22`
* Source: My IP
* EBS: Default root volume

---

## 2. SSH Connection from Windows

Located the `.pem` key:

```powershell
cd $HOME\Downloads
dir aws-practice-key.pem
```

Connected to EC2:

```powershell
ssh -i ".\aws-practice-key.pem" ec2-user@<PUBLIC_IP>
```

Example:

```powershell
ssh -i ".\aws-practice-key.pem" ec2-user@35.154.213.126
```

Successfully connected:

```text
[ec2-user@ip-...]$
```

---

## 3. Basic Linux Commands

Check current user:

```bash
whoami
```

Check current directory:

```bash
pwd
```

Check system information:

```bash
uname -a
```

Check Python version:

```bash
python3 --version
```

---

## 4. Create Python Project on EC2

Create project directory:

```bash
mkdir aws-python-app
```

Move into the directory:

```bash
cd aws-python-app
```

Check current location:

```bash
pwd
```

Expected:

```text
/home/ec2-user/aws-python-app
```

---

## 5. Create Python Application

Create Python file:

```bash
nano app.py
```

Python code:

```python
print("Hello from my AWS EC2 server!")
print("I deployed my Python application on AWS.")
```

Save in Nano:

```text
Ctrl + O → Enter → Ctrl + X
```

Run the application:

```bash
python3 app.py
```

Expected output:

```text
Hello from my AWS EC2 server!
I deployed my Python application on AWS.
```

---

## 6. Important Concepts Learned

### EC2

A virtual server in AWS used to run applications.

### Security Group

A virtual firewall that controls inbound and outbound traffic.

### SSH

Secure protocol used to remotely connect to a Linux EC2 server.

### Key Pair

Used for secure SSH authentication.

### Public IP

Allows the EC2 server to communicate over the internet.

### VPC

A logically isolated virtual network in AWS.

### EBS

Persistent block storage attached to an EC2 instance.

---

## 7. Important Observation

When an EC2 instance is **stopped and started**, its public IPv4 address can change.

Therefore, check the current Public IPv4 address before reconnecting:

```powershell
ssh -i ".\aws-practice-key.pem" ec2-user@<NEW_PUBLIC_IP>
```

## Hands-on Result

✅ Created EC2 instance
✅ Configured Security Group
✅ Created SSH key pair
✅ Connected to Linux server using SSH
✅ Practiced Linux commands
✅ Verified Python on EC2
✅ Created a Python project on the cloud server

## Next

* Build a FastAPI application on EC2
* Configure Security Group for the application
* Access FastAPI from a browser
* Practice Docker on EC2
* Practice IAM Roles with EC2
* Connect EC2 with S3
