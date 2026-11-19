# Lab 13: Docker Networking Basics

## 1. Objectives

- Understand Docker networking basics.
- Connect containers on the same network.
- Explore Docker networks using Docker CLI commands.
- Understand the difference between the default bridge and user-defined bridge networks.
- Verify communication between containers using ping and Docker DNS.

## 2. Environment

- Operating System: Ubuntu 24.04
- Docker Server Version: 29.10.0
- Docker Image: alpine:3.20
- Network Driver: Bridge
- GitHub Repository: Devops-Docker-Deep-Dive

**Note:** The requested Docker 27.3.1 package was not available in the configured repository. Docker 29.10.0 was installed as permitted by the lab instructions.

## 3. Docker Installation

### Update Package Lists

```bash
sudo apt update
```

### Install Required Packages

```bash
sudo apt install -y ca-certificates curl jq
```

### Configure Docker Repository

```bash
sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc
```

The Docker repository was already configured through `docker.sources`. The duplicate `docker.list` file created during setup was removed.

### Install Docker

```bash
VERSION_STRING=5:29.10.0-1~ubuntu.24.04~noble

sudo apt install -y \
  docker-ce=$VERSION_STRING \
  docker-ce-cli=$VERSION_STRING \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin

sudo systemctl enable --now docker
```

### Verify Docker

```bash
sudo docker version --format '{{.Server.Version}}'

sudo systemctl is-active docker

sudo docker run --rm hello-world
```

**Verified Results:**
- Docker Version: 29.10.0
- Docker Service: active
- Hello World: Successful

## 4. Task 1: Launch Two Containers on Default Bridge

### Pull Alpine Image

```bash
sudo docker pull alpine:3.20
```

### Run Two Containers

```bash
sudo docker run -d --name container1 alpine:3.20 sleep infinity

sudo docker run -d --name container2 alpine:3.20 sleep infinity
```

### List Running Containers

```bash
sudo docker ps --format '{{.Names}} {{.Status}}'
```

**Verified Results:**
- container1: Running
- container2: Running
- Both containers used the default bridge network.

### Inspect Default Bridge

```bash
sudo docker network inspect bridge \
  --format '{{json .IPAM.Config}}' | jq
```

**Verified Network Subnet:**

```text
172.17.0.0/16
```

## 5. Task 2: Find Container IP Addresses

### Inspect Container IP Addresses

```bash
IP1=$(sudo docker inspect -f \
  '{{.NetworkSettings.Networks.bridge.IPAddress}}' container1)

IP2=$(sudo docker inspect -f \
  '{{.NetworkSettings.Networks.bridge.IPAddress}}' container2)

echo "container1=$IP1"
echo "container2=$IP2"
```

**Verified Output:**

```text
container1=172.17.0.2
container2=172.17.0.3
```

**Note:** The network-specific inspection path was used because the older `.NetworkSettings.IPAddress` template was unavailable on this Docker version.

## 6. Task 3: Verify Container Connectivity

### Check Ping Utility

```bash
sudo docker exec container1 which ping
```

**Verified Output:**

```text
/bin/ping
```

### Ping container2 by IP Address

```bash
sudo docker exec container1 ping -c 2 "$IP2"
```

**Verified Result:**

```text
2 packets transmitted, 2 packets received, 0% packet loss
```

The containers successfully communicated using their IP addresses.

### Test Default Bridge Name Resolution

```bash
sudo docker exec container1 ping -c 2 container2
```

**Verified Output:**

```text
ping: bad address 'container2'
```

This failure was expected. The default bridge does not provide automatic container-name DNS resolution.

## 7. Create a User-Defined Bridge Network

### Create Network

```bash
sudo docker network create labnet
```

### Launch Containers on labnet

```bash
sudo docker run -d --name c1 \
  --network labnet alpine:3.20 sleep infinity

sudo docker run -d --name c2 \
  --network labnet alpine:3.20 sleep infinity
```

### Test Container Communication by Name

```bash
sudo docker exec c1 ping -c 2 c2
```

**Verified Result:**

```text
2 packets transmitted, 2 packets received, 0% packet loss
```

The container `c1` successfully resolved and pinged `c2` by its name.

### Inspect Network Containers

```bash
sudo docker network inspect labnet \
  | jq '[.[0].Containers[].Name] | sort'
```

**Verified Output:**

```json
[
  "c1",
  "c2"
]
```

## 8. Default Bridge vs User-Defined Bridge

| Feature | Default Bridge | User-Defined Bridge |
|---|---|---|
| Container communication | By IP | By IP and name |
| Automatic DNS | No | Yes |
| Network creation | Created by Docker | Created by user |
| Container isolation | Network-based | Network-based |
| Configuration | Basic | More flexible |

### Key Difference

The default bridge allows containers to communicate using IP addresses, but does not provide automatic container-name resolution.

A user-defined bridge network provides automatic DNS, allowing containers to communicate using their names.

## 9. Task 4: Cleanup

### Remove All Lab Containers

```bash
sudo docker rm -f container1 container2 c1 c2 || true
```

### Remove Custom Network

```bash
sudo docker network rm labnet || true
```

### Verify Cleanup

```bash
sudo docker ps -a --format '{{.Names}}'

sudo docker network inspect labnet
```

**Verified Results:**
- container1 removed: PASS
- container2 removed: PASS
- c1 removed: PASS
- c2 removed: PASS
- labnet removed: PASS
- No lab containers remained.

## 10. Key Learnings

1. Docker containers can communicate through Docker networks.
2. The default bridge supports communication through container IP addresses.
3. The default bridge does not provide automatic container-name DNS resolution.
4. User-defined bridge networks provide automatic DNS resolution.
5. `docker inspect` helps retrieve container network information.
6. `docker network inspect` displays network configuration and attached containers.
7. The `ping` command verifies connectivity between containers.

## 11. LMS Evaluation

- Lab Name: Docker Networking Basics
- Lab Status: PASSED
- Final Score: 100/100
- Evaluator: Al Baari

**Result:** Successfully completed all Lab 13 tasks and verified Docker container networking.

