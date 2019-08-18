## 1. Install VM

**VirtualBox and Vagrant**
1. VirtualBox, which you can get from this download page.
2. Vagrant, which you can get from this download page.
3. Virtualize CentOs & install Guest Additions
```git
mkdir that-folder
cd that-folder
vagrant init centos/7
vagrant plugin install vagrant-vbguest && vagrant plugin install vagrant-sshfs
vagrant up && vagrant ssh
```

4. Server Set Up
```git
usermod -aG wheel username
sudo yum install dnf -y
sudo dnf update && sudo dnf upgrade -y
sudo dnf install nano vim mtr net-tools nmap tcpdump traceroute libpcap nmap-ncat bind-utils -y
```

5. Allow bridged adapter. Open .Vagrantfile
```git
config.vm.network "public_network", ip: "192.168.1.13", gateway: "192.168.1.1", bootproto: "static", bridge: "Qualcomm Atheros AR8151 PCI-E Gigabit Ethernet Controller (NDIS 6.30)"
```
`sudo systemctl restart network`

6. TEST: HTTP head request+ take response in netcat as input. Accessing server's IP and port, should be redirected.
`sudo printf 'HTTP/1.1 302 Moved\r\nLocation: https://www.eff.org/' | nc -l 2345`


## 2. PostgreSQL

```git
sudo yum install postgresql-server postgresql-contrib
```

**Initialize your Postgres database and start PostgreSQL:

```git
sudo postgresql-setup initdb
sudo systemctl start postgresql
```

Optional: Configure PostgreSQL to start on boot:

```git
sudo systemctl enable postgresql
```