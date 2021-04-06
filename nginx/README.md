# Nginx Reverse Proxy 
    


## docker.nginx.service 

    pi@raspberrypi:~ $ sudo cat /etc/systemd/system/docker.nginx.service 



    [Unit]
    Description=Docker Nginx Server
    # After=network.target
    # After=syslog.target
    Requires=docker.service
    After=docker.service

    [Service]
    Type=oneshot
    WorkingDirectory=/home/pi
    RemainAfterExit=yes
    # ExecStart=/home/pi/orientdb/orientdb-tp3-3.1.6/bin/server.sh 
    ExecStart=/usr/local/bin/docker-compose -f "/home/pi/xaas/nginx/docker-compose.yml" up -d --build
    # ExecStart=/usr/local/bin/docker-compose -f "/home/pi/xaas/nginx/docker-compose.yml" up -d 
    # ExecStart=/usr/local/bin/docker-compose up -d 
    ExecStop=/usr/local/bin/docker-compose -f "/home/pi/xaas/nginx/docker-compose.yml" down
    # ExecStop=/usr/local/bin/docker-compose down
    # User=pi
    TimeoutStartSec=0

    [Install]
    WantedBy=multi-user.target

## cmds 

    sudo cp docker.nginx.service /etc/systemd/system 
    sudo systemctl start docker.nginx.service
    sudo systemctl enable docker.nginx.service
    sudo systemctl daemon-reload

# Links

https://www.domysee.com/blogposts/reverse-proxy-nginx-docker-compose

https://stackoverflow.com/questions/43671482/how-to-run-docker-compose-up-d-at-system-start-up 

https://mehmandarov.com/start-docker-containers-automatically/ 

https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/
