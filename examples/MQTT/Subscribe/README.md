# How to Test MQTT Subscribe Example

![][link-mqtt]

![][link-mqtt_0]

## Step 1: Prepare Software

> The following serial terminal program is required for **MQTT Subscribe** test, download and install from below links.

### &#10004;[**Tera Term**][link-tera_term]  or  &#10004; [**Mosquitto**][link-mosquitto]



## Step 2: Prepare hardware

If you are using WIZnet's PICO board, you can skip '1. Combine...'

1. If you are using WIZnet Ethernet HAT, Combine it with Raspberry Pi Pico.

2. Connect ethernet cable to your PICO board ethernet port.

3. Connect your PICO board to desktop or laptop using USB cable. 



## Step 3: Setup MQTT Subscribe Example

To test the **MQTT Subscribe example**, minor settings shall be done in code.


1. Initialize ethernet interface with DHCP.

```python
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)
```

2. In the MQTT configuration, the broker IP address is the IP of your desktop.

```python
# Set up a MiniMQTT Client
# NOTE: We'll need to connect insecurely for ethernet configurations.
mqtt_client = MQTT.MQTT(
    broker="192.168.1.11",  #setup your PC IP address.
    username="rpi-pico",       
    password="wiznet",      
    is_ssl=False,
    socket_pool=None,
    ssl_context=None,
    keep_alive=60,
)
```

3. going to use MQTT Subscribe.

```python
#MQTT Subscriber Run
while True:
    #mqtt_client.loop()

    #send a new message
    mqtt_client.subscribe(mqtt_topic)

    time.sleep(1)

#Disconnected
print("Disconnecting from %s" % mqtt_client.broker)
mqtt_client.disconnect()
```

4. Copy **MQTT Subscribe code** to **code.py** on your RPi Pico and save. Make sure that PC is configured in same subnet 192.168.1.xxx.



## Step 4: Upload and Run

1. Check COMport in [Device Manager] and then open Serial Terminal.

![][link-port]![][link-terminal]

2. Create broker using mosquitto by executing the following command. If the broker is created normally, the broker's IP address is the current IP of your desktop or laptop, and the port is 1883 by default.

```
mosquitto -c mosquitto.conf -p 1883 -v
```

![][link-mqtt_1]

3. If the MQTT subscribe example works normally on Raspberry Pi Pico, connecting to the broker and subscribing to the subscribe topic.

![][link-mqtt_2]

4. Join the broker with the command below and send a topic to the broker. The broker sends a message to the subscriber.

```
mosquitto_pub -h 192.168.1.11 -t WIZnetTest -m "Hello Pico, I'm broker"
```

![][link-mqtt_3]



**user manual in video** - https://www.youtube.com/watch?v=F4E-bdppvZw




## Appendix

- In Mosquitto versions earlier than 2.0 the default is to allow clients to connect without authentication. In 2.0 and up, you must choose your authentication options explicitly before clients can connect. Therefore, if you are using version 2.0 or later, refer to following link to setup 'mosquitto.conf' in the directory where Mosquitto is installed.

    - [**Authentication Methods**][link-authentication_methods]

![][link-mqtt_conf]



## Attach

Attach a flow that operates through [WIRESHARK](https://www.wireshark.org/#download).

- [MQTT_sub.pcapng](https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/examples/MQTT/Subscribe/MQTT_sub.pcapng)



 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)



<!--
Link
-->

[link-tera_term]: https://osdn.net/projects/ttssh2/releases/
[link-mosquitto]: https://mosquitto.org/download/

[link-port]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/PORT.jpg
[link-terminal]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/Terminal.jpg
[link-mqtt]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/MQTT.png
[link-mqtt_0]:https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/MQTT_0.jpg
[link-mqtt_1]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/MQTT_Sub_1.PNG
[link-mqtt_2]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/MQTT_Sub_2.PNG
[link-mqtt_3]: https://github.com/Wiznet/RP2040-HAT-CircuitPython/blob/master/images/MQTT/MQTT_Sub_3.PNG
[link-mqtt_conf]: https://github.com/Wiznet-OpenHardware/RP2040-HAT-CircuitPython/blob/main/img/MQTT/MQTT_conf.png
[link-authentication_methods]: https://mosquitto.org/documentation/authentication-methods/
