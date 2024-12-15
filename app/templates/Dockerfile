# Dockerfile for serving HTML files via Nginx
FROM nginx:alpine

WORKDIR /usr/share/nginx/html/templates

# Copy the HTML files into the container
COPY . .

# Expose the port for the Nginx server
EXPOSE 80
