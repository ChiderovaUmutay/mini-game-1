import random
import time

from helpers.display_functions import display_hero_info, display_robot_info
from helpers.info_messages import WELCOME_MESSAGE, FAREWELL_MESSAGE, ROUND_INFO
from helpers.variables import robot_data, hero_data, \
    HERO_MISS_PERCENTAGE, \
    HERO_ATTACKS_EVENT, \
    HERO_MISSED_EVENT, \
    ROBOT_WAS_INJURED_EVENT

def run() -> None:
    print(WELCOME_MESSAGE)
    robot, hero = robot_data, hero_data
    round_count = 0
    while robot.get("hp") > 0:
        round_count += 1
        print(ROUND_INFO.format(round_count))
        time.sleep(1)
        display_hero_info(HERO_ATTACKS_EVENT)
        hit_probability = random.randint(1, 100)
        if hit_probability >= HERO_MISS_PERCENTAGE:
            hero_gun = hero.get("gun")
            robot_defence = robot.get("defence")
            damage = hero_gun - robot_defence
            robot = modify_health(robot, -damage)
        else:
            display_hero_info(HERO_MISSED_EVENT)
def modify_health(robot: dict, dmg: int) -> dict:
    robot["hp"] += dmg
    data_for_message = [str(dmg).replace("-", ""), robot.get("hp") if robot.get("hp") >= 0 else 0]
    display_robot_info(ROBOT_WAS_INJURED_EVENT, data_for_message)
    return robot

if __name__ == "__main__":
    try:
        run()
    except:
        print(FAREWELL_MESSAGE)
