# ⚙️ EC2 Auto Start/Stop Setup

## 📌 Overview

This guide explains how to automate start and stop of EC2 instances using AWS Lambda and EventBridge.

---

## 🧱 Architecture

EventBridge → Lambda → EC2

## 🔐 Step 1: Create IAM Role

- Create IAM Role with Lambda service
- Attach policy 

## ⚙️ Step 2: Create Lambda Function

- Create 2 lambda function: Start EC2 & Stop EC2 and update the code. 

## ⏰ Step 3: EventBridge Scheduler

- Setup a Scheduler as per your requirement.

- Ex. Start at 9:00 AM IST 
    - cron(30 3 * * ? *)

- Ex. Stop at 9:00 PM IST
    - cron(30 15 * * ? *)

## 🧪 Testing

- Run Lambda manually
- Verify instance state
- Check CloudWatch logs