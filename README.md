# 🚀 AWS Auto Start/Stop Automation

## 📌 Overview

This repository provides step-by-step guides to automate start and stop of AWS resources to optimize cloud costs.

Currently supported services:
- EC2
- RDS
- ECS

## 💰 Why This?

AWS resources run 24/7 by default, even when not in use.

This solution helps:
- Reduce unnecessary costs
- Automate resource lifecycle
- Maintain availability during working hours

---

## 📂 Folder Structure

- `/EC2` → EC2 automation steps  
- `/RDS` → RDS automation steps  
- `/ECS` → ECS automation steps

## ⚠️ Important Notes

- RDS cannot be stopped for more than 7 days
- Aurora & Multi-AZ RDS are not supported for stop/start

## 🎯 Outcome

- Reduce cost by ~50% for dev and stage env

## 👨‍💻 Author

Abhishek Monpara