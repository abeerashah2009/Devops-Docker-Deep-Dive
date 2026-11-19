
# Lab 19 – Docker Inspect and Metadata

## 1. Lab Overview

**Objective:** Learn how to inspect Docker containers and images, understand metadata, extract configuration details using `jq`, and use inspection commands for automation and debugging.

**LMS Result:** Passed – 100/100

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Docker Engine: 29.10.0
- Docker Compose: 5.8.0
- jq: 1.7
- Container Image: nginx:1.27-alpine

## 3. Create the Web Container

```bash
sudo docker run -d \
  --name web \
  -e APP_ENV=lab \
  -p 8081:80 \
  -v lab-vol:/data \
  nginx:1.27-alpine
```

Container configuration:

- Name: web
- Environment variable: APP_ENV=lab
- Host port: 8081
- Container port: 80
- Named volume: lab-vol
- Mount destination: /data

## 4. Inspect Containers and Images

List running containers:

```bash
sudo docker ps
```

Inspect container metadata:

```bash
sudo docker inspect web
```

Display the first 20 lines:

```bash
sudo docker inspect web | head -20
```

List Docker images:

```bash
sudo docker images
```

Inspect image metadata:

```bash
sudo docker inspect nginx:1.27-alpine | jq -r '.[0].Id, .[0].Architecture, .[0].Os'
```

Verified image details:

- Architecture: amd64
- Operating System: linux

## 5. Understand Docker Inspect Output

Display top-level metadata keys:

```bash
sudo docker inspect web | jq '.[0] | keys'
```

Check container status:

```bash
sudo docker inspect -f '{{.State.Status}}' web
```

Verified status: running

Important metadata sections:

- Config: Container configuration and environment variables.
- NetworkSettings: Network configuration and IP address.
- Mounts: Volume mount information.
- State: Current container status and runtime state.
- HostConfig: Host-side container configuration.

## 6. Inspect Environment Variables

Display environment variables:

```bash
sudo docker inspect --format '{{json .Config.Env}}' web
```

Find the lab environment variable:

```bash
sudo docker inspect web | jq -r '.[0].Config.Env[]' | grep APP_ENV=lab
```

Extract APP_ENV using jq:

```bash
sudo docker inspect web | jq -r '.[0].Config.Env[] | select(startswith("APP_ENV"))'
```

Verified output:

```text
APP_ENV=lab
```

## 7. Inspect Network Configuration

Get the container bridge IP:

```bash
sudo docker inspect -f '{{.NetworkSettings.Networks.bridge.IPAddress}}' web
```

Verified container IP: 172.17.0.2

Check port bindings:

```bash
sudo docker inspect -f '{{json .HostConfig.PortBindings}}' web
```

Verified mapping:

- Host port: 8081
- Container port: 80

Test the published web server:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
```

Verified HTTP response: 200

## 8. Inspect Volume Mounts

Inspect the container mounts:

```bash
sudo docker inspect -f '{{json .Mounts}}' web | jq
```

Verified volume details:

- Type: volume
- Name: lab-vol
- Source: /var/lib/docker/volumes/lab-vol/_data
- Destination: /data
- Driver: local

## 9. Automation and Debugging with jq

Extract APP_ENV automatically:

```bash
sudo docker inspect web | jq -r '.[0].Config.Env[] | select(startswith("APP_ENV"))'
```

Display all environment variables:

```bash
sudo docker inspect web | jq '.[0].Config.Env'
```

Generate a one-line container summary:

```bash
sudo docker inspect web | jq -r '.[0] | "\(.Name) \(.State.Status) \(.NetworkSettings.Networks.bridge.IPAddress)"'
```

Verified summary:

```text
/web running 172.17.0.2
```

## 10. Cleanup

Remove the container:

```bash
sudo docker rm -f web
```

Remove the named volume:

```bash
sudo docker volume rm lab-vol
```

Verify container removal:

```bash
sudo docker ps -a --filter "name=^web$"
```

Verify volume removal:

```bash
sudo docker volume ls --filter "name=^lab-vol$"
```

Both resources were successfully removed.

## 11. Final Verification

- [x] Docker Engine installed and verified.
- [x] Nginx container created successfully.
- [x] Container metadata inspected.
- [x] Image metadata inspected.
- [x] Container state verified.
- [x] Environment variable extracted using jq.
- [x] Network IP and port bindings inspected.
- [x] HTTP response verified as 200.
- [x] Named volume inspected.
- [x] One-line metadata summary generated.
- [x] Container and volume removed.
- [x] Cleanup verified.
- [x] LMS evaluation passed.

## 12. LMS Result

**Lab 19 – Docker Inspect and Metadata**

**Score: 100 / 100**

**Status: PASSED**
