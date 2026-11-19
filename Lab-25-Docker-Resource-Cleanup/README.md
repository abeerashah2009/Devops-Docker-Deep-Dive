# Lab 25 – Docker Resource Cleanup

## 1. Objective

The objective of this lab was to identify unused Docker resources, remove them safely, and monitor Docker disk usage.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Docker Version: 29.9.0
- Test Image: alpine:3.20

## 3. Task 1 – List Docker Resources

### 3.1 List all Docker images

```bash
sudo docker images
```

This command displays available Docker images, including repository, tag, image ID, and size.

### 3.2 List all containers

```bash
sudo docker ps -a
```

This command displays running and stopped containers.

### 3.3 Check Docker disk usage

```bash
sudo docker system df
```

This command displays disk usage for images, containers, volumes, and build cache.

## 4. Task 2 – Remove Unused Docker Resources

### 4.1 Remove dangling images

```bash
sudo docker image prune -f
```

This removes dangling images that are not tagged and are not referenced by containers.

### 4.2 Remove all unused images

```bash
sudo docker image prune -a -f
```

This removes all images not used by existing containers, including tagged images.

### 4.3 Remove stopped containers

```bash
sudo docker container prune -f
```

This removes stopped containers.

### 4.4 Remove unused volumes

```bash
sudo docker volume prune -f
```

This removes unused anonymous volumes.

To include unused named volumes:

```bash
sudo docker volume prune -a -f
```

## 5. Task 3 – Monitor and Manage Disk Usage

### 5.1 Check Docker disk usage

```bash
sudo docker system df
```

### 5.2 General Docker cleanup

```bash
sudo docker system prune -f
```

This removes stopped containers, unused networks, dangling images, and unused build cache.

### 5.3 Include all unused images

```bash
sudo docker system prune -a -f
```

This also removes unused images that are not referenced by containers.

**Important:** Prune commands can permanently remove resources. Review what is unused before running cleanup commands on production systems.

### 5.4 Example cron scheduling

A weekly cleanup can be scheduled with cron. Review the command carefully before enabling automatic cleanup.

Example cron entry (runs every Sunday at 2:00 AM):

```cron
0 2 * * 0 /usr/bin/docker system prune -f
```

Edit the cron table with:

```bash
crontab -e
```

This example is documentation only; no automatic cleanup job was scheduled during this lab.

## 6. Practical Test and Verification

Created disposable test resources:

- Image: `alpine:3.20`
- Stopped container: `lab25-stopped`
- Unused volume: `lab25-unused-volume`

Verified the stopped container was removed using:

```bash
sudo docker container prune -f
```

Verified the unused image was removed using:

```bash
sudo docker image prune -a -f
```

Verified the unused named volume was removed using:

```bash
sudo docker volume prune -a -f
```

Final verification commands:

```bash
sudo docker images
sudo docker ps -a
sudo docker volume ls
sudo docker system df
sudo docker network ls
```

Final result:

- Images: 0
- Containers: 0
- Local volumes: 0
- Build cache: 0
- Docker disk usage: 0B
- Default networks: bridge, host, none

## 7. Learning Outcomes

In this lab, I learned how to:

1. List Docker images and containers.
2. Identify unused Docker resources.
3. Remove dangling and unused images.
4. Remove stopped containers.
5. Remove unused volumes.
6. Monitor Docker disk usage with `docker system df`.
7. Perform general cleanup using `docker system prune`.
8. Understand cron-based cleanup scheduling.

## 8. Conclusion

Docker cleanup helps control disk usage and keeps the Docker environment organized. Regular monitoring and careful use of prune commands help remove unnecessary resources while protecting workloads that are still in use.

## 9. LMS Evaluation

- Lab: Docker Resource Cleanup
- Practical tasks: Completed
- LMS Result: Passed
- Score: 95 / 100
