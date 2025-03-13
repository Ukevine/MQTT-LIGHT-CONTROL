import paho.mqtt.client as mqtt # type: ignore

BROKER = "broker.hivemq.com"  # Alternative broker
PORT = 1883
TOPIC = "/student_group/light_control"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"✅ Connected with result code {reason_code}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"📩 Received: {msg.topic} → {msg.payload.decode()}")

def on_log(client, userdata, level, buf):
    print(f"🔍 MQTT Log: {buf}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="MyClientID")
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log  # Debug logs

try:
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
except Exception as e:
    print(f"❌ Connection Failed: {e}")
