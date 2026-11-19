# Lab 16: Docker Compose Basics

## 1. Objectives

- Understand Docker Compose fundamentals.
- Create and configure a `docker-compose.yml` file.
- Deploy and manage multiple containers using Docker Compose.
- Verify services, application logs, and cleanup.

## 2. Environment

- OS: Ubuntu 24.04
- Docker Engine: 29.9.0
- Docker Compose: v5.6.0
- Web image: nginx:1.27-alpine
- App image: alpine:3.20

## 3. Verify Docker Installation

Check Docker and Compose versions:

```bash
docker --version
sudo docker compose version
```

Check Docker service:

```bash
sudo systemctl enable --now docker
sudo systemctl is-active docker
```

Run the Hello World test:

```bash
sudo docker run --rm hello-world
```

**Result:** Docker Engine and Compose were available and working successfully.

## 4. Create the Project Directory

```bash
mkdir -p ~/docker-compose-basics
cd ~/docker-compose-basics
```

## 5. Create docker-compose.yml

Create the Compose configuration:

```yaml
services:
  web:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"
  app:
    image: alpine:3.20
    command: ["echo", "Hello, Docker Compose!"]
```

The `web` service runs an Nginx web server and maps host port 8080 to container port 80.

The `app` service runs an Alpine container and prints a message.

## 6. Validate the Compose Configuration

```bash
sudo docker compose config
sudo docker compose config --services
```

Expected services:

```text
app
web
```

**Result:** Compose configuration validated successfully.

## 7. Check Port 8080

```bash
ss -ltn | grep ':8080' || echo "port 8080 is free"
```

**Result:** Port 8080 was free before starting the services.

## 8. Start Services

```bash
sudo docker compose up -d
```

Check container status:

```bash
sudo docker compose ps -a
```

Observed results:

- `web`: Running.
- `app`: Exited (0), as expected after printing its message.

## 9. Verify Nginx Web Server

Check HTTP response:

```bash
curl -fs --retry 20 --retry-delay 2 --retry-all-errors \
-o /dev/null -w '%{http_code}\n' http://localhost:8080
```

Expected HTTP status:

```text
200
```

Check the Nginx welcome page:

```bash
curl -s localhost:8080 | grep -i 'Welcome to nginx'
```

Verified output:

```text
<title>Welcome to nginx!</title>
<h1>Welcome to nginx!</h1>
```

**Result:** Nginx responded successfully on port 8080.

## 10. Verify Application Logs

```bash
sudo docker compose logs app | grep 'Hello, Docker Compose!'
```

Verified output:

```text
app-1  | Hello, Docker Compose!
```

**Result:** The Alpine application printed the expected message.

## 11. Stop Services and Clean Up

Remove containers and the Compose network:

```bash
sudo docker compose down
```

Verify containers were removed:

```bash
sudo docker compose ps -a
```

Verify the Nginx image remains available:

```bash
sudo docker images nginx
```

Check Docker service:

```bash
sudo systemctl is-active docker
```

**Result:**
- Both containers removed.
- Compose network removed.
- No Compose containers remaining.
- Nginx image preserved.
- Docker service remained active.

## 12. Key Learnings

- Docker Compose manages multiple containers using one YAML configuration file.
- `docker compose config` validates the configuration.
- `docker compose up -d` starts services in detached mode.
- `docker compose ps -a` displays service container states.
- `docker compose logs` displays application output.
- `docker compose down` removes containers and the project network.
- Images remain available after Compose cleanup.

## 13. LMS Evaluation

- Lab Status: PASSED
- Final Score: 100/100
- Evaluated by: Al Baari
- Result: Successful

**Lab 16 — Docker Compose Basics completed successfully with 100/100.**
