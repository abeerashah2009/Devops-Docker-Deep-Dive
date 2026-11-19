# Lab 11: Working with Volumes

## 1. Objectives

- Understand Docker volumes and data persistence.
- Create, manage, and inspect a named Docker volume.
- Share persistent data between containers using a volume.
- Verify that data remains available after removing a container.

## 2. Environment

- Operating System: Ubuntu 24.04
- Docker Version: 29.9.0
- Docker Image: `alpine:3.20`
- Volume Name: `myvolume`
- Container Name: `volcontainer`
- Container Mount Path: `/data`
- Data File: `/data/hello.txt`

## 3. Verify Docker

Check the Docker version:

```bash
docker --version
```

Test Docker without sudo:

```bash
docker run --rm alpine:3.20 echo ok
```

Expected output:

```text
ok
```

Docker was installed and running successfully.

## 4. Create a Named Volume

Create the volume:

```bash
docker volume create myvolume
```

Verify it:

```bash
docker volume ls | grep myvolume
```

Expected output:

```text
local     myvolume
```

The named volume `myvolume` was created successfully.

## 5. Run a Container Using the Volume

Run an Alpine container and mount the volume at `/data`:

```bash
docker run --name volcontainer \
  -v myvolume:/data \
  -d alpine:3.20 \
  sh -c "echo 'Hello World' > /data/hello.txt"
```

Check the container:

```bash
docker ps -a --filter name=volcontainer
```

The container wrote `Hello World` into the file stored in the mounted volume.

## 6. Read Data and Inspect the Volume

Read the file using a temporary container:

```bash
docker run --rm -v myvolume:/data alpine:3.20 cat /data/hello.txt
```

Verified output:

```text
Hello World
```

Inspect the volume:

```bash
docker volume inspect myvolume
```

The inspection confirmed:
- Volume name: `myvolume`
- Driver: `local`
- Scope: `local`
- Mountpoint: `/var/lib/docker/volumes/myvolume/_data`

## 7. Verify Data Persistence

Remove the original container:

```bash
docker rm -f volcontainer
```

Read the file again:

```bash
docker run --rm -v myvolume:/data alpine:3.20 cat /data/hello.txt
```

Verified output:

```text
Hello World
```

The data remained available even after the original container was removed.

## 8. Final Verification

Verify that the data persists:

```bash
docker run --rm -v myvolume:/data alpine:3.20 cat /data/hello.txt | grep -q 'Hello World' && echo "PASS: Data persists"
```

Verify that the volume exists:

```bash
docker volume ls | grep -q myvolume && echo "PASS: Volume exists"
```

Both checks passed:

```text
PASS: Data persists
PASS: Volume exists
```

## 9. Key Learnings

- Docker volumes provide persistent storage.
- A named volume can be mounted inside a container using `-v`.
- Temporary containers can access data stored in an existing volume.
- Removing a container does not automatically remove its named volume.
- Docker volumes are useful for applications that need persistent data, such as databases and data-driven services.

## 10. Cleanup and Data Management

The original container was removed:

```bash
docker rm -f volcontainer
```

The named volume `myvolume` was intentionally retained to preserve the lab data.

To remove this volume after it is no longer needed:

```bash
docker volume rm myvolume
```

**Note:** Removing a volume deletes the data stored in it. Do not run this command while the lab data is still needed.

## 11. LMS Evaluation

- Lab Name: Working with Volumes
- Lab Status: PASSED
- Final Score: 100/100
- Evaluator: Al Baari

**Result:** All practical tasks and final persistence checks were completed successfully. The LMS evaluation confirmed a score of 100/100.
