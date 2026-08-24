# 🚀 Session Resume Guide — Docker Monitoring Stack Project

> **Purpose:** This document provides complete context for ANY AI agent (or human) to seamlessly continue this project from where it left off.

---

## 📍 Current Status: STOPPED AT TASK 4

**Last completed task:** Task 2 (Docker Basics + Dynamic Dashboard)
**Next task to do:** Task 3 — Dockerize (formalize), then Task 4 — Docker Compose

---

## 🎯 Project Overview

| Item | Value |
|------|-------|
| **Project Name** | `docker-monitoring-stack` |
| **GitHub Repo** | https://github.com/sunam007/docker-monitoring-stack |
| **Description** | A DevOps monitoring application using Docker, Docker Compose, NGINX, and Flask |
| **Working Directory** | `/home/osborne-junious/poridhi-lab/mil-one-project` |
| **Project Folder** | `/home/osborne-junious/poridhi-lab/mil-one-project/docker-project` |
| **Server IP** | `192.168.1.9` (was `192.168.1.8` — DHCP changed it!) |
| **Dashboard URL** | `http://192.168.1.9:9090` |
| **Collector Port** | `6000` (internal), mapped to host `6000` |
| **Dashboard Port** | Host `9090` → Container `80` |

---

## ✅ Completed Tasks

### Task 1 — Linux Setup ✅
- Created `docker-project/` with subfolders `dashboard/` and `collector/`
- Created `dashboard/index.html` (dynamic with JavaScript)
- Created `collector/app.py` (Flask + psutil with `/status` endpoint)
- Created `collector/requirements.txt` (flask, flask-cors, psutil)
- Verified IP: `192.168.1.8`, disk space OK, permissions OK
- Tested API locally with curl — got real JSON metrics

### Task 2 — Docker Basics, Image Management, Networking & Storage ✅
- ✅ Docker installed (version 29.1.3)
- ✅ Pulled NGINX image
- ✅ Built custom `dashboard:latest` image (with NGINX + custom HTML + nginx.conf)
- ✅ Built custom `collector:latest` image (Python + Flask + psutil + flask-cors)
- ✅ Created Docker network: `monitoring-net` (bridge driver)
- ✅ Created Docker volume: `monitoring-data`
- ✅ Both containers running:
  - `dashboard` — port `9090 → 80`
  - `collector` — port `6000 → 6000`, mounted volume at `/data`
- ✅ Cross-container communication verified (dashboard → collector via name)
- ✅ Live dynamic dashboard working with real metrics!

### Bonus: Dynamic Dashboard ✅
- HTML updated with JavaScript that calls `/api/status` every 2 seconds
- Progress bars, status indicator, hostname display, last updated timestamp
- **Uses NGINX reverse proxy** (see troubleshooting note below)

---

## ⚠️ IMPORTANT: Troubleshooting Context

**The dashboard had an issue that was fixed!** Read `docs/troubleshooting-unsafe-port.md` for full details.

### The Problem
Browser Console showed: `net::ERR_UNSAFE_PORT` when fetching `http://192.168.1.8:6000/status`

**Chrome blocks port 6000** as it's on the "unsafe ports" list (port 6000 was historically used by X11).

### The Fix: NGINX Reverse Proxy
1. **`dashboard/nginx.conf`** — Added `location /api/ { proxy_pass http://collector:6000/; }`
2. **`dashboard/Dockerfile`** — Removed default NGINX config, copies our custom one
3. **`dashboard/index.html`** — Changed API URL from `:6000/status` to `/api/status`

**How it works now:**
```
Browser → http://192.168.1.8:9090/api/status
   ↓
NGINX (in dashboard container)
   ↓
http://collector:6000/status (inside Docker network)
   ↓
Flask API returns JSON → Browser displays metrics
```

---

## 📁 Current Project Structure

