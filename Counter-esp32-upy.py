
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

#import webrepl

#webrepl.start()

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ap = network.WLAN(network.AP_IF)
ap.config(essid="ESP_WIFI")
ap.config(max_clients=5)
ap.active(True)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

##defining pins according to the 5011BS 7-Segment schematic:
a = Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(18, Pin.OUT)
f = Pin(19, Pin.OUT)
g = Pin(21, Pin.OUT)


#define push buttons:
IncrementButton = Pin(3, Pin.IN, Pin.PULL_UP)
DecrementButton = Pin(1, Pin.IN, Pin.PULL_UP) 
ResetButton     = Pin(16,Pin.IN, Pin.PULL_UP)


#define push buttons:
x = IncrementButton.value()
y = DecrementButton.value()
z = ResetButton.value()


#starting a counter variable:
counter = 0



#define functions to display each number on the 7-Segment:
# Display 0 on 7-seg
def display0():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level
  e.off()                # set pin e to "off" (low) level
  f.off()                # set pin f to "off" (low) level 
  g.on()                 # set pin g to "on" (high) level
     
# Display 1 on 7-seg
def display1():
  a.on()                 # set pin a to "on" (high) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level 
  d.on()                 # set pin d to "on" (high) level
  e.on()                 # set pin e to "on" (high) level
  f.on()                 # set pin f to "on" (high) level 
  g.on()                 # set pin g to "on" (high) level
     
# Display 2 on 7-seg
def display2():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.on()                 # set pin c to "on"  (high) level 
  d.off()                # set pin d to "off" (low) level
  e.off()                # set pin e to "off" (low) level
  f.on()                 # set pin f to "on" (high) level 
  g.off()                # set pin g to "off" (low) level
     
# Display 3 on 7-seg
def display3():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level
  e.on()                 # set pin e to "on" (high) level
  f.on()                 # set pin f to "on" (high) level 
  g.off()                # set pin g to "off" (low) level

# Display 4 on 7-seg
def display4():
  a.on()                 # set pin a to "on" (high) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level 
  d.on()                 # set pin d to "on" (high) level
  e.on()                 # set pin e to "on" (high) level
  f.off()                # set pin f to "off" (low) level 
  g.off()                # set pin g to "off" (low) level
     
# Display 5 on 7-seg
def display5():
  a.off()                # set pin a to "off" (low) level
  b.on()                 # set pin b to "on" (high) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level
  e.on()                 # set pin e to "on" (high) level
  f.off()                # set pin f to "off" (low) level 
  g.off()                # set pin g to "off" (low) level
     
# Display 6 on 7-seg
def display6():
  a.off()                # set pin a to "off" (low) level
  b.on()                 # set pin b to "on" (high) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level
  e.off()                # set pin e to "off" (low) level
  f.off()                # set pin f to "off" (low) level 
  g.off()                # set pin g to "off" (low) level
     
# Display 7 on 7-seg
def display7():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level
  d.on()                 # set pin d to "on" (high) level
  e.on()                 # set pin e to "on" (high) level
  f.on()                 # set pin f to "on" (high) level 
  g.on()                 # set pin g to "on" (high) level
     
# Display 8 on 7-seg
def display8():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level
  e.off()                # set pin e to "off" (low) level
  f.off()                # set pin f to "off" (low) level 
  g.off()                # set pin g to "off" (low) level
    
# Display 9 on 7-seg
def display9():
  a.off()                # set pin a to "off" (low) level
  b.off()                # set pin b to "off" (low) level
  c.off()                # set pin c to "off" (low) level
  d.off()                # set pin d to "off" (low) level 
  e.on()                 # set pin e to "on" (high) level
  f.off()                # set pin f to "off" (low) level 
  g.off()                # set pin g to "off" (low) level
  

####Web Page Properties####

