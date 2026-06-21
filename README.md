# AI-Based Predictive Maintenance System

## Overview

An AI-powered predictive maintenance system designed for personal computers and data centers.

The system collects live hardware telemetry, stores historical performance data, visualizes system health through a dashboard, and uses machine learning to estimate system risk levels.

---

## Dashboard

<img width="1847" height="950" alt="Screenshot 2026-06-21 164134" src="https://github.com/user-attachments/assets/20c0fdf3-c2f8-4c8c-b735-b70a32c832b2" />

<img width="1725" height="742" alt="Screenshot 2026-06-21 164154" src="https://github.com/user-attachments/assets/672d70da-a128-4cbf-9ec4-341e0ecda215" />

<img width="1732" height="607" alt="Screenshot 2026-06-21 164205" src="https://github.com/user-attachments/assets/0db0b144-22cd-4bc6-a40a-85f5463a1961" />

<img width="1760" height="576" alt="Screenshot 2026-06-21 164215" src="https://github.com/user-attachments/assets/d1483189-f517-49fc-971f-753647afc12b" />

<img width="1758" height="677" alt="Screenshot 2026-06-21 164228" src="https://github.com/user-attachments/assets/79becf6b-da44-4d4a-ab56-aa5c2c8825fa" />

---

## Features

* Real-time CPU monitoring
* Real-time RAM monitoring
* Disk usage monitoring
* CPU frequency tracking
* Telemetry data collection
* Interactive Streamlit dashboard
* Machine learning risk classification
* Historical system analysis

---

## Technologies Used

* Python
* Pandas
* Psutil
* Streamlit
* Scikit-Learn
* Joblib

---

## Project Workflow

System Telemetry

↓

Data Collection

↓

CSV Storage

↓

Machine Learning Model

↓

Risk Prediction

↓

Dashboard Visualization

---

## Machine Learning Model

A Random Forest Classifier is trained using collected system telemetry data.

Risk Categories:

* LOW
* MEDIUM
* HIGH

The trained model predicts system risk based on:

* CPU Usage
* RAM Usage
* Disk Usage
* CPU Frequency
* Available RAM
* Available Disk Space

---

## Future Improvements

* Automatic anomaly detection
* Email alerts
* Multi-device monitoring
* Data center integration
* Cloud deployment
* Failure forecasting

---

## Author

Dhruv Sagar
B.Tech Information Technology
Alliance University
