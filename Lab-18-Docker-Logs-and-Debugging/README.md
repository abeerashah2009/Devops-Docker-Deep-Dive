# Lab 18 – Docker Logs and Debugging

## LMS Result

- **Status:** Passed
- **Score:** 88/100
- **Practical:** Docker Logs and Debugging

## Environment

- Operating System: Ubuntu 24.04 LTS
- Docker Engine: 29.10.0
- Docker Compose: v5.8.0
- Nginx Image: `nginx:1.27-alpine`
- Alpine Image: `alpine:latest`

## Task 1 – Run a Container in the Background

### 1. Pull the Nginx image

```bash
sudo docker pull nginx:1.27-alpine
```

### 2. Start the container

```bash
sudo docker run -d --name my_nginx -p 8082:80 nginx:1.27-alpine
```

### 3. Verify the container

```bash
sudo docker ps --filter name=my_nginx
```

The container started successfully.

### 4. Test the web server

```bash
curl -sI http://localhost:8082 | head -1
```

**Verified output:**

```text
HTTP/1.1 200 OK
```

## Task 2 – View and Debug Container Logs

### 1. View startup logs

```bash
sudo docker logs my_nginx
```

Nginx startup and configuration messages were displayed.

### 2. Generate HTTP requests

Successful request:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082/
```

Output: `200`

Missing page request:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082/nope
```

Output: `404`

### 3. Filter access logs

```bash
sudo docker logs my_nginx 2>&1 | grep 'GET /'
```

The logs showed both successful and failed GET requests.

### 4. Follow logs in real time

```bash
sudo timeout 5 docker logs -f --tail 20 my_nginx
```

The command displayed recent logs and followed new log entries for five seconds.

### 5. View recent logs

```bash
sudo docker logs --since 1m my_nginx 2>&1 | tail -n 5
```

### 6. Create a failing container

```bash
sudo docker run --name bad alpine sh -c 'echo oops; exit 3'
```

### 7. Inspect its logs

```bash
sudo docker logs bad
```

Verified output:

```text
oops
```

### 8. Check the exit code

```bash
sudo docker inspect -f '{{.State.ExitCode}}' bad
```

Verified output:

```text
3
```

## Task 3 – Troubleshooting with Docker Exec

### 1. Inspect processes and environment

```bash
sudo docker exec my_nginx sh -c 'ps aux; env'
```

Verified:
- Nginx master process: PID 1
- Nginx worker processes: PIDs 31 and 32
- Container environment variables displayed successfully

### 2. Check the Nginx version variable

```bash
sudo docker exec my_nginx sh -c 'env | grep NGINX_VERSION'
```

Verified output:

```text
NGINX_VERSION=1.27.5
```

## Cleanup

Remove both lab containers:

```bash
sudo docker rm -f my_nginx bad
```

Verify remaining containers:

```bash
sudo docker ps -a
```

No lab containers remained.

Verify Docker service:

```bash
systemctl is-active docker
```

Verified output:

```text
active
```

## Final Result

- Nginx container started and served HTTP requests.
- Docker logs were inspected and filtered.
- HTTP 200 and 404 responses were verified.
- A failed container was investigated using its logs and exit code.
- Docker Exec was used to inspect processes and environment variables.
- Lab containers were removed successfully.
- **Al Nafi LMS Score: 88/100**
- **Status: Passed**
