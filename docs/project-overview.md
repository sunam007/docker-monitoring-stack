# DevOps Monitoring App Project — Overview & Plan

## 👨‍🏫 Teacher's Role

I'll be your friendly DevOps teacher and will:
- ✅ Explain each step in simple, friendly language
- ✅ Guide you step-by-step through the entire project
- ✅ Wait for you to complete each step before moving to the next
- ✅ Help troubleshoot if you get stuck
- ✅ Be patient and make sure you understand *why* we're doing each thing

---

## 📚 Project Goal

Deploy a small monitoring application on a Linux server using Docker and Docker Compose. The app has two services:

- **Dashboard** — serves a metrics web page using NGINX
- **Metrics Collector** — exposes API endpoints to collect system metrics

---

## 🗺️ Tasks Overview

### Task 1 — 🐧 Linux Setup
- Create a project directory
- Create a simple `index.html` with a metrics dashboard placeholder
- Create a basic metrics API with a `/status` endpoint
- Check the Linux IP address, disk space, and file permissions

### Task 2 — 🐳 Docker Basics, Image Management, Networking & Storage
- Pull and manage the NGINX image
- Build your own dashboard and collector images
- Run both containers
- Map host port **9090 → dashboard port 80**
- Create a Docker network and connect both services
- Create a Docker volume and attach it to the appropriate container
- Verify the images, containers, network, and volume
- ⚠️ Services must communicate via **service/container names** (not hard-coded IPs)

### Task 3 — 📦 Dockerize the Application
- Create a Dockerfile for both services
  - Dashboard uses **NGINX**
  - Metrics collector runs on **port 6000**
- Both services run independently in containers
- The dashboard can communicate with the collector

**Expected flow:**
```
Browser → Dashboard :80 → Collector :6000
```
- Verify with Docker commands and `curl` requests

### Task 4 — 🎼 Docker Compose
- Create a `compose.yaml` to manage the complete application
- Must include:
  - Dashboard service
  - Collector service
  - Port mapping
  - Docker network
  - Docker volume
  - Appropriate restart policy
- Start with: `docker compose up -d`
- Verify with:
  - `docker compose ps`
  - `docker compose logs`

**Access URL:** `http://<server-ip>:9090`

### Task 5 — 🔍 Monitoring & Troubleshooting
Useful commands:
- `docker ps`
- `docker logs <container>`
- `docker inspect <container>`
- `docker stats`
- `docker network inspect <network>`
- `curl`
- `ss -tulnp`

**If the application does not work**, identify the issue, fix it, and briefly explain:
- What caused the problem?
- Which command helped you find it?
- How did you fix it?

### Bonus — ⭐ Restart Policy
- Add a restart policy to the services
- Explain what it does

---

## 📦 Project Structure

```
docker-project/
├── compose.yaml
├── dashboard/
│   ├── Dockerfile
│   └── index.html
└── collector/
    ├── Dockerfile
    └── application files
```

---

## 🖼️ Required Screenshots

1. Screenshot of the working dashboard
2. Screenshot of `docker compose ps`
3. Screenshot showing Docker images
4. Screenshot showing the Docker network
5. Screenshot showing the Docker volume

---

## 🚀 How We'll Work Together

For each step, I'll:
1. Tell you **what to do** and **why**
2. Give you the **exact command** to run
3. Wait for you to say **"done"** or paste the output
4. Then move to the **next step**