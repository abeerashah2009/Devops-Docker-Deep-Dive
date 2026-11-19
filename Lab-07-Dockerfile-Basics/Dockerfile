# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install curl and certificates, then clean package lists
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Create a file inside the image
RUN echo "built with Dockerfile Basics" > /etc/lab-info

# Default command when the container starts
CMD ["curl", "--version"]
