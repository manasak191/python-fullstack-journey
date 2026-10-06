# AWS EC2 Hands-on – Assignment 1
## Deploy Static Website on EC2

### Architecture
Browser
  ↓
EC2 Public IP
  ↓
Security Group
  ↓
HTTP Port 80
  ↓
Apache/httpd
  ↓
/var/www/html/index.html

### Apache installation
sudo dnf install httpd -y

### Start Apache
sudo systemctl start httpd

### Check Apache
sudo systemctl status httpd

### Enable Apache at boot
sudo systemctl enable httpd

### Website directory
/var/www/html

### Create website
sudo nano /var/www/html/index.html

### Test from EC2
curl http://localhost

### Security Group
SSH:
Port 22 → My IP

HTTP:
Port 80 → Anywhere IPv4 (0.0.0.0/0)

### Access website
http://<EC2-PUBLIC-IP>

### Concepts learned
- EC2
- Apache Web Server
- HTTP
- Port 80
- SSH Port 22
- Security Groups
- Public IPv4
- Linux systemctl
- Document Root
- Static Website Deployment


Have you deployed a website on AWS EC2?"

"Yes. I deployed a static HTML website on an Amazon Linux EC2 instance using Apache HTTP Server. I configured the Security Group to allow SSH on port 22 and HTTP on port 80, installed and started Apache, placed my HTML file in /var/www/html, and accessed the website using the EC2 public IP."


EC2 can host websites

EC2 isn't only for running Python applications. You can use it as a server for:

HTML/CSS websites
Java applications
Node.js applications
Python applications
APIs
Databases and other services
2. What is Apache?

Apache is a web server.

Its job is basically:

Receive a request → find the requested website file → send it back to the browser.

In your case:

Browser requests /
       ↓
Apache
       ↓
/var/www/html/index.html
       ↓
Browser receives HTML