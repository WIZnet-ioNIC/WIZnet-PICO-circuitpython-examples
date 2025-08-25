# How to Test LoopBack Example

![][link-loopback_0]

## Step 1: Prepare Software

> The following serial terminal program is required for **LoopBack** test, download and install from below links.

### &#10004;[**Tera Term**][link-tera_term]  or  &#10004; [**Hercules**][link-hercules]



## Step 2: Prepare hardware

If you are using WIZnet's PICO board, you can skip '1. Combine...'

1. If you are using WIZnet Ethernet HAT, Combine it with Raspberry Pi Pico.

2. Connect ethernet cable to your PICO board ethernet port.

3. Connect your PICO board to desktop or laptop using USB cable. 


## Step 3: Setup LoopBack Example

> To test the **LoopBack example**, minor settings shall be done in code.


1. Initialize ethernet interface with DHCP

```python
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)
```

2. Copy **LoopBack code** to **code.py** on your RPi Pico and save. Make sure that PC is configured in same subnet 192.168.1.xxx.



## Step 4: Upload and Run

1. Check COMport in [Device Manager] and then open Serial Terminal.

![][link-port]![][link-terminal]

2. The Loopback is executed and the server waits in Listen state.

![][link-loopback_1]

3. Open the Hercules program to set **[IP Address]** and **[PORT number]** and Connect to the Server.

![][link-loopback_2]

4. You can confirm that the client has connected to the server.

![][link-loopback_3]

5. If you send the phrase Loopback Test, you can see that you are sending and receiving data.

![][link-loopback_4]



## Attach

Attach a flow that operates through [WIRESHARK][link-wireshark].

- [Loopback.pcapng](https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/examples/Loopback/Loopback.pcapng)




 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)





<!--
Link
-->

[link-tera_term]: https://osdn.net/projects/ttssh2/releases/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility
[link-wireshark]: https://www.wireshark.org/#download
[link-loopback_0]: https://github.com/Wiznet-OpenHardware/RP2040-HAT-CircuitPython/blob/main/img/LOOPBACK/Loopback.jpg



[link-port]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/PORT.jpg
[link-terminal]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/Terminal.jpg


[link-loopback_1]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/PICO_Loopback_1.jpg
[link-loopback_2]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/PICO_Loopback_2.jpg
[link-loopback_3]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/PICO_Loopback_3.jpg
[link-loopback_4]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/LOOPBACK/PICO_Loopback_4.jpg
