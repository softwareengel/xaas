# OrientDB 


docker run -d --name orientdb -p 2424:2424 -p 2480:2480 -e ORIENTDB_ROOT_PASSWORD=rootpwd orientdb

    pi@raspberrypi:~ $ docker run -d --name orientdb -p 2424:2424 -p 2480:2480 -e ORIENTDB_ROOT_PASSWORD=p orientdb
    Unable to find image 'orientdb:latest' locally
    latest: Pulling from library/orientdb
    docker: no matching manifest for linux/arm/v7 in the manifest list entries.
    See 'docker run --help'.