# 🛢️ RDS Auto Start/Stop Setup

## 📌 Overview

This guide explains how to automate start and stop of RDS instances using AWS Lambda and EventBridge.

---

## 🧱 Architecture

EventBridge → Lambda → RDS

---

## ⚠️ Important Limitations

- Only works for Single-AZ RDS
- Not supported for:
  - Multi-AZ
  - Aurora clusters
- Max stop duration = 7 days

## 🔐 Step 1: Create IAM Role

- Create IAM Role with Lambda service
- Attach policy 

## ⚙️ Step 2: Create Lambda Function

- Create 2 lambda function: Start RDS & Stop RDS and update the code. 

## ⏰ Step 3: EventBridge Scheduler

- Setup a Scheduler as per your requirement.

- Ex. Start at 9:00 AM IST 
    - cron(30 3 * * ? *)

- Ex. Stop at 9:00 PM IST
    - cron(30 15 * * ? *)

## 🧪 Testing

- Trigger Lambda manually
- Verify DB status
- Check logs