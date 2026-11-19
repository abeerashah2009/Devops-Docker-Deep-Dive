# Lab 30 - Practical Evidence

## 1. Docker Installation

- Docker Engine: 27.3.1
- Docker Compose: v5.8.0

## 2. Docker Compose Validation

Result: Docker Compose configuration is valid.

## 3. Successful Automated Test

```text
1 passed in 0.90s
Test exit code: 0
```

## 4. Intentional Test Failure

```text
1 failed in 1.27s
CI test exit code: 1
```

The correct assertion was restored after the failure test.

## 5. CI/CD Pipeline

Verified stages:

- BUILD completed.
- TEST completed with 1 passed.
- DEPLOY completed.

## 6. Flask Application

```text
Hits: 1
Hits: 2
```

## 7. Container Verification

- Redis: Running and healthy.
- Flask web: Running.
- Docker image: cicd-lab:1.0

## 8. LMS Evaluation

**Final Score: 100/100**

**Status: Passed**
