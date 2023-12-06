import inspect
import random
import time

from helpers.display_functions import display_hero_info, display_robot_info
from helpers.info_messages import GAME_RESULTS_MESSAGE, WIN_MESSAGE, FAREWELL_MESSAGE, WELCOME_MESSAGE
from helpers.variables import HERO_FINISHED_EVENT, \
    HERO_CHARACTER_NAME, \
    HERO_ATTACKS_EVENT, \
    HERO_MISSED_EVENT, \
    HERO_WAS_INJURED_EVENT, \
    ROBOT_FINISHED_EVENT, \
    ROBOT_CHARACTER_NAME, \
    ROBOT_MISSES_TURN_EVENT, \
    ROBOT_USE_HOMING_MISSILES_EVENT, \
    ROBOT_USE_REGULAR_CARTRIDGES_EVENT, \
    ROBOT_MISSED_EVENT, \
    ROBOT_JAMMED_EVENT, \
    ROBOT_WAS_INJURED_EVENT, robot_data, hero_data


def run() -> None:
    print(WELCOME_MESSAGE)
    robot, hero = robot_data, hero_data
    while hero.get("hp") > 0:
        robot = hero_turn(hero, robot)
        time.sleep(5)
        if robot.get("hp") > 0:
            hero = robot_turn(robot, hero)
            time.sleep(5)
        else:
            break
    hero_health_info = display_hero_info(HERO_FINISHED_EVENT, hero.get("hp") if hero.get("hp") >= 0 else 0)
    robot_health_info = display_robot_info(ROBOT_FINISHED_EVENT, robot.get("hp") if robot.get("hp") >= 0 else 0)
    winner_character = ROBOT_CHARACTER_NAME if robot.get('hp') > 0 else HERO_CHARACTER_NAME
    print(f'{GAME_RESULTS_MESSAGE}{hero_health_info}{robot_health_info}{WIN_MESSAGE.format(winner_character)}')


def hero_turn(hero: dict, robot: dict) -> dict:
    display_hero_info(HERO_ATTACKS_EVENT)
    hit_probability = random.randint(1, 100)
    if hit_probability >= 25:
        hero_gun = hero.get("gun")
        robot_defence = robot.get("defence")
        damage = hero_gun - robot_defence
        robot = modify_robot_health(robot, -damage)
    else:
        display_hero_info(HERO_MISSED_EVENT)
    return robot


def robot_turn(robot: dict, hero: dict) -> dict:
    action_probability = random.randint(1, 100)
    if action_probability <= 33:
        actions = [use_homing_missiles, use_regular_cartridges, robot_jam]
        action = random.choice(actions)
        if inspect.getfullargspec(action).args:
            hero = action(robot, hero)
        else:
            action()
    else:
        display_robot_info(ROBOT_MISSES_TURN_EVENT)
    return hero


def use_homing_missiles(robot: dict, hero: dict) -> dict:
    robot_gun = robot.get("gun")
    one_third_robot_gun = (robot_gun / 30) * 100
    hero_defence = hero.get("defence")
    damage = robot_gun + one_third_robot_gun - hero_defence
    display_robot_info(ROBOT_USE_HOMING_MISSILES_EVENT)
    hero = modify_hero_health(hero, -damage)
    return hero


def use_regular_cartridges(robot: dict, hero: dict) -> dict:
    display_robot_info(ROBOT_USE_REGULAR_CARTRIDGES_EVENT)
    hit_probability = random.randint(1, 100)
    if hit_probability >= 50:
        robot_gun = robot.get("gun")
        hero_defence = hero.get("defence")
        damage = robot_gun - hero_defence
        hero = modify_hero_health(hero, -damage)
    else:
        display_robot_info(ROBOT_MISSED_EVENT)
    return hero


def robot_jam() -> None:
    display_robot_info(ROBOT_JAMMED_EVENT)


def modify_robot_health(robot: dict, dmg: int) -> dict:
    robot["hp"] += dmg
    data_for_message = [str(dmg).replace("-", ""), robot.get("hp") if robot.get("hp") >= 0 else 0]
    display_robot_info(ROBOT_WAS_INJURED_EVENT, data_for_message)
    return robot


def modify_hero_health(hero: dict, dmg: int) -> dict:
    hero["hp"] += dmg
    data_for_message = [str(dmg).replace("-", ""), hero.get("hp") if hero.get("hp") >= 0 else 0]
    display_hero_info(HERO_WAS_INJURED_EVENT, data_for_message)
    return hero


if __name__ == "__main__":
    try:
        run()
    except:
        print(FAREWELL_MESSAGE)
