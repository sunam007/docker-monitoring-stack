# Troubleshooting: ERR_UNSAFE_PORT Issue

## 🎯 TL;DR

The dashboard showed **"Cannot reach Metrics Collector"** because **Chrome blocks port 6000** for security. We fixed it by making **NGINX act as a reverse proxy** — now the browser only talks to port 9090, and NGINX forwards API requests to the collector internally.

---

## ❌ Why It Wasn't Working

### The Three Failed Attempts

#### 1️⃣ First Issue: CORS (Cross-Origin Resource Sharing)
**Symptom:** Browser blocked the API call from `http://192.168.1.8:9090` to `http://192.168.1.8:6000` because they have **different ports** = different origin.

**Fix:** Added `flask-cors` to the collector and enabled CORS in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

#### 2️⃣ Second Issue: Docker Build Cache
**Symptom:** Even after adding CORS, the issue persisted because Docker used **cached layers** instead of rebuilding.

**Fix:** Force rebuild with `--no-cache` flag (later resolved when adding the proxy).

#### 3️⃣ Third Issue (THE REAL ONE): ERR_UNSAFE_PORT 🎯
**Symptom:** Browser Console showed:
```
GET http://192.168.1.8:6000/status net::ERR_UNSAFE_PORT
```

**Root Cause:** **Chrome blocks port 6000** because it's on the list of "unsafe ports" (port 6000 was historically used by X11, and browsers block it for security).

---

## ✅ The Fix: NGINX Reverse Proxy

### What We Changed

#### 1. Created `dashboard/nginx.conf`
A custom NGINX configuration that:
- Serves the dashboard HTML on `/`
- **Proxies** `/api/*` requests to `http://collector:6000/*`

```nginx
location /api/ {
    proxy_pass http://collector:6000/;
}
```

#### 2. Updated `dashboard/Dockerfile`
- Removed the default NGINX config
- Copied our custom `nginx.conf` into the container

```dockerfile
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
```

#### 3. Updated `dashboard/index.html`
Changed the API URL from direct access → through the proxy:
```javascript
// Before (broken):
const API_URL = 'http://' + window.location.hostname + ':6000/status';

// After (works):
const API_URL = '/api/status';
```

---

## 🔄 How It Works Now (The New Flow)

```
Browser → http://192.168.1.8:9090/api/status
            ↓
         NGINX (in dashboard container)
            ↓
         http://collector:6000/status (inside Docker network)
            ↓
         Flask API returns JSON
            ↓
         Browser displays live metrics! 📊
```

**Key benefit:** The browser **never** talks to port 6000 directly — only to port 9090. NGINX handles the backend communication internally using Docker's DNS.

---

## 🎓 Why This Is The Professional Solution

| Approach | Pros | Cons |
|----------|------|------|
| ❌ Browser → Port 6000 directly | Simple | Blocked by Chrome |
| ❌ Change collector port | Easy fix | Breaks task requirement (port 6000) |
| ❌ Restart Chrome with flags | Quick | Only works locally, not for users |
| ✅ **NGINX reverse proxy** | Production-grade, works for all users, hides backend | Slightly more setup |

This is exactly how **production systems** (like API gateways, CDNs) work — the public-facing service proxies requests to internal services. 🏆

---

## 📁 Files Changed

- ✏️ `dashboard/nginx.conf` (created)
- ✏️ `dashboard/Dockerfile` (updated)
- ✏️ `dashboard/index.html` (updated)
- ✏️ `collector/app.py` (CORS added)
- ✏️ `collector/requirements.txt` (flask-cors added)

---

## 🔍 Commands That Helped Diagnose

```bash
# Found the actual error in browser console (F12 → Console)
# Showed: net::ERR_UNSAFE_PORT

# This was the "command" — F12 Developer Tools!
```
