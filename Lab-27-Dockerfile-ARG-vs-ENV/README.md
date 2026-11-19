# Lab 27 – Dockerfile ARG vs ENV

## Lab Information

- **Lab:** 27
- **Topic:** Dockerfile ARG vs ENV
- **Platform:** Ubuntu 24.04
- **Docker Version:** 29.9.0
- **Base Image:** python:3.12-slim
- **LMS Score:** 100/100
- **Status:** Passed

---

## 1. Understanding ARG and ENV

### ARG – Build-Time Variable

- ARG defines a variable used during Docker image building.
- It can receive a value through `--build-arg`.
- It is not automatically available as a runtime environment variable.
- ARG values can be visible in Docker image history.
- Never use ARG for passwords, tokens, or secrets.

### ENV – Runtime Environment Variable

- ENV defines an environment variable in the image.
- It is available when the container runs.
- Its value can be overridden using `docker run -e`.
- It is useful for application configuration.

---

## 2. Create the Project

```bash
mkdir docker-arg-env-demo
cd docker-arg-env-demo
```

## 3. Initial Dockerfile

```dockerfile
FROM python:3.12-slim

ARG APP_VERSION=1.0.0

ENV APP_ENV=production

RUN echo "Building version $APP_VERSION"

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
```

## 4. Python Application

Create `app.py`:

```python
import os

print("Application environment:", os.environ.get("APP_ENV"))
print("Application version:", os.environ.get("APP_VERSION"))
```

## 5. Build the Docker Image

```bash
sudo docker build --progress=plain \
  --build-arg APP_VERSION=2.0.0 \
  -t arg-env-demo .
```

### Verified Build Output

```text
Building version 2.0.0
```

The image was successfully built with the tag `arg-env-demo:latest`.

## 6. Test Runtime Environment Variables

### Run the Container

```bash
sudo docker run --rm arg-env-demo
```

### Verified Output

```text
Application environment: production
Application version: None
```

**Explanation:** APP_VERSION is an ARG, so it is not automatically available inside the running container.

### Verify Default ENV

```bash
sudo docker run --rm arg-env-demo | grep production
```

Output:

```text
Application environment: production
```

### Override ENV at Runtime

```bash
sudo docker run --rm -e APP_ENV=dev arg-env-demo | grep dev
```

Output:

```text
Application environment: dev
```

**Result:** The ENV value was successfully overridden at runtime.

---

## 7. Inspect Docker Image History

```bash
sudo docker history --no-trunc arg-env-demo | grep APP_VERSION
```

### Verified Result

The image history displayed:

```text
RUN |1 APP_VERSION=2.0.0 /bin/sh -c echo "Building version $APP_VERSION"
ARG APP_VERSION=2.0.0
```

**Security Note:** ARG values can be exposed through image metadata and build history. Do not use ARG to pass sensitive information.

---

## 8. Persist a Build Argument Using ENV

The Dockerfile was updated to make the build-time value available at runtime.

### Updated Dockerfile

```dockerfile
FROM python:3.12-slim

ARG APP_VERSION=1.0.0

ENV APP_ENV=production
ENV APP_VERSION_BUILT=$APP_VERSION

RUN echo "Building version $APP_VERSION"

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
```

### Updated Python Application

```python
import os

print("Application environment:", os.environ.get("APP_ENV"))
print("Application version:", os.environ.get("APP_VERSION"))

print("Application version built:", os.environ.get("APP_VERSION_BUILT"))
```

### Rebuild the Image

```bash
sudo docker build --progress=plain \
  --build-arg APP_VERSION=2.0.0 \
  -t arg-env-demo .
```

### Run the Updated Container

```bash
sudo docker run --rm arg-env-demo
```

### Verified Final Output

```text
Application environment: production
Application version: None
Application version built: 2.0.0
```

**Result:** The build argument was copied into `APP_VERSION_BUILT` using ENV and became available at runtime.

---

## 9. ARG vs ENV Comparison

| Feature | ARG | ENV |
|---|---|---|
| Purpose | Build-time variable | Runtime environment variable |
| Build usage | Yes | Yes |
| Runtime availability | Not automatically | Yes |
| Runtime override | Not directly | `docker run -e` |
| Image history | Can be visible | Stored in image configuration |

### Real-World Example

For a web application:

- ARG can specify a software version during image creation.
- ENV can configure the application environment.
- ENV can hold a database endpoint that differs between development and production.

---

## 10. What I Learned

- How to define Docker ARG variables.
- How to use build arguments with `--build-arg`.
- How to define runtime variables with ENV.
- How to override ENV values using `docker run -e`.
- Why ARG is not automatically available at runtime.
- How to inspect Docker image history.
- How to transfer a build-time value into an ENV variable.
- Why secrets should not be passed through Docker ARG.

---

## 11. LMS Evaluation

- **Lab:** 27 – Dockerfile ARG vs ENV
- **Score:** 100 / 100
- **Status:** Lab Passed
- **Evaluator:** Al Baari

**Lab 27 successfully completed with 100/100.**
