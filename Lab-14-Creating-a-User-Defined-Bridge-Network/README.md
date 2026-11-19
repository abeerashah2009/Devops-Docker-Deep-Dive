# Lab 14: Creating a User-Defined Bridge Network

## 1. Objectives

- Understand Docker bridge networks.
- Create a custom bridge network.
- Connect multiple containers to the same network.
- Communicate between containers using their names.
- Test HTTP connectivity between containers.
- Compare user-defined bridge networking with the default bridge.

## 2. Environment

| Component | Version |
|---|---|
| Operating System | Ubuntu 24.04.5 LTS |
| Docker Engine | 29.9.0 |
| Nginx Image | nginx:1.27 |
| Curl Image | curlimages/curl |

Docker was already installed on the lab VM. Its service was active, and the Hello World test completed successfully.

## 3. Verify Docker Installation

```bash
sudo docker --version
sudo systemctl is-active docker
sudo docker run --rm hello-world
```

**Result:** Docker was working correctly.

## 4. Task 1 — Create a Custom Bridge Network

Created a user-defined bridge network named `mynet`.

```bash
sudo docker network create mynet
sudo docker network ls --filter name=mynet
sudo docker network inspect mynet --format 'Name={{.Name}} Driver={{.Driver}} Scope={{.Scope}}'
```

**Verified results:**

- Network name: `mynet`
- Driver: `bridge`
- Scope: `local`

## 5. Task 2 — Run Containers on the Custom Network

Pulled the Nginx image:

```bash
sudo docker pull nginx:1.27
```

Created two containers on the same custom network:

```bash
sudo docker run -d --name container1 --network mynet nginx:1.27

sudo docker run -d --name container2 --network mynet nginx:1.27
```

Verified running containers:

```bash
sudo docker ps --format '{{.Names}} {{.Status}}'
```

Verified network attachments:

```bash
sudo docker network inspect mynet --format '{{range .Containers}}{{.Name}} {{end}}'
```

**Result:** Both containers were running and attached to `mynet`.

## 6. Task 3 — Test Container Name Resolution

Used `getent hosts` from inside `container1`:

```bash
sudo docker exec container1 getent hosts container2
```

**Verified output:**

```text
172.18.0.3 container2
```

The IP address can vary between Docker networks and lab environments.

**Result:** Docker's embedded DNS successfully resolved `container2` by its container name.

## 7. Test HTTP Communication

Used a temporary curl container connected to `mynet` to request the Nginx page:

```bash
sudo docker run --rm --network mynet curlimages/curl -s --retry 10 --retry-delay 2 --retry-all-errors http://container2 | head -n 5
```

The Nginx welcome page was returned.

Verified the HTTP status code:

```bash
sudo docker run --rm --network mynet curlimages/curl -s -o /dev/null -w '%{http_code}\n' http://container2
```

**Verified result:**

```text
200
```

**Result:** HTTP communication between containers by name was successful.

## 8. Task 4 — Compare with the Default Bridge

Created `container3` without specifying a custom network:

```bash
sudo docker run -d --name container3 nginx:1.27
```

Verified its network mode:

```bash
sudo docker inspect container3 --format '{{.HostConfig.NetworkMode}}'
```

**Verified result:**

```text
bridge
```

Tested name resolution from a temporary curl container:

```bash
sudo docker run --rm curlimages/curl -s -m 5 http://container3
echo "exit code: $?"
```

**Verified result:**

```text
exit code: 6
```

Exit code `6` indicates that curl could not resolve the host name.

**Conclusion:** The default bridge does not provide the same automatic container-name DNS resolution as a user-defined bridge.

## 9. Cleanup

Removed all lab containers:

```bash
sudo docker rm -f container1 container2 container3
```

Removed the custom network:

```bash
sudo docker network rm mynet
```

Verified that the network was removed:

```bash
sudo docker network ls --filter name=mynet
```

Verified that no lab containers remained:

```bash
sudo docker ps -a --format '{{.Names}}'
```

**Result:** All lab containers and the custom network were successfully removed.

## 10. Key Learnings

1. Docker user-defined bridge networks provide automatic container-name resolution.
2. Containers on the same custom network can communicate with each other.
3. Docker's embedded DNS resolves container names on user-defined networks.
4. A temporary curl container can test HTTP connectivity without installing curl inside Nginx.
5. HTTP status `200` confirms a successful web request.
6. The default bridge does not provide equivalent automatic name resolution.
7. Cleaning up containers and networks keeps the lab environment organized.

## 11. LMS Evaluation

- Lab Status: **PASSED**
- Final Score: **100/100**
- Evaluator: **Al Baari**

**Lab 14 completed successfully.**
