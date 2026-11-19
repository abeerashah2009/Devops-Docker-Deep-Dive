# Lab 23 - Evidence

## Environment
- Ubuntu 24.04 LTS
- Docker 29.10.0

## Alpine Verification
- Base image: alpine:3.20
- Image: my-alpine-image
- Curl version: 8.14.1
- Image size: 23,802,979 bytes
- Status: Passed

## Ubuntu Verification
- Base image: ubuntu:24.04
- Image: my-ubuntu-image
- Curl version: 8.5.0
- Image size: 130,684,776 bytes
- Status: Passed

## Image Comparison
- Alpine: 23.8 MB
- Ubuntu: 131 MB
- Alpine is approximately 5.49 times smaller.

## Cleanup
- my-alpine-image: Removed
- my-ubuntu-image: Removed
- Verified using docker images.

## LMS Evaluation
- Status: Passed
- Score: 100 / 100
