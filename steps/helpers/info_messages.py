hero_info_messages: dict = {
    "hero_took_damage": "HIT! HIT! HIT!\nThe hero received {} units damage!\n",
    "hero_health_info": "The hero's remaining health is {} units.\n",
    "hero_missed": "The hero missed!\n",
    "hero_misses_turn": "The hero misses a turn!\n",
    "hero_attacks": "Hero attacks!\n",
    "hero_defends_himself": "The hero defends himself and activates a protective field, the strength of which is equal to {}!\n",
    "hero_deactivate_protected_field": "The hero removed the protective field!\n",
    "hero_repelled_attack": "The hero repelled the attack with a protective field!\n",
    "hero_injected_adrenaline": "The hero injected adrenaline!\n",
    "adrenaline_qty_info": "The number of syringes with adrenaline in the backpack is equal to {}!\n",
    "adrenaline_ended_info": "The syringes with adrenaline have run out!\nThe hero makes a second move.\n"
}

robot_info_messages: dict = {
    "robot_took_damage": "HIT! HIT! HIT!\nThe robot received {} units damage!\n",
    "robot_health_info": "The robot's remaining health is {} units.\n",
    "robot_missed": "The robot missed!\n",
    "robot_misses_turn": "The robot skips a turn!\n",
    "robot_use_homing_missiles": "The robot uses homing missiles!\n",
    "robot_use_regular_cartridges": "The robot uses regular ammunition!\n",
    "robot_throw_poison_grenade": "The robot threw a poison grenade!\n",
    "robot_jammed": "The robot is jammed!\n"
}

WELCOME_MESSAGE = f"{'-' * 30}👽 🆚 🤖{'-' * 30}\n"
FAREWELL_MESSAGE = "\nThe game has stopped.\nGood luck👋🏻"
INPUT_MESSAGE = "Enter one of actions ({}):\n"
REPEAT_INPUT_MESSAGE = "Please enter an action from the list provided."
GAME_RESULTS_MESSAGE = f"{'-' * 15}GAME RESULTS{'-' * 15}\n"
WIN_MESSAGE = "{} WON!!!"
