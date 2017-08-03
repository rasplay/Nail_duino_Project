#include <Servo.h>

// Servo instance
Servo myservoLR; //Left Right Servo
Servo myservoUD; //Up Down Servo

// Define Servo Pin
int pinnoUD = 10;
int pinnoLR = 9;

// Initial & Limit Value
int posUD = 10; // Minimum Limit on Upper
int posLR = 90; // Init Center Position

String readString, selector, position, sbuffer;

int move;

void setup()
{
    // Serial Setup
    Serial.begin(9600); // initialize serial communications at 9600 bps:

    // Arduino Pin No.
    myservoUD.attach(pinnoUD);
    myservoLR.attach(pinnoLR);

    // wait 1sec
    delay(1000);

    // move to Initial Position
    myservoUD.write(posUD);
    myservoLR.write(posLR);
}

void loop() {

    while (Serial.available()) {
        if (Serial.available() >0) {
            char c = Serial.read();  //gets one byte from serial buffer
            readString += c; //makes the string readString

            // End Character
            if ( c == ';' ) break;
        }
        else delay(100);  //delay to allow buffer to fill
    }

    delay(10);  //delay to allow buffer to fill

    if (readString.length() >= 0) {
        // expect a string like "UD130" containing the two servo positions
        selector = readString.substring(0, 2); //get the first 2 characters like "UD"
        position = readString.substring(2, 5); //get the next 3 characters like "130"

        // check format position isnumber
        if ( position[0] >= '0' && position[0] <= '9'
          && position[1] >= '0' && position[1] <= '9'
          && position[2] >= '0' && position[2] <= '9')
        {
            //  check two bytes known code 
            // "UD" is selcted UpDown Motor
            if ( selector[0] == 'U' && selector[1] == 'D' )
            {
                // Position Set
                posUD = position.toInt();
                // Run the motor
                myservoUD.write(posUD);

                // Return Used Value
                sbuffer=selector + position +';';
                Serial.print(sbuffer);
            }
            // "LR" is selcted LeftRight Motor
            else if ( selector[0] == 'L' && selector[1] == 'R' )
            {
                // Position Set
                posLR = position.toInt();
                // Run the motor
                myservoLR.write(posLR);

                // Return Used Value
                sbuffer=selector + position +';';
                Serial.print(sbuffer);
            }
        }

        // init buffer
        readString="";

        delay(10); //delay to allow buffer to fill

    }
}

