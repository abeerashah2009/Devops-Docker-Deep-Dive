# Lab 29 – Practical Evidence

## 1. Registry Image Download

Command:
```bash
sudo docker pull registry:2.8.3
```

Result: Registry image downloaded successfully.

## 2. Private Registry Started

Command:
```bash
sudo docker run -d -p 5000:5000 --name myregistry registry:2.8.3
```

Verification:
```bash
sudo docker ps --filter name=myregistry
curl -s http://localhost:5000/v2/
```

Result: Registry container was running and API returned `{}`.

## 3. Alpine Image Pulled and Tagged

Commands:
```bash
sudo docker pull alpine:3.20
sudo docker tag alpine:3.20 localhost:5000/myimage:1
sudo docker images localhost:5000/myimage
```

Result: Alpine image downloaded and tagged successfully.

## 4. Image Pushed Successfully

Command:
```bash
sudo docker push localhost:5000/myimage:1
```

Result: Image push completed successfully.

## 5. Registry Verification

Repository API:
```bash
curl -s http://localhost:5000/v2/_catalog
```

Verified response:
```json
{"repositories":["myimage"]}
```

Tag API:
```bash
curl -s http://localhost:5000/v2/myimage/tags/list
```

Verified response:
```json
{"name":"myimage","tags":["1"]}
```

## 6. Image Retrieval Test

Commands:
```bash
sudo docker rmi localhost:5000/myimage:1 alpine:3.20
sudo docker pull localhost:5000/myimage:1
sudo docker images localhost:5000/myimage
```

Result: Image was successfully pulled again from the private registry.

## 7. Container Execution Test

Command:
```bash
sudo docker run --rm localhost:5000/myimage:1 echo "hello from my private registry"
```

Verified output:
```text
hello from my private registry
```

## 8. Cleanup Verification

Commands:
```bash
sudo docker rm -f myregistry
sudo docker rmi localhost:5000/myimage:1
sudo docker ps -a --filter name=myregistry
sudo docker images localhost:5000/myimage
```

Result: Temporary registry container and tagged image were removed.

## 9. LMS Evaluation

- Lab: 29 – Pushing Images to a Private Registry
- Evaluator: Al Baari
- Score: 100/100
- Status: Passed