```
/home/osborne-junious/poridhi-lab/mil-one-project/
├── docs/
│   ├── project-overview.md          ← Full project description
│   ├── steps.md                      ← Progress tracker with checkboxes
│   ├── task-1-results.md             ← Task 1 verification results
│   ├── troubleshooting-unsafe-port.md  ← ERR_UNSAFE_PORT fix
│   └── SESSION-RESUME.md             ← THIS FILE
└── docker-project/
    ├── README.md                     ← Professional project README
    ├── .git/                         ← Git repo initialized
    ├── dashboard/
    │   ├── Dockerfile                ← NGINX image with custom config
    │   ├── nginx.conf                ← Reverse proxy config
    │   └── index.html                ← Dynamic dashboard with JavaScript
    └── collector/
        ├── Dockerfile                ← Python + Flask image
        ├── app.py                    ← Flask API with /status + / + CORS
        └── requirements.txt          ← flask, flask-cors, psutil
```

---

## 🐳 Currently Running Containers

| Container | Image | Port | Network | Volume | Status |
|-----------|-------|------|---------|--------|--------|
| `dashboard` | `dashboard:latest` | `9090 → 80` | `monitoring-net` | - | ✅ Running |
| `collector` | `collector:latest` | `6000 → 6000` | `monitoring-net` | `monitoring-data:/data` | ✅ Running |

### Docker Resources
- **Network:** `monitoring-net` (bridge driver)
- **Volume:** `monitoring-data` (mounted to collector at `/data`)

### To check current state, run:
```bash
sudo docker ps
sudo docker images
sudo docker network ls
sudo docker volume ls
```

---

## 📋 Task 3 — Dockerize the Application (NEXT)

**Status:** Mostly done! The Dockerfiles exist and the app is containerized.

### Task 3 Requirements (from instructions):
- ✅ Dockerfile for both services (DONE)
- ✅ Dashboard uses NGINX (DONE)
- ✅ Metrics collector runs on port 6000 (DONE)
- ✅ Both services run independently in containers (DONE)
- ✅ Dashboard can communicate with collector (DONE via NGINX proxy)
- ✅ Verify with Docker commands and curl (DONE)

**Action:** Mark Task 3 as complete. Verify curl commands still work:

```bash
# From host
curl http://localhost:6000/status

# From dashboard container (uses service name, not IP)
sudo docker exec -it dashboard wget -qO- http://collector:6000/status

# Browser test
# Visit http://192.168.1.8:9090 (should show live metrics)
```

---

## 📋 Task 4 — Docker Compose (PRIMARY NEXT TASK)

### Task 4 Requirements (from instructions):
Create a `compose.yaml` that:
- Defines **dashboard service**
- Defines **collector service**
- Includes **port mapping**
- Includes **Docker network**
- Includes **Docker volume**
- Has appropriate **restart policy**

### Steps to do:
1. **Stop current containers** (so Compose can manage them):
   ```bash
   sudo docker stop dashboard collector
   sudo docker rm dashboard collector
   ```

2. **Create `compose.yaml`** in `/home/osborne-junious/poridhi-lab/mil-one-project/docker-project/`

3. **The compose.yaml should include:**
   - Build context for both services (using their Dockerfiles)
   - Port mappings (9090:80 for dashboard, 6000:6000 for collector)
   - Network definition (`monitoring-net`)
   - Volume definition (`monitoring-data`)
   - Restart policy (`unless-stopped` is recommended for bonus)

4. **Run:**
   ```bash
   sudo docker compose up -d
   ```

5. **Verify:**
   ```bash
   sudo docker compose ps
   sudo docker compose logs
   ```

6. **Test in browser:** `http://192.168.1.8:9090`

---

## ⭐ BONUS Task: Restart Policy

Already mentioned in Task 4. Add this to each service in `compose.yaml`:
```yaml
restart: unless-stopped
```

**What it does:** Automatically restarts containers if they crash or if the Docker daemon/server reboots. Containers won't restart only if you manually stop them.

---

## 📋 Task 5 — Monitoring & Troubleshooting ✅ COMPLETE

All monitoring commands verified working (docker ps, docker logs, docker inspect, docker stats, docker network inspect, curl, ss -tulnp).

## 📋 Remaining tasks for tomorrow:

