#include <Servo.h>
// RIGHT FORWARD AND BACK
int rf=4;
int rb=2;
// LEFT FORWARD AND BACK
int lf=8;
int lb=7;

// PWM PIN RIGHT AND LEFT
int ENA=6;
int ENB=5;

// SENSOR
int TRIG = 14;
int ECHO = 15;

// SERVO
Servo Servo1;
int SERVO = 16;

// TURN AMOUNT (MS)
int turn = 330;

// STOP DISTANCE (INCHES)
int max_dist = 5;

// MOTOR SPEED
int mtr_speed = 150;
int max_speed = 255;
int offset = -10;

void STOP()
{
 digitalWrite(rf,LOW);
 digitalWrite(rb,LOW);
 digitalWrite(lb,LOW);
 digitalWrite(lf,LOW);

}

void FORWARD()
{
 digitalWrite(rf,HIGH);
 digitalWrite(rb,LOW);
 digitalWrite(lb,LOW);
 digitalWrite(lf,HIGH);

}

void BACK()
{
 digitalWrite(rf,LOW);
 digitalWrite(rb,HIGH);
 digitalWrite(lb,HIGH);
 digitalWrite(lf,LOW);

}

void LEFT()
{
 digitalWrite(rf,HIGH);
 digitalWrite(rb,LOW);
 digitalWrite(lb,HIGH);
 digitalWrite(lf,LOW);

}

void TURNLEFT()
{
  analogWrite(5, max_speed);
  analogWrite(6, max_speed);
  LEFT();
  delay(turn);
  STOP();
  analogWrite(5, mtr_speed+offset);
  analogWrite(6, mtr_speed);
}

void RIGHT()
{
 digitalWrite(rf,LOW);
 digitalWrite(rb,HIGH);
 digitalWrite(lb,LOW);
 digitalWrite(lf,HIGH);
}

void TURNRIGHT()
{
  analogWrite(5, max_speed);
  analogWrite(6, max_speed);
  RIGHT();
  delay(turn);
  STOP();
  analogWrite(5, mtr_speed+offset);
  analogWrite(6, mtr_speed);
}

void AROUND()
{
  analogWrite(5, max_speed);
  analogWrite(6, max_speed);
  RIGHT();
  delay(turn*1.7);
  STOP();
  analogWrite(5, mtr_speed+offset);
  analogWrite(6, mtr_speed);
}

int CHECK()
{
// SERVO LEFT
  Servo1.write(180);
  delay(500);
  int left = DISTANCE();
  Serial.println(left);
  digitalWrite(TRIG, LOW);
  pulseIn(ECHO, LOW);
  delay(500);
// SERVO RIGHT
  Servo1.write(0);
  delay(500);
  int right = DISTANCE();
  Serial.println(right);
  delay(500);
  // RESET AND DIFFERENCE
  Servo1.write(90);
  int difference = abs(right-left);
/////////////////////////////////////////////////
// IF RIGHT SIDE IS GREATER THAN LEFT SIDE, TURN RIGHT (90 DEGREES)
  if (right > max_dist && left <= max_dist)
// IF RIGHT SIDE IS GREATER THAN (APPROXIMATE) MAX RANGE, TURN AROUND (180 DEGREES)
    if (right > 400)
    {
      AROUND();
      delay(100);
      FORWARD();
    }
// MOVE FORWARD IF RIGHT SIDE IS OK
    else
    {
      TURNRIGHT();
      delay(100);
      FORWARD();
    }
/////////////////////////////////////////////////
// IF LEFT SIDE IS GREATER THAN RIGHT SIDE, TURN LEFT(90 DEGREES)
  else if (right <= max_dist && left > max_dist)
// IF LEFT SIDE IS GREATER THAN (APPROXIMATE) MAX RANGE, TURN AROUND (180 DEGREES)
    if (left > 400)
    {
      AROUND();
      delay(100);
      FORWARD();
    }
// MOVE FORWARD IF LEFT SIDE IS OK
    else
    {
      TURNLEFT();
      delay(100);
      FORWARD();
    }
// IF BOTH DIRECTIONS ARE HIGH (THIS IS A SENSOR PROBLEM WITH READING VERY HIGH NUMBERS WHEN IT LOOKS TOO FAR AWAY)
  else if (right > max_dist && left > max_dist or right <= max_dist && left <= max_dist)
  {
// CHECK THE RIGHT SIDE FIRST (90 DEGREES)
    TURNRIGHT();
    delay(100);
    int look = DISTANCE();
    delay(500);
// IF THE ROBOT IS CLOSE TO THE RIGHT SIDE, TURN AROUND (180 DEGREES)
    if (look <= max_dist)
    {
      AROUND();
      delay(100);
      int look = DISTANCE();
      delay(500);
// IF THE ROBOT IS CLOSE TO THE LEFT SIDE, TURN LEFT (90 DEGREES)
      if (look <= max_dist)
      {
        LEFT();
        delay(100);
        FORWARD();
      }
// IF THE ROBOT IS NOT CLOSE TO THE LEFT SIDE, MOVE FORWARD
      else
      {
        FORWARD();
      }
    }
// IF THE ROBOT IS NOT CLOSE TO THE RIGHT SIDE, MOVE FORWARD
    else
    {
      FORWARD();
    }
  }
/////////////////////////////////////////////////


}
// SENSOR FUNCTION (FOR MONITORING)
void SENSE()
{
  int inches = DISTANCE();
  Serial.println(inches);
}

// SENSOR FUNCTION FOR GETTING DISTANCE
int DISTANCE()
{
  unsigned long duration;
  int inches;
  int centimeters;
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(5);
  digitalWrite(TRIG, LOW);
  duration = pulseIn(ECHO, HIGH);
  centimeters = (duration*0.034)/2;
  inches = centimeters/2.54;
  return inches;
}

void setup() {
  Serial.begin(9600);
  pinMode(rf,OUTPUT);
  pinMode(rb,OUTPUT);
  pinMode(lb,OUTPUT);
  pinMode(lf,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Servo1.attach(SERVO);
  pinMode(LED_BUILTIN, OUTPUT);
  analogWrite(5, mtr_speed+offset);
  analogWrite(6, mtr_speed);
}

void loop() {
  int distance = DISTANCE();
// SENSE();
  if (distance > max_dist)
  {
    FORWARD();
  }
  else
  {
    STOP();
    digitalWrite(TRIG, LOW);
    pulseIn(ECHO, LOW);
    CHECK();
  }
  delay(100);
}
