// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
    // Serial Setup
    Serial.begin(9600); // initialize serial communications at 9600 bps:

    // initialize the digital pin as an output.
    pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
    char c = Serial.read();  //gets one byte from serial buffer
    if ( c == '1')
        digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    else if ( c == '0')
        digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW

    delay(1000);               // wait for a second
}
