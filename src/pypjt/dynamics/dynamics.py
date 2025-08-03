from ..common import get_logger
from ..robot import Robot

class Dynamics:
    def __init__(self, robot: Robot):
        self.logger = get_logger()
        self.robot = robot
    
    def get_fd(self):
        self.logger.info("Get forward dynamics.")

    def get_id(self):
        self.logger.info("Get inverse dynamics.")
