import random

from display_functions import display_hero_info, display_robot_info
from variables import HERO_MISSED_EVENT, HERO_ATTACKS_EVENT, ROBOT_WAS_INJURED_EVENT


def run() -> None:
    robot, hero = get_characters_data()
    while robot.get("hp") > 0:
        hit_probability = random.randint(1, 100)
        if hit_probability >= 25:
            hero_gun = hero.get("gun")
            robot_defence = robot.get("defence")
            damage = hero_gun - robot_defence
            display_hero_info(HERO_ATTACKS_EVENT)
            robot = modify_health(robot, -damage)
        else:
            display_hero_info(HERO_MISSED_EVENT)


def get_characters_data() -> (dict, dict):
    robot = {
        "hp": 1300,
        "defence": 120,
        "gun": 300
    }
    hero = {
        "hp": 2000,
        "defence": 100,
        "gun": 250,
        "protective_field": 150
    }
    return robot, hero


def modify_health(robot: dict, dmg: int) -> dict:
    robot["hp"] = robot.get("hp") + dmg
    data_for_message = [str(dmg).replace("-", ""), robot.get("hp") if robot.get("hp") >= 0 else 0]
    display_robot_info(ROBOT_WAS_INJURED_EVENT, data_for_message)
    return robot

if __name__ == "__main__":
    run()
