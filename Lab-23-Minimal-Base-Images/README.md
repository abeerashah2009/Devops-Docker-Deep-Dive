# Lab 23 - Minimal Base Images

## 1. Objective

- Understand minimal Docker base images.
- Build Alpine and Ubuntu Docker images.
- Install and verify curl in both images.
- Compare image sizes.
- Clean up Docker images.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Docker Version: 29.10.0
- Architecture: x86_64

## 3. Alpine Docker Image

**Dockerfile:**

```dockerfile
FROM alpine:3.20
RUN apk add --no-cache curl bash
```

**Build:**

```bash
sudo docker build -t my-alpine-image .
```

**Verify curl:**

```bash
sudo docker run --rm my-alpine-image curl --version
```

**Result:** Curl 8.14.1 successfully verified.

## 4. Ubuntu Docker Image

**Dockerfile:**

```dockerfile
FROM ubuntu:24.04
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl bash ca-certificates \
    && rm -rf /var/lib/apt/lists/*
```

**Build:**

```bash
sudo docker build -f Dockerfile.ubuntu -t my-ubuntu-image .
```

**Verify curl:**

```bash
sudo docker run --rm my-ubuntu-image curl --version
```

**Result:** Curl 8.5.0 successfully verified.

## 5. Image Size Comparison

Command:

```bash
sudo docker images
```

| Image | Size |
|---|---:|
| Alpine | 23.8 MB |
| Ubuntu | 131 MB |

Exact sizes:

- Alpine: 23,802,979 bytes
- Ubuntu: 130,684,776 bytes

Alpine is approximately 5.49 times smaller than Ubuntu.

## 6. Cleanup

Removed both custom images:

```bash
sudo docker rmi my-alpine-image my-ubuntu-image
```

Verified cleanup:

```bash
sudo docker images
```

Both custom images were successfully removed.

## 7. Learning Outcomes

- Learned about minimal Docker base images.
- Built images using Alpine and Ubuntu.
- Installed packages using apk and apt-get.
- Verified curl inside containers.
- Compared Docker image sizes.
- Practiced Docker image cleanup.

## 8. LMS Result

- Lab: Lab 23 - Minimal Base Images
- Status: Passed
- Score: 100 / 100
