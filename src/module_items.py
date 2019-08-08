# -*- coding: utf8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
	["no_item", "INVALID ITEM", [("invalid_item", imodbits_none)], 2|itp_primary|itp_secondary, itc_longsword, 3, thrust_damage(10, blunt)|hit_points(16384)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(90), imodbits_none],

	["tutorial_spear", "Spear", [("spear", imodbits_none)], 4|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itc_spear, 0, thrust_damage(19, pierce)|spd_rtng(80)|abundance(100)|weight(4.5)|weapon_length(158), imodbits_polearm],

	["tutorial_club", "Club", [("club", imodbits_none)], 2|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar, 0, thrust_damage(0, pierce)|hit_points(11264)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(11, blunt)|weapon_length(95), imodbits_none],

	["tutorial_battle_axe", "Battle Axe", [("battle_ax", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi, 0, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(88)|abundance(100)|weight(5.0)|swing_damage(27, cut)|weapon_length(108), imodbits_axe|imodbits_mace],

	["tutorial_arrows", "Arrows", [("arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, thrust_damage(0, pierce)|max_ammo(20)|abundance(160)|weight(3.0)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["tutorial_bolts", "Bolts", [("bolt", imodbits_none), ("flying_bolt", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", imodbit_large_bag|ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0, thrust_damage(0, pierce)|max_ammo(18)|abundance(90)|weight(2.25)|weapon_length(55), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	["tutorial_short_bow", "Self Bow", [("short_bow", imodbits_none), ("short_bow_carry", ixmesh_carry)], 8|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, thrust_damage(12, pierce)|spd_rtng(98)|abundance(100)|weight(1.0)|shoot_speed(49), imodbits_bow],

	["tutorial_crossbow", "Crossbow", [("crossbow", imodbits_none)], 9|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, thrust_damage(32, pierce)|max_ammo(1)|spd_rtng(42)|abundance(100)|weight(3.0)|shoot_speed(68), imodbits_crossbow],

	["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger", imodbits_none)], 10|itp_primary, itcf_throw_knife, 0, thrust_damage(16, cut)|max_ammo(14)|spd_rtng(102)|abundance(100)|weight(3.5)|shoot_speed(25), imodbits_missile],

	["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse", imodbits_none)], itp_type_horse, 0, 0, horse_maneuver(38)|abundance(90)|thrust_damage(8, cut)|horse_speed(40)|body_armor(3), imodbits_horse_basic],

	["tutorial_shield", "Kite Shield", [("shield_kite_a", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118, hit_points(480)|spd_rtng(82)|abundance(100)|weight(2.5)|shield_width(150)|resistance(1), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["tutorial_staff_no_attack", "Staff", [("wooden_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_parry_polearm, 9, thrust_damage(0, blunt)|spd_rtng(120)|abundance(100)|weight(3.5)|swing_damage(0, blunt)|weapon_length(115), imodbits_none],

	["tutorial_staff", "Staff", [("wooden_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 9, thrust_damage(16, blunt)|hit_points(16384)|spd_rtng(120)|abundance(100)|weight(3.5)|swing_damage(16, blunt)|weapon_length(115), imodbits_none],

	["tutorial_sword", "Sword", [("long_sword", imodbits_none), ("scab_longsw_a", ixmesh_carry)], 2|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 0, thrust_damage(15, pierce)|hit_points(18432)|spd_rtng(100)|abundance(100)|weight(1.5)|swing_damage(18, cut)|weapon_length(102), imodbits_sword],

	["tutorial_axe", "Axe", [("iron_ax", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi, 0, thrust_damage(0, pierce)|hit_points(19456)|spd_rtng(91)|abundance(100)|weight(4.0)|swing_damage(19, cut)|weapon_length(108), imodbits_axe|imodbits_mace],

	["tutorial_dagger", "Dagger", [("practice_dagger", imodbits_none)], 2|itp_primary|itp_secondary, itc_longsword, 3, thrust_damage(10, blunt)|hit_points(16384)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(40), imodbits_none],

	["horse_meat", "Horse Meat", [("raw_meat", imodbits_none)], itp_type_goods|itp_food|itp_consumable, 0, 12, max_ammo(40)|abundance(100)|weight(40.0)|food_quality(30), imodbits_none],

	["practice_sword", "Practice Sword", [("practice_sword", imodbits_none)], 2|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary, itc_longsword, 3, thrust_damage(20, blunt)|hit_points(22528)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(22, blunt)|weapon_length(90), imodbits_none],

	["heavy_practice_sword", "Heavy Practice Sword", [("heavy_practicesword", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary, itc_greatsword, 21, thrust_damage(24, blunt)|hit_points(30720)|spd_rtng(94)|abundance(100)|weight(6.25)|swing_damage(30, blunt)|weapon_length(128), imodbits_none],

	["practice_dagger", "Practice Dagger", [("practice_dagger", imodbits_none)], 2|itp_no_parry|itp_wooden_attack|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger, 2, thrust_damage(14, blunt)|hit_points(16384)|spd_rtng(110)|abundance(100)|weight(0.5)|swing_damage(16, blunt)|weapon_length(47), imodbits_none],

	["practice_axe", "Practice Axe", [("hatchet", imodbits_none)], 2|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar, 24, thrust_damage(0, pierce)|hit_points(24576)|spd_rtng(95)|abundance(100)|weight(2.0)|swing_damage(24, blunt)|weapon_length(75), imodbits_axe|imodbits_mace],

	["arena_axe", "Axe", [("arena_axe", imodbits_none)], 2|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar, 137, thrust_damage(0, pierce)|hit_points(24576)|spd_rtng(100)|abundance(100)|weight(1.5)|swing_damage(24, blunt)|weapon_length(69), imodbits_axe|imodbits_mace],

	["arena_sword", "Sword", [("arena_sword_one_handed", imodbits_none), ("sword_medieval_b_scabbard", ixmesh_carry)], 2|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 243, thrust_damage(20, blunt)|hit_points(22528)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(22, blunt)|weapon_length(95), imodbits_sword_high],

	["arena_sword_two_handed", "Two Handed Sword", [("arena_sword_two_handed", imodbits_none)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_greatsword, 670, thrust_damage(24, blunt)|hit_points(30720)|spd_rtng(93)|abundance(100)|weight(2.75)|swing_damage(30, blunt)|weapon_length(110), imodbits_sword_high],

	["arena_lance", "Lance", [("arena_lance", imodbits_none)], 4|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itcf_carry_spear|itc_staff, 90, thrust_damage(25, blunt)|hit_points(20480)|spd_rtng(96)|abundance(100)|weight(2.5)|swing_damage(20, blunt)|weapon_length(150), imodbits_polearm],

	["practice_staff", "Practice Staff", [("wooden_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 9, thrust_damage(18, blunt)|hit_points(18432)|spd_rtng(103)|abundance(100)|weight(2.5)|swing_damage(18, blunt)|weapon_length(118), imodbits_none],

	["practice_lance", "Practice Lance", [("joust_of_peace", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head|itp_couchable, itc_pike|itc_greatlance, 18, thrust_damage(15, blunt)|spd_rtng(58)|abundance(100)|weight(4.25)|swing_damage(0, blunt)|weapon_length(240), imodbits_none],

	["practice_shield", "Practice Shield", [("shield_round_a", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20, hit_points(200)|spd_rtng(100)|abundance(100)|weight(3.5)|shield_width(50)|resistance(1), imodbits_none,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["practice_bow", "Practice Bow", [("hunting_bow", imodbits_none), ("hunting_bow_carry", ixmesh_carry)], 8|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, thrust_damage(21, blunt)|spd_rtng(90)|abundance(100)|weight(1.5)|shoot_speed(40), imodbits_bow],

	["practice_crossbow", "Practice Crossbow", [("crossbow_a", imodbits_none)], 9|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, thrust_damage(32, blunt)|max_ammo(1)|spd_rtng(42)|abundance(100)|weight(3.0)|shoot_speed(68), imodbits_crossbow],

	["practice_javelin", "Practice Javelins", [("javelin", imodbits_none), ("javelins_quiver_new", ixmesh_carry)], 10|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, thrust_damage(27, blunt)|max_ammo(50)|spd_rtng(91)|abundance(100)|weight(5.0)|weapon_length(75)|shoot_speed(28), imodbits_thrown],

	["practice_javelin_melee", "practice javelin melee", [("javelin", imodbits_none)], 4|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itc_staff, 0, thrust_damage(14, blunt)|hit_points(12288)|spd_rtng(91)|abundance(100)|weight(1.0)|swing_damage(12, blunt)|weapon_length(75), imodbits_polearm],

	["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger", imodbits_none)], 10|itp_primary, itcf_throw_knife, 0, thrust_damage(16, blunt)|max_ammo(10)|spd_rtng(102)|abundance(100)|weight(3.5)|shoot_speed(25), imodbits_thrown],

	["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger", imodbits_none)], 10|itp_primary, itcf_throw_knife, 0, thrust_damage(16, blunt)|max_ammo(100)|spd_rtng(102)|abundance(100)|weight(3.5)|shoot_speed(25), imodbits_thrown],

	["practice_horse", "Practice Horse", [("saddle_horse", imodbits_none)], itp_type_horse, 0, 37, horse_maneuver(37)|abundance(100)|thrust_damage(14, cut)|horse_speed(40)|body_armor(10), imodbits_none],

	["practice_arrows", "Practice Arrows", [("arena_arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, max_ammo(80)|abundance(100)|weight(1.5)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["practice_bolts", "Practice Bolts", [("bolt", imodbits_none), ("flying_bolt", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", imodbit_large_bag|ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0, max_ammo(49)|abundance(100)|weight(2.25)|weapon_length(55), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["practice_arrows_10_amount", "Practice Arrows", [("arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, max_ammo(10)|abundance(100)|weight(1.5)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["practice_arrows_100_amount", "Practice Arrows", [("arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, max_ammo(100)|abundance(100)|weight(1.5)|weapon_length(95), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["practice_bolts_9_amount", "Practice Bolts", [("bolt", imodbits_none), ("flying_bolt", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", imodbit_large_bag|ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0, max_ammo(9)|abundance(100)|weight(2.25)|weapon_length(55), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["practice_boots", "Practice Boots", [("woolen_hose_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 11, abundance(100)|weight(1.0)|leg_armor(10), imodbits_cloth],

	["book_tactics", "De Re Militari", [("book_a", imodbits_none)], itp_type_book, 0, 4000, abundance(100)|weight(2.0), imodbits_none],

	["book_persuasion", "Rhetorica ad Herennium", [("book_b", imodbits_none)], itp_type_book, 0, 5000, abundance(100)|weight(2.0), imodbits_none],

	["book_leadership", "The Life of Alixenus the Great", [("book_d", imodbits_none)], itp_type_book, 0, 4200, abundance(100)|weight(2.0), imodbits_none],

	["book_intelligence", "Essays on Logic", [("book_e", imodbits_none)], itp_type_book, 0, 2900, abundance(100)|weight(2.0), imodbits_none],

	["book_trade", "A Treatise on the Value of Things", [("book_f", imodbits_none)], itp_type_book, 0, 3100, abundance(100)|weight(2.0), imodbits_none],

	["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d", imodbits_none)], itp_type_book, 0, 4200, abundance(100)|weight(2.0), imodbits_none],

	["book_engineering", "Method of Mechanical Theorems", [("book_open", imodbits_none)], itp_type_book, 0, 4000, abundance(100)|weight(2.0), imodbits_none],

	["book_wound_treatment_reference", "The Book of Healing", [("book_c", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["book_training_reference", "Manual of Arms", [("book_open", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["book_surgery_reference", "The Great Book of Surgery", [("book_c", imodbits_none)], itp_type_book, 0, 3500, abundance(100)|weight(2.0), imodbits_none],

	["spice", "Spice", [("spice_sack", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["salt", "Salt", [("salt_sack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 255, abundance(120)|weight(50.0), imodbits_none],

	["oil", "Oil", [("oil", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 450, max_ammo(50)|abundance(60)|weight(50.0), imodbits_none],

	["pottery", "Pottery", [("jug", imodbits_none)], itp_type_goods|itp_merchandise, 0, 100, abundance(90)|weight(50.0), imodbits_none],

	["raw_flax", "Flax Bundle", [("raw_flax", imodbits_none)], itp_type_goods|itp_merchandise, 0, 150, abundance(90)|weight(40.0), imodbits_none],

	["linen", "Linen", [("linen", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbits_none],

	["wool", "Wool", [("wool_sack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 130, abundance(90)|weight(40.0), imodbits_none],

	["wool_cloth", "Wool Cloth", [("wool_cloth", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbits_none],

	["raw_silk", "Raw Silk", [("raw_silk_bundle", imodbits_none)], itp_type_goods|itp_merchandise, 0, 600, abundance(90)|weight(30.0), imodbits_none],

	["raw_dyes", "Dyes", [("dyes", imodbits_none)], itp_type_goods|itp_merchandise, 0, 200, abundance(90)|weight(10.0), imodbits_none],

	["velvet", "Velvet", [("velvet", imodbits_none)], itp_type_goods|itp_merchandise, 0, 1025, abundance(30)|weight(40.0), imodbits_none],

	["iron", "Iron", [("iron", imodbits_none)], itp_type_goods|itp_merchandise, 0, 264, abundance(60)|weight(60.0), imodbits_none],

	["tools", "Tools", [("iron_hammer", imodbits_none)], itp_type_goods|itp_merchandise, 0, 410, abundance(90)|weight(50.0), imodbits_none],

	["raw_leather", "Hides", [("leatherwork_inventory", imodbits_none)], itp_type_goods|itp_merchandise, 0, 120, abundance(90)|weight(40.0), imodbits_none],

	["leatherwork", "Leatherwork", [("leatherwork_frame", imodbits_none)], itp_type_goods|itp_merchandise, 0, 220, abundance(90)|weight(40.0), imodbits_none],

	["raw_date_fruit", "Date Fruit", [("date_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, max_ammo(10)|abundance(100)|weight(40.0)|food_quality(10), imodbits_none],

	["furs", "Furs", [("fur_pack", imodbits_none)], itp_type_goods|itp_merchandise, 0, 391, abundance(90)|weight(40.0), imodbits_none],

	["wine", "Wine", [("amphora_slim", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 220, max_ammo(50)|abundance(60)|weight(30.0), imodbits_none],

	["ale", "Ale", [("ale_barrel", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 120, max_ammo(50)|abundance(70)|weight(30.0), imodbits_none],

	["smoked_fish", "Smoked Fish", [("smoked_fish", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 65, max_ammo(150)|abundance(110)|weight(15.0)|food_quality(50), imodbits_none],

	["cheese", "Cheese", [("cheese_b", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(90)|abundance(110)|weight(6.0)|food_quality(40), imodbits_none],

	["honey", "Honey", [("honey_pot", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 220, max_ammo(90)|abundance(110)|weight(5.0)|food_quality(40), imodbits_none],

	["sausages", "Sausages", [("sausages", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(120)|abundance(110)|weight(10.0)|food_quality(40), imodbits_none],

	["cabbages", "Cabbages", [("cabbage", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 30, max_ammo(150)|abundance(110)|weight(15.0)|food_quality(40), imodbits_none],

	["dried_meat", "Dried Meat", [("smoked_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(150)|abundance(100)|weight(15.0)|food_quality(70), imodbits_none],

	["apples", "Fruit", [("apple_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 44, max_ammo(150)|abundance(110)|weight(20.0)|food_quality(40), imodbits_none],

	["raw_grapes", "Grapes", [("grapes_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 75, max_ammo(30)|abundance(90)|weight(40.0)|head_armor(10), imodbits_none],

	["raw_olives", "Olives", [("olive_inventory", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 100, max_ammo(30)|abundance(90)|weight(40.0)|head_armor(10), imodbits_none],

	["grain", "Grain", [("wheat_sack", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 30, max_ammo(150)|abundance(110)|weight(30.0)|head_armor(40), imodbits_none],

	["cattle_meat", "Beef", [("raw_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 80, max_ammo(50)|abundance(100)|weight(20.0)|food_quality(80), imodbits_none],

	["bread", "Bread", [("bread_a", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 50, max_ammo(50)|abundance(110)|weight(30.0)|food_quality(40), imodbits_none],

	["chicken", "Chicken", [("chicken", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, max_ammo(50)|abundance(110)|weight(10.0)|food_quality(40), imodbits_none],

	["pork", "Pork", [("pork", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(50)|abundance(100)|weight(15.0)|food_quality(70), imodbits_none],

	["butter", "Butter", [("butter_pot", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 150, max_ammo(30)|abundance(110)|weight(6.0)|food_quality(40), imodbits_none],

	["siege_supply", "Supplies", [("ale_barrel", imodbits_none)], itp_type_goods, 0, 96, abundance(70)|weight(40.0), imodbits_none],

	["quest_wine", "Wine", [("amphora_slim", imodbits_none)], itp_type_goods, 0, 46, max_ammo(50)|abundance(60)|weight(40.0), imodbits_none],

	["quest_ale", "Ale", [("ale_barrel", imodbits_none)], itp_type_goods, 0, 31, max_ammo(50)|abundance(70)|weight(40.0), imodbits_none],

	["sumpter_horse", "Packhorse", [("sumpter_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 134, hit_points(65)|horse_maneuver(43)|abundance(90)|difficulty(1)|thrust_damage(9, cut)|horse_speed(40)|body_armor(17)|horse_scale(100), imodbits_horse_basic],

	["saddle_horse", "Rouncey", [("saddle_horse", imodbits_none), ("horse_c", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 240, hit_points(65)|horse_maneuver(46)|abundance(90)|difficulty(1)|thrust_damage(10, cut)|horse_speed(42)|body_armor(14)|horse_scale(104), imodbits_horse_basic],

	["steppe_horse", "Steppe Horse", [("steppe_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 192, hit_points(65)|horse_maneuver(51)|abundance(80)|difficulty(2)|thrust_damage(8, cut)|horse_speed(44)|body_armor(15)|horse_scale(90), imodbits_horse_basic, [], [fac_culture_mongol]],

	["arabian_horse_a", "Arabian Horse", [("arabian_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 550, hit_points(65)|horse_maneuver(45)|abundance(80)|difficulty(2)|thrust_damage(12, cut)|horse_speed(48)|body_armor(15)|horse_scale(100), imodbit_champion|imodbits_horse_basic, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["courser", "Palfrey", [("courser", imodbits_none)], itp_type_horse|itp_merchandise, 0, 600, hit_points(65)|horse_maneuver(47)|abundance(70)|difficulty(2)|thrust_damage(22, cut)|horse_speed(48)|body_armor(12)|horse_scale(106), imodbit_champion|imodbits_horse_basic],

	["arabian_horse_b", "Arabian Horse", [("arabian_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 700, hit_points(65)|horse_maneuver(54)|abundance(80)|difficulty(3)|thrust_damage(16, cut)|horse_speed(44)|body_armor(15)|horse_scale(100), imodbit_champion|imodbits_horse_basic, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["hunter", "Courser", [("hunting_horse", imodbits_none), ("hunting_horse", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(65)|horse_maneuver(46)|abundance(60)|difficulty(3)|thrust_damage(28, cut)|horse_speed(45)|body_armor(18)|horse_scale(108), imodbit_champion|imodbits_horse_basic],

	["warhorse", "War Horse", [("warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_white", "Barded Destrier", [("covered_horse_white", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_red", "Barded Destrier", [("covered_horse_red", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_blue", "Barded Destrier", [("covered_horse_blue", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_yellow", "Barded Destrier", [("covered_horse_yellow", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_player", "Custom Barded Destrier", [("covered_horse_player", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_lionel", "Barded Destrier", [("covered_horse_lionel", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_lethwin", "Barded Destrier", [("covered_horse_lethwin", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_01", "Caparisoned Destrier", [("rnd_horse_01", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_02", "Caparisoned Destrier", [("rnd_horse_02", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_03", "Caparisoned Destrier", [("rnd_horse_03", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_04", "Caparisoned Destrier", [("rnd_horse_04", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_05", "Caparisoned Destrier", [("rnd_horse_05", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_06", "Caparisoned Destrier", [("rnd_horse_06", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_07", "Caparisoned Destrier", [("rnd_horse_07", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_08", "Caparisoned Destrier", [("rnd_horse_08", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_09", "Caparisoned Destrier", [("rnd_horse_09", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_10", "Caparisoned Destrier", [("rnd_horse_10", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_11", "Caparisoned Destrier", [("rnd_horse_11", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_12", "Caparisoned Destrier", [("rnd_horse_12", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_13", "Caparisoned Destrier", [("rnd_horse_13", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_14", "Caparisoned Destrier", [("rnd_horse_14", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_15", "Caparisoned Destrier", [("rnd_horse_15", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_16", "Caparisoned Destrier", [("rnd_horse_16", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_17", "Caparisoned Destrier", [("rnd_horse_17", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_18", "Caparisoned Destrier", [("rnd_horse_18", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_19", "Caparisoned Destrier", [("rnd_horse_19", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_20", "Caparisoned Destrier", [("rnd_horse_20", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_21", "Caparisoned Destrier", [("rnd_horse_21", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_22", "Caparisoned Destrier", [("rnd_horse_22", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_horse_23", "Caparisoned Destrier", [("rnd_horse_23", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["warhorse_denmark_a", "Danish Destrier", [("warhorse_denmark_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_4]],

	["warhorse_england_a", "English Destrier", [("warhorse_england_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_devalence", "English Destrier", [("warhorse_devalence", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_demontfort", "English Destrier", [("warhorse_demontfort", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_mortimer", "English Destrier", [("warhorse_mortimer", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_bigod", "English Destrier", [("warhorse_bigod", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_dewarenne", "English Destrier", [("warhorse_dewarenne", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_france_a", "French Destrier", [("warhorse_france_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["warhorse_hre_a", "HRE Destrier", [("warhorse_hre_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_6]],

	["warhorse_bohemia", "Bohemian Destrier", [("warhorse_bohemia", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_6]],

	["warhorse_hungary_a", "Hungarian Destrier", [("warhorse_hungary_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_7]],

	["warhorse_ireland_a", "Irish Destrier", [("warhorse_gaelic", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_13]],

	["warhorse_lithuania_a", "Lithuanian Destrier", [("warhorse_lithuania_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_2]],

	["warhorse_norway_a", "Norwegian Destrier", [("warhorse_norway_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_11]],

	["warhorse_novgorod_a", "Russian Destrier", [("warhorse_novgorod_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_8]],

	["warhorse_scotland_a", "Scottish Destrier", [("warhorse_scotland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_12]],

	["warhorse_sweden_a", "Swedish Destrier", [("warhorse_sweden_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_14]],

	["warhorse_przemysl2", "Polish Destrier", [("warhorse_przemysl2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_czersk", "Polish Destrier", [("warhorse_czersk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_slask_a", "Caparisoned Destrier", [("warhorse_slask_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_siemowit_a", "Caparisoned Destrier", [("warhorse_siemowit_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_poland_a", "Polish Destrier", [("warhorse_poland_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_poland_b", "Polish Destrier", [("warhorse_poland_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_kaliskie_a", "Polish Destrier", [("warhorse_kaliskie_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_gslask", "Polish Destrier", [("warhorse_gslask", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_swietopelk", "Polish Destrier", [("warhorse_swietopelk", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_a", "Polish Destrier", [("warhorse_pol_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_b", "Polish Destrier", [("warhorse_pol_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_c", "Polish Destrier", [("warhorse_pol_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_d", "Polish Destrier", [("warhorse_pol_d", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_e", "Polish Destrier", [("warhorse_pol_e", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_pol_g", "Polish Destrier", [("warhorse_pol_g", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["warhorse_swidnica", "Polish Destrier", [("warhorse_swidnica", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5]],

	["teu_warhorse_c", "Teutonic Destrier", [("teu_war_horse_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1]],

	["teu_warhorse_b", "Teutonic Destrier", [("teu_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1]],

	["teu_warhorse_a", "Teutonic Destrier", [("teu_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1]],

	["mon_lamellar_horse_a", "Lamellar Destrier", [("warhorse_lamellar_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mon_lamellar_horse_b", "Lamellar Destrier", [("warhorse_lamellar_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mon_lamellar_horse_c", "Lamellar Destrier", [("warhorse_lamellar_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kau_montcada_horse", "Montcada Destrier", [("kau_montcada_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_alego_horse", "Alego Destrier", [("kau_alego_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_cervello_horse", "Cervello Destrier", [("kau_cervello_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_cruilles_horse", "Cruilles Destrier", [("kau_cruilles_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_epyres_horse", "Epyres Destrier", [("kau_epyres_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_luna_horse", "Luna Destrier", [("kau_luna_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_reino_horse", "Reino Destrier", [("kau_reino_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_urgell_horse", "Urgell Destrier", [("kau_urgell_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["templar_warhorse_a", "Caparisoned Destrier", [("templar_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_23]],

	["hospitaller_warhorse_a", "Caparisoned Destrier", [("hospitaller_war_horse_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_23]],

	["hospitaller_warhorse_b", "Caparisoned Destrier", [("hospitaller_war_horse_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_23]],

	["warhorse_sarranid", "Lamellar War Horse", [("warhorse_sarranid", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["warhorse_steppe", "Lamellar War Horse", [("warhorse_steppe", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mongol]],

	["byz_warhorse", "Lamellar War Horse", [("byz_warhorse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["jerusalem_horse", "Caparisoned Destrier", [("jerusalem_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_23]],

	["tripoli_horse", "Caparisoned Destrier", [("tripoli_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_23]],

	["portugal_horse", "Caparisoned Destrier", [("portugal_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_16]],

	["castile_horse", "Caparisoned Destrier", [("castile_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_18]],

	["arrows", "Arrows", [("arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 72, thrust_damage(30, cut)|max_ammo(60)|abundance(160)|weight(3.0)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["khergit_arrows", "Mongol Arrows", [("arrow_b", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 410, thrust_damage(33, cut)|max_ammo(60)|abundance(30)|weight(3.5)|weapon_length(95), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])],
[fac_culture_mongol]],

	["barbed_arrows", "Barbed Arrows", [("barbed_arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124, thrust_damage(31, cut)|max_ammo(60)|abundance(70)|weight(3.0)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["bodkin_arrows", "Bodkin Arrows", [("piercing_arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350, thrust_damage(32, cut)|max_ammo(60)|abundance(50)|weight(3.0)|weapon_length(91), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["bolts", "Bolts", [("bolt", imodbits_none), ("flying_bolt", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64, thrust_damage(36, cut)|max_ammo(29)|abundance(90)|weight(2.25)|weapon_length(63), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["steel_bolts", "Steel Bolts", [("bolt", imodbits_none), ("flying_bolt", ixmesh_flying_ammo), ("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210, thrust_damage(40, cut)|max_ammo(29)|abundance(20)|weight(2.5)|weapon_length(63), imodbits_missile,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["cartridges", "Cartridges", [("cartridge_a", imodbits_none)], itp_type_bullets|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 41, thrust_damage(1, pierce)|max_ammo(50)|abundance(90)|weight(2.25)|weapon_length(3), imodbits_missile],

	["pilgrim_disguise", "Pilgrim Disguise", [("peasant_man_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 25, abundance(100)|weight(2.0)|leg_armor(8)|body_armor(19), imodbits_cloth],

	["pilgrim_hood", "Pilgrim Hood", [("hood_new", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 35, abundance(100)|weight(1.25)|head_armor(14), imodbits_cloth],

	["leather_gloves", "Leather Gloves", [("leather_gloves_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 40, abundance(120)|weight(0.25)|body_armor(2), imodbits_cloth],

	["mail_mittens", "Mail Mittens", [("mail_mittens_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 360, abundance(100)|weight(0.5)|body_armor(6), imodbits_armor],

	["scale_gauntlets", "Scale Gauntlets", [("scale_gauntlets_b_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 810, abundance(100)|weight(0.75)|body_armor(9), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["lamellar_gauntlets", "Lamellar Gauntlets", [("scale_gauntlets_a_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 1000, abundance(100)|weight(0.75)|body_armor(10), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["wrapping_boots", "Ankle Boots", [("wrapping_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth],

	["woolen_hose", "Woolen Hose", [("woolen_hose_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["hunter_boots", "Hunter Boots", [("hide_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 432, abundance(100)|weight(1.25)|leg_armor(9), imodbits_cloth],

	["hide_boots", "Hide Boots", [("hide_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth],

	["ankle_boots", "Ankle Boots", [("leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 288, abundance(100)|weight(1.0)|leg_armor(6), imodbits_cloth],

	["nomad_boots", "Nomad Boots", [("rus_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth],

	["leather_boots", "Leather Boots", [("leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 720, abundance(100)|weight(1.25)|leg_armor(10), imodbits_cloth],

	["splinted_leather_greaves", "Mail with Shoes", [("leather_greaves_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1728, abundance(100)|weight(3.0)|leg_armor(24), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["mail_chausses", "Mail Chausses", [("mail_chausses_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1872, abundance(100)|weight(3.0)|leg_armor(26), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["splinted_greaves", "Splinted Greaves", [("kua_splinted_greaves_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2016, abundance(100)|weight(3.5)|leg_armor(28)|difficulty(7), imodbits_armor, [], [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["splinted_greaves_long", "Splinted Greaves", [("kua_splinted_greaves_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2016, abundance(100)|weight(3.5)|leg_armor(28)|difficulty(7), imodbits_armor, [], [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mail_boots", "Mail Boots", [("mail_spurs_cp1257", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2520, abundance(100)|weight(3.0)|leg_armor(35)|difficulty(8), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["mail_boots_long", "Mail Boots", [("mail_spurs_cp1257_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2520, abundance(100)|weight(3.0)|leg_armor(35)|difficulty(8), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["kau_mail_boots_dark", "Hardened Hose", [("kau_mail_boots_a_dark", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 1800, abundance(100)|weight(3.0)|leg_armor(25)|difficulty(4), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["kau_mail_boots_dark_long", "Hardened Hose", [("kau_mail_boots_a_dark_long", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(25)|difficulty(4), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sarranid_boots_a", "Saracen Shoes", [("sarranid_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_a_long", "Saracen Shoes", [("cuman_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_b", "Saracen Leather Boots", [("sarranid_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1008, abundance(100)|weight(1.0)|leg_armor(14), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_b_long", "Saracen Leather Boots", [("cuman_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1008, abundance(100)|weight(1.0)|leg_armor(14), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_c", "Saracen camel boots", [("sarranid_camel_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1728, abundance(100)|weight(1.0)|leg_armor(14), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_d", "Saracen Mail Boots", [("sarranid_mail_chausses", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 2520, abundance(100)|weight(1.0)|leg_armor(35), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_boots_d_long", "Saracen Mail Boots", [("leather_greaves_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 2520, abundance(100)|weight(1.0)|leg_armor(35), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["raf_mail_chausses", "Mail Chausses With Padding", [("raf_chausses", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1872, abundance(100)|weight(3.0)|leg_armor(26), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["kau_mail_boots", "Hardened Hose", [("kau_mail_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1800, abundance(100)|weight(3.0)|leg_armor(8)|difficulty(4), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["mamluke_boots", "Mameluke Boots", [("mamluke_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["cuman_boots", "Cuman Boots", [("cuman_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_kingdom_7]],

	["byz_lord_boots", "Byzantine Boots", [("byz_lord_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2520, abundance(100)|weight(3.0)|leg_armor(12)|difficulty(8), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_lord_boots_long", "Byzantine Boots", [("rus_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2520, abundance(100)|weight(3.0)|leg_armor(12)|difficulty(8), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["lapcie", "Eastern Wrapping Shoes", [("lapcie", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic]],

	["byz_boots_c", "Byzantine Leather Boots", [("byz_leather_boots_c", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_cavalry_boots", "Byzantine Leather Boots", [("byz_cavalry_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1296, abundance(100)|weight(1.25)|leg_armor(18), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_boots_a", "Byzantine Leather Boots", [("byz_leather_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_boots_b", "Byzantine Leather Boots", [("byz_leather_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_greaves", "Byzantine Graves", [("byzantine_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1728, abundance(100)|weight(3.0)|leg_armor(24), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["leather_fur_boots", "Boots With Fur", [("leather_fur_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(4), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["red_hose", "Hose", [("red_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["green_hose", "Hose", [("green_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["grey_hose", "Hose", [("grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["dark_grey_hose", "Hose", [("dark_grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["yellow_hose", "Hose", [("yellow_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["green_hose_b", "Hose", [("green_hose_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["tied_up_shoes", "Hose", [("grey_hose", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["blue_hose_mod", "Hose", [("blue_hose_mod", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["berber_shoes", "Berber Shoes", [("berber_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0), imodbits_cloth, [], [fac_culture_andalus]],

	["legs_with_shoes", "Shoes", [("legs_with_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["bare_legs", "Legs", [("bare_legs", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["shoes", "Shoes", [("shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["priest_2_boots", "Hose", [("priest_2_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["blue_hose", "Blue Hose", [("blue_hose_mod", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rus_cav_boots", "Nomad Boots", [("rus_cav_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_kingdom_7]],

	["rus_boots_a", "Rus' Boots", [("rus_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_rus]],

	["rus_boots_b", "Rus' Boots", [("rus_boots_b", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_rus]],

	["red_dress", "Red Dress", [("red_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth],

	["brown_dress", "Brown Dress", [("brown_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth],

	["green_dress", "Green Dress", [("green_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth],

	["khergit_lady_dress", "Mongol Lady Dress", [("khergit_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_lady_dress_b", "Mongol Leather Lady Dress", [("khergit_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_mongol]],

	["sarranid_lady_dress", "Saracen Lady Dress", [("sarranid_lady_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_lady_dress_b", "Saracen Lady Dress", [("sarranid_lady_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_common_dress", "Saracen Dress", [("sarranid_common_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_common_dress_b", "Saracen Dress", [("sarranid_common_dress_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["nomad_armor", "Nomad Armor", [("nomad_armor_new", imodbits_none)], itp_type_body_armor|itp_merchandise, 0, 33, abundance(100)|weight(2.0)|body_armor(10), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_armor", "Mongol Armor", [("khergit_armor_new", imodbits_none)], itp_type_body_armor|itp_merchandise, 0, 65, abundance(100)|weight(2.0)|body_armor(14), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_jacket", "Leather Jacket", [("leather_jacket_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 75, abundance(100)|weight(3.0)|body_armor(15), imodbits_cloth],

	["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 12, abundance(100)|weight(5.0)|body_armor(6), imodbits_cloth],

	["fur_coat", "Fur Coat", [("fur_coat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 65, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(8), imodbits_armor],

	["merchant_outfit", "Merchant Outfit", [("nobleman_outfit_b_new", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(100)|weight(4.0)|leg_armor(10)|body_armor(14), imodbits_cloth],

	["blue_dress", "Blue Dress", [("blue_dress_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6, abundance(100)|weight(1.0)|leg_armor(2)|body_armor(6), imodbits_cloth],

	["peasant_dress", "Peasant Dress", [("peasant_dress_b_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6, abundance(100)|weight(1.0)|leg_armor(2)|body_armor(6), imodbits_cloth],

	["linen_tunic", "Linen Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 16, abundance(100)|weight(1.0)|leg_armor(1)|body_armor(6), imodbits_cloth],

	["short_tunic", "Tunic With Felt Vest", [("rich_tunic_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 21, abundance(100)|weight(1.0)|leg_armor(1)|body_armor(7), imodbits_cloth],

	["red_shirt", "Red Shirt", [("rich_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 21, abundance(100)|weight(1.0)|leg_armor(1)|body_armor(7), imodbits_cloth],

	["robe", "Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 65, abundance(100)|weight(1.5)|leg_armor(6)|body_armor(8), imodbits_cloth],

	["coarse_tunic", "Tunic with Cape", [("coarse_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(2.0)|leg_armor(6)|body_armor(11), imodbits_cloth],

	["leather_vest", "Linen Vest", [("leather_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 27, abundance(100)|weight(4.0)|body_armor(9), imodbits_cloth],

	["steppe_armor", "Steppe Armor", [("lamellar_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 225, abundance(100)|weight(5.0)|leg_armor(4)|body_armor(22), imodbits_cloth, [], [fac_culture_mongol]],

	["gambeson_a", "Gambeson", [("gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gambeson_b", "Gambeson", [("gambeson_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gambeson_c", "Gambeson", [("gambeson_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gambeson_d", "Gambeson", [("gambeson_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["padded_cloth", "Leather Aketon", [("padded_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 147, abundance(100)|weight(6.0)|leg_armor(6)|body_armor(15), imodbits_cloth],

	["nomad_vest", "Nomad Vest", [("nomad_vest_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 65, abundance(50)|weight(7.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_culture_mongol]],

	["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 161, abundance(100)|weight(7.0)|leg_armor(9)|body_armor(13), imodbits_cloth],

	["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth],

	["haubergeon", "Haubergeon", [("kau_mail_shirt_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_rus]],

	["lamellar_vest_khergit", "Mongol Lamellar Vest", [("lamellar_vest_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_mongol]],

	["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["coat_of_plates", "Coat of Plates", [("coat_of_plates_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red_mod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["pelt_coat", "Pelt Coat", [("thick_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 33, abundance(100)|weight(2.0)|leg_armor(1)|body_armor(9), imodbits_cloth],

	["bishop_cop", "Coat of Plates", [("bishop_CoP", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["sarranid_cloth_robe", "Worn Robe", [("sar_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 108, abundance(100)|weight(1.0)|leg_armor(9)|body_armor(9), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 108, abundance(100)|weight(1.0)|leg_armor(9)|body_armor(9), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(100)|weight(3.0)|leg_armor(9)|body_armor(15), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["archers_vest", "Archer's Padded Vest", [("archers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_leather_armor", "Saracen Padded Kaftan", [("kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arabian_armor_b", "Saracen Guard Armor", [("arabian_armor_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_mail_shirt", "Saracen Mail Shirt", [("sarranian_mail_shirt", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["mamluke_mail", "Mamluke Mail", [("arabian_armor_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["veteran_surcoat_a", "Surcoat over Mail", [("surcoat_cop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["veteran_surcoat_b", "Surcoat over Mail", [("surcoat_cop_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["veteran_surcoat_c", "Surcoat over Mail", [("surcoat_cop_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["veteran_surcoat_d", "Surcoat over Mail", [("surcoat_cop_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["veteran_surcoat_e", "Surcoat over Mail", [("surcoat_cop_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["arena_outfit_a", "Surcoat over Mail", [("arena_outfit_blue", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(3)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["arena_outfit_b", "Surcoat over Mail", [("arena_outfit_green", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(3)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["arena_outfit_c", "Surcoat over Mail", [("arena_outfit_red", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(3)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["arena_outfit_d", "Surcoat over Mail", [("arena_outfit_yellow", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(3)|body_armor(51), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_aragon_knight", "Aragonian Mail", [("kau_aragon_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_aragon_a", "Aragonian Mail", [("kau_aragon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_aragon_b", "Aragonian Mail", [("kau_aragon_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_aragon_c", "Aragonian Mail", [("kau_aragon_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_montcada_surcoat", "Montcada Surcoat", [("kau_montcada_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_alego_surcoat", "Alego Surcoat", [("kau_alego_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_cervello_surcoat", "Cervello Surcoat", [("kau_cervello_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_cruilles_surcoat", "Cruilles Surcoat", [("kau_cruilles_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_entenca_surcoat", "Entensa Surcoat", [("kau_entenca_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_epyres_surcoat", "Epyres Surcoat", [("kau_epyres_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_luna_surcoat", "Luna Surcoat", [("kau_luna_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_pons_surcoat", "Pons Surcoat", [("kau_pons_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_castile_knight", "Crown of Castile Mail", [("kau_castile_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_18]],

	["kau_castile_a", "Crown of Castile Mail", [("kau_castile_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_18]],

	["kau_castile_b", "Crown of Castile Mail", [("kau_castile_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_18]],

	["kau_castile_c", "Crown of Castile Mail", [("kau_castile_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_18]],

	["kau_santiago", "Santiago Mail", [("kau_santiago", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_16]],

	["kau_portugal_a", "Portugese Mail", [("kau_portugal_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_16]],

	["kau_portugal_b", "Portugese Mail", [("kau_portugal_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_16]],

	["kau_portugal_c", "Portugese Mail", [("kau_portugal_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_16]],

	["kau_portugal_d", "Portugese Mail", [("kau_portugal_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_16]],

	["kau_papal", "Papal Surcoat over Mail", [("kau_papal", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_papacy]],

	["kau_sicily_a", "Sicilian Mail", [("kau_sicily_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_24]],

	["kau_sicily_b", "Sicilian Mail", [("kau_sicily_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_24]],

	["kau_antioch", "Antioch Mail", [("kau_antioch", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor|imodbits_armor, [], [fac_kingdom_23]],

	["kau_cyprus", "Cyprus Mail", [("kau_cyprus", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["kau_antioch", "Antioch Mail", [("kau_antioch", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor|imodbits_armor, [], [fac_kingdom_23]],

	["kau_jerusalem", "Jerusalem Mail", [("kau_jerusalem", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["kau_latin_a", "Latin Empire Mail", [("kau_latin_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_26]],

	["kau_latin_b", "Latin Empire Mail", [("kau_latin_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_26]],

	["kau_athens", "Latin Empire Mail", [("kau_athens", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_26]],

	["kau_courtenay", "Latin Empire Mail", [("kau_courtenay", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_26]],

	["rnd_surcoat_01", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_01"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_02", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_02"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		[fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_03", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_03", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_03"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		[fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_04", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_04", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_04"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_05", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_05", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_05"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_06", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_06", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_06"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_07", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_07", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_07"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_08", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_08", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_08"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_09", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_09", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_09"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_10", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_10", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_10"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_11", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_11", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_11"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_12", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_12", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_12"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_13", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_13", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_13"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_14", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_14", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_14"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_15", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_15", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_15"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_16", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_16", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_16"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_17", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_17", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_17"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_18", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_18", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_18"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_19", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_19", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_19"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_20", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_20", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_20"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_21", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_21", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_21"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_22", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_22", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
		[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_22"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])],
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_surcoat_23", "Knightly Plated Surcoat with Mail", [("rnd_surcoat_23", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, 
	[(ti_on_init_item,
		[
			(assign, ":var_1", "itm_rnd_surcoat_23"),
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_set_matching_items", ":var_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["surcoat_denmark_a", "Plated Surcoat over Mail", [("surcoat_denmark_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_4]],

	["surcoat_england_a", "Plated Surcoat over Mail", [("surcoat_england_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_devalence", "Plated Surcoat over Mail", [("surcoat_devalence", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_demontfort", "Plated Surcoat over Mail", [("surcoat_demontfort", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_mortimer", "Plated Surcoat over Mail", [("surcoat_mortimer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_bigod", "Plated Surcoat over Mail", [("surcoat_bigod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_dewarenne", "Plated Surcoat over Mail", [("surcoat_dewarenne", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_france_a", "Plated Surcoat over Mail", [("surcoat_france_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_10]],

	["surcoat_hre_a", "Plated Surcoat over Mail", [("surcoat_hre_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_6]],

	["richard_of_cornwall_surcoat_over_mail", "Plated Surcoat over Mail", [("surcoat_richard_of_cornwall_wb", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor],

	["surcoat_bohemia", "Plated Surcoat over Mail", [("surcoat_bohemia_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_6]],

	["surcoat_hungary_a", "Plated Surcoat over Mail", [("surcoat_hungary_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_7]],

	["surcoat_ireland_a", "Plated Surcoat over Mail", [("surcoat_gaelic_kingdoms", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_13]],

	["surcoat_lithuania_a", "Scale Armour", [("surcoat_lithuania_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_2]],

	["surcoat_lithuania_b", "Leather Scale Armour", [("surcoat_lithuania_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_2]],

	["surcoat_norway_a", "Plated Surcoat over Mail", [("surcoat_norway", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_11]],

	["surcoat_novgorod", "Novgorod Lamellar Armour", [("surcoat_novgorod", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_rus]],

	["surcoat_scotland_a", "Plated Surcoat over Mail", [("surcoat_scotland", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_12]],

	["surcoat_sweden_a", "Plated Surcoat over Mail", [("surcoat_sweden_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_14]],

	["surcoat_kaliskie", "Plated Surcoat over Mail", [("surcoat_kaliskie_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_poland_a", "Plated Surcoat over Mail", [("surcoat_poland_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["siemowit_surcoat_over_mail", "Plated Surcoat over Mail", [("surcoat_siemowit_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_gslask", "Plated Surcoat over Mail", [("surcoat_gslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_dslask", "Plated Surcoat over Mail", [("surcoat_dslask_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_mazowsze", "Plated Surcoat over Mail", [("surcoat_mazowsze_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_swidnica", "Plated Surcoat over Mail", [("surcoat_swidnica_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_swietopelk", "Plated Surcoat over Mail", [("surcoat_swietopelk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_henry3", "Plated Surcoat over Mail", [("surcoat_henry3_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_a", "Plated Surcoat over Mail", [("surcoat_pol_wb_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_b", "Scale Armour", [("surcoat_pol_wb_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_c", "Plated Surcoat over Mail", [("surcoat_pol_wb_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_d", "Plated Surcoat over Mail", [("surcoat_pol_wb_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_e", "Plated Surcoat over Mail", [("surcoat_pol_wb_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_f", "Plated Surcoat over Mail", [("surcoat_pol_wb_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_pol_g", "Plated Surcoat over Mail", [("surcoat_pol_wb_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_czersk", "Plated Surcoat over Mail", [("surcoat_czersk_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["surcoat_przemysl2", "Plated Surcoat over Mail", [("surcoat_przemysl2_wb", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_5]],

	["teu_hochmeister_surcoat", "Plated Mail with Surcoat", [("teu_hochmeister_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 17173, abundance(100)|weight(25.0)|leg_armor(33)|difficulty(9)|body_armor(74), imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_thick|imodbit_reinforced],

	["teu_brother_surcoat_a", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_b", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_c", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_d", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_brother_surcoat_e", "Teutonic Mail with Surcoat", [("teu_brother_surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_sariant_mail", "Mail with Surcoat", [("teu_sariant_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_postulant_a", "Postulant Tunic", [("teu_postulant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_hbrother_mail", "Gambeson", [("teu_hbrother_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_sergeant", "Gambeson", [("teutonic_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["liv_sergeant", "Gambeson", [("livonian_sergeant", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_monk_surcoat_a", "Livonian gambeson", [("teu_monk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["liv_tunic_a", "Livonian Tunic", [("liv_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_gambeson", "Gambeson", [("teu_gambeson", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_coat_of_plates", "Coat of Plates", [("teu_coat_of_plates_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["scale_shirt_a", "Scale Shirt", [("raf_scale_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic]],

	["kau_padded_mail_a", "Padded Aketon", [("kau_padded_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_a", "Mail", [("kau_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_b", "Maille", [("kau_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_haubergeon_a", "Rich Aketon", [("kau_haubergeon_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_a", "Aketon", [("kau_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_b", "Mail Shirt", [("kau_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_c", "Rich Aketon", [("kau_mail_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_mail_shirt_d", "Padded Shirt", [("kau_mail_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_rus_a", "Rus Heraldic Shirt With Mail", [("kau_rus_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_b", "Eastern Scale Armor", [("kau_rus_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_d", "Eastern Padded Armor", [("kau_rus_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_scale_a", "Eastern Nobleman Scale Armor", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_noble_b", "Eastern Nobleman Lamellar Armor", [("kau_rus_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_lamellar_vest", "Eastern Lamellar Vest", [("kau_rus_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_noble_a", "Eastern Mail", [("kau_rus_nobleman_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_c", "Eastern Leather Lamellar Armor with Maille", [("kau_rus_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_mail_shirt_a", "Leather Scale Armour", [("kau_rusmilitia", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus]],

	["kau_rus_mail_shirt_b", "Rus Middle Class Aketon", [("kau_rus_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_rus]],

	["rus_mail_shirt_c", "Rus Mail Shirt", [("rus_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic]],

	["kau_rus_e", "Eastern Shirt", [("kau_rus_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_rus]],

	["kau_lit_mail", "Baltic lamellar", [("balt_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_mazovian, fac_culture_baltic, fac_culture_rus]],

	["kau_rus_tunic_a", "Rus' Tunic", [("kau_rus_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 27, abundance(100)|weight(4.0)|body_armor(9), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_tunic_b", "Rus' Tunic", [("kau_rus_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 27, abundance(100)|weight(4.0)|body_armor(9), imodbits_cloth, [], [fac_culture_rus]],

	["kau_rus_tunic_c", "Rus' Tunic", [("kau_rus_tunic_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 27, abundance(100)|weight(4.0)|body_armor(9), imodbits_cloth, [], [fac_culture_rus]],

	["kau_arab_aketon_blue", "Scale Vest", [("kau_arab_aketon_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_aketon", "Padded Cloth", [("kau_arab_aketon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_aketon_red", "Padded Cloth", [("kau_arab_aketon_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_aketon_green", "Padded Cloth", [("kau_arab_aketon_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_a", "Tunic", [("kau_ayubbid", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_b", "Tunic", [("kau_ayubbid_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_lamellar_vest_c", "Tunic", [("kau_ayubbid_copy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_a", "Lamellar Vest", [("arab_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_b", "Lamellar Vest", [("arab_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_c", "Lamellar Vest", [("arab_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_d", "Lamellar Vest", [("arab_mail_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_mail_shirt_a", "Kaftan", [("kau_mail_sara", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_mail_shirt_b", "Mail Shirt", [("kau_mail_saracen", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_mail_shirt_c", "Mail Shirt", [("kau_mail_saracen_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_mail_shirt_d", "Hardened Kaftan", [("kau_mail_saracen_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_tunic_a", "Bedouin Tunic", [("kau_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kau_arab_tunic_b", "Bedouin Tunic", [("kau_muslim_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_banded_a", "Saracen Banded Armour", [("kau_banded_armor_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_banded_b", "Saracen Banded Armour", [("kau_banded_armor_muslim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_banded_c", "Saracen Banded Armour", [("kau_banded_armor_muslima", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["templar_sarjeant_surcoat", "Surcoat over Mail", [("templar_serjeant_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["templar_sarjeant_mail", "Mail Hauberk", [("templar_serjeant_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["templar_mail_a", "Templar gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_23]],

	["templar_tunic_a", "Postulant Tunic", [("templar_postulant_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_23]],

	["templar_knight_a", "Templar Mail with Surcoat", [("templar_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["templar_knight_b", "Templar Mail with Surcoat", [("templar_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["templar_knight_c", "Templar Mail with Surcoat", [("templar_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["templar_gambeson_a", "Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_23]],

	["hospitaller_knight_a", "Mail with Surcoat", [("hospitaller_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor|imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_knight_b", "Mail with Surcoat", [("hospitaller_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_knight_c", "Mail with Surcoat", [("hospitaller_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_knight_d", "Mail with Surcoat", [("hospitaller_knight_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_knight_e", "Mail with Surcoat", [("hospitaller_knight_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_knight_f", "Mail with Surcoat", [("hospitaller_knight_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_sarjeant_surcoat", "Surcoat over Mail", [("templar_serjeant_surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_sarjeant_mail", "Mail Hauberk", [("templar_serjeant_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["hospitaller_tunic_a", "Postulant Tunic", [("templar_postulant_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_23]],

	["hospitaller_gambeson_a", "Gambeson", [("templar_gambeson_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_23]],

	["hospitaller_knight_a", "Mail with Surcoat", [("hospitaller_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor|imodbits_armor, [], [fac_kingdom_23]],

	["hirdman_a", "Coat of Plates", [("kau_hirdman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["cuman_shirt_a", "Cuman Tunic", [("cuman_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_kingdom_7]],

	["cuman_shirt_b", "Cuman Tunic", [("cuman_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_7]],

	["cuman_shirt_c", "Cuman Tunic", [("cuman_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_7]],

	["cuman_shirt_d", "Cuman Tunic", [("cuman_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_kingdom_7]],

	["kipchak_shirt_a", "Kipchak Tunic", [("kipchak_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_kingdom_7]],

	["kipchak_shirt_b", "Kipchak Tunic", [("kipchak_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_kingdom_7]],

	["kipchak_mail_a", "Kipchak Mail Shirt", [("kipchak_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_7]],

	["mongol_warrior_a", "Mongol Tunic", [("mongol_light_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_b", "Mongol Kaftan", [("mongol_light_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_c", "Mongol Leather Vest", [("mongol_leather_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_d", "Chinese Kaftan", [("mongol_warrior_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_tunic_b", "Mongol Tunic", [("mongol_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_warrior_ilkhanate", "Mongol Mail", [("ilkhanate_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_mongol]],

	["mamluk_shirt_a", "Mamluk shirt", [("mamluk_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_b", "Mail Shirt", [("mamluk_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_c", "Mail Shirt", [("mamluk_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_d", "Lamellar", [("mamluk_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_e", "Seljuk Mail Shirt", [("mamluk_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_shirt_f", "Arab scale Armour", [("mamluk_shirt_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["peasant_tunic_a", "Linen Tunic", [("peasant_outfit_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["peasant_b", "Linen Tunic", [("peasant_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["peasant_c", "Linen Tunic", [("peasant_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["peasant_d", "Tunic with Cape", [("peasant_man_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["ragged_cloth_b", "Ragged Cloth", [("ragged_cloth_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["peasant_f", "Ragged Cloth", [("ragged_cloth_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["peasant_g", "Linen Tunic", [("peasant_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["byz_lord", "Byzantine Armour", [("byz_lord", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_emperor", "Byzantine Armour", [("byz_emperor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["bishop_a", "Bishop Mail", [("bishop_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["varangian_a", "Varangian Mail Hauberk", [("varangian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_22]],

	["varangian_b", "Varangian Lamellar", [("varangian_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_22]],

	["varangian_c", "Varangian Lamellar", [("varangian_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_22]],

	["kau_rus_noble_d", "Eastern Nobleman Lamellar Armor", [("kau_rus_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_rus]],

	["balt_lamellar_vest_a", "Baltic Shirt", [("balt_lamellar_vest_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_vest_b", "Baltic Shirt", [("balt_lamellar_vest_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_vest_c", "Baltic Lamellar Vest", [("balt_lamellar_vest_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["byz_mail_a", "Byzantine Mail", [("byzantine_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_lamellar_a", "Byzantine Lamellar Leather Armour", [("byz_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_lamellar_b", "Byzantine Lamellar Leather Armour", [("byz_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_leather_a", "Byzantine Leather Armour", [("byz_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_leather_b", "Byzantine Leather Armour", [("byz_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_padded_leather", "Byzantine Padded Leather Armour", [("byz_padded_cloth", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_scale_armor", "Byzantine Scale Armor", [("byz_cavalry", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_22]],

	["byz_cavalry_a", "Byzantine Cavalry Armour", [("byz_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_cavalry_b", "Byzantine Cavalry Armour", [("byz_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_mail_b", "Byzantine Mail", [("byz_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_a", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_b", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_hcavalry_c", "Byzantine Heavy Cavalry Armour", [("byz_hcavalry_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_psiloi_a", "Linen Tunic", [("byz_psiloi_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["byz_psiloi_b", "Linen Tunic", [("byz_psiloi_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["byz_kataphrakt", "Cataphract Armour", [("byz_kataphrakt", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kipchak_lamellar_a", "Kipchak Mail", [("kipchak_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kipchak_lamellar_b", "Kipchak Lamellar Armor", [("kipchak_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["balt_shirt_a", "Shirt With Fur Vest", [("balt_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_b", "Shirt", [("balt_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_e", "Shirt", [("balt_shirt_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_shirt_d", "Shirt", [("balt_shirt_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_fur_coat_a", "Fur Coat", [("balt_fur_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_fur_coat_b", "Fur Coat", [("balt_fur_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["mon_lamellar_a", "Mongol Lamellar Armor", [("mon_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_mongol]],

	["mon_lamellar_b", "Mongol Lamellar Armor", [("mon_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_mongol]],

	["byz_footman_a", "Byzantine Mail", [("byz_footman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_footman_b", "Byzantine Padded Cloth", [("byz_footman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_footman_c", "Byzantine Mail", [("byz_footman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_1", "Byzantine Scoutati Armour", [("byz_swordsman_r", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_2", "Byzantine Scoutati Armour", [("byz_swordsman_w", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_3", "Byzantine Scoutati Armour", [("byz_swordsman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_swordsman_4", "Byzantine Scoutati Armour", [("byz_swordsman_p", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_guard_a", "Byzantine Guard Armour", [("byz_guard_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_guard_b", "Byzantine Guard Armour", [("byz_guard_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kau_arab_nobleman", "Saracen Noble Armour", [("kau_arab_nobleman", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["almogavar_a", "Pelt Coat", [("almogavar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["almogavar_b", "Pelt Coat", [("almogavar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["almogavar_c", "Pelt Coat", [("almogavar_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_iberian]],

	["burlap_tunic", "Burlap Tunic", [("shirt_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5, abundance(100)|weight(1.0)|leg_armor(1)|body_armor(3), imodbits_armor],

	["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["sarranid_head_cloth", "Lady Head Cloth", [("tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["head_wrappings", "Head Wrapping", [("head_wrapping", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["turret_hat_green", "Barbette", [("barbette_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["wimple_a", "Wimple", [("wimple_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["wimple_with_veil", "Wimple with Veil", [("wimple_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["straw_hat", "Straw Hat", [("straw_hat_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["headcloth", "Headcloth", [("headcloth_a_new", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["arming_cap", "Arming Cap", [("1257_arming_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["fur_hat", "Fur Hat", [("fur_hat_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["nomad_cap", "Nomad Cap", [("nomad_cap_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["steppe_cap", "Steppe Cap", [("steppe_cap_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["padded_coif", "Padded Coif", [("padded_coif_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["woolen_cap", "Woolen Cap", [("woolen_cap_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["felt_hat", "Felt Hat", [("felt_hat_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["felt_hat_b", "Felt Hat", [("felt_hat_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["leather_cap", "Leather Cap", [("leather_cap_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth],

	["female_hood", "Lady's Hood", [("ladys_hood_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["leather_steppe_cap_c", "Steppe Cap", [("nomad_cap_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["mail_coif", "Mail Coif with skullcap", [("coif_1257", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["footman_helmet", "Footman's Helmet", [("skull_cap_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate],

	["khergit_lady_hat", "Mongol Lady Hat", [("khergit_lady_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_lady_hat_b", "Mongol Lady Leather Hat", [("khergit_lady_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mongol]],

	["sarranid_felt_hat", "Saracen Felt Hat", [("sar_helmet3", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban", "Turban", [("tuareg_open", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["desert_turban", "Desert Turban", [("tuareg", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban_a", "Turban", [("arab_turban_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban_b", "Turban", [("arab_turban_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["turban_c", "Turban", [("arab_turban_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_coif", "Saracen Mail Coif", [("arabic_coif", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["seljuk_helmet", "Seljuk Helmet", [("seljuk_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_warrior_cap", "Saracen Warrior Cap", [("tuareg_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_helmet1", "Saracen Keffiyeh Helmet", [("sar_helmet1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_mail_coif", "Saracen Mail Coif", [("tuareg_helmet2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_veiled_helmet", "Saracen Veiled Helmet", [("sar_helmet4", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["vaegir_mask", "Rus War Mask", [("vaeg_helmet9", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["osp_great_helm_a", "Great Helm", [("osp_greathelm_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["osp_great_helm_b", "Great Helm", [("osp_greathelm_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["osp_byzantion_a", "Brimmed Helmet", [("osp_byzantion_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["vik_norman_helmet_a", "Norman Helmet", [("vik_coifedpointyhelm", imodbits_none), ("inv_vik_coifedpointyhelm", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["vik_norman_helmet_b", "Norman Helmet", [("vik_normanhelmet", imodbits_none), ("inv_vik_normanhelmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["vik_norman_helmet_c", "Norman Helmet", [("vik_pointedhelmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["vik_norman_helmet_e", "Plain Helm", [("viki_plainhelm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["vik_spangen_a", "Spangen Helm", [("vik_norskspangen1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["vik_spangen_b", "Spangen Helm", [("vik_norskspangendecorated", imodbits_none), ("inv_vik_norskspangendecorated", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["balt_spiked_helmet", "Balt Spiked Cap", [("pointy_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_footman_helmet", "Balt Footman Helmet", [("lit_segmented_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_helmet_a", "Balt Helmet", [("lit_segmented_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_helmet_b", "Balt Helmet", [("pointy_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_helmet_c", "Balt Helmet", [("rusiu_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["teu_kettle_hat_a", "Kettle Helm", [("teu_kettle_hat_cloth_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_kettle_hat_b", "Kettle Helm", [("teu_kettle_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_kingdom_1, fac_kingdom_23]],

	["slonim", "Slonim", [("slonim", imodbits_none), ("inv_slonim", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["osp_faceplate", "Chapel de fer", [("osp_faceplate", imodbits_none), ("inv_osp_faceplate", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_01", "Winged Great Helmet", [("rnd_helm_01", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_02", "Winged Great Helmet", [("rnd_helm_02", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_03", "Great Helmet", [("rnd_helm_03", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_04", "Great Helm", [("civan_helm_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_05", "Great Helm", [("civan_helm_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["rnd_helm_06", "Great Helm", [("civan_helm_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kau_alego_helmet", "Aragonese Helmet", [("kau_alego_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_epyres_helmet", "Aragonese Helmet", [("kau_epyres_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_pons_helmet", "Aragonese Helmet", [("kau_pons_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["kau_urgell_helmet", "Aragonese Helmet", [("kau_urgell_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["byz_yoman_a", "Byzantine Helmet", [("facecovermail_plume", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_b", "Byzantine Helmet", [("facecovermail_kettlehat", imodbits_none), ("inv_facecovermail_kettlehat", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_c", "Byzantine Skullcap Helmet", [("facecovermail_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_yoman_d", "Byzantine Helmet", [("facecovermail", imodbits_none), ("inv_facecovermail", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["templar_kettlehat_a", "Kettle Helm", [("templar_kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_kingdom_23]],

	["hospitaller_kettlehat_a", "Kettle Helm", [("templar_kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_kingdom_23]],

	["elm1", "Skullcap with Ventail", [("elm_type1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["elm2", "Skullcap with Arming Cap", [("elm_type2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["elm3", "Mail Coif with Noseguard", [("elm_type3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["elm5", "Aragonese Helmet", [("elm_type5", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth, [], [fac_culture_iberian]],

	["elm6", "Flutted Spangen Helmet", [("elm_type6", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["elm7", "Reinforced Mail Coif", [("elm_type7", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["elm8", "Spangen Helmet", [("elm_type8", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["elm9", "Yesenovo Helm", [("elm_type9", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["elm10", "Byzantine Brimmed Helmet", [("byz_kettle", imodbits_none), ("inv_byz_kettle", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_helmet_a", "Byzantine Footman's Helmet", [("byz_helmet_a", imodbits_none), ("inv_byz_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth],

	["skullcap", "Skullcap", [("skull_cap_new_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_plate],

	["raf_spangen", "Spangen Helm", [("spangen", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["arab_helmet_a", "Andalusian Tiara", [("arab_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_helmet_b", "Saracen Helm", [("arab_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_helmet_c", "Saracen Helm", [("arab_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["berber_helmet_a", "Berber Helm", [("berber_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus]],

	["maciejowski_helm", "Decorated Great Helm", [("maciejowskihelm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["talak_litchina", "Litchina Helmet", [("talak_litchina", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["crown_coif", "Crown", [("coif_crown_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["aragon_crown", "Crown", [("aragon_crown", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian]],

	["talak_crown_ornate", "Ornate Crowned Helm", [("talak_crown_ornate", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["cuman_cap_a", "Cuman Hat", [("cuman_cap_a", imodbits_none), ("inv_cuman_cap_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_armor, [], [fac_kingdom_7]],

	["cuman_cap_b", "Cuman Hat", [("cuman_cap_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_armor, [], [fac_kingdom_7]],

	["cuman_cap_c", "Cuman Hat", [("cuman_cap_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_armor, [], [fac_kingdom_7]],

	["maciejowski_kettle_hat_a", "Kettle Hat", [("maciejowski_kettle_a", imodbits_none), ("inv_maciejowski_kettle_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["maciejowski_kettle_hat_b", "Kettle Hat", [("maciejowski_kettle_b", imodbits_none), ("inv_maciejowski_kettle_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["norman_coif_a", "Kettle Hat", [("red_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["maciejowski_crown", "Crowned Great Helm", [("crown_helm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["crowned_norman", "Crowned Norman Helm", [("crown_helmtet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["norman_coif_b", "Kettle Hat", [("norman_helmtet", imodbits_none), ("inv_norman_helmtet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_covers_beard, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rus_helm_a", "Gnezdovo Helm", [("gnezdovo_helm_a", imodbits_none), ("inv_gnezdovo_helm_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["rus_helmet_b", "Slavic Helm", [("rus_helmet_b", imodbits_none), ("inv_rus_helmet_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["norman_coif_c", "Kettle Helmet", [("blue_helmet", imodbits_none), ("inv_blue_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["norman_coif_d", "Kettle Hat", [("green_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["norman_coif_e", "Norman Helmet", [("white_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["teu_kettle_hat_a_mail", "Kettle Helm", [("teu_kettle_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_23]],

	["templar_kettlehat_a_mail", "Kettle Helm", [("templar_kettle_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_kingdom_23]],

	["hospitaller_kettlehat_a_mail", "Kettle Helm", [("templar_kettle_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_kingdom_23]],

	["kolpak_mail", "Cervilliere", [("kolpak_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_kingdom_23]],

	["mail_coif_b", "Decorated Mail Coif", [("bandage_coif_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor],

	["mail_coif_c", "Decorated Mail Coif", [("bandage_coif_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_armor],

	["norman_faceplate", "Scullcap wth Nose Guard", [("norman_faceplate_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["varangian_helm", "Varangian Helmet", [("varangian_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mamluke_helm", "Mamluke Helmet", [("mamluk_helmet", imodbits_none), ("inv_baltic_ponted_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["wooden_stick", "Wooden Stick", [("wooden_stick", imodbits_none)], 2|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar, 61, thrust_damage(0, pierce)|hit_points(9216)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(9, blunt)|weapon_length(62), imodbits_none],

	["cudgel", "Cudgel", [("club", imodbits_none)], 2|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar, 291, thrust_damage(0, pierce)|hit_points(18432)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(18, blunt)|weapon_length(68), imodbits_none],

	["hammer", "Hammer", [("iron_hammer_new", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar, 113, thrust_damage(0, pierce)|hit_points(13312)|spd_rtng(98)|abundance(100)|weight(1.25)|swing_damage(13, blunt)|weapon_length(58), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["club", "Club", [("club", imodbits_none)], 2|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar, 291, thrust_damage(0, pierce)|hit_points(18432)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(18, blunt)|weapon_length(68), imodbits_none, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["winged_mace", "Flanged Mace", [("flanged_mace", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 435, thrust_damage(0, pierce)|hit_points(22528)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(22, blunt)|weapon_length(68), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["spiked_mace", "Spiked Mace", [("spiked_mace_new", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 440, thrust_damage(0, pierce)|hit_points(24576)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(24, blunt)|weapon_length(73), imodbits_pick, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["military_hammer", "Military Hammer", [("military_hammer", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_axe_left_hip|itc_scimitar, 487, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(98)|abundance(100)|weight(1.25)|swing_damage(27, blunt)|weapon_length(58), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["maul", "Maul", [("maul_b", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_nodachi, 97, thrust_damage(0, pierce)|hit_points(36864)|spd_rtng(87)|abundance(100)|weight(6.0)|swing_damage(36, blunt)|difficulty(11)|weapon_length(69), imodbits_axe|imodbits_mace],

	["sledgehammer", "Sledgehammer", [("maul_c", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_nodachi, 101, thrust_damage(0, pierce)|hit_points(41984)|spd_rtng(86)|abundance(100)|weight(7.0)|swing_damage(41, blunt)|difficulty(12)|weapon_length(69), imodbits_axe|imodbits_mace],

	["warhammer", "Great Hammer", [("maul_d", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_nodachi, 290, thrust_damage(0, pierce)|hit_points(46080)|spd_rtng(83)|abundance(100)|weight(9.0)|swing_damage(45, blunt)|difficulty(14)|weapon_length(68), imodbits_axe|imodbits_mace],

	["pickaxe", "Pickaxe", [("fighting_pick_new", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_axe_left_hip|itc_scimitar, 562, thrust_damage(0, pierce)|hit_points(25600)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(25, pierce)|weapon_length(68), imodbits_pick, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["spiked_club", "Spiked Club", [("spiked_club", imodbits_none)], 2|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar, 298, thrust_damage(0, pierce)|hit_points(16384)|spd_rtng(95)|abundance(100)|weight(1.5)|swing_damage(16, pierce)|weapon_length(79), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["fighting_pick", "Fighting Pick", [("fighting_pick_new", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_axe_left_hip|itc_scimitar, 562, thrust_damage(0, pierce)|hit_points(25600)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(25, pierce)|weapon_length(68), imodbits_pick, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["military_pick", "Military Pick", [("steel_pick_new", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_axe_left_hip|itc_scimitar, 580, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(97)|abundance(100)|weight(1.25)|swing_damage(27, pierce)|weapon_length(64), imodbits_pick, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["morningstar", "Flanged Mace", [("bb_serbian_flanged_mace_1", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced, itcf_carry_axe_left_hip|itc_cleaver|itc_nodachi, 1300, thrust_damage(0, pierce)|hit_points(31744)|spd_rtng(93)|abundance(100)|weight(1.75)|swing_damage(31, pierce)|difficulty(13)|weapon_length(87), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sickle", "Sickle", [("sickle", imodbits_none)], 2|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itc_cleaver, 9, thrust_damage(0, pierce)|hit_points(22528)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(22, cut)|weapon_length(53), imodbits_none],

	["cleaver", "Cleaver", [("cleaver_new", imodbits_none)], 2|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itc_cleaver, 14, thrust_damage(0, pierce)|hit_points(24576)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(24, cut)|weapon_length(29), imodbits_none],

	["knife", "Knife", [("peasant_knife_new", imodbits_none)], 2|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger, 18, thrust_damage(20, pierce)|hit_points(22528)|spd_rtng(110)|abundance(100)|weight(0.5)|swing_damage(22, cut)|weapon_length(40), imodbits_sword],

	["butchering_knife", "Butchering Knife", [("khyber_knife_new", imodbits_none)], 2|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_right|itc_dagger, 23, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(108)|abundance(100)|weight(0.75)|swing_damage(25, cut)|weapon_length(61), imodbits_sword],

	["dagger", "Dagger", [("dagger_b", imodbits_none), ("dagger_b_scabbard", ixmesh_carry), ("dagger_b", imodbits_good), ("dagger_b_scabbard", ixmesh_carry|imodbits_good)], 2|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 37, thrust_damage(35, pierce)|hit_points(22528)|spd_rtng(109)|abundance(100)|weight(0.75)|swing_damage(22, cut)|weapon_length(47), imodbits_sword_high],

	["falchion", "Falchion", [("falchion_new", imodbits_none)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 2668, thrust_damage(5, pierce)|hit_points(41984)|spd_rtng(101)|abundance(100)|weight(1.25)|swing_damage(41, cut)|difficulty(8)|weapon_length(71), imodbits_sword, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["scimitar", "Scimitar", [("scimitar_a", imodbits_none), ("scab_scimeter_a", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 4027, thrust_damage(0, pierce)|hit_points(38912)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(38, cut)|weapon_length(97), imodbits_sword_high, [], [fac_culture_rus]],

	["scimitar_b", "Elite Scimitar", [("scimitar_b", imodbits_none), ("scab_scimeter_b", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 4417, thrust_damage(0, pierce)|hit_points(39936)|spd_rtng(97)|abundance(100)|weight(1.75)|swing_damage(39, cut)|weapon_length(100), imodbits_sword_high, [], [fac_culture_rus]],

	["arabian_sword_a", "Saracen Sword", [("arabian_sword_a", imodbits_none), ("scab_arabian_sword_a", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3615, thrust_damage(19, pierce)|hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|weapon_length(97), imodbits_sword_high, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arabian_sword_b", "Saracen Arming Sword", [("arabian_sword_b", imodbits_none), ("scab_arabian_sword_b", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2510, thrust_damage(25, pierce)|hit_points(30720)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(30, cut)|weapon_length(97), imodbits_sword_high, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["sarranid_cavalry_sword", "Saracen Cavalry Sword", [("arabian_sword_c", imodbits_none), ("scab_arabian_sword_c", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 4770, thrust_damage(9, pierce)|hit_points(39936)|spd_rtng(96)|abundance(100)|weight(1.75)|swing_damage(39, cut)|weapon_length(105), imodbits_sword_high, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arabian_sword_d", "Saracen Guard Sword", [("arabian_sword_d", imodbits_none), ("scab_arabian_sword_d", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3818, thrust_damage(20, pierce)|hit_points(37888)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(37, cut)|weapon_length(97), imodbits_sword_high, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["andalusian_sword", "Andalusian Sword", [("andalusian_sword", imodbits_none), ("scab_andalusian_sword", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3346, thrust_damage(18, pierce)|hit_points(35840)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(35, cut)|weapon_length(96), imodbits_sword_high, [], [fac_culture_andalus]],

	["hatchet", "Hatchet", [("vik_hoggox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 296, hit_points(20480)|spd_rtng(98)|abundance(25)|weight(1.0)|swing_damage(20, pierce)|difficulty(9)|weapon_length(48), imodbits_pick],

	["talak_warhammer", "Warhammer", [("warhammer", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_longsword, 969, thrust_damage(10, blunt)|hit_points(30720)|spd_rtng(97)|abundance(2)|weight(1.5)|swing_damage(30, blunt)|difficulty(7)|weapon_length(69), imodbits_pick],

	["talak_bastard_sword", "Hand and a Half Sword", [("talak_bastard_sword", imodbits_none), ("talak_scab_bastard_sword", ixmesh_carry), ("talak_bastard_sword", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_twohanded|itcf_carry_sword_back|itcf_show_holster_when_drawn|itc_dagger|itc_nodachi, 4709, thrust_damage(21, pierce)|hit_points(43008)|spd_rtng(93)|abundance(2)|weight(1.75)|swing_damage(42, cut)|difficulty(9)|weapon_length(100), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["raf_one_handed_axe_a", "One Handed Axe", [("vik_einhendi_danox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 623, hit_points(31744)|spd_rtng(95)|abundance(25)|weight(1.5)|swing_damage(31, pierce)|difficulty(9)|weapon_length(67), imodbits_pick],

	["raf_one_handed_axe_b", "One Handed Axe", [("vik_einhendi_breithofudox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 771, hit_points(33792)|spd_rtng(95)|abundance(25)|weight(1.75)|swing_damage(33, pierce)|difficulty(9)|weapon_length(70), imodbits_pick],

	["raf_one_handed_axe_c", "One Handed Axe", [("vik_einhendi_haloygox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 623, hit_points(31744)|spd_rtng(95)|abundance(25)|weight(1.5)|swing_damage(31, pierce)|difficulty(9)|weapon_length(67), imodbits_pick],

	["raf_one_handed_axe_d", "One Handed Axe", [("vik_einhendi_hedmarkrox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 239, hit_points(24576)|spd_rtng(98)|abundance(25)|weight(1.25)|swing_damage(24, pierce)|difficulty(9)|weapon_length(52), imodbits_pick],

	["raf_one_handed_axe_e", "One Handed Axe", [("vik_einhendi_trondrox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 623, hit_points(31744)|spd_rtng(95)|abundance(25)|weight(1.5)|swing_damage(31, pierce)|difficulty(9)|weapon_length(67), imodbits_pick],

	["raf_one_handed_axe_f", "One Handed Axe", [("vik_einhendi_vendelox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 203, hit_points(23552)|spd_rtng(98)|abundance(25)|weight(1.25)|swing_damage(23, pierce)|difficulty(9)|weapon_length(50), imodbits_pick],

	["raf_one_handed_axe_g", "One Handed Axe", [("vik_hoggox", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 171, hit_points(22528)|spd_rtng(98)|abundance(25)|weight(1.0)|swing_damage(22, pierce)|difficulty(9)|weapon_length(48), imodbits_pick],

	["raf_one_handed_axe_h", "Bearded Axe", [("talak_bearded_axe", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 285, hit_points(25600)|spd_rtng(97)|abundance(20)|weight(1.25)|swing_damage(25, pierce)|difficulty(7)|weapon_length(55), imodbits_pick],

	["raf_two_handed_axe_a", "Two Handed Axe", [("vik_tveirhendr_hedmarkox", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, itcf_carry_axe_back|itc_nodachi, 1933, hit_points(44032)|spd_rtng(86)|abundance(25)|weight(2.25)|swing_damage(43, pierce)|difficulty(10)|weapon_length(94), imodbits_pick],

	["raf_two_handed_axe_b", "Two Handed Axe", [("vik_tveirhendr_danox", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, itcf_carry_axe_back|itc_nodachi, 1933, hit_points(44032)|spd_rtng(86)|abundance(25)|weight(2.25)|swing_damage(43, pierce)|difficulty(10)|weapon_length(94), imodbits_pick],

	["raf_two_handed_axe_c", "Nordic Axe", [("talak_nordic_axe", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, itcf_carry_axe_back|itc_nodachi, 2196, hit_points(46080)|spd_rtng(84)|abundance(2)|weight(2.25)|swing_damage(45, pierce)|difficulty(12)|weapon_length(98), imodbits_pick],

	["sarranid_mace_1", "Iron Mace", [("mace_small_d", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 922, thrust_damage(0, pierce)|hit_points(31744)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(31, blunt)|weapon_length(71), imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 730, thrust_damage(0, pierce)|hit_points(32768)|spd_rtng(94)|abundance(100)|weight(1.75)|swing_damage(32, pierce)|difficulty(9)|weapon_length(71), imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 680, thrust_damage(0, pierce)|hit_points(31744)|spd_rtng(95)|abundance(100)|weight(1.75)|swing_damage(31, pierce)|difficulty(9)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_type_xii", "Counter Point Series Type XII Sword", [("sword_type_xii_low", imodbits_none), ("sword_1257_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3467, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_type_xiia", "Counter Point Series Type XIIA Sword", [("sword_type_xiia_low", imodbits_none), ("sword_bastard_1257_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_twohanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_dagger|itc_nodachi, 5236, thrust_damage(25, pierce)|hit_points(44032)|spd_rtng(93)|abundance(80)|weight(1.75)|swing_damage(43, cut)|difficulty(8)|weapon_length(103), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_type_xiii", "Counter Point Series Type XIII Sword", [("sword_type_xiii_low", imodbits_none), ("sword_1257_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3467, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_type_xiiia", "Counter Point Series Type XIIIA Sword", [("sword_type_xiiia_low", imodbits_none), ("sword_bastard_1257_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_twohanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_dagger|itc_nodachi, 5576, thrust_damage(25, pierce)|hit_points(45056)|spd_rtng(92)|abundance(80)|weight(1.75)|swing_damage(44, cut)|difficulty(8)|weapon_length(105), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_type_xiiib", "Counter Point Series Type XIIIB Sword", [("sword_type_xiiib_low", imodbits_none), ("sword_1257_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary|itp_secondary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3467, thrust_damage(22, pierce)|hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_type_xiv", "Counter Point Series Type XIV Sword", [("sword_type_xiv_low", imodbits_none), ("sword_short_1257_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2560, thrust_damage(36, pierce)|hit_points(25600)|spd_rtng(100)|abundance(100)|weight(1.25)|swing_damage(25, cut)|difficulty(8)|weapon_length(80), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["cp391_sword", "Counter Point Series Knightly Sword", [("cp391_sword1", imodbits_none), ("cp391_sword1_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3207, thrust_damage(26, pierce)|hit_points(37888)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(37, cut)|difficulty(8)|weapon_length(88), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["spatha", "Spatha", [("spatha", imodbits_none), ("spatha_scab", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2205, thrust_damage(32, pierce)|hit_points(33792)|spd_rtng(100)|abundance(100)|weight(1.25)|swing_damage(33, cut)|difficulty(8)|weapon_length(81), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["bb_serbian_sword_1", "Serbian Sword ", [("bb_serbian_sword_1", imodbits_none), ("bb_serbian_sword_1_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["bb_serbian_sword_5", "Serbian Sword", [("bb_serbian_sword_5", imodbits_none), ("bb_serbian_sword_5_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["bb_rus_sword_6", "Rus Sword", [("bb_rus_sword_6", imodbits_none), ("bb_rus_sword_6_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["bb_rus_sword_1", "Rus Sword", [("bb_rus_sword_1", imodbits_none), ("bb_rus_sword_1_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["bb_rus_sword_3", "Rus Sword", [("bb_rus_sword_3", imodbits_none), ("bb_rus_sword_3_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["two_handed_cleaver", "War Cleaver", [("military_cleaver_a", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_nodachi, 350, hit_points(46080)|spd_rtng(85)|abundance(100)|weight(2.25)|swing_damage(45, cut)|difficulty(10)|weapon_length(97), imodbits_sword_high, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b", imodbits_none)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 360, thrust_damage(0, pierce)|hit_points(34816)|spd_rtng(88)|abundance(100)|weight(2.25)|swing_damage(34, cut)|weapon_length(91), imodbits_sword_high, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["military_cleaver_c", "Military Cleaver", [("military_cleaver_c", imodbits_none)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 370, thrust_damage(0, pierce)|hit_points(35840)|spd_rtng(88)|abundance(100)|weight(2.25)|swing_damage(35, cut)|weapon_length(91), imodbits_sword_high, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["military_sickle_a", "Military Sickle", [("military_sickle_a", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 340, thrust_damage(0, pierce)|hit_points(31744)|spd_rtng(101)|abundance(100)|weight(1.25)|swing_damage(31, pierce)|difficulty(9)|weapon_length(75), imodbits_axe|imodbits_mace],

	["shortened_voulge", "Shortened Voulge", [("two_handed_battle_axe_c", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_unbalanced, itcf_carry_axe_back|itc_nodachi, 400, thrust_damage(0, pierce)|hit_points(47104)|spd_rtng(93)|abundance(100)|weight(1.75)|swing_damage(46, cut)|difficulty(10)|weapon_length(99), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["long_axe", "Long Axe", [("long_danox", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_carry_axe_back|itc_staff, 1300, thrust_damage(19, blunt)|hit_points(54272)|spd_rtng(75)|abundance(100)|weight(2.75)|swing_damage(53, cut)|difficulty(10)|weapon_length(115), imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_nordic, fac_culture_mazovian, fac_culture_baltic]],

	["long_axe_alt", "Long Axe", [("long_danox", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_unbalanced, itcf_carry_axe_back|itc_nodachi, 1300, thrust_damage(0, pierce)|hit_points(54272)|spd_rtng(75)|abundance(100)|weight(2.75)|swing_damage(53, cut)|difficulty(10)|weapon_length(115), imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_nordic, fac_culture_mazovian, fac_culture_baltic]],

	["long_axe_b", "Long War Axe", [("long_hedmarkox", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_carry_axe_back|itc_staff, 1100, thrust_damage(18, blunt)|hit_points(58368)|spd_rtng(71)|abundance(100)|weight(3.0)|swing_damage(57, cut)|difficulty(10)|weapon_length(122), imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_nordic, fac_culture_mazovian, fac_culture_baltic]],

	["long_axe_b_alt", "Long War Axe", [("long_hedmarkox", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_unbalanced, itcf_carry_axe_back|itc_nodachi, 1100, thrust_damage(0, pierce)|hit_points(58368)|spd_rtng(71)|abundance(100)|weight(3.0)|swing_damage(57, cut)|difficulty(10)|weapon_length(122), imodbits_axe|imodbits_mace, [], [fac_culture_finnish, fac_culture_nordic, fac_culture_mazovian, fac_culture_baltic]],

	["bardiche", "Bardiche", [("two_handed_battle_axe_d", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_unbalanced, itcf_carry_axe_back|itc_nodachi, 600, thrust_damage(0, pierce)|hit_points(47104)|spd_rtng(83)|abundance(100)|weight(2.5)|swing_damage(46, cut)|difficulty(10)|weapon_length(101), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["hafted_blade_b", "Hafted Blade", [("khergit_pike_b", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_carry_spear|itc_guandao, 500, thrust_damage(15, pierce)|hit_points(52224)|spd_rtng(83)|abundance(100)|weight(2.25)|swing_damage(51, cut)|weapon_length(130), imodbits_polearm, [], [fac_culture_mongol]],

	["hafted_blade_a", "Hafted Blade", [("khergit_pike_a", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_carry_spear|itc_guandao, 500, thrust_damage(16, pierce)|hit_points(55296)|spd_rtng(75)|abundance(100)|weight(2.75)|swing_damage(54, cut)|weapon_length(153), imodbits_polearm, [], [fac_culture_mongol]],

	["shortened_military_scythe", "Shortened Military Scythe", [("two_handed_battle_scythe_a", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(49152)|spd_rtng(90)|abundance(100)|weight(2.0)|swing_damage(48, cut)|difficulty(10)|weapon_length(114), imodbits_axe|imodbits_mace, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["sword_viking_1", "Nordic Sword", [("sword_viking_c", imodbits_none), ("sword_viking_c_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2975, thrust_damage(21, pierce)|hit_points(33792)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(33, cut)|weapon_length(96), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["sword_viking_2", "Nordic Sword", [("sword_viking_b", imodbits_none), ("sword_viking_b_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3093, thrust_damage(21, pierce)|hit_points(34816)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(34, cut)|weapon_length(95), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small", imodbits_none), ("sword_viking_b_small_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1994, thrust_damage(21, pierce)|hit_points(31744)|spd_rtng(100)|abundance(100)|weight(1.25)|swing_damage(31, cut)|weapon_length(82), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["sword_viking_3", "Nordic War Sword", [("sword_viking_a", imodbits_none), ("sword_viking_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3467, thrust_damage(21, pierce)|hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|weapon_length(95), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small", imodbits_none), ("sword_viking_a_small_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2260, thrust_damage(33, pierce)|hit_points(29696)|spd_rtng(100)|abundance(100)|weight(1.25)|swing_damage(29, cut)|weapon_length(82), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["sword_khergit_1", "Sabre", [("khergit_sword_b", imodbits_none), ("khergit_sword_b_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 2741, hit_points(39936)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(39, cut)|weapon_length(86), imodbits_sword_high, [], [fac_culture_mongol, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_2", "Sabre", [("khergit_sword_c", imodbits_none), ("khergit_sword_c_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 3036, hit_points(40960)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(40, cut)|weapon_length(88), imodbits_sword_high, [], [fac_culture_mongol, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_3", "Sabre", [("khergit_sword_a", imodbits_none), ("khergit_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 3134, hit_points(41984)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(41, cut)|weapon_length(87), imodbits_sword_high, [], [fac_culture_mongol, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d", imodbits_none), ("khergit_sword_d_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 3383, hit_points(43008)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(42, cut)|weapon_length(88), imodbits_sword_high, [], [fac_culture_mongol, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["mace_1", "Spiked Club", [("mace_d", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 494, thrust_damage(0, pierce)|hit_points(23552)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(23, pierce)|weapon_length(70), imodbits_axe|imodbits_mace],

	["mace_2", "Knobbed Mace", [("mace_a", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 731, thrust_damage(0, pierce)|hit_points(28672)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(28, blunt)|weapon_length(70), imodbits_axe|imodbits_mace],

	["mace_3", "Spiked Mace", [("mace_c", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 785, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(29, blunt)|weapon_length(70), imodbits_axe|imodbits_mace],

	["mace_4", "Winged Mace", [("mace_b", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 922, thrust_damage(0, pierce)|hit_points(31744)|spd_rtng(96)|abundance(100)|weight(1.5)|swing_damage(31, blunt)|weapon_length(71), imodbits_axe|imodbits_mace],

	["club_with_spike_head", "Spiked Staff", [("mace_e", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_thrust_twohanded|itcf_carry_axe_back|itc_dagger|itc_nodachi, 122, thrust_damage(24, pierce)|hit_points(21504)|spd_rtng(72)|abundance(100)|weight(2.5)|swing_damage(21, blunt)|difficulty(9)|weapon_length(115), imodbits_axe|imodbits_mace, [], [fac_kingdom_6]],

	["long_spiked_club", "Long Spiked Club", [("mace_long_c", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_axe_back|itc_staff, 200, thrust_damage(6, blunt)|hit_points(60416)|spd_rtng(79)|abundance(100)|weight(2.75)|swing_damage(59, blunt)|weapon_length(126), imodbits_axe|imodbits_mace, [], [fac_culture_rus]],

	["long_hafted_knobbed_mace", "Long Hafted Knobbed Mace", [("mace_long_a", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_axe_back|itc_staff, 250, thrust_damage(7, blunt)|hit_points(63488)|spd_rtng(79)|abundance(100)|weight(2.75)|swing_damage(62, blunt)|weapon_length(133), imodbits_axe|imodbits_mace, [], [fac_culture_rus]],

	["long_hafted_spiked_mace", "Long Hafted Spiked Mace", [("mace_long_b", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itcf_carry_axe_back|itc_staff, 300, thrust_damage(8, blunt)|hit_points(2048)|spd_rtng(71)|abundance(100)|weight(3.0)|swing_damage(66, blunt)|weapon_length(140), imodbits_axe|imodbits_mace, [], [fac_culture_rus]],

	["studded_club", "Studded Club", [("studded_club", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_axe_back|itc_greatsword, 260, thrust_damage(8, blunt)|hit_points(38912)|spd_rtng(92)|abundance(100)|weight(2.0)|swing_damage(38, blunt)|difficulty(8)|weapon_length(92), imodbits_axe|imodbits_mace, [], [fac_culture_rus]],

	["scythe", "Scythe", [("scythe", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_staff, 43, thrust_damage(25, cut)|hit_points(30720)|spd_rtng(88)|abundance(100)|weight(3.0)|swing_damage(30, cut)|weapon_length(182), imodbits_polearm],

	["pitch_fork", "Pitch Fork", [("pitch_fork", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itc_spear, 19, thrust_damage(23, pierce)|spd_rtng(91)|abundance(100)|weight(3.5)|swing_damage(0, blunt)|weapon_length(154), imodbits_polearm],

	["military_fork", "Military Fork", [("military_fork", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itc_spear, 153, thrust_damage(28, pierce)|spd_rtng(91)|abundance(100)|weight(4.5)|swing_damage(0, blunt)|weapon_length(135), imodbits_polearm],

	["battle_fork", "Battle Fork", [("battle_fork", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itc_spear, 282, thrust_damage(35, pierce)|spd_rtng(93)|abundance(100)|weight(4.5)|swing_damage(0, blunt)|weapon_length(142), imodbits_polearm],

	["glaive", "Glaive", [("glaive_b", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_staff, 700, thrust_damage(35, cut)|hit_points(53248)|spd_rtng(72)|abundance(100)|weight(2.75)|swing_damage(52, cut)|weapon_length(160), imodbits_polearm, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["staff", "Staff", [("wooden_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 36, thrust_damage(8, blunt)|hit_points(10240)|spd_rtng(94)|abundance(100)|weight(1.5)|swing_damage(10, blunt)|weapon_length(128), imodbits_polearm],

	["quarter_staff", "Quarter Staff", [("quarter_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 60, thrust_damage(10, blunt)|hit_points(13312)|spd_rtng(93)|abundance(100)|weight(2.0)|swing_damage(13, blunt)|weapon_length(137), imodbits_polearm],

	["iron_staff", "Iron Staff", [("iron_staff", imodbits_none)], 4|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 202, thrust_damage(12, blunt)|hit_points(17408)|spd_rtng(89)|abundance(100)|weight(2.0)|swing_damage(17, blunt)|weapon_length(128), imodbits_polearm],

	["military_scythe", "Military Scythe", [("spear_e_2-5m", imodbits_none), ("spear_c_2-5m", imodbits_bad)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 155, thrust_damage(28, pierce)|hit_points(41984)|spd_rtng(89)|abundance(100)|weight(2.5)|swing_damage(41, cut)|difficulty(10)|weapon_length(153), imodbits_polearm],

	["light_lance", "Light Lance", [("spear_b_2-75m", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_cutting_spear, 180, thrust_damage(28, pierce)|hit_points(10240)|spd_rtng(86)|abundance(100)|weight(4.5)|swing_damage(10, cut)|weapon_length(250), imodbits_polearm],

	["lance", "Lance", [("spear_d_2-8m", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_cutting_spear, 135, thrust_damage(30, pierce)|hit_points(10240)|spd_rtng(85)|abundance(100)|weight(4.75)|swing_damage(10, cut)|weapon_length(255), imodbits_polearm],

	["heavy_lance", "Heavy Lance", [("spear_f_2-9m", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_cutting_spear, 180, thrust_damage(34, pierce)|hit_points(10240)|spd_rtng(82)|abundance(100)|weight(5.0)|swing_damage(10, cut)|difficulty(10)|weapon_length(260), imodbits_polearm],

	["muslim_lance", "Heavy Lance", [("muslim_lance", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_cutting_spear, 180, thrust_damage(36, pierce)|hit_points(11264)|spd_rtng(80)|abundance(100)|weight(5.0)|swing_damage(11, cut)|difficulty(10)|weapon_length(262), imodbits_polearm, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	
	["heraldic_lance", "Heraldic Lance", [("heraldic_lance", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_cutting_spear, 200, thrust_damage(40, pierce)|hit_points(10240)|spd_rtng(82)|abundance(100)|weight(2.75)|swing_damage(10, cut)|difficulty(10)|weapon_length(260), imodbits_polearm, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_heraldic_lance_1", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["bamboo_spear", "Bamboo Spear", [("arabian_spear_a_3m", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 80, thrust_damage(30, pierce)|hit_points(12288)|spd_rtng(87)|abundance(100)|weight(2.0)|swing_damage(12, cut)|weapon_length(200), imodbits_polearm, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["berber_spear", "Berber Spear", [("berber_spear", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 80, thrust_damage(30, pierce)|hit_points(12288)|spd_rtng(87)|abundance(100)|weight(2.0)|swing_damage(12, cut)|weapon_length(200), imodbits_polearm, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["spear_a", "Spear", [("vik_atgeirr1", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 156, thrust_damage(46, pierce)|hit_points(29696)|spd_rtng(99)|abundance(100)|weight(2.25)|swing_damage(29, cut)|weapon_length(103), imodbits_polearm],

	
	["spear_b", "Spear", [("vik_bryntvari", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 155, thrust_damage(51, pierce)|hit_points(33792)|spd_rtng(98)|abundance(100)|weight(1.25)|swing_damage(33, cut)|weapon_length(76), imodbits_polearm],

	["spear_c", "Spear", [("vik_bryntvari2", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 135, thrust_damage(45, pierce)|hit_points(28672)|spd_rtng(99)|abundance(100)|weight(2.25)|swing_damage(28, cut)|weapon_length(105), imodbits_polearm],

	["spear_d", "Spear", [("vik_fjadraspjot", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 143, thrust_damage(41, pierce)|hit_points(23552)|spd_rtng(91)|abundance(100)|weight(2.75)|swing_damage(23, cut)|weapon_length(124), imodbits_polearm],

	["spear_e", "Spear", [("vik_hoggkesja", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 142, thrust_damage(41, pierce)|hit_points(23552)|spd_rtng(91)|abundance(100)|weight(2.75)|swing_damage(23, cut)|weapon_length(121), imodbits_polearm],

	["spear_f", "Spear", [("vik_kastad_krokaspjott", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 146, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(89)|abundance(100)|weight(2.25)|swing_damage(29, cut)|weapon_length(155), imodbits_polearm],

	["spear_g", "Spear", [("vik_kastspjottmidtaggir", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 142, thrust_damage(46, pierce)|hit_points(29696)|spd_rtng(95)|abundance(100)|weight(2.25)|swing_damage(29, cut)|weapon_length(105), imodbits_polearm],

	["spear_h", "Spear", [("vik_krokaspjott1", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 145, thrust_damage(33, pierce)|hit_points(22528)|spd_rtng(90)|abundance(100)|weight(2.75)|swing_damage(22, cut)|weapon_length(152), imodbits_polearm],

	["spear_i", "Spear", [("vik_krokaspjott2", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 141, thrust_damage(41, pierce)|hit_points(25600)|spd_rtng(91)|abundance(100)|weight(2.5)|swing_damage(25, cut)|weapon_length(126), imodbits_polearm],

	["spear_j", "Spear", [("vik_langr_bryntvari", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 170, thrust_damage(30, pierce)|hit_points(17408)|spd_rtng(91)|abundance(100)|weight(3.5)|swing_damage(17, cut)|weapon_length(192), imodbits_polearm],

	["spear_k", "Spear", [("vik_langr_hoggspjott1", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 160, thrust_damage(32, pierce)|hit_points(18432)|spd_rtng(92)|abundance(100)|weight(3.5)|swing_damage(18, cut)|weapon_length(187), imodbits_polearm],

	["spear_l", "Spear", [("vik_langr_svia", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 170, thrust_damage(28, pierce)|hit_points(16384)|spd_rtng(91)|abundance(100)|weight(3.75)|swing_damage(16, cut)|weapon_length(195), imodbits_polearm],

	["spear_m", "Spear", [("vik_spjot", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 160, thrust_damage(41, pierce)|hit_points(24576)|spd_rtng(93)|abundance(100)|weight(2.75)|swing_damage(24, cut)|weapon_length(119), imodbits_polearm],

	["spear_n", "Spear", [("vik_spjotkesja", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 175, thrust_damage(29, pierce)|hit_points(16384)|spd_rtng(88)|abundance(100)|weight(3.75)|swing_damage(16, cut)|weapon_length(193), imodbits_polearm],

	["spear_o", "Spear", [("vik_svia2", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 150, thrust_damage(41, pierce)|hit_points(23552)|spd_rtng(112)|abundance(100)|weight(2.75)|swing_damage(23, cut)|weapon_length(120), imodbits_polearm],

	["spear_p", "Spear", [("vik_sviar", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 160, thrust_damage(43, pierce)|hit_points(27648)|spd_rtng(94)|abundance(100)|weight(2.25)|swing_damage(27, cut)|weapon_length(108), imodbits_polearm],

	["wooden_shield", "Wooden Shield", [("shield_round_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["nordic_shield", "Nordic Shield", [("shield_round_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 28, hit_points(44)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(38), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 5, hit_points(31)|spd_rtng(41)|abundance(100)|weight(2.5)|shield_width(40)|resistance(34), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 4, hit_points(26)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(40)|resistance(32), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		
	["tab_shield_small_round_n", "Plain Shield", [("tableau_shield_small_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 6, hit_points(31)|spd_rtng(105)|abundance(100)|weight(2.0)|shield_width(40)|resistance(35), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":trigger_param_1", ":trigger_param_2")
		]),
		
#####Begin add effect to shields
(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
	["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 56, hit_points(35)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(50)|resistance(48), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 84, hit_points(41)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(50)|resistance(55), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(47)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_round_d", "Well Made Round Shield", [("tableau_shield_round_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 152, hit_points(51)|spd_rtng(84)|abundance(100)|weight(4.0)|shield_width(50)|resistance(67), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_round_e", "Heavy Round Shield", [("tableau_shield_round_4", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_kite_c", "Kite Shield", [("tableau_shield_kite_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_kite_cav_a", "Horseman's Kite Shield", [("tableau_shield_kite_4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(31)|spd_rtng(103)|abundance(100)|weight(2.0)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_kite_cav_b", "Knightly Kite Shield", [("tableau_shield_kite_4", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 76, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(70)|shield_height(50), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_heater_c", "Heater Shield", [("tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_heater_cav_a", "Horseman's Heater Shield", [("tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(30)|spd_rtng(103)|abundance(100)|weight(2.0)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_heater_cav_b", "Knightly Heater Shield", [("tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 76, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(70)|shield_height(50), imodbits_shield,
		[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_pavise_d", "Heavy Board Shield", [("tableau_shield_pavise_1", imodbits_none)], itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 1594, hit_points(98)|spd_rtng(78)|abundance(100)|weight(5.0)|shield_width(43)|resistance(67)|shield_height(100), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 30, hit_points(31)|spd_rtng(105)|abundance(100)|weight(2.0)|shield_width(40)|resistance(61), imodbits_shield,
		[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 40, hit_points(37)|spd_rtng(103)|abundance(100)|weight(2.5)|shield_width(40)|resistance(67), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 45, hit_points(42)|spd_rtng(100)|abundance(100)|weight(3.0)|shield_width(40)|resistance(70), imodbits_shield,
		[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":trigger_param_1", ":trigger_param_2")
#####Begin add effect to shields for tableau
#For none-culture
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["lit_pavise_a_3", "Lithuanian Shield", [("lithuanian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_b_3", "Lithuanian Shield", [("lithuanian_shield2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_c_3", "Lithuanian Shield", [("lithuanian_shield3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_d_3", "Lithuanian Shield", [("lithuanian_shield4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_e_3", "Lithuanian Shield", [("lithuanian_shield5", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_f_3", "Lithuanian Shield", [("lithuanian_shield6", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_g_3", "Lithuanian Shield", [("lithuanian_shield7", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lit_pavise_h_3", "Lithuanian Shield", [("lithuanian_shield8", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 208, hit_points(64)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(61)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["lithuanian_shield9", "Heavy Lithuanian Shield", [("lithuanian_shield9", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 276, hit_points(70)|spd_rtng(81)|abundance(100)|weight(5.5)|shield_width(40)|resistance(67)|shield_height(60), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_2]],

	["arab_shield_a_3", "Saracen Round Shield", [("arab_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_b_3", "Saracen Round Shield", [("arab_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_c_3", "Saracen Round Shield", [("arab_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_d_3", "Saracen Round Shield", [("arab_shield_d", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_e_3", "Saracen Round Shield", [("arab_shield_e", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_f_3", "Saracen Round Shield", [("arab_shield_f", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_g_3", "Saracen Round Shield", [("arab_shield_g", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_h_3", "Saracen Round Shield", [("arab_shield_h", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_shield_i_3", "Saracen Round Shield", [("arab_shield_i", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["cuman_shield_a_3", "Cuman Round Shield", [("cuman_shield_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_7]],

	["cuman_shield_b_3", "Cuman Round Shield", [("cuman_shield_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_7]],

	["cuman_shield_c_3", "Cuman Round Shield", [("cuman_shield_c", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 114, hit_points(54)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(50)|resistance(61), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_7]],

	["talak_buckler", "Buckler", [("talak_buckler", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_dagger_front_left, 0, hit_points(25)|spd_rtng(140)|abundance(100)|weight(1.0)|shield_width(32)|resistance(24), imodbits_shield, 
#####Begin add effect to shields
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["tab_shield_iberia_c", "Iberian Shield", [("tableau_shield_iberia", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_iberia_shield", ":trigger_param_1", ":trigger_param_2")

#####Begin add effect to shields for tableau
#For culture-wise
#old: 		])]
#old: ,
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		
		
		 [fac_culture_iberian]],

	["berber_shield_3", "Berber Shield", [("berber_shield", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_marinid]],

	["byz_shield", "Heavy Byzantine Kite Shield", [("byz_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(51)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(36)|resistance(67)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_kite", "Kite Shield", [("tableau_shield_kite_byz", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 67, hit_points(64)|spd_rtng(85)|abundance(100)|weight(5.5)|shield_width(40)|resistance(67)|shield_height(65), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_byz", ":trigger_param_1", ":trigger_param_2")

#####Begin add effect to shields TABLEAU + CULTURE
#old: 		])]
#old: ,
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		
		
		 [fac_culture_rus, fac_culture_mazovian, fac_culture_baltic]],

	["byz_shield_round", "Round Shield", [("tableau_shield_round_byz", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 76, hit_points(64)|spd_rtng(90)|abundance(100)|weight(5.0)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":trigger_param_1", ":trigger_param_2")
	
#####Begin add effect to shields TABLEAU + CULTURE
#old: 		])]
#old: ,
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		
		
		
		[fac_culture_rus]],

	["adarga_a", "Moorish Shield", [("adarga_a", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["adarga_b", "Moorish Shield", [("adarga_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["byz_shield_1", "Byzantine Shield", [("byz_shield_1", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_2", "Byzantine Shield", [("byz_shield_2", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_3", "Byzantine Cavalry Shield", [("byz_shield_3", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_4", "Byzantine Infantry Shield", [("byz_shield_4", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byz_shield_5", "Byzantine Infantry Shield", [("byz_shield_5", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_shield_1", "Almond Shield", [("rus_shield_1", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["rus_shield_2", "Almond Shield", [("rus_shield_2", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["reiforced_shield_horse", "Almond Shield", [("reiforced_shield_horse", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["reiforced_shield_infantry", "Almond Shield", [("reiforced_shield_infantry", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["1257_pavise", "Pavise Shield", [("1257_pavise", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(40)|resistance(61)|shield_height(80), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":trigger_param_1", ":trigger_param_2")

#####Begin add effect to shields for tableau RAW
#old: 		])]
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])]
		
		],
		#####End add effect to shields
		

	["jarid", "Jarids", [("jarid_new", imodbits_none), ("jarid_quiver", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 560, thrust_damage(29, cut)|max_ammo(5)|spd_rtng(89)|abundance(100)|weight(4.0)|accuracy(95)|difficulty(2)|weapon_length(65)|shoot_speed(27), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])],
		[fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["darts", "Darts", [("dart_b", imodbits_none), ("dart_b_bag", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 155, thrust_damage(36, cut)|max_ammo(7)|spd_rtng(95)|abundance(100)|weight(5.0)|difficulty(1)|weapon_length(32)|shoot_speed(26), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["war_darts", "War Darts", [("dart_a", imodbits_none), ("dart_a_bag", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 285, thrust_damage(38, cut)|max_ammo(7)|spd_rtng(93)|abundance(100)|weight(5.0)|difficulty(1)|weapon_length(45)|shoot_speed(25), imodbits_thrown,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["javelin", "Javelins", [("javelin", imodbits_none), ("javelins_quiver_new", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 300, thrust_damage(31, cut)|max_ammo(5)|spd_rtng(91)|abundance(100)|weight(5.0)|accuracy(95)|difficulty(1)|weapon_length(75)|shoot_speed(28), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["balt_javelin", "Balt Javelins", [("javelin", imodbits_none), ("javelins_quiver_new", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 300, thrust_damage(31, cut)|max_ammo(10)|spd_rtng(91)|abundance(100)|weight(5.0)|accuracy(95)|difficulty(1)|weapon_length(75)|shoot_speed(28), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])],
		[fac_culture_mazovian, fac_culture_baltic]],

	["throwing_spears", "Throwing Spears", [("jarid_new_b", imodbits_none), ("jarid_new_b_bag", ixmesh_carry)], 10|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 525, thrust_damage(36, cut)|max_ammo(5)|spd_rtng(87)|abundance(100)|weight(4.0)|accuracy(95)|difficulty(2)|weapon_length(65)|shoot_speed(23), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["stones", "Stones", [("throwing_stone", imodbits_none)], 10|itp_merchandise|itp_primary, itcf_throw_stone, 1, thrust_damage(4, blunt)|max_ammo(18)|spd_rtng(97)|abundance(100)|weight(4.0)|weapon_length(8)|shoot_speed(9), imodbit_large_bag,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["throwing_knives", "Throwing Knives", [("throwing_knife", imodbits_none)], 10|itp_merchandise|itp_primary, itcf_throw_knife, 76, thrust_damage(13, cut)|max_ammo(14)|spd_rtng(110)|abundance(100)|weight(3.5)|shoot_speed(9), imodbits_thrown, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["throwing_daggers", "Throwing Daggers", [("throwing_dagger", imodbits_none)], 10|itp_merchandise|itp_primary, itcf_throw_knife, 193, thrust_damage(15, cut)|max_ammo(13)|spd_rtng(102)|abundance(100)|weight(3.5)|shoot_speed(11), imodbits_thrown,
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],
	
	["light_throwing_axes", "Light Throwing Axes", [("francisca", imodbits_none)], 10|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_axe, 360, thrust_damage(35, cut)|max_ammo(5)|spd_rtng(90)|abundance(5)|weight(5.0)|difficulty(2)|weapon_length(53)|shoot_speed(11), imodbits_thrown_minus_heavy],

	["light_throwing_axes_melee", "Light Throwing Axe", [("francisca", imodbits_none)], 2|itp_primary|itp_bonus_against_shield, itc_scimitar, 360, hit_points(26624)|spd_rtng(99)|abundance(5)|weight(1.0)|swing_damage(26, cut)|difficulty(2)|weapon_length(53), imodbits_thrown_minus_heavy],

	["hunting_bow", "Hunting Self Bow", [("short_bow", imodbits_none), ("short_bow_carry", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 17, thrust_damage(5, cut)|spd_rtng(75)|abundance(100)|weight(1.0)|accuracy(97)|shoot_speed(45), imodbits_bow],

	["short_bow", "Self Bow", [("hunting_bow", imodbits_none), ("hunting_bow_carry", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 58, thrust_damage(6, cut)|spd_rtng(70)|abundance(100)|weight(1.0)|accuracy(95)|difficulty(3)|shoot_speed(68), imodbits_bow],

	["nomad_bow", "Hun Bow", [("nomad_bow", imodbits_none), ("nomad_bow_case", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 164, thrust_damage(9, cut)|spd_rtng(60)|abundance(100)|weight(1.25)|accuracy(94)|difficulty(4)|shoot_speed(75), imodbits_bow, [], [fac_culture_mongol, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium, fac_kingdom_7, fac_kingdom_31]],

	["long_bow", "Long Bow", [("long_bow", imodbits_none), ("long_bow_carry", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 145, thrust_damage(8, cut)|spd_rtng(45)|abundance(100)|weight(1.75)|accuracy(91)|difficulty(5)|shoot_speed(82), imodbits_bow, [], [fac_kingdom_6, fac_kingdom_4, fac_kingdom_11, fac_kingdom_14, fac_kingdom_9, fac_kingdom_12, fac_kingdom_13]],
    #START EDIT
	#Default ["khergit_bow", "Mongol Bow", [("khergit_bow", imodbits_none), ("khergit_bow_case", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 269, thrust_damage(8, cut)|spd_rtng(50)|abundance(100)|weight(1.25)|accuracy(93)|difficulty(6)|shoot_speed(79), imodbits_bow, [], [fac_culture_mongol]],
	["khergit_bow", "Mongol Bow", [("nomad_bow", imodbits_none), ("nomad_bow_case", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 269, thrust_damage(8, cut)|spd_rtng(50)|abundance(100)|weight(1.25)|accuracy(93)|difficulty(6)|shoot_speed(79), imodbits_bow, [], [fac_culture_mongol]],
	#Edited in item_kinds.txt
    ##END EDIT KHERGIT BOW MONGOL BOW
	["strong_bow", "Composite Bow", [("strong_bow", imodbits_none), ("strong_bow_case", ixmesh_carry)], 8|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 437, thrust_damage(7, cut)|spd_rtng(47)|abundance(100)|weight(1.25)|accuracy(95)|difficulty(2)|shoot_speed(70), imodbits_crossbow, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium, fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian, fac_culture_rus]],

	["hunting_crossbow", "Hunting Crossbow", [("crossbow_new", imodbits_none)], 9|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 22, thrust_damage(30, cut)|max_ammo(1)|spd_rtng(45)|abundance(100)|weight(2.25)|shoot_speed(45), imodbits_crossbow],

	["light_crossbow", "Light Crossbow", [("crossbow_new", imodbits_none)], 9|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 67, thrust_damage(32, cut)|max_ammo(1)|spd_rtng(35)|abundance(100)|weight(2.5)|difficulty(7)|shoot_speed(52), imodbits_crossbow],

	["crossbow", "Crossbow", [("crossbow_b", imodbits_none)], 9|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 182, thrust_damage(36, cut)|max_ammo(1)|spd_rtng(30)|abundance(100)|weight(3.0)|difficulty(8)|shoot_speed(75), imodbits_crossbow],

	["heavy_crossbow", "Heavy Crossbow", [("crossbow_c", imodbits_none)], 9|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 349, thrust_damage(44, cut)|max_ammo(1)|spd_rtng(25)|abundance(100)|weight(3.5)|difficulty(9)|shoot_speed(80), imodbits_crossbow],

	["sniper_crossbow", "Siege Crossbow", [("crossbow_c", imodbits_none)], 9|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 683, thrust_damage(50, cut)|max_ammo(1)|spd_rtng(20)|abundance(100)|weight(3.75)|difficulty(10)|shoot_speed(90), imodbits_crossbow],
####Begin default Torch
#	["torch", "Torch", [("club", imodbits_none)], 2|itp_primary, itc_scimitar, 11, thrust_damage(0, pierce)|hit_points(11264)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(11, blunt)|weapon_length(95), imodbits_none, 
#	[(ti_on_init_item,
#		[
#			(set_position_delta, 0, 60, 0),
#			(particle_system_add_new, "psys_torch_fire"),
#			(particle_system_add_new, "psys_torch_smoke"),
#			(set_current_color, 150, 130, 70),
#			(add_point_light, 10, 30)
#		])]
#	],
####End default torch

	["torch", "Torch", [("club", imodbits_none)], itp_type_shield|itp_shield_no_parry|itp_force_attach_left_hand|itp_merchandise, 0,33, weight(2)|abundance(100)|body_armor(5)|hit_points(4)|spd_rtng(96)|shield_height(1)|shield_width(1), imodbits_none,
	[(ti_on_init_item,
		[
			(set_position_delta, 0, 60, 0),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(set_current_color, 150, 130, 70),
			(add_point_light, 10, 30)
		])]
	],
#End edited torch
#If adding new weapons, don't use morghs just copy their code into the item_kinds unless you absolutely have to.
	["lyre", "Lyre", [("lyre", imodbits_none)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_next_item_as_melee, itcf_carry_bow_back, 118, hit_points(480)|spd_rtng(82)|abundance(100)|weight(2.5)|shield_width(90)|resistance(1), imodbits_none],

	["lute", "Lute", [("lute", imodbits_none)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_next_item_as_melee, itcf_carry_bow_back, 118, hit_points(480)|spd_rtng(82)|abundance(100)|weight(2.5)|shield_width(90)|resistance(1), imodbits_none],

	["khergit_war_helmet", "Mongol War Helmet", [("tattered_steppe_cap_a_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_guard_helmet", "Mongol Guard Helmet", [("lamellar_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_cavalry_helmet", "Mongol Cavalry Helmet", [("lamellar_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_mongol]],

	["khergit_guard_boots", "Mongol Guard Boots", [("lamellar_boots_a", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2520, abundance(100)|weight(1.0)|leg_armor(35), imodbits_cloth, [], [fac_culture_mongol]],

	["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6, abundance(100)|weight(1.0)|leg_armor(2)|body_armor(6), imodbits_cloth],

	["keys", "Ring of Keys", [("throwing_axe_a", imodbits_none)], 2|itp_primary|itp_bonus_against_shield, itc_scimitar, 240, hit_points(29696)|max_ammo(5)|spd_rtng(98)|abundance(100)|weight(5.0)|swing_damage(29, cut)|weapon_length(53), imodbits_thrown],

	["bride_dress", "Bride Dress", [("bride_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(100)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth],

	["bride_crown", "Crown of Flowers", [("bride_crown", imodbits_none)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1, abundance(100)|weight(0.5)|head_armor(4), imodbits_cloth],

	["bride_shoes", "Bride Shoes", [("bride_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 30, abundance(100)|weight(1.0)|leg_armor(8), imodbits_cloth],

	["practice_bow_2", "Practice Bow", [("hunting_bow", imodbits_none), ("hunting_bow_carry", ixmesh_carry)], 8|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, thrust_damage(21, blunt)|spd_rtng(90)|abundance(100)|weight(1.5)|shoot_speed(40), imodbits_bow],

	["practice_arrows_2", "Practice Arrows", [("arena_arrow", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, max_ammo(80)|abundance(100)|weight(1.5)|weapon_length(95), imodbits_missile],

	["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, abundance(100)|weight(22.0)|leg_armor(1)|body_armor(1), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["almogavar_sword", "Almogavar Cleaver", [("almogavar_sword", imodbits_none), ("almogavar_sword_carry", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1270, thrust_damage(15, cut)|hit_points(39936)|spd_rtng(102)|abundance(100)|weight(0.75)|swing_damage(39, cut)|difficulty(8)|weapon_length(51), imodbits_sword, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["welsh_archer", "Welsh Bowman Tunic", [("welsh_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2219, abundance(100)|weight(16.0)|leg_armor(8)|body_armor(35), imodbits_cloth, [], [fac_kingdom_9]],

	["armenian_knight_a", "Armenian Knight Mail", [("armenian_knight_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["armenian_knight_b", "Armenian Knight Mail", [("armenian_knight_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["armenian_knight_c", "Armenian Knight Mail", [("armenian_knight_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_23]],

	["archer_a", "Tunic with Hood", [("archer_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["archer_b", "Tunic ", [("archer_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["archer_c", "Tunic", [("archer_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_a", "Gambeson", [("surcoat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_b", "Gambeson", [("surcoat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_c", "Gambeson", [("surcoat_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_d", "Gambeson", [("surcoat_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_e", "Gambeson", [("surcoat_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surcoat_f", "Mail", [("surcoat_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["surcoat_g", "Cloth Over Mail", [("surcoat_g", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["teu_hbrother_a", "Halbbrudder Surcoat over Mail", [("teu_hbrother_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["teu_hbrother_b", "Halbbrudder Surcoat over Mail", [("teu_hbrother_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_23]],

	["flat_kettle_hat", "Flattop Kettle Hat", [("flat_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["seljuk_horse", "Seljuk Horse", [("seljuk_horse", imodbits_none)], itp_type_horse, 0, 3800, hit_points(120)|horse_maneuver(40)|abundance(10)|difficulty(4)|thrust_damage(38, cut)|horse_speed(38)|body_armor(45)|horse_scale(110), imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_22]],

	["seljuk_armour", "Seljuk Armour", [("seljuk_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_kingdom_22]],

	["seljuk_lamellar_a", "Seljuk Lamellar Vest", [("seljuk_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_22]],

	["seljuk_lamellar_b", "Seljuk Lamellar Vest", [("seljuk_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_kingdom_22]],

	["andalus_helmet_a", "Andalusian Helm", [("andalus_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["andalus_infantry_helmet", "Andalusian Helm", [("andalus_infantry_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["andalusian_knight", "Andalusian Surcoat over Mail", [("andalusian_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_andalus]],

	["gaelic_mail_shirt_a", "Gaelic gambeson", [("gaelic_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_1", "Targe", [("s_h1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["highlander_boots_1", "Highlander Boots", [("highlander_boots_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 384, abundance(100)|weight(1.25)|leg_armor(8), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_byrnie_a", "Gaelic Byrnie", [("gaelic_byrnie_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_byrnie_b", "Gaelic Byrnie", [("gaelic_byrnie_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["genoa_padded_a", "Padded Armour", [("genoa_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_padded_b", "Padded Armour", [("genoa_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_padded_c", "Padded Armour", [("genoa_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_mail_b", "Genoese Armour", [("genoa_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["genoa_mail_c", "Genoese Armour", [("genoa_mail_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["andalusian_shield_1", "Old Moorish Shield", [("andalusian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 117, hit_points(28)|spd_rtng(96)|abundance(100)|weight(2.0)|shield_width(36)|resistance(48)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["andalusian_shield_2", "Plain Moorish Shield", [("andalusian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 177, hit_points(36)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(36)|resistance(55)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["andalusian_shield_3", "Moorish Shield", [("andalusian_shield", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 242, hit_points(43)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|resistance(61)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["andalusian_shield_4", "Heavy Moorish Shield", [("heavy_adarga", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, hit_points(51)|spd_rtng(87)|abundance(100)|weight(3.5)|shield_width(36)|resistance(67)|shield_height(70), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_andalus]],

	["andalusian_helmet_a", "Andalusian Helmet", [("andalusian_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(100)|weight(1.75)|difficulty(7)|head_armor(70), imodbits_plate, [], [fac_culture_andalus]],

	["andalusian_helmet_b", "Iberian Helmet", [("andalusian_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(100)|weight(1.75)|difficulty(7)|head_armor(70), imodbits_plate, [], [fac_culture_andalus]],

	["noble_cloak", "Nobleman Outfit", [("noble_cloak", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["meghrebi_leather_a", "Meghrebi Padded Armour", [("meghrebi_leather_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["meghrebi_leather_b", "Meghrebi Leather Armour", [("meghrebi_leather_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["meghrebi_leather_c", "Meghrebi Kaftan with Cape", [("meghrebi_leather_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_marinid]],

	["meghrebi_vest", "Meghrebi Kaftan", [("meghrebi_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_marinid]],

	["buff_leather", "Buff Leather Armour", [("buff_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_marinid]],

	["black_guard", "Kaftan", [("black_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["black_guard_helmet", "Saracen Fluted Helmet", [("black_guard_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["gaelic_mail_shirt_b", "Gaelic Scale", [("gaelic_mail_shirt_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["surcoat_gaelic", "Gaelic Mail", [("gaelic_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_13]],

	["almohad_robe_a", "Almohad Robe", [("almohad_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_b", "Almohad Robe", [("almohad_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_c", "Almohad Robe", [("almohad_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_robe_d", "Almohad Robe", [("almohad_robe_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_a", "Almohad Padded Armour", [("almohad_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_b", "Almohad Padded Armour", [("almohad_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_padded_c", "Almohad Padded Armour", [("almohad_padded_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_cavalry_a", "Almohad Cavalry Robe", [("almohad_cavalry_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["almohad_cavalry_b", "Almohad Cavalry Robe", [("almohad_cavalry_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["andalusian_archers_vest", "Andalusian Robe", [("andalusianarchers_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["andalusian_skirmisher_armor", "Andalusian Mail", [("andalusianskirmisher_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_andalus]],

	["arabian_lamellar", "Felt Vest", [("arabian_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["horse_d", "Courser", [("horse_d", imodbits_none), ("horse_d", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(65)|horse_maneuver(46)|abundance(60)|difficulty(3)|thrust_damage(28, cut)|horse_speed(45)|body_armor(18)|horse_scale(108), imodbit_champion|imodbits_horse_basic],

	["arab_nobleman_a", "Arabian Nobleman Robe", [("arab_nobleman_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_nobleman_b", "Arabian Nobleman Robe", [("arab_nobleman_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_nobleman_c", "Arabian Nobleman Robe", [("arab_nobleman_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["andalusian_heavy_a", "Andalusian Scale Armour", [("andalusian_heavy_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus]],

	["andalusian_heavy_b", "Andalusian Scale Armour", [("andalusian_heavy_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus]],

	["berber_tunic_a", "Berber Robe", [("berber_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_tunic_b", "Scale Vest", [("berber_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_tunic_c", "Berber Robe", [("berber_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus]],

	["berber_turban", "Moorish Turban", [("berber_turban", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_andalus]],

	["iberian_leather_armour_a", "Iberian Leather Armour", [("iberian_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["iberian_leather_armour_b", "Iberian Leather Armour", [("iberian_leather_armour_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["iberian_leather_armour_c", "Iberian Leather Armour", [("iberian_leather_armour_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["andalusi_horseman_robe", "Moorish Horseman Robe", [("andalusi_horseman_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_andalus]],

	["galloglass_mail", "Gallóglach Mail Armour", [("galloglass_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus]],

	["galloglass_padded", "Gallóglach Padded Armour", [("galloglass_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["baltic_sword", "Baltic Sword", [("baltic_sword", imodbits_none), ("sword_medieval_b_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 2896, hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|weapon_length(91), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["man_at_arms_a", "Cloth over Aketon", [("man_at_arms_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["man_at_arms_b", "Rich Cloth over Mail", [("man_at_arms_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["man_at_arms_c", "Rich Cloth over Mail", [("man_at_arms_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["arab_padded_vest", "Saracen Padded Vest", [("arab_padded_vest", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_archer", "Saracen Archer Vest", [("arab_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_infantry_lamellar_a", "Mail with Lamellar Vest", [("mamluk_infantry_lamellar_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_infantry_lamellar_b", "Mail with Lamellar Vest", [("mamluk_infantry_lamellar_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["targe_2", "Targe", [("s_h1_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_3", "Targe", [("s_h1_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_4", "Targe", [("s_h2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_5", "Targe", [("s_h2_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["targe_6", "Targe", [("s_h2_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 22, hit_points(36)|spd_rtng(100)|abundance(100)|weight(2.0)|shield_width(50)|resistance(35), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["balt_lamellar_coat_a", "Fur Coat with Lamellar Vest", [("baltic_lamellar_coat_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_lamellar_coat_b", "Fur Coat with Lamellar Vest", [("baltic_lamellar_coat_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["rus_padded", "Eastern Scale Armour", [("rus_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_rus]],

	["baltic_sword_b", "Baltic Sword (Brador)", [("baltic_sword_b", imodbits_none), ("baltic_sword_b_scab", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 3622, hit_points(36864)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(36, cut)|weapon_length(94), imodbits_sword_high, [], [fac_culture_mazovian, fac_culture_baltic]],

	["mongol_helmet_a", "Mongol Helmet", [("mongol_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_mongol]],

	["mongol_helmet_b", "Mongol Helmet", [("mongol_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mongol]],

	["mongol_helmet_c", "Mongol Helmet", [("mongol_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mongol]],

	["steppe_helmet", "Eastern Helmet", [("steppe_helmet", imodbits_none), ("inv_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mongol]],

	["priest_cap_1", "Cap", [("1257_arming_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["priest_cap_2", "Cap", [("1257_arming_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["priest_robe_1", "Priest Robe", [("priest_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["priest_robe_2", "Priest Robe", [("priest_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth],

	["priest_robe_3", "Priest Robe", [("priest_2_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["surgeon", "Surgeon Outfit", [("surgeon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth],

	["bishop_great_helm", "Bishop Great Helm", [("bishop_tophelm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_kingdom_23]],

	["bishop_armour", "Bishop Armour", [("bishop", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 17821, abundance(10)|weight(36.0)|leg_armor(29)|difficulty(14)|body_armor(80), imodbits_armor, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["bishop_mitre", "Bishop mittre", [("bishop_mitre", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth],

	["bishop_staff", "Bishop Staff", [("bishop_staff", imodbits_none)], 4|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_parry_polearm, 9, thrust_damage(0, blunt)|spd_rtng(120)|abundance(100)|weight(3.5)|swing_damage(0, blunt)|weapon_length(115), imodbits_none],

	["varangian_shield_a", "Varangian Shield", [("varangian_shield_a", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["varangian_shield_b", "Varangian Shield", [("varangian_shield_b", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["varangian_shield_c", "Varangian Shield", [("varangian_shield_c", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sabre", "Byzantine Sabre", [("byzantine_sabre", imodbits_none), ("byzantine_sabre_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 3899, hit_points(39936)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(39, cut)|weapon_length(93), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword", "Byzantine Sword", [("byzantine_sword_a", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(23, pierce)|hit_points(38912)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(38, cut)|difficulty(8)|weapon_length(93), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_1", "Byzantine Sword", [("byzantine_sword_1", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(23, pierce)|hit_points(39936)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(39, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_3", "Byzantine Sword", [("byzantine_sword_3", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(23, pierce)|hit_points(38912)|spd_rtng(97)|abundance(100)|weight(1.5)|swing_damage(38, cut)|difficulty(8)|weapon_length(94), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_4", "Byzantine Sword", [("byzantine_sword_4", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(23, pierce)|hit_points(40960)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(40, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_5", "Byzantine Sword", [("byzantine_sword_5", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(23, pierce)|hit_points(38912)|spd_rtng(97)|abundance(100)|weight(1.5)|swing_damage(38, cut)|difficulty(8)|weapon_length(94), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_7", "Byzantine Sword", [("byzantine_sword_7", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(24, pierce)|hit_points(39936)|spd_rtng(97)|abundance(100)|weight(1.5)|swing_damage(39, cut)|difficulty(8)|weapon_length(95), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["byzantine_sword_extra", "Byzantine Sword", [("byzantine_sword_extra", imodbits_none), ("byzantine_sword_a_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3702, thrust_damage(25, pierce)|hit_points(38912)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(38, cut)|difficulty(8)|weapon_length(93), imodbits_sword_high, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_shield_a_3", "Almond Shield", [("rus_shield_a", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["rus_shield_b_3", "Almond Shield", [("rus_shield_b", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["rus_shield_c_3", "Almond Shield", [("rus_shield_c", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["rus_shield_d_3", "Almond Shield", [("rus_shield_d", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 50, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(61)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_rus]],

	["cuman_noble_helmet", "Cuman Noble Helmet", [("cuman_noble", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["ghulam_helmet", "Ghulam Helmet", [("ghulam_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["ilkhanate_mongol_helmet", "Mongol Helmet", [("ilkhanate_mongol_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mongol]],

	["polski_helm", "Polish Helmet", [("polska_helma", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_kingdom_5]],

	["mamluke_helm_b", "Mighfar", [("mamluke_helm_b", imodbits_none), ("inv_mamluke_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mongol_helmet_d", "Mongol Leather Helmet", [("mongol_leather_helm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mongol]],

	["nikloskoe_helmet_warrior", "Nikloskoe Helmet", [("nikloskoe_helmet_warrior", imodbits_none), ("inv_nikloskoe_helmet_warrior", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["kiev_helmet_2_facemail", "Rus Helmet", [("kiev_helmet_2_facemail", imodbits_none), ("inv_kiev_helmet_2_facemail", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["kiev_helmet_1_facemail_1", "Rus Helmet", [("kiev_helmet_1_facemail_1", imodbits_none), ("inv_kiev_helmet_1_facemail_1", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["rus_byzantinenoble_kettle", "Byzantine Kettle Helm", [("rus_byzantinenoble_kettle", imodbits_none), ("inv_byzantinenoble_kettle", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_helmet_a", "Eastern Helmet", [("rus_helmet_a", imodbits_none), ("inv_rus_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_rus]],

	["rus_infantry_helmet", "Eastern Infantry Helmet", [("rus_infantry_helmet", imodbits_none), ("inv_rus_infantry_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_rus]],

	["rus_militia_helmet", "Eastern Militia Helmet", [("rus_militia_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_rus]],

	["rus_noble_helmet", "Yesenovo Helmet", [("rus_noble_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_rus]],

	["seljuk_archer_cap", "Seljuk Cap", [("seljuk_archer_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["ilkhanate_cap", "Ilkanate Hat", [("ilkhanate_cap", imodbits_none), ("inv_ilkhanate_cap", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["cuman_cap_d", "Cuman Hat Coif", [("cuman_cap_d", imodbits_none), ("inv_cuman_cap_d", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_armor, [], [fac_kingdom_7]],

	["anatolian_horseman_lamellar", "Anatolian Lamellar Armor", [("anatolian_horseman_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["anatolian_leather_lamellar", "Anatolian Leather Lamellar Armor", [("anatolian_leather_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["anatolian_mail", "Anatolian Mail Shirt", [("anatolian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["arab_headcloth", "Headcloth", [("arab_headcloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth],

	["seljuk_tunic", "Seljuk Tunic With Mail", [("seljuk_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["seljuk_tunic_b", "Seljuk Tunic With Mail", [("seljuk_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["seljuk_tunic_c", "Seljuk Tunic With Mail", [("seljuk_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["rus_noble_mail", "Rus Nobleman Mail", [("rus_noble_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus]],

	["rus_mask_helmet", "Rus Mask Helmet", [("mask_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["mamluk_lamellar", "Mamluk Lamellar Armour", [("mamluk_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["rus_leather_scale", "Rus Scale Armour", [("rus_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_rus]],

	["rus_leather_scale_b", "Rus Leather Scale Armour", [("rus_scale_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_rus]],

	["rohatyna", "Rohatyna", [("bear_spear", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_cutting_spear, 146, thrust_damage(39, pierce)|hit_points(32768)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(32, cut)|difficulty(8)|weapon_length(155), imodbits_polearm],

	["flat_topped_helmet_a", "Spangen Helmet", [("flattop_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["flat_topped_helmet_b", "Spangen Helmet", [("flattop_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["great_helmet_a", "Great Helm", [("greathelmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_b", "Great Helm", [("greathelmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_c", "Great Helm", [("greathelmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_d", "Creveille", [("greathelmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["great_helmet_decorative", "Phrigian Helm", [("greathelmet_decorative", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["bill", "Bill", [("bill", imodbits_none)], 4|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_staff, 200, hit_points(44032)|spd_rtng(84)|abundance(100)|weight(2.25)|swing_damage(43, cut)|difficulty(8)|weapon_length(128), imodbits_polearm, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["almogavar_helmet", "Almoghavar Helmet", [("almogavar_helmet", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["curonian_helmet", "Curonian Helmet", [("curonian_helmet", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["balt_padded_a", "Balt Padded Armour", [("balt_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_kingdom_2]],

	["balt_padded_b", "Balt Leather Vest", [("balt_padded_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_2]],

	["thomas_padded_armour", "Tomgirtas, the famous drunk warrior padded armor", [("thomas_padded_armour", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_kingdom_2]],

	["militia_tunic_a", "Militia Tunic", [("militia_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["militia_tunic_b", "Militia Tunic", [("militia_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rus_militia_padded_a", "Rus Padded Armour", [("rus_militia_padded_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_rus]],

	["little_samogitian", "Žemaitukas", [("horse_d", imodbits_none), ("horse_d", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 512, hit_points(65)|horse_maneuver(49)|abundance(60)|difficulty(3)|thrust_damage(10, cut)|horse_speed(45)|body_armor(17)|horse_scale(95), imodbit_champion|imodbits_horse_basic, [], [fac_culture_mazovian, fac_culture_baltic]],

	["kettlehat_a", "Kettle Helm", [("kettlehat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["kettlehat_b", "Kettle Helm", [("kettlehat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["kettlehat_c", "Kettle Helm", [("kettlehat_cheek", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["andalus_marinid_hasfid_elite_a", "Moorish Robe over Mail", [("andalus_marinid_hasfid_elite_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_marinid]],

	["andalus_marinid_hasfid_elite_b", "Moorish Robe over Mail", [("andalus_marinid_hasfid_elite_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_marinid]],

	["berber_kaftan", "Moorish Kaftan", [("berber_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["berber_mail_a", "Moorish Robe over Mail", [("berber_mail_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_marinid]],

	["berber_mail_b", "Moorish Robe over Mail", [("berber_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_marinid]],

	["seljuk_hauberk_jawshan", "Seljuk Jawshan", [("seljuk_hauberk_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_jawshan_leather", "Leather Jawshan", [("mamluk_jawshan_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["horse_e", "Courser", [("horse_e", imodbits_none), ("horse_e", imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 810, hit_points(65)|horse_maneuver(46)|abundance(60)|difficulty(3)|thrust_damage(28, cut)|horse_speed(45)|body_armor(18)|horse_scale(108), imodbit_champion|imodbits_horse_basic],

	["gaelic_shirt_blue", "Gaelic Shirt", [("gaelic_shirt_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["gaelic_shirt_green", "Gaelic Shirt", [("gaelic_shirt_green_muted", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["gaelic_shirt_red", "Gaelic Shirt", [("gaelic_shirt_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth],

	["andalusian_helmet_c", "Andalusian Helmet", [("andalusian_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus]],

	["andalusian_helmet_d", "Andalusian Helmet", [("andalusian_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["arab_helmet_d", "Saracen Helmet", [("arab_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["mamluk_helm_b", "Tawashi Helmet", [("mamluk_helmet_4", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["iberian_cleaver", "Iberian Cleaver", [("iberian_cleaver", imodbits_none)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 1005, thrust_damage(0, pierce)|hit_points(35840)|spd_rtng(93)|abundance(100)|weight(1.75)|swing_damage(35, cut)|weapon_length(77), imodbits_sword_high, [], [fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian]],

	["moorish_hat", "Moorish Hat", [("moorish_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth],

	["alsacian_sword", "Alsatian Sword (Al Mansur)", [("alsacian_sword", imodbits_none), ("alsacian_sword_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 2832, thrust_damage(20, pierce)|hit_points(34816)|spd_rtng(99)|abundance(100)|weight(1.5)|swing_damage(34, cut)|difficulty(8)|weapon_length(90), imodbits_sword_high, [], [fac_kingdom_10]],

	["moorish_axe", "Moorish Axe", [("moorish_axe", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 843, hit_points(34816)|spd_rtng(94)|abundance(25)|weight(1.75)|swing_damage(34, pierce)|difficulty(9)|weapon_length(74), imodbits_pick],

	["kettle_cloth", "Kettle Helm", [("kettle_cloth", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["1257_hood", "Hood", [("1257_hood", imodbits_none), ("inv_1257_hood", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rus_helmet", "Rus Helmet", [("rus_helmet", imodbits_none), ("inv_rus_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["rus_helmet_1", "Rus Helmet", [("rus_helmet1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["rus_helmet_2", "Rus Helmet", [("rus_helmet2", imodbits_none), ("inv_rus_helmet2", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["rus_helmet_3", "Rus Helmet", [("rus_helmet3", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_rus]],

	["balt_rus_cap", "Leather Cap", [("balt_rus_hat", imodbits_none), ("inv_balt_rus_hat", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

	["moors_quilted_kaftan_blue", "Moorish Padded Kaftan", [("moors_quilted_kaftan_blue", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_marinid]],

	["moors_quilted_kaftan_brown", "Moorish Padded Kaftan", [("moors_quilted_kaftan_brown", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_marinid]],

	["czekan", "Czekan", [("czekan", imodbits_none)], 2|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_mace_left_hip|itc_scimitar, 954, hit_points(35840)|spd_rtng(93)|abundance(25)|weight(1.75)|swing_damage(35, pierce)|difficulty(9)|weapon_length(75), imodbits_pick, [], [fac_kingdom_5, fac_kingdom_8, fac_kingdom_15]],

	["ilkhanate_kaftan", "Mongol Kaftan", [("mongol_ilkhanate_kaftan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_mongol]],

	["turk_kaftan_beige", "Turkic Kaftan", [("turk_kaftan_beige", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15]],

	["turk_kaftan_furtrim", "Turkic Kaftan", [("turk_kaftan_furtrim", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15]],

	["turk_kaftan_green", "Turkic Lamellar Armour", [("turk_kaftan_green", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_cloth, [], [fac_kingdom_22, fac_kingdom_7, fac_kingdom_29, fac_kingdom_30, fac_kingdom_15]],

	["saracen_mail", "Saracen Mail", [("kau_arabian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["jineta_sword", "Jineta Sword", [("jineta_sword", imodbits_none), ("jineta_sword_scabbard", ixmesh_carry)], 2|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 3740, thrust_damage(23, pierce)|hit_points(37888)|spd_rtng(98)|abundance(100)|weight(1.5)|swing_damage(37, cut)|difficulty(8)|weapon_length(96), imodbits_sword_high, [], [fac_culture_iberian]],

	["gaelic_helmet_a", "Gaelic Helmet", [("gaelic_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth, [], [fac_kingdom_13]],

	["priest_cap_2", "Cap", [("priest_cap_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth|imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["byz_helmet_b", "Byzantine Helmet", [("byz_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["pilgrim_hat", "Hat", [("pilgrim_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["gaelic_long_tunic_a", "Tunic", [("gaelic_long_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_long_tunic_b", "Tunic", [("gaelic_long_tunic_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_long_tunic_c", "Tunic", [("gaelic_long_tunic_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 192, abundance(50)|weight(6.0)|leg_armor(5)|difficulty(1)|body_armor(12), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_a", "Gaelic Infantry Shield", [("gaelic_shield_a", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 166, hit_points(55)|spd_rtng(81)|abundance(100)|weight(4.5)|shield_width(50)|resistance(69), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_b", "Gaelic Shield", [("gaelic_shield_b", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["gaelic_shield_c", "Gaelic Shield", [("gaelic_shield_c", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 67, hit_points(37)|spd_rtng(100)|abundance(100)|weight(2.5)|shield_width(30)|resistance(67)|shield_height(50), imodbits_shield, 
#####Begin add effect to shields with culture
#####For fac_kingdom 
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 6), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 6), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["rhodok_great_helmet", "Great Helm", [("rhodok_great_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rhodok_four_plated_helmet", "Norman Helm", [("rhodok_four_plated_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rhodok_kettle_hat_c", "Kettle Hat", [("rhodok_kettle_hat_c", imodbits_none), ("inv_rhodok_kettle_hat_c", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["rhodok_nasal_helmet_a", "Norman Helm", [("rhodok_nasal_helmet_a", imodbits_none), ("inv_rhodok_nasal_helmet_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["saint_thomas_knight", "Order Mantle", [("saint_thomas_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["lazarus_serjeant_tunic", "Order Mantle", [("lazarus_serjeant_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["calatrava_knight", "Order Mantle", [("calatrava_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["santiago_knight", "Order Mantle", [("santiago_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_kingdom_23]],

	["studden_leather_armour_a", "Padded Leather Armour", [("studden_leather_armour_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["faris_helmet", "Saracen Helm", [("faris_helmet", imodbits_none)], itp_type_head_armor, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["arab_mail_e", "Saracen Lamellar Armour", [("arab_mail_e", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["georgian_mail", "Armenian Mail Shirt", [("georgian_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["seljuk_scale_a", "Saracen Lamellar Armour", [("seljuk_scale_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["balt_shirt_c", "Fur Vest", [("balt_shirt_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_baltic]],

	["armenian_mail_b", "Armenian Mail Shirt", [("armenian_mail_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4037, abundance(80)|weight(21.0)|leg_armor(17)|difficulty(9)|body_armor(41), imodbits_armor, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["kau_turcopole_a", "Padded Armour", [("kau_turcopole_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["kau_turcopole_b", "Padded Armour", [("kau_turcopole_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["mamluk_cap", "Seljuk Cap", [("mamluk_cap", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["1257_hood", "Hood", [("1257_hood", imodbits_none), ("inv_1257_hood", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western, fac_culture_iberian, fac_culture_italian, fac_culture_anatolian_christian, fac_culture_finnish, fac_culture_nordic]],

	["berber_turban_cape", "Berber Turban", [("berber_turban_cape", imodbits_none), ("inv_berber_turban_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_andalus]],

	["bulgar_warrior_a", "Scale Armour", [("bulgar_warrior_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_rus, fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["bulgar_warrior_b", " Leather Armour", [("bulgar_warrior_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_cloth, [], [fac_culture_rus]],

	["bulgar_helm", "Bulgar Helm", [("bulgar_helm", imodbits_none), ("inv_bulgar_helm", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_cloth, [], [fac_culture_rus]],

	["bulgar_helm_b", "Bulgar Helm", [("bulgar_helm_b", imodbits_none), ("inv_bulgar_helm_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_cloth, [], [fac_culture_rus]],

	["berber_robe_a", "Berber Bobe", [("berber_robe_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["berber_robe_b", "Berber Bobe", [("berber_robe_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["berber_robe_c", "Berber Bobe", [("berber_robe_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_marinid]],

	["saracen_kaftan_a", "Kaftan", [("saracen_kaftan_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["saracen_kaftan_b", "Kaftan", [("saracen_kaftan_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["saracen_kaftan_c", "Kaftan", [("saracen_kaftan_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["saracen_kaftan_d", "Kaftan", [("saracen_kaftan_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["rus_hat_with_padding", "Rus Hat", [("rus_hat_with_padding", imodbits_none), ("inv_rus_hat_with_padding", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_rus]],

	["mongol_fur_hat", "Mongol Tribal Hat", [("mongol_fur_hat", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_mongol]],

	["mongol_tunic_a", "Mongol Lamellar Armour", [("mongol_warrior_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7561, abundance(60)|weight(26.0)|leg_armor(20)|difficulty(10)|body_armor(51), imodbits_armor, [], [fac_culture_mongol]],

	["gaelic_tunic_cape_a", "Gaelic Tunic", [("gaelic_tunic_cape_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 320, abundance(50)|weight(11.0)|leg_armor(10)|difficulty(3)|body_armor(21), imodbits_cloth, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["kettle_cloth_cape_b", "Kettle Hat", [("kettle_cloth_cape_b", imodbits_none), ("inv_kettle_cloth_cape_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["kettle_cloth_cape", "Kettle Hat", [("kettle_cloth_cape", imodbits_none), ("inv_kettle_cloth_cape", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["wenceslav_helmet", "Saint Wenceslav Helmet", [("wenceslav_helmet", imodbits_none), ("inv_wenceslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["baltic_ponted_helmet", "Balt Helmet", [("baltic_ponted_helmet", imodbits_none), ("inv_baltic_ponted_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_mazovian, fac_culture_baltic]],

	["berber_white_turban", "Turban Helm", [("berber_white_turban", imodbits_none), ("inv_berber_white_turban", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["surcoat_france_b", "Surcoat With Golden Mail", [("surcoat_france_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_kingdom_10]],

	["byzantine_crown", "Crown", [("byzantine_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbits_plate, [], [fac_culture_rus]],

	["rus_coat", "Rus Coat", [("rus_coat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 481, abundance(100)|weight(14.0)|leg_armor(12)|difficulty(5)|body_armor(26), imodbits_armor, [], [fac_culture_rus]],

	["moor_helmet_a", "Andalusian Helmet", [("moor_helmet_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["moor_helmet_b", "Andalusian Helmet", [("moor_helmet_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["moor_helmet_c", "Andalusian Helmet", [("moor_helmet_c", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["moor_helmet_d", "Andalusian Helmet", [("moor_helmet_d", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["berber_helmet_g", "Berber Helm", [("berber_helmet_g", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["andalusian_helmet_e", "Andalusian Helmet", [("andalusian_helmet_e", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_andalus]],

	["megreb_spangen", "Plain Helm", [("megreb_spangen", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_andalus]],

	["mamluke_helm_ventail", "Mamluke Helmet", [("mamluke_helm_ventail", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_mamluke, fac_culture_anatolian]],

	["mongol_kettle", "Mongol Kettle Hat", [("mongol_kettle", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_mongol]],

	["kipchak_steppe_helmet", "Kiphak steppe helmet", [("kipchak_steppe_helmet", imodbits_none), ("inv_kipchak_steppe_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbits_plate, [], [fac_culture_mongol]],

	["mongol_warrior_de", "Mongol Lamellar Armour", [("mongol_warrior_de", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 883, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(8)|body_armor(33), imodbits_armor, [], [fac_culture_mongol]],

	["yaroslav_helmet", "Rus Noble Helmet", [("yaroslav_helmet", imodbits_none), ("inv_yaroslav_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["polovtsian_helmet", "Volga Bulgar Noble Helmet", [("polovtsian_helmet", imodbits_none), ("inv_polovtsian_helmet", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_rus]],

	["byz_helmet_golden", "Byzantine Helmet", [("byz_helmet_golden", imodbits_none), ("inv_byz_helmet_golden", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 3600, abundance(80)|weight(2.0)|head_armor(60), imodbits_plate, [], [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]],

	["nordic_fur_cap", "Nordic Hat", [("nordic_fur_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_cloth, [], [fac_culture_rus]],

	["gaelic_crown", "Crown", [("gaelic_crown", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 300, abundance(30)|weight(0.5)|head_armor(4), imodbits_plate, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["helmet_with_feathers", "Winged Great Helmet", [("helmet_with_feathers", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 8100, abundance(30)|weight(3.0)|head_armor(90), imodbits_plate, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot2", "Great Helm", [("frenchpepperpot2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot3", "Great Helm", [("frenchpepperpot3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["munitionshelm2", "Great Helm", [("munitionshelm2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["pepperpothelm1", "Great Helm", [("pepperpothelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["munitionshelm1", "Great Helm", [("munitionshelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["frenchpepperpot", "Great Helm", [("frenchpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 4900, abundance(60)|weight(2.5)|head_armor(70), imodbit_rusty|imodbit_crude|imodbits_shield, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["strely", "Strely", [("strely", imodbits_none), ("flying_arrow", ixmesh_flying_ammo), ("rus_strely_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical, 124, thrust_damage(31, cut)|max_ammo(60)|abundance(70)|weight(3.0)|weapon_length(95), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["new_turban_a", "Turban", [("new_turban_a", imodbits_none), ("inv_new_turban_a", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["new_turban_b", "Turban", [("new_turban_b", imodbits_none), ("inv_new_turban_b", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 43, abundance(60)|weight(0.5)|head_armor(8), imodbits_plate, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],

	["kufia_berber_black", "Berber Helm", [("kufia_berber_black", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 2500, abundance(80)|weight(1.75)|head_armor(50), imodbits_plate, [], [fac_culture_andalus]],

	["african_spangen", "Spangen Helm", [("african_spangen", imodbits_none)], itp_type_head_armor|itp_covers_head|itp_couchable, 0, 1600, abundance(100)|weight(1.5)|head_armor(40), imodbits_plate, [], [fac_culture_marinid]],

	["african_turban", "African Turban", [("african_turban", imodbits_none)], itp_type_head_armor|itp_covers_head|itp_couchable, 0, 267, abundance(80)|weight(1.0)|head_armor(20), imodbits_cloth, [], [fac_culture_marinid]],

	["head_african", "African Head", [("head_african", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head|itp_couchable, 0, 6, abundance(100)|weight(0.5), imodbits_cloth, [], [fac_culture_marinid]],

	["african_hat", "African Hat", [("african_hat", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head|itp_couchable, 0, 3, abundance(30)|weight(0.5)|head_armor(4), imodbits_cloth, [], [fac_culture_marinid]],

	["legs_african", "African Boots", [("legs_african", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid]],

	["hands_african", "Hands African", [("hands_african_L", imodbits_none)], itp_type_hand_armor, 0, 40, abundance(120)|weight(0.25), imodbits_cloth, [], [fac_culture_marinid]],

	["african_trousers", "Trousers", [("african_trousers", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 96, abundance(100)|weight(1.0)|leg_armor(2), imodbits_cloth, [], [fac_culture_marinid]],

	["irish_surcoat", "Surcoat over Mail", [("irish_surcoat", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11616, abundance(40)|weight(31.0)|leg_armor(24)|difficulty(12)|body_armor(64), imodbits_armor, [], [fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]],

	["crown_european", "Crown", [("crown_european", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(100)|weight(1.0)|head_armor(10), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["crown", "Crown", [("crown", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(100)|weight(1.0)|head_armor(10), imodbits_cloth, [], [fac_culture_mazovian, fac_culture_teutonic, fac_culture_western]],

	["seljuk_hair", "Seljuk Hairstyle", [("seljuk_hair", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 3, abundance(100)|weight(1.0)|head_armor(2), imodbits_cloth, [], [fac_culture_andalus, fac_culture_mamluke, fac_culture_anatolian]],
#
#
#
#itcf_overswing_polearm                               = 0x0000000000000200
#itcf_slashright_polearm                              = 0x0000000000000400
#itcf_slashleft_polearm                               = 0x0000000000000800
#
	["flag_pole_1", "Flag", [("flag_pole_1", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_slashleft_polearm|itcf_slashright_polearm|itcf_overswing_polearm|itc_parry_polearm, 1500, thrust_damage(0, blunt)|spd_rtng(85)|abundance(1)|weight(16.5)|swing_damage(32, blunt)|weapon_length(155), imodbits_none, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_flag_pole", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["flag_pole_2", "Flag", [("flag_pole_2", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_slashleft_polearm|itcf_slashright_polearm|itcf_overswing_polearm|itc_parry_polearm, 1500, thrust_damage(0, blunt)|spd_rtng(85)|abundance(1)|weight(16.5)|swing_damage(32, blunt)|weapon_length(155), imodbits_none,
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_flag_pole", ":trigger_param_1", ":trigger_param_2")
		])]
	],
	
	["flag_pole_3", "Flag", [("flag_pole_3", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_slashleft_polearm|itcf_slashright_polearm|itcf_overswing_polearm|itc_parry_polearm, 1500, thrust_damage(0, blunt)|spd_rtng(85)|abundance(1)|weight(16.5)|swing_damage(32, blunt)|weapon_length(155), imodbits_none, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner_old", "tableau_flag_pole", ":trigger_param_1", ":trigger_param_2")
		])]
	],

	["cross", "Cross", [("true_cross", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, thrust_damage(0, blunt)|spd_rtng(60)|abundance(100)|weight(16.5)|swing_damage(0, blunt)|weapon_length(155), imodbits_none],

		
	
["lance_banner_jer", "Jerusalem Lance", [("spear_baner_jerusalem_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_jer1", "Jerusalem Lance", [("spear_baner_jerusalem_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_jer2", "Jerusalem Lance", [("spear_baner_jerusalem_e",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_jer3", "Jerusalem Lance", [("spear_baner_jerusalem_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_ibe", "Jerusalem Lance", [("spear_baner_ibelin_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ibe1", "Jerusalem Lance", [("spear_baner_ibelin_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ibe2", "Jerusalem Lance", [("spear_baner_ibelin_g",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ibe3", "Jerusalem Lance", [("spear_baner_ibelin_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_ant", "Antioch Lance", [("spear_baner_antiohia_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ant1", "Antioch Lance", [("spear_baner_antiohia_d",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ant2", "Antioch Lance", [("spear_baner_antiohia_f",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_ant3", "Antioch Lance", [("spear_baner_antiohia_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_tri", "Antioch Lance", [("spear_baner_tripol_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tri1", "Antioch Lance", [("spear_baner_tripol_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tri2", "Antioch Lance", [("spear_baner_tripol_f",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tri3", "Antioch Lance", [("spear_baner_tripol_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_tem", "Templar Lance", [("spear_baner_templar_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem1", "Templar Lance", [("spear_baner_templar_e",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem2", "Templar Lance", [("spear_baner_templar_h",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem3", "Templar Lance", [("spear_baner_templar_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_tem4", "Templar Lance", [("spear_baner_templar_g",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem5", "Templar Lance", [("spear_baner_templar_k",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem6", "Templar Lance", [("spear_baner_templar_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_tem7", "Templar Lance", [("spear_baner_templar_d",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_hos", "Hospitaller Lance", [("spear_baner_hospillers_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_hos1", "Hospitaller Lance", [("spear_baner_hospillers_d",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_hos2", "Hospitaller Lance", [("spear_baner_hospillers_f",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_hos3", "Hospitaller Lance", [("spear_baner_hospillers_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_hos4", "Hospitaller Lance", [("spear_baner_hospillers_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["lance_banner_hos5", "Hospitaller Lance", [("spear_baner_hospillers_e",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["lance_banner_teu", "Teutonic Lance", [("spear_baner_tevton_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],
["lance_banner_teu1", "Teutonic Lance", [("spear_baner_tevton_e",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],
["lance_banner_teu2", "Teutonic Lance", [("spear_baner_tevton_f",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],
["lance_banner_teu3", "Teutonic Lance", [("spear_baner_tevton_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],

["lance_banner_teu4", "Teutonic Lance", [("spear_baner_tevton_d",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],
["lance_banner_teu5", "Teutonic Lance", [("spear_baner_tevton_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],

["lance_banner_sar", "Eastern Lance", [("spear_baner_saracin_b",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["lance_banner_sar1", "Eastern Lance", [("spear_baner_saracin_a",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],

["lance_banner_sar2", "Eastern Lance", [("spear_baner_saracin_d",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["lance_banner_sar3", "Eastern Lance", [("spear_baner_saracin_c",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],

["lance_banner_sar4", "Eastern Lance", [("spear_baner_saracin_e",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["lance_banner_sar5", "Eastern Lance", [("spear_baner_saracin_f",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["lance_banner_sar6", "Eastern Lance", [("spear_baner_saracin_g",0)], itp_couchable|4|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 360 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(10240)|spd_rtng(75) | weapon_length(190)|swing_damage(10 , cut) | thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
	#hit_points(22528)|spd_rtng
	
["pike_banner_teu", "Teutonic Spear", [("spear_baner_tevton_d",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],

["pike_banner_jer", "Jerusalem Spear", [("spear_baner_jerusalem_a",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],
["pike_banner_jer1", "Jerusalem Spear", [("spear_baner_ibelin_b",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],

["pike_banner_ant", "Antioch Spear", [("spear_baner_antiohia_c",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],
["pike_banner_ant1", "Antioch Spear", [("spear_baner_tripol_b",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],

["pike_banner_tem", "Templar Spear", [("spear_baner_templar_c",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],
["pike_banner_tem1", "Templar Spear", [("spear_baner_templar_d",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],

["pike_banner_hos", "Hospitaller Spear", [("spear_baner_hospillers_a",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],
["pike_banner_hos1", "Hospitaller Spear", [("spear_baner_hospillers_c",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_papacy, fac_kingdom_23] ],

["pike_banner_teu1", "Teutonic Spear", [("spear_baner_tevton_c",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_teutonic] ],


["pike_banner_sar", "Eastern Spear", [("spear_baner_saracin_b",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["pike_banner_sar1", "Eastern Spear", [("spear_baner_saracin_a",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["pike_banner_sar2", "Eastern Spear", [("spear_baner_saracin_d",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],
["pike_banner_sar3", "Eastern Spear", [("spear_baner_saracin_c",0)], 4|itp_merchandise|itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear|itc_parry_polearm, 145 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(22528)|spd_rtng(90)|weapon_length(245)|swing_damage(95 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_mamluke] ],

#hit_points(17408)|spd_rtng
["cross_jer", "Jerusalem Staff", [("flag_jerusalem_a",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["battlefield_cross", "Christ Staff", [("battlefield_cross",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["cross_jer1", "Jerusalem Staff", [("flag_ibelin_b",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["cross_ant", "Antioch Staff", [("flag_antiohia_c",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["cross_ant1", "Antioch Staff", [("flag_tripol_b",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["cross_tem", "Templar Staff", [("flag_templar_c",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["cross_tem1", "Templar Staff", [("flag_templar_d",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["cross_hos", "Hospitaller Staff", [("flag_hospillers_a",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],
["cross_hos1", "Hospitaller Staff", [("flag_hospillers_c",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_kingdom_23, fac_papacy] ],

["cross_teu", "Teutonic Staff", [("flag_tevton_d",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_teutonic] ],
["cross_teu1", "Teutonic Staff", [("flag_tevton_c",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(10)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_teutonic] ],

["battlefield_crescent", "Staff", [("battlefield_crescent",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_mamluke] ],

["crescent_sar", "Eastern Staff", [("flag_saracin_b",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_mamluke] ],
["crescent_sar1", "Eastern Staff", [("flag_saracin_a",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_mamluke] ],
["crescent_sar2", "Eastern Staff", [("flag_saracin_d",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_mamluke] ],
["crescent_sar3", "Eastern Staff", [("flag_saracin_c",0)], 4|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff, 202 , abundance(3)|weight(2.75)|difficulty(10)|hit_points(17408)|spd_rtng(81) | weapon_length(245)|swing_damage(26 , blunt) | thrust_damage(33 ,  blunt),imodbits_polearm, [], [fac_culture_mamluke] ],

	
	
	#####Add weapons above this line
	["cross_end", "Cross_end", [("true_cross", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_parry_polearm, 40000, thrust_damage(0, blunt)|spd_rtng(60)|abundance(100)|weight(16.5)|swing_damage(0, blunt)|weapon_length(155), imodbits_none],
	#####Start adding armors below this line
			##### 5 new heraldic armors, 1 after advancement of technology, 4 initially available
	
	#####STRONGER VARIANT, MAYBE FOR INFANTRY/CAV
		["heraldic_mail_with_surcoat_tab_a", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4411, abundance(8)|weight(22.0)|leg_armor(28)|difficulty(12)|body_armor(63), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	],
	
	#####WEAKER VARIANT, INF/CAV
		["heraldic_mail_with_surcoat_tab_d", "Heraldic Mail with Surcoat", [("heraldic_armor_new_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2911, abundance(10)|weight(19.0)|leg_armor(23)|difficulty(11)|body_armor(51), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	],
	
	
	
		#####STRONGER VARIANT, ARCHERS.
		["heraldic_mail_with_surcoat_tab_b", "Heraldic Mail with Surcoat", [("heraldic_armor_new_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2443, abundance(8)|weight(15.0)|leg_armor(15)|difficulty(10)|body_armor(43), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	],
	
	######WEAKER VARIANT, ARCHERS
		["heraldic_mail_with_surcoat_tab_c", "Heraldic Mail with Surcoat", [("heraldic_armor_new_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1673, abundance(10)|weight(13.0)|leg_armor(11)|difficulty(8)|body_armor(32), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			#(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	],
	#tableau_heater_shield_1 <Dosen't randomize
	
	#####Higher era
#		["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, abundance(100)|weight(22.0)|leg_armor(1)|body_armor(1), imodbits_armor, 
#	[(ti_on_init_item,
#		[
#			(store_trigger_param_1, ":trigger_param_1"),
#			(store_trigger_param_2, ":trigger_param_2"),
#			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
#		])]
#	],
	#####Higher era end

	["items_end", "Items End", [("shield_round_a", imodbits_none)], 0, 0, 1, abundance(100), imodbits_none],
["invisiblegloves","Invisiblegloves", [("invisiblegloves",0)], itp_type_hand_armor,0, 550, weight(0)|abundance(5)|body_armor(0)|difficulty(0),imodbits_armor],
["invisible_head", "Headless", [("invalid_item",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["cut_off_head_male", "Bloody Male Head", [("cut_off_head_male",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["cut_off_head_female", "Bloody Female Head", [("cut_off_head_female",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],


]