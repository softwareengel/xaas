# Prometheus TSDB

e.g. for Logging nginx (?) only numerical data

##

    sudo apt update

    docker run -p 9090:9090 prom/prometheus

    docker run -d -p 9090:9090 --name prom -v /home/pi/xaas/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

Arm7 (Raspi 3,4) , Arm 6 (Raspi 1,2)

    wget https://github.com/prometheus/node_exporter/releases/download/v1.2.2/node_exporter-1.2.2.linux-armv7.tar.gz

    tar xfz node_exporter-1.2.2.linux-armv7.tar.gz 

    mv node_exporter-1.2.2.linux-armv7 node_exporter

    sudo nano /etc/systemd/system/node_exporter.service

```

[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=pi
ExecStart=/home/pi/xaas/prometheus/node_exporter/node_exporter

[Install]
WantedBy=default.target
```

    sudo systemctl daemon-reload  

    sudo systemctl start node_exporter

    sudo systemctl enable node_exporter 

    sudo systemctl status node_exporter


## Links

https://pimylifeup.com/raspberry-pi-prometheus/

https://ducko.uk/installing-grafana-prometheus-via-docker-to-monitor-raspberry-pi-metrics/
