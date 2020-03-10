char x; // for incoming serial data

void setup() {
  Serial.begin(115200); // opens serial port
  pinMode(2, OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    x = Serial.read();
  }
  
  if(incomingByte == 'S'){
    tone(2, 5, 1000);
    
  }
  if(incomingByte == 'A'){
    tone(2, 600, 1000);
    
  }
  if(incomingByte == 'T'){
    tone(2, 700, 1000);
    
  }
  if(incomingByte == 'U'){
    tone(2, 900, 1000);
    
  }
  if(incomingByte == 'R'){
    tone(2, 1500, 1000);
   
  }
  if(incomingByte == 'N'){
    tone(2,30, 1000);
    
  }
  
}
