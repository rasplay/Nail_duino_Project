#!/bin/bash

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

echo "All Done."
echo "Check and reboot now to apply changes."
echo 'You must reboot'
exit 0
