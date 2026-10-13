Assignment 7 — Interview revision notes

Project: Deploy a Node.js Application on AWS EC2

Objective: Deploy a Node.js web server on an Ubuntu EC2 instance and access it through a browser.

Technologies: AWS EC2, Ubuntu, Node.js, npm, PM2, security groups.

What I did:

Launched an Ubuntu EC2 instance.

Installed Node.js and npm.

Built a basic HTTP server using Node.js.

Tested the application using curl.

Configured the security group to allow traffic on port 3000.

Used PM2 to manage the application in the background.

Common interview questions

1. What is Amazon EC2?

Amazon EC2 is a cloud service that provides virtual servers to run applications.

2. What is Node.js?

Node.js is a JavaScript runtime that lets us execute JavaScript outside a browser, including on backend servers.

3. What is npm?

npm is a package manager used to install and manage Node.js packages.

4. What is a security group?

A security group acts as a virtual firewall that controls inbound and outbound traffic for AWS resources.

5. Why did you use PM2?

PM2 manages Node.js processes, runs applications in the background, and can restart them if they crash.

6. What does port 3000 do?

It is the port on which our Node.js server listens for HTTP requests.

Before we move to Assignment 8

One important note: PM2 keeps the application running in the background, but that alone doesn't guarantee automatic startup after an EC2 reboot. We can configure that separately if required.

Also, because port 3000 is publicly reachable only from your configured security-group source, check that your inbound rule is restricted to your IP.