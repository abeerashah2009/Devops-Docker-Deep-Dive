# Lab 08 – Understanding Image Layers & Caching

## 1. Objective

Understand Docker image layers, caching, and how Dockerfile instruction order affects build performance.

Learn how to optimize Docker builds by separating dependency installation from application source code.

## 2. Environment

- Host OS: Ubuntu 24.04
- Docker Version: 29.9.0
- Buildx Version: 0.38.0
- Base Image: node:22-alpine
- Application: Node.js
- Dependency: Express 4.21.0

## 3. Introduction to Docker Image Layers

A Docker image consists of multiple layers.

Each Dockerfile instruction can create a new image layer.

Docker uses build cache to reuse previously created layers when the instruction and its required inputs have not changed.

Important concepts:

- `FROM` – selects the base image.
- `WORKDIR` – sets the working directory.
- `COPY` – copies files into the image.
- `RUN` – executes commands during image building.
- `EXPOSE` – documents the application port.
- `CMD` – defines the default container command.

## 4. Create Node.js Application

Created the project directory:

```bash
mkdir -p ~/docker-image-layers
```

Created `app.js`:

```javascript
const http = require('http');
const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello from layers lab\n'));

http.createServer(app).listen(8080, () => console.log('listening on 8080'));
```

Created `package.json` with the pinned Express dependency:

```json
{
  "name": "layers-lab",
  "version": "1.0.0",
  "main": "app.js",
  "dependencies": {
    "express": "4.21.0"
  }
}
```

## 5. First Dockerfile – Inefficient Build

The first Dockerfile copied all application files before installing dependencies.

```dockerfile
FROM node:22-alpine

WORKDIR /usr/src/app

COPY . .

RUN npm install

EXPOSE 8080

CMD [ "node", "app.js" ]
```

Built the image:

```bash
sudo docker build --progress=plain -t my_node_app .
```

Changed the application source:

```bash
echo "// change 1" >> app.js
```

Rebuilt and measured the build time:

```bash
time sudo docker build --progress=plain -t my_node_app .
```

**Observed result:**

- `COPY . .` executed again.
- `RUN npm install` executed again.
- Dependency installation was repeated after changing only the source file.

**Measured rebuild time: 11.856 seconds**

## 6. Second Dockerfile – Optimized Build

Rearranged the Dockerfile to copy dependency files and install dependencies before copying application source.

```dockerfile
FROM node:22-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "app.js" ]
```

Built the optimized image:

```bash
sudo docker build --progress=plain -t my_node_app_v2 .
```

Changed the source code:

```bash
echo "// change 2" >> app.js
```

Rebuilt and measured the time:

```bash
time sudo docker build --progress=plain -t my_node_app_v2 .
```

**Verified cached steps:**

```text
WORKDIR /usr/src/app       CACHED
COPY package*.json ./     CACHED
RUN npm install           CACHED
COPY . .                  Executed again
```

**Measured optimized rebuild time: 0.875 seconds**

## 7. Build Time Comparison

| Build Type | Rebuild Time |
|---|---:|
| Inefficient Dockerfile | 11.856 seconds |
| Optimized Dockerfile | 0.875 seconds |

The optimized rebuild was approximately 92.6% faster.

## 8. Inspect Docker Image History

Command:

```bash
sudo docker history my_node_app_v2
```

Verified the image history contained:

- CMD instruction
- EXPOSE instruction
- COPY application source
- RUN npm install
- COPY package files
- WORKDIR instruction
- Node.js base image layers

## 9. Verify Node.js and npm

Command:

```bash
sudo docker run --rm my_node_app_v2 sh -c 'node --version && npm --version && cat package.json'
```

Verified:

- Node.js version: v22.23.5
- npm version: 10.9.9
- Express dependency: 4.21.0

## 10. Clean Up Docker Images

Removed both custom images:

```bash
sudo docker rmi my_node_app my_node_app_v2
```

Verified cleanup:

```bash
sudo docker images | grep my_node_app || echo "images removed"
```

Output:

```text
images removed
```

## 11. Key Learnings

1. Docker images consist of multiple layers.
2. Docker reuses cached layers when their instructions and inputs remain unchanged.
3. Changing a file can invalidate its COPY layer and subsequent layers.
4. Installing dependencies before copying source code improves caching.
5. Keeping package files separate helps avoid unnecessary dependency installation.
6. `docker history` displays image build layers.
7. `--progress=plain` helps identify cached and executed build steps.
8. Optimized Dockerfiles can significantly reduce rebuild time.

## 12. LMS Assessment Result

**Score: 94/100 – PASSED**

Al Baari evaluated the lab and confirmed successful completion.

All practical tasks were completed, verified, and evaluated successfully.
