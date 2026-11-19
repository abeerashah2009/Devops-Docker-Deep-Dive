# Lab 29 – Pushing Images to a Private Registry

## 1. Lab Overview

**Topic:** Pushing Images to a Private Registry
**Platform:** Ubuntu 24.04 LTS
**Tool:** Docker
**Registry Image:** registry:2.8.3
**Test Image:** alpine:3.20
**Registry Address:** localhost:5000
**LMS Score:** 100/100
**Status:** Passed

## 2. Objective

The objective of this lab was to learn how to:

- Set up a private Docker registry.
- Pull an image from Docker Hub.
- Tag an image for a private registry.
- Push an image to the private registry.
- Verify repositories and image tags.
- Pull the image back from the private registry.
- Run the retrieved image.
- Clean up Docker resources.

## 3. Download Registry Image

```bash
sudo docker pull registry:2.8.3
sudo docker images registry
```

The registry image downloaded successfully.

## 4. Start Private Registry

```bash
sudo docker run -d -p 5000:5000 --name myregistry registry:2.8.3
```

Verify the registry:

```bash
sudo docker ps --filter name=myregistry
curl -s http://localhost:5000/v2/
```

**Verified API response:**

```text
{}
```

## 5. Pull Alpine Image

```bash
sudo docker pull alpine:3.20
sudo docker images alpine
```

The Alpine image downloaded successfully.

## 6. Tag Image for Private Registry

```bash
sudo docker tag alpine:3.20 localhost:5000/myimage:1
sudo docker images localhost:5000/myimage
```

The image was tagged successfully.

**Image tag:**

`localhost:5000/myimage:1`

## 7. Push Image to Private Registry

```bash
sudo docker push localhost:5000/myimage:1
```

The image layer was pushed successfully.

## 8. Verify Registry Repository and Tags

Check the repository:

```bash
curl -s http://localhost:5000/v2/_catalog
```

**Verified output:**

```json
{"repositories":["myimage"]}
```

Check the image tags:

```bash
curl -s http://localhost:5000/v2/myimage/tags/list
```

**Verified output:**

```json
{"name":"myimage","tags":["1"]}
```

## 9. Pull Image from Private Registry

To verify image retrieval, the local image copies were removed:

```bash
sudo docker rmi localhost:5000/myimage:1 alpine:3.20
```

Then the image was pulled again:

```bash
sudo docker pull localhost:5000/myimage:1
sudo docker images localhost:5000/myimage
```

The image was successfully downloaded from the private registry.

## 10. Run Retrieved Image

```bash
sudo docker run --rm localhost:5000/myimage:1 echo "hello from my private registry"
```

**Verified output:**

```text
hello from my private registry
```

## 11. Cleanup

Remove the temporary registry container:

```bash
sudo docker rm -f myregistry
```

Remove the retrieved image:

```bash
sudo docker rmi localhost:5000/myimage:1
```

Final verification confirmed that the registry container and tagged image were removed.

**Note:** The temporary registry container was removed after testing. Its stored registry data was not retained.

## 12. Skills Learned

- Docker private registry setup.
- Docker image tagging.
- Docker image pushing and pulling.
- Registry API verification.
- Docker image management.
- Container cleanup.

## 13. LMS Result

**Final Score: 100/100**

**Evaluation:** Al Baari
**Result:** Lab Passed

All practical tasks were completed and verified successfully.
