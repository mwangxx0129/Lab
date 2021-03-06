# Ubuntu 16.04 LTS
# install ubuntu alongside with Win10
* when enter boot selection, choose UEFI [your U driver]

# Install dependencies
sudo apt-get install -f

# update
sudo apt-get update

# Install git

sudo apt-get install git

# Install Terminator
sudo apt-get install terminator


# Install NodeJs: (root)

curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -

sudo apt-get install -y nodejs

# Install Nodemon

sudo npm install -g nodemon

# Install Redis

wget http://download.redis.io/releases/redis-3.2.6.tar.gz

tar xzf redis-3.2.6.tar.gz

cd redis-3.2.6

make

sudo make install

cd utils

sudo ./install_server.sh

# Install python 2.7: This is installed already in Ubuntu
python --version
Python 2.7.12

# Install pip

(sudo apt-get update)

sudo apt install python-pip

sudo pip install Flask

# Install Docker

curl -fsSL https://get.docker.com/ | sh

Setup docker permission:

sudo usermod -aG docker $(whoami)

(you need to logout and login again after set permission)

To start docker when the system boots: sudo systemctl enable docker

# Install Nginx
(For ubuntu 16.04) Add following two lines into /etc/apt/sources.list

deb http://nginx.org/packages/ubuntu/ xenial nginx

deb-src http://nginx.org/packages/ubuntu/ xenial nginx

Then run:

sudo apt-get update

sudo apt-get install nginx

# Install angular/cli(optional)

sudo npm install -g @angular/cli

# Trouble shooting
## redis
sudo apt-get install make

sudo apt-get install build-essential
