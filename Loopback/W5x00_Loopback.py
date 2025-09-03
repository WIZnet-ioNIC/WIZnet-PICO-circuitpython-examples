import digitalio
import time
import board
if board.board_id in ("wiznet_w55rp20_evb_pico", "wiznet_w6300_evb_pico2"):
    import wiznet
else:
    import busio
    
from adafruit_wiznet5k.adafruit_wiznet5k import *
import adafruit_wiznet5k.adafruit_wiznet5k_socketpool as socketpool

print("Wiznet5k Loopback Test (DHCP)")
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

# Reset W5x00 first
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

# # Initialize ethernet interface without DHCP
# eth = WIZNET5K(spi_bus, cs, is_dhcp=False, mac=MY_MAC, debug=False)
# # Set network configuration
# eth.ifconfig = (IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER)

# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)

# Initialize a socket for our server
pool = socketpool.SocketPool(eth)
server = pool.socket()  # Allocate socket for the server
server_ip = None  # IP address of server
server_port = 5000  # Port to listen on
server.bind((server_ip, server_port))  # Bind to IP and Port
server.listen()  # Begin listening for incoming clients
print("server listen")

print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))

conn = None

while True:
    # Maintain DHCP lease
    eth.maintain_dhcp_lease()

    if conn is None:
        conn, addr = server.accept()  # Wait for a connection from a client.
        print("socket connected")
        print(conn, addr)
    else :
        if conn._status in (
            SNSR_SOCK_FIN_WAIT,
        ):
            print("socket SNSR_SOCK_FIN_WAIT")
            conn.close()
            conn = None
        elif conn._status in (
            SNSR_SOCK_CLOSE_WAIT,
        ):
            print("socket SNSR_SOCK_CLOSE_WAIT")
            conn.disconnect()
            conn.close()
            conn = None
        else :
            # print("socket established", conn.status)
            avail = conn._available()
            if avail:
                # print("Received size:", avail)
                # data = conn.recv(0)
                data = conn._embed_recv(2048)
                if data:
                    print("DATA ptr", id(data), ",DATA Len: ", len(data))
                    conn.send(data)  # Echo message back to client
