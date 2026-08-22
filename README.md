# 🐳 Docker Monitoring Stack

> A DevOps monitoring application using Docker, Docker Compose, NGINX, and Flask.

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/NGINX-009639?style=flat&logo=nginx&logoColor=white)](https://nginx.org/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A multi-container monitoring application that collects and displays real-time Linux system metrics (CPU, memory, disk, uptime) through a web-based dashboard.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Docker Commands](#-docker-commands)
- [Screenshots](#-screenshots)
- [Key Features](#-key-features)
- [Troubleshooting](#-troubleshooting)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

This project demonstrates a complete **DevOps workflow** for deploying a containerized monitoring application on a Linux server. It covers:

- 🐧 Linux environment setup
- 🐳 Docker containerization
- 🌐 Docker networking
- 💾 Persistent storage with Docker volumes
- 🎼 Multi-container orchestration with Docker Compose
- 🔍 Monitoring and debugging techniques

---

## 🏗️ Architecture

```
User/Browser
     │
     ▼
   :9090
┌──────────────┐
│   Dashboard  │
│    NGINX     │
│     :80      │
└──────┬───────┘
       │
   Docker Network
       │
┌──────▼───────┐
│   Metrics    │
│  Collector   │
│     :6000    │
└──────┬───────┘
       │
       ▼
  Docker Volume
```

**Flow:** Browser → Dashboard (NGINX :80) → Metrics Collector (Flask :6000) → Docker Volume

---

## 🛠️ Tech Stack

| Component | Technology | Port |
|-----------|------------|------|
| **Frontend Dashboard** | NGINX (Alpine) | 80 → mapped to 9090 |
| **Metrics Collector** | Python 3.11 + Flask | 6000 |
| **System Metrics** | psutil library | - |
| **Containerization** | Docker + Docker Compose | - |
| **Web Server** | Gunicorn-ready Flask app | - |

---

## 📁 Project Structure

```
docker-monitoring-stack/
├── compose.yaml              # Docker Compose configuration
├── README.md                 # This file
├── dashboard/
│   ├── Dockerfile            # NGINX image with custom HTML
│   └── index.html            # Metrics dashboard UI
└── collector/
    ├── Dockerfile            # Python + Flask image
    ├── app.py                # Flask API with /status endpoint
    └── requirements.txt      # Python dependencies
```

---

## ✅ Prerequisites

- Linux server (Ubuntu 20.04+ recommended)
- Docker Engine 20.10+
- Docker Compose v2.0+
- Python 3.10+ (only for local testing)
- Ports `9090` and `6000` available

### Check your environment:
```bash
docker --version
docker compose version
hostname -I    # Get your server IP
```

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/sunam007/docker-monitoring-stack.git
cd docker-monitoring-stack
```

### 2. Build and start the application
```bash
docker compose up -d
```

### 3. Verify the deployment
```bash
docker compose ps
docker compose logs
```

### 4. Access the dashboard
Open your browser and visit:
```
http://<server-ip>:9090
```

---

## 💻 Usage

### Start the application
```bash
docker compose up -d
```

### Stop the application
```bash
docker compose down
```

### View logs
```bash
docker compose logs            # All services
docker compose logs dashboard  # Specific service
docker compose logs -f         # Follow logs in real-time
```

### Restart a service
```bash
docker compose restart dashboard
docker compose restart collector
```

### Rebuild after code changes
```bash
docker compose up -d --build
```

---

## 📡 API Endpoints

The Metrics Collector exposes the following endpoints:

### `GET /`
Returns basic service information.
```bash
curl http://localhost:6000/
```
**Response:**
```json
{
  "service": "Metrics Collector",
  "status": "running",
  "endpoint": "/status"
}
```

### `GET /status`
Returns real-time system metrics.
```bash
curl http://localhost:6000/status
```
**Response:**
```json
{
  "hostname": "your-server",
  "platform": "Linux",
  "uptime": "5:23:45",
  "cpu": {
    "percent": 17.0,
    "cores": 4
  },
  "memory": {
    "total_gb": 7.64,
    "used_gb": 4.04,
    "percent": 61.5
  },
  "disk": {
    "total_gb": 93.31,
    "used_gb": 46.0,
    "percent": 52.0
  }
}
```

---

## 🐳 Docker Commands

### Images
```bash
docker images                    # List all images
docker pull nginx                # Pull NGINX image
docker build -t dashboard .      # Build dashboard image
docker build -t collector .      # Build collector image
```

### Containers
```bash
docker ps                        # Running containers
docker ps -a                     # All containers
docker logs <container>          # View logs
docker inspect <container>       # Detailed info
docker stats                     # Live CPU/memory usage
```

### Networks
```bash
docker network ls                              # List networks
docker network create monitoring-net          # Create network
docker network inspect monitoring-net          # Network details
```

### Volumes
```bash
docker volume ls                               # List volumes
docker volume create monitoring-data           # Create volume
docker volume inspect monitoring-data          # Volume details
```

---

## 📸 Screenshots

> Add screenshots here after running the application

- 🖼️ Dashboard (`http://<server-ip>:9090`)
- 🖼️ `docker compose ps` output
- 🖼️ Docker images (`docker images`)
- 🖼️ Docker network (`docker network ls`)
- 🖼️ Docker volume (`docker volume ls`)

---

## ⭐ Key Features

- ✅ **Multi-container architecture** — separate services for frontend and backend
- ✅ **Custom Docker network** — services communicate via container names (no hard-coded IPs)
- ✅ **Persistent storage** — Docker volume survives container restarts
- ✅ **Restart policies** — `restart: unless-stopped` for high availability
- ✅ **Port mapping** — host `9090` → container `80`
- ✅ **Real-time metrics** — CPU, memory, disk, uptime updated live
- ✅ **JSON API** — clean REST API for system metrics
- ✅ **Health monitoring** — verify with `docker stats` and logs

---

## 🔍 Troubleshooting

If the application doesn't work, use these steps:

### 1. Check if containers are running
```bash
docker compose ps
```

### 2. View error logs
```bash
docker compose logs
docker logs <container-name>
```

### 3. Inspect network connectivity
```bash
docker network inspect monitoring-net
docker exec -it dashboard curl http://collector:6000/status
```

### 4. Check listening ports
```bash
ss -tulnp | grep -E '9090|6000'
```

### 5. Rebuild from scratch
```bash
docker compose down
docker compose up -d --build
```

---

## 📚 What I Learned

This project covers essential DevOps skills:

- 🐧 Linux system administration (IP, disk, permissions)
- 🐳 Docker fundamentals (images, containers, Dockerfiles)
- 🌐 Docker networking (bridge networks, DNS resolution)
- 💾 Persistent storage (Docker volumes)
- 🎼 Container orchestration (Docker Compose)
- 🔍 Debugging and monitoring (`docker logs`, `docker stats`, `docker inspect`)
- 📝 API design (Flask + JSON endpoints)
- 🔄 Restart policies and high availability

---

## 👨‍💻 Author

**sunam007**
- GitHub: [@sunam007](https://github.com/sunam007)
- Email: asaduzzaman.sunam@gmail.com

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Built as part of a DevOps learning lab
- Uses [psutil](https://github.com/giampaolo/psutil) for system metrics
- Powered by [Docker](https://www.docker.com/) and [NGINX](https://nginx.org/)

---

**⭐ If you find this project useful, please give it a star on GitHub!**