### Commands to demonstrate:
```bash
sudo docker ps
sudo docker logs <container>
sudo docker inspect <container>
sudo docker stats
sudo docker network inspect monitoring-net
curl http://localhost:6000/status
ss -tulnp
```

### Troubleshooting template:
If something breaks, document:
- 🔍 What caused the problem?
- 🛠️ Which command helped find it?
- ✅ How did you fix it?

---

## 📸 Required Screenshots (for submission)

1. 🖼️ **Working dashboard** at `http://192.168.1.8:9090` (live metrics)
2. 🖼️ **`docker compose ps`** output (after Task 4)
3. 🖼️ **Docker images** (`sudo docker images`)
4. 🖼️ **Docker network** (`sudo docker network ls` or inspect)
5. 🖼️ **Docker volume** (`sudo docker volume ls` or inspect)

---

## 🔑 Key Gotchas to Remember

1. **Always use `sudo` for Docker commands** in new terminal sessions (unless you've run `newgrp docker`)
2. **Don't use line breaks (`\`) in docker run** — use single-line commands or proper multi-line scripts
3. **Browser blocks port 6000** — always go through the NGINX proxy at `/api/status`
4. **Use service names, not IPs** — Docker's built-in DNS resolves container names
5. **The collector image needs `--no-cache` rebuild** if you change requirements (sometimes)

---

## 📝 Git Status (Last Known)

**Commits pushed to GitHub:**
```
525d33c Add Dockerfiles, build images, run containers with network & volume
fa33f4a readme.md file added
0d36c17 project initialized
```

**Repo:** https://github.com/sunam007/docker-monitoring-stack
**Credentials:** Stored (PAT saved, no re-prompt needed)

---

## 🚀 Quick Start Commands (When Resuming)

### Check everything is still running:
```bash
sudo docker ps
curl http://localhost:6000/status
```

### View dashboard:
Open browser to: `http://192.168.1.8:9090`

### Start working on Task 4:
```bash
cd /home/osborne-junious/poridhi-lab/mil-one-project/docker-project
```

---

## 📚 Files to Reference

| File | What It Contains |
|------|------------------|
| `docs/project-overview.md` | Full task list and requirements |
| `docs/steps.md` | Progress tracker with checkboxes |
| `docs/task-1-results.md` | Task 1 verification results |
| `docs/troubleshooting-unsafe-port.md` | ERR_UNSAFE_PORT fix details |
| `docker-project/README.md` | Project README for GitHub |
| `docker-project/dashboard/Dockerfile` | Dashboard image definition |
| `docker-project/dashboard/nginx.conf` | Reverse proxy config |
| `docker-project/dashboard/index.html` | Dynamic dashboard UI |
| `docker-project/collector/Dockerfile` | Collector image definition |
| `docker-project/collector/app.py` | Flask API code |
| `docker-project/collector/requirements.txt` | Python dependencies |

---

## 🎯 The Mission When You Resume

> **You are a friendly DevOps teacher. Continue from Task 4 — Docker Compose.**
>
> Help them:
> 1. Stop existing containers
> 2. Create `compose.yaml` with all required services
> 3. Add restart policy (bonus)
> 4. Run `docker compose up -d`
> 5. Verify with `docker compose ps` and `docker compose logs`
> 6. Test in browser
> 7. Then move to Task 5 (monitoring/troubleshooting)
> 8. Capture all required screenshots
> 9. Commit and push to GitHub

**Be friendly, step-by-step, and wait for the user to complete each step before moving on.**

---

## ⚡ Last Verified Working State

- ✅ Dashboard live at `http://192.168.1.8:9090` showing real metrics
- ✅ CPU: ~26.6%
- ✅ Memory: ~41.0%
- ✅ Disk: ~52.5%
- ✅ Uptime: 4:34:38
- ✅ Both containers running, network connected, volume mounted
- ✅ NGINX reverse proxy working correctly
- ✅ CORS enabled on Flask

**Everything is in a working state. Just stop containers, create compose.yaml, and run docker compose up -d!**