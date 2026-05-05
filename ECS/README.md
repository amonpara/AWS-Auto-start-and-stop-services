# 🐳 ECS Auto Start/Stop Setup

## 📌 Overview

This guide explains how to automate start and stop of ECS services using AWS Lambda and EventBridge Scheduler.

Unlike EC2/RDS, ECS services are controlled by adjusting the **desired count** of tasks.

## 💡 Concept

- **Start ECS Service** → Set desired count > 0  
- **Stop ECS Service** → Set desired count = 0  

---

## 🧱 Architecture

EventBridge (Scheduler with Input)
        ↓
      Lambda
        ↓
   ECS Service Update

## 🔐 Step 1: IAM Role for Lambda 

- Create IAM Role with Lambda service
- Attach policy

## ⚙️ Step 2: Create Lambda Function

- Create lambda function: ECS-start-stop and update the code. 

## ⏰ Step 3: EventBridge Scheduler

- Create a Scheduler Rules for that
- Add cron for start at 9:00 AM IST
    - cron(30 3 * * ? *)
    - Add Input Constant JSON

- Add cron for stop at 9:00 PM IST
    - cron(30 15 * * ? *)
    - Add Input Constant JSON

## 🧪 Step 4: Testing

- Trigger Lambda manually with:
    - { "action": "start" }
- Then:
    - { "action": "stop" }

- Verify:
    - ECS Service desired count updates
    - Tasks start/stop accordingly

## ⚠️ Important Notes

- Ensure your service supports scaling to 0 tasks
- If using Load Balancer:
    - Health checks may fail when stopped (expected)
    - Startup may take time depending on container/image size