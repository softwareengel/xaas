#!/bin/bash
sudo raspi-config --expand-rootfs
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoclean

curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker pi
sudo apt-get install -y libffi-dev libssl-de
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose



