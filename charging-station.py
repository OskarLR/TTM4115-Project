import paho.mqtt.client as mqtt
import logging
import json
from appJar import gui

# TODO: choose proper MQTT broker address
MQTT_BROKER = 'mqtt20.iik.ntnu.no'
MQTT_PORT = 1883

# Updated MQTT topics for e-scooter system
MQTT_TOPIC_INPUT = 'ttm4115/team_17/charging_command'
MQTT_TOPIC_OUTPUT = 'ttm4115/team_17/charging_status'


class ChargingStationComponent:
    """
    The component to manage charging stations.
    """

    def on_connect(self, client, userdata, flags, rc):
        # Log that we are connected
        self._logger.debug('MQTT connected to {}'.format(client))

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        self._logger.info(f"Received message: {payload}")
        if payload["command"] == "start_charging":
            scooter_id = payload["scooter_id"]
            self._logger.info(f"Starting charging for scooter {scooter_id}")
            # Simulate starting charging
            response = {"scooter_id": scooter_id, "status": "charging"}
            self.mqtt_client.publish(MQTT_TOPIC_OUTPUT, json.dumps(response))
        elif payload["command"] == "get_charging_status":
            scooter_id = payload["scooter_id"]
            self._logger.info(f"Getting charging status for scooter {scooter_id}")
            # Simulate charging status
            response = {"scooter_id": scooter_id, "status": "fully_charged"}
            self.mqtt_client.publish(MQTT_TOPIC_OUTPUT, json.dumps(response))

    def __init__(self):
        # Get the logger object for the component
        self._logger = logging.getLogger(__name__)
        print('logging under name {}.'.format(__name__))
        self._logger.info('Starting Component')

        # Create a new MQTT client
        self._logger.debug('Connecting to MQTT broker {} at port {}'.format(MQTT_BROKER, MQTT_PORT))
        self.mqtt_client = mqtt.Client()
        # Callback methods
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        # Connect to the broker
        self.mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
        # Start the internal loop to process MQTT messages
        self.mqtt_client.loop_start()

    def stop(self):
        """
        Stop the component.
        """
        # Stop the MQTT client
        self.mqtt_client.loop_stop()

# Logging configuration
debug_level = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(debug_level)
ch = logging.StreamHandler()
ch.setLevel(debug_level)
formatter = logging.Formatter('%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

t = ChargingStationComponent()