def web_page():
 
  html = """<html>
  <head> 
  <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;} h2{coulor: #2196F3 ; padding: 2vh;}p{font-size: 1rem}
  .button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button{background-color: #4286f4;} </style>
  </head>
  
  <body> 
  <h1>ESP Counter Controller</h1> 
  <h2>Team 33</h2>
  <p>counter state: <strong>""" +str(counter)+ """</strong></p>
  
    <style>
  
  .counter__value{width:30%;height:60px;margin:auto;background:rgba(255,255,255,0.75);backdrop-filter:blur(10px);font-size:45px;padding-top:6px;border-radius:10px;color:#2c3e50e6;margin-bottom:120px}

  .btn {border: 2px solid black; background-color: white;color: black;padding: 14px 28px;font-size: 16px; cursor: pointer;}
  .increment { border-color: #4CAF50;color: green;}
  .increment:hover {background-color: #4CAF50;color: white;}
  .decrement {border-color: #f44336;color: red}
  .decrement:hover {background: #f44336;color: white;}
  .reset {border-color: #2196F3;color: dodgerblue}
  .reset:hover {background: #2196F3;color: white;}
  </style>
  
  <p><a href="/?incbutton"><button class="btn increment">Increment</button></a></p>
  <p><a href="/?decbutton"><button class="btn decremnt">Decrement</button></a></p>
  <p><a href="/?resbutton"><button class="btn reset">Reset</button></a></p>
  

  </body>
  
  </html>"""
  return html

#7-Seg boots at 0 display:
display0()

#define an increment function for phyiscal push button:
def incrementButton_callback(pin):
  global counter
  if x :
    counter =counter + 1 
    if counter == 1:
      display1()
    elif counter == 2:   
      display2()
    elif counter == 3:   
      display3()
    elif counter == 4:   
      display4()
    elif counter == 5:   
      display5()
    elif counter == 6:   
      display6()
    elif counter == 7:
      display7()
    elif counter == 8:   
      display8()
    elif counter == 9:   
      display9()
    else :
      display0()
      counter = 0


#define an decrement function for phyiscal push button:  
def decrementButton_Callback(pin):
  global counter 
  if y:
    counter = counter-1
    if counter == 1  :
      display1()
    elif counter == 2  :   
      display2()
    elif counter == 3  :   
      display3()
    elif counter == 4  :   
      display4()
    elif counter == 5  :   
      display5()
    elif counter == 6  :   
      display6()
    elif counter == 7  :   
      display7()
    elif counter == 8  :   
      display8()
    elif counter == 9  :   
      display9()
    else               :
      display0()
      counter = 0  

     
#define an reset function for phyiscal push button:
def resetButton_callback(pin):
  global counter
  if z :
    display0()
    counter =0


###main function to push buttons 
IncrementButton.irq(trigger=Pin.IRQ_FALLING, handler=incrementButton_callback) #interrupt for Increment Button
DecrementButton.irq(trigger=Pin.IRQ_FALLING, handler=decrementButton_Callback) #interrupt for decrement Button    
ResetButton.irq(trigger=Pin.IRQ_FALLING, handler=resetButton_callback)         #interrupt for Reset Button 


#creating socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))                                        #bind the socket to an address (network interface and port number) using the bind() method
s.listen(5)


while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)

  inc_button = request.find('/?incbutton')
  dec_button = request.find('/?decbutton')
  reset_button= request.find('/?resbutton')
  
  #increment response for server
  if inc_button == 6  :
    counter = counter + 1
    if counter == 1:
       display1()
    elif counter == 2:   
       display2()
    elif counter == 3:   
       display3()
    elif counter == 4:   
       display4()
    elif counter == 5:   
       display5()
    elif counter == 6:   
       display6()
    elif counter == 7:   
       display7()
    elif counter == 8:   
       display8()
    elif counter == 9:   
       display9()
    else :   
       display0()
       counter = 0
       
  #decrement response for server
  if dec_button == 6 :
    counter = counter - 1
    if counter == 1  :
       display1()
    elif counter == 2  :   
       display2()
    elif counter == 3  :   
       display3()
    elif counter == 4  :   
       display4()
    elif counter == 5 :   
       display5()
    elif counter == 6  :   
       display6()
    elif counter == 7 :   
       display7()
    elif counter == 8 :   
       display8()
    elif counter == 9 :   
       display9()
    else :   
       display0()
       counter = 0  
  
    #reset response for server
  if reset_button == 6 :
    display0()
    counter = 0
    
  # response  call  the web_page() function and reurns HTML
  response = web_page()
  
  # Sending the response to the socket client
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  
  # Closing the  connection
  conn.close()




