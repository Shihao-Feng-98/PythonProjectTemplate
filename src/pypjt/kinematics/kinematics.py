from ..common import get_logger
from ..robot import Robot
from ..utils import skew, rodrigues

class Kinematics:
    def __init__(self, robot: Robot):
        self.logger = get_logger()
        self.robot = robot
    
    def get_fk(self):
        self.logger.info("Get forward kinematics.")

    def get_ik(self):
        self.logger.info("Get inverse kinematics.")
