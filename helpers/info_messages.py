hero_info_messages: dict = {
    "hero_attacks": "👽🚀 ACTION: Hero attacks!\n",
    "hero_defends_himself": "👽🚀 ACTION: The hero defends himself and activates a protective field, the strength of which is equal to {}!\n",
    "hero_injected_adrenaline": "👽🚀 ACTION: The hero injected adrenaline!\n",
    "hero_skips_turn": "👽🚀 ACTION: The hero skips a turn!\n",
    "hero_took_damage": "🤖📈 RESULT: HIT💥 HIT💥 HIT💥\n👽📌 INFO: The hero received {} units damage!\n",
    "hero_missed": "👽📈 RESULT: The hero missed!\n",
    "hero_repelled_attack": "👽📈 RESULT: The hero repelled the attack with a protective field!\n",
    "hero_deactivate_protected_field": "👽📌 INFO: The hero removed the protective field!\n",
    "adrenaline_qty_info": "👽📌 INFO: The number of syringes with adrenaline in the backpack is equal to {}!\n",
    "adrenaline_ended_info": "👽📌 INFO: The syringes with adrenaline have run out!\nThe hero makes a second move.\n",
    "hero_health_info": "👽💊 HEALTH INFO: The hero's remaining health is {} units.\n",
}

robot_info_messages: dict = {
    "robot_skips_turn": "🤖🚀 ACTION: The robot skips a turn!\n",
    "robot_use_homing_missiles": "🤖🚀 ACTION: The robot uses homing missiles!\n",
    "robot_use_regular_cartridges": "🤖🚀 ACTION: The robot uses regular ammunition!\n",
    "robot_throw_poison_grenade": "🤖🚀 ACTION: The robot threw a poison grenade!\n",
    "robot_jammed": "🤖🚀 ACTION: The robot is jammed!\n",
    "robot_missed": "🤖📈 RESULT: The robot missed!\n",
    "robot_took_damage": "👽📈 RESULT: HIT💥 HIT💥 HIT💥\n🤖📌 INFO: The robot received {} units damage!\n",
    "robot_health_info": "🤖💊 HEALTH INFO: The robot's remaining health is {} units.\n",
}

WELCOME_MESSAGE = f"{'=' * 30}👽 🆚 🤖{'=' * 30}\n"
FAREWELL_MESSAGE = "\nThe game has stopped.\nGood luck👋🏻"
INPUT_MESSAGE = "🕹 Enter one of actions ({}):\n"
REPEAT_INPUT_MESSAGE = "🙋🏻 Please enter an action from the list provided."
GAME_RESULTS_MESSAGE = f"{'=' * 23}GAME RESULTS{'=' * 23}\n"
WIN_MESSAGE = f"{'=' * 24}" + "{} WON🏅" + f"{'=' * 24}\n"
ROUND_INFO = f"{'-' * 10}" + "ROUND #{}" + f"{'-' * 10}\n"