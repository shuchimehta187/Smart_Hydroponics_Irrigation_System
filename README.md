# 🌱 Smart Hydroponics System using Digital Twin Technology

A full-stack smart irrigation and hydroponics system that leverages IoT sensors, a Digital Twin, real-time weather data, and automation to create a more efficient and sustainable farming method.

## 🚀 Project Overview

This project focuses on automating hydroponic farming using sensors, a digital twin model, and a web interface. The goal is to collect real-time environmental data, simulate plant conditions, and trigger automated actions through connected actuators — all visualized via a dashboard.



## 🧩 Features

### 🌐 Frontend (AgriTwin Web Interface)
- Built using **React.js**, **Tailwind CSS**, and **OpenWeatherMap API**
- Geolocation to fetch current weather conditions
- Real-time dashboard for sensor data (temperature, humidity, wind, air pressure)
- Modular pages:
  - **Home:** Displays current weather + sensor data
  - **About Us:** Explains hydroponics and automation process
  - **Policy (Twin logic):** Verifies sensor status and recommends corrective action
  - **Login/Sign up:** (Under development)

### 🛠 Backend
- Built using **Node.js** + **Express.js**
- Stores and serves data using **MongoDB**
- Backend auto-fetches data every 3 minutes for seamless frontend updates
- MongoDB Compass is used for database visualization





## 🧱 Tech Stack

| Component        | Tech Used                  |
|------------------|----------------------------|
| Frontend         | React.js, Tailwind CSS     |
| Backend          | Node.js, Express.js        |
| Database         | MongoDB, MongoDB Compass   |
| Weather API      | OpenWeatherMap             |
| IoT Integration  | Raspberry Pi + Sensors     |
| Automation       | Relay module (Fan + Pump)  |



