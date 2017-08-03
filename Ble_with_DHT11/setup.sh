sudo apt-get update;sudo apt-get upgrade -y

sudo apt-get install libdbus-1-dev libglib2.0-dev libdbus-glib-1-dev -y
sudo apt-get install libusb-dev libudev-dev libreadline-dev libical-dev -y
sudo apt-get install python-pip -y

mkdir -p work
cd work

#git clone https://github.com/IanHarvey/bluepy.git
git clone https://github.com/rasplay/bluepy.git
cd bluepy
python setup.py build
sudo python setup.py install

sudo cp ./bluepy/btle.py /usr/lib/python2.7/dist-packages/
sudo cp ./bluepy/bluepy-helper /usr/lib/python2.7/dist-packages/
sudo cp ./bluepy/uuids.json /usr/lib/python2.7/dist-packages/

echo "run"
echo " $ sudo hciconfig hci0 up"
echo " $ sudo hcitool lescan"
echo " $ python dht11tohm11.py"
