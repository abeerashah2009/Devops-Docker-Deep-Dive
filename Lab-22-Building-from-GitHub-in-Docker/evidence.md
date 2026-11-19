
# Lab 22 - Evidence

## 1. LMS Evaluation

- Lab: Building from GitHub in Docker
- Evaluator: Al Baari
- Score: 100 / 100
- Status: Passed
- Total Time: 10h 7m
- Time Spent Today: 2h 47m

## 2. Environment Verification

- OS: Ubuntu 24.04 LTS
- Docker: 29.9.0
- Git: 2.43.0
- Docker Service: Active

## 3. Git Repository Evidence

Local bare repository created:

`/tmp/remote.git`

Application commit:

`63d4e6f`

Workflow commit:

`8458e31`

## 4. Docker Build Evidence

Command:

`sudo docker build -t my-flask-app .`

Result: Build completed successfully.

## 5. Container Test Evidence

Command:

`curl http://localhost:5000`

Verified response:

`Hello, Docker!`

Container name: `flask-lab`

Port mapping: `5000:5000`

Container cleanup completed successfully.

## 6. GitHub Actions Evidence

Workflow:

`.github/workflows/docker-image.yml`

YAML validation result:

`Jobs: ['build']`

Workflow was created and validated locally. It was not executed on GitHub Actions.

## 7. Final Result

All practical tasks completed successfully.

**LMS Score: 100 / 100**

**Status: PASSED**
