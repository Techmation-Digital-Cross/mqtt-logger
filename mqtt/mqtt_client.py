import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

# Default mqtt client config
broker_host = os.environ.get("MQTT_BROKER_HOST", "'MQTT_BROKER_HOST' env var not found")
broker_port = os.environ.get("MQTT_BROKER_PORT", "'MQTT_BROKER_PORT' env var not found")


class MqttClient:

    CLEAN_SESSION = True
    PROTOCOL = mqtt.MQTTv311
    TRANSPORT = "tcp"

    def __init__(self, client_id, user_data, topics):
        self.client_id = client_id
        self.user_data = user_data
        self.topics = topics

    def _handle_on_connect(self, client, userdata, flags, result_code):
        print("User datas: ", userdata)
        print("Subscribing topics...")

        for topic in self.topics:
            client.subscribe(topic)
            print("Topic subscribed : " + topic)

    @staticmethod
    def _handle_on_disconnect(self, client, userdata, result_code):
        print("Client is disconnected from server.")

    def connect(self, handle_on_message):
        client = mqtt.Client(
            client_id=self.client_id,
            clean_session=self.CLEAN_SESSION,
            userdata=self.user_data,
            protocol=self.PROTOCOL,
            transport=self.TRANSPORT
        )

        client.on_connect = self._handle_on_connect
        client.on_disconnect = self._handle_on_disconnect
        client.on_message = handle_on_message
        client.connect(host=broker_host, port=int(broker_port))

        client.loop_forever()
