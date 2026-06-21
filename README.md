# AI-Based Predictive Maintenance System

## Overview

An AI-powered predictive maintenance system designed for personal computers and data centers.

The system collects live hardware telemetry, stores historical performance data, visualizes system health through a dashboard, and uses machine learning to estimate system risk levels.

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
