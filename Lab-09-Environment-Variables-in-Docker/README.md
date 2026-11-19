# Lab 09 – Environment Variables in Docker

## 1. Objective

Understand how to use environment variables inside Docker containers.

Learn how to:
- Define environment variables using Dockerfile `ENV`.
- Override variables using `docker run -e`.
- Load variables using `--env-file`.
- Understand environment-variable precedence.

## 2. Environment Setup

- Operating System: Ubuntu 24.04
- Docker Version: 29.9.0
- Base Image: python:3.12-slim
- Docker Image: env-example

Verified Docker installation:

```bash
docker --version
sudo docker run --rm hello-world
```

Expected output:

```text
Docker version 29.9.0
Hello from Docker!
```

Docker service status:

```text
active
```

## 3. Create Docker Project

Created the project directory:

```bash
mkdir -p ~/docker-env-lab
cd ~/docker-env-lab
```

Created a Dockerfile containing:

```dockerfile
FROM python:3.12-slim

ENV MYVAR="Hello, Docker!"

CMD ["sh", "-c", "echo \"$MYVAR\""]
```

### Explanation

- `FROM` selects the Python base image.
- `ENV` defines an environment variable.
- `CMD` prints the environment variable when the container starts.

## 4. Build the Docker Image

Build command:

```bash
sudo docker build -t env-example .
```

Verified image:

```bash
sudo docker images env-example
```

Image successfully created:

```text
env-example:latest
```

## 5. Run Container with Dockerfile ENV

Command:

```bash
sudo docker run --rm env-example
```

Verified output:

```text
Hello, Docker!
```

Checked the environment variable:

```bash
sudo docker inspect env-example --format '{{range .Config.Env}}{{println .}}{{end}}'
```

Verified:

```text
MYVAR=Hello, Docker!
```

## 6. Override Environment Variable Using -e

Command:

```bash
sudo docker run --rm -e MYVAR="Hello from docker run" env-example
```

Verified output:

```text
Hello from docker run
```

Additional verification:

```bash
sudo docker run --rm -e MYVAR=x env-example | grep -x x
```

Output:

```text
x
```

The `-e` option overrides the default value defined in the Dockerfile.

## 7. Load Environment Variables Using --env-file

Created an environment file named `app.env`:

```text
MYVAR=Hello from env file
```

Created using:

```bash
cat > app.env <<'EOF'
MYVAR=Hello from env file
EOF
```

Ran the container:

```bash
sudo docker run --rm --env-file app.env env-example
```

Verified output:

```text
Hello from env file
```

## 8. Environment Variable Precedence

Tested both `--env-file` and `-e` together:

```bash
sudo docker run --rm --env-file app.env -e MYVAR="Hello from -e" env-example
```

Verified output:

```text
Hello from -e
```

### Precedence Order

1. Runtime `-e` – Highest priority.
2. `--env-file` – Second priority.
3. Dockerfile `ENV` – Default value.

The runtime value takes precedence over the environment file and Dockerfile default.

## 9. Verify Original Image ENV

Command:

```bash
sudo docker inspect env-example --format '{{range .Config.Env}}{{println .}}{{end}}' | grep '^MYVAR='
```

Verified output:

```text
MYVAR=Hello, Docker!
```

Runtime overrides do not modify the original image configuration.

## 10. Important Learnings

1. Environment variables configure applications inside containers.
2. Dockerfile `ENV` defines default environment variables.
3. The `-e` option overrides environment variables at runtime.
4. `--env-file` loads variables from a configuration file.
5. Runtime `-e` takes precedence over `--env-file`.
6. Runtime configuration avoids rebuilding images for different settings.
7. Never store real passwords or secrets in Dockerfile `ENV`.
8. Environment variables can be visible through `docker inspect`.

## 11. LMS Assessment Result

**Score: 100/100 – PASSED**

Al Baari evaluated the lab and confirmed:

- Lab Status: Passed
- Final Score: 100/100
- All practical tasks successfully completed.
