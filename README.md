# Hometemp

TO DO: This is a super quick and dirty dump to GitHub of my project.  Clean this bad boy up and make it presentable!

A project to attach one or many MAX31850 Thermocouple Aplifiers to a Raspberry Pi

### Wiring

#### One MAX31850 Thermocouple Amplifier

![Raspberry Pi + one MAX31850 Thermocouple Amplifier](Resources/Raspberry Pi + MAX31850 Thermocouple Amplifier_bb.png)

##### Many MAX31850 Thermocouple Amplifiers
 
![Raspberry Pi + many MAX31850 Thermocouple Amplifiers](Resources/Raspberry Pi + MAX31850 Thermocouple Amplifiers_bb.png)

### Configure Raspberry Pi

The Raspberry Pi must be configured to support 1-Wire devices.
```
sudo nano /boot/config.txt
```
Append file with the following lines:
'# Enable OneWire support'
'dtoverlay=w1-gpio'

![/boot/config.txt](Resources/2-12-2016 3-48-50 PM.png)

The Raspberry Pi must also be configured to load the drivers at startup.

```
sudo nano /etc/modules
```

Append file with the following lines:

'w1-gpio'
'w1-therm'

![/etc/modules](Resources/2-12-2016 3-46-49 PM.png)

Reboot the Raspberry Pi

```
sudo reboot
```

Test that the drivers have loaded and the thermocouple amplifiers have been detected.

```
ls /sys/bus/w1/devices
```

You should see a list of your devices.

![ls /sys/bus/w1/devices](Resources/2-12-2016 4-04-11 PM.png)

Test one of the devices
```
cat /sys/bus/w1/devices/3b-000000183532/w1_slave
```

![cat /sys/bus/w1/devices/3b-000000183532/w1_slave](Resources/2-12-2016 4-05-53 PM.png)
