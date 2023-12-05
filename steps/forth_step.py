import inspect
import random
import time

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
    HERO_REPELLED_ATTACK_EVENT, \
    HERO_INJECTED_ADRENALINE_EVENT, \
    ADRENALINE_QTY_INFO, \
    ROBOT_FINISHED_EVENT, \
    ROBOT_CHARACTER_NAME, \
    ROBOT_MISSES_TURN_EVENT, \
    ROBOT_USE_HOMING_MISSILES_EVENT, \
    ROBOT_USE_REGULAR_CARTRIDGES_EVENT, \
    ROBOT_MISSED_EVENT, \
    ROBOT_JAMMED_EVENT, \
    ROBOT_WAS_INJURED_EVENT, \
    ROBOT_THROW_POISON_GRENADE, ADRENALINE_ENDED, robot_data, hero_data


def run() -> None:
    robot, hero = robot_data, hero_data
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
    hero_health_info = display_hero_info(HERO_FINISHED_EVENT, round(hero.get("hp")) if hero.get("hp") >= 0 else 0)
    robot_health_info = display_robot_info(ROBOT_FINISHED_EVENT, round(robot.get("hp")) if robot.get("hp") >= 0 else 0)
    winner_character = ROBOT_CHARACTER_NAME if robot.get('hp') > 0 else HERO_CHARACTER_NAME
    print(f'{GAME_RESULTS_MESSAGE}{hero_health_info}{robot_health_info}{WIN_MESSAGE.format(winner_character)}')


def hero_turn(hero: dict, robot: dict) -> (dict, str):
    actions = [hero_attack, hero_defence, hero_pass, hero_injected_adrenaline]
    action = random.choice(actions)
    if len(inspect.getfullargspec(action).args) == 2:
        character_data, character_name = action(hero, robot)
        time.sleep(5)
        return character_data, character_name
    elif len(inspect.getfullargspec(action).args) == 1:
        hero = action(hero)
        time.sleep(5)
        return hero, HERO_CHARACTER_NAME
    elif len(inspect.getfullargspec(action).args) == 0:
        action()
        time.sleep(5)
        return hero, HERO_CHARACTER_NAME


def hero_attack(hero: dict, robot: dict) -> (dict, str):
    hit_probability = random.randint(1, 100)
    if hit_probability >= 25:
        hero_gun = hero.get("gun")
        robot_defence = robot.get("defence")
        damage = hero_gun - robot_defence
        display_hero_info(HERO_ATTACKS_EVENT)
        robot = modify_robot_health(robot, -damage)
    else:
        display_hero_info(HERO_MISSED_EVENT)
    return robot, ROBOT_CHARACTER_NAME


def hero_defence(hero: dict) -> dict:
    return equip_shield(hero)


def hero_pass() -> None:
    display_hero_info(HERO_MISSES_TURN_EVENT)


def hero_injected_adrenaline(hero, robot):
    adrenaline = hero.get("adrenaline", 0)
    if adrenaline > 0:
        hero = modify_hero_health(hero, hero.get("adrenaline_power"))
        hero["adrenaline"] -= 1
        display_hero_info(HERO_INJECTED_ADRENALINE_EVENT)
        print(display_hero_info(HERO_FINISHED_EVENT, hero.get("hp")))
        display_hero_info(ADRENALINE_QTY_INFO, hero.get("adrenaline"))
        return hero, HERO_CHARACTER_NAME
    else:
        display_hero_info(ADRENALINE_ENDED)
        return hero_turn(hero, robot)


def equip_shield(hero: dict) -> dict:
    hero["defence"] += hero.get("protective_field")
    hero["has_shield"] = True
    display_hero_info(HERO_DEFENDS_HIMSELF_EVENT, hero.get("defence"))
    return hero


def remove_shield(hero: dict) -> dict:
    hero["defence"] -= hero.get("protective_field")
    hero["has_shield"] = False
    display_hero_info(HERO_DEACTIVATE_PROTECTED_FIELD_EVENT)
    return hero


def robot_turn(robot: dict, hero: dict) -> dict:
    action_probability = random.randint(1, 100)
    if action_probability <= 33:
        actions = [robot_use_homing_missiles, robot_use_regular_cartridges, robot_throw_grenade, robot_jam]
        action = random.choice(actions)
        if len(inspect.getfullargspec(action).args) > 0:
            hero = action(robot, hero)
        else:
            action()
    else:
        display_robot_info(ROBOT_MISSES_TURN_EVENT)
    time.sleep(5)
    return hero


def robot_use_homing_missiles(robot: dict, hero: dict) -> dict:
    robot_gun = robot.get("gun")
    one_third_robot_gun = (robot_gun / 30) * 100
    damage = robot_gun + one_third_robot_gun - hero.get("defence")
    display_robot_info(ROBOT_USE_HOMING_MISSILES_EVENT)
    hero = modify_hero_health(hero, -damage)
    data_for_message = [damage, hero.get("hp") if hero.get("hp") >= 0 else 0]
    display_hero_info(HERO_WAS_INJURED_EVENT, data_for_message)
    return hero


def robot_use_regular_cartridges(robot: dict, hero: dict) -> dict:
    hit_probability = random.randint(1, 100)
    if hit_probability >= 50:
        damage = robot.get("gun") - hero.get("defence")
        display_robot_info(ROBOT_USE_REGULAR_CARTRIDGES_EVENT)
        hero = modify_hero_health(hero, -damage)
        data_for_message = [damage, hero.get("hp") if hero.get("hp") >= 0 else 0]
        display_hero_info(HERO_WAS_INJURED_EVENT, data_for_message)
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
            data_for_message = [damage, hero.get("hp") if hero.get("hp") >= 0 else 0]
            display_hero_info(HERO_WAS_INJURED_EVENT, data_for_message)
        else:
            display_hero_info(HERO_REPELLED_ATTACK_EVENT)
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
    return hero


if __name__ == "__main__":
    run()
