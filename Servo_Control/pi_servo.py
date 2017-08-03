import time
import Servo

def main():
    servo = Servo.SERVO(9600, 2.0)
    print "Connected"

    # Initial Position
    UDpos=90
    LRpos=90

    # loop part
    while(True):

        # Increase Position
        UDpos += 1
        LRpos += 1
        print "UDpos : %d" % UDpos

        # Limit Position Set
        if ( UDpos > 180 ):
            UDpos = 10
        if ( LRpos > 180 ):
            LRpos = 10

        # Some Error Check
        rtc = True
        rtc = servo.setUDPosition(UDpos)
        if rtc is False:
            print "false:%d" % UDpos
        rtc = True
        rtc = servo.setLRPosition(LRpos)
        if rtc is False:
            print "false:%d" % LRpos

if __name__ == "__main__":
    main()
