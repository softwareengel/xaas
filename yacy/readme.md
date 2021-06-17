# yacy  - working 


    
## yacy/yacy_search_server:armv7-latest 

    docker run -d --name yacy -p 8090:8090 -p 8443:8443 -v yacy_data:/opt/yacy_search_server/DATA --log-opt max-size=200m --log-opt max-file=2 yacy/yacy_search_server:armv7-latest 

## Problem Heap Space 

    BusyThread Thread 'BusyThread Switchboard.dhtTransferJob' runs short memory cycle.

set values 

    http://localhost:8090/Performance_p.html
    http://localhost:8090/ConfigHTCache_p.html


## yacy 

    docker run -d --name yacy -p 8090:8090 -p 8443:8443 -v yacy_data:/opt/yacy_search_server/DATA --log-opt max-size=200m --log-opt max-file=2 yacy/yacy_search_server:latest

# compile 
    git clone https://github.com/yacy/yacy_search_server.git
    cd yacy_search_server
    ant clean all dist

# Links

https://yacy.net/download_installation/
https://github.com/yacy/yacy_search_server 
https://github.com/yacy/yacy_search_server/blob/master/docker/Readme.md 

