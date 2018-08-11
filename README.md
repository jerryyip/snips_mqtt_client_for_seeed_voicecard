# snips_mqtt_client_for_seeed_voicecard

## Requirements
- requests
- paho.mqtt


## Usage

1. Copy this file into /etc/systemd/system as root, for example:

```
sudo cp snips_seeed_led.service /etc/systemd/system/snips_seeed_led.service
```

2. Once this has been copied, you can attempt to start the service using the following command:

```
sudo systemctl start snips_seeed_led.service
```

Stop it using following command:

```
sudo systemctl stop snips_seeed_led.service
```

3. When you are happy that this starts and stops your app, you can have it start automatically on reboot by using this command:

```
sudo systemctl enable snips_seeed_led.service
```
