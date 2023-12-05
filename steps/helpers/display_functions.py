from helpers.info_messages import hero_info_messages, robot_info_messages
from helpers.variables import HERO_WAS_INJURED_EVENT, \
    HERO_FINISHED_EVENT, \
    ROBOT_WAS_INJURED_EVENT, \
    ROBOT_FINISHED_EVENT

def display_hero_info(event: str, args=None) -> None or str:
    if event == HERO_WAS_INJURED_EVENT:
        display_character_info(args,
                               character_messages=hero_info_messages,
                               consts=[HERO_WAS_INJURED_EVENT, HERO_FINISHED_EVENT])
    elif event == HERO_FINISHED_EVENT:
        return hero_info_messages.get(HERO_FINISHED_EVENT).format(args)
    else:
        print(hero_info_messages.get(event).format(args) if args is not None else hero_info_messages.get(event))

def display_robot_info(event: str, args=None) -> None or str:
    if event == ROBOT_WAS_INJURED_EVENT:
        display_character_info(args,
                               character_messages=robot_info_messages,
                               consts=[ROBOT_WAS_INJURED_EVENT, ROBOT_FINISHED_EVENT])
    elif event == ROBOT_FINISHED_EVENT:
        robot_hp = args
        return robot_info_messages.get(ROBOT_FINISHED_EVENT).format(robot_hp)
    else:
        print(robot_info_messages.get(event))

def display_character_info(args: list, character_messages: dict, consts: list):
    dmg, hp = args[0], args[1]
    damage_const, health_const = consts[0], consts[1]
    damage_info_message = character_messages.get(damage_const).format(dmg)
    health_info_message = character_messages.get(health_const).format(hp)
    print(f"{damage_info_message}{health_info_message}")