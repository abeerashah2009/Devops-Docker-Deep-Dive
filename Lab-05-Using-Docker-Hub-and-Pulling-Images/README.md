
# Lab 05 - Using Docker Hub and Pulling Images

## Objective
Learn how to use Docker Hub, search for official images, pull Docker images, and inspect image layers.

## Environment
- OS: Ubuntu 24.04
- Docker Version: 29.9.0
- Image: nginx:1.27
- Registry: Docker Hub

## Task 1 - Understanding Docker Hub

Docker Hub is a centralized platform for storing, sharing, and downloading container images.

Verified Docker Hub API connectivity:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://hub.docker.com/v2/repositories/library/nginx/
```

Result: HTTP 200

## Task 2 - Searching for Official Images

Search Nginx images:

```bash
sudo docker search --limit 5 nginx
```

Search official images only:

```bash
sudo docker search --filter is-official=true --limit 5 nginx
```

Result: Official Nginx image found with [OK].

Retrieved available tags using the Docker Hub API.

## Task 3 - Pulling the Nginx Image

Pulled the pinned Nginx image:

```bash
sudo docker pull nginx:1.27
```

Result: Image downloaded successfully.

Verified local image:

```bash
sudo docker images nginx
```

Image details:
- Repository: nginx
- Tag: 1.27
- Image ID: 6784fb0834aa
- Disk Usage: 282MB
- Content Size: 75.5MB

## Task 4 - Inspecting Image Layers

Viewed image history:

```bash
sudo docker history --format 'table {{.CreatedBy}}\t{{.Size}}' nginx:1.27
```

Counted filesystem layers:

```bash
sudo docker image inspect nginx:1.27 --format '{{len .RootFS.Layers}}'
```

Result: 7 filesystem layers.

## Key Concepts Learned

1. Docker Hub is a public registry for container images.
2. Official images are maintained by Docker or the associated project owner.
3. `docker search` searches for available images.
4. `docker pull` downloads an image and its layers.
5. `docker images` lists locally available images.
6. `docker history` displays image build history.
7. `docker image inspect` provides detailed image information.
8. Docker image layers are read-only filesystem changes stacked together.

## LMS Result

- Lab Name: Using Docker Hub and Pulling Images
- Score: 100/100
- Status: PASSED

## Conclusion

Successfully connected to Docker Hub, searched for the official Nginx image, downloaded nginx:1.27, verified the local image, and inspected its history and filesystem layers.
