import RPi.GPIO as GPIO
import time


from http.server import BaseHTTPRequestHandler, HTTPServer
import time


print ("EDU - AMPEL")  
print ("RPi: " , GPIO.RPI_REVISION, GPIO.RPI_INFO )

# Webserver 

hostName = "0.0.0.0"
hostPort = 8000
GPIO.setmode(GPIO.BCM) 
isGruen = False

def setLED (rot, gelb, gruen):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(4, GPIO.OUT)
    isGruen = gruen
    if gruen :
        GPIO.output (4, True)
    else:
        GPIO.output (4, False)
    
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print ("INFO:", self.client_address, self.path ) 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('<html><head> <meta charset="UTF-8"><title>Ampel</title>', "utf-8"))
        style ="""
            <style>
        body {
            background-color: lightgrey;
        }

        h1 {
            color: red;
        }

        p {
            color: blue;
            font-family: Arial, Helvetica, sans-serif;
        }

        .circle {
            height: 50px;
            width: 50px;
            border-radius: 50%;
        }

        .button {
            background-color: #4caf50;
            border: none;
            color: white;
            padding: 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
        }
    </style>
        """
        self.wfile.write(bytes(style, "utf8"))
        self.wfile.write(bytes('</head>', "utf-8"))
        self.wfile.write(bytes("<body><p>Webserver Response</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        htmlform = """
    <form action="send" method="GET">
        <label>Ampel 1:</label><br />
        <div class="circle" style="background-color: orangered;"></div><br>
        <div class="circle" style="background-color: yellow;"></div><br>
        <div class="circle" style="background-color: greenyellow;"></div><br>
        <input name="inp" id="inp" class="button" type="submit" value="Press"
            style="background-color: gray; border-radius: 50%;" /><br>
    </form>
        """

        self.wfile.write(bytes(htmlform, "utf8"))

        if ("gruen" in self.path):
            setLED(0,0,1)
            self.wfile.write(bytes("<p> %s</p>" % "Grün", "utf-8"))
        else:
            setLED(0,0,0)
        
        self.wfile.write(bytes("</body></html>", "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass # ^z 

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
GPIO.cleanup()