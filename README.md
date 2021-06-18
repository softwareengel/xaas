# xaas

## setup PI 

  sudo raspi-config --expand-rootfs
  
  sudo apt-get update
  
  sudo apt-get upgrade -y
  
  sudo apt-get autoclean

## git 

  https://github.com/softwareengel/xaas

  git config --global user.email "you@example.com"
  
  git config --global user.name "Your Name"

  git clone https://github.com/softwareengel/xaas

# docker 

https://maker-tutorials.com/docker-raspberry-pi-installieren-raspbian-debian-stretch-jessie/

  curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

## Test Docker RASPI

  sudo docker run hello-world

## change Container start option to restart 

docker update --restart=always <container>

# python webserver 

# jenkins 

# nginx reverse proxy 

  
##  usb drive 
sudo apt-get -y install ntfs-3g hfsutils hfsprogs exfat-fuse

  lsblk
  mount /dev/sda1 /media/usb

[1] https://jankarres.de/2013/01/raspberry-pi-usb-stick-und-usb-festplatte-einbinden/
[2] https://www.elektronik-kompendium.de/sites/raspberry-pi/1911271.htm
