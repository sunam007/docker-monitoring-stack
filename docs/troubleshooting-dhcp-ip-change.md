# Troubleshooting: Site Unreachable After Session Restart

## 🎯 TL;DR

The dashboard was unreachable because the **server's IP address changed** (from `192.168.1.8` to `192.168.1.9`) due to DHCP lease renewal. Fixed by using the new IP.

---

## ❌ Symptom

Browser shows: "This site can't be reached" / "ERR_UNSAFE_PORT" or similar connection error when trying to access `http://<old-ip>:9090`.

---

## 🔍 Diagnostic Steps

### 1️⃣ Verified Docker is working locally
```bash
curl -I http://localhost:9090
# Result: HTTP/1.1 200 OK ✅
```

### 2️⃣ Verified ports are listening on all interfaces
```bash
ss -tulnp | grep 9090
# Result: LISTEN 0.0.0.0:9090 ✅
```

### 3️⃣ Found the actual problem
```bash
hostname -I
# Result: 192.168.1.9 (NOT 192.168.1.8!)
```

---

## 🛠️ Root Cause

**DHCP (Dynamic Host Configuration Protocol)** automatically assigns IP addresses to devices on a network. When the DHCP lease expires (typically every few hours or after a reboot), the router may assign a different IP address.

### Why this happens:
- Most home/office networks use DHCP for convenience
- IPs are "leased" for a period (e.g., 24 hours)
- On lease renewal, the router may give a different IP if the original is reassigned
- Server reboots, network changes, or router restarts can also trigger this

---

## ✅ The Fix

Just use the **new IP address** in the browser:
- ❌ `http://192.168.1.8:9090` (old IP)
- ✅ `http://192.168.1.9:9090` (current IP)

---

## 🎓 How to Prevent This in the Future

### Solution 1: Set a Static IP (Recommended for servers)
Reserve a specific IP for your server in your router's DHCP settings (often called "Address Reservation" or "Static DHCP").

### Solution 2: Use `localhost` instead
If accessing from the same machine:
```bash
http://localhost:9090
```
This always works regardless of IP changes.

### Solution 3: Use mDNS / Hostname
Some networks support `.local` hostnames:
```bash
http://your-server-name.local:9090
```

---

## 📝 Quick Diagnostic Checklist

If the dashboard is unreachable, check these in order:

| Step | Command | What It Tells You |
|------|---------|-------------------|
| 1 | `docker-compose ps` | Are containers running? |
| 2 | `curl -I http://localhost:9090` | Does dashboard work locally? |
| 3 | `ss -tulnp \| grep 9090` | Is port listening on all interfaces? |
| 4 | `hostname -I` | What's the current server IP? |
| 5 | `sudo ufw status` | Is firewall blocking the port? |

---

## 🔑 Key Takeaway

**Always run `hostname -I` first when you can't reach your dashboard!**

It's the fastest way to find out if your IP changed. 🚀
