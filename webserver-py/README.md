# Simple Webserver in Python 

For testing ports and requests 

    docker build --pull --rm -f "xaas/webserver-py/Dockerfile" -t pi:latest "xaas/webserver-py

    docker-compose -f "xaas/webserver-py/docker-compose.yml" up -d --build
