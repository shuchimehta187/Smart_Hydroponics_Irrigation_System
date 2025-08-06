# 🌿 Smart Hydroponics System using Digital Twin & IoT

An intelligent and sustainable hydroponic farming system that uses real-time sensor data, digital twin modeling, and AI-driven control to optimize plant growth.

## 📌 Project Overview

This project integrates sensors, actuators, a Raspberry Pi, and AWS Cloud (IoT Core, DynamoDB) to manage a smart hydroponic system. A digital twin continuously simulates plant growth and environmental conditions, enabling precision irrigation and nutrient delivery.

---

## 🧩 Key Modules

### 🔷 1. Sensor & Actuator Integration
- Collects real-time data from temperature, humidity, water level, wind, and air pressure sensors.
- Automates actions via relay-controlled fan and pump using Raspberry Pi.

### 🔷 2. Cloud Connectivity
- Uses **AWS IoT Core** to send sensor data securely to the cloud.
- Stores and visualizes data in **DynamoDB** for digital twin insights.

### 🔷 3. 🌐 Web Interface (IrrigoTwin)

A full-stack module developed using **React.js**, **Tailwind CSS**, **Node.js**, and **MongoDB** to visualize sensor data and weather conditions.

#### Features:
- **Geolocation-based Weather:** Integrated via OpenWeatherMap API.
- **Sensor Dashboard:** Displays humidity, temperature, wind, and air pressure.
- **About Page:** Explains hydroponics and system overview.
- **Policy Page:** Shows digital twin logic and sensor health checks.
- **Backend Server:** Built with Express.js and MongoDB (MongoDB Compass for GUI).

> 🖼️ UI Preview:
> - Home, Dashboard, and Data Panels
> - Live sensor data auto-refreshes every 3 minutes

> 🔧 Login/Signup functionality is planned for future implementation.

---

## 🛠 Tech Stack

- **Hardware:** Raspberry Pi, Sensors (DHT22, Water Level, Surface Temperature Controller, etc.), Relay Module, Analog-to-Digital Converter
- **Backend:** AWS IoT Core, MongoDB, Express.js
- **Frontend:** React.js, Tailwind CSS, OpenWeatherMap API
- **Modeling:** Digital Twin (Plant Growth Simulation)


