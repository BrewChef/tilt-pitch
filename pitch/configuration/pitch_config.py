import json
import os

class PitchConfig:

    def __init__(self, data: dict):
        # Webhook
        self.webhook_urls = list()
        # File Path
        self.log_file_path = 'pitch_log.json'
        self.log_file_max_mb = 10
        # Prometheus
        self.prometheus_enabled = True
        self.prometheus_port = 8000
        # InfluxDB
        self.influxdb_hostname = None
        self.influxdb_database = None
        self.influxdb_port = None
        self.influxdb_username = None
        self.influxdb_password = None
        self.influxdb_batch_size = 10
        self.influxdb_timeout_seconds = 5
        # Simulations
        self.simulate_beacons = False
        # Load user inputs from config file
        self.update(data)

    def update(self, data: dict):
        self.__dict__.update(data)

    def get_original_gravity(self, color: str):
        return self.__dict__.get(color + '_original_gravity')

    def get_brew_name(self, color: str):
        return self.__dict__.get(color + '_name', color)


    @staticmethod
    def load(additional_config: dict = None):
        file_path = "pitch.json"
        config_raw = dict()

        if os.path.isfile(file_path):
            file_open = open(file_path, "r").read()
            config_raw = json.loads(file_open)

        config = PitchConfig(config_raw)
        if additional_config is not None:
            config.update(additional_config)

        return config

