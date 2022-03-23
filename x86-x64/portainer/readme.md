# portainer docker 

```bash
    docker run -d --name=portainer \
    -p 8000:8000 \
    -p 9000:9000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /volume1/docker/portainer:/data \
    --restart=always \
    portainer/portainer-ce
```

## History 
```
    1  sudo apt-get update 
    2  sudo apt-get upgrade
    3  ip
    4  ip addr
    5  ls
    6  top
    7  sudo apt update
    8  sudo apt install apt-transport-https ca-certificates curl software-properties-common
    9  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   10  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
   11  sudo apt update
   12  apt-cache policy docker-ce
   13  sudo apt install docker-ce
   14  apt-cache policy docker-ce
   15  sudo systemctl status docker
   16  sudo reboot now
   17  sudo usermod -aG docker $sse
   18  su - $sse
   19  sudo usermod -aG docker username
   20  sudo usermod -aG docker $docker
   21  sudo usermod -aG docker $sse
   22  sudo reboot now
   23  sudo groupadd docker
   24  sudo usermod -aG docker $USER
   25  newgrp docker
   26  sudo reboot now 
   27  git
   28  git clone https://github.com/softwareengel/xaas.git
   29  ip addr
   30  lsof -i
   31  lsof 
   32  ip addr
   33  docker run -d --name=grafana -p 3000:3000 grafana/grafana:7.4.3
   34  exit
   35  df -h
   36  df 
   37  top
   38  htop
   39  ntop
   40  top
   41  df -h
   42  df 
   43  df -h
   44  docker ps
   45  history 
```