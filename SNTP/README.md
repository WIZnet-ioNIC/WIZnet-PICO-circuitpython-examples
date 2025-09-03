# How to SNTP Example

![][link-NTP]

## Step 1: Prepare Software

> The following serial terminal program is required for **SNTP** test, download and install from below links.

### &#10004;[**Tera Term**][link-tera_term]  or  &#10004; [**Hercules**][link-hercules]



## Step 2: Prepare hardware

If you are using WIZnet's PICO board, you can skip '1. Combine...'

1. If you are using WIZnet Ethernet HAT, Combine it with Raspberry Pi Pico.

2. Connect ethernet cable to your PICO board ethernet port.

3. Connect your PICO board to desktop or laptop using USB cable. 


## Step 3: Prepare libraries

Download the required library files and copy them to the CIRCUITPY drive of your Pico.

- [adafruit_wiznet5k](https://github.com/adafruit/Adafruit_CircuitPython_Wiznet5k/tree/main/adafruit_wiznet5k)

- [Adafruit_CircuitPython_NTP](https://github.com/adafruit/Adafruit_CircuitPython_NTP)



## Step 4: Setup SNTP Example

> To test the **SNTP example**, minor settings shall be done in code.



1. Import **NTP Library** and setup configuration.

```python
from adafruit_wiznet5k.wiznet5k_ntp import NTP

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
```

2. Initialize **DHCP**

```python
# Setup your network configuration below
# random MAC, later should change this value on your vendor ID
MY_MAC = (0x00, 0x01, 0x02, 0x03, 0x04, 0x05)
```

```python
# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)
```

3. Convert the **URL** of the server and get time information through **NTP**.

```python
#NTP
ntpserver_ip = eth.pretty_ip(eth.get_host_by_name("time.google.com"))
print("NTP : %s" % ntpserver_ip)  #DNS Domain
ntp = NTP(iface = eth, ntp_address = ntpserver_ip ,utc=9)
cal = ntp.get_time()
print("The date is %s %d/%d/%d" %(days[cal.tm_wday], cal.tm_mday,cal.tm_mon,cal.tm_year))
print("The time is %d:%02d:%02d" %(cal.tm_hour,cal.tm_min,cal.tm_sec))
```

4. Copy **SNTP code** to **code.py** on your RPi Pico and save. Make sure that PC is configured in same subnet 192.168.1.xxx.



## Step 5: Upload and Run

1. Check COMport in [Device Manager] and then open Serial Terminal.

![][link-port]![link-terminal]

2. Access the domain URL of the server and convert it to an IP address. Also, get the time information value and print it out.

![][link-SNTP]



## Attach

Attach a flow that operates through [WIRESHARK](https://www.wireshark.org/#download).

- [SNTP.pcapng](https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/examples/SNTP/SNTP.pcapng)




 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)


<!--
Link
-->

[link-tera_term]: https://osdn.net/projects/ttssh2/releases/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility
[link-NTP]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/SNTP/NTP.jpg



[link-port]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/SNTP/PORT.jpg
[link-Terminal]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/SNTP/Terminal.jpg
[link-SNTP]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/SNTP/SNTP_1.PNG
