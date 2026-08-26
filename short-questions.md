# Short Questions

**What is the difference between a Docker image and a container?**
An image is the blueprint (for example `dashboard:latest`). A container is a running — or stopped — instance of that image. I build the image once, then I can start one or more containers from it.

**What does 9090:80 mean?**
It’s a port mapping: host port `9090` maps to container port `80`. In my project, NGINX listens on 80 inside the dashboard container, so I open the app at `http://localhost:9090`.

**Why do containers need a Docker network?**
So they can talk to each other on an isolated network using service names instead of hard-coded IPs. My dashboard reaches the collector at `collector:6000` through `monitoring-net`.

**Why do we use Docker volumes?**
Volumes keep data outside the container’s filesystem, so it survives restarts and rebuilds. I use `monitoring-data` mounted at `/data` on the collector for that.

**What problem does Docker Compose solve?**
It lets me run a multi-container app with one file and one command. Instead of typing long `docker run` commands for ports, networks, volumes, and restart policies, I use `compose.yaml` and `docker compose up -d`.
