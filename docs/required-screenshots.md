# Required Screenshots (Lab Submission)

Capture these **5 screenshots** for submission. Make sure the stack is running first:

```bash
docker compose up -d
```

On Windows, open the dashboard at: `http://localhost:9090`  
On the Linux lab server, use: `http://<server-ip>:9090`

Save images into [`screenshots/`](../screenshots/) using the filenames below. They are embedded in the project [README Screenshots section](../README.md#screenshots).

---

## Checklist

| # | Screenshot | Save as | What to show | Command / URL |
|---|------------|---------|--------------|---------------|
| 1 | Working dashboard | [`screenshots/01-dashboard.png`](../screenshots/01-dashboard.png) | Live metrics page in the browser (CPU, memory, disk, uptime updating) | Open `http://localhost:9090` (or `http://<server-ip>:9090`) |
| 2 | Compose status | [`screenshots/02-compose-ps.png`](../screenshots/02-compose-ps.png) | Both `dashboard` and `collector` containers running | `docker compose ps` |
| 3 | Docker images | [`screenshots/03-docker-images.png`](../screenshots/03-docker-images.png) | Your built images listed (e.g. `dashboard`, `collector`) | `docker images` |
| 4 | Docker network | [`screenshots/04-docker-network.png`](../screenshots/04-docker-network.png) | Network `monitoring-net` present | `docker network ls` |
| 5 | Docker volume | [`screenshots/05-docker-volume.png`](../screenshots/05-docker-volume.png) | Volume `monitoring-data` present | `docker volume ls` |

---

## How to capture each one

### 1. Working dashboard

1. Start the stack: `docker compose up -d`
2. Open the browser to `http://localhost:9090`
3. Wait until metrics load (not “Cannot reach Metrics Collector”)
4. Take a full-page or window screenshot of the live dashboard

### 2. `docker compose ps`

```bash
cd docker-monitoring-stack
docker compose ps
```

Screenshot the terminal output showing both services as **running**.

### 3. Docker images

```bash
docker images
```

Screenshot output that includes `dashboard` and `collector` (and usually `nginx` / `python` base images).

### 4. Docker network

```bash
docker network ls
```

Confirm `monitoring-net` is in the list. Optional detail screenshot:

```bash
docker network inspect monitoring-net
```

### 5. Docker volume

```bash
docker volume ls
```

Confirm `monitoring-data` is in the list. Optional detail screenshot:

```bash
docker volume inspect monitoring-data
```

---

## Tips

- Prefer clear terminal fonts and a readable browser window.
- On the Linux lab VM, older docs used `sudo docker ...` — on Windows Docker Desktop, `sudo` is usually not needed.
- Do **not** use `http://localhost:6000` in Chrome for the dashboard proof; use port **9090**.
- If the dashboard URL fails on Linux, check the current IP with `hostname -I` (see `troubleshooting-dhcp-ip-change.md`).
- Save files with the exact names in the checklist into [`screenshots/`](../screenshots/) so the [README](../README.md#screenshots) embeds stay valid.
