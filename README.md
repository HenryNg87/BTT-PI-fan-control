# BTT-PI-fan-control
Fan control with python script

#Requiement****
sudo apt update
sudo apt install gpiod

# Test the fan
gpioset gpiochip0 211=1

# Install python3 and python3-libgpiod
sudo apt install python3 python3-pip
sudo apt install python3-libgpiod

# Install simple-pid
pip3 install simple-pid


# Verify install
python3 --version

Installation :
Download the fan_control.py from this repos
Navigate to the file and run: python3 fan_control.py
For running without keep terminal try to use screen or nohup, etc

sudo apt-get install screen
screen
# Navigate to the python script
Run the script like previous step
Now ctl + A and then D to quit the screen. It shuold works without the terminal
To retach the screen run: screen -R



