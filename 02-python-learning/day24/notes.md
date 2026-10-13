Assignment 8: Configure Nginx Reverse Proxy on AWS EC2
1. Objective

Configure Nginx as a reverse proxy to forward HTTP requests to a Node.js application running on an Ubuntu EC2 instance.

2. Technologies used

AWS EC2: Hosts the application on a cloud server.

Ubuntu: Operating system of the EC2 instance.

Node.js: Runs the web application on port 3000.

PM2: Manages and monitors the Node.js process.

Nginx: Receives HTTP requests on port 80 and forwards them to Node.js.

3. Architecture
User's Browser

HTTP — Port 80

Nginx Reverse Proxy

Forwards to 127.0.0.1:3000

Node.js Application + PM2
4. Important commands

Purpose

	

Command




Install Nginx

	

sudo apt install -y nginx




Start and enable Nginx

	

sudo systemctl enable --now nginx




Check Nginx status

	

sudo systemctl status nginx




Create configuration

	

sudo nano /etc/nginx/sites-available/my-node-app




Enable configuration

	

sudo ln -s /etc/nginx/sites-available/my-node-app /etc/nginx/sites-enabled/my-node-app




Test configuration

	

sudo nginx -t




Reload Nginx

	

sudo systemctl reload nginx




Check Node.js with PM2

	

pm2 status




View application logs

	

pm2 logs my-node-app --lines 15




Test locally

	

curl http://localhost

5. Nginx configuration

File: /etc/nginx/sites-available/my-node-app

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

After creating the file, enable it, test the configuration using sudo nginx -t, and reload Nginx.

6. AWS Security Group

SSH — TCP port 22, restricted to your IP.

HTTP — TCP port 80, restricted to your IP for practice.

Port 3000 was used to test Node.js directly. Once the reverse proxy is verified, you can remove its inbound rule if direct access is no longer required.

7. Common error

Error: EADDRINUSE: address already in use 0.0.0.0:3000

Meaning: Another process is already using port 3000.

Commands to troubleshoot:

sudo lsof -i :3000
pm2 status
pm2 restart my-node-app

Inspect the process before stopping it to avoid terminating the wrong application.

8. Interview questions

Q1. What is a reverse proxy?

A reverse proxy receives client requests and forwards them to a backend server, then returns the response to the client.

Q2. Why use Nginx with Node.js?

Nginx provides a public HTTP entry point, forwards requests to Node.js, and can help with load balancing, TLS termination, and serving static files.

Q3. What is PM2?

PM2 is a process manager for Node.js applications. It helps keep applications running and provides process monitoring and logs.

Q4. Why use port 80?

Port 80 is the standard port for HTTP traffic, so users can access the website without specifying a port number.

Q5. How do you test Nginx configuration?

Run sudo nginx -t before reloading Nginx.

Result: Nginx was configured as a reverse proxy, and the Node.js application returned the expected response using curl http://localhost.