# OrientDB 

# .service ohne Docker 
Als erstes muss eine .service Datei unter /etc/systemd/system angelegt werden

File: orientdb.service 
``` 
[Unit]
Description= OrientDB  Server
After=network.target
# After=syslog.target

[Service]
# ExecStart=/home/pi/orientdb/orientdb-tp3-3.1.6/bin/server.sh 
# ExecStop=/home/pi/orientdb/orientdb-tp3-3.1.6/bin/shutdown -p p
ExecStart=/home/pi/xaas/orientdb/orientdb-tp3-3.1.10/bin/server.sh 
ExecStop=/home/pi/xaas/orientdb/orientdb-tp3-3.1.10/bin/shutdown -p p
# User=pi


[Install]
WantedBy=multi-user.target
```

    sudo systemctl enable  orientdb.service
    sudo systemctl status orientdb.service
    sudo systemctl start orientdb.service
    sudo systemctl stop orientdb.service
    sudo systemctl disable orientdb.service

## OrientDB Docker - NOT WORKING

docker run -d --name orientdb -p 2424:2424 -p 2480:2480 -e ORIENTDB_ROOT_PASSWORD=rootpwd orientdb

## Error: 

```  
    pi@raspberrypi:~ $ docker run -d --name orientdb -p 2424:2424 -p 2480:2480 -e ORIENTDB_ROOT_PASSWORD=p orientdb
    Unable to find image 'orientdb:latest' locally
    latest: Pulling from library/orientdb
    docker: no matching manifest for linux/arm/v7 in the manifest list entries.
    See 'docker run --help'.
```
# Links 

https://orientdb.org/download 

## Version 3.1.10
wget https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.1.10/orientdb-tp3-3.1.10.zip 

## Version 3.1.6 
wget https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.1.6/orientdb-tp3-3.1.6.zip

## Version 3.2 (not tested)
https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.2.0/orientdb-tp3-3.2.0.zip 
