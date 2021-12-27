# pgsql on raspi 

## Working: 
$ docker run --name mypostgres -e POSTGRES_PASSWORD=p -d  -p 5432:5432 arm32v7/postgres

## test


``` dockerfile 
    FROM postgres:12

    LABEL maintainer="PostGIS Project - https://postgis.net"

    ENV POSTGIS_MAJOR 3
    ENV POSTGIS_VERSION 3.0.0+dfsg-2~exp1.pgdg100+1

    RUN apt-get update \
        && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
        && apt-get install -y --no-install-recommends \
            postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
            postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts=$POSTGIS_VERSION \
        && rm -rf /var/lib/apt/lists/*

    RUN mkdir -p /docker-entrypoint-initdb.d
    COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh
    COPY ./update-postgis.sh /usr/local/bin
```
docker run -d \
    --name some-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    arm32v7/postgres


docker run --platform linux/arm/v7 --name some-postgis -e POSTGRES_PASSWORD=p -d postgis/postgis -p 5432:5432 


docker run --name some-postgis -e POSTGRES_PASSWORD=mysecretpassword -d postgis/postgis
docker run -d \       
--name some-postgres \
-e POSTGRES_PASSWORD=mypassword \
-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
-p 5432:5432 \
postgres
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm/v7) and no specific platform was requested

linux/arm/v7 


# Links
https://hub.docker.com/r/arm32v7/postgres/

https://github.com/postgis/docker-postgis

https://hub.docker.com/r/tobi312/rpi-postgresql-postgis/


