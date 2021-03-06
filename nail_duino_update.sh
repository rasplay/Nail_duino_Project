#!/bin/bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.org
sudo cp /etc/apt/preferences /etc/apt/preferences.org

sudo sed -i '$a\# Source repository to add' /etc/apt/sources.list

sudo sed -i '$a\deb-src http://archive.raspbian.org/raspbian wheezy main contrib non-free rpi' /etc/apt/sources.list

sudo sed -i '$a\deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi' /etc/apt/sources.list

sudo sed -i '$a\deb http://archive.raspbian.org/raspbian jessie main contrib non-free rpi' /etc/apt/sources.list

sudo sed -i '$a\deb-src http://archive.raspbian.org/raspbian jessie main contrib non-free rpi' /etc/apt/sources.list

echo "Package: *
Pin: release n=wheezy
Pin-Priority: 900
Package: *
Pin: release n=jessie
Pin-Priority: 300
Package: *
Pin: release o=Raspbian
Pin-Priority: -10" >> preferences
sudo cp preferences /etc/apt/preferences

sudo apt-get update; sudo apt-get upgrade -y

sudo apt-get -t jessie install libjssc-java libastylej-jni libcommons-exec-java libcommons-httpclient-java libcommons-logging-java libjmdns-java libjna-java libjsch-java xrdp -y

git clone https://github.com/NicoHood/Arduino-IDE-for-Raspberry

cd Arduino-IDE-for-Raspberry

sudo apt-get remove -y arduino arduino-core

sudo dpkg -i arduino-core_1.6.3_all.deb arduino_1.6.3_all.deb

cd /usr/share/arduino/hardware/arduino/avr

sudo rm programmers.txt

sudo wget http://rasplay.org/rpi/m_duino/nail_duino/programmers.txt

sudo mv /etc/apt/sources.list /etc/apt/sources.list.nailduino
sudo mv /etc/apt/preferences /etc/apt/preferences.nailduino
sudo mv /etc/apt/sources.list.org /etc/apt/sources.list
sudo mv /etc/apt/preferences.org /etc/apt/preferences

echo "All Done."
echo 'Thax For Nail Duino on the Raspberrypi'
exit 0
