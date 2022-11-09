#include <Servo.h>
Servo myservox; 
Servo myservoy;
String inByte;
int posx, posy;
void setup() {
  myservox.attach(8); //attach servo x to pin 8
  myservoy.attach(10); //attach servo y to pin 10
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
    { 
    posx = Serial.parseInt(); 
    posy = Serial.parseInt();       
    // move servo
    myservox.write(posx);
    myservoy.write(posy);
    }
    
}
