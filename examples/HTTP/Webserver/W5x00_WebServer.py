import digitalio
import time
import board
if board.board_id in ("wiznet_w55rp20_evb_pico", "wiznet_w6300_evb_pico2"):
    import wiznet
else:
    import busio

import adafruit_connection_manager
import adafruit_requests as requests
from adafruit_wiznet5k.adafruit_wiznet5k import *
from adafruit_wsgi.wsgi_app import WSGIApp
import adafruit_wiznet5k.adafruit_wiznet5k_wsgiserver as server
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket

print("Wiznet5k WebServer Test(DHCP)")

# Setup your network configuration below
# random MAC, later should change this value on your vendor ID
MY_MAC = "00:01:02:03:04:05"
IP_ADDRESS = (192, 168, 1, 100)
SUBNET_MASK = (255, 255, 255, 0)
GATEWAY_ADDRESS = (192, 168, 1, 1)
DNS_SERVER = (8, 8, 8, 8)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ethernetRst = digitalio.DigitalInOut(board.W5K_RST)
ethernetRst.direction = digitalio.Direction.OUTPUT

# For Adafruit Ethernet FeatherWing
cs = digitalio.DigitalInOut(board.W5K_CS)
# For Particle Ethernet FeatherWing
# cs = digitalio.DigitalInOut(board.D5)

if board.board_id == "wiznet_w55rp20_evb_pico":
    spi_bus = wiznet.PIO_SPI(board.W5K_SCK, MOSI=board.W5K_MOSI, MISO=board.W5K_MISO)
elif board.board_id == "wiznet_w6300_evb_pico2":
    spi_bus = wiznet.PIO_SPI(board.W5K_SCK, quad_io0=board.W5K_MOSI, quad_io1=board.W5K_MISO, quad_io2=board.W5K_IO2, quad_io3=board.W5K_IO3)
else:
    spi_bus = busio.SPI(board.W5K_SCK, MOSI=board.W5K_MOSI, MISO=board.W5K_MISO)

# Reset W5500 first
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

# Initialize ethernet interface without DHCP
# eth = WIZNET5K(spi_bus, cs, is_dhcp=False, mac=MY_MAC, debug=False)
# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)

# Set network configuration
# eth.ifconfig = (IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER)

print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))

# Here we create our application, registering the
# following functions to be called on specific HTTP GET requests routes
web_app = WSGIApp()

html_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RaspberryPi Pico Web server - WIZnet W5100S/W5500</title>
</head>
<body>
<div align="center">
<H1>RaspberryPi Pico Web server & WIZnet Ethernet HAT</H1>
<h2>Network Information</h2>
<p>
Chip Version is $CHIPNAME<br>
My IP address is $IPADDRESS<br>
</p>
<h2>Control LED</h2>
<p>
<label for="led_on"></label><a href="/led_on" id="led_on"> [ON] </a><br>
</p>
<p>
<label for="led_off"></label><a href="/led_off" id="led_off"> [OFF] </a><br>
</p>
</div>
</body>
</html>
'''

html_string = html_string.replace("$CHIPNAME",eth.chip)
html_string = html_string.replace("$IPADDRESS",eth.pretty_ip(eth.ip_address))

#HTTP Request handlers
@web_app.route("/led_on")
def led_on(request):  # pylint: disable=unused-argument
    print("LED on!")
    led.value = True
    return ("200 OK", [], " led on!")
	
@web_app.route("/led_off")
def led_off(request): # pylint: disable=unused-argument
	print("LED off!")
	led.value = False
	return ("200 OK", [], " led off!")

@web_app.route("/")
def root(request):  # pylint: disable=unused-argument
    print("Root WSGI handler")
    # return ("200 OK", [], ["Root document"])
    return ("200 OK", [], [html_string])

# Here we setup our server, passing in our web_app as the application
server.set_interface(eth)
print(eth.chip)
wsgiServer = server.WSGIServer(80, application=web_app)

print("Open this IP in your browser: ", eth.pretty_ip(eth.ip_address))

# Start the server
wsgiServer.start()

while True:
    # Our main loop where we have the server poll for incoming requests
    wsgiServer.update_poll()
    # Maintain DHCP lease
    eth.maintain_dhcp_lease()
    # Could do any other background tasks here, like reading sensors

