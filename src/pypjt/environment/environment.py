from .geometry import Geometry
from ..robot import Robot
from ..common import get_logger


class Environment:
    def __init__(self):
        self.logger = get_logger()

    def load_from_file(self):
        self.logger.info("Load from file.")

    def save_to_file(self):
        self.logger.info("Save to file.")

    def add_body(self, body: Geometry):
        self.logger.info("Add body.")

    def remove_body(self):
        self.logger.info("Remove body.")

    def add_robot(self, robot: Robot):
        self.logger.info("Add robot.")
    
    def remove_robot(self):
        self.logger.info("Remove robot.")