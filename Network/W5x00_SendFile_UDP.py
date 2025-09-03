import digitalio
import time
import board
if board.board_id in ("wiznet_w55rp20_evb_pico", "wiznet_w6300_evb_pico2"):
    import wiznet
else:
    import busio
    
from adafruit_wiznet5k.adafruit_wiznet5k import *
import adafruit_wiznet5k.adafruit_wiznet5k_socketpool as socketpool
import sys
import os

print("Send the files using Wiznet5k UDP")

# Setup your network configuration below
# random MAC, later should change this value on your vendor ID
MY_MAC = "00:01:02:03:04:05"
IP_ADDRESS = (192, 168, 1, 111)
SUBNET_MASK = (255, 255, 255, 0)
GATEWAY_ADDRESS = (192, 168, 1, 1)
DNS_SERVER = (8, 8, 8, 8)
port = 5001
MAX_SIZE = 1024

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

# # Initialize ethernet interface without DHCP
# eth = WIZNET5K(spi_bus, cs, is_dhcp=False, mac=MY_MAC, debug=False)
# # Set network configuration
# eth.ifconfig = (IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER)

# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=False, mac=MY_MAC, debug=False)
#if eth() != True :
eth.ifconfig = (IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER)

# Initialize a socket for our server
pool = socketpool.SocketPool(eth)
sock = socketpool.Socket(pool, pool.AF_INET, pool.SOCK_DGRAM)  # Allocate socket for the server
server_ip = '192.168.1.200'  # IP address of server
server_port = 5000  # Port to listen on

print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))

class file:
    count=0
    
    def __init__(self, filename):
        self.filename = filename


    def sendfile(filename):
        data_trans = 0
        print( filename)
        with open(filename, 'rb') as f :
            try:
                data=f.read() #Read
                data_trans = len(data)    
            except Exception as e:
                print('error!!!! %s' %e)   
        print('Complete transmission data[%s], transmission size[%d]' %(filename, data_trans))
        return data


while True: #Loop
    print('\'/exit\'')

    filename = input('Input the Filename:')

    if filename == '/exit':
        sys.exit()
    sock = socketpool.Socket(pool, pool.AF_INET, pool.SOCK_DGRAM)
    sock.bind((eth.pretty_ip(eth.ip_address),port))

    data = file.sendfile(filename)  
    if len(data) > MAX_SIZE:  # If it is longer than the limited length
        cnt = 0
        while(cnt+1)*MAX_SIZE < len(data): #Repeat if shorter than the Total data
            data_tmp = data[cnt*MAX_SIZE:(cnt+1)*MAX_SIZE] #split transmission
            sock.sendto(data_tmp,(server_ip, server_port))
            cnt = cnt +1
        data_tmp = data[cnt*MAX_SIZE:len(data)] # last transmission
        sock.sendto(data_tmp,(server_ip, server_port))
    else :
        sock.sendto(data,(server_ip, server_port))
        
