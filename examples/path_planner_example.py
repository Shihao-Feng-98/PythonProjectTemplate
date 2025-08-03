from pypjt.environment import Environment, Box
from pypjt import Robot
from pypjt.planner import PathPlanner


def main():
    env = Environment()
    env.add_body(Box())
    robot = Robot()
    path_planner = PathPlanner(env, robot)
    path_planner.plan_path()

if __name__ == "__main__":
    main()