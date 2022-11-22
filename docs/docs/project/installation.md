# Instillation

## Raspberry Pi 4
::: warning This project was done using a Raspberry Pi 4, with a fresh OS install. Using a different version of the Raspberry Pi and/or an existing OS instillation may not work and likely cause issues. Don't want to delete your existing OS, just get a new SD card. 
:::

### OS Installation
1. Install the latest Raspberry Pi OS lite (64-Bit) using the Raspberry Pi Imager.
2. In the options you want to enable SSH, using password authentication. Then set the username and password and save it somewhere.

### System setup

1. ``sudo raspi-config``
2. Interface
3. I2C > Enable
4. Save and exit
5. ``sudo apt-get update``
6. ``sudo apt-get upgrade``
7. Run ``python --version`` to check the installed python version. This needs to be 3.8 or greater

## Node
Node will need to be installed to run the dashboard and also for pm2 which runs all the python processes. To install node I use [nvm](https://github.com/nvm-sh/nvm), you can install it with the following commands.
```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
```
Close your terminal and re-open it for the nvm command to work, now we need to install a node version.
```bash
nvm install v16.18.1
```
After installation nvm will often use the installed version, but you may need to tell it to do so with the command below.
```bash
nvm use v16.18.1

#Run the node version command below to check that the install worked
node --version
```
## Redis
Sensor data is stored in Redis using the TimeSeries module, so we will first have to install this and add the module.

To install redis, run the following commands.
```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```
Once Redis is installed you need to load the timeseries module.

::: tip The wget command below will download a compiled redistimeseries.so, this was compiled from the redis source code as their download links don't seem to work anymore. You can also download the file from the files page on this site.
:::

```bash
wget https://becreative.distillation.dev/project-files/redistimeseries.so
sudo chmod +x redistimeseries.so
sudo cp redistimeseries.so /etc/redis/
sudo nano /etc/redis/redis.conf
```
In this file scroll down to the modules heading and add the following line
```
loadmoule /etc/redis/redistimeseries.so
```
Now restart the redis-server
```
sudo systemctl restart redis-server
```

## Control System
::: danger Before starting on this section its a good idea to reboot the Pi using ``sudo reboot now`` Otherwise some scripts might require this during there operation.
:::

This section will cover the project files. There are 3 main sections they are:
- Backend: Contains all the sensor scripts, api server and self driving logic
- Dashboard: The frontend of the application for interacting with the vehicle and monitoring sensors.
- Docs: The documentation of this project, you should not need to use this.

First though lets get the project files.

::: warning If you get a command not found for git then install it using ``sudo apt-get install git``
:::
```bash
git clone https://github.com/nagsterFVZ/self-driving.git
# Lets open the directory
cd self-driving
```
### Backend
First open the backend folder
```bash
cd /backend
```
For ease of setup, I have created some bash files that install the needed system packages and python libraries.
::: info If this fails due to pip not being installed you can install it with
``sudo apt install python3-venv python3-pip`` 
:::

```bash
sudo ./packages.bash
sudo ./circuit-python-setup.bash
sudo pip install -r requirements.txt
```
::: info The command above may warn of installing packages as root, this is fine as its the only project on the system and some of the packages require root installation
:::
