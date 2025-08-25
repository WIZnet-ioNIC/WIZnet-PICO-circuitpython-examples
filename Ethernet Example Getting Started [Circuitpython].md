


<a name="Ethernet_Example_Getting_Started"></a>

:rocket:Ethernet Example Getting Started [CircuitPython]
===========================


> These sections will guide you through a series of steps from configuring development environment to running ethernet examples using the **WIZnet's ethernet products**.

- [Ethernet Example Getting Started [Circuitpython]](#ethernet-example-getting-started-circuitpython)
- [Hardware requirements](#hardware_requirements)
- [Development environment configuration](#development_environment_configuration)
  - [STEP1 : **Installing Circuitpython**](#step1--installing-circuitpython)
  - [STEP2 : **Setup WIZnet Ethernet Libraray**](#step2--setup-wiznet-ethernet-libraray)
- [Ethernet example structure](#ethernet_example_structure)
- [Ethernet example testing](#Ethernet_example_testing)
- [Documentation](#Documentation)



<a name="hardware_requirements"></a>

# :hammer:Hardware requirements

The Ethernet examples are compatible with the following Raspberry Pi-compatible WIZnet Ethernet I/O modules. These modules integrate **WIZnet Ethernet chips** with either the **RP2040** or **RP2350** microcontrollers.

| Board/Module Name              | MCU      | Ethernet Chip  | Interface     | Socket # | TX/RX Buffer  | Notes                                  |
|--------------------------------|----------|----------------|---------------|----------|---------------|----------------------------------------|
| **[WIZnet Ethernet HAT][link-wiznet_ethernet_hat]** |  | W5100S | SPI | 4 | 16KB | RP Pico-compatible |
| **[W5100S-EVB-Pico][link-w5100s-evb-pico]** | RP2040 | W5100S | SPI | 4 | 16KB |  |
| **[W5500-EVB-Pico][link-w5500-evb-pico]** | RP2040 | W5500 | SPI | 8 | 32KB |  |
| **[W55RP20-EVB-Pico][link-w55rp20-evb-pico]** | RP2040 | W5500 | SPI (PIO) | 8 | 32KB | SiP: RP2040 + W5500 |
| **[W5100S-EVB-Pico2][link-w5100s-evb-pico2]** | RP2350 | W5100S | SPI | 4 | 16KB |  |
| **[W5500-EVB-Pico2][link-w5500-evb-pico2]** | RP2350 | W5500 | SPI | 8 | 32KB |  |
| **[W6300-EVB-Pico2][link-w6300-evb-pico2]** | RP2350 | W6300 | QSPI (PIO) | 8 | 64KB | Supports IPv4/IPv6 |


<a name="development_environment_configuration"></a>

# :bulb:Development environment configuration

> To test the ethernet examples, the development environment must be configured to use Raspberry Pi Pico. The ethernet examples were tested by configuring the development environment for **Windows**. Please refer to the '**9.2. Building on MS Windows**' section of '**Getting started with Raspberry Pi Pico**' document below and configure accordingly.

![][link-CircuitPython]

## STEP - 1 : [**Installing CircuitPython**][link-Installing Circuitpython]

:warning:**Notice**

Install `CircuitPython` on Raspberry Pi Pico by referring to the link above.:point_down:

 - **[https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython)**



------

It makes it easier than ever to get prototyping by requriring no upfront desktop software downloads. Simply copy and edit files on the `CIRCUITPY` drive to iterate.


<p align="center"> <image src= "./images/START/Library000.png"></p>

You edit and save your code on code.py, run your code on the board.

Let's test "LED on" and "LED off" code. Actually, just visit the below page to blink led on your rpi pico board.

- [https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/blinky-and-a-button](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/blinky-and-a-button)


## STEP - 2 : [**Setup WIZnet Ethernet Libraray**][link-Setup WIZnet Libraray]

1. Copy the [**WIZnet library**][link-library] into the lib folder inside the Raspberry Pi Pico.
   [https://learn.adafruit.com/ethernet-for-circuitpython/circuitpython-setup](https://learn.adafruit.com/ethernet-for-circuitpython/circuitpython-setup)
   
   Before continuing, make sure your board's lib folder has at least the following files and folders copied over:
   
   `adafruit_wiznet5k`
   
   `adafruit_bus_device`
   
   `adafruit_requests.mpy`

<p align="center"> <image src= "./images/START/Library001.png"></p>



2. you need to open `PuTTY`. Under Connection type: choose the button next to Serial.
   In the box under Serial line, enter the serial port you found that your board is using. In the box under Speed, enter `115200`. 

<p align="center"> <image src= "./images/START/Library004.png"></p>

3. To see your COM port number, please open `Device Manager` on your Windows.
<p align="center"> <image src= "./images/START/Library005.png"></p>

4. see the terminal screen as follows. If you connect the WIZnet Ethernet HAT, you can see the `Chip Version:W5100S or W5500`
<p align="center"> <image src= "./images/START/Library006.png"></p>



<a name="ethernet_example_structure"></a>

# :open_file_folder:Ethernet example structure

Ethernet examples are available at '**RP2040-HAT-CircuitPython/example/**' directory. As of now, following examples are provided.

- [**DHCP**][link-DHCP]
- [**Loopback**][link-loopback]
- [**DNS**][link-DNS]
- [**HTTP**][link-HTTP]
  - [WebServer][link-WebServer]
  - [WebClient][link-WebClient]
- [**MQTT**][link-MQTT]
  - [Publish][link-MQTT_Pub]
  - [Subscribe][link-MQTT_Sub]
  - [PubSub][link-pubsub]
- [**SNTP**][link-SNTP]
- [**Adafruit IO**][link-adafruit_io]
  - [UpLink][link-uplink]
  - [DownLink][link-downlink]

<a name="Ethernet_example_testing"></a>

# :pushpin:Ethernet example testing

Check if the network is connected normally and if the data is sent to each other.

[W5x00_Ping_Test.py](https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/blob/master/examples/Network/W5x00_Ping_Test.py)

> This is the code to set the IP of 192.168.1.100
>
> I hope that the PC also has an environment that communicates with 192.168.1.xxx.

1. Copy the content to code.py on your RPi Pico and save.

![][link-ping_1]

2. Press the `Win+R` key to enter cmd and press Enter or OK to execute the **command prompt**.

![][link-ping_2]

3. When the command prompt window appears, type the **ping command** and press Enter.

```
ping 192.168.1.100 (-option)
```

![][link-ping_3]

4. Ping tests begin as packets are exchanged between hosts.

![][link-ping_4]

5. If you look at the time and loss rate among the statistical results, you can find out the status of the Internet network.

- It's normal when you see the screen below, and the packet loss rate is important.

![][link-ping_5]



<a name="Documentation"></a>

# :books:Documentation

Documentation for WIZnet Ethernet HAT and Raspberry pi pico board
## Raspberry Pi Pico
 [**Raspberry Pi Pico Datasheet**](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)

  An RP2040-based microcontroller board

 [**Getting started with Raspberry Pi Pico**](https://www.raspberrypi.org/documentation/microcontrollers/raspberry-pi-pico.html)

 C/C++ development with Raspberry Pi Pico and other RP2040-based microcontroller boards



<!--

Link

-->

[link-CircuitPython]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/Circuitpython.png
[link-PICO]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PICO.jpg
[link-raspberrypi_pico]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/raspberrypi_pico.png
[link-HAT]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/HAT.png"



[link-Installing Circuitpython]:https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython
[link-Setup WIZnet Libraray]:https://learn.adafruit.com/ethernet-for-circuitpython/circuitpython-setup



[link-w5100s]: https://docs.wiznet.io/Product/iEthernet/W5100S/overview
[link-rp2040]: https://www.raspberrypi.org/products/rp2040/
[link-PICO_HAT]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/HAT.png
[link-PICO_EVB]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/EVB.png

[link-wiznet_ethernet_chips]: https://docs.wiznet.io/Product/iEthernet#product-family
[link-w55rp20-evb-pico]: https://docs.wiznet.io/Product/ioNIC/W55RP20/w55rp20-evb-pico
[link-raspberry_pi_pico]: https://www.raspberrypi.com/products/raspberry-pi-pico/
[link-wiznet_ethernet_hat]: https://docs.wiznet.io/Product/Open-Source-Hardware/wiznet_ethernet_hat
[link-w5100s-evb-pico]: https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico
[link-w5500-evb-pico]: https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico
[link-w6100-evb-pico]: https://docs.wiznet.io/Product/iEthernet/W6100/w6100-evb-pico
[link-w6300-evb-pico]: https://docs.wiznet.io/Product/iEthernet/W6300/w6300-evb-pico
[link-w5100s-evb-pico2]: https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico2
[link-w5500-evb-pico2]: https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico2
[link-w6100-evb-pico2]: https://docs.wiznet.io/Product/iEthernet/W6100/w6100-evb-pico2
[link-w6300-evb-pico2]: https://docs.wiznet.io/Product/iEthernet/W6300/w6300-evb-pico2

[link-raspberry_pi_pico]: https://www.raspberrypi.org/products/raspberry-pi-pico
[link-wiznet_ethernet_hat]: https://docs.wiznet.io/Product/Open-Source-Hardware/wiznet_ethernet_hat
[link-wiznet_W5100S_evb_pico]:https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico
[link-library]:https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/libraries/adafruit_wiznet5k



[link-DHCP]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/DHCP
[link-Network]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/Network
[link-loopback]:  https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/Loopback
[link-DNS]:  https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/DNS
[link-WebServer]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/HTTP/Webserver
[link-HTTP]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/HTTP
[link-WebClient]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/HTTP/Webclient
[link-MQTT]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/MQTT
[link-MQTT_Pub]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/MQTT/Publish
[link-MQTT_Sub]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/MQTT/Subscribe
[link-pubsub]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/MQTT/PubSub
[link-SNTP]:  https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/SNTP
[link-adafruit_io]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/Adafruit_IO
[link-uplink]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/Adafruit_IO/UpLink
[link-downlink]: https://github.com/WIZnet-ioNIC/WIZnet-PICO-circuitpython-examples/tree/master/examples/Adafruit_IO/DownLink



[link-ping_1]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PING_1.jpg
[link-ping_2]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PING_2.jpg
[link-ping_3]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PING_3.jpg
[link-ping_4]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PING_4.jpg

[link-ping_5]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/START/PING_5.jpg


_[▲ Back to Top](#Ethernet_Example_Getting_Started)_ 

