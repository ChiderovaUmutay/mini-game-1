HERO_CHARACTER_NAME = "Герой"
HERO_WAS_INJURED_EVENT = "hero_took_damage"
HERO_FINISHED_EVENT = "hero_health_info"
HERO_MISSED_EVENT = "hero_missed"
HERO_MISSES_TURN_EVENT = "hero_misses_turn"
HERO_ATTACKS_EVENT = "hero_attacks"
HERO_DEFENDS_HIMSELF_EVENT = "hero_defends_himself"
HERO_DEACTIVATE_PROTECTED_FIELD_EVENT = "hero_deactivate_protected_field"
HERO_REPELLED_ATTACK_EVENT = "hero_repelled_attack"
HERO_INJECTED_ADRENALINE_EVENT = "hero_injected_adrenaline"
ADRENALINE_QTY_INFO = "adrenaline_qty_info"
ADRENALINE_ENDED = "adrenaline_ended"

ROBOT_CHARACTER_NAME = "Робот"
ROBOT_WAS_INJURED_EVENT = "robot_took_damage"
ROBOT_FINISHED_EVENT = "robot_health_info"
ROBOT_MISSED_EVENT = "robot_missed"
ROBOT_MISSES_TURN_EVENT = "robot_misses_turn"
ROBOT_USE_HOMING_MISSILES_EVENT = "robot_use_homing_missiles"
ROBOT_USE_REGULAR_CARTRIDGES_EVENT = "robot_use_regular_cartridges"
ROBOT_THROW_POISON_GRENADE = "robot_throw_poison_grenade"
ROBOT_JAMMED_EVENT = "robot_jammed"

robot_data = {
    "hp": 1300,  # жизненная энергия, запас здоровья
    "defence": 120,  # защита, броня
    "gun": 300  # оружие
}

hero_data = {
    "hp": 2000,
    "defence": 100,
    "gun": 250,
    "protective_field": 150,  # защитное поле
    "has_shield": False,
    "adrenaline": 1,
    "adrenaline_power": 500
}
