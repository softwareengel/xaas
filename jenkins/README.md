# jenkins on raspi working 

    java -version
    sudo apt-get install openjdk-11-jdk

    wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

    sudo apt-get update

    sudo apt-get install jenkins


    sudo service jenkins start
    sudo service jenkins stop
    sudo service jenkins status
    
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

    sudo apt-get install maven 

    mvn install -DskipTests 

## USB Stick 

- do not format stick  in FAT 
- use ext3 / ext4 as file format 


## USB Stick ... NOT WOrking 
    lsblk

/dev/sdc1 on /media/pi/B472-156E type vfat (rw,nosuid,nodev,relatime,sync,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,errors=remount-ro,uhelper=udisks2)
etc/fstab 
    # UUID=B472-156E /mnt/usb1  vfat defaults,auto,user,rw,umask=0000 0 0

    UUID=B472-156E    /mnt/usb1       vfat    defaults,auto,users,rw,nofail,noatime 0 0

Find user id 
    id -u pi

Find groups 
    pi@raspberrypi:~ $ id -G pi
    1000 4 20 24 27 29 44 46 60 100 105 109 999 998 997

In linux, e.g. ubuntu, you can add user jenkins to the root group:

    sudo usermod -a -G root jenkins

Then restart jenkins:

    sudo service jenkins restart

Be aware that, adding jenkins user to root group can make the user too powerful, use with caution


# NOT WORKING 
.bashrc

    export JENKINS_HOME="/mnt/usb1/jenkins"

Test

    echo "$JENKINS_HOME"

# Links 

https://developer-blog.net/raspberry-pi-als-jenkins-server/ 
