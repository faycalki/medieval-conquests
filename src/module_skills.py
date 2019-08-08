from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.

skills = [
	("trade", "Trade", sf_base_att_cha|sf_effects_party, 10, "Every_level_of_this_skill_reduces_your_trade_penalty_by_5%%._(Party_skill)"),

	("leadership", "Leadership", sf_base_att_cha, 10, "Every_point_increases_maximum_number_of_troops_you_can_command_by_5,_increases_your_party_morale_and_reduces_troop_wages_by_5%%._(Leader_skill)"),

	("prisoner_management", "Prisoner Management", sf_base_att_cha, 10, "Every_level_of_this_skill_increases_maximum_number_of_prisoners_by_%d._(Leader_skill)"),

	("reserved_1", "Reserved Skill 1", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_2", "Reserved Skill 2", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_3", "Reserved Skill 3", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_4", "Reserved Skill 4", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("persuasion", "Persuasion", sf_base_att_int, 10, "This_skill_helps_you_make_other_people_accept_your_point_of_view._It_also_lowers_the_minimum_level_of_relationship_needed_to_get_NPCs_to_do_what_you_want._(Personal_skill)"),

	("engineer", "Engineer", sf_base_att_int|sf_effects_party, 10, "This_skill_allows_you_to_construct_siege_equipment_and_fief_improvements_more_efficiently._(Party_skill)"),

	("first_aid", "First Aid", sf_base_att_int|sf_effects_party, 10, "Heroes_regain_5%%_per_skill_level_of_hit-points_lost_during_mission._(Party_skill)"),

	("surgery", "Surgery", sf_base_att_int|sf_effects_party, 10, "Each_point_to_this_skill_gives_a_4%%_chance_that_a_mortally_struck_party_member_will_be_wounded_rather_than_killed._(Party_skill)"),

	("wound_treatment", "Wound Treatment", sf_base_att_int|sf_effects_party, 10, "Party_healing_speed_is_increased_by_20%%_per_level_of_this_skill._(Party_skill)"),

	("inventory_management", "Inventory Management", sf_base_att_int, 10, "Increases_inventory_capacity_by_+6_per_skill_level._(Leader_skill)"),

	("spotting", "Spotting", sf_base_att_int|sf_effects_party, 10, "Party_seeing_range_is_increased_by_10%%_per_skill_level._(Party_skill)"),

	("pathfinding", "Path-finding", sf_base_att_int|sf_effects_party, 10, "Party_map_speed_is_increased_by_3%%_per_skill_level._(Party_skill)"),

	("tactics", "Tactics", sf_base_att_int|sf_effects_party, 10, "Every_two_levels_of_this_skill_increases_starting_battle_advantage_by_1._(Party_skill)"),

	("tracking", "Tracking", sf_base_att_int|sf_effects_party, 10, "Tracks_become_more_informative._(Party_skill)"),

	("trainer", "Trainer", sf_base_att_int, 10, "Every_day,_each_hero_with_this_skill_adds_some_experience_to_every_other_member_of_the_party_whose_level_is_lower_than_his/hers._Experience_gained_goes_as:_{0,4,10,16,23,30,38,46,55,65,80}._(Personal_skill)"),

	("reserved_5", "Reserved Skill 5", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_6", "Reserved Skill 6", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_7", "Reserved Skill 7", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_8", "Reserved Skill 8", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("looting", "Looting", sf_base_att_agi|sf_effects_party, 10, "This_skill_increases_the_amount_of_loot_obtained_by_10%%_per_skill_level._(Party_skill)"),

	("horse_archery", "Horse Archery", sf_base_att_agi, 10, "Reduces_damage_and_accuracy_penalties_for_archery_and_throwing_from_horseback._(Personal_skill)"),

	("riding", "Riding", sf_base_att_agi, 10, "Enables_you_to_ride_horses_of_higher_difficulty_levels_and_increases_your_riding_speed_and_manuever._(Personal_skill)"),

	("athletics", "Athletics", sf_base_att_agi, 10, "Improves_your_running_speed._(Personal_skill)"),

	("shield", "Shield", sf_base_att_agi, 10, "Reduces_damage_to_shields_(by_8%%_per_skill_level)_and_improves_shield_speed_and_coverage._(Personal_skill)"),

	("weapon_master", "Weapon Master", sf_base_att_agi, 10, "Makes_it_easier_to_learn_weapon_proficiencies_and_increases_the_proficiency_limits._Limits_go_as:_60,_100,_140,_180,_220,_260,_300,_340,_380,_420._(Personal_skill)"),

	("reserved_9", "Reserved Skill 9", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_10", "Reserved Skill 10", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_11", "Reserved Skill 11", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_12", "Reserved Skill 12", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_13", "Reserved Skill 13", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("power_draw", "Power Draw", sf_base_att_str, 10, "Lets_character_use_more_powerful_bows._Each_point_to_this_skill_(up_to_four_plus_power-draw_requirement_of_the_bow)_increases_bow_damage_by_14%%._(Personal_skill)"),

	("power_throw", "Power Throw", sf_base_att_str, 10, "Each_point_to_this_skill_increases_throwing_damage_by_10%%._(Personal_skill)"),

	("power_strike", "Power Strike", sf_base_att_str, 10, "Each_point_to_this_skill_increases_melee_damage_by_8%%._(Personal_skill)"),

	("ironflesh", "Ironflesh", sf_base_att_str, 10, "Each_point_to_this_skill_increases_hit_points_by_+2._(Personal_skill)"),

	("reserved_14", "Reserved Skill 14", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_15", "Reserved Skill 15", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_16", "Reserved Skill 16", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_17", "Reserved Skill 17", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_18", "Reserved Skill 18", sf_inactive, 10, "This_is_a_reserved_skill."),

]