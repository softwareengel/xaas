# Grafana Raspi Docker 


## stmp info 

docker run \
  -d \
  -p 3000:3000 \
  --name grafana \
  -e "GF_SMTP_ENABLED=true" \
  -e "GF_SMTP_HOST=smtp.example.com" \
  -e "GF_SMTP_USER=myuser" \
  -e "GF_SMTP_PASSWORD=mysecret" \
  grafana/grafana:5.1.0

Links:

- grafana docker raspi 
https://grafana.com/docs/grafana/latest/installation/docker/

- install grafana monitor for raspi 

https://grafana.com/blog/2021/01/26/how-to-connect-and-monitor-your-raspberry-pi-with-grafana-cloud/
## REset Password Docker Grafana 

    docker ps
    docker exec -it c16ae5b49cd4 grafana-cli admin reset-admin-password p12345

Links:

https://sleeplessbeastie.eu/2019/12/11/how-to-reset-admin-password-in-grafana-container/

# Links


