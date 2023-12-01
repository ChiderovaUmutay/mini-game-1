import random


def run():
    robot, hero = get_characters_data()
    while robot.get("hp") > 0:
        hit_probability = random.randint(1, 100)
        if hit_probability >= 25:
            hero_gun = hero.get("gun")
            robot_defence = robot.get("defence")
            damage = hero_gun - robot_defence
            robot = modify_health(robot, -damage)
            display_robot_info(robot.get("hp"), damage)
        else:
            print("The hero didn't hit\n\n")


def get_characters_data():
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


def modify_health(robot, dmg):
    robot["hp"] = robot.get("hp") + dmg
    return robot


def display_robot_info(hp, damage):
    message = f"HIT HIT HIT\n" \
              f"Робот получил {damage} ед. урона\n" \
              f"Остаток здоровье робота составляет {hp} ед.\n"
    message += "\nGame over!" if hp == 0 else "\n"
    print(message)

if __name__ == "__main__":
    run()
