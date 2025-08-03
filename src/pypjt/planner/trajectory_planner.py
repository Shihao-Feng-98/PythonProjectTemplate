import time
from ..common import get_logger, timer


class TrajectoryPlanner:
    def __init__(self):
        self.logger = get_logger()

    @timer
    def plan_traj(self):
        time.sleep(1.)
        self.logger.info("Plan trajectory.")