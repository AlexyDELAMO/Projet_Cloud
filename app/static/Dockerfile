# Dockerfile for serving CSS files via Nginx
FROM nginx:alpine

WORKDIR /usr/share/nginx/html/static

# Copy the CSS files into the container
COPY . .

# Expose the port for the Nginx server
EXPOSE 80
