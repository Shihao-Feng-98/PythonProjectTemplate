import time
from ..common import get_logger, timer
from ..environment import Environment
from ..robot import Robot
from ..collision import CollisionChecker


class PathPlanner:
    def __init__(self, env: Environment, robot: Robot):
        self.logger = get_logger()
        self.env = env
        self.robot = robot
        self.collision_checker = CollisionChecker()

    @timer
    def plan_path(self):
        time.sleep(1.)
        self.logger.info("Plan path.")