# Lab 24 - Evidence

## Environment
- Ubuntu 24.04 LTS
- Docker 29.9.0
- Python 3.12-slim
- Flask 3.0.3

## Task 1 - Custom Image Tag
- Image built: myapp:v1
- Build status: Successful
- Image ID: 9eb4ef499ee1

## Task 2 - Local Registry
- Registry: registry:2.8.3
- Registry address: 127.0.0.1:5000
- Registry API: Verified
- Repository: myapp
- Version tag: 1.0.0
- Additional tag: latest
- Both pushes: Successful

## Task 3 - Application Test
- Container: myapp-test
- Image: localhost:5000/myapp:1.0.0
- Port: 8000
- Application response: Hello, World!
- Test status: Passed

## Version Management
- Custom tag: myapp:v1
- Semantic version: 1.0.0
- Latest tag: latest
- Date-based tag: 2026.11.19
- All tags referenced the same image ID.

## Cleanup
- Application container removed.
- Registry container removed.
- All custom image tags removed.
- Cleanup verified successfully.

## LMS Evaluation
- Lab: Lab 24 - Docker Tagging and Versioning
- Status: Passed
- Score: 100 / 100
