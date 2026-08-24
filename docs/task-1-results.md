# Task 1 — Linux Setup Results

## TL;DR

Task 1 complete ✅ — Created the project structure, built a working metrics API, and verified the Linux environment. The Metrics Collector (`app.py`) successfully runs locally and returns real-time system metrics (CPU, memory, disk, uptime) as JSON on port 6000.

---

## 📊 Linux Environment Summary (Example Output)

### 🌐 IP Address — `hostname -I`
```
192.168.1.8 172.16.0.2 2606:4700:110:8b08:2d09:cdd0:8e9:8a9c
```
**Main local IP:** `192.168.1.8`

This will be used later to access the dashboard at: **`http://192.168.1.8:9090`**

### 💾 Disk Space — `df -h`
```
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           783M  2.0M  781M   1% /run
/dev/sda1        94G   47G   43G  52% /
tmpfs           3.9G  1.1M  3.9G   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
/dev/sdb2        95M   38M   58M  40% /boot/efi
tmpfs           783M   42M  741M   6% /run/user/1000
/dev/sda2       837G  458G  380G  55% /media/osborne-junious/Data
```
**Disk OK** — Main partition `/` has 43 GB free (52% used). Docker images will fit comfortably.

### 📁 File Permissions — `ls -la .../docker-project`
```
total 16
drwxrwxr-x 4 osborne-junious osborne-junious 4096 Aug 22 23:14 .
drwxrwxr-x 4 osborne-junious osborne-junious 4096 Aug 22 23:11 ..
drwxrwxr-x 2 osborne-junious osborne-junious 4096 Aug 22 23:42 collector
drwxrwxr-x 2 osborne-junious osborne-junious 4096 Aug 22 23:23 dashboard
```
**Permissions OK** — Owner is `osborne-junious`, permissions are `rwxr-xr-x`. Docker can read these folders.

---

## 🧪 Metrics Collector — Local Test Output

### Command run:
```bash
curl http://localhost:6000/status
```

### Response received (real JSON):
```json
{
  "cpu": {"cores": 4, "percent": 17.0},
  "disk": {"percent": 52.0, "total_gb": 93.31, "used_gb": 46.0},
  "hostname": "osborne-pc",
  "memory": {"percent": 61.5, "total_gb": 7.64, "used_gb": 4.04},
  "platform": "Linux",
  "uptime": "2:57:46"
}
```
**Status:** ✅ API working perfectly — returning real system metrics.

---

## 📁 Project Structure Created
```
docker-project/
├── dashboard/
│   └── index.html
└── collector/
    ├── app.py
    └── requirements.txt
```

---

## ✅ Task 1 Checklist
- [x] Created `docker-project/` directory
- [x] Created `dashboard/` and `collector/` subfolders
- [x] Created `index.html` (dashboard placeholder)
- [x] Created `app.py` (Metrics Collector with `/status` endpoint)
- [x] Created `requirements.txt` (Flask + psutil)
- [x] Installed dependencies and tested locally
- [x] Verified IP, disk space, and file permissions

---

## 🚀 Next: Task 2 — Docker Basics
Move on to creating Dockerfiles, building images, and running containers.
