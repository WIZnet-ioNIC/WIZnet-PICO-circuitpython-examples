# How to WebClient Example

![][link-http]


## Step 1: Prepare Software

> The following serial terminal program is required for **Webclient** test, download and install from below links.

### &#10004;[**Tera Term**][link-tera_term]  or  &#10004; [**Hercules**][link-hercules]




## Step 2: Prepare hardware

If you are using WIZnet's PICO board, you can skip '1. Combine...'

1. If you are using WIZnet Ethernet HAT, Combine it with Raspberry Pi Pico.

2. Connect ethernet cable to your PICO board ethernet port.

3. Connect your PICO board to desktop or laptop using USB cable. 



## Step 3: Setup WebClinet Example

> To test the **Webclient example**, minor settings shall be done in code.


1. Initialize ethernet interface with DHCP

```python
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)
```

2. HTML request, Access **HTML URL** and **Json URL**

```python
TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_URL = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"
```

3. Run Pico to open the web client.

```python
##run Webclient
while True:
    # Maintain DHCP lease
    eth.maintain_dhcp_lease()

    led.value = not led.value
    time.sleep(1)
```

4. Copy **Webclient code** to **code.py** on your RPi Pico and save. Make sure that PC is configured in same subnet 192.168.1.xxx.



## Step 4: Upload and Run

1. Check COMport in [Device Manager] and then open Serial Terminal.

![][link-port]![][link-terminal]

2. Use DNS to access the address of the server. After that, it accesses the server in each URL and prints the contents. The text of each URL is as follows.

![][link-webclient_1]

3. Text content in **HTML**.

![][link-webclient_2]

4. Text content in **Json**.

![][link-webclient_3]



## Attach

Attach a flow that operates through [WIRESHARK](https://www.wireshark.org/#download).

- [HTTP_Client.pcapng](https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/examples/HTTP/Webclient/HTTP_Client.pcapng)



 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)






<!--
Link
-->

[link-tera_term]: https://osdn.net/projects/ttssh2/releases/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility
[link-http]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/HTTP_0.jpg
[link-http_0]: https://github.com/Wiznet-OpenHardware/RP2040-HAT-CircuitPython/blob/main/img/HTTP/HTTP.png



[link-port]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/PORT.jpg
[link-terminal]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/Terminal.jpg

[link-webclient_1]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/Webclient_1.PNG
[link-webclient_2]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/Webclient_2.PNG
[link-webclient_3]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/HTTP/Webclient_3.PNG
