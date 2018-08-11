import paho.mqtt.client as mqtt
try:
    import pixels
    led = pixels.pixels
except:
    from pixel_ring import pixel_ring
    led = pixel_ring
    from gpiozero import LED
    power = LED(5)
    power.on() 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/broker/version")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "hermes/hotword/toggleOff":
        led.wakeup()
    elif msg.topic == "hermes/hotword/toggleOn":
        led.off()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

topics = [("hermes/intent/#", 0), ("hermes/hotword/#", 0), ("hermes/asr/#", 0), ("hermes/nlu/#", 0),
                  ("snipsmanager/#", 0)]


client.subscribe(topics)

client.loop_forever()

try:
    power.off()
except:
    pass


# MQTT_TOPIC_NLU = "hermes/nlu/"
# MQTT_TOPIC_HOTWORD = "hermes/hotword/"
# MQTT_TOPIC_ASR = "hermes/asr/"
# MQTT_TOPIC_DIALOG_MANAGER = "hermes/dialogueManager/"
# MQTT_TOPIC_SNIPSFILE = "snipsskills/setSnipsfile/"
# MQTT_TOPIC_INTENT = "hermes/intent/"
# MQTT_TOPIC_SESSION_QUEUED = MQTT_TOPIC_DIALOG_MANAGER + "sessionQueued"
# MQTT_TOPIC_SESSION_STARTED = MQTT_TOPIC_DIALOG_MANAGER + "sessionStarted"
# MQTT_TOPIC_SESSION_ENDED = MQTT_TOPIC_DIALOG_MANAGER + "sessionEnded"
