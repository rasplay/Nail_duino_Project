import serial
import time

class SERVO:
    DEFAULT_BAUDRATE = 9600
    DEFAULT_TIMEOUT = 2.0
    DEVICE = "/dev/ttyAMA0"

    UD_POSITION = 90
    LR_POSITION = 10

    # Connection Initializing 
    def __init__(self, arg_baudrate=DEFAULT_BAUDRATE, arg_timeout=DEFAULT_TIMEOUT):
        self.port = serial.Serial(self.DEVICE, baudrate=arg_baudrate, timeout=arg_timeout)
        self.initPosition()

    # Init Position
    def initPosition(self):
        ud_pos = 90
        lr_pos = 90
        self.setUDPosition(ud_pos)
        self.setLRPosition(lr_pos)

    # Set UpDown Position
    def setUDPosition(self, pos):
        selector = "UD"
        # Making Send Data format
        sendData = selector + str('%03d' % pos) + ';'
        self.port.write(sendData)
        # Read Answerback Data
        rcvData = self.readDataEnd(';')
        return self.isSucceed(sendData, rcvData)

    # Set LeftRight Position
    def setLRPosition(self, pos):
        selector = "LR"
        # Making Send Data format
        sendData = selector + str('%03d' % pos) + ';'
        self.port.write(sendData)
        # Read Answerback Data
        rcvData = self.readDataEnd(';')
        return self.isSucceed(sendData, rcvData)

    # Read Data for size
    def readData(self, size):
        rts = self.port.read(size)
        return rts

    # Read Data for End Character
    def readDataEnd(self, ch='\n'):
        line = []
        str1 = ''
        while True:
            for c in self.port.read():
                line.append(c)
                if (c == ch) :
                    str1 = ''.join(line)
                    return str1

    # Check SendData is same.
    def isSucceed(self, sendData, rcvData):
        #print ("[" + sendData + "]" + "[" + rcvData + "]")
        if ( sendData == rcvData ) :
            return True
        else :
            print ("ReturnData:         [" + rcvData + "]")
            return False
