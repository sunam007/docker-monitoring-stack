# DevOps Monitoring App — Progress Tracker

Welcome! This file tracks your progress through the entire DevOps project.
Each step has a checkbox `[ ]` you can mark as you complete it.

---

## Progress Summary

- [ ] Task 1 — Linux Setup
- [ ] Task 2 — Docker Basics, Image Management, Networking & Storage
- [ ] Task 3 — Dockerize the Application
- [ ] Task 4 — Docker Compose
- [ ] Task 5 — Monitoring & Troubleshooting
- [ ] Bonus — Restart Policy
- [x] Final — Screenshots & Submission

---

## Task 1 — 🐧 Linux Setup

### Step 1.1: Create project directory
- [ ] Navigate to your working directory: `cd /home/osborne-junious/poridhi-lab/mil-one-project`
- [ ] Create the project folder: `mkdir -p docker-project`
- [ ] Verify it exists: `ls -la docker-project`

### Step 1.2: Create subfolders for services
- [ ] Create dashboard folder: `mkdir -p docker-project/dashboard`
- [ ] Create collector folder: `mkdir -p docker-project/collector`
- [ ] Verify both exist: `ls -la docker-project`

### Step 1.3: Create `index.html` for the dashboard
- [ ] Navigate to dashboard folder: `cd docker-project/dashboard`
- [ ] Create `index.html` with a metrics dashboard placeholder (HTML page with a heading + placeholders for CPU, memory, disk)
- [ ] Verify: `cat index.html`

### Step 1.4: Create the metrics API (`/status` endpoint)
- [ ] Navigate to collector folder: `cd ../collector`
- [ ] Decide on language (recommended: **Python + Flask**)
- [ ] Create `app.py` with a `/status` endpoint that returns system metrics as JSON
- [ ] Verify the file exists: `ls -la`

### Step 1.5: Install Python dependencies (locally for testing)
- [ ] Install Flask: `pip install flask psutil` (or `pip3 install ...`)
- [ ] Run the app locally: `python3 app.py`
- [ ] Test with curl: `curl http://localhost:6000/status` (run in another terminal)
- [ ] Stop the local server (Ctrl+C) — we'll run it in Docker later

### Step 1.6: Check Linux environment info
- [ ] Check IP address: `hostname -I` or `ip addr`
- [ ] Check disk space: `df -h`
- [ ] Check file permissions: `ls -la`

✅ **Task 1 complete when:** All checkboxes above are ticked.

---

## Task 2 — 🐳 Docker Basics, Image Management, Networking & Storage

### Step 2.1: Verify Docker is installed
- [ ] Run: `docker --version`
- [ ] Run: `docker info` (should not give errors)

### Step 2.2: Pull the official NGINX image
- [ ] Run: `docker pull nginx`
- [ ] Verify: `docker images`

### Step 2.3: Create Dockerfile for the Dashboard (NGINX)
- [ ] Navigate: `cd docker-project/dashboard`
- [ ] Create `Dockerfile`:
  - Use `FROM nginx:alpine`
  - Copy `index.html` into `/usr/share/nginx/html/`
- [ ] Build the image: `docker build -t dashboard:latest .`
- [ ] Verify: `docker images | grep dashboard`

### Step 2.4: Create Dockerfile for the Metrics Collector
- [ ] Navigate: `cd ../collector`
- [ ] Create `Dockerfile`:
  - Use `FROM python:3.11-slim`
  - Install `flask` and `psutil`
  - Copy `app.py`
  - Expose port `6000`
  - Run with `CMD ["python3", "app.py"]`
- [ ] Create `requirements.txt` (lists: `flask`, `psutil`)
- [ ] Build the image: `docker build -t collector:latest .`
- [ ] Verify: `docker images | grep collector`

### Step 2.5: Create a Docker network
- [ ] Run: `docker network create monitoring-net`
- [ ] Verify: `docker network ls`

### Step 2.6: Create a Docker volume
- [ ] Run: `docker volume create monitoring-data`
- [ ] Verify: `docker volume ls`

### Step 2.7: Run the Collector container
- [ ] Run: `docker run -d --name collector --network monitoring-net -v monitoring-data:/data -p 6000:6000 collector:latest`
- [ ] Verify it's running: `docker ps`
- [ ] Test: `curl http://localhost:6000/status`

### Step 2.8: Run the Dashboard container
- [ ] Run: `docker run -d --name dashboard --network monitoring-net -p 9090:80 dashboard:latest`
- [ ] Verify it's running: `docker ps`
- [ ] Test in browser: `http://<server-ip>:9090`

### Step 2.9: Verify everything
- [ ] Verify images: `docker images`
- [ ] Verify containers: `docker ps`
- [ ] Verify network: `docker network inspect monitoring-net`
- [ ] Verify volume: `docker volume inspect monitoring-data`

✅ **Task 2 complete when:** Both containers are running and accessible.

