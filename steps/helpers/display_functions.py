from helpers.info_messages import hero_info_messages, robot_info_messages
from helpers.variables import HERO_WAS_INJURED_EVENT, \
    HERO_FINISHED_EVENT, \
    ROBOT_WAS_INJURED_EVENT, \
    ROBOT_FINISHED_EVENT

def display_hero_info(event: str, args=None) -> None or str:
    if args is not None:
        if event == HERO_WAS_INJURED_EVENT:
            display_character_info(args,
                                   character_messages_dict=hero_info_messages,
                                   consts=[HERO_WAS_INJURED_EVENT, HERO_FINISHED_EVENT])
        elif event == HERO_FINISHED_EVENT:
            hero_hp = args
            return hero_info_messages.get(HERO_FINISHED_EVENT).format(hero_hp)
        else:
            print(hero_info_messages.get(event).format(args))
    else:
        print(hero_info_messages.get(event))

def display_robot_info(event: str, args=None) -> None or str:
    if event == ROBOT_WAS_INJURED_EVENT:
        display_character_info(args,
                               character_messages_dict=robot_info_messages,
                               consts=[ROBOT_WAS_INJURED_EVENT, ROBOT_FINISHED_EVENT])
    elif event == ROBOT_FINISHED_EVENT:
        robot_hp = args
        return robot_info_messages.get(ROBOT_FINISHED_EVENT).format(robot_hp)
    else:
        print(robot_info_messages.get(event))

def display_character_info(args, character_messages_dict, consts):
    dmg, hp = args[0], args[1]
    damage_const, health_const = consts[0], consts[1]
    damage_info_message = character_messages_dict.get(damage_const).format(dmg)
    health_info_message = character_messages_dict.get(health_const).format(hp)
    print(f"{damage_info_message}{health_info_message}")