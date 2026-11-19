# Lab 17 – Docker Compose Web + Database Stack

## 1. Lab Overview

**Objective:** Deploy an Nginx web server and MySQL database using Docker Compose.

**LMS Result:** 100 / 100 — Passed

This lab demonstrates:
- Docker Compose multi-container applications
- Web and database services
- Environment variables and secret protection
- MySQL health checks
- Service dependency management
- Persistent Docker volumes
- Container network connectivity

## 2. Environment

| Component | Version / Configuration |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Docker Engine | 29.9.0 |
| Docker Compose | v5.6.0 |
| Web Image | nginx:1.27-alpine |
| Database Image | mysql:8.4 |
| Database | exampledb |
| Web Port | 8080 |
| Database Port | 3306 |

## 3. Project Structure

```text
Lab-17-Docker-Compose-Web-DB-Stack/
├── .gitignore
├── docker-compose.yml
└── README.md
```

The `.env` file is created locally but excluded from Git because it contains the MySQL root password.

## 4. Supporting Tools

Installed or verified the required tools:

```bash
sudo apt update
sudo apt install -y ca-certificates curl jq openssl

jq --version
openssl version
```

## 5. Environment Variable and Password

Generated a random MySQL root password:

```bash
openssl rand -hex 16
```

Created the `.env` file:

```bash
echo "MYSQL_ROOT_PASSWORD=$(openssl rand -hex 16)" > .env
chmod 600 .env
```

Verified permissions and password length without displaying the secret:

```bash
ls -l .env
awk -F= '{print "Password length:", length($2)}' .env
```

Verified that Git ignores the secret:

```bash
git check-ignore .env
```

Expected result:

```text
.env
```

## 6. Docker Compose Configuration

Created `docker-compose.yml`:

```yaml
services:
  web:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mysql:8.4
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: exampledb
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h localhost -uroot -p$$MYSQL_ROOT_PASSWORD"]
      interval: 5s
      timeout: 5s
      retries: 20

volumes:
  db_data:
```

### Important concepts

- `web`: Runs the Nginx web server.
- `db`: Runs the MySQL database.
- `depends_on`: Makes the web service wait until the database is healthy.
- `healthcheck`: Checks MySQL readiness.
- `db_data`: Stores persistent database data.
- `${MYSQL_ROOT_PASSWORD}`: Reads the password from `.env`.

## 7. Validate Configuration

```bash
sudo docker compose config --quiet
sudo docker compose config --services
```

Verified:
- Compose configuration was valid.
- Both `db` and `web` services were listed.

## 8. Start Services

Used the project name `web-db-stack` to create the expected network name:

```bash
sudo docker compose -p web-db-stack up -d --wait
```

Checked running containers:

```bash
sudo docker compose -p web-db-stack ps
```

Both containers started successfully. The MySQL container reported `healthy`.

## 9. Verify Container Health

```bash
sudo docker compose -p web-db-stack ps --format json
```

Verified:
- MySQL: running and healthy.
- Nginx: running.

## 10. Test the Web Server

```bash
curl -sI http://localhost:8080 | head -1
```

Verified output:

```text
HTTP/1.1 200 OK
```

This confirmed that Nginx was serving HTTP requests successfully.

## 11. Verify MySQL Database

```bash
sudo docker compose -p web-db-stack exec -T db sh -c \
'MYSQL_PWD=$MYSQL_ROOT_PASSWORD mysql -uroot -e "SHOW DATABASES;"'
```

Verified databases included:

```text
exampledb
information_schema
mysql
performance_schema
sys
```

Confirmed the required database:

```bash
sudo docker compose -p web-db-stack exec -T db sh -c \
'MYSQL_PWD=$MYSQL_ROOT_PASSWORD mysql -uroot -e "SHOW DATABASES;"' | grep exampledb
```

Verified output:

```text
exampledb
```

## 12. Test Container Network Connectivity

```bash
sudo docker run --rm \
--network web-db-stack_default \
busybox:1.36 nc -zv db 3306
```

Verified output:

```text
db (172.18.0.2:3306) open
```

This confirmed that the database was reachable through the Docker Compose network.

## 13. Cleanup

Stopped and removed containers and the Compose network:

```bash
sudo docker compose -p web-db-stack down
```

The `-v` option was intentionally not used because the database volume needed to be retained.

Verified the volume:

```bash
sudo docker volume ls | grep web-db-stack_db_data
```

Verified output:

```text
local     web-db-stack_db_data
```

Also verified:

```bash
sudo systemctl is-active docker
```

Result:

```text
active
```

## 14. LMS Result

**Lab 17 – Docker Compose for a Web + DB Stack**

**Final Score: 100 / 100**

**Status: PASSED**

Evaluated by Al Baari.

## 15. Skills Practiced

- Docker Compose
- Nginx container deployment
- MySQL container deployment
- Environment variable configuration
- Secret file permissions
- Docker health checks
- Service dependency management
- Named volumes and persistent storage
- Docker networking
- Container connectivity testing
- Application cleanup

**Conclusion:** Successfully deployed and tested a multi-container web and database application using Docker Compose. Verified HTTP access, MySQL database creation, container health, network connectivity, and persistent volume retention.
