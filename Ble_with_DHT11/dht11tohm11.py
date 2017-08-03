#####################################################################
import sys      # for user input
import time     # for wait commands
import datetime # for current time
import struct
import timeit
import random

from btle import UUID, Peripheral

class HM10(Peripheral):
    _ctrlUUID=UUID("00001800-0000-1000-8000-00805f9b34fb")
    _dataUUID=UUID("0000aaa0-0000-1000-8000-00805f9b34fb")
    def __init__(self, addr):
        Peripheral.__init__(self,addr)
        self.discoverServices()
        #for cUUID in self.services:
        #    print("== %s =="%str(cUUID))
        #    print(self.getServiceByUUID(cUUID).getCharacteristics())
                
        self.ctrl_SRV=self.getServiceByUUID(self._ctrlUUID)
        self.data_SRV=self.getServiceByUUID(self._dataUUID)

        self.data = self.data_SRV.getCharacteristics()[0]
        
        self.ctrl = self.ctrl_SRV.getCharacteristics()[0]

cHM10 = HM10("7C:66:9D:9B:20:F6")
cHM10.ctrl.write(struct.pack("B", 0xff))

################################################
def PARSE(data):
    if str(data) == "":
        return
    else:
        data_hex = data.encode("hex")
        if ( len(data_hex) > 14 ):
            print ("realData:"+data)
            rtcCode1 = data[0:4]
            humidity = data_hex[4:8]
            rtcCode2 = data[8:12]
            temperature = data_hex[12:16]

####################### MAIN #######################################
def main():
    if True:
        try:
            while True:
                if ( cHM10.data.peripheral.waitForNotifications(3) ):
                    cHM10.data.read()
                    response=cHM10.data.peripheral.getNtfyData()
                    PARSE(response) 

            cHM10.disconnect()
        
        except Exception,e1:    # Catches any errors in the serial communication
            print("Error on main: "+str(e1))
    else:
        print("Cannot open serial port")

#-----------------------------------------------------------------------

if __name__=="__main__":
    main()
