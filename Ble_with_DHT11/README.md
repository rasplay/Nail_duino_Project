# NailduinoBle
Raspberrypi to Nailduino(Arduino) Ble Connection

## Software

### Installation
  * Download Source Code.
  ```
  $ git clone https://github.com/rasplay/NailduinoBle.git
  ```
  
  * Just run script.
  ```
  $ cd NailduinoBle
  $ sh ./setup.sh
  ...
  ...
  ```
  
### Run
  * Find your BLE dongle
  ```
  $ sudo hcitool lescan
  ...
  < ctrl+c Escape >
  ```

  * Turn on BLE dongle
  ```
  $ sudo hciconfig hci0 up
  ```
  
  * Run
  ```
  $ python dht11tohm11.py
  ```
  
