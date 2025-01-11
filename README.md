# Docker imajını build almak için aşağıdaki komutu kullanabilirsiniz:

```bash
docker build -t endgame-app .


# Docker imajını çalıştırmak için aşağıdaki komutu kullanın:

docker run -p 5000:5000 --name endgame-app-container --network host endgame-app



# Docker container'ınızın çalıştığını doğrulamak için aşağıdaki komutu kullanın:

docker ps -a


# Docker container'ınızı istediğiniz port üzerinden çalıştırmak için:

docker run -p 5000:5000 --name endgame-app-container endgame-app



