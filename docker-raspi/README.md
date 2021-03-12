# docker on raspi 

```bash 
    sudo apt-get update
    curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
    sudo usermod -aG docker pi
    sudo apt-get install -y libffi-dev libssl-de
    sudo apt-get install -y python3 python3-pip
    sudo apt-get remove python-configparser
    sudo pip3 -v install docker-compose
    
```
# Links
<https://blog.anoff.io/2020-12-install-docker-raspi/>