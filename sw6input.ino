int button1 = 2;
int button2 = 3;
int button3 = 4;
int button4 = 5;
int button5 = 6;
int button6 = 7;
bool b1 =1;
bool b2 =1;
bool b3 =1;
bool b4 =1;
bool b5 =1;
bool b6 =1;
 
void setup() 
{
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);
  pinMode(button4, INPUT_PULLUP);
  pinMode(button5, INPUT_PULLUP);
  pinMode(button6, INPUT_PULLUP);
  Serial.begin(9600);
}

 
void loop() {
   if (digitalRead(button1) == 0)
   {
      while (digitalRead(button1) == 0)
      {
        b1= !b1;
        delay(500);
      }
   }
   if (b1==0)
   {
     Serial.println("s1 on");
      b1= !b1;
   }
 if (digitalRead(button2) == 0)
   {
      while (digitalRead(button2) == 0)
      {
        b2= !b2;
        delay(500);
      }
   }
   if (b2==0)
   {
     Serial.println("s2 on");
      b2= !b2;
   } 
   if (digitalRead(button3) == 0)
   {
      while (digitalRead(button3) == 0)
      {
        b3= !b3;
        delay(500);
      }
   }
   if (b3==0)
   {
     Serial.println("s3 on");
      b3= !b3;
   }
    if (digitalRead(button4) == 0)
   {
      while (digitalRead(button4) == 0)
      {
        b4= !b4;
        delay(500);
      }
   }
   if (b4==0)
   {
     Serial.println("s4 on");
      b4= !b4;
   }
    if (digitalRead(button5) == 0)
   {
      while (digitalRead(button5) == 0)
      {
        b5= !b5;
        delay(500);
      }
   }
   if (b5==0)
   {
     Serial.println("s5 on");
      b5= !b5;
   }
    if (digitalRead(button6) == 0)
   {
      while (digitalRead(button6) == 0)
      {
        b6= !b6;
        delay(500);
      }
   }
   if (b6==0)
   {
     Serial.println("s6 on");
      b6= !b6;
   }
}
