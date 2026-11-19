# Lab 30 - Docker in CI/CD Pipeline

## 1. Lab Overview

This lab demonstrates how Docker can be used in a Continuous Integration and Continuous Deployment (CI/CD) pipeline.

The project uses:
- Docker Engine
- Docker Compose
- Python Flask
- Redis
- Pytest
- GitHub Actions

## 2. Application Structure

| File | Purpose |
|---|---|
| `app.py` | Flask web application |
| `test_app.py` | Automated application test |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Builds the application image |
| `docker-compose.yml` | Configures Flask, Redis and test services |
| `ci.sh` | Automates build, test and deployment |
| `.github/workflows/ci.yml` | GitHub Actions workflow |

## 3. Docker Version

Docker Engine: `27.3.1`

Docker Compose: `v5.8.0`

## 4. Application Architecture

The project contains three Docker Compose services:

1. **Redis:** Stores the application hit counter.
2. **Web:** Runs the Flask application on port 5000.
3. **Test:** Runs automated tests using Pytest.

Redis health checks ensure that the database is ready before the web and test services start.

## 5. Build and Test

Build the Docker image:

```bash
sudo docker compose build
```

Run the automated test:

```bash
sudo docker compose up --build --abort-on-container-exit --exit-code-from test test redis
```

Verified successful result:

```text
1 passed
exit code: 0
```

## 6. Failure Detection

An incorrect test assertion was introduced intentionally.

Verified failure result:

```text
1 failed
CI test exit code: 1
```

The original assertion was restored:

```python
assert second == first + 1
```

## 7. CI/CD Pipeline

The `ci.sh` script automates three stages:

- **BUILD:** Builds the Docker image.
- **TEST:** Runs automated tests.
- **DEPLOY:** Starts the Flask application.

Run the pipeline:

```bash
sudo ./ci.sh
```

The pipeline completed successfully.

## 8. Application Verification

The Flask application was tested using curl:

```text
Hits: 1
Hits: 2
```

The Redis and Flask web containers were verified running.

Docker image:

```text
cicd-lab:1.0
```

## 9. GitHub Actions

A workflow reference is included at:

`.github/workflows/ci.yml`

It is configured to run the CI script from the Lab 30 folder when changes are pushed. The workflow file has been prepared but has not been independently verified by a GitHub Actions run.

## 10. Cleanup

Containers and networks can be removed using:

```bash
sudo docker compose down -v
```

## 11. LMS Result

**Lab:** 30 - Docker in CI/CD Pipeline

**Score:** 100/100

**Status:** Passed

## 12. Learning Outcome

I learned how to build Docker images, configure multi-container applications, run automated tests, detect test failures, automate CI/CD stages and deploy a Flask application using Docker Compose.
