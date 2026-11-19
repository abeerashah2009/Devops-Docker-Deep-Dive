# Lab 25 – Docker Resource Cleanup Evidence

## Environment

- VM: Ubuntu 24.04
- Docker: 29.9.0

## Task 1 – Resource Inspection

Commands executed:

```bash
sudo docker images
sudo docker ps -a
sudo docker system df
sudo docker volume ls
sudo docker network ls
```

Initial Docker environment had no images, containers, or volumes.

## Task 2 – Test Resources Created

- Pulled `alpine:3.20`
- Created stopped container `lab25-stopped`
- Created unused volume `lab25-unused-volume`

Test container completed successfully with output:

```text
Lab 25 cleanup test
```

## Task 3 – Cleanup Results

| Cleanup operation | Result |
|---|---|
| `docker image prune -f` | Executed |
| `docker container prune -f` | Stopped container removed |
| `docker volume prune -f` | Executed |
| `docker image prune -a -f` | Alpine image removed |
| `docker volume prune -a -f` | Named test volume removed |
| `docker system prune -f` | Executed |
| `docker system prune -a -f` | Executed |

Image cleanup reclaimed **12.19 MB**.

Stopped container was successfully deleted.

Unused named volume was successfully deleted.

## Final Verification

Final commands:

```bash
sudo docker images
sudo docker ps -a
sudo docker volume ls
sudo docker system df
sudo docker network ls
```

Final Docker disk usage:

```text
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B
```

Default networks remained available:

- bridge
- host
- none

## Cron Scheduling

Documented an example weekly cron cleanup command. No automatic cron job was scheduled.

## LMS Result

## LMS Result

- Status: Lab Passed
- Score: 95 / 100
- Evaluated by: Al Baari
