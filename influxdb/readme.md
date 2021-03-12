# raspi docker influx

    docker run --rm influxdb:1.8 influxd config > influxdb.conf

    sed -i 's/^  auth-enabled = false$/  auth-enabled = true/g' influxdb.conf
    docker run --rm telegraf telegraf config > telegraf.conf

''' 
    docker run --rm telegraf telegraf config > telegraf.conf
# now modify it to tell it how to authenticate against influxdb
    sed -i 's/^  # urls = \["http:\/\/127\.0\.0\.1:8086"\]$/  urls = \["http:\/\/influxdb:8086"\]/g' telegraf.conf
    sed -i 's/^  # database = "telegraf"$/  database = "telegraf"/' telegraf.conf
    sed -i 's/^  # username = "telegraf"$/  username = "telegraf"/' telegraf.conf
    sed -i 's/^  # password = "metricsmetricsmetricsmetrics"$/  password = "p"/' telegraf.conf
# as we run inside docker, the telegraf hostname is different from our Raspberry hostname, let's change it
    sed -i 's/^  hostname = ""$/  hostname = "'${HOSTNAME}'"/' telegraf.conf
''' 

''' 
    docker exec -it influxdb influx
    > auth
    username: engels
    password: 

    create database telegraf
    create user telegraf with password 'p'
    grant write on telegraf to telegraf
''' 

SELECT mean("usage_system") AS "mean_usage_system", mean("usage_user") AS "mean_usage_user", mean("usage_iowait") AS "mean_usage_iowait", mean("usage_idle") AS "mean_usage_idle" FROM "telegraf"."autogen"."cpu" WHERE time > :dashboardTime: AND time < :upperDashboardTime: AND "cpu"='cpu-total' GROUP BY time(:interval:) FILL(null)

# Links

https://blog.anoff.io/2020-12-run-influx-on-raspi-docker-compose/
