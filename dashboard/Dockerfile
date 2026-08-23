# Use the official NGINX image as the base
FROM nginx:alpine

# Remove the default NGINX config
RUN rm /etc/nginx/conf.d/default.conf

# Copy our custom NGINX config (with reverse proxy for the collector)
COPY nginx.conf /etc/nginx/conf.d/

# Copy our custom HTML file into NGINX's default serving directory
COPY index.html /usr/share/nginx/html/index.html

# NGINX exposes port 80
EXPOSE 80

# NGINX runs automatically when the container starts (CMD inherited from base image)
