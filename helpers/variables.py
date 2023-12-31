HERO_CHARACTER_NAME = "👽"
HERO_MISS_PERCENTAGE = 25
HERO_WAS_INJURED_EVENT = "hero_took_damage"
HERO_MISSED_EVENT = "hero_missed"
HERO_SKIPS_TURN_EVENT = "hero_skips_turn"
HERO_ATTACKS_EVENT = "hero_attacks"
HERO_DEFENDS_HIMSELF_EVENT = "hero_defends_himself"
HERO_DEACTIVATE_PROTECTED_FIELD_EVENT = "hero_deactivate_protected_field"
HERO_REPELLED_ATTACK_EVENT = "hero_repelled_attack"
HERO_INJECTED_ADRENALINE_EVENT = "hero_injected_adrenaline"
HERO_HEALTH_INFO = "hero_health_info"
ADRENALINE_QTY_INFO = "adrenaline_qty_info"
ADRENALINE_ENDED_INFO = "adrenaline_ended_info"

ROBOT_CHARACTER_NAME = "🤖"
ROBOT_SKIP_TURN_PERCENTAGE = 33
ROBOT_MISS_CARTRIDGES_PERCENTAGE = 50
ROBOT_THROW_GRENADE_PERCENTAGE = 25
ROBOT_WAS_INJURED_EVENT = "robot_took_damage"
ROBOT_HEALTH_INFO = "robot_health_info"
ROBOT_MISSED_EVENT = "robot_missed"
ROBOT_SKIPS_TURN_EVENT = "robot_skips_turn"
ROBOT_USE_HOMING_MISSILES_EVENT = "robot_use_homing_missiles"
ROBOT_USE_REGULAR_CARTRIDGES_EVENT = "robot_use_regular_cartridges"
ROBOT_THROW_POISON_GRENADE = "robot_throw_poison_grenade"
ROBOT_JAMMED_EVENT = "robot_jammed"

robot_data = {
    "hp": 1300,
    "defence": 120,
    "gun": 300
}

hero_data = {
    "hp": 2000,
    "defence": 100,
    "gun": 250,
    "protective_field": 150,
    "has_shield": False,
    "adrenaline": 1,
    "adrenaline_power": 500
}

HERO_ATTACK_ACTION = "attack"
HERO_DEFENSE_ACTION = "defense"
HERO_PASS_ACTION = "pass"
HERO_INJECTING_ADRENALINE_ACTION = "injecting adrenaline"
