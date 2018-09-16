#!/bin/bash

sudo yum -y update
sudo yum -y install httpd mod_ssl

sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload

sudo service httpd start
sudo service httpd status


echo "This is no longer a silly script" > /tmp/silly.txt

#commands found at 
#https://www.liquidweb.com/kb/how-to-install-apache-on-centos-7/