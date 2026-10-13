AWS EC2 – Assignment 2
Deploy Java Spring Boot JAR on EC2
Objective

Deploy and run a Java Spring Boot .jar application on an Amazon Linux EC2 instance.

Architecture

Browser
↓
EC2 Public IP : 8080
↓
Spring Boot Application
↓
Java .jar file

Concepts Learned
1. JAR

JAR stands for Java Archive.

A Spring Boot application can be packaged into a .jar file containing the application and its required components.

Example:

my-spring-app.jar

A JAR can be executed using:

java -jar my-spring-app.jar
2. Java on EC2

Our EC2 instance is running Amazon Linux.

Java was installed using:

sudo dnf install java-17-amazon-corretto -y

Amazon Corretto is AWS's distribution of OpenJDK.

Verify Java:

java -version

Expected output contains:

openjdk version "17..."
Corretto-17
3. Running a JAR

The general command is:

java -jar <actual-jar-file>.jar

Example:

java -jar my-spring-app.jar
Important

This command:

java -jar your-application.jar

was only an example.

your-application.jar must be replaced with the actual JAR filename.

If the JAR doesn't exist in the current directory, Java will show an error such as:

Unable to access jarfile ...
4. Check for JAR files

To see files in the current directory:

ls -la

To specifically look for JAR files:

ls *.jar

If there is no JAR file, we need to create/build or upload one before running it.

5. Application Port

Spring Boot commonly uses:

Port 8080

So the Security Group needs an inbound rule:

Custom TCP
Port: 8080
Source: My IP

For a public demo application, the source could be:

0.0.0.0/0

But for practice, restricting it to your IP is safer when possible.

6. Difference Between Assignment 1 and Assignment 2
Assignment 1
Browser
   ↓
Port 80
   ↓
Apache
   ↓
HTML file
Assignment 2
Browser
   ↓
Port 8080
   ↓
Spring Boot
   ↓
Java JAR

Apache serves static files, while Spring Boot runs an actual Java application.

7. Deployment Steps — Remaining
Step 1 — Create Spring Boot application

Create a simple Spring Boot application with an endpoint such as:

GET /

which returns:

Hello from Spring Boot on AWS EC2!
Step 2 — Build the application

Build/package the application into a JAR.

Example with Maven:

mvn clean package

The JAR will normally appear inside:

target/
Step 3 — Transfer JAR to EC2

Transfer the generated JAR from the local computer to EC2.

Step 4 — Configure Security Group

Allow the Spring Boot application port:

TCP 8080
Step 5 — Run the application

On EC2:

java -jar <actual-jar-file>.jar
Step 6 — Test

From the EC2 server:

curl http://localhost:8080

Then from your computer:

http://<EC2-PUBLIC-IP>:8080
What I Learned from Assignment 2
What a Java JAR file is
How Java applications can run on EC2
How to install Java on Amazon Linux
Amazon Corretto
How java -jar works
Why an actual JAR file is required
Application ports
Spring Boot's commonly used port 8080
How Security Groups control application access
Difference between a static website and a backend application
Basic EC2 application deployment workflow
Interview Answer

If asked:

"Have you deployed a Spring Boot application on EC2?"


"Yes. I deployed a Spring Boot application on an Amazon Linux EC2 instance. I installed Java using Amazon Corretto, transferred the Spring Boot JAR to the EC2 server, configured the Security Group to allow the application port, and ran the application using the java -jar command. I then tested the application through the EC2 public IP."