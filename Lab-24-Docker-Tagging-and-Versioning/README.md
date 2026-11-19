# Lab 24 - Docker Tagging and Versioning

## 1. Objective

- Understand Docker image tagging and versioning.
- Build Docker images with custom tags.
- Push images to a local Docker registry.
- Verify image tags and registry contents.
- Learn semantic and date-based versioning.
- Clean up Docker containers and images.

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Docker Version: 29.9.0
- Base Image: python:3.12-slim
- Application: Python Flask
- Flask Version: 3.0.3
- Local Registry: registry:2.8.3

## 3. Create Flask Application

Created three project files:

- app.py
- requirements.txt
- Dockerfile

### app.py

```python
import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return f"Hello, {os.environ.get('NAME', 'World')}!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

### requirements.txt

```text
flask==3.0.3
```

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME=World

CMD ["python", "app.py"]
```

## 4. Build Image with Custom Tag

Command:

```bash
sudo docker build -t myapp:v1 .
```

Verified image:

```bash
sudo docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}' | grep myapp
```

Image tag: `myapp:v1`

Image ID:

`sha256:9eb4ef499ee18509ac3ce1a732ceb451b660d26677990ddd7d5c231ecf978893`

## 5. Start Local Docker Registry

Started the registry:

```bash
sudo docker run -d --name registry -p 127.0.0.1:5000:5000 registry:2.8.3
```

Verified registry API:

```bash
curl http://localhost:5000/v2/
```

Result: Registry API responded successfully.

## 6. Create and Push Version Tags

Created two registry tags:

```bash
sudo docker tag myapp:v1 localhost:5000/myapp:1.0.0
sudo docker tag myapp:v1 localhost:5000/myapp:latest
```

Pushed both tags:

```bash
sudo docker push localhost:5000/myapp:1.0.0
sudo docker push localhost:5000/myapp:latest
```

Both pushes completed successfully.

### Registry Verification

```bash
curl -s http://localhost:5000/v2/_catalog
curl -s http://localhost:5000/v2/myapp/tags/list
```

Verified repository: `myapp`

Verified tags:

- 1.0.0
- latest

All three tags pointed to the same image ID.

## 7. Run and Test Application

Started the tagged container:

```bash
sudo docker run -d --name myapp-test -p 127.0.0.1:8000:8000 localhost:5000/myapp:1.0.0
```

Tested the application:

```bash
curl http://localhost:8000/
```

Expected and verified output:

```text
Hello, World!
```

## 8. Naming Conventions and Version Management

Learned these versioning approaches:

### Semantic Versioning

Examples:

- 1.0.0
- 1.0.1
- 1.1.0

### Date-Based Versioning

Created date-based tag:

`myapp:2026.11.19`

### Latest Tag

Used `latest` as an additional image tag.

All tags referred to the same image ID during verification.

## 9. Cleanup

Removed test containers:

```bash
sudo docker rm -f myapp-test registry
```

Removed all lab image tags:

```bash
sudo docker rmi localhost:5000/myapp:1.0.0 localhost:5000/myapp:latest myapp:2026.11.19 myapp:v1
```

Verified cleanup:

```bash
sudo docker images | grep myapp
sudo docker ps -a
```

Result: All custom images and lab containers were successfully removed.

## 10. Learning Outcomes

- Built Docker images with custom tags.
- Used semantic versioning.
- Created date-based image tags.
- Started and used a local Docker registry.
- Pushed images to a registry.
- Verified repositories and tags through the Registry API.
- Ran and tested a Flask application from a tagged image.
- Cleaned up Docker images and containers.

## 11. LMS Evaluation

- Lab: Lab 24 - Docker Tagging and Versioning
- Status: Passed
- Score: 100 / 100
