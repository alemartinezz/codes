# Ubuntu Server Configuration (AWS)

Linux Ubuntu Configuration Project hosted by AWS (Lightsail) as part of the Full-Stack Nanodegree Program.

You can access: 
- [http://18.218.248.76.xip.io](http://18.218.248.76.xip.io) OR
- [ec2-18-218-248-76.us-east-2.compute.amazonaws.com](ec2-18-218-248-76.us-east-2.compute.amazonaws.com)

for the deployed [Item catalog project](https://github.com/alemartinezz/law-app_udacity)

Port: 2200

## Create the Ubuntu Server

- Create a new [Amazon web Service account](https://aws.amazon.com/en/) and select a payment method.
- Create an instance of a new Ubuntu VM.
- Start running the server.
- Download the `server.pem` file (keys).
- If youre using windows, open *puttyGen*. Convert the **.pem** file to **ppk** format with the same filename.
- Open putty and load the converted file in the SSH - Auth section.
- Copy the provided address (instances section) of you AWS panel, to the Putty's address with an `ubuntu@` (user) before. It will look like this: ``ubuntu@ec2-18-218-248-76.us-east-2.compute.amazonaws.com``. Port 22 is ok for now.
- This should be enough to allow connection to the server.


# Security

## Updates

These commands will update all currently installed packages.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

Install unattended-upgrades
```
sudo apt-get install unattended-upgrades
```

Uncomment the line and save:
```
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades

{distro_id}:${distro_codename}-updates
```

Uncomment these lines
```
sudo nano /etc/apt/apt.conf.d/20auto-upgrades

APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";
```

Run
```
sudo unattended-upgrade -d
```

Activate
```
sudo dpkg-reconfigure --priority=low unattended-upgrades
```


## Install fall2ban

Install fall2ban and sendmail
```
sudo apt-get install fail2ban sendmail iptables-persistent
```

Create a copy file
```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

Change settings
```
sudo nano /etc/fail2ban/jail.local

set bantime = 600
destemail = useremail@domain
action = %(action_mwl)s 
port = ssh -> port = 2200
```

Restart service
```
sudo service fail2ban restart
```

## Only allow connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).

```
sudo ufw default deny incoming

sudo ufw default allow outgoing

sudo ufw allow 2200/tcp

sudo ufw allow www

sudo ufw allow 123/udp

sudo ufw deny 22

sudo ufw show added

sudo ufw enable

sudo ufw status
```

## Edit the sshd_config file.

Edit the file `sshd_config` with nano.
```
sudo nano /etc/ssh/sshd_config
```
Search for the line and uncomment it, change port from 22 to 2200. (Around line 13)
```
Port 2200
```

## Configure the instance on AWS page
After that, open the instances in the aws page and set:

- Custom TCP 2200
- Custom UDP 123
- HTTP 80

Now you can connect to the 2200 port.


# User Management

## Disable remote login of the root user.
Edit with nano /etc/ssh/sshd_config file
```
sudo nano /etc/ssh/sshd_config
```

find PermitRootLogin and change it to no (uncomment the line)
```
PermitRootLogin no
```

## Create a user `grader` and give sudo access.

Create the grader user.
```
sudo adduser grader

sudo usermod -aG sudo grader
```

Edit visudo file.
```
sudo visudo
```

Add the following line under root
```
root    ALL=(ALL:ALL) ALL
grader  ALL=(ALL:ALL) ALL
```

Confirm the sudo access running the commands
```
su grader

sudo -l
```

## Create an SSH keypair for grader user, using the ssh-keypair tool

In your **local machine**, into the .ssh folder, run the `ssh-keygen` command. Give it the name "grader_keys".

```
cd

cd .ssh

ssh-keygen
```

This will create two files: `grader_keys` and `grader_keys.pub`. Open the `grader_keys.pub` and copy the content.
```
cat grader_keys.pub
```

In the virtual machine, create a new file named `authorized_keys` as grader, under the /home/.ssh folder and paste the content generated.
```
su grader

sudo mkdir ~/.ssh

sudo nano ~/.ssh/authorized_keys

(paste the key generated)
```

Change the permissions.
```
sudo chmod 700 .ssh

sudo chmod 644 .ssh/authorized_keys
```

Edit file /etc/ssh/sshd_config and set password authentication to no.
```
PasswordAuthentication no
```

And then restart service ssh.
```
sudo service ssh restart
```

I am using windows, so I had to open PuttyGen and convert the generated file `grader_key` into ppk.

After that, open Putty and load the generated grader_key.ppk file and connect to port 2200 as grader:
```
grader@ec2-18-222-73-30.us-east-2.compute.amazonaws.com
```

Now you should be logged in as grader.


# Application Functionality


## Install Apache & PostgreSQL for serving the Python 3 app as a WSGI app.
```
sudo apt-get install apache2 libapache2-mod-wsgi
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt-get install python3-pip
sudo apt-get install postgresql
```

Install python app dependencies.
```
sudo pip3 install flask packaging google-api-python-client passlib flask-httpauth
sudo pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests
```

## Configure the Apache2 WSGI app to point to the Python app.

Install
```
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

Create folder and import inside it (That's for make the wsgi work).
```
sudo mkdir /var/www/catalog

cd /var/www/catalog

sudo git clone https://github.com/alemartinezz/law-app_udacity.git
```


**The WSGI path should not be with slashes, that's why I renamed the directory of the imported project**
```
sudo mv law-app_udacity LawAppUdacity
```

Change the name of the run file and edit the app variable
```
cd LawAppUdacity

sudo mv run.py __init__.py

sudo nano __init__.py

Change:
app.run(host="0.0.0.0", port=8000)
to:
app.run()
```

**Create the file catalog.wsgi:** (This should be located in the parent directoy of the project as shown)
```
sudo nano /var/www/catalog/catalog.wsgi
```

Paste the follwoing content:
```
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/")

from LawAppUdacity import app as application
application.secret_key = 'SUPER_SECRET_KEY'
```

**Create the VirtualHost file:**
```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Paste the following text:
```
<VirtualHost *:80>
    ServerName 18.222.73.30
    ServerAlias ec2-18-222-73-30.us-east-2.compute.amazonaws.com
    WSGIScriptAlias / /var/www/catalog/catalog.wsgi
    <Directory /var/www/catalog/LawAppUdacity/>
    	Order allow,deny
  	    Allow from all
        Options -Indexes
    </Directory>
    Alias /static /var/www/catalog/LawAppUdacity/static
    <Directory /var/www/catalog/LawAppUdacity/static/>
  	    Order allow,deny
  	    Allow from all
        Options -Indexes
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Enable virtual host: 
```
sudo a2ensite catalog
```

Disable default page:
```
sudo a2dissite 000-default.conf
```

Reload Apache:
```
sudo service apache2 reload
```

If you get problems, reinstall apache and delete `/etc/apache2/sites-enabled/000-default.conf` file :@
```
sudo apt-get --purge remove apache2

sudo apt-get autoremove

sudo rm -r /etc/apache2/sites-enabled/000-default.conf

sudo apt-get install apache2

sudo /etc/init.d/apache2 restart
```

## Set up the database

Create DB user and database for the project. (Be aware to put the same DB user in your project so you dont have to change the files):

```
sudo -u postgres psql

CREATE USER vagrant WITH PASSWORD 'laCumbre1';
CREATE DATABASE law OWNER vagrant;
GRANT ALL PRIVILEGES ON DATABASE law TO vagrant;
\q
```

**Add vagrant to sudo**
```
sudo adduser vagrant

sudo usermod -aG sudo vagrant
```

Edit visudo file.
```
sudo visudo
```

Add the following line under root
```
root    ALL=(ALL:ALL) ALL
grader  ALL=(ALL:ALL) ALL
vagrant  ALL=(ALL:ALL) ALL
```

Run python3 `database_setup.py` and `orm_setup.py` to seed the database items:
```
cd /var/www/catalog/LawAppUdacity
python3.6 database_setup.py
python3.6 orm_setup.py
```


## Generate Oauth credentials

Open the Google credentials and generate with the .xip.io domain

Insert in the JavaScript authorized origins
```
http://18.218.248.76.xip.io
```

Insert in the authorized URI redirects
```
http://18.218.248.76.xip.io/gconnect
```

**If you log in but not redirect, check your URI redirect addresses in the google credentials**

## Now you should be able to acces the website

Open in the browser:
```
http://18.218.248.76.xip.io
```


## Fixing errors and bibliography

Implement the fixes needed. Probably changing the postgre config file and some more.

**The WSGI path should NOT be with slashes, that's why I renamed the directory of the imported project**
- [https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them](https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them)

**Invalid command wsgi alias**
- [https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them](https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them)

**This will happen 99% sure**
- [https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge)

**This will happen 99% sure (JSON)**
- [https://stackoverflow.com/questions/31168606/internal-server-error-target-wsgi-script-cannot-be-loaded-as-python-module-and](https://stackoverflow.com/questions/31168606/internal-server-error-target-wsgi-script-cannot-be-loaded-as-python-module-and)

**Implement .xip.io domain**
- [https://stackoverflow.com/questions/36020374/google-permission-denied-to-generate-login-hint-for-target-domain-not-on-localh](https://stackoverflow.com/questions/36020374/google-permission-denied-to-generate-login-hint-for-target-domain-not-on-localh)

**The typo issue**
- [https://github.com/udacity/ud330/issues/75](https://github.com/udacity/ud330/issues/75)

**Unicode error**
- [https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20/38826645](https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20/38826645)


### Useful commands

**Check apache logs for errors**
```
sudo cat /var/log/apache2/error.log 
```

Restart apache
```
sudo service apache2 restart

sudo systemctl restart apache2
```

Find conf file postgres (inside psql)
```
show hba_file;
```

Restart postgresql
```
/etc/init.d/postgresql restart
```
