### MYSQL DOCKER

```bash
docker pull mysql:latest
```

```bash
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=strong_password -d mysql
```

exec into the container

```bash
docker exec -it mysql3 mysql -u root -p
```

By default you wont be able to connect if you are not a root user, so we will update the mysql user table.

```bash
SELECT User, Host FROM mysql.user;
```

Replace the ip with your machines ip, this will create a new user with user mysql and respectice password with all the permissions, only for the given ip address. If you want to give access to all replace ip address with "%"

```bash
CREATE USER 'mysql'@'192.168.65.1' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'192.168.65.1';
FLUSH PRIVILEGES;
```
