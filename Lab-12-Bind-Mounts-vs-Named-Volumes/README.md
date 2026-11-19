# Lab 12: Bind Mounts vs. Named Volumes

## 1. Objectives

- Understand the differences between Docker bind mounts and named volumes.
- Create and use a bind mount.
- Create and use a Docker-managed named volume.
- Verify data sharing and persistence.
- Identify suitable use cases for both storage methods.

## 2. Environment

- Operating System: Ubuntu 24.04.5 LTS
- Docker Version: 29.9.0
- Nginx Image: `nginx:1.27-alpine`
- Bind Mount Host Directory: `~/bind-lab/host-directory`
- Bind Mount Container Path: `/usr/share/nginx/html`
- Named Volume: `my-volume`
- First Host Port: `8080`
- Second Host Port: `8081`

## 3. Verify Docker and Ports

Check Docker:

```bash
sudo docker --version
sudo systemctl is-active docker
sudo docker run --rm alpine:3.20 echo ok
```

The Docker service was active and the Alpine test returned:

```text
ok
```

Check required ports:

```bash
sudo ss -ltn | grep -E ':(8080|8081)\b'
```

Both ports were free before starting the containers.

## 4. Introduction to Docker Storage

Docker provides different ways to store and share data.

**Bind Mount:**
- Connects a host directory to a container directory.
- Host changes are immediately reflected inside the container.
- Useful for development environments and sharing project files.

**Named Volume:**
- Managed by Docker.
- Stored in Docker's volume storage area.
- Can retain data independently of a container.
- Useful for persistent application data and databases.

## 5. Create and Use a Bind Mount

Create the host directory and file:

```bash
mkdir -p ~/bind-lab/host-directory

echo "Hello from the host!" > ~/bind-lab/host-directory/host-file.txt
```

Run Nginx with a read-only bind mount:

```bash
sudo docker run -d \
  --name nginx-bind \
  -v ~/bind-lab/host-directory:/usr/share/nginx/html:ro \
  -p 8080:80 \
  nginx:1.27-alpine
```

Verify the file through Nginx:

```bash
curl -fs http://localhost:8080/host-file.txt
```

Expected output:

```text
Hello from the host!
```

## 6. Verify Host Changes

Modify the file on the host:

```bash
echo "Edited on the host" >> ~/bind-lab/host-directory/host-file.txt
```

Read it through the container:

```bash
curl -s http://localhost:8080/host-file.txt
```

Verified output:

```text
Hello from the host!
Edited on the host
```

The changes made on the host appeared immediately through Nginx.

## 7. Verify Read-Only Protection

Run:

```bash
sudo docker exec nginx-bind touch /usr/share/nginx/html/new.txt
```

Expected error:

```text
touch: /usr/share/nginx/html/new.txt: Read-only file system
```

The `:ro` option prevents the container from writing to the bind-mounted directory.

## 8. Create and Use a Named Volume

Create the named volume:

```bash
sudo docker volume create my-volume
```

Verify it:

```bash
sudo docker volume ls | grep my-volume
```

Run Nginx using the named volume:

```bash
sudo docker run -d \
  --name nginx-volume \
  -v my-volume:/usr/share/nginx/html \
  -p 8081:80 \
  nginx:1.27-alpine
```

Copy the host file into the container:

```bash
sudo docker cp ~/bind-lab/host-directory/host-file.txt nginx-volume:/usr/share/nginx/html/
```

Read the file through Nginx:

```bash
curl -fs http://localhost:8081/host-file.txt
```

Verified output:

```text
Hello from the host!
Edited on the host
```

## 9. Inspect the Named Volume

Inspect Docker volume metadata:

```bash
sudo docker volume inspect my-volume
```

Verified details:

- Volume Name: `my-volume`
- Driver: `local`
- Scope: `local`
- Mountpoint: `/var/lib/docker/volumes/my-volume/_data`

Docker manages this volume independently of the container.

## 10. Verify Named Volume Persistence

Remove the original container:

```bash
sudo docker rm -f nginx-volume
```

Start a replacement container using the same volume:

```bash
sudo docker run -d \
  --name nginx-volume2 \
  -v my-volume:/usr/share/nginx/html \
  -p 8081:80 \
  nginx:1.27-alpine
```

Read the file again:

```bash
curl -fs http://localhost:8081/host-file.txt
```

Verified output:

```text
Hello from the host!
Edited on the host
```

The data remained available after the original container was removed.

## 11. Bind Mounts vs. Named Volumes

| Feature | Bind Mounts | Named Volumes |
|---|---|---|
| Storage location | Host directory | Docker-managed location |
| Management | User manages host path | Docker manages volume |
| Host changes | Reflected immediately | Not directly linked to an arbitrary host directory |
| Persistence | Independent of container | Independent of container |
| Common use | Development files | Application and database data |

### When to Use Bind Mounts

Use bind mounts when:
- Developing applications.
- Sharing source code with containers.
- Editing files directly on the host.
- Requiring immediate host-to-container changes.

### When to Use Named Volumes

Use named volumes when:
- Storing persistent application data.
- Running databases and data-driven services.
- Keeping data separate from container lifecycle.
- Using Docker-managed storage.

## 12. Cleanup

Remove the containers:

```bash
sudo docker rm -f nginx-bind nginx-volume2
```

Remove the named volume:

```bash
sudo docker volume rm my-volume
```

Remove the host directory:

```bash
rm -rf ~/bind-lab
```

Final checks confirmed:
- Both containers removed.
- Named volume removed.
- Host directory removed.
- Ports 8080 and 8081 released.

## 13. Key Learnings

- Bind mounts connect host directories to container paths.
- The `:ro` option provides read-only access.
- Host changes are immediately reflected through bind mounts.
- Named volumes are managed by Docker.
- Named volume data can survive container removal.
- Both storage methods support persistent data, but their management and use cases differ.

## 14. LMS Evaluation

- Lab Name: Bind Mounts vs. Named Volumes
- Lab Status: PASSED
- Final Score: 100/100
- Evaluator: Al Baari

**Result:** All practical tasks, data-sharing checks, persistence checks, and cleanup operations were completed successfully. The LMS evaluation confirmed 100/100.
