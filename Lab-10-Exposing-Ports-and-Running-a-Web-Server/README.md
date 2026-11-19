# Lab 10: Exposing Ports and Running a Web Server

## 1. Lab Objectives

- Understand Docker port mapping.
- Deploy Apache HTTP Server using a Docker container.
- Access a containerized website from the host terminal.
- Verify HTTP response and clean up the container.

## 2. Lab Environment

- Operating System: Ubuntu 24.04.5 LTS
- Docker Version: 29.9.0
- Docker Image: `httpd:2.4`
- Container Name: `web`
- Host Port: `8080`
- Container Port: `80`

## 3. Verify Docker Installation

Check Docker version and service:

```bash
sudo docker --version
systemctl is-active docker
```

Pull the Apache image:

```bash
sudo docker pull httpd:2.4
```

Verify Docker functionality:

```bash
sudo docker run --rm hello-world
```

Result: Docker was installed, active, and working successfully.

## 4. Check Host Port 8080

Check whether port 8080 is available:

```bash
ss -ltn | grep ':8080' || echo "port 8080 is free"
```

Result: `port 8080 is free`

## 5. Create a Custom Web Page

Create the website directory:

```bash
mkdir -p ~/site
```

Create the `index.html` file:

```bash
cat > ~/site/index.html <<'EOF'
<html><body><h1>Hello from Docker httpd</h1></body></html>
EOF
```

Verify the file:

```bash
cat ~/site/index.html
```

Expected HTML:

```html
<html><body><h1>Hello from Docker httpd</h1></body></html>
```

## 6. Run Apache Container with Port Mapping

Start the container:

```bash
sudo docker run -d \
  --name web \
  -p 8080:80 \
  -v ~/site:/usr/local/apache2/htdocs \
  httpd:2.4
```

Explanation:

- `-d`: Runs the container in the background.
- `--name web`: Assigns the container name.
- `-p 8080:80`: Maps host port 8080 to container port 80.
- `-v`: Mounts the custom website directory into Apache's web root.
- `httpd:2.4`: Uses the Apache HTTP Server image.

Verify the running container:

```bash
sudo docker ps --filter name=web
```

Verify port mapping:

```bash
sudo docker port web
```

Verified mapping:

```text
80/tcp -> 0.0.0.0:8080
80/tcp -> [::]:8080
```

## 7. Access the Website from the Terminal

Request the webpage:

```bash
curl -fs --retry 20 --retry-delay 2 --retry-all-errors http://localhost:8080
```

Verify the HTTP status:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8080
```

Verified HTTP status:

```text
200
```

Check the expected page content:

```bash
curl -fs http://localhost:8080 | grep -F "Hello from Docker httpd"
```

Result: The expected heading was returned by the web server.

## 8. Troubleshooting and Logs

Check the container:

```bash
sudo docker ps --filter name=web
```

View Apache logs:

```bash
sudo docker logs web
```

Check firewall status if needed:

```bash
sudo ufw status
```

## 9. Clean Up

Remove the container:

```bash
sudo docker rm -f web
```

Verify that the container was removed:

```bash
sudo docker ps -a --filter name=web
```

Check that host port 8080 is free:

```bash
ss -ltn | grep ':8080' || echo "port 8080 is free"
```

Result:
- The `web` container was removed successfully.
- No matching container remained.
- Host port 8080 was released.
- The `httpd:2.4` image remained available.

## 10. Key Concepts Learned

**Docker Image:** A package containing the application and its required files and dependencies.

**Containerization:** Running an application in an isolated container environment.

**Port Mapping:** Connecting a host port to a port inside a container.

**Volume Mount:** Sharing files or directories between the host and a container.

**HTTP Status 200:** Indicates that the HTTP request was successful.

## 11. LMS Evaluation Result

- Lab: Lab 10 – Exposing Ports and Running a Web Server
- Status: PASSED
- Score: **100/100**
- Evaluated by: Al Baari

All practical tasks were completed and verified successfully.
