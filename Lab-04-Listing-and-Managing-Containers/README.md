# Lab 04 - Listing & Managing Containers

## Lab Information

- **Topic:** Listing and Managing Docker Containers
- **Platform:** Ubuntu 24.04.5 LTS
- **Tool:** Docker Engine 29.9.0
- **Image:** nginx:1.27
- **Container Name:** my_nginx
- **LMS Score:** 100 / 100
- **Status:** PASSED

## 1. Objectives

- Start a container in detached mode.
- List running containers.
- Stop a running container.
- Restart a stopped container.
- Remove a container.

## 2. Docker Environment Verification

Docker was already installed on the lab VM.

Verified:
- Ubuntu 24.04.5 LTS
- Docker version 29.9.0
- Docker service active
- Official Docker APT repository configured

Package information was refreshed using:

```bash
sudo apt update
```

## 3. Task 1 - Start a Container in Background

Downloaded the Nginx image:

```bash
sudo docker pull nginx:1.27
```

Started the container:

```bash
sudo docker run -d --name my_nginx -p 8080:80 nginx:1.27
```

Explanation:
- `-d` runs the container in detached mode.
- `--name my_nginx` assigns a container name.
- `-p 8080:80` maps host port 8080 to container port 80.

Verified the Nginx welcome page:

```bash
curl -s http://localhost:8080 | head -n 5
```

Result: **Welcome to nginx!**

## 4. Task 2 - List Running Containers

Used:

```bash
sudo docker ps
```

Filtered container information:

```bash
sudo docker ps --filter name=my_nginx \
--format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
```

Verified:
- Container: `my_nginx`
- Image: `nginx:1.27`
- Status: Running (`Up`)
- Port mapping: `8080:80`

## 5. Task 3 - Stop a Container

Stopped the container:

```bash
sudo docker stop my_nginx
```

Checked all containers:

```bash
sudo docker ps -a --filter name=my_nginx \
--format '{{.Names}}: {{.Status}}'
```

Result: `my_nginx: Exited (0)`

Direct localhost verification:

```bash
curl --noproxy '*' -s -o /dev/null \
-w "%{http_code}\n" http://localhost:8080
```

Result: `000`

Note: The lab VM uses an HTTP proxy. The direct localhost check bypassed the proxy to verify the stopped container correctly.

## 6. Task 4 - Restart a Stopped Container

Restarted the container:

```bash
sudo docker start my_nginx
```

Checked its status:

```bash
sudo docker ps --filter name=my_nginx --format '{{.Status}}'
```

Tested the web server:

```bash
sleep 2
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
```

Result: HTTP `200`

The Nginx container restarted successfully and served requests again.

## 7. Task 5 - Remove the Container

Stopped the container:

```bash
sudo docker stop my_nginx
```

Removed it:

```bash
sudo docker rm my_nginx
```

Verified removal:

```bash
sudo docker ps -a
sudo docker ps -a --filter name=my_nginx --format '{{.Names}}'
```

Result: No `my_nginx` container remained.

## 8. Important Commands Revision

| Command | Purpose |
|---|---|
| `docker pull` | Download an image |
| `docker run -d` | Start a container in background |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop` | Stop a container |
| `docker start` | Restart a stopped container |
| `docker rm` | Remove a container |
| `docker logs` | View container logs |

## 9. What I Learned

- How to download and run an Nginx image.
- How to use detached mode.
- How to publish container ports.
- How to list and filter containers.
- How to stop and restart containers.
- How to remove containers after use.
- How to verify container behavior using HTTP status codes.

## 10. Final LMS Result

- **Evaluation:** Al Baari
- **Score:** 100 / 100
- **Status:** PASSED

Lab 04 - Listing & Managing Containers completed successfully.
