#include <WiFi.h>
#include <HTTPClient.h>
#include <HttpClient.h>


const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 5000;


// defines pins numbers
const int trigPin = 2;
const int echoPin = 5;

// defines variables
long duration;
int distance;

void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication

WiFi.begin(ssid, password);
Serial.println("Connecting");
while(WiFi.status() != WL_CONNECTED) {
  delay(500);
  Serial.print(".");
}
Serial.println("");
Serial.print("Connected to WiFi network with IP Address: ");
Serial.println(WiFi.localIP());

Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}

void loop() {
// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance in CMs
// To measure the distance the sound has travelled we use the formula: Distance = (Time x SpeedOfSound) / 2.
// The "2" is in the formula because the sound has to travel back and forth. 
// First the sound travels away from the sensor, and then it bounces off of a surface and returns back
// speedofsound = 0.034 centimeter/microsecond
distance= duration*0.034/2;
// 400 centimeter is the max range of this sensor
if (distance < 72 ) 
        {
        Serial.println("object detected");

        HTTPClient http;

      String serverPath = "http://YOUR_SERVER_IP:PORT/security/alert/True";
      // e.g String serverPath = "http://192.168.1.5:8000/security/alert/True";
      
      // Your Domain name with URL path or IP address with path
      http.begin(serverPath.c_str());
      
      // Send HTTP GET request
      int httpResponseCode = http.GET();
      
      if (httpResponseCode>0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        Serial.println(payload);
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      // Free resources
      http.end();
        }
// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
}
