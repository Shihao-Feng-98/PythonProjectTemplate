def test_path_planner():
    from pypjt.environment import Environment, Box
    from pypjt import Robot
    from pypjt.planner import PathPlanner

    env = Environment()
    env.add_body(Box())
    robot = Robot()
    path_planner = PathPlanner(env, robot)
    assert path_planner.plan_path() == None
