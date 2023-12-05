import inspect
import random


def run() -> None:
    robot, hero = get_characters_data()
    while hero.get("hp") > 0:
        character_data, character_name = hero_turn(hero, robot)
        if character_name == "robot":
            robot = character_data
        else:
            hero = character_data
        if robot.get("hp") > 0:
            hero = robot_turn(robot, hero)
            remove_shield(hero) if hero.get("has_shield") is True else None
        else:
            break
    hero_health_info = get_character_health_info_message(hero.get("hp"), character="героя")
    robot_health_info = get_character_health_info_message(robot.get("hp"), character="робота")
    winner_character = 'Робот' if robot.get('hp') > 0 else 'Герой'
    win_message = f"{winner_character} победил!!!"
    print(f'\n{hero_health_info}\n{robot_health_info}\n{win_message}')


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
        return robot, "robot"
    elif len(inspect.getfullargspec(action).args) == 1:
        hero = action(hero)
    elif len(inspect.getfullargspec(action).args) == 0:
        action()
    return hero, "hero"


def hero_attack(hero: dict, robot: dict) -> dict:
    hit_probability = random.randint(1, 100)
    if hit_probability >= 25:
        hero_gun = hero.get("gun")
        robot_defence = robot.get("defence")
        damage = hero_gun - robot_defence
        robot = modify_robot_health(robot, -damage)
    else:
        print("The hero didn't hit\n\n")
    return robot


def hero_defence(hero: dict) -> dict:
    return equip_shield(hero)


def hero_pass() -> None:
    print("Герой пропускает ход\n\n")


def equip_shield(hero: dict) -> dict:
    hero["defence"] = hero.get("protective_field") + hero.get("defence")
    hero["has_shield"] = True
    print(f"Герой защищается и активирует защитное поле, сила которого равна {hero.get('defence')}!")
    return hero


def remove_shield(hero: dict) -> dict:
    hero["defence"] = hero.get("defence") - hero.get("protective_field")
    hero["has_shield"] = False
    print("Герой снял защитное поле!")
    return hero


def robot_turn(robot: dict, hero: dict) -> dict:
    action_probability = random.randint(1, 100)
    if action_probability <= 33:
        actions = [robot_use_homing_missiles, robot_use_regular_cartridges, robot_jam]
        action = random.choice(actions)
        if inspect.getfullargspec(action).args:
            hero = action(robot, hero)
        else:
            action()
    else:
        print("Робот пропускает ход\n\n")
    return hero


def robot_use_homing_missiles(robot: dict, hero: dict) -> dict:
    robot_gun = robot.get("gun")
    one_third_robot_gun = (robot_gun / 30) * 100
    hero_defence = hero.get("defence")
    damage = robot_gun + one_third_robot_gun - hero_defence
    print("Робот использовал самонаводящиеся ракеты")
    hero = modify_hero_health(hero, -damage)
    return hero


def robot_use_regular_cartridges(robot: dict, hero: dict) -> dict:
    hit_probability = random.randint(1, 100)
    if hit_probability >= 50:
        robot_gun = robot.get("gun")
        hero_defence = hero.get("defence")
        damage = robot_gun - hero_defence
        print("Робот использовал патроны")
        hero = modify_hero_health(hero, -damage)
    else:
        print("Робот промазал\n\n")
    return hero


def robot_jam() -> None:
    print("Робот заклинил\n\n")


def modify_robot_health(robot: dict, dmg: int) -> dict:
    robot["hp"] = robot.get("hp") + dmg
    display_character_info(robot.get("hp"), str(dmg).replace("-", ""), character=["Робот", "робота"])
    return robot


def modify_hero_health(hero: dict, dmg: int) -> dict:
    hero["hp"] = hero.get("hp") + dmg
    display_character_info(hero.get("hp"), str(dmg).replace("-", ""), character=["Герой", "героя"])
    return hero


def display_character_info(hp: int, damage: str, character: list) -> None:
    nominative_case, genitive_case = character[0], character[1]
    character_health_info: str = get_character_health_info_message(hp, genitive_case)
    message = f'HIT HIT HIT\n' \
              f'"{nominative_case} получил {damage} ед. урона"\n' \
              f'{character_health_info}\n'
    message += "Game over!" if hp <= 0 else "\n\n"
    print(message)


def get_character_health_info_message(hp: int, character: str) -> str:
    character_hp = str(hp)
    return f'"Остаток здоровья у {character} составляет {character_hp if character_hp.startswith("-") is False else 0} ед."'


if __name__ == "__main__":
    run()
