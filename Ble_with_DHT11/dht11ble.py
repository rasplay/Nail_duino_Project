#####################################################################
# Aldo Vargas
# 
#
# Purpose:
#   Connects a Raspberry Pi to the MultiWii Flight Controller. Based on 
#   the work made by Drew Brandsen.
#   Using MutliWii Serial Protocol (MSP), requests flight telemetry
#   data. Attitude and RC input values coming from the RX/TX with the
#   purpose to do systems identification, or just act as a data logger.
#   
#
########################################################################


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
        for cUUID in self.services:
            print("== %s =="%str(cUUID))
            print(self.getServiceByUUID(cUUID).getCharacteristics())
                
        self.ctrl_SRV=self.getServiceByUUID(self._ctrlUUID)
        self.data_SRV=self.getServiceByUUID(self._dataUUID)

        self.data = self.data_SRV.getCharacteristics(UUID("0000aaa1-0000-1000-8000-00805f9b34fb"))[0]
        
        #print("== CTRL ==")
        #print(self.ctrl_SRV.getCharacteristics())
        #print("== DATA ==")
        #print(self.data_SRV.getCharacteristics())
        self.ctrl = self.ctrl_SRV.getCharacteristics()[0]

cHM10 = HM10("7C:66:9D:9B:20:F6")
cHM10.ctrl.write(struct.pack("B", 0xff))

#############################################################
# littleEndian(value)
#	receives: a parsed, hex data piece
#	outputs:  the decimal value of that data
#	function: swaps byte by byte to convert little
#			endian to big endian
#	function: calls 2's compliment to convert to decimal
#	returns:  The integer value
#############################################################
def littleEndian(value):
	length = len(value)	# gets the length of the data piece
	actual = ""
	for x in range(0, length/2):	#go till you've reach the halway point
		actual += value[length-2-(2*x):length-(2*x)]	#flips all of the bytes (the last shall be first)
		x += 1
	intVal = twosComp(actual)	# sends the data to be converted from 2's compliment to int
	return intVal				# returns the integer value

###################################################################
# twosComp(hexValue)
#	receives: the big endian hex value (correct format)
#	outputs:  the decimal value of that data
#	function: if the value is negative, swaps all bits
#			up to but not including the rightmost 1.
#			Else, just converts straight to decimal.
#			(Flip all the bits left of the rightmost 1)
#	returns:  the integer value
###################################################################
def twosComp(hexValue):
	firstVal = int(hexValue[:1], 16)
	if firstVal >= 8:	# if first bit is 1
		bValue = bin(int(hexValue, 16))
		bValue = bValue[2:]	# removes 0b header
		newBinary = []
		length = len(bValue)
		index = bValue.rfind('1')	# find the rightmost 1
		for x in range(0, index+1):	# swap bits up to rightmost 1
			if x == index:		#if at rightmost one, just append remaining bits
				newBinary.append(bValue[index:])
			elif bValue[x:x+1] == '1':
				newBinary.append('0')
			elif bValue[x:x+1] == '0':
				newBinary.append('1')
			x += 1
		newBinary = ''.join(newBinary) 	# converts char array to string
		finalVal = -int(newBinary, 2)	# converts to decimal
		return finalVal
			
	else:		# if not a negative number, simply convert to decimal
		return int(hexValue, 16)


################################################
def PARSE(data):
    if str(data) == "":
        return
    else:
        data_hex = data.encode("hex")
        print ("data:%s" % data_hex)


####################### MAIN #######################################
def main():
    global beginFlag

    print ("Beginning in 3 seconds...")
    
    if True:
        try:
            while True:
                #if ( cHM10.data.peripheral.waitForNotifications(3) ):
                #    cHM10.data.read()
                #    response=cHM10.data.peripheral.getNtfyData()
                #    PARSE(response) 
                response=cHM10.data.read()
                #response=cHM10.data.peripheral.getNtfyData()
                PARSE(response)

            cHM10.disconnect()
        
        except Exception,e1:    # Catches any errors in the serial communication
            print("Error on main: "+str(e1))
    else:
        print("Cannot open serial port")

#-----------------------------------------------------------------------
if __name__=="__main__":
    main()
