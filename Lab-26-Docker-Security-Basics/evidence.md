# Lab 26 – Evidence

## LMS Evaluation

- Lab: Docker Security Basics
- Score: 100 / 100
- Status: Passed
- Evaluator: Al Baari

## Practical Evidence

1. **Non-root user:** Container output showed `Running as user: appuser`.
2. **Linux capabilities:** `CapEff` became `0000000000000000` after dropping all capabilities.
3. **CHOWN capability:** Ownership change failed without the capability and succeeded after adding `CHOWN`.
4. **Network isolation:** Internal network test returned `Network unreachable`, exit code 1.
5. **Read-only filesystem:** Write attempt failed with `Read-only file system`.
6. **No new privileges:** Output showed `NoNewPrivs: 1`.
7. **Resource limits:** Docker inspection showed `mem=268435456 pids=64`.
8. **Memory limit:** Test process exited with code 137.
9. **Docker Bench Security:** Version `v1.6.0` was cloned and the audit was started. Initial host warnings and image lookup errors were observed.

## Cleanup

- Removed the temporary internal network.
- Removed the resource-limited test container.

## Final Result

**100 / 100 — Lab Passed**
