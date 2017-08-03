sudo sed -i "s/console=ttyAMA0,115200 kgdboc=ttyAMA0,115200//" /boot/cmdline.txt
sudo sed -i "/-L ttyAMA0 115200 vt100/s/T0/#T0/" /etc/inittab
sudo echo 'KERNEL=="ttyAMA0", SYMLINK+="ttyS0",GROUP="dialout",MODE:=0666' >> /etc/udev/rules.d/85-paperduinopi.rules
sudo apt-get update; sudo apt-get upgrade -y
wget http://rasplay.org/rpi/m_duino/avrdude_5.10-4_armhf.deb
sudo dpkg -i avrdude_5.10-4_armhf.deb
sudo chmod 4755 /usr/bin/avrdude
sudo apt-get install -y arduino
wget http://rasplay.org/rpi/m_duino/setup.sh
sudo sh ./setup.sh
sudo avrdude -p m328p -c gpio
echo 'You must reboot'
