Assignment 6 — Interview notes

Project: EC2 Monitoring using Amazon CloudWatch and SNS

Objective: Monitor an EC2 instance and receive email notifications when CPU utilization exceeds 80%.

Services used: Amazon EC2, Amazon CloudWatch, Amazon SNS.

What I implemented:

Selected the EC2 CPU utilization metric.

Created a CloudWatch alarm with an 80% threshold.

Configured an SNS topic for email notifications.

Confirmed the email subscription and verified the alarm status.

Common interview questions

1. What is Amazon CloudWatch?

Amazon CloudWatch is a monitoring service that collects metrics, logs, and events from AWS resources. It helps monitor application and infrastructure performance.

2. What is a CloudWatch alarm?

A CloudWatch alarm monitors a metric against a specified condition and changes state when that condition is met.

3. What is Amazon SNS?

Amazon Simple Notification Service (SNS) sends notifications to subscribers, such as email addresses, when a service publishes a message.

4. Why did you use CloudWatch with SNS?

CloudWatch detects a threshold breach, and SNS sends an email notification so the administrator can investigate.

5. Why is the alarm showing OK?

It means the alarm's condition is not currently breached. If the alarm doesn't have sufficient recent data, it may instead show INSUFFICIENT_DATA.