---

## Task 3 — 📦 Dockerize the Application

### Step 3.1: Finalize Dashboard Dockerfile
- [ ] Dashboard uses **NGINX** (port 80 inside container)
- [ ] The `index.html` is served from `/usr/share/nginx/html/`

### Step 3.2: Finalize Collector Dockerfile
- [ ] Collector runs on **port 6000**
- [ ] `app.py` listens on `0.0.0.0` (so it's reachable from outside)
- [ ] Has a `/status` endpoint
- [ ] Uses Python libraries like `psutil` for metrics

### Step 3.3: Confirm services can communicate
- [ ] Both containers attached to same network
- [ ] Dashboard can reach collector via the name **`collector`** (not IP!)
- [ ] Test: `docker exec -it dashboard curl http://collector:6000/status`

### Step 3.4: Verify with curl
- [ ] From host: `curl http://localhost:6000/status`
- [ ] From host: `curl http://localhost:9090/` (returns HTML)
- [ ] From inside dashboard container: `curl http://collector:6000/status`

✅ **Task 3 complete when:** Both services run independently and communicate via service name.

---

## Task 4 — 🎼 Docker Compose

### Step 4.1: Create `compose.yaml`
- [ ] Create the file: `docker-project/compose.yaml`
- [ ] Add both services: `dashboard` and `collector`
- [ ] Define port mappings
- [ ] Define network (or use the default one)
- [ ] Define volume
- [ ] Add restart policy (e.g., `restart: always` or `unless-stopped`)

### Step 4.2: Clean up old containers (if any)
- [ ] Stop old containers: `docker stop dashboard collector`
- [ ] Remove them: `docker rm dashboard collector`
- [ ] (We'll use Compose to run them now)

### Step 4.3: Start the application with Compose
- [ ] Navigate: `cd docker-project`
- [ ] Run: `docker compose up -d`
- [ ] Verify: `docker compose ps`
- [ ] Check logs: `docker compose logs`

### Step 4.4: Test the app
- [ ] Open browser → `http://<server-ip>:9090`
- [ ] Confirm metrics dashboard loads

✅ **Task 4 complete when:** App runs from `docker compose up -d` and is accessible.

---

## Task 5 — 🔍 Monitoring & Troubleshooting

### Step 5.1: Run monitoring commands
- [ ] `docker ps` — list running containers
- [ ] `docker logs <container>` — view logs
- [ ] `docker inspect <container>` — detailed info
- [ ] `docker stats` — live resource usage
- [ ] `docker network inspect <network>` — network details
- [ ] `curl http://localhost:6000/status` — test the API
- [ ] `ss -tulnp` — check listening ports

### Step 5.2: Troubleshoot any issues
If something breaks, document it:
- 🔍 **What caused the problem?** → _______________
- 🛠️ **Which command found it?** → _______________
- ✅ **How did you fix it?** → _______________

✅ **Task 5 complete when:** You can confidently explain the app's state using Docker commands.

---

## Bonus — ⭐ Restart Policy

### Step: Add & explain restart policy
- [ ] In `compose.yaml`, add restart policy (e.g., `restart: unless-stopped`)
- [ ] **Explain what it does:** The restart policy automatically restarts containers if they crash or if the server reboots. `unless-stopped` means it restarts unless you manually stop it.

✅ **Bonus complete when:** Restart policy is added and explained.

---

## Final — 📦 Screenshots & Submission

### Required Screenshots
Saved under [`screenshots/`](../screenshots/) and embedded in [README.md](../README.md#screenshots). Capture guide: [`docs/required-screenshots.md`](required-screenshots.md).

- [x] 🖼️ Screenshot of the working dashboard → `screenshots/01-dashboard.png`
- [x] 🖼️ Screenshot of `docker compose ps` → `screenshots/02-compose-ps.png`
- [x] 🖼️ Screenshot showing Docker images → `screenshots/03-docker-images.png`
- [x] 🖼️ Screenshot showing the Docker network → `screenshots/04-docker-network.png`
- [x] 🖼️ Screenshot showing the Docker volume → `screenshots/05-docker-volume.png`

### Final Folder Structure
Verify your project looks like this:
```
docker-project/
├── compose.yaml
├── README.md
├── screenshots/
│   ├── 01-dashboard.png
│   ├── 02-compose-ps.png
│   ├── 03-docker-images.png
│   ├── 04-docker-network.png
│   └── 05-docker-volume.png
├── dashboard/
│   ├── Dockerfile
│   └── index.html
└── collector/
    ├── Dockerfile
    └── application files (app.py, requirements.txt)
```

✅ **Project complete when:** All screenshots are saved AND folder structure matches.

---

## 🎉 Completion Status

Count your ticked boxes:
- **Total steps:** ~50+
- **You are done when:** All top-level task checkboxes (Task 1 → Final) are ✅

Good luck! 🚀
