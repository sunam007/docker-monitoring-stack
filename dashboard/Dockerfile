# Use the official NGINX image as the base
FROM nginx:alpine

# Copy our custom HTML file into NGINX's default serving directory
COPY index.html /usr/share/nginx/html/index.html

# NGINX (alpine version) exposes port 80 by default
EXPOSE 80

# NGINX runs automatically when the container starts (CMD inherited from base image)
