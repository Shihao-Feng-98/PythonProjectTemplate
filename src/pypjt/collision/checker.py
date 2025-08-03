from ..environment import Geometry
from ..common import get_logger

class CollisionChecker:
    def __init__(self):
        self.logger = get_logger()

    def add_collision_object(self, object: Geometry):
        self.logger.info("Add collision object.")

    def remove_collision_object(self):
        self.logger.info("Remove collision object.")
    
    def check_collision(self):
        self.logger.info("Check collision.")