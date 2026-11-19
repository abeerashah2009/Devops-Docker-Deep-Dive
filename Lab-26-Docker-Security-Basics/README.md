# Lab 26 – Docker Security Basics

## Lab Information

- **Lab:** 26
- **Topic:** Docker Security Basics
- **Platform:** Ubuntu 24.04
- **Docker Version:** 29.9.0
- **LMS Result:** 100/100
- **Status:** Passed

---

## 1. Run Containers as a Non-Root User

### Objective
Run a Docker container using a normal user instead of root.

### Dockerfile

```dockerfile
FROM ubuntu:24.04

RUN useradd -m appuser

USER appuser

COPY example-script.sh /home/appuser/example-script.sh

CMD ["bash", "/home/appuser/example-script.sh"]
```

### Shell Script

```bash
#!/bin/bash
echo "Running as user: $(whoami)"
```

### Build and Run

```bash
sudo docker build -t non-root-user-example .
sudo docker run --rm non-root-user-example
```

### Verified Output

```text
Running as user: appuser
```

**Result:** The container successfully ran as a non-root user.

---

## 2. Linux Capabilities

### Objective
Understand how Docker capabilities control container privileges.

### Check Default Capabilities

```bash
sudo docker run --rm alpine:3.20 sh -c 'grep CapEff /proc/self/status'
```

### Drop All Capabilities

```bash
sudo docker run --rm --cap-drop ALL alpine:3.20 sh -c 'grep CapEff /proc/self/status'
```

### Verified Output

```text
Default CapEff: 00000000a80425fb
After dropping all: 0000000000000000
```

### Test CHOWN Capability

```bash
sudo docker run --rm alpine:3.20 chown nobody /tmp

sudo docker run --rm --cap-drop ALL alpine:3.20 chown nobody /tmp

sudo docker run --rm --cap-drop ALL --cap-add CHOWN alpine:3.20 chown nobody /tmp
```

**Result:** Dropping all capabilities blocked the ownership change. Adding `CHOWN` restored that permission.

### Test Network Capability

The ping test was also performed with and without `NET_RAW`.

Ping succeeded in both cases because this environment supports unprivileged ICMP sockets. Therefore, ping success alone does not prove that `NET_RAW` is available.

---

## 3. Compare Base Image Sizes

### Command

```bash
sudo docker images --format '{{.Repository}}:{{.Tag}} {{.Size}}'
```

### Verified Results

- Alpine 3.20: 12.2 MB
- Ubuntu-based custom image: 118 MB

**Result:** The Alpine base image is smaller and can help reduce image size.

---

## 4. Docker Network Isolation

### Create an Internal Network

```bash
sudo docker network create --internal isolated-net
```

### Test Internet Connectivity

```bash
sudo docker run --rm --network isolated-net alpine:3.20 ping -c1 -W2 8.8.8.8
```

### Verified Output

```text
ping: sendto: Network unreachable
Network test exit code: 1
```

### Remove the Network

```bash
sudo docker network rm isolated-net
```

**Result:** The internal Docker network blocked external network connectivity.

---

## 5. Read-Only Filesystem

### Command

```bash
sudo docker run --rm --read-only alpine:3.20 touch /x
```

### Verified Output

```text
touch: /x: Read-only file system
Read-only test exit code: 1
```

**Result:** The container could not write to its read-only filesystem.

---

## 6. No New Privileges

### Command

```bash
sudo docker run --rm --security-opt no-new-privileges alpine:3.20 grep NoNewPrivs /proc/self/status
```

### Verified Output

```text
NoNewPrivs: 1
```

**Result:** The no-new-privileges security option was successfully enabled.

---

## 7. Docker Resource Limits

### Start a Container with Resource Limits

```bash
sudo docker run -d \
  --name limited \
  --memory=256m \
  --cpus=1 \
  --pids-limit=64 \
  alpine:3.20 sleep 60
```

### Verify Limits

```bash
sudo docker inspect limited --format 'mem={{.HostConfig.Memory}} pids={{.HostConfig.PidsLimit}}'
```

### Verified Output

```text
mem=268435456 pids=64
```

### Cleanup

```bash
sudo docker rm -f limited
```

**Result:** Memory and process limits were successfully configured.

---

## 8. Test Memory Limit

### Command

```bash
sudo docker run --rm \
  --memory=32m \
  --memory-swap=32m \
  alpine:3.20 \
  sh -c 'x=$(head -c 100000000 /dev/zero | tr "\0" a); echo done'
```

### Verified Output

```text
Memory test exit code: 137
```

**Result:** The process was terminated after exceeding the available memory limit.

---

## 9. Docker Bench Security Audit

### Install Git

```bash
sudo apt install -y git
```

### Clone Docker Bench Security

```bash
cd ~

git clone --depth 1 --branch v1.6.0 \
  https://github.com/docker/docker-bench-security.git
```

### Verify Version

```bash
cd ~/docker-bench-security
git describe --tags --always
```

### Verified Version

```text
v1.6.0
```

### Run Security Audit

```bash
sudo sh docker-bench-security.sh
```

The audit started and reported host configuration warnings, including missing separate container partition and audit configuration checks.

The displayed audit output also included image lookup errors for `12.2MB` and `118MB`. These were recorded as audit output and were not treated as successful security checks.

**Result:** Docker Bench Security v1.6.0 was launched and its initial audit findings were reviewed.

---

## 10. Final Cleanup

The temporary internal network and resource-limited container were removed after testing.

---

## 11. What I Learned

- How to run Docker containers as non-root users.
- How Linux capabilities restrict container permissions.
- Why smaller base images are useful.
- How internal Docker networks isolate containers.
- How read-only filesystems improve security.
- How to enable `no-new-privileges`.
- How to configure Docker memory, CPU, and process limits.
- How to run Docker Bench Security.

---

## 12. LMS Result

- **Score:** 100 / 100
- **Status:** Lab Passed
- **Evaluation:** Al Baari

**Lab 26 – Docker Security Basics successfully completed with 100/100.**
