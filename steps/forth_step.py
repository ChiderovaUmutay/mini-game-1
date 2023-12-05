import inspect
import random

from helpers.display_functions import display_hero_info, display_robot_info
from helpers.info_messages import GAME_RESULTS_MESSAGE, WIN_MESSAGE
from helpers.variables import HERO_FINISHED_EVENT, \
    HERO_CHARACTER_NAME, \
    HERO_ATTACKS_EVENT, \
    HERO_MISSED_EVENT, \
    HERO_MISSES_TURN_EVENT, \
    HERO_DEFENDS_HIMSELF_EVENT, \
    HERO_DEACTIVATE_PROTECTED_FIELD_EVENT, \
    HERO_WAS_INJURED_EVENT, \
    ROBOT_FINISHED_EVENT, \
    ROBOT_CHARACTER_NAME, \
    ROBOT_MISSES_TURN_EVENT, \
    ROBOT_USE_HOMING_MISSILES_EVENT, \
    ROBOT_USE_REGULAR_CARTRIDGES_EVENT, \
    ROBOT_MISSED_EVENT, \
    ROBOT_JAMMED_EVENT, \
    ROBOT_WAS_INJURED_EVENT, HERO_REPELLED_ATTACK, ROBOT_THROW_POISON_GRENADE


def run() -> None:
    robot, hero = get_characters_data()
    while hero.get("hp") > 0:
        character_data, character_name = hero_turn(hero, robot)
        if character_name == ROBOT_CHARACTER_NAME:
            robot = character_data
        else:
            hero = character_data
        if robot.get("hp") > 0:
            hero = robot_turn(robot, hero)
            remove_shield(hero) if hero.get("has_shield") is True else None
        else:
            break
    hero_health_info = display_hero_info(HERO_FINISHED_EVENT, hero.get("hp") if hero.get("hp") >= 0 else 0)
    robot_health_info = display_robot_info(ROBOT_FINISHED_EVENT, robot.get("hp") if robot.get("hp") >= 0 else 0)
    winner_character = ROBOT_CHARACTER_NAME if robot.get('hp') > 0 else HERO_CHARACTER_NAME
    print(f'{GAME_RESULTS_MESSAGE}{hero_health_info}{robot_health_info}{WIN_MESSAGE.format(winner_character)}')


def get_characters_data() -> (dict, dict):
    robot = {
        "hp": 1300,  # жизненная энергия, запас здоровья
        "defence": 120,  # защита, броня
        "gun": 300  # оружие
    }
    hero = {
        "hp": 2000,
        "defence": 100,
        "gun": 250,
        "protective_field": 150,  # защитное поле
        "has_shield": False
    }
    return robot, hero


def hero_turn(hero: dict, robot: dict) -> (dict, str):
    actions = [hero_attack, hero_defence, hero_pass]
    action = random.choice(actions)
    if len(inspect.getfullargspec(action).args) == 2:
        robot = action(hero, robot)
        return robot, ROBOT_CHARACTER_NAME
    elif len(inspect.getfullargspec(action).args) == 1:
        hero = action(hero)
    elif len(inspect.getfullargspec(action).args) == 0:
        action()
    return hero, HERO_CHARACTER_NAME


def hero_attack(hero: dict, robot: dict) -> dict:
    hit_probability = random.randint(1, 100)
    if hit_probability >= 25:
        hero_gun = hero.get("gun")
        robot_defence = robot.get("defence")
        damage = hero_gun - robot_defence
        display_hero_info(HERO_ATTACKS_EVENT)
        robot = modify_robot_health(robot, -damage)
    else:
        display_hero_info(HERO_MISSED_EVENT)
    return robot


def hero_defence(hero: dict) -> dict:
    return equip_shield(hero)


def hero_pass() -> None:
    display_hero_info(HERO_MISSES_TURN_EVENT)


def equip_shield(hero: dict) -> dict:
    hero["defence"] = hero.get("protective_field") + hero.get("defence")
    hero["has_shield"] = True
    display_hero_info(HERO_DEFENDS_HIMSELF_EVENT, hero.get("defence"))
    return hero


def remove_shield(hero: dict) -> dict:
    hero["defence"] = hero.get("defence") - hero.get("protective_field")
    hero["has_shield"] = False
    display_hero_info(HERO_DEACTIVATE_PROTECTED_FIELD_EVENT)
    return hero


def robot_turn(robot: dict, hero: dict) -> dict:
    action_probability = random.randint(1, 100)
    if action_probability <= 33:
        actions = [robot_use_homing_missiles, robot_use_regular_cartridges, robot_throw_grenade, robot_jam]
        action = random.choice(actions)
        if inspect.getfullargspec(action).args:
            hero = action(robot, hero)
        else:
            action()
    else:
        display_robot_info(ROBOT_MISSES_TURN_EVENT)
    return hero


def robot_use_homing_missiles(robot: dict, hero: dict) -> dict:
    robot_gun = robot.get("gun")
    one_third_robot_gun = (robot_gun / 30) * 100
    damage = robot_gun + one_third_robot_gun - hero.get("defence")
    display_robot_info(ROBOT_USE_HOMING_MISSILES_EVENT)
    hero = modify_hero_health(hero, -damage)
    return hero


def robot_use_regular_cartridges(robot: dict, hero: dict) -> dict:
    hit_probability = random.randint(1, 100)
    if hit_probability >= 50:
        damage = robot.get("gun") - hero.get("defence")
        display_robot_info(ROBOT_USE_REGULAR_CARTRIDGES_EVENT)
        hero = modify_hero_health(hero, -damage)
    else:
        display_robot_info(ROBOT_MISSED_EVENT)
    return hero


def robot_throw_grenade(robot: dict, hero: dict):
    hit_probability = random.randint(1, 100)
    if hit_probability <= 25:
        display_robot_info(ROBOT_THROW_POISON_GRENADE)
        if hero.get("has_shield") is False:
            damage = robot.get("gun") * 2
            hero = modify_hero_health(hero, -damage)
        else:
            display_hero_info(HERO_REPELLED_ATTACK)
    else:
        display_robot_info(ROBOT_MISSED_EVENT)
    return hero


def robot_jam() -> None:
    display_robot_info(ROBOT_JAMMED_EVENT)


def modify_robot_health(robot: dict, dmg: int) -> dict:
    robot["hp"] = robot.get("hp") + dmg
    data_for_message = [str(dmg).replace("-", ""), robot.get("hp") if robot.get("hp") >= 0 else 0]
    display_robot_info(ROBOT_WAS_INJURED_EVENT, data_for_message)
    return robot


def modify_hero_health(hero: dict, dmg: int) -> dict:
    hero["hp"] = hero.get("hp") + dmg
    data_for_message = [str(dmg).replace("-", ""), hero.get("hp") if hero.get("hp") >= 0 else 0]
    display_hero_info(HERO_WAS_INJURED_EVENT, data_for_message)
    return hero


if __name__ == "__main__":
    run()
