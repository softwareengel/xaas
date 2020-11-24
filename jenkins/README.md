# jenkins


    java -version
    sudo apt-get install openjdk-11-jdk

    wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

    sudo apt-get update
    sudo apt-get install jenkins

    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

    sudo service jenkins start
    sudo service jenkins stop
    sudo service jenkins status


# Links 

https://developer-blog.net/raspberry-pi-als-jenkins-server/ 
