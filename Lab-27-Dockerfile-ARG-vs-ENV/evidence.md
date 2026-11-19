# Lab 27 – Evidence

## LMS Evaluation

- **Lab:** Dockerfile ARG vs ENV
- **Score:** 100 / 100
- **Status:** Passed
- **Evaluator:** Al Baari

## Practical Evidence

1. **Docker image build:** Successfully built `arg-env-demo` using `APP_VERSION=2.0.0`.
2. **Build-time ARG:** Build output showed `Building version 2.0.0`.
3. **Default ENV:** Application displayed `APP_ENV=production`.
4. **ARG runtime test:** Application displayed `APP_VERSION=None`.
5. **ENV override:** Application displayed `APP_ENV=dev` after using `docker run -e`.
6. **Image history:** Docker history displayed the APP_VERSION build argument.
7. **ARG-to-ENV test:** Updated Dockerfile persisted the build version using `APP_VERSION_BUILT`.
8. **Final application output:** Displayed `Application version built: 2.0.0`.

## Final Verified Output

```text
Application environment: production
Application version: None
Application version built: 2.0.0
```

## Final Result

**100 / 100 — Lab Passed**

Lab 27 practical tasks successfully completed and documented.
