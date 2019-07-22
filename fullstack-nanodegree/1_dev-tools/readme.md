# part 1: Developer's Tools
Brush up your knowledge of essential developers' tools such as the Unix shell, Git, and Github;then apply your skills to investigate HTTP, the Web's fundamental protocol and basicnetworking skills like DNS, NAT, IPv6, Bandwidth, Latency and how to use tcpdump to explore the packages in the network.

- Shell Workshop

- **GIT Version Control**
  - Create Git Repo
  - **Publish your page**
  - Review a repo's history
  - Add commits
  - Tagging, branching and merging: Be able to work for another's repo. Contribute in Open Source.
  - Undoing changes.
  - Remote repositories.
  - Staying in sync with another's repo: Use pull request, Git rebase.

- **HTTP Request and Responses**
  - HTTP in real world.
  - HTTP Servers and Clients

- **Networking for web developers**
  - DNS: Names and Addresses
  - Adressing & Networks: Network blocks, interfaces, NAT, IPV6
  - Protocol Layers: TCPDump
  - Big Networks: Brandwidth, Latency, Filtering.


## Itz a Set up

1. Programs: VSCode, git, Python, nmap. Local web server.
2. Virtualize with VirtualBox and Vagrant.
3. Deploy to Heroku.

### 1. Programas

**VSCode**
1. Download and install: https://code.visualstudio.com/
2. Extensions: vscode-icons, Python, pyLint, GitLens, markdownlint.

**Git and Github**
1. Create Github account: https://github.com/ 
2. Download Git and set up: https://git-scm.com/downloads
```git
git config --global user.name "Your Name"
git config --global user.email "youremail@gmail.com"
git config color.ui auto
git config core.editor "code --wait"
```

3.	Clone repository
```git
git clone https://github.com/user/repository
```

4. Update .bash_profile
```git
touch .bash_profile
vim .bash_profile
```

```git
# Git aliases:
alias gs="git status"

# links a mis carpetas:
`alias repos="cd 'C:\Users\Gateway i5\repos'"`
`alias todo="cd 'C:\Users\Gateway i5\repos\todo'"`

echo 'Welcome Sir...' $USER. Hoy es date

export PS1="\A \u@\H \\$\[$(tput sgr0)\]"
```

Exit the insert mode by hitting the esc key. Save and close your file by typing the following :wq+Enter. Finally, update the file to use your new changes by typing:
```git
source .bash_profile
```

**Python 3**

(Centos) Install release-scl dependency
```git
Install release-scl
```

Check the python version
```git
python3 -V
```

Install requests
```git
pip install requests
```

Start Local web server
```git
python3 -m http.server 8000
```
```git
browser: localhost:8000`
```

Start file
```git
`python3 BookmarkServer.py`
```

**nmap**
```git
dnf install nmap
```
To check whether ncat is installed and working, open up two terminals. In one of them, run `ncat -l 9999` then in the other, `ncat localhost 9999`. Then type something into each terminal and press Enter. You should see the message on the opposite terminal.


### 2. Deploy to Heroku

1.	Sign up for a free Heroku account: https://www.heroku.com
2.	Download the Heroku command-line interface (CLI): https://devcenter.heroku.com/articles/heroku-cli
3.	Authenticate the Heroku CLI with your account
`heroku login`

4.	Create configuration files Procfile, requirements.txt, and runtime.txt and check them into your Git repository.
**requirements.txt**
```git
vim requirements.txt
requests>=2.12
```

**runtime.txt**
```git
vim runtime.txt
python-3.6.0
```

**.Procfile**
```git
vim .Procfile
web: python BookmarkServer.py
```

5. Modify your server to listen on a configurable port.
```python
if __name__ == '__main__':
port = int(os.environ.get('PORT', 8000)) # Use PORT if it's there.
server_address = ('', port)
httpd = http.server.HTTPServer(server_address, Shortener)
httpd.serve_forever()
```

6.	Check your server code into a new local Git repository and deploy to heroku.
`git init`

`git add .`

(output)
```git
Gateway i5@DESKTOP-TKOVDVR MINGW64 ~/repos/heroku (master)$ ls
BookmarkServer.py*  Procfile  requirements.txt  runtime.txt
```
```git
git commit -m "Checking in my bookmark server!"
heroku create your-app-name
git push heroku master
```


### 3. CentOs

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

7. Install Flask 