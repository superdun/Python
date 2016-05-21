#include <Servo.h> 

Servo myservo;
char line='a';   // 传入的串行数据
int ret = 0;
 
void setup() {
  Serial.begin(9600);  
  myservo.attach(9); 
  myservo.write(90);
}
 
void loop() {
// Serial.println('123');
  // 纯口可用时操作
  if (Serial.available() > 0) {
    
   // Serial.println(line);
    line = Serial.read();
    Serial.print(line);
    if (line=='a'){
      myservo.write(10);
    }
    if(line=='b'){
      myservo.write(90);
    }

  }

}
