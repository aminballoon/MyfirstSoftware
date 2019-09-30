int button1 = 2;
int button2 = 3;
int button3 = 4;
int button4 = 5;
int button5 = 6;
int button6 = 7;
 
boolean current = LOW;
boolean last = LOW;
boolean toggle = false;
boolean b1 =LOW;
boolean c1=false;
boolean b2 =LOW;
boolean c2=false;
boolean b3 =LOW;
boolean c3=false;
boolean b4 =LOW;
boolean c4=false;
boolean b5 =LOW;
boolean c5=false;
boolean b6 =LOW;
boolean c6=false;
 
void setup() 
{
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
  pinMode(button5, INPUT);
  pinMode(button6, INPUT);
  Serial.begin(9600);
}
 
void loop() {
   b1=digitalRead(button1);
   if (b1 == HIGH)
   {
      c1=!c1;
      if (c1==true)
      {
          Serial.println("s1 on");
      }
      delay(1):
   }
   b2=digitalRead(button1);
   if (b2 == HIGH)
   {
      c2=!c2;
      if (c2==true)
      {
          Serial.println("s2 on");
      }
      delay(1):
   }
   b3=digitalRead(button1);
   if (b3 == HIGH)
   {
      c3=!c3;
      if (c3==true)
      {
          Serial.println("s3 on");
      }
      delay(1):
   }
   b4=digitalRead(button1);
   if (b4 == HIGH)
   {
      c4=!c4;
      if (c4==true)
      {
          Serial.println("s4 on");
      }
      delay(1):
   }
   b5=digitalRead(button1);
   if (b5 == HIGH)
   {
      c5=!c5;
      if (c5==true)
      {
          Serial.println("s5 on");
      }
      delay(1):
   }
   b6=digitalRead(button1);
   if (b6 == HIGH)
   {
      c6=!c6;
      if (c1==true)
      {
          Serial.println("s6 on");
      }
      delay(1):
   }

}
