

# Lab 06 – Running Interactive Containers

## 1. Objective
Learn how to run interactive and detached Docker containers and explore the Linux environment inside a container.

## 2. Environment
- Host OS: Ubuntu 24.04
- Docker Version: 29.9.0
- Docker Image: ubuntu:24.04

## 3. Pull Ubuntu Image

**Command:**
```bash
sudo docker pull ubuntu:24.04
```

**Result:** Ubuntu 24.04 image downloaded successfully.

## 4. Run Interactive Container

**Command:**
```bash
sudo docker run -it ubuntu:24.04 /bin/bash
```

The `-it` options allow us to interact with the container through a terminal.

### Commands Tested Inside Container

| Command | Purpose |
|---|---|
| `hostname` | Displays container hostname |
| `ls /` | Lists root directory contents |
| `whoami` | Shows current user |
| `ps aux` | Displays running processes |
| `cat /etc/os-release` | Displays operating system details |

**Verified Output:**
- User: `root`
- OS: Ubuntu 24.04.5 LTS
- VERSION_ID: `24.04`
- Hostname: `f6b0a0ac732b`

## 5. Exit Interactive Container

**Command:**
```bash
exit
```

**Verification:**
```bash
sudo docker ps -a
```

Both interactive containers showed:

`Exited (0)`

This means the containers stopped successfully.

## 6. Run Detached Container

**Command:**
```bash
sudo docker run -d --name bg-demo ubuntu:24.04 sleep 300
```

The `-d` option runs the container in the background.

**Verification:**
```bash
sudo docker ps
```

**Result:** The `bg-demo` container was running successfully.

## 7. Execute Command Inside Detached Container

**Command:**
```bash
sudo docker exec bg-demo cat /etc/os-release | grep VERSION_ID
```

**Output:**
```text
VERSION_ID="24.04"
```

The command executed successfully inside the running container.

## 8. Container Cleanup

Removed the detached container:

```bash
sudo docker rm -f bg-demo
```

Checked exited Ubuntu containers:

```bash
sudo docker ps -aq --filter ancestor=ubuntu:24.04 --filter status=exited
```

Removed the exited lab containers:

```bash
sudo docker rm $(sudo docker ps -aq --filter ancestor=ubuntu:24.04 --filter status=exited)
```

Final verification:

```bash
sudo docker ps -a
```

**Result:** No containers remained.

## 9. Key Learnings

1. Interactive mode provides direct terminal access to a container.
2. Detached mode runs a container in the background.
3. `docker exec` executes commands inside a running container.
4. `docker ps` displays running containers.
5. `docker ps -a` displays all containers, including stopped ones.
6. `docker rm` removes stopped containers.

## 10. LMS Assessment Result

**Score: 100/100 – PASSED**

All practical tasks were completed and evaluated successfully.
