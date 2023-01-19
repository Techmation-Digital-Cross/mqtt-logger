import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from mqtt.mqtt_client import MqttClient

load_dotenv()

APPLICATIONS_ENV = os.environ.get("APPLICATIONS")
applications = APPLICATIONS_ENV.split(",")
service_topic = os.environ.get("SERVICE_TOPIC", "'SERVICE_TOPIC' env var not found")


def get_available_apps():
    return APPLICATIONS_ENV


class LogService:
    def __init__(self, app_name):
        self.app_name = app_name

    def start(self, service_name):
        print("--------------------Stared Services---------------------------")
        print("{:<20} {:<30} {:<30}".format('Time', 'Application', 'Service'))
        print("{:<20} {:<30} {:<30}".format(datetime.now().strftime("%H:%M:%S"), self.app_name, service_name))
        print("====================---------------===========================")

        topics = [self.app_name + "/" + service_name + service_topic]

        mqtt_client = MqttClient(
            datetime.now().strftime("%H:%M:%S") + "==" + self.app_name + "," + service_name + "client",
            {},
            topics
        )

        mqtt_client.connect(handle_on_message=self.log)

    @staticmethod
    def log(client, userdata, message):
        topic = message.topic
        app_name = topic.split("/")[0].upper()
        service_name = topic.split("/")[1].upper()
        log = message.payload.decode("utf8").replace("'", '"')

        print(app_name+"/"+service_name+" ==> " + datetime.now().strftime("%H:%M:%S") + " : " + log)

    # Checking is given service is available
    def check_service(self, service_name):
        try:
            self._is_service_available(service_name)
        except Exception as error:
            if error.args[0] == "APP_NOT_FOUND":
                print("Err", "Application not found !", sep="--")
                print("INFO", "Available applications :" + get_available_apps(), sep="--")
            elif error.args[0] == "SERVICE_NOT_FOUND":
                print("ERROR", "Service not found !", sep="---")
                print("INFO", "Available services :" + self.get_available_services(), sep="--")

            sys.exit(0)

    def _is_service_available(self, service_name):
        # Checking if application is in available applications
        if self.app_name not in applications:
            raise Exception("APP_NOT_FOUND")

        SERVICES_ENV = os.environ.get(self.app_name.upper() + "_SERVICE_NAMES")
        services = SERVICES_ENV.split(",")

        # Checking if service is in available services
        if service_name not in services:
            raise Exception("SERVICE_NOT_FOUND")

    def get_available_services(self):
        return os.environ.get(self.app_name.upper() + "_SERVICE_NAMES")
