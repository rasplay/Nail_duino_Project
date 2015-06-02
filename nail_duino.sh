#!/bin/bash

sudo sed -i "s/console=ttyAMA0,115200 kgdboc=ttyAMA0,115200//" /boot/cmdline.txt

sudo sed -i "/-L ttyAMA0 115200 vt100/s/T0/#T0/" /etc/inittab

sudo echo 'KERNEL=="ttyAMA0", SYMLINK+="ttyS0",GROUP="dialout",MODE:=0666' >> /etc/udev/rules.d/85-paperduinopi.rules

sudo apt-get update
#sudo apt-get upgrade -y

wget http://rasplay.org/rpi/m_duino/avrdude_5.10-4_armhf.deb

sudo dpkg -i avrdude_5.10-4_armhf.deb

sudo chmod 4755 /usr/bin/avrdude

sudo apt-get install -y arduino

cd /tmp

doBackup() {
  cd $1
  echo -n " $2: "
  if [ -f $2.bak ]; then
    echo "Backup of $2 exists, not overwriting"
  else
    mv $2 $2.bak
    mv /tmp/$2 .
    echo "OK"
  fi
}

echo "Setting up Raspberry Pi to make it work with the Gertboard"
echo "and the ATmega chip on-board with the Arduino IDE."
echo ""
echo "Checking ..."

echo -n "  Avrdude: "
if [ ! -f /etc/avrdude.conf ]; then
  echo "Not installed. Please install it first"
  exit 1
fi

fgrep -sq GPIO /etc/avrdude.conf
if [ $? != 0 ]; then
  echo "No GPIO support. Please make sure you install the right version"
  exit 1
fi
echo "OK"

echo -n "  Arduino IDE: "
if [ ! -f /usr/share/arduino/hardware/arduino/programmers.txt ]; then
  echo "Not installed. Please install it first"
  exit 1
fi
echo "OK"

echo "Fetching files:"
for file in boards.txt programmers.txt avrsetup ; do
  echo "  $file"
  rm -f $file
  wget -q http://rasplay.org/rpi/m_duino/$file
done

echo "Replacing/updating files:"

rm -f /usr/local/bin/avrsetup
mv /tmp/avrsetup /usr/local/bin
chmod 755 /usr/local/bin/avrsetup

cd /etc
echo -n "inittab: "
if [ -f inittab.bak ]; then
  echo "Backup exists: not overwriting"
else
  cp -a inittab inittab.bak
  sed -e 's/^.*AMA0.*$/#\0/' < inittab > /tmp/inittab.$$
  mv /tmp/inittab.$$ inittab
  echo "OK"
fi

cd /boot
echo -n "cmdline.txt: "
if [ -f cmdline.txt.bak ]; then
  echo "Backup exists: not overwriting"
else
  cp -a cmdline.txt cmdline.txt.bak
  cat cmdline.txt					|	\
		sed -e 's/console=ttyAMA0,115200//'	|	\
		sed -e 's/console=tty1//'		|	\
		sed -e 's/kgdboc=ttyAMA0,115200//' > /tmp/cmdline.txt.$$
  mv /tmp/cmdline.txt.$$ cmdline.txt
  echo "OK"
fi

doBackup /usr/share/arduino/hardware/arduino boards.txt

doBackup /usr/share/arduino/hardware/arduino programmers.txt

sudo avrdude -p m328p -c gpio

echo "All Done."
echo "Check and reboot now to apply changes."
echo 'You must reboot'
exit 0
