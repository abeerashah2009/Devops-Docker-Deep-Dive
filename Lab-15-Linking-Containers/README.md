# Lab 15: Linking Containers

## 1. Objectives

- Understand Docker container linking.
- Connect containers using the `--link` flag.
- Compare legacy links with user-defined bridge networks.
- Understand why Docker networks are recommended.

## 2. Environment

- Operating System: Ubuntu 24.04.5 LTS
- Docker Engine: 29.9.0
- Web Server Image: `httpd:2.4`
- Database Image: `mysql:8.4`
- Test Client Image: `alpine:3.20`

## 3. Docker Verification

Verified Docker installation and service:

```bash
sudo docker --version
sudo systemctl is-active docker
sudo docker run --rm hello-world
```

**Results:**
- Docker version 29.9.0
- Docker service: active
- Hello World test: successful

## 4. Task 1 — Linking Containers with --link

### 4.1 Pull Required Images

```bash
sudo docker pull httpd:2.4
sudo docker pull mysql:8.4
```

Both images downloaded successfully.

### 4.2 Start MySQL Container

```bash
sudo docker run --name mydb \
-e MYSQL_ROOT_PASSWORD=my-secret-pw \
-d mysql:8.4
```

Waited until MySQL was ready:

```bash
until sudo docker exec mydb mysqladmin ping -uroot -pmy-secret-pw --silent; do
    sleep 2
done
```

**Result:** MySQL initialized successfully.

### 4.3 Start Apache with a Link

```bash
sudo docker run --name myweb \
--link mydb:mysql \
-d httpd:2.4
```

Docker displayed a warning that links on the default bridge network are deprecated.

### 4.4 Verify the Link

```bash
sudo docker exec myweb cat /etc/hosts | grep mysql
sudo docker exec myweb getent hosts mysql
```

**Verified result:**

```text
172.17.0.2 mysql <container-id> mydb
172.17.0.2 mysql
```

The IP address may differ between environments.

### 4.5 Verify One-Way Communication

```bash
sudo docker exec mydb cat /etc/hosts | grep -c myweb
```

**Output:**

```text
0
```

The database container did not have a `myweb` entry. This demonstrated the one-way nature of the legacy link.

### 4.6 Remove Linked Containers

```bash
sudo docker rm -f myweb mydb
```

Both containers were removed successfully.

## 5. Task 2 — User-Defined Bridge Network

### 5.1 Create a Network

```bash
sudo docker network create mynetwork
```

Verify its configuration:

```bash
sudo docker network inspect mynetwork \
--format 'Name={{.Name}} Driver={{.Driver}} Scope={{.Scope}}'
```

**Verified result:**

```text
Name=mynetwork Driver=bridge Scope=local
```

### 5.2 Start Containers on the Network

Start MySQL:

```bash
sudo docker run --name mydb \
--network mynetwork \
-e MYSQL_ROOT_PASSWORD=my-secret-pw \
-d mysql:8.4
```

Start Apache:

```bash
sudo docker run --name myweb \
--network mynetwork \
-d httpd:2.4
```

Wait for MySQL initialization:

```bash
until sudo docker exec mydb mysqladmin ping -uroot -pmy-secret-pw --silent; do
    sleep 2
done
```

**Result:** MySQL was ready.

### 5.3 Verify DNS in Both Directions

From Apache to MySQL:

```bash
sudo docker exec myweb getent hosts mydb
```

Verified result:

```text
172.18.0.2 mydb
```

From MySQL to Apache:

```bash
sudo docker exec mydb getent hosts myweb
```

Verified result:

```text
172.18.0.3 myweb
```

The IP addresses may differ between environments.

### 5.4 Verify Network Membership

```bash
sudo docker network inspect mynetwork \
--format '{{range .Containers}}{{.Name}} {{end}}'
```

**Verified result:** Both `myweb` and `mydb` were attached to `mynetwork`.

### 5.5 Test Connectivity with Alpine

```bash
sudo docker run --rm --network mynetwork alpine:3.20 \
ping -c 2 mydb
```

**Verified result:**

```text
2 packets transmitted, 2 packets received, 0% packet loss
```

The temporary Alpine container successfully reached MySQL.

## 6. Task 3 — Drawbacks of Container Linking

1. **Legacy feature:** The `--link` feature is deprecated and Docker recommends user-defined networks.
2. **Limited flexibility:** Legacy links work on the default bridge network.
3. **One-way communication:** The linked container receives the alias, but the target container does not automatically receive a matching entry.
4. **Scalability:** User-defined networks provide automatic DNS resolution and make service communication easier to manage.
5. **Better connectivity:** Containers on the same user-defined network can resolve one another by container name.

## 7. Cleanup

Remove both containers:

```bash
sudo docker rm -f myweb mydb
```

Remove the custom network:

```bash
sudo docker network rm mynetwork
```

Verify cleanup:

```bash
sudo docker ps -a --format '{{.Names}}'
sudo docker network ls --filter name=mynetwork
sudo systemctl is-active docker
```

**Verified results:**
- No lab containers remained.
- `mynetwork` was removed.
- Docker service remained active.

## 8. Key Learnings

- Learned how to connect containers using Docker's legacy `--link` flag.
- Verified the linked container's hostname alias using `/etc/hosts` and `getent`.
- Observed that legacy linking provides one-way host entry configuration.
- Created a user-defined bridge network.
- Verified automatic DNS resolution in both directions.
- Tested container connectivity using Alpine.
- Understood why user-defined networks are recommended over legacy links.

## 9. LMS Evaluation

- Lab Status: **PASSED**
- Final Score: **100/100**
- Evaluation: Successful

**Lab 15 — Linking Containers completed successfully.**
