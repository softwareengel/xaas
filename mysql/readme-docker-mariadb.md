
# Docker MariaDB

https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/

    docker search mariadb

<https://peppe8o.com/create-a-custom-mariadb-container-with-raspberry-pi-and-docker/>

<https://github.com/ernestgwilsonii/docker-raspberry-pi-mariadb>

# History 

    1  mc
    2  ls -al 
    3  cd SanDiskSecureAccess/
    4  ls -al 
    5  exit
    6  docker run hello-world
    7  sudo apt-get install -y libffi-dev libssl-dev
    8  sudo apt-get install -y python3 python3-pip
    9  sudo apt-get upgraad
   10  sudo apt-get upgrade 
   11  spt-get install xrdp 
   12  sudo apt-get install xrdp 
   13  sudp apt-get install docker
   14  sudo apt-get install docker
   15  curl -sSL https://get.docker.com | sh
   16  sudo usermod -aG docker pi
   17  sudo usermod -aG docker $USER
   18  newgrp docker 
   19  ls 
   20  ls /dev/sda
   21  ls /dev/sda1
   22  cd /media/
   23  ls
   24  cd pi/
   25  ls 
   26  cd B472-156E/
   27  cd raspi/
   28  ls
   29  ls -al 
   30  history 
   31  lsusb 
   32  sudo apt-get install gparted
   33  gparted 
   34  exit
   35  git clone https://github.com/softwareengel/xaas.git
   36  sudo apt-get install -y libffi-dev libssl-de
   37  sudo apt-get install -y python3 python3-pip
   38  sudo apt-get remove python-configparser
   39  sudo pip3 -v install docker-compose
   40  sudo apt-get update
   41  git config --global user.email "pi51@sse.de"
   42  git config --global user.name "pi51"
   43  sudo apt-get update
   44  curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
   45  sudo apt-get install -y libffi-dev libssl-de
   46  sudo apt-get install -y python3 python3-pip
   47  sudo apt-get remove python-configparser
   48  sudo pip3 -v install docker-compose
   49  cd /
   50  ls -al 
   51  nginx
   52  sudo apt-get install nginx
   53  exit
   54  npm -v
   55  node -v
   56  sudo apt-get install dotnet5
   57  sudo apt-get update 
   58  sudo apt-get upgrade
   59  sudo apt-get install -y apt-transport-https
   60  sudo apt-get install -y aspnetcore-runtime-5.0
   61  wget https://packages.microsoft.com/config/ubuntu/20.10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
   62  sudo dpkg -i packages-microsoft-prod.deb
   63  sudo apt-get update;   sudo apt-get install -y apt-transport-https &&   sudo apt-get update &&   sudo apt-get install -y aspnetcore-runtime-5.0
   64  sudo apt-get install -y dotnet-runtime-5.0
   65  sudo apt-get update;   sudo apt-get install -y apt-transport-https &&   sudo apt-get update &&   sudo apt-get install -y aspnetcore-runtime-5.0
   66  wget https://dot.net/v1/dotnet-install.sh
   67  chmod +x dotnet-install.sh 
   68  ./dotnet-install.sh -c 5.0 --runtime aspnetcore
   69  dotnet
   70  .dotnet/dotnet 
   71  .dotnet/dotnet -info
   72  .dotnet/dotnet --info
   73  cd src
   74  ls
   75  unzip net5.0.zip 
   76  dir
   77  cd net5.0/
   78  dir
   79  ~/.dotnet/dotnet 
   80  ~/.dotnet/dotnet Serene2.Web.dll 
   81  ~/.dotnet/dotnet ./Serene2.Web.dll 
   82  cd publish/
   83  dir *.dll
   84  ~/.dotnet/dotnet ./Serene2.Web.dll 
   85  cd ..
   86  cd ~
   87  cd pu
   88  cd src/
   89  cd publish/
   90  dir
   91  dotnet Serene9.Web.dll 
   92  ~/.dotnet/dotnet Serene9.Web.dll 
   93  ~/.dotnet/dotnet 
   94  ~/.dotnet/dotnet ./Serene9.Web.Dll
   95  cd ..
   96  ~/.dotnet/dotnet publish/Serene9.Web.Dll
   97  cd publish/
   98  ~/.dotnet/dotnet ./Serene9.Web.Dll
   99  exit
  100  cd src/
  101  cd publish/
  102  dir
  103  ~/.dotnet/dotnet 
  104  ~/.dotnet/dotnet Serene9.Web.dll 
  105  sudo apt-get update
  106  curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
  107  sudo usermod -aG docker pi
  108  sudo apt-get install -y libffi-dev libssl-de
  109  exit
  110  dir
  111  cd src/
  112  dir
  113  cd ..
  114  ls -al 
  115  .dotnet/dotnet 
  116  .dotnet/dotnet ./src/publish/Serene9.Web.dll 
  117  cd src/publish/
  118  ~/.dotnet/dotnet ./Serene9.Web.dll 
  119  sudo usermod -aG docker pi
  120  sudo apt-get install -y libffi-dev libssl-de
  121  sudo apt-get upgrade
  122  sudo usermod -aG docker pi
  123  sudo apt-get install -y libffi-dev libssl-de
  124  sudo apt-get remove python-configparser
  125  sudo apt autoremove
  126  sudo pip3 -v install docker-compose
  127  cd ..
  128  ~/.dotnet/dotnet Serene9.Web.dll 
  129  cd src/publish/
  130  ~/.dotnet/dotnet Serene9.Web.dll 
  131  docker search mariadb
  132  docker run --port 127.0.0.1:3306:3306  --name some-mariadb -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb:tag
  133  cd ..
  134  cd xaas/
  135  cd mysql/
  136  mkdir /opt/docker-compose && cd /opt/docker-compose
  137  mkdir /docker-compose && cd /docker-compose
  138  mkdir dompose2
  139  cd dompose2/
  140  git clone https://github.com/ernestgwilsonii/docker-raspberry-pi-mariadb.git
  141  cd docker-raspberry-pi-mariadb
  142  time docker build --no-cache -t ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37 -f Dockerfile.armhf .
  143  docker run --name mysql -it -e MYSQL_ROOT_PASSWORD=SetThisToSomethingStrong! -p 3306:3306 ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37
  144  sudo docker run --name mysql -it -e MYSQL_ROOT_PASSWORD=SetThisToSomethingStrong! -p 3306:3306 ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37
  145  sudo docker build --pull --rm -f "mysql/Dockerfile" -t xaas-mariadb:latest "mysql"
  146  docker build --pull --rm -f "mysql/Dockerfile" -t xaas-mariadb:latest "mysql"
  147  cd ..
  148  sudo docker build --pull --rm -f "mysql/Dockerfile" -t xaas-mariadb:latest "mysql"
  149  cd ..
  150  sudo docker build --pull --rm -f "mysql/Dockerfile" -t xaas-mariadb:latest "mysql"
  151  cd ..
  152  ls
  153  curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
  154  sudo docker run hello-world
  155  sudo reboot now
  156  docker ps
  157  docker exec -it $(docker ps | grep mysql | awk '{print $1}') bash
  158  exit
  159  docker stop mysql && docker rm mysql
  160  docker stop mysql2 && docker rm mysql2
  161  cd mysql/
  162  cd dompose2/
  163  docker run --name mysql -it -e MYSQL_ROOT_PASSWORD=SetThisToSomethingStrong! -p 3306:3306 ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37
  164  docker run --name mysql -it -e MYSQL_ROOT_PASSWORD=p -p 3306:3306 ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37
  165  docker run --name mysql2 -it -e MYSQL_ROOT_PASSWORD=SetThisToSomethingStrong! -p 3306:3306 ernestgwilsonii/docker-raspberry-pi-mariadb:10.1.37
  166  history
  