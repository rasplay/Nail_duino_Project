servoMultiduino
===============

Control two servo motors for Raspberrypi and Atmega328p

Project by www.rasplay.org -Multiduino-

Multiduino = Multi-Pi + Atmega328p(for arduino)

Dependency
I. HardWare

 1. Raspberry-pi, it is ultra-low-cost ($35) credit-card sized computer, can run Linux.

 2. Multi-Pi(optional), it is Raspberry-pi extension Board, easy to connect DC Motor and it is like breadboard. Some sample in www.rasplay.org

 3. Atmega328p, connected Raspberry-pi using serial port, ttyAMA0.

II. SoftWare

 1. Using Python source code on Raspberry-pi

     One Servo Motor Control Class Library file.

     One Sample used library.

 2. Using C source code .ino file on Atmega328p

III. Using Code

 On Raspberrypi
 
 0. python-serial

  $ sudo apt-get install python-serial -y
  
 1. Cloning git source code

  $ git clone https://github.com/rasplay/servoMultiduino.git
  
 2. Compile and Upload on Atmega328p

  . I'm using SCONS compile and upload util ( visit https://scons.org )
  
  . Some sample post
  
      RPino Command Line Compile&Upload with RPi (http://www.rasplay.org/?p=5081 )
      
  . Using gertboard bootloader ( https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/ )

  $ scons ARDUINO_PORT=/dev/ttyS0 ARDUINO_BOARD=multiduino ARDUINO_VER=1.0.1 ARDUINO_HOME=/usr/share/arduino upload

  . Uploading Complete
 
 3. Run python program RaspberryPi 

  $ python pi_servo.py 

Enjoy!!
