# Portainer Raspi Docker

```bash
    sudo apt update
    sudo apt upgrade 
    sudo docker pull portainer/portainer-ce:linux-arm
    sudo docker run --restart always -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:linux-arm
```


# reset password 

https://docs.portainer.io/v/ce-2.9/advanced/reset-admin
```bash
# stop the existing Portainer container
docker container stop portainer

# run the helper using the same bind-mount/volume for the data volume
docker run --rm -v portainer_data:/data portainer/helper-reset-password
2020/06/04 00:13:58 Password succesfully updated for user: admin
2020/06/04 00:13:58 Use the following password to login: &_4#\3^5V8vLTd)E"NWiJBs26G*9HPl1

# restart portainer and use the password above to login
docker container start portainer
```
# von syno 
```
docker run -d --name=portainer \
-p 8000:8000 \
-p 9000:9000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /volume1/docker/portainer:/data \
--restart=always \
portainer/portainer-ce
```

# reset admin oassword 

    docker stop "id-portainer-container"
    docker run --rm -v portainer_data:/data portainer/helper-reset-password

* Links:

https://docs.portainer.io/v/ce-2.9/advanced/reset-admin

# Agent
