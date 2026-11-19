
# Lab 22 - Building from GitHub in Docker

## Lab Information

- **Lab Name:** Building from GitHub in Docker
- **Platform:** Al Nafi LMS
- **Evaluation:** Al Baari
- **Final Score:** 100 / 100
- **Status:** Passed
- **Total Lab Time:** 10h 7m
- **Time Spent Today:** 2h 47m
- **Operating System:** Ubuntu 24.04 LTS
- **Docker Version:** 29.9.0
- **Git Version:** 2.43.0

---

## 1. Objectives

- Understand Docker integration with Git repositories.
- Create a Dockerfile inside a Git project.
- Clone a repository and build a Docker image.
- Run an application inside a Docker container.
- Create a GitHub Actions workflow for Docker image building.

## 2. Project Structure

```text
Lab-22-Building-from-GitHub-in-Docker/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .github/
│   └── workflows/
│       └── docker-image.yml
└── README.md
```

## 3. Create Flask Application

Created a simple Flask application using Python.

**File: app.py**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

**File: requirements.txt**

```text
flask==3.0.3
```

## 4. Create Dockerfile

The Dockerfile uses Python 3.12 slim as the base image.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
```

## 5. Configure Docker Ignore

**File: .dockerignore**

```text
.git
__pycache__
*.pyc
```

This prevents unnecessary Git and Python cache files from entering the Docker build context.

## 6. Initialize Local Git Remote

Created a local bare Git repository to simulate a GitHub remote.

```bash
git init --bare -b main /tmp/remote.git
```

Cloned the repository:

```bash
git clone /tmp/remote.git docker-github-lab
cd docker-github-lab
```

Added and committed project files:

```bash
git add .
git commit -m "Add simple Flask application and Dockerfile"
git push origin main
```

**First commit:** `63d4e6f`

## 7. Clone Repository and Build Docker Image

Cloned the project again:

```bash
git clone /tmp/remote.git docker-github-lab-build
cd docker-github-lab-build
```

Built the Docker image:

```bash
sudo docker build -t my-flask-app .
```

**Result:** Docker image built successfully.

## 8. Run Docker Container

Started the Flask container:

```bash
sudo docker run -d --name flask-lab -p 5000:5000 my-flask-app
```

Tested the application:

```bash
curl http://localhost:5000
```

**Verified output:**

```text
Hello, Docker!
```

Checked the running container:

```bash
sudo docker ps --filter name=flask-lab
```

Removed the container after testing:

```bash
sudo docker rm -f flask-lab
```

**Result:** Application successfully ran inside the Docker container and responded on port 5000.

## 9. Create GitHub Actions Workflow

Created the workflow directory:

```bash
mkdir -p .github/workflows
```

**File: .github/workflows/docker-image.yml**

```yaml
name: Docker Image CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Build Docker image
      uses: docker/build-push-action@v6
      with:
        context: .
        file: ./Dockerfile
        push: false
        tags: my-flask-app:latest
```

## 10. Validate Workflow YAML

Installed the YAML validation package:

```bash
sudo apt install -y python3-yaml
```

Validated the workflow:

```bash
python3 -c "import yaml; d=yaml.safe_load(open('.github/workflows/docker-image.yml')); print('Jobs:', list(d['jobs']))"
```

**Verified output:**

```text
Jobs: ['build']
```

The workflow was created and validated locally. It was not executed by GitHub Actions because the practical used a local bare Git repository.

## 11. Commit and Push Workflow

```bash
git add .github/workflows/docker-image.yml

git commit -m "Add GitHub Actions workflow for Docker build"

git push origin main
```

**Second commit:** `8458e31`

Verified both commits in the local remote:

```text
8458e31 Add GitHub Actions workflow for Docker build
63d4e6f Add simple Flask application and Dockerfile
```

## 12. Skills Practiced

- Git initialization and cloning
- Git commits and push operations
- Dockerfile creation
- Docker image building
- Docker container management
- Flask application deployment
- Docker port mapping
- Docker build context and .dockerignore
- GitHub Actions workflow configuration
- YAML validation

## 13. Final LMS Evaluation

- **Evaluator:** Al Baari
- **Score:** 100 / 100
- **Result:** PASSED
- **Total Lab Time:** 10h 7m
- **Time Spent Today:** 2h 47m

All practical tasks were completed successfully and the LMS awarded full marks.

---

**Lab 22 Completed Successfully — 100/100**
