from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

#####Kaos safe begin
from module_game_menus import *
#####Kaos asfe end
####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################



simple_triggers = [
	(ti_on_party_encounter,
		[]),

	(ti_simulate_battle,
		[]),

	(1.0,
		[
			(gt, "$auto_besiege_town", 0),
			(gt, "$g_player_besiege_town", 0),
			(ge, "$g_siege_method", 1),
			(store_current_hours, ":current_hours"),
			(eq, "$g_siege_force_wait", 0),
			(ge, ":current_hours", "$g_siege_method_finish_hours"),
			(neg|is_currently_night),
			(rest_for_hours, 0, 0, 0)
		]),

	(0.0,
		[
			(try_begin),
				(eq, "$bug_fix_version", 0),
				(disable_party, "p_test_scene"),
				(faction_set_note_available, "fac_player_faction", 0),
				(faction_set_note_available, "fac_no_faction", 0),
				(try_begin),
					(neg|check_quest_active, "qst_kidnapped_girl"),
					(party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
				(try_end),
				(try_for_range, ":troop", "trp_knight_1_1", "trp_knight_1_1_wife"),
					(try_begin),
						(troop_slot_eq, ":troop", slot_troop_occupation, 0),
						(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
						(is_between, ":faction_of_troop_troop", "fac_kingdom_1", "fac_kingdoms_end"),
						(troop_set_slot, ":troop", slot_troop_occupation, 2),
					(try_end),
				(try_end),
				(call_script, "script_initialize_item_info"),
				(assign, "$bug_fix_version", 1),
			(try_end),
			(eq, "$g_player_is_captive", 1),
			(gt, "$capturer_party", 0),
			(party_is_active, "$capturer_party"),
			(party_relocate_near_party, "p_main_party", "$capturer_party", 0)
		]),

	(0.0,
		[
			(try_begin),
				(gt, "$g_last_rest_center", 0),
				(party_get_battle_opponent, ":battle_opponent_l_g_last_rest_center", "$g_last_rest_center"),
				(gt, ":battle_opponent_l_g_last_rest_center", 0),
				(store_faction_of_party, ":faction_of_party_g_last_rest_center", "$g_last_rest_center"),
				(store_relation, ":relation_faction_of_party_g_last_rest_center_player_supporters_faction", ":faction_of_party_g_last_rest_center", "fac_player_supporters_faction"),
				(store_faction_of_party, ":faction_of_party_battle_opponent_l_g_last_rest_center", ":battle_opponent_l_g_last_rest_center"),
				(store_relation, ":relation_faction_of_party_battle_opponent_l_g_last_rest_center_player_supporters_faction", ":faction_of_party_battle_opponent_l_g_last_rest_center", "fac_player_supporters_faction"),
				(ge, ":relation_faction_of_party_g_last_rest_center_player_supporters_faction", 0),
				(lt, ":relation_faction_of_party_battle_opponent_l_g_last_rest_center_player_supporters_faction", 0),
				(start_encounter, "$g_last_rest_center"),
				(rest_for_hours, 0, 0, 0),
			(else_try),
				(store_current_hours, ":current_hours"),
				(assign, ":value", 0),
				(try_begin),
					(neq, "$g_check_autos_at_hour", 0),
					(ge, ":current_hours", "$g_check_autos_at_hour"),
					(assign, ":value", 1),
					(assign, "$g_check_autos_at_hour", 0),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(map_free),
				(try_begin),
					(ge, "$auto_menu", 1),
					(jump_to_menu, "$auto_menu"),
					(assign, "$auto_menu", -1),
				(else_try),
					(ge, "$auto_enter_town", 1),
					(start_encounter, "$auto_enter_town"),
				(else_try),
					(ge, "$auto_besiege_town", 1),
					(start_encounter, "$auto_besiege_town"),
				(else_try),
					(ge, "$g_camp_mode", 1),
					(assign, "$g_camp_mode", 0),
					(assign, "$g_infinite_camping", 0),
					(assign, "$g_player_icon_state", 0),
					(rest_for_hours, 0, 0, 0),
					(display_message, "@Breaking camp..."),
				(try_end),
			(try_end)
		]),

	(0.0,
		[
			(troop_slot_ge, "trp_notification_menu_types", 0, 1),
			(troop_get_slot, ":notification_menu_types_relations_begin", "trp_notification_menu_types", slot_troop_relations_begin),
			(troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", slot_troop_relations_begin),
			(troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", slot_troop_relations_begin),
			(jump_to_menu, ":notification_menu_types_relations_begin"),
			(assign, ":var_2", 2),
			(try_for_range, ":localvariable", 1, ":var_2"),
				(try_begin),
					(troop_slot_ge, "trp_notification_menu_types", ":localvariable", 1),
					(val_add, ":var_2", 1),
				(try_end),
				(store_sub, ":value", ":localvariable", 1),
				(troop_get_slot, ":notification_menu_types_localvariable", "trp_notification_menu_types", ":localvariable"),
				(troop_set_slot, "trp_notification_menu_types", ":value", ":notification_menu_types_localvariable"),
				(troop_get_slot, ":notification_menu_types_localvariable", "trp_notification_menu_var1", ":localvariable"),
				(troop_set_slot, "trp_notification_menu_var1", ":value", ":notification_menu_types_localvariable"),
				(troop_get_slot, ":notification_menu_types_localvariable", "trp_notification_menu_var2", ":localvariable"),
				(troop_set_slot, "trp_notification_menu_var2", ":value", ":notification_menu_types_localvariable"),
			(try_end)
		]),

	(3.0,
		[
			(map_free),
			(call_script, "script_get_closest_center", "p_main_party"),
			(party_get_slot, ":reg0_center_original_faction", reg0, slot_center_original_faction),
			(music_set_situation, 65536),
			(try_begin),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_20"),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_25"),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_28"),
				(eq, ":reg0_center_original_faction", "fac_kingdom_31"),
				(music_set_culture, 8),
			(else_try),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_28"),
				(eq, ":reg0_center_original_faction", "fac_kingdom_31"),
				(music_set_culture, 16),
			(else_try),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_3"),
				(eq, ":reg0_center_original_faction", "fac_kingdom_27"),
				(music_set_culture, 4),
			(else_try),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_4"),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_11"),
				(this_or_next|eq, ":reg0_center_original_faction", "fac_kingdom_2"),
				(eq, ":reg0_center_original_faction", "fac_kingdom_14"),
				(music_set_culture, 2),
			(else_try),
				(music_set_culture, 1),
			(try_end)
		]),

	(0.0,
		[
			(try_begin),
				(eq, "$caravan_escort_state", 1),
				(party_is_active, "$caravan_escort_party_id"),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_caravan_escort_destination_town_caravan_escort_party_id", "$caravan_escort_destination_town", "$caravan_escort_party_id"),
				(lt, ":distance_to_party_from_party_caravan_escort_destination_town_caravan_escort_party_id", 2),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_main_party_caravan_escort_party_id", "p_main_party", "$caravan_escort_party_id"),
				(lt, ":distance_to_party_from_party_main_party_caravan_escort_party_id", 5),
				(assign, "$talk_context", 2),
				(assign, "$g_encountered_party", "$caravan_escort_party_id"),
				(party_stack_get_troop_id, ":party_stack_troop_id_caravan_escort_party_id_0", "$caravan_escort_party_id", 0),
				(party_stack_get_troop_dna, ":party_stack_troop_dna_caravan_escort_party_id_0", "$caravan_escort_party_id", 0),
				(start_map_conversation, ":party_stack_troop_id_caravan_escort_party_id_0", ":party_stack_troop_dna_caravan_escort_party_id_0"),
			(try_end),
			(try_begin),
				(gt, "$g_reset_mission_participation", 1),
				(try_for_range, ":troop", "trp_npc1", "trp_heroes_end"),
					(troop_set_slot, ":troop", slot_troop_mission_participation, 0),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 0),
			(faction_slot_eq, "fac_player_supporters_faction", slot_faction_ai_state, 6),
			(store_current_hours, ":current_hours"),
			(faction_get_slot, ":player_supporters_faction_ai_current_state_started", "fac_player_supporters_faction", slot_faction_ai_current_state_started),
			(val_sub, ":current_hours", ":player_supporters_faction_ai_current_state_started"),
			(gt, ":current_hours", 168),
			(call_script, "script_faction_conclude_feast", "fac_player_supporters_faction", 6),
			(display_message, "@Your kingdoms feast have concluded.")
		]),

	(4.0,
		[
			(try_for_range, ":troop", "trp_knight_1_1_wife", "trp_heroes_end"),
				(neg|troop_slot_ge, ":troop", 8, 0),
				(call_script, "script_get_kingdom_lady_social_determinants", ":troop"),
				(assign, ":var_2", reg1),
				(troop_set_slot, ":troop", slot_troop_cur_center, ":var_2"),
			(try_end)
		]),

#	(2.0,
#		[]),

	(24.0,
		[
			(try_begin),
				(neg|check_quest_active, "qst_visit_lady"),
				(neg|troop_slot_ge, "trp_player", 8, 1),
				(neg|troop_slot_ge, "trp_player", 30, "trp_npc1"),
				(assign, ":value", -1),
				(assign, ":value_2", 120),
				(try_for_range, ":troop", "trp_knight_1_1_wife", "trp_heroes_end"),
					(troop_slot_ge, ":troop", 5, 2),
					(neg|troop_slot_eq, ":troop", slot_troop_met, 4),
					(troop_slot_eq, ":troop", slot_troop_love_interest_3, 0),
					(troop_slot_eq, ":troop", slot_troop_spouse, -1),
					(troop_get_slot, ":troop_cur_center", ":troop", slot_troop_cur_center),
					(is_between, ":troop_cur_center", "p_town_1_1", "p_village_1_1"),
					(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop"),
					(gt, reg0, 1),
					(store_current_hours, ":current_hours"),
					(troop_get_slot, ":troop_last_talk_time", ":troop", slot_troop_last_talk_time),
					(val_sub, ":current_hours", ":troop_last_talk_time"),
					(gt, ":current_hours", ":value_2"),
					(assign, ":value_2", ":current_hours"),
					(assign, ":value", ":troop"),
					(assign, ":var_7", ":troop_cur_center"),
				(try_end),
				(try_begin),
					(gt, ":value", 0),
					(call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":value", ":var_7"),
				(try_end),
			(try_end)
		]),

	(1.0,
		[
			(ge, "$g_player_raiding_village", 1),
			(try_begin),
				(neq, "$g_player_is_captive", 0),
				(assign, "$g_player_raiding_village", 0),
			(else_try),
				(map_free),
				(assign, "$g_player_raiding_village", 0),
			(else_try),
				(this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, 2),
				(party_slot_eq, "$g_player_raiding_village", slot_village_state, 4),
				(start_encounter, "$g_player_raiding_village"),
				(rest_for_hours, 0),
				(assign, "$g_player_raiding_village", 0),
				(assign, "$g_player_raid_complete", 1),
			(else_try),
				(party_slot_eq, "$g_player_raiding_village", slot_village_state, 1),
				(rest_for_hours, 3, 3, 1),
			(else_try),
				(rest_for_hours, 0, 0, 0),
				(assign, "$g_player_raiding_village", 0),
				(assign, "$g_player_raid_complete", 0),
			(try_end)
		]),

	(168.0,
		[
			(assign, "$g_presentation_lines_to_display_begin", 0),
			(assign, "$g_presentation_lines_to_display_end", 15),
			(assign, "$g_apply_budget_report_to_gold", 1),
			(store_current_hours, "$g_last_payday"),
			(try_begin),
				(eq, "$g_infinite_camping", 0),
				(start_presentation, "prsnt_budget_report"),
				(try_begin),
					(gt, "$g_player_debt_to_party_members", 5000),
					(call_script, "script_add_notification_menu", "mnu_dplmc_deserters", 20, 0),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(le, "$auto_menu", 0),
			(gt, "$players_kingdom", 0),
			(neq, "$players_kingdom", "fac_player_supporters_faction"),
			(eq, "$player_has_homage", 0),
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(assign, ":value", 0),
			(try_begin),
				(is_between, ":player_spouse", "trp_npc1", "trp_knight_1_1_wife"),
				(store_faction_of_troop, ":faction_of_troop_player_spouse", ":player_spouse"),
				(eq, ":faction_of_troop_player_spouse", "$players_kingdom"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 0),
			(store_current_day, ":current_day"),
			(gt, ":current_day", "$mercenary_service_next_renew_day"),
			(jump_to_menu, "mnu_oath_fulfilled")
		]),

	(180.0,
		[
			(val_sub, "$g_player_luck", 1),
			(val_max, "$g_player_luck", 0)
		]),

	(72.0,
		[
			(assign, "$lady_flirtation_location", 0)
		]),

	(4.0,
		[
			(assign, "$g_time_to_spare", 1),
			(try_begin),
				(troop_slot_ge, "trp_player", 30, "trp_npc1"),
				(assign, "$g_player_banner_granted", 1),
			(try_end)
		]),

	(24.0,
		[
			(eq, "$g_player_banner_granted", 1),
			(troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
			(le, "$auto_menu", 0),
			(start_presentation, "prsnt_banner_selection")
		]),

	(24.0,
		[
			(call_script, "script_get_player_party_morale_values"),
			(assign, ":var_1", reg0),
			(party_get_morale, ":morale_main_party", "p_main_party"),
			(store_sub, ":value", ":var_1", ":morale_main_party"),
			(store_div, ":value_2", ":value", 5),
			(store_mul, ":value_3", ":value_2", 5),
			(try_begin),
				(neq, ":value_3", ":value"),
				(try_begin),
					(gt, ":value", 0),
					(val_add, ":value_2", 1),
				(else_try),
					(val_sub, ":value_2", 1),
				(try_end),
			(try_end),
			(val_add, ":morale_main_party", ":value_2"),
			(party_set_morale, "p_main_party", ":morale_main_party")
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks_party", ":party"),
				(try_for_range_backwards, ":var_3", 0, ":num_prisoner_stacks_party"),
					(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_party_var_3", ":party", ":var_3"),
					(neg|troop_is_hero, ":party_prisoner_stack_troop_id_party_var_3"),
					(party_prisoner_stack_get_size, ":party_prisoner_stack_size_party_var_3", ":party", ":var_3"),
					(store_random_in_range, ":random_in_range_0_40", 0, 40),
					(val_mul, ":party_prisoner_stack_size_party_var_3", ":random_in_range_0_40"),
					(val_div, ":party_prisoner_stack_size_party_var_3", 100),
					(party_remove_prisoners, ":party", ":party_prisoner_stack_troop_id_party_var_3", ":party_prisoner_stack_size_party_var_3"),
				(try_end),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_get_slot, ":troop_player_debt", ":troop", slot_troop_player_debt),
				(val_mul, ":troop_player_debt", 101),
				(val_div, ":troop_player_debt", 100),
				(troop_set_slot, ":troop", slot_troop_player_debt, ":troop_player_debt"),
				(call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop"),
			(try_end)
		]),

	(24.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(ge, ":troop_leaded_party", 1),
				(party_is_active, ":troop_leaded_party"),
				(party_get_attached_to, ":attached_to_troop_leaded_party", ":troop_leaded_party"),
				(is_between, ":attached_to_troop_leaded_party", "p_town_1_1", "p_salt_mine"),
				(party_slot_eq, ":attached_to_troop_leaded_party", slot_center_is_besieged_by, -1),
				(store_faction_of_party, ":faction_of_party_troop_leaded_party", ":troop_leaded_party"),
				(try_begin),
					(this_or_next|eq, ":faction_of_party_troop_leaded_party", "fac_player_supporters_faction"),
					(eq, ":faction_of_party_troop_leaded_party", "$players_kingdom"),
					(assign, ":value", 1),
					(store_random_in_range, ":random_in_range_0_2", 0, 2),
					(val_add, ":value", ":random_in_range_0_2"),
				(else_try),
					(game_get_reduce_campaign_ai, ":game_reduce_campaign_ai"),
					(try_begin),
						(eq, ":game_reduce_campaign_ai", 0),
						(assign, ":value", 3),
					(else_try),
						(eq, ":game_reduce_campaign_ai", 1),
						(assign, ":value", 2),
					(else_try),
						(eq, ":game_reduce_campaign_ai", 2),
						(assign, ":value", 1),
					(try_end),
				(try_end),
				(try_begin),
					(faction_slot_eq, ":faction_of_party_troop_leaded_party", slot_faction_marshall, ":troop"),
					(val_add, ":value", 1),
				(try_end),
				(try_for_range, ":unused", 0, ":value"),
				#(neq, ":troop", 3730), #Patch world map bug
					(call_script, "script_hire_men_to_kingdom_hero_party", ":troop"),
				(try_end),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(neg|party_slot_eq, ":party", slot_town_lord, "trp_player"),
				(party_set_slot, ":party", 700, 0),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"), #castles maximum garrison size
				(party_slot_ge, ":party", 7, 0),
				(party_slot_eq, ":party", slot_center_is_besieged_by, -1),
				(party_slot_eq, ":party", 700, 0),
				(try_begin),
				(gt, "$adjust_size", 30),
				(assign, ":value_2", "$adjust_size"),
				(val_add, ":value_2", 270), #adjust size, adjust_size
				(else_try),
				(assign, ":value_2", 300), #DEF
				(try_end),
				(try_begin),
					(is_between, ":party", "p_town_1_1", "p_castle_1_1"), #towns maximum garrison size
					(try_begin),
					(gt, "$adjust_size", 30),
					(assign, ":value_2", "$adjust_size"),
					(val_add, ":value_2", 470), #adjust_size adjust size
					(else_try),
					(assign, ":value_2", 500),
					(try_end),
					#(assign, ":value_2", 500), #DEF
				(try_end),
				(party_get_num_companions, ":num_companions_party", ":party"),
				(try_begin),
					(lt, ":num_companions_party", ":value_2"),
					(call_script, "script_cf_reinforce_party", ":party"),
				(try_end),
			(try_end)
		]),

#	(360.0,
#		[]),

	(6.0,
		[
			(store_current_day, ":current_day"),
			(try_begin),
				(neq, ":current_day", "$g_last_half_payment_check_day"),
				(assign, "$g_last_half_payment_check_day", ":current_day"),
				(try_begin),
					(eq, "$g_half_payment_checkpoint", 1),
					(val_add, "$g_cur_week_half_daily_wage_payments", 1),
				(try_end),
				(assign, "$g_half_payment_checkpoint", 1),
			(try_end),
			(assign, ":value", 0),
			(try_begin),
				(neg|map_free),
				(ge, "$g_last_rest_center", 0),
				(this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
				(is_between, "$g_last_rest_center", "p_town_1_1", "p_village_1_1"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 0),
			(assign, "$g_half_payment_checkpoint", 0)
		]),

	(2.0,
		[
			(store_current_hours, ":current_hours"),
			(try_begin),
				(gt, ":current_hours", 168),
				(call_script, "script_randomly_start_war_peace_new", 1),
			(try_end),
			(store_sub, ":value", "fac_kingdoms_end", 1),
			(try_begin),
				(ge, "$g_diplo_kingdom", ":value"),
				(try_begin),
					(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 0),
					(assign, "$g_diplo_kingdom", "fac_player_supporters_faction"),
				(else_try),
					(assign, "$g_diplo_kingdom", "fac_kingdom_1"),
				(try_end),
			(else_try),
				(val_add, "$g_diplo_kingdom", 1),
			(try_end)
		]),

	(24.0,
		[
			(try_begin),
				(call_script, "script_raf_create_incidents"),
				(assign, ":var_1", reg0),
				(assign, ":var_2", reg1),
				(gt, ":var_1", 0),
				(gt, ":var_2", 0),
				(store_faction_of_party, ":faction_of_party_var_1", ":var_1"),
				(store_faction_of_party, ":faction_of_party_var_2", ":var_2"),
				(neq, ":var_1", ":var_2"),
				(neq, ":faction_of_party_var_1", ":faction_of_party_var_2"),
				(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction_of_party_var_2", ":faction_of_party_var_1"),
				(eq, reg0, 0),
				(try_begin),
					(party_slot_eq, ":var_1", slot_center_original_faction, ":faction_of_party_var_2"),
					(call_script, "script_notification_border_incident", ":var_1", -1),
				(else_try),
					(party_slot_eq, ":var_1", slot_center_ex_faction, ":faction_of_party_var_2"),
					(call_script, "script_notification_border_incident", ":var_1", -1),
				(else_try),
					(set_fixed_point_multiplier, 1),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_2", ":var_1", ":var_2"),
					(lt, ":distance_to_party_from_party_var_1_var_2", 25),
					(call_script, "script_notification_border_incident", ":var_1", ":var_2"),
				(try_end),
			(try_end),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_slot_eq, ":script_param_2", slot_faction_state, 0),
				(try_for_range, ":faction_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(neq, ":script_param_2", ":faction_2"),
					(faction_slot_eq, ":faction_2", slot_faction_state, 0),
					(store_add, ":value", ":faction_2", 120),
					(val_sub, ":value", "fac_player_supporters_faction"),
					(faction_get_slot, ":faction_value", ":script_param_2", ":value"),
					(try_begin),
						(ge, ":faction_value", 1),
						(try_begin),
							(eq, ":faction_value", 1),
							(call_script, "script_update_faction_notes", ":script_param_2"),
							(lt, ":script_param_2", ":faction_2"),
							(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":script_param_2", ":faction_2"),
						(try_end),
						(val_sub, ":faction_value", 1),
						(faction_set_slot, ":script_param_2", ":value", ":faction_value"),
					(try_end),
					(store_add, ":value_2", ":faction_2", 170),
					(val_sub, ":value_2", "fac_player_supporters_faction"),
					(faction_get_slot, ":faction_value_2", ":script_param_2", ":value_2"),
					(try_begin),
						(ge, ":faction_value_2", 1),
						(try_begin),
							(store_relation, ":relation_faction_faction_2", ":script_param_2", ":faction_2"),
							(lt, ":relation_faction_faction_2", 0),
							(faction_set_slot, ":script_param_2", ":value_2", 0),
						(else_try),
							(eq, ":faction_value_2", 1),
							(call_script, "script_notification_casus_belli_expired", ":script_param_2", ":faction_2"),
							(faction_set_slot, ":script_param_2", ":value_2", 0),
						(else_try),
							(val_sub, ":faction_value_2", 1),
							(faction_set_slot, ":script_param_2", ":value_2", ":faction_value_2"),
						(try_end),
					(try_end),
					(try_begin),
						(store_relation, ":relation_faction_faction_2", ":script_param_2", ":faction_2"),
						(lt, ":relation_faction_faction_2", 0),
						(store_add, ":value_3", ":faction_2", 220),
						(val_sub, ":value_3", "fac_player_supporters_faction"),
						(faction_get_slot, ":faction_value_3", ":script_param_2", ":value_3"),
						(val_add, ":faction_value_3", 1),
						(faction_set_slot, ":script_param_2", ":value_3", ":faction_value_3"),
					(try_end),
				(try_end),
				(call_script, "script_update_faction_notes", ":script_param_2"),
			(try_end)
		]),

	(48.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(gt, ":troop_leaded_party", "p_salt_mine"),
				(party_is_active, ":troop_leaded_party"),
				(store_skill_level, ":skill_level_17_troop", 17, ":troop"),
				(val_add, ":skill_level_17_troop", 3),
				(store_mul, ":value", ":skill_level_17_troop", 500),
				(assign, ":value_2", 30),
				(try_begin),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(neq, ":faction_of_troop_troop", "$players_kingdom"),
					(game_get_reduce_campaign_ai, ":game_reduce_campaign_ai"),
					(try_begin),
						(eq, ":game_reduce_campaign_ai", 0),
						(assign, ":value_2", 35),
						(val_mul, ":value", 3),
						(val_div, ":value", 2),
					(else_try),
						(eq, ":game_reduce_campaign_ai", 2),
						(assign, ":value_2", 25),
						(val_div, ":value", 2),
					(try_end),
				(try_end),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(le, ":random_in_range_0_100", ":value_2"),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(party_get_slot, ":party_town_lord", ":party", slot_town_lord),
				(neq, ":party_town_lord", "trp_player"),
				(assign, ":value", 3000),
				(assign, ":value_2", 30),
				(try_begin),
					(assign, ":var_11", -1),
					(try_begin),
						(ge, ":party_town_lord", 0),
						(store_faction_of_troop, ":var_11", ":party_town_lord"),
					(try_end),
					(neq, ":var_11", "$players_kingdom"),
					(game_get_reduce_campaign_ai, ":game_reduce_campaign_ai"),
					(try_begin),
						(eq, ":game_reduce_campaign_ai", 0),
						(assign, ":value_2", 35),
						(val_mul, ":value", 3),
						(val_div, ":value", 2),
					(else_try),
						(eq, ":game_reduce_campaign_ai", 2),
						(assign, ":value_2", 25),
						(val_div, ":value", 2),
					(try_end),
				(try_end),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(le, ":random_in_range_0_100", ":value_2"),
			(try_end)
		]),

	(24.0,
		[
			(call_script, "script_process_sieges")
		]),

	(2.0,
		[
			(call_script, "script_process_village_raids")
		]),

	(7.0,
		[
			(call_script, "script_init_ai_calculation"),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(call_script, "script_calculate_troop_ai", ":troop"),
			(try_end)
		]),

	(24.0,
		[
			(assign, "$men_are_pleased", 0)
		]),

	(24.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_get_slot, ":troop_intrigue_impatience", ":troop", slot_troop_intrigue_impatience),
				(val_sub, ":troop_intrigue_impatience", 5),
				(val_max, ":troop_intrigue_impatience", 0),
				(troop_set_slot, ":troop", slot_troop_intrigue_impatience, ":troop_intrigue_impatience"),
			(try_end),
			(store_random_in_range, ":random_in_range_1_3", 1, 3),
			(val_min, ":random_in_range_1_3", 2),
			(try_for_range, ":troop_2", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_get_slot, ":troop_2_days_on_mission", ":troop_2", slot_troop_days_on_mission),
				(ge, ":troop_2_days_on_mission", 1),
				(val_sub, ":troop_2_days_on_mission", ":random_in_range_1_3"),
				(val_max, ":troop_2_days_on_mission", 0),
				(troop_set_slot, ":troop_2", slot_troop_days_on_mission, ":troop_2_days_on_mission"),
			(try_end),
			(troop_get_slot, ":troop_2_days_on_mission", "trp_player", slot_troop_days_on_mission),
			(val_sub, ":troop_2_days_on_mission", ":random_in_range_1_3"),
			(val_max, ":troop_2_days_on_mission", 0),
			(troop_set_slot, "trp_player", slot_troop_days_on_mission, ":troop_2_days_on_mission")
		]),

	(6.0,
		[
			(call_script, "script_cf_random_political_event"),
			(call_script, "script_cf_random_political_event")
		]),

	(0.5,
		[
			(val_add, "$g_lord_long_term_count", 1),
			(try_begin),
				(neg|is_between, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin", "trp_knight_1_1_wife"),
				(assign, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin"),
			(try_end),
			(assign, ":value", "$g_lord_long_term_count"),
			(try_begin),
				(eq, ":value", "trp_kingdom_heroes_including_player_begin"),
				(assign, ":value", "trp_player"),
			(try_end),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, 9, ":value"),
				(display_message, "@{!}DEBUG -- Doing political calculations for {s9}"),
			(try_end),
			(try_begin),
				(troop_slot_eq, ":value", slot_troop_occupation, 2),
				(neq, ":value", "trp_player"),
				(assign, ":value_2", -1),
				(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
					(party_slot_eq, ":party", slot_town_lord, ":value"),
					(assign, ":value_2", ":party"),
				(try_end),
				(try_begin),
					(eq, ":value_2", -1),
					(store_faction_of_troop, ":faction_of_troop_value", ":value"),
					(faction_get_slot, ":faction_of_troop_value_leader", ":faction_of_troop_value", slot_faction_leader),
					(troop_get_slot, ":value_lord_reputation_type", ":value", slot_lord_reputation_type),
					(try_begin),
						(neq, ":faction_of_troop_value_leader", ":value"),
						(try_begin),
							(this_or_next|eq, ":value_lord_reputation_type", 2),
							(this_or_next|eq, ":value_lord_reputation_type", 3),
							(this_or_next|eq, ":value_lord_reputation_type", 4),
							(eq, ":value_lord_reputation_type", 5),
							(call_script, "script_troop_change_relation_with_troop", ":value", ":faction_of_troop_value_leader", -4),
							(val_add, "$total_no_fief_changes", -4),
						(else_try),
							(eq, ":value_lord_reputation_type", 1),
							(call_script, "script_troop_change_relation_with_troop", ":value", ":faction_of_troop_value_leader", -2),
							(val_add, "$total_no_fief_changes", -2),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(this_or_next|troop_slot_eq, ":value", slot_troop_occupation, 2),
				(eq, ":value", "trp_player"),
				(try_begin),
					(eq, ":value", "trp_player"),
					(assign, ":var_7", "$players_kingdom"),
				(else_try),
					(store_faction_of_troop, ":var_7", ":value"),
				(try_end),
				(faction_get_slot, ":faction_of_troop_value_leader", ":var_7", slot_faction_leader),
				(neq, ":value", ":faction_of_troop_value_leader"),
				(neg|is_between, ":value", "trp_kingdom_1_lord", "trp_kingdom_1_pretender"),
				(neg|is_between, ":value", "trp_kingdom_1_pretender", "trp_knight_1_1"),
				(assign, ":var_8", 0),
				(try_for_range, ":party_2", "p_town_1_1", "p_village_1_1"),
					(store_faction_of_party, ":faction_of_party_party_2", ":party_2"),
					(eq, ":faction_of_party_party_2", ":var_7"),
					(val_add, ":var_8", 1),
				(try_end),
				(try_begin),
					(this_or_next|eq, ":var_7", "$players_kingdom"),
					(eq, ":var_7", "fac_player_supporters_faction"),
					(val_add, ":var_8", 1),
				(try_end),
				(call_script, "script_troop_get_relation_with_troop", ":value", ":faction_of_troop_value_leader"),
				(this_or_next|le, reg0, -50),
				(eq, ":var_8", 0),
				(call_script, "script_cf_troop_can_intrigue", ":value", 0),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(try_begin),
					(this_or_next|eq, ":var_8", 0),
					(neq, ":random_in_range_0_2", 0),
					(neq, ":value", "trp_player"),
					(try_begin),
						(neq, ":var_8", 0),
						(assign, "$g_give_advantage_to_original_faction", 1),
					(try_end),
					(store_faction_of_troop, ":faction_of_troop_value_2", ":value"),
					(call_script, "script_lord_find_alternative_faction", ":value"),
					(assign, ":var_13", reg0),
					(assign, "$g_give_advantage_to_original_faction", 0),
					(try_begin),
						(neq, ":var_13", ":faction_of_troop_value_2"),
						(is_between, ":var_13", "fac_player_supporters_faction", "fac_kingdoms_end"),
						(str_store_troop_name_link, 1, ":value"),
						(str_store_faction_name_link, 2, ":var_13"),
						(str_store_faction_name_link, 3, ":var_7"),
						(call_script, "script_change_troop_faction", ":value", ":var_13"),
						(try_begin),
							(ge, "$cheat_mode", 1),
							(str_store_troop_name, 4, ":value"),
							(display_message, "@{!}DEBUG - {s4} faction changed in defection"),
						(try_end),
						(troop_get_type, reg4, ":value"),
						(str_store_string, 4, "str_lord_defects_ordinary"),
						(display_log_message, "@{!}{s4}"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(this_or_next|eq, ":var_13", "$players_kingdom"),
							(eq, ":var_7", "$players_kingdom"),
							(call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":value", ":var_7"),
						(try_end),
					(try_end),
				(else_try),
					(neq, ":faction_of_troop_value_leader", "trp_player"),
					(call_script, "script_troop_get_relation_with_troop", ":value", ":faction_of_troop_value_leader"),
					(le, reg0, -50),
					(call_script, "script_indict_lord_for_treason", ":value", ":var_7"),
				(try_end),
			(else_try),
				(neq, ":value", "trp_player"),
				(store_faction_of_troop, ":var_7", ":value"),
				(faction_slot_ge, ":var_7", 64, 1),
				(neg|troop_slot_ge, ":value", 154, 1),
				(this_or_next|troop_slot_eq, ":value", slot_troop_stance_on_faction_issue, -1),
				(neq, "$players_kingdom", ":var_7"),
				(troop_slot_eq, ":value", slot_troop_occupation, 2),
				(call_script, "script_npc_decision_checklist_take_stand_on_issue", ":value"),
				(troop_set_slot, ":value", slot_troop_stance_on_faction_issue, reg0),
			(try_end),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(call_script, "script_troop_get_relation_with_troop", ":value", ":troop"),
				(lt, reg0, 0),
				(assign, ":var_15", reg0),
				(store_sub, ":value_3", 0, ":var_15"),
				(store_random_in_range, ":random_in_range_0_300", 0, 300),
				(lt, ":random_in_range_0_300", ":value_3"),
				(call_script, "script_troop_change_relation_with_troop", ":value", ":troop", 1),
				(val_add, "$total_relation_changes_through_convergence", 1),
			(try_end)
		]),

	(3.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(try_begin),
					(this_or_next|party_slot_ge, ":party", 54, 0),
					(party_slot_eq, ":party", slot_village_state, 1),
					(party_slot_eq, ":party", slot_center_last_spotted_enemy, -1),
					(call_script, "script_process_alarms_new", ":party"),
				(else_try),
					(this_or_next|neg|party_slot_ge, ":party", 54, 0),
					(neg|party_slot_eq, ":party", slot_village_state, 1),
					(party_set_slot, ":party", slot_center_last_spotted_enemy, -1),
					(party_set_slot, ":party", slot_center_sortie_strength, 0),
					(party_set_slot, ":party", slot_center_sortie_enemy_strength, 0),
				(try_end),
			(try_end)
		]),

	(1.0,
		[
			(call_script, "script_allow_vassals_to_join_indoor_battle"),
			(call_script, "script_process_kingdom_parties_ai")
		]),

	(3.0,
		[
			(store_current_hours, ":current_hours"),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(party_get_slot, ":party_center_is_besieged_by", ":party", slot_center_is_besieged_by),
				(gt, ":party_center_is_besieged_by", 0),
				(party_is_active, ":party_center_is_besieged_by"),
				(store_faction_of_party, ":faction_of_party_party_center_is_besieged_by", ":party_center_is_besieged_by"),
				(party_slot_ge, ":party", 54, 1),
				(party_get_slot, ":party_center_siege_begin_hours", ":party", slot_center_siege_begin_hours),
				(store_sub, ":party_center_siege_begin_hours", ":current_hours", ":party_center_siege_begin_hours"),
				(assign, ":value", 0),
				(assign, ":value_2", 0),
				(assign, ":var_8", 0),
				(assign, ":value_3", 0),
				(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
					(troop_slot_eq, ":troop", slot_troop_occupation, 2),
					(neg|troop_slot_ge, ":troop", 8, 0),
					(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
					(gt, ":troop_leaded_party", 0),
					(party_is_active, ":troop_leaded_party"),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(eq, ":faction_of_troop_troop", ":faction_of_party_party_center_is_besieged_by"),
					(assign, ":value_4", 0),
					(try_begin),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 1),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_object, ":party"),
						(assign, ":value_4", 1),
					(else_try),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 11),
						(party_get_slot, ":troop_leaded_party_ai_object", ":troop_leaded_party", slot_party_ai_object),
						(gt, ":troop_leaded_party_ai_object", 0),
						(party_is_active, ":troop_leaded_party_ai_object"),
						(party_slot_eq, ":troop_leaded_party_ai_object", slot_party_ai_state, 1),
						(party_slot_eq, ":troop_leaded_party_ai_object", slot_party_ai_object, ":party"),
						(assign, ":value_4", 1),
					(try_end),
					(eq, ":value_4", 1),
					(party_get_battle_opponent, ":battle_opponent_troop_leaded_party", ":troop_leaded_party"),
					(this_or_next|lt, ":battle_opponent_troop_leaded_party", 0),
					(eq, ":battle_opponent_troop_leaded_party", ":party"),
					(try_begin),
						(faction_slot_eq, ":faction_of_party_party_center_is_besieged_by", slot_faction_marshall, ":troop"),
						(assign, ":value_3", 1),
					(try_end),
					(call_script, "script_party_calculate_regular_strength", ":troop_leaded_party"),
					(val_add, ":var_8", reg0),
				(try_end),
				(try_begin),
					(gt, ":var_8", 0),
					(party_collect_attachments_to_party, ":party", "p_collective_enemy"),
					(call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
					(assign, ":var_16", reg0),
					(try_begin),
						(eq, "$auto_enter_town", ":party"),
						(eq, "$g_player_is_captive", 0),
						(call_script, "script_party_calculate_regular_strength", "p_main_party"),
						(val_add, ":var_16", reg0),
						(val_mul, ":var_8", 2),
					(try_end),
					(party_get_slot, ":party_center_siege_hardness", ":party", slot_center_siege_hardness),
					(val_add, ":party_center_siege_hardness", 100),
					(val_mul, ":var_16", ":party_center_siege_hardness"),
					(val_div, ":var_16", 100),
					(val_max, ":var_16", 1),
					(try_begin),
						(eq, ":value_3", 1),
						(eq, ":faction_of_party_party_center_is_besieged_by", "$players_kingdom"),
						(check_quest_active, "qst_follow_army"),
						(val_mul, ":var_8", 2),
					(try_end),
					(store_mul, ":value_5", ":var_8", 100),
					(val_div, ":value_5", ":var_16"),
					(store_sub, ":value_6", ":value_5", 240),
					(try_begin),
						(gt, ":value_6", -100),
						(store_div, ":value_7", ":party_center_siege_begin_hours", 2),
						(val_add, ":value_6", ":value_7"),
					(try_end),
					(val_div, ":value_6", 5),
					(val_max, ":value_6", 0),
					(store_sub, ":value_8", 175, ":value_5"),
					(val_max, ":value_8", 0),
					(try_begin),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(lt, ":random_in_range_0_100", ":value_6"),
						(gt, ":party_center_siege_begin_hours", 24),
						(assign, ":value", 1),
					(else_try),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(lt, ":random_in_range_0_100", ":value_8"),
						(assign, ":value_2", 1),
					(try_end),
				(else_try),
					(assign, ":value_2", 1),
				(try_end),
				(try_begin),
					(eq, ":value", 1),
					(call_script, "script_begin_assault_on_center", ":party"),
				(else_try),
					(eq, ":value_2", 1),
					(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
						(troop_slot_eq, ":troop", slot_troop_occupation, 2),
						(neg|troop_slot_ge, ":troop", 8, 0),
						(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
						(gt, ":troop_leaded_party", 0),
						(party_is_active, ":troop_leaded_party"),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 1),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_object, ":party"),
						(party_slot_eq, ":troop_leaded_party", slot_party_ai_substate, 1),
						(call_script, "script_party_set_ai_state", ":troop_leaded_party", -1, -1),
						(call_script, "script_party_set_ai_state", ":troop_leaded_party", 1, ":party"),
						(party_set_slot, ":party", slot_center_siege_begin_hours, ":current_hours"),
					(try_end),
				(try_end),
			(try_end)
		]),

	(0.5,
		[
			(call_script, "script_recalculate_ais"),
			(val_add, "$g_ai_kingdom", 1),
			(try_begin),
				(ge, "$g_ai_kingdom", "fac_kingdoms_end"),
				(assign, "$g_ai_kingdom", "fac_player_supporters_faction"),
			(try_end)
		]),

	(24.0,
		[
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(call_script, "script_faction_recalculate_strength", ":script_param_2"),
			(try_end),
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(neg|faction_slot_eq, ":faction_of_troop_troop", slot_faction_ai_state, 0),
				(neg|faction_slot_eq, ":faction_of_troop_troop", slot_faction_ai_state, 6),
				(neg|faction_slot_eq, ":faction_of_troop_troop", slot_faction_ai_state, 1),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(party_is_active, ":troop_leaded_party"),
				(val_add, "$total_vassal_days_on_campaign", 1),
				(party_slot_eq, ":troop_leaded_party", slot_party_ai_state, 11),
				(val_add, "$total_vassal_days_responding_to_campaign", 1),
			(try_end)
		]),

	(36.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_heroes_end"),
				(troop_set_slot, ":troop", slot_troop_does_not_give_quest, 0),
			(try_end),
			(try_for_range, ":troop", "trp_village_1_elder", "trp_merchants_end"),
				(troop_set_slot, ":troop", slot_troop_does_not_give_quest, 0),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(call_script, "script_refresh_village_merchant_inventory", ":party"),
			(try_end)
		]),

	(48.0,
		[
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(call_script, "script_refresh_village_defenders", ":party"),
				(party_set_slot, ":party", slot_village_player_can_not_steal_cattle, 0),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(neg|is_between, ":party", "p_castle_1_1", "p_village_1_1"),
				(party_get_slot, ":party_village_number_of_cattle", ":party", slot_village_number_of_cattle),
				(party_get_slot, ":party_center_head_sheep", ":party", slot_center_head_sheep),
				(party_get_slot, ":party_center_acres_pasture", ":party", slot_center_acres_pasture),
				(val_max, ":party_center_acres_pasture", 1),
				(store_mul, ":value", ":party_village_number_of_cattle", 400),
				(store_mul, ":value_2", ":party_center_head_sheep", 200),
				(val_add, ":value", ":value_2"),
				(val_div, ":value", ":party_center_acres_pasture"),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(try_begin),
					(eq, ":random_in_range_0_100", 0),
					(val_min, ":party_village_number_of_cattle", 10),
				(else_try),
					(gt, ":value", 100),
					(val_mul, ":party_center_head_sheep", 90),
					(val_div, ":party_center_head_sheep", 100),
					(val_mul, ":party_village_number_of_cattle", 90),
					(val_div, ":party_village_number_of_cattle", 100),
				(else_try),
					(lt, ":value", 30),
					(val_mul, ":party_village_number_of_cattle", 120),
					(val_div, ":party_village_number_of_cattle", 100),
					(val_add, ":party_village_number_of_cattle", 1),
					(val_mul, ":party_center_head_sheep", 120),
					(val_div, ":party_center_head_sheep", 100),
					(val_add, ":party_center_head_sheep", 1),
				(else_try),
					(lt, ":value", 60),
					(val_mul, ":party_village_number_of_cattle", 110),
					(val_div, ":party_village_number_of_cattle", 100),
					(val_add, ":party_village_number_of_cattle", 1),
					(val_mul, ":party_center_head_sheep", 110),
					(val_div, ":party_center_head_sheep", 100),
					(val_add, ":party_center_head_sheep", 1),
				(else_try),
					(lt, ":value", 100),
					(lt, ":random_in_range_0_100", 50),
					(val_mul, ":party_village_number_of_cattle", 105),
					(val_div, ":party_village_number_of_cattle", 100),
					(try_begin),
						(le, ":party_village_number_of_cattle", 20),
						(val_add, ":party_village_number_of_cattle", 1),
					(try_end),
					(val_mul, ":party_center_head_sheep", 105),
					(val_div, ":party_center_head_sheep", 100),
					(try_begin),
						(le, ":party_center_head_sheep", 20),
						(val_add, ":party_center_head_sheep", 1),
					(try_end),
				(try_end),
				(party_set_slot, ":party", slot_village_number_of_cattle, ":party_village_number_of_cattle"),
				(party_set_slot, ":party", slot_center_head_sheep, ":party_center_head_sheep"),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(try_begin),
					(party_slot_ge, ":party", 7, 0),
					(party_get_slot, ":party_center_accumulated_rents", ":party", slot_center_accumulated_rents),
					(assign, ":value", 800),
					(try_begin),
						(party_slot_eq, ":party", slot_party_type, 4),
						(try_begin),
							(party_slot_eq, ":party", slot_village_state, 0),
							(assign, ":value", 3000),
						(try_end),
					(else_try),
						(party_slot_eq, ":party", slot_party_type, 2),
						(assign, ":value", 6000),
					(else_try),
						(party_slot_eq, ":party", slot_party_type, 3),
						(assign, ":value", 10000),
					(try_end),
					(party_get_slot, ":party_town_prosperity", ":party", slot_town_prosperity),
					(store_add, ":value_2", 35, ":party_town_prosperity"),
					(val_mul, ":value", ":value_2"),
					(val_div, ":value", 135),
					(try_begin),
						(party_slot_eq, ":party", slot_town_lord, "trp_player"),
						(game_get_reduce_campaign_ai, ":game_reduce_campaign_ai"),
						(try_begin),
							(eq, ":game_reduce_campaign_ai", 0),
							(val_mul, ":value", 3),
							(val_div, ":value", 4),
						(else_try),
							(eq, ":game_reduce_campaign_ai", 1),
						(else_try),
							(eq, ":game_reduce_campaign_ai", 2),
							(val_mul, ":value", 4),
							(val_div, ":value", 3),
						(try_end),
					(try_end),
					(party_get_slot, ":party_400", ":party", 400),
					(store_mul, ":value_3", ":value", ":party_400"),
					(val_div, ":value_3", 100),
					(val_add, ":party_center_accumulated_rents", ":value_3"),
					(val_add, ":party_center_accumulated_rents", ":value"),
					(party_set_slot, ":party", slot_center_accumulated_rents, ":party_center_accumulated_rents"),
				(try_end),
			(try_end)
		]),

	(32.0,
		[
			(eq, "$players_kingdom", 0),
			(le, "$g_invite_faction", 0),
			(eq, "$g_player_is_captive", 0),
			(troop_get_type, ":type_player", "trp_player"),
			(try_begin),
				(eq, ":type_player", 1),
				(eq, "$npc_with_sisterly_advice", 0),
				(try_for_range, ":troop", "trp_npc1", "trp_kingdom_1_lord"),
					(main_party_has_troop, ":troop"),
					(troop_get_type, ":type_troop", ":troop"),
					(eq, ":type_troop", 1),
					(troop_slot_ge, "trp_player", 7, 150),
					(troop_slot_ge, ":troop", 139, 1),
					(assign, "$npc_with_sisterly_advice", ":troop"),
				(try_end),
			(else_try),
				(store_random_in_range, ":random_in_range_kingdom_1_kingdoms_end", "fac_kingdom_1", "fac_kingdoms_end"),
				(assign, ":var_5", 999999),
				(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
					(store_faction_of_party, ":faction_of_party_party", ":party"),
					(eq, ":faction_of_party_party", ":random_in_range_kingdom_1_kingdoms_end"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_main_party_party", "p_main_party", ":party"),
					(val_min, ":var_5", ":distance_to_party_from_party_main_party_party"),
				(try_end),
				(lt, ":var_5", 30),
				(store_relation, ":relation_random_in_range_kingdom_1_kingdoms_end_player_supporters_faction", ":random_in_range_kingdom_1_kingdoms_end", "fac_player_supporters_faction"),
				(faction_get_slot, ":random_in_range_kingdom_1_kingdoms_end_leader", ":random_in_range_kingdom_1_kingdoms_end", slot_faction_leader),
				(call_script, "script_troop_get_player_relation", ":random_in_range_kingdom_1_kingdoms_end_leader"),
				(assign, ":var_11", reg0),
				(call_script, "script_get_number_of_hero_centers", "trp_player"),
				(assign, ":var_12", reg0),
				(eq, "$g_infinite_camping", 0),
				(assign, ":value", 0),
				(try_begin),
					(ge, "p_main_party", 0),
					(store_party_size_wo_prisoners, ":value", "p_main_party"),
				(try_end),
				(try_begin),
					(eq, ":var_12", 0),
					(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
					(ge, ":player_renown", 160),
					(ge, ":relation_random_in_range_kingdom_1_kingdoms_end_player_supporters_faction", 0),
					(ge, ":var_11", 0),
					(ge, ":value", 45),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(lt, ":random_in_range_0_100", 50),
					(call_script, "script_get_poorest_village_of_faction", ":random_in_range_kingdom_1_kingdoms_end"),
					(assign, "$g_invite_offered_center", reg0),
					(ge, "$g_invite_offered_center", 0),
					(assign, "$g_invite_faction", ":random_in_range_kingdom_1_kingdoms_end"),
					(jump_to_menu, "mnu_invite_player_to_faction"),
				(else_try),
					(gt, ":var_12", 0),
					(neq, "$players_oath_renounced_against_kingdom", ":random_in_range_kingdom_1_kingdoms_end"),
					(ge, ":relation_random_in_range_kingdom_1_kingdoms_end_player_supporters_faction", -40),
					(ge, ":var_11", -20),
					(ge, ":value", 30),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(lt, ":random_in_range_0_100", 20),
					(assign, "$g_invite_faction", ":random_in_range_kingdom_1_kingdoms_end"),
					(assign, "$g_invite_offered_center", -1),
					(jump_to_menu, "mnu_invite_player_to_faction_without_center"),
				(try_end),
			(try_end)
		]),

	(168.0,
		[
			(assign, ":var_1", 0),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_slot_eq, ":script_param_2", slot_faction_state, 0),
				(try_for_range, ":faction_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(faction_slot_eq, ":faction_2", slot_faction_state, 0),
					(neq, ":faction_2", ":script_param_2"),
					(store_relation, ":relation_faction_faction_2", ":script_param_2", ":faction_2"),
					(lt, ":relation_faction_faction_2", 0),
					(val_add, ":var_1", 1),
				(try_end),
				(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(eq, ":faction_of_troop_troop", ":script_param_2"),
					(try_begin),
						(eq, ":var_1", 2),
						(store_random_in_range, ":random_in_range_3000_9999", 3000, 9999),
					(else_try),
						(gt, ":var_1", 3),
						(store_random_in_range, ":random_in_range_3000_9999", 7000, 9999),
					(else_try),
						(store_random_in_range, ":random_in_range_3000_9999", 0, 9999),
					(try_end),
					(troop_set_slot, ":troop", slot_troop_temp_decision_seed, ":random_in_range_3000_9999"),
				(try_end),
			(try_end)
		]),

	(0.3,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_heroes_end"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(ge, ":troop_leaded_party", 1),
				(party_is_active, ":troop_leaded_party"),
				(party_get_attached_to, ":attached_to_troop_leaded_party", ":troop_leaded_party"),
				(lt, ":attached_to_troop_leaded_party", 1),
				(party_get_cur_town, ":cur_town_troop_leaded_party", ":troop_leaded_party"),
				(is_between, ":cur_town_troop_leaded_party", "p_town_1_1", "p_salt_mine"),
				(call_script, "script_get_relation_between_parties", ":cur_town_troop_leaded_party", ":troop_leaded_party"),
				(try_begin),
					(ge, reg0, 0),
					(party_attach_to_party, ":troop_leaded_party", ":cur_town_troop_leaded_party"),
				(else_try),
					(party_set_ai_behavior, ":troop_leaded_party", 0),
				(try_end),
				(try_begin),
					(this_or_next|party_slot_eq, ":cur_town_troop_leaded_party", slot_party_type, 3),
					(party_slot_eq, ":cur_town_troop_leaded_party", slot_party_type, 2),
					(store_faction_of_party, ":faction_of_party_troop_leaded_party", ":troop_leaded_party"),
					(store_faction_of_party, ":faction_of_party_cur_town_troop_leaded_party", ":cur_town_troop_leaded_party"),
					(eq, ":faction_of_party_troop_leaded_party", ":faction_of_party_cur_town_troop_leaded_party"),
					(party_get_num_prisoner_stacks, ":num_prisoner_stacks_troop_leaded_party", ":troop_leaded_party"),
					(gt, ":num_prisoner_stacks_troop_leaded_party", 0),
					(assign, "$g_move_heroes", 1),
					(call_script, "script_party_prisoners_add_party_prisoners", ":cur_town_troop_leaded_party", ":troop_leaded_party"),
					(assign, "$g_move_heroes", 1),
					(call_script, "script_party_remove_all_prisoners", ":troop_leaded_party"),
				(try_end),
			(try_end),
			(try_for_parties, ":var_8"),
				(gt, ":var_8", "p_spawn_points_end"),
				(party_get_template_id, ":template_id_var_8", ":var_8"),
				(ge, ":template_id_var_8", "pt_steppe_bandit_lair"),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_main_party_var_8", "p_main_party", ":var_8"),
				(lt, ":distance_to_party_from_party_main_party_var_8", 3),
				(party_set_flags, ":var_8", 256, 0),
				(party_set_flags, ":var_8", 16384, 1),
			(try_end)
		]),

	(48.0,
		[
			(call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", 50),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(assign, ":value", 30),
				(try_begin),
					(party_slot_eq, ":party", slot_center_has_prisoner_tower, 1),
					(assign, ":value", 5),
				(try_end),
				(call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":party", ":value"),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(neg|troop_slot_ge, ":troop", 8, 0),
				(neg|troop_slot_ge, ":troop", 10, 1),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(try_begin),
					(eq, ":faction_of_troop_troop", "fac_outlaws"),
				(else_try),
					(try_begin),
						(eq, "$cheat_mode", 2),
						(str_store_troop_name, 4, ":troop"),
						(display_message, "str_debug__attempting_to_spawn_s4"),
					(try_end),
					(call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":faction_of_troop_troop", ":troop"),
					(assign, ":var_3", reg0),
					(try_begin),
						(eq, "$cheat_mode", 2),
						(assign, reg7, ":var_3"),
						(str_store_party_name, 7, ":var_3"),
						(display_message, "str_debug__s0_is_spawning_around_party__s7"),
					(try_end),
					(call_script, "script_create_kingdom_hero_party", ":troop", ":var_3"),
					(try_begin),
						(eq, "$g_there_is_no_avaliable_centers", 0),
						(party_attach_to_party, "$pout_party", ":var_3"),
					(try_end),
					(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
					(call_script, "script_party_set_ai_state", ":troop_leaded_party", 7, ":var_3"),
				(else_try),
					(neg|faction_slot_eq, ":faction_of_troop_troop", slot_faction_state, 0),
					(try_begin),
						(is_between, ":troop", "trp_kingdom_1_lord", "trp_kingdom_1_pretender"),
						(troop_set_slot, ":troop", slot_troop_change_to_faction, "fac_commoners"),
					(else_try),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(lt, ":random_in_range_0_100", 10),
						(call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":faction_of_troop_troop"),
						(troop_set_slot, ":troop", slot_troop_change_to_faction, reg0),
					(try_end),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_village_state, 0),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(lt, ":random_in_range_0_100", 60),
				(party_get_slot, ":party_village_market_town", ":party", slot_village_market_town),
				(party_slot_eq, ":party_village_market_town", slot_center_is_besieged_by, -1),
				(call_script, "script_do_villager_center_trade", ":party", ":party_village_market_town"),
				(assign, ":var_4", reg0),
				(call_script, "script_do_villager_center_trade", ":party_village_market_town", ":party"),
				(party_get_slot, ":party_village_market_town_center_accumulated_tariffs", ":party_village_market_town", slot_center_accumulated_tariffs),
				(party_get_slot, ":party_village_market_town_town_prosperity", ":party_village_market_town", slot_town_prosperity),
				(assign, ":var_7", ":var_4"),
				(val_mul, ":var_7", ":party_village_market_town_town_prosperity"),
				(val_div, ":var_7", 100),
				(val_div, ":var_7", 20),
				(val_add, ":party_village_market_town_center_accumulated_tariffs", ":var_7"),
				(party_set_slot, ":party_village_market_town", slot_center_accumulated_tariffs, ":party_village_market_town_center_accumulated_tariffs"),
				(party_get_slot, ":party_village_market_town_food_store", ":party_village_market_town", slot_party_food_store),
				(call_script, "script_center_get_food_store_limit", ":party_village_market_town"),
				(assign, ":var_18", reg0),
				(val_add, ":party_village_market_town_food_store", 1000),
				(val_min, ":party_village_market_town_food_store", ":var_18"),
				(party_set_slot, ":party_village_market_town", slot_party_food_store, ":party_village_market_town_food_store"),
			(try_end)
		]),

	(72.0,
		[
			(call_script, "script_update_trade_good_prices"),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(party_get_slot, ":party_town_player_odds", ":party", slot_town_player_odds),
				(try_begin),
					(gt, ":party_town_player_odds", 1000),
					(val_mul, ":party_town_player_odds", 95),
					(val_div, ":party_town_player_odds", 100),
					(val_max, ":party_town_player_odds", 1000),
				(else_try),
					(lt, ":party_town_player_odds", 1000),
					(val_mul, ":party_town_player_odds", 105),
					(val_div, ":party_town_player_odds", 100),
					(val_min, ":party_town_player_odds", 1000),
				(try_end),
				(party_set_slot, ":party", slot_town_player_odds, ":party_town_player_odds"),
			(try_end)
		]),

	(8.0,
		[
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 11),
				(party_is_in_any_town, ":var_1"),
				(store_faction_of_party, ":faction_of_party_var_1", ":var_1"),
				(faction_get_slot, ":faction_of_party_var_1_num_towns", ":faction_of_party_var_1", slot_faction_num_towns),
				(try_begin),
					(le, ":faction_of_party_var_1_num_towns", 0),
					(remove_party, ":var_1"),
				(else_try),
					(party_get_cur_town, ":cur_town_var_1", ":var_1"),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(try_begin),
						(party_slot_eq, ":cur_town_var_1", slot_town_lord, "trp_player"),
						(game_get_reduce_campaign_ai, ":game_reduce_campaign_ai"),
						(try_begin),
							(eq, ":game_reduce_campaign_ai", 0),
							(assign, ":value", 35),
						(else_try),
							(eq, ":game_reduce_campaign_ai", 1),
							(assign, ":value", 45),
						(else_try),
							(eq, ":game_reduce_campaign_ai", 2),
							(assign, ":value", 60),
						(try_end),
					(else_try),
						(assign, ":value", 45),
					(try_end),
					(lt, ":random_in_range_0_100", ":value"),
					(assign, ":value_2", 1),
					(try_begin),
						(is_between, ":cur_town_var_1", "p_town_1_1", "p_village_1_1"),
						(neg|party_slot_eq, ":cur_town_var_1", slot_center_is_besieged_by, -1),
						(assign, ":value_2", 0),
					(try_end),
					(eq, ":value_2", 1),
					(assign, ":value_3", 0),
					(try_begin),
						(party_get_slot, ":var_1_ai_state", ":var_1", slot_party_ai_state),
						(eq, ":var_1_ai_state", 13),
						(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
						(eq, ":cur_town_var_1", ":var_1_ai_object"),
						(assign, ":value_3", 1),
					(try_end),
					(assign, ":value_4", -1),
					(try_begin),
						(eq, "$caravan_escort_party_id", ":var_1"),
						(neg|party_is_in_town, ":var_1", "$caravan_escort_destination_town"),
						(assign, ":value_4", "$caravan_escort_destination_town"),
					(else_try),
						(call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_town_var_1", ":faction_of_party_var_1"),
						(assign, ":value_4", reg0),
					(try_end),
					(is_between, ":value_4", "p_town_1_1", "p_castle_1_1"),
					(neg|party_is_in_town, ":var_1", ":value_4"),
					(try_begin),
						(eq, ":value_3", 1),
						(str_store_party_name, 7, ":cur_town_var_1"),
						(call_script, "script_do_merchant_town_trade", ":var_1", ":cur_town_var_1"),
					(try_end),
					(party_set_ai_behavior, ":var_1", 1),
					(party_set_ai_object, ":var_1", ":value_4"),
					(party_set_flags, ":var_1", 65536, 0),
					(party_set_slot, ":var_1", slot_party_ai_state, 13),
					(party_set_slot, ":var_1", slot_party_ai_object, ":value_4"),
				(try_end),
			(try_end)
		]),

	(8.0,
		[
			(eq, 0, 1),
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 15),
				(party_is_in_any_town, ":var_1"),
				(party_get_slot, ":var_1_home_center", ":var_1", slot_party_home_center),
				(party_get_cur_town, ":cur_town_var_1", ":var_1"),
				(assign, ":value", 1),
				(try_begin),
					(is_between, ":cur_town_var_1", "p_town_1_1", "p_village_1_1"),
					(neg|party_slot_eq, ":cur_town_var_1", slot_center_is_besieged_by, -1),
					(assign, ":value", 0),
				(try_end),
				(eq, ":value", 1),
				(try_begin),
					(eq, ":cur_town_var_1", ":var_1_home_center"),
					(call_script, "script_do_party_center_trade", ":var_1", ":var_1_home_center", 25),
					(store_faction_of_party, ":faction_of_party_cur_town_var_1", ":cur_town_var_1"),
					(party_set_faction, ":var_1", ":faction_of_party_cur_town_var_1"),
					(party_get_slot, ":var_1_home_center_village_market_town", ":var_1_home_center", slot_village_market_town),
					(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_home_center_village_market_town"),
					(party_set_slot, ":var_1", slot_party_ai_state, 13),
					(party_set_ai_behavior, ":var_1", 1),
					(party_set_ai_object, ":var_1", ":var_1_home_center_village_market_town"),
				(else_try),
					(try_begin),
						(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
						(eq, ":cur_town_var_1", ":var_1_ai_object"),
						(call_script, "script_do_party_center_trade", ":var_1", ":var_1_ai_object", 25),
						(assign, ":var_8", reg0),
						(party_get_slot, ":var_1_ai_object_center_accumulated_tariffs", ":var_1_ai_object", slot_center_accumulated_tariffs),
						(party_get_slot, ":var_1_ai_object_town_prosperity", ":var_1_ai_object", slot_town_prosperity),
						(assign, ":var_11", ":var_8"),
						(val_mul, ":var_11", ":var_1_ai_object_town_prosperity"),
						(val_div, ":var_11", 100),
						(val_div, ":var_11", 20),
						(val_add, ":var_1_ai_object_center_accumulated_tariffs", ":var_11"),
						(try_begin),
							(ge, "$cheat_mode", 3),
							(assign, reg4, ":var_11"),
							(str_store_party_name, 4, ":var_1_ai_object"),
							(assign, reg5, ":var_1_ai_object_center_accumulated_tariffs"),
							(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
						(try_end),
						(party_set_slot, ":var_1_ai_object", slot_center_accumulated_tariffs, ":var_1_ai_object_center_accumulated_tariffs"),
						(party_get_slot, ":var_1_ai_object_food_store", ":var_1_ai_object", slot_party_food_store),
						(call_script, "script_center_get_food_store_limit", ":var_1_ai_object"),
						(assign, ":var_13", reg0),
						(val_add, ":var_1_ai_object_food_store", 1000),
						(val_min, ":var_1_ai_object_food_store", ":var_13"),
						(party_set_slot, ":var_1_ai_object", slot_party_food_store, ":var_1_ai_object_food_store"),
						(try_begin),
							(store_random_in_range, ":random_in_range_0_100", 0, 100),
							(lt, ":random_in_range_0_100", 35),
							(call_script, "script_change_center_prosperity", ":var_1_home_center", 1),
							(val_add, "$newglob_total_prosperity_from_village_trade", 1),
						(try_end),
					(try_end),
					(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_home_center"),
					(party_set_slot, ":var_1", slot_party_ai_state, 13),
					(party_set_ai_behavior, ":var_1", 1),
					(party_set_ai_object, ":var_1", ":var_1_home_center"),
				(try_end),
			(try_end)
		]),

	(2.0,
		[
			(try_for_range, ":party", "p_castle_1_1", "p_village_1_1"),
				(party_slot_eq, ":party", slot_center_is_besieged_by, -1),
				(party_get_slot, ":party_food_store", ":party", slot_party_food_store),
				(val_add, ":party_food_store", 100),
				(call_script, "script_center_get_food_store_limit", ":party"),
				(assign, ":var_3", reg0),
				(val_min, ":party_food_store", ":var_3"),
				(party_set_slot, ":party", slot_party_food_store, ":party_food_store"),
			(try_end)
		]),

	(0.2,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_heroes_end"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(gt, ":troop_leaded_party", 0),
				(try_begin),
					(party_is_active, ":troop_leaded_party"),
					(try_begin),
						(get_party_ai_current_behavior, ":party_ai_current_behavior_troop_leaded_party", ":troop_leaded_party"),
						(eq, ":party_ai_current_behavior_troop_leaded_party", 5),
						(assign, ":value", 1),
						(try_begin),
							(this_or_next|troop_slot_eq, ":troop", slot_lord_reputation_type, 7),
							(troop_slot_eq, ":troop", slot_lord_reputation_type, 1),
							(get_party_ai_current_object, ":party_ai_current_object_troop_leaded_party", ":troop_leaded_party"),
							(party_is_active, ":party_ai_current_object_troop_leaded_party"),
							(party_get_battle_opponent, ":battle_opponent_party_ai_current_object_troop_leaded_party", ":party_ai_current_object_troop_leaded_party"),
							(party_is_active, ":battle_opponent_party_ai_current_object_troop_leaded_party"),
							(assign, ":value", 0),
						(try_end),
						(eq, ":value", 1),
						(store_faction_of_party, ":faction_of_party_troop_leaded_party", ":troop_leaded_party"),
						(party_get_slot, ":troop_leaded_party_commander_party", ":troop_leaded_party", slot_party_commander_party),
						(faction_get_slot, ":faction_of_party_troop_leaded_party_marshall", ":faction_of_party_troop_leaded_party", slot_faction_marshall),
						(neq, ":faction_of_party_troop_leaded_party_marshall", ":troop"),
						(assign, ":value", 1),
						(try_begin),
							(ge, ":faction_of_party_troop_leaded_party_marshall", 0),
							(troop_get_slot, ":faction_of_party_troop_leaded_party_marshall_leaded_party", ":faction_of_party_troop_leaded_party_marshall", slot_troop_leaded_party),
							(party_is_active, ":faction_of_party_troop_leaded_party_marshall_leaded_party", 0),
							(eq, ":troop_leaded_party_commander_party", ":faction_of_party_troop_leaded_party_marshall_leaded_party"),
							(assign, ":value", 0),
						(try_end),
						(eq, ":value", 1),
						(assign, ":value_2", 0),
						(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
							(eq, ":value_2", 0),
							(party_slot_eq, ":party", slot_center_is_besieged_by, -1),
							(store_faction_of_party, ":faction_of_party_party", ":party"),
							(store_relation, ":relation_faction_of_party_party_faction_of_party_troop_leaded_party", ":faction_of_party_party", ":faction_of_party_troop_leaded_party"),
							(gt, ":relation_faction_of_party_party_faction_of_party_troop_leaded_party", 0),
							(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_leaded_party_party", ":troop_leaded_party", ":party"),
							(lt, ":distance_to_party_from_party_troop_leaded_party_party", 20),
							(party_get_position, 1, ":troop_leaded_party"),
							(party_get_position, 2, ":party"),
							(neg|position_is_behind_position, 2, 1),
							(call_script, "script_party_set_ai_state", ":troop_leaded_party", 14, ":party"),
							(assign, ":value_2", 1),
						(try_end),
					(try_end),
				(else_try),
					(troop_set_slot, ":troop", slot_troop_leaded_party, -1),
				(try_end),
			(try_end)
		]),

	(0.5,
		[
			(store_current_hours, ":current_hours"),
			(store_mod, ":value", ":current_hours", 11),
			(store_sub, ":value_2", ":current_hours", 5),
			(party_get_num_companions, ":num_companions_main_party", "p_main_party"),
			(party_get_num_prisoners, ":num_prisoners_main_party", "p_main_party"),
			(val_add, ":num_companions_main_party", ":num_prisoners_main_party"),
			(convert_to_fixed_point, ":num_companions_main_party"),
			(store_sqrt, ":value_3", ":num_companions_main_party"),
			(convert_from_fixed_point, ":value_3"),
			(try_begin),
				(eq, ":value", 0),
				(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(faction_get_slot, ":faction_player_alarm", ":script_param_2", slot_faction_player_alarm),
					(val_sub, ":faction_player_alarm", 1),
					(val_max, ":faction_player_alarm", 0),
					(faction_set_slot, ":script_param_2", slot_faction_player_alarm, ":faction_player_alarm"),
				(try_end),
			(try_end),
			(eq, "$g_player_is_captive", 0),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(store_faction_of_party, ":script_param_2", ":party"),
				(store_relation, ":relation_faction_player_supporters_faction", ":script_param_2", "fac_player_supporters_faction"),
				(lt, ":relation_faction_player_supporters_faction", 0),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_main_party_party", "p_main_party", ":party"),
				(lt, ":distance_to_party_from_party_main_party_party", 5),
				(store_mul, ":value_4", ":distance_to_party_from_party_main_party_party", ":distance_to_party_from_party_main_party_party"),
				(store_sub, ":value_5", 20, ":value_4"),
				(store_sub, ":value_6", 20, ":relation_faction_player_supporters_faction"),
				(store_mul, ":value_7", ":value_5", ":value_6"),
				(val_mul, ":value_7", ":value_3"),
				(store_div, ":value_8", ":value_7", 10),
				(store_random_in_range, ":random_in_range_0_1000", 0, 1000),
				(lt, ":random_in_range_0_1000", ":value_8"),
				(faction_get_slot, ":faction_player_alarm", ":script_param_2", slot_faction_player_alarm),
				(val_add, ":faction_player_alarm", 1),
				(val_min, ":faction_player_alarm", 100),
				(faction_set_slot, ":script_param_2", slot_faction_player_alarm, ":faction_player_alarm"),
				(try_begin),
					(neg|party_slot_ge, ":party", 42, ":value_2"),
					(str_store_party_name_link, 1, ":party"),
					(display_message, "@Your party is spotted by {s1}."),
					(party_set_slot, ":party", slot_center_last_player_alarm_hour, ":current_hours"),
				(try_end),
			(try_end)
		]),

	(14.0,
		[
			(eq, "$g_player_is_captive", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(assign, ":var_2", 0),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
				(val_add, ":var_2", ":party_stack_size_main_party_localvariable"),
			(try_end),
			(val_div, ":var_2", 3),
			(try_begin),
				(eq, ":var_2", 0),
				(val_add, ":var_2", 1),
			(try_end),
			(try_begin),
				(assign, ":var_5", 0), #number_of_Food_player_has
				(try_for_range, ":item", "itm_smoked_fish", "itm_siege_supply"), #item = cur_edible
					(call_script, "script_cf_player_has_item_without_modifier", ":item", 41),
					(val_add, ":var_5", 1),
				(try_end),
			(try_end),
			(assign, ":var_7", ":var_2"),
			(assign, ":value", 0), #value = no_food_displayed
			(try_for_range, ":unused", 0, ":var_7"), #var_7 = consumpion_amount
				(assign, ":var_10", 0),
				(try_for_range, ":item_2", "itm_smoked_fish", "itm_siege_supply"), #itm_smoked_fish food_begin, itm_siege_supply = food_end
					(item_set_slot, ":item_2", slot_item_is_checked, 0),
					(call_script, "script_cf_player_has_item_without_modifier", ":item_2", 41), #item_2 = cur_food 41 = imod_rotten
					(val_add, ":var_10", 1),
				(try_end),
				(try_begin),
					(gt, ":var_10", 0), #Available food
					(store_random_in_range, ":random_in_range_0_var_10", 0, ":var_10"), #random_in_range = selected_food
					(call_script, "script_consume_food", ":random_in_range_0_var_10"),
				(else_try),
					(eq, ":value", 0),
					(display_message, "@Party has nothing to eat!", 0x00ff0000),
					(call_script, "script_change_player_party_morale", -3),
		#####Hunger OSP Begin
	    (try_begin),
		(eq, "$hardcore_mode", 1), #Added
        (eq, ":value", 0),
        (eq, "$malus_de_faim", 0),   
        (call_script, "script_hungry-damages_1429"),
 		(display_message, "@I'm feeling weaker, I need food to regain my strength!", 0x00ff0000),
		(try_end),
		#####Hunger OSP End
		(assign, ":value", 1), #default just remove above if you want to get rid of hunger OSP

					(try_begin),
						(call_script, "script_party_count_fit_regulars", "p_main_party"),
						(gt, reg0, 0),
						(call_script, "script_objectionable_action", 2, "str_men_hungry"),
					(try_end),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
			(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
				(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
				(this_or_next|eq, ":inventory_slot_player_localvariable", "itm_cattle_meat"),
				(this_or_next|eq, ":inventory_slot_player_localvariable", "itm_chicken"),
				(eq, ":inventory_slot_player_localvariable", "itm_pork"),
				(troop_get_inventory_slot_modifier, ":inventory_slot_modifier_player_localvariable", "trp_player", ":localvariable"),
				(try_begin),
					(ge, ":inventory_slot_modifier_player_localvariable", 37),
					(lt, ":inventory_slot_modifier_player_localvariable", 41),
					(val_add, ":inventory_slot_modifier_player_localvariable", 1),
					(troop_set_inventory_slot_modifier, "trp_player", ":localvariable", ":inventory_slot_modifier_player_localvariable"),
				(else_try),
					(lt, ":inventory_slot_modifier_player_localvariable", 37),
					(troop_set_inventory_slot_modifier, "trp_player", ":localvariable", 37),
				(try_end),
			(try_end)
		]),

#	(72.0,
#		[]),

	(0.0,
		[
			(troop_get_inventory_slot, ":inventory_slot_player_8", "trp_player", 8),
			(assign, ":value", -1),
			(try_begin),
				(eq, "$g_player_icon_state", 0),
				(try_begin),
					(ge, ":inventory_slot_player_8", 0),
					(assign, ":value", "icon_player_horseman"),
				(else_try),
					(assign, ":value", "icon_player"),
				(try_end),
			(else_try),
				(eq, "$g_player_icon_state", 1),
				(assign, ":value", "icon_camp"),
			(else_try),
				(eq, "$g_player_icon_state", 2),
				(assign, ":value", "icon_ship"),
			(try_end),
			(try_begin),
				(call_script, "script_cf_is_party_on_water", "p_main_party"),
				(assign, ":value", "icon_longship"),
			(try_end),
			(neq, ":value", "$g_player_party_icon"),
			(assign, "$g_player_party_icon", ":value"),
			(party_set_icon, "p_main_party", ":value")
		]),

	(4.0,
		[
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(store_div, ":value", ":troop_gold_player", 100),
			(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
			(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
				(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
				(ge, ":inventory_slot_player_localvariable", 0),
				(try_begin),
					(is_between, ":inventory_slot_player_localvariable", "itm_spice", "itm_siege_supply"),
					(store_item_value, ":item_value_inventory_slot_player_localvariable", ":inventory_slot_player_localvariable"),
					(val_add, ":troop_gold_player", ":item_value_inventory_slot_player_localvariable"),
				(try_end),
			(try_end),
			(val_clamp, ":value", 0, 100),
			(party_set_bandit_attraction, "p_main_party", ":value")
		]),

	(3.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, 2),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "fac_player_supporters_faction"),
				(call_script, "script_activate_player_faction", "trp_player"),
			(try_end)
		]),

	(6.0,
		[
			(gt, "$g_prisoner_recruit_troop_id", 0),
			(gt, "$g_prisoner_recruit_size", 0),
			(gt, "$g_prisoner_recruit_last_time", 0),
			(is_currently_night),
			(try_begin),
				(store_skill_level, ":skill_level_leadership_player", "skl_leadership", "trp_player"),
				(val_mul, ":skill_level_leadership_player", 5),
				(store_sub, ":value", 66, ":skill_level_leadership_player"),
				(gt, ":value", 0),
				(assign, ":value_2", 0),
				(try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(lt, ":random_in_range_0_100", ":value"),
					(val_add, ":value_2", 1),
				(try_end),
				(party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":value_2"),
				(assign, ":value_2", reg0),
				(gt, ":value_2", 0),
				(try_begin),
					(gt, ":value_2", 1),
					(assign, reg2, 1),
				(else_try),
					(assign, reg2, 0),
				(try_end),
				(assign, reg1, ":value_2"),
				(str_store_troop_name_by_count, 1, "$g_prisoner_recruit_troop_id", ":value_2"),
				(display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night."),
			(try_end),
			(assign, "$g_prisoner_recruit_troop_id", 0),
			(assign, "$g_prisoner_recruit_size", 0)
		]),

	(24.0,
		[
			(neq, "$g_ransom_offer_rejected", 1),
			(call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
			(eq, reg0, 0),
			(assign, ":value", "p_village_1_1"),
			(try_for_range, ":party", "p_town_1_1", ":value"),
				(party_slot_eq, ":party", slot_town_lord, "trp_player"),
				(call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":party"),
				(eq, reg0, 1),
				(assign, ":value", 0),
			(try_end)
		]),

	(72.0,
		[
			(assign, "$g_ransom_offer_rejected", 0),
			(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
				(party_get_slot, ":party_town_lord", ":party", slot_town_lord),
				(gt, ":party_town_lord", 0),
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks_party", ":party"),
				(try_for_range_backwards, ":var_4", 0, ":num_prisoner_stacks_party"),
					(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_party_var_4", ":party", ":var_4"),
					(troop_is_hero, ":party_prisoner_stack_troop_id_party_var_4"),
					(troop_slot_eq, ":party_prisoner_stack_troop_id_party_var_4", slot_troop_occupation, 2),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(try_begin),
						(le, ":random_in_range_0_100", 10),
						(call_script, "script_calculate_ransom_amount_for_troop", ":party_prisoner_stack_troop_id_party_var_4"),
						(assign, ":var_7", reg0),
						(troop_get_slot, ":party_town_lord_wealth", ":party_town_lord", slot_troop_wealth),
						(val_add, ":party_town_lord_wealth", ":var_7"),
						(troop_set_slot, ":party_town_lord", slot_troop_wealth, ":party_town_lord_wealth"),
						(party_remove_prisoners, ":party", ":party_prisoner_stack_troop_id_party_var_4", 1),
						(call_script, "script_remove_troop_from_prison", ":party_prisoner_stack_troop_id_party_var_4"),
						(store_faction_of_troop, ":faction_of_troop_party_town_lord", ":party_town_lord"),
						(store_faction_of_troop, ":faction_of_troop_party_prisoner_stack_troop_id_party_var_4", ":party_prisoner_stack_troop_id_party_var_4"),
						(str_store_troop_name, 1, ":party_prisoner_stack_troop_id_party_var_4"),
						(str_store_faction_name, 2, ":faction_of_troop_party_town_lord"),
						(str_store_faction_name, 3, ":faction_of_troop_party_prisoner_stack_troop_id_party_var_4"),
						(store_relation, ":relation_faction_of_troop_party_prisoner_stack_troop_id_party_var_4_players_kingdom", ":faction_of_troop_party_prisoner_stack_troop_id_party_var_4", "$players_kingdom"),
						(try_begin),
							(this_or_next|lt, ":relation_faction_of_troop_party_prisoner_stack_troop_id_party_var_4_players_kingdom", 0),
							(eq, ":faction_of_troop_party_prisoner_stack_troop_id_party_var_4", "$players_kingdom"),
							(display_log_message, "@{s1} of {s3} has been released from captivity."),
						(try_end),
					(try_end),
				(try_end),
			(try_end)
		]),

	(72.0,
		[
			(call_script, "script_update_mercenary_units_of_towns"),
			(call_script, "script_update_ransom_brokers"),
			(call_script, "script_update_tavern_travellers"),
			(call_script, "script_update_tavern_minstrels"),
			(call_script, "script_update_booksellers"),
			(call_script, "script_update_villages_infested_by_bandits"),
			(call_script, "script_update_manor_infested_by_bandits"),
			(eq, "$use_feudal_lance", 0),
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(call_script, "script_update_volunteer_troops_in_village", ":party"),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
				(call_script, "script_update_volunteer_troops_in_village", ":party"),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end),
			(try_for_range, ":party", "p_castle_1_1", "p_village_1_1"),
				(call_script, "script_update_volunteer_troops_in_village", ":party"),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end)
		]),

	(24.0,
		[
			(call_script, "script_update_other_taverngoers")
		]),

	(36.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(this_or_next|party_slot_eq, ":party", slot_party_type, 3),
				(party_slot_eq, ":party", slot_party_type, 4),
				(call_script, "script_center_remove_walker_type_from_walkers", ":party", 1),
				(call_script, "script_center_remove_walker_type_from_walkers", ":party", 2),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(try_begin),
					(lt, ":random_in_range_0_100", 70),
					(neg|party_slot_ge, ":party", 50, 60),
					(call_script, "script_cf_center_get_free_walker", ":party"),
					(call_script, "script_center_set_walker_to_type", ":party", reg0, 1),
				(try_end),
			(try_end)
		]),

	(12.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(party_get_slot, ":party_center_current_improvement", ":party", slot_center_current_improvement),
				(gt, ":party_center_current_improvement", 0),
				(party_get_slot, ":party_center_improvement_end_hour", ":party", slot_center_improvement_end_hour),
				(store_current_hours, ":current_hours"),
				(ge, ":current_hours", ":party_center_improvement_end_hour"),
				(party_set_slot, ":party", ":party_center_current_improvement", 1),
				(party_set_slot, ":party", slot_center_current_improvement, 0),
				(call_script, "script_get_improvement_details", ":party_center_current_improvement"),
				(try_begin),
					(party_slot_eq, ":party", slot_town_lord, "trp_player"),
					(str_store_party_name, 4, ":party"),
					(display_log_message, "@Building of {s0} in {s4} has been completed."),
				(try_end),
				(try_begin),
					(is_between, ":party", "p_village_1_1", "p_salt_mine"),
					(eq, ":party_center_current_improvement", 131),
					(call_script, "script_change_center_prosperity", ":party", 5),
				(try_end),
				(try_begin),
					(is_between, ":party", "p_village_1_1", "p_salt_mine"),
					(eq, ":party_center_current_improvement", 248),
					(party_get_slot, ":party_village_bound_center", ":party", slot_village_bound_center),
					(party_get_position, 0, ":party_village_bound_center"),
					(map_get_land_position_around_position, 1, 0, 3),
					(party_set_position, "p_village_player", 1),
					(party_set_flags, "p_village_player", 256, 0),
					(str_store_party_name, 10, ":party_village_bound_center"),
					(str_store_string, 11, "@{s10} Village"),
					(party_set_name, "p_village_player", 11),
					(party_set_flags, "p_village_player", 256, 0),
					(party_set_slot, "p_village_player", slot_village_bound_center, ":party_village_bound_center"),
					(party_get_slot, ":party_town_center", ":party", slot_town_center),
					(party_set_slot, "p_village_player", slot_town_center, ":party_town_center"),
					(party_get_position, 0, ":party"),
					(map_get_land_position_around_position, 1, 0, 3),
					(party_set_position, "p_castle_player", 1),
					(party_set_flags, "p_castle_player", 256, 0),
					(str_store_party_name, 10, ":party"),
					(str_store_string, 11, "@{s10} Castle"),
					(party_set_name, "p_castle_player", 11),
					(party_set_slot, ":party", slot_village_bound_center, "p_castle_player"),
					(party_set_slot, "p_castle_player", slot_party_type, 2),
					(party_set_slot, "p_village_player", slot_party_type, 4),
					(call_script, "script_give_center_to_faction_aux", "p_castle_player", "$players_kingdom"),
					(call_script, "script_give_center_to_faction_aux", "p_village_player", "$players_kingdom"),
					(try_begin),
						(call_script, "script_cf_get_random_lord_except_king_with_faction", "$players_kingdom"),
						(call_script, "script_give_center_to_lord", "p_village_player", reg0, 0),
					(else_try),
						(call_script, "script_give_center_to_lord", "p_village_player", "trp_player", 0),
					(try_end),
					(call_script, "script_give_center_to_lord", "p_castle_player", "trp_player", 0),
					(call_script, "script_give_center_to_lord", ":party", "trp_player", 0),
					(call_script, "script_update_village_market_towns"),
					(party_get_slot, ":party_center_culture", ":party", slot_center_culture),
					(party_get_slot, ":party_center_original_faction", ":party", slot_center_original_faction),
					(party_set_slot, "p_castle_player", slot_center_culture, ":party_center_culture"),
					(party_set_slot, "p_castle_player", slot_center_original_faction, ":party_center_original_faction"),
					(party_set_slot, "p_village_player", slot_center_culture, ":party_center_culture"),
					(party_set_slot, "p_village_player", slot_center_original_faction, ":party_center_original_faction"),
					(party_get_current_terrain, ":current_terrain_castle_player", "p_castle_player"),
					(try_begin),
						(this_or_next|eq, ":current_terrain_castle_player", 5),
						(eq, ":current_terrain_castle_player", 13),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_desert_tier1"),
						(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(else_try),
						(this_or_next|eq, ":current_terrain_castle_player", 4),
						(eq, ":current_terrain_castle_player", 12),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_castle_player_nordic_1"),
						(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(else_try),
						(eq, "fac_kingdom_10", "$players_kingdom"),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_french_tier1"),
						(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 1),
					(else_try),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_central_europe_tier1"),
						(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(try_end),
					(party_set_slot, "p_village_player", slot_town_center, "scn_village_eastern"),
					(party_set_slot, "p_castle_player", slot_town_castle, "scn_interior_moscow"),
					(party_set_slot, "p_castle_player", slot_town_prison, "scn_castle_prison_eastern"),
					(party_set_slot, "p_village_player", slot_center_original_faction, "$players_kingdom"),
					(party_set_slot, "p_castle_player", slot_center_original_faction, "$players_kingdom"),
					(party_set_slot, "p_village_player", slot_center_accumulated_rents, 0),
					(party_set_slot, "p_village_player", slot_center_accumulated_tariffs, 0),
					(party_set_slot, "p_castle_player", slot_center_accumulated_rents, 0),
					(party_set_slot, "p_castle_player", slot_center_accumulated_tariffs, 0),
					(try_begin),
						(party_clear, "p_castle_player"),
						(remove_member_from_party, "trp_temp_lord", "p_castle_player"),
					(try_end),
				(try_end),
				(party_get_current_terrain, ":current_terrain_castle_player", "p_castle_player"),
				(try_begin),
					(this_or_next|eq, ":current_terrain_castle_player", 5),
					(eq, ":current_terrain_castle_player", 13),
					(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(try_begin),
						(eq, ":party_center_current_improvement", 252),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_desert_tier2"),
					(else_try),
						(eq, ":party_center_current_improvement", 253),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_desert_tier3"),
					(try_end),
				(else_try),
					(this_or_next|eq, ":current_terrain_castle_player", 4),
					(eq, ":current_terrain_castle_player", 12),
					(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(try_begin),
						(eq, ":party_center_current_improvement", 252),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_castle_player_nordic_2"),
					(else_try),
						(eq, ":party_center_current_improvement", 253),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_castle_player_nordic_3"),
					(try_end),
				(else_try),
					(eq, "fac_kingdom_10", "$players_kingdom"),
					(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 1),
					(try_begin),
						(eq, ":party_center_current_improvement", 252),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_french_tier2"),
					(else_try),
						(eq, ":party_center_current_improvement", 253),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_french_tier3"),
					(try_end),
				(else_try),
					(party_set_slot, "p_castle_player", slot_center_siege_with_belfry, 0),
					(try_begin),
						(eq, ":party_center_current_improvement", 252),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_central_europe_tier2"),
					(else_try),
						(eq, ":party_center_current_improvement", 253),
						(party_set_slot, "p_castle_player", slot_town_center, "scn_player_castle_central_europe_tier3"),
					(try_end),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(assign, ":var_1", 0),
			(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
				(party_get_slot, ":party_town_has_tournament", ":party", slot_town_has_tournament),
				(try_begin),
					(eq, ":party_town_has_tournament", 1),
					(call_script, "script_fill_tournament_participants_troop", ":party", 0),
					(call_script, "script_sort_tournament_participant_troops"),
					(call_script, "script_get_num_tournament_participants"),
					(store_sub, ":value", reg0, 1),
					(call_script, "script_remove_tournament_participants_randomly", ":value"),
					(call_script, "script_sort_tournament_participant_troops"),
					(troop_get_slot, ":tournament_participants_relations_begin", "trp_tournament_participants", slot_troop_relations_begin),
					(try_begin),
						(is_between, ":tournament_participants_relations_begin", "trp_npc1", "trp_knight_1_1_wife"),
						(str_store_troop_name_link, 1, ":tournament_participants_relations_begin"),
						(str_store_party_name_link, 2, ":party"),
						(display_message, "@{s1} has won the tournament at {s2}."),
						(call_script, "script_change_troop_renown", ":tournament_participants_relations_begin", 20),
					(try_end),
				(try_end),
				(val_sub, ":party_town_has_tournament", 1),
				(val_max, ":party_town_has_tournament", 0),
				(party_set_slot, ":party", slot_town_has_tournament, ":party_town_has_tournament"),
				(try_begin),
					(gt, ":party_town_has_tournament", 0),
					(val_add, ":var_1", 1),
				(try_end),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(this_or_next|party_slot_eq, ":party", slot_party_type, 3),
				(party_slot_eq, ":party", slot_party_type, 4),
				(party_get_slot, ":party_center_has_bandits", ":party", slot_center_has_bandits),
				(try_begin),
					(le, ":party_center_has_bandits", 0),
					(assign, ":value_2", 0),
					(try_begin),
						(check_quest_active, "qst_deal_with_night_bandits"),
						(quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, ":party"),
						(neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
						(assign, ":value_2", 1),
					(else_try),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(lt, ":random_in_range_0_100", 3),
						(assign, ":value_2", 1),
					(try_end),
					(try_begin),
						(eq, ":value_2", 1),
						(store_random_in_range, ":random_in_range_0_100", 0, 3),
						(try_begin),
							(eq, ":random_in_range_0_100", 0),
							(assign, ":value_3", "trp_bandit"),
						(else_try),
							(eq, ":random_in_range_0_100", 1),
							(assign, ":value_3", "trp_mountain_bandit"),
						(else_try),
							(assign, ":value_3", "trp_forest_bandit"),
						(try_end),
						(party_set_slot, ":party", slot_center_has_bandits, ":value_3"),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_party_name, 1, ":party"),
							(display_message, "@{!}{s1} is infested by bandits (at night)."),
						(try_end),
					(try_end),
				(else_try),
					(try_begin),
						(assign, ":value_4", 40),
						(try_begin),
							(party_slot_eq, ":party", slot_party_type, 3),
							(assign, ":value_4", 20),
						(try_end),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(lt, ":random_in_range_0_100", ":value_4"),
						(party_set_slot, ":party", slot_center_has_bandits, 0),
						(try_begin),
							(eq, "$cheat_mode", 1),
							(str_store_party_name, 1, ":party"),
							(display_message, "@{s1} is no longer infested by bandits (at night)."),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_slot_eq, ":script_param_2", slot_faction_ai_state, 6),
				(faction_get_slot, ":faction_ai_object", ":script_param_2", slot_faction_ai_object),
				(is_between, ":faction_ai_object", "p_town_1_1", "p_castle_1_1"),
				(party_slot_ge, ":faction_ai_object", 156, 1),
				(party_set_slot, ":faction_ai_object", slot_town_has_tournament, 2),
			(try_end),
			(try_begin),
				(lt, ":var_1", 3),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(lt, ":random_in_range_0_100", 5),
				(store_random_in_range, ":random_in_range_town_1_1_castle_1_1", "p_town_1_1", "p_castle_1_1"),
				(store_random_in_range, ":random_in_range_12_15", 12, 15),
				(party_set_slot, ":random_in_range_town_1_1_castle_1_1", slot_town_has_tournament, ":random_in_range_12_15"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_party_name, 1, ":random_in_range_town_1_1_castle_1_1"),
					(display_message, "@{!}{s1} is holding a tournament."),
				(try_end),
			(try_end)
		]),

	(3.0,
		[
			(assign, "$g_player_tournament_placement", 0)
		]),

#	(8.0,
#		[]),

	(1.0,
		[
			(neg|map_free),
			(is_currently_night),
			(is_between, "$g_last_rest_center", "p_town_1_1", "p_salt_mine"),
			(neg|party_slot_eq, "$g_last_rest_center", slot_town_lord, "trp_player"),
			(store_faction_of_party, ":faction_of_party_g_last_rest_center", "$g_last_rest_center"),
			(neq, ":faction_of_party_g_last_rest_center", "fac_player_supporters_faction"),
			(store_current_hours, ":current_hours"),
			(ge, ":current_hours", "$g_last_rest_payment_until"),
			(store_add, "$g_last_rest_payment_until", ":current_hours", 24),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(party_get_num_companions, ":num_companions_main_party", "p_main_party"),
			(store_div, ":value", ":num_companions_main_party", 4),
			(val_add, ":value", 1),
			(try_begin),
				(ge, ":troop_gold_player", ":value"),
				(display_message, "@You pay for accommodation."),
				(troop_remove_gold, "trp_player", ":value"),
			(else_try),
				(gt, ":troop_gold_player", 0),
				(troop_remove_gold, "trp_player", ":troop_gold_player"),
			(try_end)
		]),

	(36.0,
		[
			(call_script, "script_spawn_bandits"),
			(call_script, "script_spawn_balts"),
			(call_script, "script_spawn_peasant_rebels"),
			(try_begin),
				(call_script, "script_cf_spawn_crusaders_and_jihadists"),
			(try_end)
		]),

	(24.0,
		[
			(call_script, "script_update_party_creation_random_limits")
		]),

	(24.0,
		[
			(assign, ":var_1", 0),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_set_slot, ":script_param_2", slot_faction_number_of_parties, 0),
			(try_end),
			(try_for_parties, ":value"),
				(store_faction_of_party, ":faction_of_party_value", ":value"),
				(is_between, ":faction_of_party_value", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(this_or_next|is_between, ":value", "p_town_1_1", "p_salt_mine"),
				(party_slot_eq, ":value", slot_party_type, 13),
				(faction_get_slot, ":faction_of_party_value_number_of_parties", ":faction_of_party_value", slot_faction_number_of_parties),
				(val_add, ":faction_of_party_value_number_of_parties", 1),
				(faction_set_slot, ":faction_of_party_value", slot_faction_number_of_parties, ":faction_of_party_value_number_of_parties"),
			(try_end),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_slot_eq, ":script_param_2", slot_faction_state, 0),
				(val_add, ":var_1", 1),
				(faction_slot_eq, ":script_param_2", slot_faction_number_of_parties, 0),
				(assign, ":value_2", 0),
				(try_begin),
					(eq, ":script_param_2", "fac_player_supporters_faction"),
					(try_begin),
						(le, "$supported_pretender", 0),
						(faction_set_slot, ":script_param_2", slot_faction_state, 2),
						(assign, ":value_2", 1),
					(try_end),
				(else_try),
					(neq, "$players_kingdom", ":script_param_2"),
					(faction_set_slot, ":script_param_2", slot_faction_state, 1),
					(try_for_parties, ":value"),
						(store_faction_of_party, ":faction_of_party_value", ":value"),
						(eq, ":faction_of_party_value", ":script_param_2"),
						(party_get_slot, ":value_home_center", ":value", slot_party_home_center),
						(store_faction_of_party, ":faction_of_party_value_home_center", ":value_home_center"),
						(party_set_faction, ":value", ":faction_of_party_value_home_center"),
					(try_end),
					(assign, ":value_3", -1),
					(try_for_range, ":troop", "trp_kingdom_1_pretender", "trp_knight_1_1"),
						(troop_slot_eq, ":troop", slot_troop_original_faction, ":script_param_2"),
						(assign, ":value_3", ":troop"),
					(try_end),
					(try_begin),
						(is_between, ":value_3", "trp_kingdom_1_pretender", "trp_knight_1_1"),
						(neq, ":value_3", "$supported_pretender"),
						(troop_set_slot, ":value_3", slot_troop_cur_center, 0),
					(try_end),
					(assign, ":value_2", 1),
					(try_begin),
						(eq, "$players_oath_renounced_against_kingdom", ":script_param_2"),
						(assign, "$players_oath_renounced_against_kingdom", 0),
						(assign, "$players_oath_renounced_given_center", 0),
						(assign, "$players_oath_renounced_begin_time", 0),
						(call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":script_param_2", 0),
					(try_end),
					(call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":script_param_2", 0),
				(try_end),
				(try_begin),
					(eq, ":value_2", 1),
					(val_sub, ":var_1", 1),
				(try_end),
				(try_for_range, ":faction_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(call_script, "script_update_faction_notes", ":faction_2"),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":var_1", 1),
				(eq, "$g_one_faction_left_notification_shown", 0),
				(assign, "$g_one_faction_left_notification_shown", 1),
				(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(faction_slot_eq, ":script_param_2", slot_faction_state, 0),
					(call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":script_param_2", 0),
				(try_end),
			(try_end)
		]),

	(3.0,
		[
			(try_begin),
				(is_between, "$g_player_court", "p_town_1_1", "p_salt_mine"),
				(party_slot_eq, "$g_player_court", slot_village_infested_by_bandits, "trp_peasant_woman"),
				(call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
			(else_try),
				(is_between, "$g_player_court", "p_town_1_1", "p_salt_mine"),
				(store_faction_of_party, ":faction_of_party_g_player_court", "$g_player_court"),
				(neq, ":faction_of_party_g_player_court", "fac_player_supporters_faction"),
				(call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
			(else_try),
				(lt, "$g_player_court", "p_town_1_1"),
				(this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(gt, "$g_player_minister", 0),
				(assign, ":value", 0),
				(try_for_range, ":party", "p_town_1_1", "p_village_1_1"),
					(eq, ":value", 0),
					(store_faction_of_party, ":faction_of_party_g_player_court", ":party"),
					(eq, ":faction_of_party_g_player_court", "fac_player_supporters_faction"),
					(assign, ":value", ":party"),
				(try_end),
				(ge, ":value", 1),
				(call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
			(try_end),
			(try_for_parties, ":var_4"),
				(gt, ":var_4", "p_spawn_points_end"),
				(party_get_template_id, ":template_id_var_4", ":var_4"),
				(is_between, ":template_id_var_4", "pt_steppe_bandits", "pt_deserters"),
				(party_template_get_slot, ":party_template_slot_template_id_var_4_party_template_lair_party", ":template_id_var_4", slot_party_template_lair_party),
				(try_begin),
					(gt, ":party_template_slot_template_id_var_4_party_template_lair_party", "p_spawn_points_end"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_var_4_party_template_slot_template_id_var_4_party_template_lair_party", ":var_4", ":party_template_slot_template_id_var_4_party_template_lair_party"),
					(gt, ":distance_to_party_from_party_var_4_party_template_slot_template_id_var_4_party_template_lair_party", 30),
					(lt, ":distance_to_party_from_party_var_4_party_template_slot_template_id_var_4_party_template_lair_party", 35),
					(party_set_ai_behavior, ":var_4", 6),
					(party_get_position, 5, ":party_template_slot_template_id_var_4_party_template_lair_party"),
					(party_set_ai_target_position, ":var_4", 5),
				(else_try),
					(get_party_ai_behavior, ":party_ai_behavior_var_4", ":var_4"),
					(eq, ":party_ai_behavior_var_4", 6),
					(try_begin),
						(gt, ":party_template_slot_template_id_var_4_party_template_lair_party", "p_spawn_points_end"),
						(store_distance_to_party_from_party, ":distance_to_party_from_party_var_4_party_template_slot_template_id_var_4_party_template_lair_party", ":var_4", ":party_template_slot_template_id_var_4_party_template_lair_party"),
						(lt, ":distance_to_party_from_party_var_4_party_template_slot_template_id_var_4_party_template_lair_party", 3),
						(party_set_ai_behavior, ":var_4", 3),
						(party_template_get_slot, ":party_template_slot_template_id_var_4_party_template_lair_spawnpoint", ":template_id_var_4", slot_party_template_lair_spawnpoint),
						(party_set_ai_object, ":var_4", ":party_template_slot_template_id_var_4_party_template_lair_spawnpoint"),
						(party_set_ai_patrol_radius, ":var_4", 45),
					(else_try),
						(lt, ":party_template_slot_template_id_var_4_party_template_lair_party", "p_spawn_points_end"),
						(party_set_ai_behavior, ":var_4", 3),
						(party_template_get_slot, ":party_template_slot_template_id_var_4_party_template_lair_spawnpoint", ":template_id_var_4", slot_party_template_lair_spawnpoint),
						(party_set_ai_object, ":var_4", ":party_template_slot_template_id_var_4_party_template_lair_spawnpoint"),
						(party_set_ai_patrol_radius, ":var_4", 45),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(troop_get_slot, ":player_betrothed", "trp_player", slot_troop_betrothed),
				(gt, ":player_betrothed", 0),
				(neg|check_quest_active, "qst_wed_betrothed"),
				(neg|check_quest_active, "qst_wed_betrothed_female"),
				(str_store_troop_name, 5, ":player_betrothed"),
				(display_message, "@Betrothal to {s5} expires"),
				(troop_set_slot, "trp_player", slot_troop_betrothed, -1),
				(troop_set_slot, ":player_betrothed", slot_troop_betrothed, -1),
			(try_end)
		]),

	(168.0,
		[
			(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
			(store_div, ":value", ":player_renown", 200),
			(val_sub, ":player_renown", ":value"),
			(troop_set_slot, "trp_player", slot_troop_renown, ":player_renown")
		]),

	(1.0,
		[
			(neg|map_free),
			(gt, "$g_player_reading_book", 0),
			(player_has_item, "$g_player_reading_book"),
			(store_attribute_level, ":attribute_level_player_2", "trp_player", 2),
			(item_get_slot, ":g_player_reading_book_intelligence_requirement", "$g_player_reading_book", slot_item_intelligence_requirement),
			(le, ":g_player_reading_book_intelligence_requirement", ":attribute_level_player_2"),
			(item_get_slot, ":g_player_reading_book_book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
			(item_get_slot, ":g_player_reading_book_book_read", "$g_player_reading_book", slot_item_book_read),
			(eq, ":g_player_reading_book_book_read", 0),
			(val_add, ":g_player_reading_book_book_reading_progress", 7),
			(item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":g_player_reading_book_book_reading_progress"),
			(ge, ":g_player_reading_book_book_reading_progress", 1000),
			(item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
			(str_store_item_name, 1, "$g_player_reading_book"),
			(str_clear, 2),
			(try_begin),
				(eq, "$g_player_reading_book", "itm_book_tactics"),
				(troop_raise_skill, "trp_player", "skl_tactics", 1),
				(str_store_string, 2, "@ Your tactics skill has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_persuasion"),
				(troop_raise_skill, "trp_player", "skl_persuasion", 1),
				(str_store_string, 2, "@ Your persuasion skill has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_leadership"),
				(troop_raise_skill, "trp_player", "skl_leadership", 1),
				(str_store_string, 2, "@ Your leadership skill has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_intelligence"),
				(troop_raise_attribute, "trp_player", 2, 1),
				(str_store_string, 2, "@ Your intelligence has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_trade"),
				(troop_raise_skill, "trp_player", "skl_trade", 1),
				(str_store_string, 2, "@ Your trade skill has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
				(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
				(str_store_string, 2, "@ Your weapon master skill has increased by 1."),
			(else_try),
				(eq, "$g_player_reading_book", "itm_book_engineering"),
				(troop_raise_skill, "trp_player", "skl_engineer", 1),
				(str_store_string, 2, "@ Your engineer skill has increased by 1."),
			(try_end),
			(unlock_achievement, 37),
			(try_begin),
				(eq, "$g_infinite_camping", 0),
				(dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
			(try_end),
			(assign, "$g_player_reading_book", 0)
		]),

	(12.0,
		[
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 17),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_main_party", ":var_1", "p_main_party"),
				(try_begin),
					(gt, ":distance_to_party_from_party_var_1_main_party", 30),
					(remove_party, ":var_1"),
					(try_begin),
						(check_quest_active, "qst_move_cattle_herd"),
						(neg|check_quest_concluded, "qst_move_cattle_herd"),
						(quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":var_1"),
						(call_script, "script_fail_quest", "qst_move_cattle_herd"),
					(try_end),
				(else_try),
					(gt, ":distance_to_party_from_party_var_1_main_party", 10),
					(party_set_slot, ":var_1", slot_town_lord, 0),
					(party_set_ai_behavior, ":var_1", 0),
				(try_end),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_town_lord, "trp_player"),
				(party_slot_eq, ":party", slot_center_has_school, 1),
				(party_get_slot, ":party_center_player_relation", ":party", slot_center_player_relation),
				(val_add, ":party_center_player_relation", 1),
				(val_min, ":party_center_player_relation", 100),
				(party_set_slot, ":party", slot_center_player_relation, ":party_center_player_relation"),
			(try_end)
		]),

	(24.0,
		[
			(try_for_range, ":quest", 0, "qst_quests_end"),
				(try_begin),
					(check_quest_active, ":quest"),
					(try_begin),
						(neg|check_quest_concluded, ":quest"),
						(quest_slot_ge, ":quest", 23, 1),
						(quest_get_slot, ":quest_expiration_days", ":quest", slot_quest_expiration_days),
						(val_sub, ":quest_expiration_days", 1),
						(try_begin),
							(eq, ":quest_expiration_days", 0),
							(call_script, "script_abort_quest", ":quest", 1),
						(else_try),
							(quest_set_slot, ":quest", slot_quest_expiration_days, ":quest_expiration_days"),
							(assign, reg0, ":quest_expiration_days"),
							(add_quest_note_from_sreg, ":quest", 7, "@You have {reg0} days to finish this quest.", 0),
						(try_end),
					(try_end),
				(else_try),
					(quest_slot_ge, ":quest", 25, 1),
					(quest_get_slot, ":quest_dont_give_again_remaining_days", ":quest", slot_quest_dont_give_again_remaining_days),
					(val_sub, ":quest_dont_give_again_remaining_days", 1),
					(quest_set_slot, ":quest", slot_quest_dont_give_again_remaining_days, ":quest_dont_give_again_remaining_days"),
				(try_end),
			(try_end)
		]),

	(2.0,
		[
			(eq, "$g_infinite_camping", 0),
			(eq, "$g_player_crusading", 0),
			(is_between, "$players_kingdom", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(eq, "$g_player_is_captive", 0),
			(try_begin),
				(check_quest_active, "qst_report_to_army"),
				(faction_slot_eq, "$players_kingdom", slot_faction_marshall, -1),
				(call_script, "script_abort_quest", "qst_report_to_army", 0),
			(try_end),
			(faction_get_slot, ":players_kingdom_ai_object", "$players_kingdom", slot_faction_ai_object),
			(neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 0),
			(neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 6),
			(assign, ":value", 1),
			(try_begin),
				(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 5),
				(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 2),
				(faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 3),
				(neg|is_between, ":players_kingdom_ai_object", "p_town_1_1", "p_village_1_1"),
				(assign, ":value", 0),
			(try_end),
			(eq, ":value", 1),
			(assign, ":value_2", 0),
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(neq, ":script_param_2", "$players_kingdom"),
				(store_relation, ":relation_faction_players_kingdom", ":script_param_2", "$players_kingdom"),
				(lt, ":relation_faction_players_kingdom", 0),
				(assign, ":value_2", 1),
			(try_end),
			(eq, ":value_2", 1),
			(neg|check_quest_active, "qst_report_to_army"),
			(neg|check_quest_active, "qst_follow_army"),
			(neg|quest_slot_ge, "qst_report_to_army", 25, 1),
			(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
			(gt, ":players_kingdom_marshall", 0),
			(troop_get_slot, ":players_kingdom_marshall_leaded_party", ":players_kingdom_marshall", slot_troop_leaded_party),
			(gt, ":players_kingdom_marshall_leaded_party", 0),
			(party_is_active, ":players_kingdom_marshall_leaded_party"),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_players_kingdom_marshall_leaded_party_main_party", ":players_kingdom_marshall_leaded_party", "p_main_party"),
			(le, ":distance_to_party_from_party_players_kingdom_marshall_leaded_party_main_party", 96),
			(assign, ":value_3", 1),
			(try_for_range, ":quest", "qst_deliver_message", "qst_follow_army"),
				(check_quest_active, ":quest"),
				(quest_slot_eq, ":quest", slot_quest_giver_troop, ":players_kingdom_marshall"),
				(assign, ":value_3", 0),
			(try_end),
			(eq, ":value_3", 1),
			(try_for_range, ":quest", "qst_destroy_bandit_lair", "qst_blank_quest_2"),
				(check_quest_active, ":quest"),
				(quest_slot_eq, ":quest", slot_quest_giver_troop, ":players_kingdom_marshall"),
				(assign, ":value_3", 0),
			(try_end),
			(eq, ":value_3", 1),
			(try_for_range, ":quest", "qst_deliver_cattle_to_army", "qst_rescue_lord_by_replace"),
				(check_quest_active, ":quest"),
				(assign, ":value_3", 0),
			(try_end),
			(eq, ":value_3", 1),
			(store_character_level, ":character_level_player", "trp_player"),
			(ge, ":character_level_player", 8),
			(assign, ":var_12", 2),
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(party_slot_eq, ":party", slot_town_lord, "trp_player"),
				(try_begin),
					(party_slot_eq, ":party", slot_party_type, 3),
					(val_add, ":var_12", 3),
				(else_try),
					(party_slot_eq, ":party", slot_party_type, 2),
					(val_add, ":var_12", 1),
				(else_try),
					(val_add, ":var_12", 1),
				(try_end),
			(try_end),
			(val_mul, ":var_12", 4),
			(val_min, ":var_12", 60),
			(quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":players_kingdom_marshall"),
			(quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":players_kingdom_marshall"),
			(quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":var_12"),
			(quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
			(quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 15),
			(jump_to_menu, "mnu_kingdom_army_quest_report_to_army")
		]),

	(3.0,
		[
			(assign, "$g_random_army_quest", -1),
			(check_quest_active, "qst_follow_army", 1),
			(is_between, "$players_kingdom", "fac_player_supporters_faction", "fac_kingdoms_end"),
			(neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 0),
			(faction_get_slot, ":players_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
			(neq, ":players_kingdom_marshall", "trp_player"),
			(gt, ":players_kingdom_marshall", 0),
			(troop_get_slot, ":players_kingdom_marshall_leaded_party", ":players_kingdom_marshall", slot_troop_leaded_party),
			(gt, ":players_kingdom_marshall_leaded_party", 0),
			(party_is_active, ":players_kingdom_marshall_leaded_party"),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_players_kingdom_marshall_leaded_party_main_party", ":players_kingdom_marshall_leaded_party", "p_main_party"),
			(try_begin),
				(lt, ":distance_to_party_from_party_players_kingdom_marshall_leaded_party_main_party", 15),
				(assign, "$g_player_follow_army_warnings", 0),
				(store_current_hours, ":current_hours"),
				(faction_get_slot, ":players_kingdom_ai_last_offensive_time", "$players_kingdom", slot_faction_ai_last_offensive_time),
				(store_sub, ":value", ":current_hours", ":players_kingdom_ai_last_offensive_time"),
				(assign, ":value_2", -1),
				(try_begin),
					(store_random_in_range, ":random_in_range_0_100", 0, 100),
					(lt, ":random_in_range_0_100", 30),
					(troop_slot_eq, ":players_kingdom_marshall", slot_troop_does_not_give_quest, 0),
					(try_for_range, ":unused", 0, 20),
						(eq, ":value_2", -1),
						(store_random_in_range, ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace", "qst_deliver_cattle_to_army", "qst_rescue_lord_by_replace"),
						(neg|quest_slot_ge, ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace", 25, 1),
						(try_begin),
							(eq, ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace", "qst_deliver_cattle_to_army"),
							(try_begin),
								(faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 2),
								(gt, ":value", 120),
								(store_random_in_range, ":random_in_range_5_10", 5, 10),
								(assign, ":value_2", "qst_deliver_cattle_to_army"),
								(quest_set_slot, ":value_2", slot_quest_target_amount, ":random_in_range_5_10"),
								(quest_set_slot, ":value_2", slot_quest_expiration_days, 10),
								(quest_set_slot, ":value_2", slot_quest_dont_give_again_period, 30),
							(try_end),
						(else_try),
							(eq, ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace", "qst_join_siege_with_army"),
							(eq, 1, 0),
							(try_begin),
								(faction_slot_eq, "$players_kingdom", slot_faction_ai_state, 2),
								(faction_get_slot, ":players_kingdom_ai_object", "$players_kingdom", slot_faction_ai_object),
								(is_between, ":players_kingdom_ai_object", "p_town_1_1", "p_village_1_1"),
								(party_get_battle_opponent, ":battle_opponent_players_kingdom_marshall_leaded_party", ":players_kingdom_marshall_leaded_party"),
								(eq, ":battle_opponent_players_kingdom_marshall_leaded_party", ":players_kingdom_ai_object"),
								(assign, ":value_2", ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace"),
								(quest_set_slot, ":value_2", slot_quest_target_center, ":players_kingdom_ai_object"),
								(quest_set_slot, ":value_2", slot_quest_expiration_days, 2),
								(quest_set_slot, ":value_2", slot_quest_dont_give_again_period, 15),
							(try_end),
						(else_try),
							(eq, ":random_in_range_deliver_cattle_to_army_rescue_lord_by_replace", "qst_scout_waypoints"),
							(try_begin),
								(assign, ":value_3", 100),
								(assign, "$qst_scout_waypoints_wp_1", -1),
								(assign, "$qst_scout_waypoints_wp_2", -1),
								(assign, "$qst_scout_waypoints_wp_3", -1),
								(assign, ":value_4", 0),
								(try_for_range, ":unused", 0, ":value_3"),
									(try_begin),
										(lt, "$qst_scout_waypoints_wp_1", 0),
										(call_script, "script_cf_get_random_enemy_center_within_range", ":players_kingdom_marshall_leaded_party", 50),
										(assign, "$qst_scout_waypoints_wp_1", reg0),
									(try_end),
									(try_begin),
										(lt, "$qst_scout_waypoints_wp_2", 0),
										(call_script, "script_cf_get_random_enemy_center_within_range", ":players_kingdom_marshall_leaded_party", 50),
										(neq, "$qst_scout_waypoints_wp_1", reg0),
										(assign, "$qst_scout_waypoints_wp_2", reg0),
									(try_end),
									(try_begin),
										(lt, "$qst_scout_waypoints_wp_3", 0),
										(call_script, "script_cf_get_random_enemy_center_within_range", ":players_kingdom_marshall_leaded_party", 50),
										(neq, "$qst_scout_waypoints_wp_1", reg0),
										(neq, "$qst_scout_waypoints_wp_2", reg0),
										(assign, "$qst_scout_waypoints_wp_3", reg0),
									(try_end),
									(neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
									(neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
									(neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
									(ge, "$qst_scout_waypoints_wp_1", 0),
									(ge, "$qst_scout_waypoints_wp_2", 0),
									(ge, "$qst_scout_waypoints_wp_3", 0),
									(assign, ":value_3", 0),
									(assign, ":value_4", 1),
								(try_end),
								(eq, ":value_4", 1),
								(assign, "$qst_scout_waypoints_wp_1_visited", 0),
								(assign, "$qst_scout_waypoints_wp_2_visited", 0),
								(assign, "$qst_scout_waypoints_wp_3_visited", 0),
								(assign, ":value_2", "qst_scout_waypoints"),
								(quest_set_slot, ":value_2", slot_quest_expiration_days, 7),
								(quest_set_slot, ":value_2", slot_quest_dont_give_again_period, 25),
							(try_end),
						(try_end),
					(try_end),
					(try_begin),
						(neq, ":value_2", -1),
						(quest_set_slot, ":value_2", slot_quest_current_state, 0),
						(quest_set_slot, ":value_2", slot_quest_giver_troop, ":players_kingdom_marshall"),
						(try_begin),
							(eq, ":value_2", "qst_join_siege_with_army"),
							(jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
						(else_try),
							(assign, "$g_random_army_quest", ":value_2"),
							(quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":players_kingdom_marshall"),
							(jump_to_menu, "mnu_kingdom_army_quest_messenger"),
						(try_end),
					(try_end),
				(try_end),
			(else_try),
				(val_add, "$g_player_follow_army_warnings", 1),
				(try_begin),
					(lt, "$g_player_follow_army_warnings", 15),
					(try_begin),
						(store_mod, ":value_5", "$g_player_follow_army_warnings", 3),
						(eq, ":value_5", 0),
						(str_store_troop_name_link, 1, ":players_kingdom_marshall"),
						(try_begin),
							(lt, "$g_player_follow_army_warnings", 8),
						(else_try),
							(display_message, "str_marshal_warning"),
						(try_end),
					(try_end),
				(else_try),
					(jump_to_menu, "mnu_kingdom_army_follow_failed"),
				(try_end),
			(try_end)
		]),

	(0.5,
		[
			(check_quest_active, "qst_move_cattle_herd"),
			(neg|check_quest_concluded, "qst_move_cattle_herd"),
			(quest_get_slot, ":move_cattle_herd_target_party", "qst_move_cattle_herd", slot_quest_target_party),
			(quest_get_slot, ":move_cattle_herd_target_center", "qst_move_cattle_herd", slot_quest_target_center),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_move_cattle_herd_target_party_move_cattle_herd_target_center", ":move_cattle_herd_target_party", ":move_cattle_herd_target_center"),
			(lt, ":distance_to_party_from_party_move_cattle_herd_target_party_move_cattle_herd_target_center", 3),
			(remove_party, ":move_cattle_herd_target_party"),
			(call_script, "script_succeed_quest", "qst_move_cattle_herd")
		]),

	(2.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_eq, ":troop", slot_troop_occupation, 2),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(ge, ":troop_leaded_party", 1),
				(party_is_active, ":troop_leaded_party"),
				(party_slot_eq, ":troop_leaded_party", slot_party_following_player, 1),
				(store_current_hours, ":current_hours"),
				(neg|party_slot_ge, ":troop_leaded_party", 32, ":current_hours"),
				(party_set_slot, ":troop_leaded_party", slot_party_commander_party, -1),
				(party_set_slot, ":troop_leaded_party", slot_party_following_player, 0),
				(assign, ":var_4", 200),
				(store_add, ":value", ":current_hours", ":var_4"),
				(party_set_slot, ":troop_leaded_party", slot_party_dont_follow_player_until_time, ":value"),
			(try_end)
		]),

	(0.5,
		[
			(try_begin),
				(check_quest_active, "qst_deliver_cattle"),
				(neg|check_quest_succeeded, "qst_deliver_cattle"),
				(quest_get_slot, ":deliver_cattle_target_center", "qst_deliver_cattle", slot_quest_target_center),
				(quest_get_slot, ":deliver_cattle_target_amount", "qst_deliver_cattle", slot_quest_target_amount),
				(quest_get_slot, ":deliver_cattle_current_state", "qst_deliver_cattle", slot_quest_current_state),
				(store_sub, ":value", ":deliver_cattle_target_amount", ":deliver_cattle_current_state"),
				(call_script, "script_remove_cattles_if_herd_is_close_to_party", ":deliver_cattle_target_center", ":value"),
				(val_add, ":deliver_cattle_current_state", reg0),
				(quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":deliver_cattle_current_state"),
				(le, ":deliver_cattle_target_amount", ":deliver_cattle_current_state"),
				(call_script, "script_succeed_quest", "qst_deliver_cattle"),
			(try_end),
			(try_begin),
				(check_quest_active, "qst_deliver_cattle_to_army"),
				(neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
				(quest_get_slot, ":deliver_cattle_to_army_giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
				(troop_get_slot, ":deliver_cattle_to_army_giver_troop_leaded_party", ":deliver_cattle_to_army_giver_troop", slot_troop_leaded_party),
				(try_begin),
					(gt, ":deliver_cattle_to_army_giver_troop_leaded_party", 0),
					(quest_get_slot, ":deliver_cattle_target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
					(quest_get_slot, ":deliver_cattle_current_state", "qst_deliver_cattle_to_army", slot_quest_current_state),
					(store_sub, ":value", ":deliver_cattle_target_amount", ":deliver_cattle_current_state"),
					(call_script, "script_remove_cattles_if_herd_is_close_to_party", ":deliver_cattle_to_army_giver_troop_leaded_party", ":value"),
					(val_add, ":deliver_cattle_current_state", reg0),
					(quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":deliver_cattle_current_state"),
					(try_begin),
						(le, ":deliver_cattle_target_amount", ":deliver_cattle_current_state"),
						(call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
					(try_end),
				(else_try),
					(call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
				(try_end),
			(try_end)
		]),

	(1.0,
		[
			(neg|map_free),
			(check_quest_active, "qst_train_peasants_against_bandits"),
			(neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
			(eq, "$qst_train_peasants_against_bandits_currently_training", 1),
			(val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
			(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
			(assign, ":var_1", reg0),
			(store_sub, ":value", 20, ":var_1"),
			(val_mul, ":value", 3),
			(val_div, ":value", 5),
			(ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":value"),
			(assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
			(rest_for_hours, 0, 0, 0),
			(jump_to_menu, "mnu_train_peasants_against_bandits_ready")
		]),

	(1.0,
		[
			(check_quest_active, "qst_scout_waypoints"),
			(neg|check_quest_succeeded, "qst_scout_waypoints"),
			(try_begin),
				(eq, "$qst_scout_waypoints_wp_1_visited", 0),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", "$qst_scout_waypoints_wp_1", "p_main_party"),
				(le, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", 3),
				(assign, "$qst_scout_waypoints_wp_1_visited", 1),
				(str_store_party_name_link, 1, "$qst_scout_waypoints_wp_1"),
				(display_message, "@{s1} is scouted."),
			(try_end),
			(try_begin),
				(eq, "$qst_scout_waypoints_wp_2_visited", 0),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", "$qst_scout_waypoints_wp_2", "p_main_party"),
				(le, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", 3),
				(assign, "$qst_scout_waypoints_wp_2_visited", 1),
				(str_store_party_name_link, 1, "$qst_scout_waypoints_wp_2"),
				(display_message, "@{s1} is scouted."),
			(try_end),
			(try_begin),
				(eq, "$qst_scout_waypoints_wp_3_visited", 0),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", "$qst_scout_waypoints_wp_3", "p_main_party"),
				(le, ":distance_to_party_from_party_qst_scout_waypoints_wp_1_main_party", 3),
				(assign, "$qst_scout_waypoints_wp_3_visited", 1),
				(str_store_party_name_link, 1, "$qst_scout_waypoints_wp_3"),
				(display_message, "@{s1} is scouted."),
			(try_end),
			(eq, "$qst_scout_waypoints_wp_1_visited", 1),
			(eq, "$qst_scout_waypoints_wp_2_visited", 1),
			(eq, "$qst_scout_waypoints_wp_3_visited", 1),
			(call_script, "script_succeed_quest", "qst_scout_waypoints")
		]),

	(3.0,
		[
			(neg|map_free),
			(check_quest_active, "qst_kill_local_merchant"),
			(quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
			(quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
			(rest_for_hours, 0, 0, 0),
			(assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
			(assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin")
		]),

	(1.0,
		[
			(neg|map_free),
			(check_quest_active, "qst_collect_taxes"),
			(eq, "$g_player_is_captive", 0),
			(eq, "$qst_collect_taxes_currently_collecting", 1),
			(quest_get_slot, ":collect_taxes_current_state", "qst_collect_taxes", slot_quest_current_state),
			(this_or_next|eq, ":collect_taxes_current_state", 1),
			(this_or_next|eq, ":collect_taxes_current_state", 2),
			(eq, ":collect_taxes_current_state", 3),
			(quest_get_slot, ":collect_taxes_target_amount", "qst_collect_taxes", slot_quest_target_amount),
			(val_sub, ":collect_taxes_target_amount", 1),
			(quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":collect_taxes_target_amount"),
			(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
			(try_begin),
				(lt, ":collect_taxes_target_amount", 0),
				(assign, ":collect_taxes_current_state", 4),
				(quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
				(rest_for_hours, 0, 0, 0),
				(jump_to_menu, "mnu_collect_taxes_complete"),
			(else_try),
				(assign, ":var_3", "$qst_collect_taxes_hourly_income"),
				(party_get_slot, ":g_encountered_party_town_prosperity", "$g_encountered_party", slot_town_prosperity),
				(store_add, ":value", 30, ":g_encountered_party_town_prosperity"),
				(val_mul, ":var_3", ":value"),
				(val_div, ":var_3", 80),
				(try_begin),
					(eq, "$qst_collect_taxes_halve_taxes", 1),
					(val_div, ":var_3", 2),
				(try_end),
				(val_max, ":var_3", 2),
				(store_random_in_range, ":random_in_range_1_var_3", 1, ":var_3"),
				(quest_get_slot, ":collect_taxes_gold_reward", "qst_collect_taxes", slot_quest_gold_reward),
				(val_add, ":collect_taxes_gold_reward", ":random_in_range_1_var_3"),
				(quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":collect_taxes_gold_reward"),
				(call_script, "script_troop_add_gold", "trp_player", ":random_in_range_1_var_3"),
			(try_end),
			(try_begin),
				(eq, ":collect_taxes_current_state", 1),
				(val_sub, "$qst_collect_taxes_menu_counter", 1),
				(le, "$qst_collect_taxes_menu_counter", 0),
				(quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
				(jump_to_menu, "mnu_collect_taxes_revolt_warning"),
			(else_try),
				(eq, ":collect_taxes_current_state", 2),
				(val_sub, "$qst_collect_taxes_unrest_counter", 1),
				(le, "$qst_collect_taxes_unrest_counter", 0),
				(eq, "$qst_collect_taxes_halve_taxes", 0),
				(quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),
				(store_div, ":value_2", 10000, "$qst_collect_taxes_total_hours"),
				(val_add, ":value_2", 30),
				(store_random_in_range, ":random_in_range_0_1000", 0, 1000),
				(try_begin),
					(lt, ":random_in_range_0_1000", ":value_2"),
					(jump_to_menu, "mnu_collect_taxes_revolt"),
				(try_end),
			(try_end)
		]),

	(72.0,
		[
			(gt, "$g_force_peace_faction_1", 0),
			(gt, "$g_force_peace_faction_2", 0),
			(try_begin),
				(store_relation, ":relation_g_force_peace_faction_1_g_force_peace_faction_2", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
				(lt, ":relation_g_force_peace_faction_1_g_force_peace_faction_2", 0),
				(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
			(try_end),
			(assign, "$g_force_peace_faction_1", 0),
			(assign, "$g_force_peace_faction_2", 0)
		]),

	(1.0,
		[
			(str_store_string, 51, "str_no_trigger_noted"),
			(try_begin),
				(gt, "$npc_to_rejoin_party", 0),
				(eq, "$g_infinite_camping", 0),
				(try_begin),
					(neg|main_party_has_troop, "$npc_to_rejoin_party"),
					(neq, "$g_player_is_captive", 1),
					(str_store_string, 51, "str_triggered_by_npc_to_rejoin_party"),
					(assign, "$npc_map_talk_context", 151),
					(start_map_conversation, "$npc_to_rejoin_party", -1),
				(else_try),
					(troop_set_slot, "$npc_to_rejoin_party", slot_troop_mission_object, 8),
					(assign, "$npc_to_rejoin_party", 0),
				(try_end),
			(else_try),
				(gt, "$npc_is_quitting", 0),
				(eq, "$g_infinite_camping", 0),
				(try_begin),
					(main_party_has_troop, "$npc_is_quitting"),
					(neq, "$g_player_is_captive", 1),
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$npc_is_quitting"),
					(neg|troop_slot_eq, "$npc_is_quitting", slot_troop_spouse, "trp_player"),
					(str_store_string, 51, "str_triggered_by_npc_is_quitting"),
					(start_map_conversation, "$npc_is_quitting", -1),
				(else_try),
					(assign, "$npc_is_quitting", 0),
				(try_end),
			(else_try),
				(gt, "$npc_with_grievance", 0),
				(eq, "$g_infinite_camping", 0),
				(eq, "$disable_npc_complaints", 0),
				(try_begin),
					(main_party_has_troop, "$npc_with_grievance"),
					(neq, "$g_player_is_captive", 1),
					(str_store_string, 51, "str_triggered_by_npc_has_grievance"),
					(assign, "$npc_map_talk_context", 61),
					(start_map_conversation, "$npc_with_grievance", -1),
				(else_try),
					(assign, "$npc_with_grievance", 0),
				(try_end),
			(else_try),
				(gt, "$npc_with_personality_clash", 0),
				(eq, "$g_infinite_camping", 0),
				(eq, "$disable_npc_complaints", 0),
				(troop_get_slot, ":npc_with_personality_clash_personalityclash_object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
				(try_begin),
					(main_party_has_troop, "$npc_with_personality_clash"),
					(main_party_has_troop, ":npc_with_personality_clash_personalityclash_object"),
					(neq, "$g_player_is_captive", 1),
					(assign, "$npc_map_talk_context", 72),
					(str_store_string, 51, "str_triggered_by_npc_has_personality_clash"),
					(start_map_conversation, "$npc_with_personality_clash", -1),
				(else_try),
					(assign, "$npc_with_personality_clash", 0),
				(try_end),
			(else_try),
				(gt, "$npc_with_political_grievance", 0),
				(eq, "$g_infinite_camping", 0),
				(eq, "$disable_npc_complaints", 0),
				(try_begin),
					(main_party_has_troop, "$npc_with_political_grievance"),
					(neq, "$g_player_is_captive", 1),
					(str_store_string, 51, "str_triggered_by_npc_has_political_grievance"),
					(assign, "$npc_map_talk_context", 145),
					(start_map_conversation, "$npc_with_political_grievance", -1),
				(else_try),
					(assign, "$npc_with_political_grievance", 0),
				(try_end),
			(else_try),
				(eq, "$disable_sisterly_advice", 0),
				(eq, "$g_infinite_camping", 0),
				(gt, "$npc_with_sisterly_advice", 0),
				(try_begin),
					(main_party_has_troop, "$npc_with_sisterly_advice"),
					(neq, "$g_player_is_captive", 1),
					(troop_slot_ge, "$npc_with_sisterly_advice", 139, 1),
					(assign, "$npc_map_talk_context", 139),
					(start_map_conversation, "$npc_with_sisterly_advice", -1),
				(else_try),
					(assign, "$npc_with_sisterly_advice", 0),
				(try_end),
			(else_try),
				(eq, "$disable_local_histories", 0),
				(eq, "$g_infinite_camping", 0),
				(try_for_range, ":troop", "trp_npc1", "trp_kingdom_1_lord"),
					(main_party_has_troop, ":troop"),
					(troop_slot_eq, ":troop", slot_troop_home_speech_delivered, 0),
					(troop_get_slot, ":troop_home", ":troop", slot_troop_home),
					(gt, ":troop_home", 0),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_home_main_party", ":troop_home", "p_main_party"),
					(lt, ":distance_to_party_from_party_troop_home_main_party", 7),
					(assign, "$npc_map_talk_context", 60),
					(str_store_string, 51, "str_triggered_by_local_histories"),
					(start_map_conversation, ":troop", -1),
				(try_end),
			(try_end),
			(try_begin),
				(check_quest_active, "qst_rebel_against_kingdom"),
				(is_between, "$supported_pretender", "trp_kingdom_1_pretender", "trp_knight_1_1"),
				(neg|main_party_has_troop, "$supported_pretender"),
				(neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, 2),
				(party_add_members, "p_main_party", "$supported_pretender", 1),
			(try_end),
			(try_begin),
				(check_quest_active, "qst_rebel_against_kingdom"),
				(is_between, "$supported_pretender", "trp_kingdom_1_pretender", "trp_knight_1_1"),
				(main_party_has_troop, "$supported_pretender"),
				(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
				(call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
			(try_end)
		]),

	(1.0,
		[
			(try_for_range, ":troop", "trp_npc1", "trp_knight_1_1_wife"),
				(troop_slot_ge, ":troop", 55, 1),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(troop_get_slot, ":troop_change_to_faction", ":troop", slot_troop_change_to_faction),
				(troop_get_slot, ":troop_leaded_party", ":troop", slot_troop_leaded_party),
				(assign, ":value", 0),
				(try_begin),
					(le, ":troop_leaded_party", 0),
					(neg|troop_slot_ge, ":troop", 8, 0),
					(assign, ":value", 1),
				(else_try),
					(gt, ":troop_leaded_party", 0),
					(party_get_attached_to, ":attached_to_troop_leaded_party", ":troop_leaded_party"),
					(try_begin),
						(lt, ":attached_to_troop_leaded_party", 0),
						(party_get_cur_town, ":attached_to_troop_leaded_party", ":troop_leaded_party"),
					(try_end),
					(this_or_next|neg|is_between, ":attached_to_troop_leaded_party", "p_town_1_1", "p_salt_mine"),
					(party_slot_eq, ":attached_to_troop_leaded_party", slot_town_lord, ":troop"),
					(assign, ":value_2", "trp_knight_1_1_wife"),
					(try_for_range, ":troop_2", "trp_npc1", ":value_2"),
						(troop_slot_eq, ":troop_2", slot_troop_occupation, 2),
						(troop_get_slot, ":troop_2_leaded_party", ":troop_2", slot_troop_leaded_party),
						(party_is_active, ":troop_2_leaded_party"),
						(store_faction_of_party, ":faction_of_party_troop_2_leaded_party", ":troop_2_leaded_party"),
						(eq, ":faction_of_party_troop_2_leaded_party", ":faction_of_troop_troop"),
						(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_leaded_party_troop_2_leaded_party", ":troop_leaded_party", ":troop_2_leaded_party"),
						(lt, ":distance_to_party_from_party_troop_leaded_party_troop_2_leaded_party", 4),
						(assign, ":value_2", 0),
					(try_end),
					(neq, ":value_2", 0),
					(assign, ":value", 1),
				(try_end),
				(eq, ":value", 1),
				(try_begin),
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, 4, ":troop"),
					(display_message, "@{!}DEBUG - {s4} faction changed from slot troop change to faction"),
				(try_end),
				(call_script, "script_change_troop_faction", ":troop", ":troop_change_to_faction"),
				(troop_set_slot, ":troop", slot_troop_change_to_faction, 0),
				(try_begin),
					(is_between, ":troop_change_to_faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
					(str_store_troop_name_link, 1, ":troop"),
					(str_store_faction_name_link, 2, ":faction_of_troop_troop"),
					(str_store_faction_name_link, 3, ":troop_change_to_faction"),
					(display_message, "@{s1} has switched from {s2} to {s3}."),
					(try_begin),
						(eq, ":faction_of_troop_troop", "$players_kingdom"),
						(call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop", ":troop_change_to_faction"),
					(else_try),
						(eq, ":troop_change_to_faction", "$players_kingdom"),
						(call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop", ":faction_of_troop_troop"),
					(try_end),
				(try_end),
			(try_end)
		]),

	(1.0,
		[
			(store_current_day, ":current_day"),
			(gt, ":current_day", "$g_last_report_control_day"),
			(store_time_of_day, ":time_of_day"),
			(ge, ":time_of_day", 18),
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(this_or_next|ge, ":time_of_day", 22),
			(eq, ":random_in_range_0_4", 0),
			(assign, "$g_last_report_control_day", ":current_day"),
			(store_troop_gold, ":troop_gold_player", "trp_player"),
			(try_begin),
				(lt, ":troop_gold_player", 0),
				(store_sub, ":value", 0, ":troop_gold_player"),
				(troop_add_gold, "trp_player", ":value"),
			(try_end),
			(party_get_morale, ":morale_main_party", "p_main_party"),
			(try_begin),
				(str_store_string, 1, "str_party_morale_is_low"),
						
				(str_clear, 2),
				(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
				(assign, ":var_8", 0),
				(try_for_range_backwards, ":var_18", 0, ":num_companion_stacks_main_party"),
					(party_stack_get_troop_id, ":party_stack_troop_id_main_party_var_9", "p_main_party", ":var_18"),
					(neg|troop_is_hero, ":party_stack_troop_id_main_party_var_9"),
					(party_stack_get_size, ":party_stack_size_main_party_var_9", "p_main_party", ":var_18"),
					(store_faction_of_troop, ":faction_of_troop_party_stack_troop_id_main_party_var_9", ":party_stack_troop_id_main_party_var_9"),
					(assign, ":var_13", ":morale_main_party"),
					(try_begin),
						(ge, ":faction_of_troop_party_stack_troop_id_main_party_var_9", "fac_kingdom_1"),
						(lt, ":faction_of_troop_party_stack_troop_id_main_party_var_9", "fac_kingdoms_end"),
						(faction_get_slot, ":faction_of_troop_party_stack_troop_id_main_party_var_9_morale_of_player_troops", ":faction_of_troop_party_stack_troop_id_main_party_var_9", slot_faction_morale_of_player_troops),
						(val_div, ":faction_of_troop_party_stack_troop_id_main_party_var_9_morale_of_player_troops", 100),
						(val_add, ":var_13", ":faction_of_troop_party_stack_troop_id_main_party_var_9_morale_of_player_troops"),
					(try_end),
					(lt, ":var_13", 32),
					(store_sub, ":value_2", 36, ":var_13"),
					(val_div, ":value_2", 4),
					(assign, ":var_16", 0),
					(try_for_range, ":unused", 0, ":party_stack_size_main_party_var_9"),
						(store_random_in_range, ":random_in_range_0_4", 0, 100),
						(lt, ":random_in_range_0_4", ":value_2"),
						(val_add, ":var_16", 1),
						(remove_member_from_party, ":party_stack_troop_id_main_party_var_9", "p_main_party"),
					(try_end),
					(try_begin),
						(ge, ":var_16", 1),
						(str_store_troop_name, 2, ":party_stack_troop_id_main_party_var_9"),
						(assign, reg0, ":var_16"),
						(try_begin),
							(ge, ":var_8", 1),
							(str_store_string, 1, "str_s1_reg0_s2"),
						(else_try),
							(str_store_string, 3, 1),
							(str_store_string, 1, "str_s3_reg0_s2"),
						(try_end),
						(val_add, ":var_8", ":var_16"),
					(try_end),
				(try_end),
				(try_begin),
					(ge, ":var_8", 1),
					(try_begin),
						(ge, ":var_8", 2),
						(str_store_string, 2, "str_have_deserted_the_party"),
						#(play_sound, "snd_recruits_left"),
					(else_try),
						(str_store_string, 2, "str_has_deserted_the_party"),
						#(play_sound, "snd_recruits_left"),
						#(play_sound, "snd_recruits_left"),
					(try_end),
					(str_store_string, 1, "str_s1_s2"),
					(eq, "$g_infinite_camping", 0),
					(dialog_box, 1, "str_weekly_report"),
					(play_sound, "snd_recruits_left"),
				(try_end),
			(try_end)
		]),

#	(1.0,
#		[]),

	(1.0,
		[
			(try_begin),
				(eq, "$g_player_is_captive", 1),
				(neg|party_is_active, "$capturer_party"),
				(rest_for_hours, 0, 0, 0),
			(try_end),
			(assign, ":var_1", "$next_center_will_be_fired"),
			(party_get_slot, ":var_1_village_smoke_added", ":var_1", slot_village_smoke_added),
			(eq, ":var_1_village_smoke_added", 0),
			(try_begin),
				(party_get_slot, ":var_1_village_bound_center", ":var_1", slot_village_bound_center),
				(party_get_slot, ":var_1_village_bound_center_town_last_nearby_fire_time", ":var_1_village_bound_center", slot_town_last_nearby_fire_time),
				(store_current_hours, ":current_hours"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(is_between, ":var_1", "p_town_1_1", "p_salt_mine"),
					(is_between, ":var_1_village_bound_center", "p_town_1_1", "p_salt_mine"),
					(str_store_party_name, 4, ":var_1"),
					(str_store_party_name, 5, ":var_1_village_bound_center"),
					(store_current_hours, reg3),
					(party_get_slot, reg4, ":var_1_village_bound_center", slot_town_last_nearby_fire_time),
					(display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
				(try_end),
				(eq, ":current_hours", ":var_1_village_bound_center_town_last_nearby_fire_time"),
				(party_add_particle_system, ":var_1", "psys_map_village_fire"),
				(party_add_particle_system, ":var_1", "psys_map_village_fire_smoke"),
			(else_try),
				(store_add, ":value", ":var_1_village_bound_center_town_last_nearby_fire_time", 4),
				(eq, ":value", ":current_hours"),
				(party_clear_particle_systems, ":var_1"),
			(try_end)
		]),

	(24.0,
		[
			(val_sub, "$g_dont_give_fief_to_player_days", 1),
			(val_max, "$g_dont_give_fief_to_player_days", -1),
			(val_sub, "$g_dont_give_marshalship_to_player_days", 1),
			(val_max, "$g_dont_give_marshalship_to_player_days", -1),
			(party_set_name, "p_steppe_bandit_spawn_point_1", "str_the_steppes"),
			(party_set_name, "p_taiga_bandit_spawn_point_1", "str_the_tundra"),
			(party_set_name, "p_forest_bandit_spawn_point_1", "str_the_forests"),
			(party_set_name, "p_forest_bandit_spawn_point_2", "str_the_forests"),
			(party_set_name, "p_mountain_bandit_spawn_point_1", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_2", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_3", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_4", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_5", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_6", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_7", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_8", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_9", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_10", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_11", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_12", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_13", "str_the_highlands"),
			(party_set_name, "p_mountain_bandit_spawn_point_14", "str_the_highlands"),
			(party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_3", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_4", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_5", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_6", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_7", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_8", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_9", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_10", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_11", "str_the_coast"),
			(party_set_name, "p_sea_raider_spawn_point_12", "str_the_coast"),
			(party_set_name, "p_desert_bandit_spawn_point_1", "str_the_deserts"),
			(party_set_name, "p_desert_bandit_spawn_point_2", "str_the_deserts"),
			(party_set_name, "p_desert_bandit_spawn_point_3", "str_the_deserts"),
			(try_begin),
				(check_quest_active, "qst_formal_marriage_proposal"),
				(check_quest_failed, "qst_formal_marriage_proposal"),
				(call_script, "script_end_quest", "qst_formal_marriage_proposal"),
			(try_end),
			(try_begin),
				(check_quest_active, "qst_lend_companion"),
				(quest_get_slot, ":lend_companion_giver_troop", "qst_lend_companion", slot_quest_giver_troop),
				(store_faction_of_troop, ":faction_of_troop_lend_companion_giver_troop", ":lend_companion_giver_troop"),
				(store_relation, ":relation_faction_of_troop_lend_companion_giver_troop_players_kingdom", ":faction_of_troop_lend_companion_giver_troop", "$players_kingdom"),
				(this_or_next|lt, ":relation_faction_of_troop_lend_companion_giver_troop_players_kingdom", 0),
				(neg|is_between, ":faction_of_troop_lend_companion_giver_troop", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(call_script, "script_abort_quest", "qst_lend_companion", 0),
			(try_end),
			(try_begin),
				(is_between, "$players_kingdom", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(neq, "$players_kingdom", "fac_player_supporters_faction"),
				(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
				(val_add, "$g_player_days_as_marshal", 1),
			(else_try),
				(assign, "$g_player_days_as_marshal", 0),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
				(party_get_slot, ":party_center_player_enterprise_consumption_order", ":party", slot_center_player_enterprise_consumption_order),
				(ge, ":party_center_player_enterprise_consumption_order", 1),
				(val_sub, ":party_center_player_enterprise_consumption_order", 1),
				(party_set_slot, ":party", slot_center_player_enterprise_consumption_order, ":party_center_player_enterprise_consumption_order"),
			(try_end)
		]),

#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),
#
#	(24.0,
#		[]),

	(12.0,
		[
			(eq, "$g_player_is_captive", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(assign, ":var_2", 0),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
				(val_add, ":var_2", ":party_stack_size_main_party_localvariable"),
			(try_end),
			(val_div, ":var_2", 3),
			(try_begin),
				(eq, ":var_2", 0),
				(val_add, ":var_2", 1),
			(try_end),
			(assign, ":var_5", ":var_2"),
			(assign, ":var_6", 0),
			(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
			(try_for_range, ":localvariable_2", 0, ":inventory_capacity_player"),
				(troop_get_inventory_slot, ":inventory_slot_player_localvariable_2", "trp_player", ":localvariable_2"),
				(try_begin),
					(ge, ":inventory_slot_player_localvariable_2", 0),
					(try_begin),
						(is_between, ":inventory_slot_player_localvariable_2", "itm_smoked_fish", "itm_siege_supply"),
						(troop_inventory_slot_get_item_amount, ":troop_inventory_slot_item_amount_player_localvariable_2", "trp_player", ":localvariable_2"),
						(troop_get_inventory_slot_modifier, ":inventory_slot_modifier_player_localvariable_2", "trp_player", ":localvariable_2"),
						(neq, ":inventory_slot_modifier_player_localvariable_2", 41),
						(val_add, ":var_6", ":troop_inventory_slot_item_amount_player_localvariable_2"),
					(try_end),
				(try_end),
			(try_end),
			(store_mul, ":value", ":var_6", 14),
			(val_div, ":value", ":var_5"),
			(try_begin),
				(le, ":value", 48),
				(gt, ":value", 0),
				(display_message, "@Your party is low on food, less than 48 hours of food remaining", 0x00ff0000),
			(try_end)
		]),

	(3.0, #3.0 World-map optimizaiton effort v1
		[
			#World Optimization Global Variable Begin
			(eq, "$messengers", 1),
			#World Optimization Global Variable End
		#(display_message, "@Spouse probably useless testing try for parties"),
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 24),
				(party_get_slot, ":var_1_orders_object", ":var_1", slot_party_orders_object),
				(party_get_slot, ":var_1_home_center", ":var_1", slot_party_home_center),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_orders_object", ":var_1", ":var_1_orders_object"),
				(try_begin),
					(le, ":distance_to_party_from_party_var_1_var_1_orders_object", 1),
					(try_begin),
						(neq, ":var_1_orders_object", ":var_1_home_center"),
						(try_begin),
							(is_between, ":var_1_orders_object", "p_village_1_1", "p_salt_mine"),
							(party_get_slot, ":var_1_orders_object_town_elder", ":var_1_orders_object", slot_town_elder),
						(else_try),
							(party_get_slot, ":var_1_orders_object_town_elder", ":var_1_orders_object", slot_town_merchant),
						(try_end),
						(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
						(troop_get_slot, ":player_spouse_162", ":player_spouse", 162),
						(troop_remove_items, ":var_1_orders_object_town_elder", "itm_bread", ":player_spouse_162"),
						(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_home_center"),
						(party_set_ai_behavior, ":var_1", 1),
						(party_set_ai_object, ":var_1", ":var_1_home_center"),
						(troop_add_items, "trp_household_possessions", "itm_bread", ":player_spouse_162"),
					(else_try),
						(remove_party, ":var_1"),
						(troop_set_slot, ":player_spouse", slot_troop_cur_center, "$g_player_court"),
					(try_end),
				(try_end),
			(try_end)
		]),

#	(720.0,
#		[
#			(try_for_parties, ":value"),
#				(party_slot_eq, ":value", slot_party_type, 22),
#				(party_get_slot, ":value_production_sources_end", ":value", slot_production_sources_end),
#				(party_get_num_companion_stacks, ":num_companion_stacks_value", ":value"),
#				(assign, ":value_2", 1),
#				(assign, ":value_3", 0),
#				(try_for_range, ":localvariable", 0, ":num_companion_stacks_value"),
#					(party_stack_get_troop_id, ":party_stack_troop_id_value_localvariable", ":value", ":localvariable"),
#					(eq, ":party_stack_troop_id_value_localvariable", "trp_dplmc_recruiter"),
#					(assign, ":value_2", 0),
#				(try_end),
#				(try_begin),
#					(party_get_battle_opponent, ":battle_opponent_value", ":value"),
#					(lt, ":battle_opponent_value", 0),
#					(eq, ":value_2", 1),
#					(party_get_slot, ":value_234", ":value", 234),
#					(str_store_party_name_link, 13, ":value_234"),
#					(assign, reg10, ":value_production_sources_end"),
#					(display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated!", 0x00ff0000),
#					(remove_party, ":value"),
#					(assign, ":value_3", 1),
#				(try_end),
#				(try_begin),
#					(eq, ":value_3", 0),
#					(party_get_slot, ":value_234", ":value", 234),
#					(store_faction_of_party, ":faction_of_party_value_234", ":value_234"),
#					(neq, ":faction_of_party_value_234", "$players_kingdom"),
#					(str_store_party_name_link, 13, ":value_234"),
#					(assign, reg10, ":value_production_sources_end"),
#					(display_log_message, "@{s13} has been taken by the enemy and your recruiter who was commissioned to recruit {reg10} recruits vanished  without a trace!", 0x00ff0000),
#					(remove_party, ":value"),
#					(assign, ":value_3", 1),
#				(try_end),
#				(eq, ":value_3", 0),
#				(party_get_num_companions, ":num_companions_value", ":value"),
#				(val_sub, ":num_companions_value", 1),
#				(party_get_slot, ":value_236", ":value", 236),
#				(lt, ":num_companions_value", ":value_production_sources_end"),
#				(try_begin),
#					(get_party_ai_object, ":party_ai_object_value", ":value"),
#					(get_party_ai_behavior, ":party_ai_behavior_value", ":value"),
#					(try_begin),
#						(neq, ":party_ai_behavior_value", 0),
#						(neq, ":party_ai_object_value", -1),
#						(party_set_slot, ":party_ai_object_value", 235, 0),
#					(try_end),
#					(assign, ":value_4", 999999),
#					(assign, ":value_5", -1),
#					(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
#						(store_distance_to_party_from_party, ":distance_to_party_from_party_value_party", ":value", ":party"),
#						(lt, ":distance_to_party_from_party_value_party", ":value_4"),
#						(try_begin),
#							(store_faction_of_party, ":faction_of_party_party", ":party"),
#							(assign, ":value_6", 100),
#							(try_begin),
#								(neq, ":faction_of_party_party", "$players_kingdom"),
#								(store_relation, ":value_6", "$players_kingdom", ":faction_of_party_party"),
#							(try_end),
#							(ge, ":value_6", 0),
#							(party_get_slot, ":party_center_player_relation", ":party", slot_center_player_relation),
#							(ge, ":party_center_player_relation", 0),
#							(party_get_slot, ":party_center_volunteer_troop_amount", ":party", slot_center_volunteer_troop_amount),
#							(gt, ":party_center_volunteer_troop_amount", 0),
#							(party_get_slot, ":party_center_original_faction", ":party", slot_center_original_faction),
#							(assign, ":value_7", 1),
#							(try_begin),
#								(eq, ":value_236", -1),
#								(assign, ":value_7", 0),
#							(else_try),
#								(eq, ":party_center_original_faction", ":value_236"),
#								(assign, ":value_7", 0),
#							(try_end),
#							(neq, ":value_7", 1),
#							(neg|party_slot_eq, ":party", slot_village_state, 2),
#							(neg|party_slot_eq, ":party", slot_village_state, 1),
#							(neg|party_slot_ge, ":party", 39, 1),
#							(neg|party_slot_eq, ":party", 235, 1),
#							(assign, ":value_4", ":distance_to_party_from_party_value_party"),
#							(assign, ":value_5", ":party"),
#						(try_end),
#					(try_end),
#					(gt, ":value_5", -1),
#					(party_set_ai_behavior, ":value", 1),
#					(party_set_ai_object, ":value", ":value_5"),
#					(party_set_slot, ":value", slot_party_ai_object, ":value_5"),
#					(party_set_slot, ":value_5", 235, 1),
#				(try_end),
#				(party_get_slot, ":value_ai_object", ":value", slot_party_ai_object),
#				(gt, ":value_ai_object", -1),
#				(store_distance_to_party_from_party, ":distance_to_party_from_party_value_value_ai_object", ":value", ":value_ai_object"),
#				(try_begin),
#					(store_faction_of_party, ":faction_of_party_value_ai_object", ":value_ai_object"),
#					(assign, ":value_6", 100),
#					(try_begin),
#						(neq, ":faction_of_party_value_ai_object", "$players_kingdom"),
#						(store_relation, ":value_6", "$players_kingdom", ":faction_of_party_value_ai_object"),
#					(try_end),
#					(ge, ":value_6", 0),
#					(party_get_slot, ":value_ai_object_center_player_relation", ":value_ai_object", slot_center_player_relation),
#					(ge, ":value_ai_object_center_player_relation", 0),
#					(call_script, "script_raf_aor_faction_to_region", ":party_center_original_faction"),
#					(assign, ":var_29", reg0),
#					(assign, ":value_7", 1),
#					(try_begin),
#						(eq, ":value_236", -1),
#						(assign, ":value_7", 0),
#					(else_try),
#						(eq, ":var_29", ":value_236"),
#						(assign, ":value_7", 0),
#					(try_end),
#					(neq, ":value_7", 1),
#					(neg|party_slot_eq, ":value_ai_object", slot_village_state, 2),
#					(neg|party_slot_eq, ":value_ai_object", slot_village_state, 1),
#					(neg|party_slot_ge, ":value_ai_object", 39, 1),
#					(le, ":distance_to_party_from_party_value_value_ai_object", 0),
#					(party_get_slot, ":value_ai_object_center_volunteer_troop_amount", ":value_ai_object", slot_center_volunteer_troop_amount),
#					(party_get_slot, ":value_ai_object_center_volunteer_troop_type", ":value_ai_object", slot_center_volunteer_troop_type),
#					(assign, ":var_32", ":value_production_sources_end"),
#					(val_sub, ":var_32", ":num_companions_value"),
#					(try_begin),
#						(gt, ":value_ai_object_center_volunteer_troop_amount", ":var_32"),
#						(assign, ":var_33", ":value_ai_object_center_volunteer_troop_amount"),
#						(val_sub, ":var_33", ":var_32"),
#						(assign, ":var_34", ":value_ai_object_center_volunteer_troop_amount"),
#						(val_sub, ":var_34", ":var_33"),
#						(assign, ":var_35", ":value_ai_object_center_volunteer_troop_amount"),
#						(val_sub, ":var_35", ":var_34"),
#						(party_set_slot, ":value_ai_object", slot_center_volunteer_troop_amount, ":var_35"),
#						(party_add_members, ":value", ":value_ai_object_center_volunteer_troop_type", ":var_34"),
#						(party_set_ai_behavior, ":value", 0),
#						(party_set_slot, ":value_ai_object", 235, 0),
#					(else_try),
#						(le, ":value_ai_object_center_volunteer_troop_amount", ":var_32"),
#						(gt, ":value_ai_object_center_volunteer_troop_amount", 0),
#						(party_set_slot, ":value_ai_object", slot_center_volunteer_troop_amount, -1),
#						(party_add_members, ":value", ":value_ai_object_center_volunteer_troop_type", ":value_ai_object_center_volunteer_troop_amount"),
#						(party_set_ai_behavior, ":value", 0),
#						(party_set_slot, ":value_ai_object", 235, 0),
#					(else_try),
#						(le, ":value_ai_object_center_volunteer_troop_amount", 0),
#						(party_set_ai_behavior, ":value", 0),
#						(party_set_slot, ":value_ai_object", 235, 0),
#					(else_try),
#						(display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!", 0x00ff2222),
#						(party_set_slot, ":value_ai_object", 235, 0),
#					(try_end),
#				(try_end),
#			(try_end),
#			(try_for_parties, ":value"),
#				(party_slot_eq, ":value", slot_party_type, 22),
#				(party_get_num_companions, ":num_companions_value", ":value"),
#				(val_sub, ":num_companions_value", 1),
#				(party_get_slot, ":value_production_sources_end", ":value", slot_production_sources_end),
#				(eq, ":num_companions_value", ":value_production_sources_end"),
#				(party_get_slot, ":value_234", ":value", 234),
#				(try_begin),
#					(neg|party_slot_eq, ":value", slot_party_ai_object, ":value_234"),
#					(party_set_slot, ":value", slot_party_ai_object, ":value_234"),
#					(party_set_ai_behavior, ":value", 1),
#					(party_set_ai_object, ":value", ":value_234"),
#				(try_end),
#				(store_distance_to_party_from_party, ":distance_to_party_from_party_value_value_234", ":value", ":value_234"),
#				(try_begin),
#					(le, ":distance_to_party_from_party_value_value_234", 0),
#					(party_get_num_companion_stacks, ":num_companion_stacks_value", ":value"),
#					(try_for_range, ":localvariable", 1, ":num_companion_stacks_value"),
#						(party_stack_get_size, ":party_stack_size_value_localvariable", ":value", ":localvariable"),
#						(party_stack_get_troop_id, ":party_stack_troop_id_value_localvariable", ":value", ":localvariable"),
#						(party_add_members, ":value_234", ":party_stack_troop_id_value_localvariable", ":party_stack_size_value_localvariable"),
#					(try_end),
#					(str_store_party_name_link, 13, ":value_234"),
#					(assign, reg10, ":num_companions_value"),
#					(display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", 0x0000ff00),
#					(remove_party, ":value"),
#				(try_end),
#			(try_end)
#		]),

#	(12.0, #World-map optimization effort v1 v2
#		[
#			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
#				(party_set_slot, ":party", 235, 0),
#			(try_end)
#		]),

	(2.0, #2.0 World-map optimizaiton effort v1
		[
					#World Optimization Global Variable Begin
			(eq, "$messengers", 1),
			#World Optimization Global Variable End
			(eq, "$g_player_chancellor", "trp_dplmc_chancellor"),
			#(display_message, "@Debug chancellor try for parties"),
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 23),
				(party_is_active, ":var_1"),
				(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
				(party_get_slot, ":var_1_orders_object", ":var_1", slot_party_orders_object),
				(try_begin),
					(party_is_active, ":var_1_ai_object"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_ai_object", ":var_1", ":var_1_ai_object"),
					(str_store_party_name, 14, ":var_1"),
					(str_store_party_name, 15, ":var_1_ai_object"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg0, ":distance_to_party_from_party_var_1_var_1_ai_object"),
						(display_message, "@Distance between {s14} and {s15}: {reg0}"),
					(try_end),
					(try_begin),
						(le, ":distance_to_party_from_party_var_1_var_1_ai_object", 1),
						(party_get_slot, ":var_1_300", ":var_1", 300),
						(str_store_item_name, 12, ":var_1_300"),
						(try_begin),
							(gt, ":var_1_orders_object", 0),
							(str_store_troop_name, 13, ":var_1_orders_object"),
						(else_try),
							(str_store_party_name, 13, ":var_1_ai_object"),
						(try_end),
						(display_log_message, "@Your caravan has brought {s12} to {s13}.", 0x0000ff00),
						(assign, ":value", 0),
						(store_faction_of_party, ":faction_of_party_var_1_ai_object", ":var_1_ai_object"),
						(try_begin),
							(gt, ":var_1_orders_object", 0),
							(faction_slot_eq, ":faction_of_party_var_1_ai_object", slot_faction_leader, ":var_1_orders_object"),
							(try_begin),
								(eq, ":var_1_300", "itm_wine"),
								(assign, ":value", 1),
							(else_try),
								(eq, ":var_1_300", "itm_oil"),
								(assign, ":value", 2),
							(try_end),
						(else_try),
							(store_random_in_range, ":random_in_range_1_3", 1, 3),
							(try_begin),
								(eq, ":var_1_300", "itm_ale"),
								(val_add, ":value", ":random_in_range_1_3"),
							(else_try),
								(eq, ":var_1_300", "itm_wine"),
								(store_add, ":value", 1, ":random_in_range_1_3"),
							(else_try),
								(eq, ":var_1_300", "itm_oil"),
								(store_add, ":value", 2, ":random_in_range_1_3"),
							(else_try),
								(eq, ":var_1_300", "itm_raw_dyes"),
								(val_add, ":value", 1),
							(else_try),
								(eq, ":var_1_300", "itm_raw_silk"),
								(val_add, ":value", 2),
							(else_try),
								(eq, ":var_1_300", "itm_velvet"),
								(val_add, ":value", 4),
							(else_try),
								(eq, ":var_1_300", "itm_smoked_fish"),
								(try_begin),
									(party_slot_eq, ":var_1_ai_object", slot_party_type, 4),
									(val_add, ":value", 1),
								(try_end),
							(else_try),
								(eq, ":var_1_300", "itm_cheese"),
								(val_add, ":value", 1),
								(try_begin),
									(party_slot_eq, ":var_1_ai_object", slot_party_type, 4),
									(val_add, ":value", 1),
								(try_end),
							(else_try),
								(eq, ":var_1_300", "itm_honey"),
								(val_add, ":value", 2),
								(try_begin),
									(party_slot_eq, ":var_1_ai_object", slot_party_type, 4),
									(val_add, ":value", 2),
								(try_end),
							(try_end),
						(try_end),
						(try_begin),
							(this_or_next|eq, ":faction_of_party_var_1_ai_object", "fac_player_supporters_faction"),
							(eq, ":faction_of_party_var_1_ai_object", "$players_kingdom"),
							(val_add, ":value", 1),
						(try_end),
						(try_begin),
							(gt, ":var_1_orders_object", 0),
							(call_script, "script_change_player_relation_with_troop", ":var_1_orders_object", ":value"),
						(else_try),
							(call_script, "script_change_player_relation_with_center", ":var_1_ai_object", ":value"),
						(try_end),
						(remove_party, ":var_1"),
					(try_end),
				(else_try),
					(display_log_message, "@Your caravan has lost its way and gave up your mission!", 0x00ff0000),
					(remove_party, ":var_1"),
				(try_end),
			(try_end)
		]),

	(2.0, #2.0 World-map optimizaiton effort v1
		[
					#World Optimization Global Variable Begin
			(eq, "$messengers", 1),
			#World Optimization Global Variable End
		#(display_message, "@Messenger testing try for parties"),
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 25),
				(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
				(party_get_slot, ":var_1_orders_object", ":var_1", slot_party_orders_object),
				(try_begin),
					(party_is_active, ":var_1_ai_object"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_ai_object", ":var_1", ":var_1_ai_object"),
					(str_store_party_name, 14, ":var_1"),
					(str_store_party_name, 15, ":var_1_ai_object"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg0, ":distance_to_party_from_party_var_1_var_1_ai_object"),
						(display_message, "@Distance between {s14} and {s15}: {reg0}"),
					(try_end),
					(try_begin),
						(le, ":distance_to_party_from_party_var_1_var_1_ai_object", 1),
						(try_begin),
							(eq, ":var_1_ai_object", "p_main_party"),
							(party_get_slot, ":var_1_orders_object_2", ":var_1", slot_party_orders_object),
							(party_get_slot, ":var_1_300", ":var_1", 300),
							(call_script, "script_add_notification_menu", "mnu_dplmc_messenger", ":var_1_orders_object_2", ":var_1_300"),
							(remove_party, ":var_1"),
						(else_try),
							(party_stack_get_troop_id, ":var_1_orders_object_2", ":var_1_ai_object", 0),
							(str_store_troop_name, 13, ":var_1_orders_object_2"),
							(try_begin),
								(eq, "$cheat_mode", 1),
								(display_log_message, "@Your messenger reached {s13}.", 0x0000ff00),
								(assign, "$g_talk_troop", ":var_1_orders_object_2"),
							(try_end),
							(party_get_slot, ":var_1_300_2", ":var_1", 300),
							(assign, ":var_1_300", 0),
							(try_begin),
								(party_set_slot, ":var_1_ai_object", slot_party_commander_party, "p_main_party"),
								(store_current_hours, ":current_hours"),
								(party_set_slot, ":var_1_ai_object", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
								(party_set_slot, ":var_1_ai_object", slot_party_orders_object, ":var_1_orders_object"),
								(party_set_slot, ":var_1_ai_object", slot_party_orders_type, ":var_1_300_2"),
								(party_set_slot, ":var_1_ai_object", slot_party_orders_time, ":current_hours"),
								(call_script, "script_npc_decision_checklist_party_ai", ":var_1_orders_object_2"),
								(try_begin),
									(eq, "$cheat_mode", 1),
									(display_message, "@{s14}"),
								(try_end),
								(try_begin),
									(eq, reg0, ":var_1_300_2"),
									(eq, reg1, ":var_1_orders_object"),
									(assign, ":var_1_300", 1),
								(try_end),
								(call_script, "script_party_set_ai_state", ":var_1_ai_object", reg0, reg1),
							(try_end),
							(party_set_ai_behavior, ":var_1", 1),
							(party_set_ai_object, ":var_1", "p_main_party"),
							(party_set_slot, ":var_1", slot_party_ai_object, "p_main_party"),
							(party_set_slot, ":var_1", slot_party_orders_object, ":var_1_orders_object_2"),
							(party_set_slot, ":var_1", 300, ":var_1_300"),
						(try_end),
					(try_end),
				(else_try),
					(display_log_message, "@Your messenger has lost it's way and gave up your mission!", 0x00ff0000),
					(remove_party, ":var_1"),
				(try_end),
			(try_end)
		]),

#	(168.0,
#		[]),

	(6.0, #2.0 World-map optimizaiton effort v1
		[
		#(display_message, "@Controlling minor parties", 0x00ff0000),
			(try_for_parties, ":var_1"),
				(party_get_template_id, ":template_id_var_1", ":var_1"),
				(this_or_next|party_slot_eq, ":var_1", slot_party_type, 7),
				(this_or_next|eq, ":template_id_var_1", "pt_peasant_rebels_euro"),
				(this_or_next|eq, ":template_id_var_1", "pt_guelphs"),
				(this_or_next|eq, ":template_id_var_1", "pt_ghibellines"),
				(this_or_next|eq, ":template_id_var_1", "pt_prussians"),
				(this_or_next|eq, ":template_id_var_1", "pt_yotvingians"),
				(this_or_next|eq, ":template_id_var_1", "pt_curonians"),
				(this_or_next|eq, ":template_id_var_1", "pt_samogitians"),
				(this_or_next|eq, ":template_id_var_1", "pt_welsh"),
				(this_or_next|eq, ":template_id_var_1", "pt_mongolian_camp"),
				(this_or_next|eq, ":template_id_var_1", "pt_crusader_raiders"),
				(this_or_next|eq, ":template_id_var_1", "pt_jihadist_raiders"),
				(this_or_next|eq, ":template_id_var_1", "pt_teutonic_raiders"),
				(eq, ":template_id_var_1", "pt_sea_raiders"),
				(party_is_active, ":var_1"),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_var_1", ":var_1"),
				(party_get_battle_opponent, ":battle_opponent_var_1", ":var_1"),
				(try_begin),
					(lt, ":battle_opponent_var_1", 0),
					(le, ":party_size_wo_prisoners_var_1", 10),
					(neq, ":template_id_var_1", "pt_sea_raiders"),
					(neq, ":template_id_var_1", "pt_mongolian_camp"),
					(remove_party, ":var_1"),
				(else_try),
					(lt, ":battle_opponent_var_1", 0),
					(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
					(gt, ":var_1_ai_object", 0),
					(party_is_active, ":var_1_ai_object"),
					(try_begin),
						(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_ai_object", ":var_1", ":var_1_ai_object"),
						(gt, ":distance_to_party_from_party_var_1_var_1_ai_object", 15),
						(party_set_ai_behavior, ":var_1", 6),
						(party_get_position, 5, ":var_1_ai_object"),
						(party_set_ai_target_position, ":var_1", 5),
					(else_try),
						(get_party_ai_behavior, ":party_ai_behavior_var_1", ":var_1"),
						(eq, ":party_ai_behavior_var_1", 6),
						(try_begin),
							(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_ai_object", ":var_1", ":var_1_ai_object"),
							(lt, ":distance_to_party_from_party_var_1_var_1_ai_object", 3),
							(party_set_ai_behavior, ":var_1", 2),
							(party_set_ai_object, ":var_1", ":var_1_ai_object"),
							(party_set_ai_patrol_radius, ":var_1", 15),
							(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_ai_object"),
						(try_end),
					(try_end),
				(try_end),
			(try_end)
		]),

	(1.0, #1.0 World-map optimizaiton effort v1
		[
					#World Optimization Global Variable Begin
			(eq, "$messengers", 1),
			#World Optimization Global Variable End
			#(display_message, "@Debug more try for parties"),
			(try_for_parties, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 26),
				(party_get_slot, ":var_1_ai_object", ":var_1", slot_party_ai_object),
				(party_get_slot, ":var_1_orders_object", ":var_1", slot_party_orders_object),
				(troop_get_slot, ":var_1_orders_object_cur_center", ":var_1_orders_object", slot_troop_cur_center),
				(party_get_slot, ":var_1_home_center", ":var_1", slot_party_home_center),
				(party_get_slot, ":var_1_center_original_faction", ":var_1", slot_center_original_faction),
				(try_begin),
					(gt, "$players_kingdom", 0),
					(neq, "$players_kingdom", ":var_1_center_original_faction"),
					(party_set_faction, ":var_1", "$players_kingdom"),
					(party_set_slot, ":var_1", slot_center_original_faction, "$players_kingdom"),
				(else_try),
					(neq, "fac_player_faction", ":var_1_center_original_faction"),
					(le, "$players_kingdom", 0),
					(party_set_faction, ":var_1", "fac_player_faction"),
					(party_set_slot, ":var_1", slot_center_original_faction, "fac_player_faction"),
				(try_end),
				(try_begin),
					(neq, ":var_1_orders_object_cur_center", ":var_1_ai_object"),
					(neq, ":var_1_ai_object", ":var_1_home_center"),
					(party_set_ai_behavior, ":var_1", 1),
					(party_set_ai_object, ":var_1", ":var_1_orders_object_cur_center"),
					(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_orders_object_cur_center"),
				(else_try),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_var_1_ai_object", ":var_1", ":var_1_ai_object"),
					(try_begin),
						(le, ":distance_to_party_from_party_var_1_var_1_ai_object", 1),
						(neq, ":var_1_ai_object", ":var_1_home_center"),
						(str_store_party_name, 25, ":var_1_home_center"),
						(str_store_troop_name, 26, ":var_1_orders_object"),
						(display_message, "@Your messenger has delivered his message to {s26} and is on his way back to {s25}", 0x0000ff00),
						(party_add_members, ":var_1", ":var_1_orders_object", 1),
						(troop_set_slot, ":var_1_orders_object", slot_troop_cur_center, ":var_1"),
						(troop_set_slot, ":var_1_orders_object", 400, 1),
						(party_set_ai_behavior, ":var_1", 1),
						(party_set_ai_object, ":var_1", ":var_1_home_center"),
						(party_set_slot, ":var_1", slot_party_ai_object, ":var_1_home_center"),
					(else_try),
						(le, ":distance_to_party_from_party_var_1_var_1_ai_object", 1),
						(eq, ":var_1_ai_object", ":var_1_home_center"),
						(troop_set_slot, ":var_1_orders_object", slot_troop_cur_center, ":var_1_home_center"),
						(str_store_party_name, 25, ":var_1_home_center"),
						(str_store_troop_name, 26, ":var_1_orders_object"),
						(display_message, "@{s26} has arrived in {s25} and is awaiting you there.", 0x0000ff00),
						(remove_party, ":var_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

	(0.0,
		[
			(eq, "$g_battle_preparation_phase", 2),
			(party_set_slot, "$g_battle_preparation", 251, 1),
			(try_for_parties, ":var_1"),
				(str_store_party_name, 20, ":var_1"),
				(neq, ":var_1", "$g_battle_preparation"),
				(neq, ":var_1", "p_main_party"),
				(neg|party_slot_eq, ":var_1", 251, 1),
				(this_or_next|party_slot_eq, ":var_1", slot_party_type, 7),
				(this_or_next|party_slot_eq, ":var_1", slot_party_type, 30),
				(party_slot_eq, ":var_1", slot_party_type, 13),
				(party_is_active, ":var_1"),
				(party_get_battle_opponent, ":battle_opponent_var_1", ":var_1"),
				(lt, ":battle_opponent_var_1", 0),
				(party_get_attached_to, ":attached_to_var_1", ":var_1"),
				(lt, ":attached_to_var_1", 0),
				(get_party_ai_behavior, ":party_ai_behavior_var_1", ":var_1"),
				(neq, ":party_ai_behavior_var_1", 8),
				(store_faction_of_party, ":faction_of_party_var_1", ":var_1"),
				(store_relation, ":relation_player_supporters_faction_faction_of_party_var_1", "fac_player_supporters_faction", ":faction_of_party_var_1"),
				(this_or_next|eq, ":faction_of_party_var_1", "$players_kingdom"),
				(lt, ":relation_player_supporters_faction_faction_of_party_var_1", 0),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_main_party", ":var_1", "p_main_party"),
				(le, ":distance_to_party_from_party_var_1_main_party", 5),
				(party_set_slot, ":var_1", 251, 1),
			(try_end),
			(try_begin),
				(map_free),
				(rest_for_hours, 12, 3, 0),
			(try_end),
			(store_current_hours, ":current_hours"),
			(store_sub, ":value", ":current_hours", "$g_battle_preparation_start"),
			(ge, ":value", 12),
			(assign, "$g_battle_preparation_phase", 3),
			(assign, "$g_battle_preparation_start", ":current_hours")
		]),

	(0.0,
		[
			(is_between, "$g_player_sally_town", "p_town_1_1", "p_salt_mine"),
			(party_is_active, "$g_player_sallies"),
			(start_encounter, "$g_player_sallies")
		]),

	(4.0,
		[
			(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
			(try_begin),
				(this_or_next|eq, ":current_terrain_main_party", 4),
				(eq, ":current_terrain_main_party", 12),
				(assign, "$tom_sand_storm_chance", 20),
				(set_global_haze_amount, 0),
				(store_random_in_range, ":random_in_range_25_101", 25, 101),
				(set_global_cloud_amount, ":random_in_range_25_101"),
			(else_try),
				(this_or_next|eq, ":current_terrain_main_party", 3),
				(eq, ":current_terrain_main_party", 11),
				(assign, "$tom_sand_storm_chance", 15),
				(store_random_in_range, ":random_in_range_25_101", 0, 101),
				(set_global_haze_amount, ":random_in_range_25_101"),
				(store_random_in_range, ":random_in_range_25_101", 15, 100),
				(set_global_cloud_amount, ":random_in_range_25_101"),
			(else_try),
				(this_or_next|eq, ":current_terrain_main_party", 2),
				(eq, ":current_terrain_main_party", 10),
				(assign, "$tom_sand_storm_chance", 10),
				(store_random_in_range, ":random_in_range_25_101", 0, 50),
				(set_global_haze_amount, ":random_in_range_25_101"),
				(store_random_in_range, ":random_in_range_25_101", 0, 80),
				(set_global_cloud_amount, ":random_in_range_25_101"),
			(else_try),
				(this_or_next|eq, ":current_terrain_main_party", 5),
				(eq, ":current_terrain_main_party", 13),
				(assign, "$tom_sand_storm_chance", 25),
				(set_global_haze_amount, 0),
				(set_global_cloud_amount, 0),
			(else_try),
				(assign, "$tom_sand_storm_chance", 15),
				(store_random_in_range, ":random_in_range_25_101", 0, 101),
				(set_global_haze_amount, ":random_in_range_25_101"),
				(store_random_in_range, ":random_in_range_25_101", 0, 101),
				(set_global_cloud_amount, ":random_in_range_25_101"),
			(try_end)
		]),

	(168.0,
		[
			(eq, "$freelancer_state", 1),
			(troop_get_slot, ":player_signup", "trp_player", slot_troop_signup),
			(troop_get_xp, ":xp_player", "trp_player"),
			(store_sub, ":value", ":xp_player", ":player_signup"),
			(try_begin),
				(troop_get_upgrade_troop, ":upgrade_troop_player_cur_troop_0", "$player_cur_troop", 0),
				(gt, ":upgrade_troop_player_cur_troop_0", 1),
				(call_script, "script_game_get_upgrade_xp", "$player_cur_troop"),
				(assign, ":var_5", reg0),
				(ge, ":value", ":var_5"),
				(try_begin),
					(call_script, "script_cf_freelancer_player_can_upgrade", ":upgrade_troop_player_cur_troop_0"),
					(troop_set_slot, "trp_player", slot_troop_signup, ":xp_player"),
					(jump_to_menu, "mnu_upgrade_path"),
				(else_try),
					(assign, ":var_6", reg0),
					(try_begin),
						(eq, ":var_6", 0),
						(display_message, "@You are not strong enough to lift a weapon fit for your promotion!"),
					(else_try),
						(eq, ":var_6", 1),
						(display_message, "@You are not strong enough to hold all that weight required with promotion!."),
					(else_try),
						(eq, ":var_6", 2),
						(display_message, "@Your arms are to weak to advance in the artillary at this moment."),
					(else_try),
						(eq, ":var_6", 3),
						(display_message, "@You require more horse riding skills to fit your next poisition!"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, "$crusader_order_joined", 1),
				(troop_add_gold, "trp_player", 100),
				(troop_add_item, "trp_player", "itm_bread"),
				(call_script, "script_change_troop_renown", "trp_player", 1),
				(call_script, "script_change_player_honor", 1),
				(add_xp_to_troop, 70, "trp_player"),
			(else_try),
				(store_character_level, ":character_level_player_cur_troop", "$player_cur_troop"),
				(store_mul, ":value_2", 10, ":character_level_player_cur_troop"),
				(troop_add_gold, "trp_player", ":value_2"),
				(add_xp_to_troop, 70, "trp_player"),
				(play_sound, "snd_money_received", 0),
			(try_end)
		]),

	(1.0,
		[
			(eq, "$freelancer_state", 1),
			(set_camera_follow_party, "$enlisted_party"),
			(party_relocate_near_party, "p_main_party", "$enlisted_party", 1),
			(assign, ":var_1", 0),
			(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
			(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
				(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
				(ge, ":inventory_slot_player_localvariable", 0),
				(is_between, ":inventory_slot_player_localvariable", "itm_smoked_fish", "itm_siege_supply"),
				(val_add, ":var_1", 1),
			(try_end),
			(try_begin),
				(lt, ":var_1", 2),
				(troop_add_item, "trp_player", "itm_bread"),
			(try_end)
		]),

	(168.0,
		[
			(troop_get_slot, ":manor_array_relations_begin", "trp_manor_array", slot_troop_relations_begin),
			(try_for_range, ":localvariable", 1, ":manor_array_relations_begin"),
				(troop_get_slot, ":manor_array_localvariable", "trp_manor_array", ":localvariable"),
				(party_get_slot, ":manor_array_localvariable_village_bound_center", ":manor_array_localvariable", slot_village_bound_center),
				(this_or_next|neg|party_slot_eq, ":manor_array_localvariable_village_bound_center", slot_village_state, 2),
				(party_slot_eq, ":manor_array_localvariable", 327, 1),
				(party_get_slot, ":manor_array_localvariable_village_bound_center_town_lord", ":manor_array_localvariable_village_bound_center", slot_town_lord),
				(party_get_slot, ":manor_array_localvariable_town_prosperity", ":manor_array_localvariable", slot_town_prosperity),
				(party_get_slot, ":manor_array_localvariable_342", ":manor_array_localvariable", 342),
				(party_get_slot, ":manor_array_localvariable_341", ":manor_array_localvariable", 341),
				(party_get_slot, ":manor_array_localvariable_367", ":manor_array_localvariable", 367),
				(assign, ":value", 0),
				(try_begin),
					(store_faction_of_party, ":faction_of_party_manor_array_localvariable_village_bound_center", ":manor_array_localvariable_village_bound_center"),
					(party_set_faction, ":manor_array_localvariable", ":faction_of_party_manor_array_localvariable_village_bound_center"),
					(party_set_slot, ":manor_array_localvariable", slot_town_lord, ":manor_array_localvariable_village_bound_center_town_lord"),
				(try_end),
				(assign, ":var_12", 0),
				(try_for_range, ":number", 303, 328),
					(party_slot_eq, ":manor_array_localvariable", ":number", 2),
					(party_set_slot, ":manor_array_localvariable", ":number", 1),
					(try_begin),
						(this_or_next|eq, ":number", 303),
						(this_or_next|eq, ":number", 306),
						(this_or_next|eq, ":number", 305),
						(eq, ":number", 304),
						(val_add, ":var_12", 15),
					(else_try),
						(eq, ":number", 307),
						(val_add, ":var_12", 10),
					(try_end),
					(try_begin),
						(eq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
						(try_begin),
							(eq, ":number", 305),
							(try_begin),
							(eq, "$colored_messages", 1),
							(display_message, "@Peasants rejoice of your whorehouse in the regional manor. You gain fame!", 0x0078cff7),
							(else_try),
							(display_message, "@Peasants rejoice of your whorehouse in the regional manor. You gain fame!"),
							(try_end),
							(call_script, "script_change_troop_renown", "trp_player", 5),
						(else_try),
							(this_or_next|eq, ":number", 322),
							(this_or_next|eq, ":number", 323),
							(this_or_next|eq, ":number", 324),
							(this_or_next|eq, ":number", 325),
							(this_or_next|eq, ":number", 326),
							(eq, ":number", 327),
							(try_begin),
							(eq, "$colored_messages", 1),
							(display_message, "@You gain right to rule for building an important building in your regional manor!", 0x007891f7),
							(else_try),
							(display_message, "@You gain right to rule for building an important building in your regional manor!"),
							(try_end),
							(call_script, "script_change_player_right_to_rule", 3),
						(else_try),
							(try_begin),
							(eq, "$colored_messages", 1),
							(display_message, "@You gain renown for funding a building in your regional manor", 0x0080f778),
							(else_try),
							(display_message, "@You gain renown for funding a building in your regional manor"),
							(try_end),
							(play_sound, "snd_manor_upgrade_complete"),
							(call_script, "script_change_troop_renown", "trp_player", 1),
						(try_end),
					(try_end),
				(try_end),
				(try_for_range, ":number", 303, 328),
					(party_slot_eq, ":manor_array_localvariable", ":number", 1),
					(store_sub, ":value_2", ":number", 308),
					(val_add, ":value_2", "trp_manor_grain"),
					(assign, ":var_15", 0),
					(assign, ":value_3", -1),
					(assign, ":value_4", -1),
					(troop_get_slot, ":value_2_301", ":value_2", 301),
					(party_get_slot, ":manor_array_localvariable_value_2_301", ":manor_array_localvariable", ":value_2_301"),
					(assign, ":var_20", 0),
					(try_begin),
						(is_between, ":number", 308, 312),
						(try_begin),
							(this_or_next|neq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
							(eq, ":manor_array_localvariable_value_2_301", 0),
							(val_add, ":var_15", 30),
							(val_add, ":var_20", 30),
						(else_try),
							(eq, ":manor_array_localvariable_value_2_301", 1),
							(troop_get_slot, ":value_3", ":value_2", 302),
							(assign, ":value_4", 4),
						(try_end),
					(else_try),
						(this_or_next|eq, ":number", 303),
						(this_or_next|eq, ":number", 304),
						(eq, ":number", 305),
						(val_add, ":var_15", 50),
						(val_add, ":var_20", 50),
					(else_try),
						(is_between, ":number", 312, 322),
						(try_begin),
							(this_or_next|neq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
							(eq, ":manor_array_localvariable_value_2_301", 0),
							(val_add, ":var_15", 80),
							(val_add, ":var_20", 80),
						(else_try),
							(this_or_next|neq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
							(eq, ":manor_array_localvariable_value_2_301", 1),
							(troop_get_slot, ":value_3", ":value_2", 302),
							(assign, ":value_4", 3),
						(try_end),
					(else_try),
						(is_between, ":number", 323, 327),
						(val_add, ":var_15", 100),
					(try_end),
					(try_begin),
						(ge, ":var_15", 1),
						(store_random_in_range, ":random_in_range_-5_5", -5, 5),
						(val_add, ":var_15", ":random_in_range_-5_5"),
						(val_add, ":value", ":var_15"),
						(val_add, ":var_20", ":random_in_range_-5_5"),
					(try_end),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(eq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
						(str_store_troop_name, 1, ":value_2"),
						(assign, reg1, ":var_20"),
						(display_message, "@MANOR troop: {s1} pays {reg1} gold"),
					(try_end),
					(ge, ":value_4", 0),
					(ge, ":value_3", 0),
					(try_begin),
						(eq, ":manor_array_localvariable_341", 1),
						(val_div, ":value_4", 2),
					(else_try),
						(eq, ":manor_array_localvariable_341", -1),
						(val_mul, ":value_4", 3),
						(val_div, ":value_4", 2),
					(try_end),
					(troop_ensure_inventory_space, "trp_manor_array", ":value_4"),
					(troop_add_items, "trp_manor_array", ":value_3", ":value_4"),
				(try_end),
				(try_begin),
					(party_slot_eq, ":manor_array_localvariable", 327, 1),
					(val_sub, ":value", 500),
					(lt, ":value", 0),
					(assign, ":value", 0),
				(try_end),
				(val_add, ":value", ":manor_array_localvariable_342"),
				(try_begin),
					(party_slot_eq, ":manor_array_localvariable", 302, 0),
					(val_clamp, ":manor_array_localvariable_342", 20, 200),
				(else_try),
					(party_slot_eq, ":manor_array_localvariable", 302, 1),
					(val_clamp, ":manor_array_localvariable_342", 20, 760),
				(else_try),
					(party_slot_eq, ":manor_array_localvariable", 302, 2),
					(val_clamp, ":manor_array_localvariable_342", 20, 1000),
				(try_end),
				(store_random_in_range, ":random_in_range_-5_5", -5, 6),
				(val_add, ":manor_array_localvariable_342", ":random_in_range_-5_5"),
				(try_begin),
					(eq, ":manor_array_localvariable_341", 1),
					(val_sub, ":var_12", 3),
					(val_add, ":manor_array_localvariable_342", 15),
					(val_mul, ":value", 3),
					(val_div, ":value", 2),
				(else_try),
					(eq, ":manor_array_localvariable_341", 0),
					(val_add, ":var_12", 1),
					(val_add, ":manor_array_localvariable_342", 40),
				(else_try),
					(eq, ":manor_array_localvariable_341", -1),
					(val_add, ":var_12", 2),
					(val_add, ":manor_array_localvariable_342", 50),
					(val_div, ":value", 2),
				(try_end),
				(val_clamp, ":var_12", 0, 100),
				(try_begin),
					(assign, ":var_22", ":manor_array_localvariable_town_prosperity"),
					(val_clamp, ":var_22", 5, 100),
					(val_mul, ":value", ":var_22"),
					(val_div, ":value", 100),
				(try_end),
				(try_begin),
					(party_set_slot, ":manor_array_localvariable", 344, -1),
					(party_slot_eq, ":manor_array_localvariable", 303, 1),
					(ge, ":manor_array_localvariable_town_prosperity", 50),
					(ge, ":manor_array_localvariable_342", 700),
					(store_random_in_range, ":random_in_range_manor_trader_silk_temp_lord", "trp_manor_trader_silk", "trp_temp_lord"),
					(party_set_slot, ":manor_array_localvariable", 344, ":random_in_range_manor_trader_silk_temp_lord"),
					(troop_get_slot, ":random_in_range_manor_trader_silk_temp_lord_302", ":random_in_range_manor_trader_silk_temp_lord", 302),
					(troop_clear_inventory, ":random_in_range_manor_trader_silk_temp_lord"),
					(store_random_in_range, ":random_in_range_-5_5", 5, 10),
					(troop_add_items, ":random_in_range_manor_trader_silk_temp_lord", ":random_in_range_manor_trader_silk_temp_lord_302", ":random_in_range_-5_5"),
					(store_troop_gold, ":troop_gold_random_in_range_manor_trader_silk_temp_lord", ":random_in_range_manor_trader_silk_temp_lord"),
					(troop_remove_gold, ":random_in_range_manor_trader_silk_temp_lord", ":troop_gold_random_in_range_manor_trader_silk_temp_lord"),
					(store_random_in_range, ":troop_gold_random_in_range_manor_trader_silk_temp_lord", 200, 800),
					(troop_add_gold, ":random_in_range_manor_trader_silk_temp_lord", ":troop_gold_random_in_range_manor_trader_silk_temp_lord"),
				(try_end),
				(try_begin),
					(party_slot_eq, ":manor_array_localvariable", 340, 1),
					(store_random_in_range, ":random_in_range_book_tactics_spice", "itm_book_tactics", "itm_spice"),
					(troop_clear_inventory, "trp_manor_trader_book"),
					(troop_add_items, "trp_manor_trader_book", ":random_in_range_book_tactics_spice", 1),
					(store_troop_gold, ":troop_gold_random_in_range_manor_trader_silk_temp_lord", "trp_manor_trader_book"),
					(troop_remove_gold, "trp_manor_trader_book", ":troop_gold_random_in_range_manor_trader_silk_temp_lord"),
					(store_random_in_range, ":troop_gold_random_in_range_manor_trader_silk_temp_lord", 200, 300),
					(troop_add_gold, "trp_manor_trader_book", ":troop_gold_random_in_range_manor_trader_silk_temp_lord"),
				(try_end),
				(val_add, ":manor_array_localvariable_367", ":value"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(eq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
					(assign, reg0, ":value"),
					(assign, reg1, ":manor_array_localvariable_367"),
					(display_message, "@final gold :{reg0}, manor gold: {reg1}"),
				(try_end),
				(val_add, ":var_12", ":manor_array_localvariable_town_prosperity"),
				(val_clamp, ":var_12", 0, 100),
				(party_set_slot, ":manor_array_localvariable", slot_town_prosperity, ":var_12"),
				(party_set_slot, ":manor_array_localvariable", 342, ":manor_array_localvariable_342"),
				(party_set_slot, ":manor_array_localvariable", 343, ":value"),
				(party_set_slot, ":manor_array_localvariable", 367, ":manor_array_localvariable_367"),
			(try_end)
		]),

	(168.0,
		[
			(troop_get_slot, ":manor_array_relations_begin", "trp_manor_array", slot_troop_relations_begin),
			(try_for_range, ":localvariable", 1, ":manor_array_relations_begin"),
				(troop_get_slot, ":manor_array_localvariable", "trp_manor_array", ":localvariable"),
				(party_get_slot, ":manor_array_localvariable_village_bound_center", ":manor_array_localvariable", slot_village_bound_center),
				(party_get_slot, ":manor_array_localvariable_village_bound_center_town_lord", ":manor_array_localvariable_village_bound_center", slot_town_lord),
				(neq, ":manor_array_localvariable_village_bound_center_town_lord", "trp_player"),
				(neg|party_slot_eq, ":manor_array_localvariable_village_bound_center", slot_village_state, 2),
				(party_get_slot, ":manor_array_localvariable_367", ":manor_array_localvariable", 367),
				(ge, ":manor_array_localvariable_367", 2000),
				(try_begin),
					(store_random_in_range, ":random_in_range_308_312", 308, 312),
					(party_slot_eq, ":manor_array_localvariable", ":random_in_range_308_312", 0),
					(party_set_slot, ":manor_array_localvariable", ":random_in_range_308_312", 1),
					(val_sub, ":manor_array_localvariable_367", 2000),
				(else_try),
					(ge, ":manor_array_localvariable_367", 3000),
					(store_random_in_range, ":random_in_range_308_312", 303, 308),
					(party_slot_eq, ":manor_array_localvariable", ":random_in_range_308_312", 0),
					(party_set_slot, ":manor_array_localvariable", ":random_in_range_308_312", 1),
					(val_sub, ":manor_array_localvariable_367", 3000),
				(else_try),
					(ge, ":manor_array_localvariable_367", 6000),
					(store_random_in_range, ":random_in_range_308_312", 303, 308),
					(party_slot_eq, ":manor_array_localvariable", ":random_in_range_308_312", 0),
					(party_set_slot, ":manor_array_localvariable", ":random_in_range_308_312", 1),
					(val_sub, ":manor_array_localvariable_367", 6000),
				(else_try),
					(ge, ":manor_array_localvariable_367", 10000),
					(store_random_in_range, ":random_in_range_308_312", 303, 308),
					(party_slot_eq, ":manor_array_localvariable", ":random_in_range_308_312", 0),
					(party_set_slot, ":manor_array_localvariable", ":random_in_range_308_312", 1),
					(val_sub, ":manor_array_localvariable_367", 10000),
				(try_end),
				(party_set_slot, ":manor_array_localvariable", 367, ":manor_array_localvariable_367"),
			(try_end)
		]),

	(168.0,
		[
			(try_for_parties, ":var_1"),
				(party_get_template_id, ":template_id_var_1", ":var_1"),
				(eq, ":template_id_var_1", "pt_manor"),
				(party_slot_ge, ":var_1", 340, 2),
				(party_set_slot, ":var_1", 709, 1),
			(try_end),
			(try_for_range, ":party", "p_town_1_1", "p_castle_1_1"),
				(try_begin),
					(party_get_slot, ":party_299", ":party", 299),
					(ge, ":party_299", 1),
					(party_get_template_id, ":template_id_party_299", ":party_299"),
					(eq, ":template_id_party_299", "pt_monastery"),
					(party_slot_ge, ":party_299", 340, 2),
					(party_set_slot, ":party_299", 709, 1),
				(try_end),
				(party_set_slot, ":party", 703, 1),
				(party_set_slot, ":party", 706, 1),
				(party_set_slot, ":party", 709, 1),
				(party_set_slot, ":party", 711, 3),
				(party_set_slot, ":party", 712, 2),
				(party_set_slot, ":party", 713, 1),
				(call_script, "script_feudal_lance_manpower_update", ":party", 15),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end),
			(try_for_range, ":party", "p_village_1_1", "p_salt_mine"),
				(call_script, "script_feudal_lance_manpower_update", ":party", 12),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end),
			(try_for_range, ":party", "p_castle_1_1", "p_village_1_1"),
				(call_script, "script_feudal_lance_manpower_update", ":party", 17),
				(call_script, "script_update_npc_volunteer_troops_in_village", ":party"),
			(try_end)
		]),

	(72.0,
		[
			(try_for_range, ":number", 3156, 3177),
				(store_random_in_range, ":random_in_range_town_1_1_castle_1_1", "p_town_1_1", "p_castle_1_1"),
				(troop_set_slot, ":number", slot_troop_cur_center, ":random_in_range_town_1_1_castle_1_1"),
				(troop_clear_inventory, ":number"),
				(try_begin),
					(is_between, ":number", "trp_trader_hat1", "trp_trader_sword1"),
					(try_for_range, reg0, 0, 30),
						(store_random_in_range, ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a", "itm_sarranid_head_cloth", "itm_leather_steppe_cap_a"),
						(troop_add_item, ":number", ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a"),
					(try_end),
				(else_try),
					(is_between, ":number", "trp_trader_sword1", "trp_trader_helmet1"),
					(try_for_range, reg0, 0, 10),
						(store_random_in_range, ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a", "itm_sword_type_xii", "itm_spatha"),
						(troop_add_item, ":number", ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a"),
					(try_end),
				(else_try),
					(is_between, ":number", "trp_trader_helmet1", "trp_trader_spice1"),
					(try_for_range, reg0, 0, 10),
						(store_random_in_range, ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a", "itm_flat_topped_helmet_a", "itm_bill"),
						(troop_add_item, ":number", ":random_in_range_sarranid_head_cloth_leather_steppe_cap_a"),
					(try_end),
				(else_try),
					(is_between, ":number", "trp_trader_spice1", "trp_trader_silk1"),
					(try_for_range, reg0, 0, 5),
						(troop_add_item, ":number", "itm_spice"),
						(troop_add_item, ":number", "itm_salt"),
					(try_end),
				(else_try),
					(is_between, ":number", "trp_trader_silk1", "trp_maid_1"),
					(try_for_range, reg0, 0, 3),
						(troop_add_item, ":number", "itm_raw_silk"),
						(troop_add_item, ":number", "itm_velvet"),
					(try_end),
				(try_end),
				(store_troop_gold, reg6, ":number"),
				(troop_remove_gold, ":number", reg6),
				(store_random_in_range, ":random_in_range_100_200", 100, 200),
				(call_script, "script_troop_add_gold", ":number", ":random_in_range_100_200"),
			(try_end)
		]),

	(24.0,
		[
			(try_for_range, ":script_param_2", "fac_player_supporters_faction", "fac_kingdoms_end"),
				(faction_set_slot, ":script_param_2", 400, 0),
				(faction_slot_eq, ":script_param_2", slot_faction_state, 0),
				(call_script, "script_check_if_faction_is_at_war", ":script_param_2"),
				(faction_set_slot, ":script_param_2", 400, reg0),
			(try_end)
		]),

	(168.0,
		[
			(try_for_range, ":party", "p_town_1_1", "p_salt_mine"),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(faction_get_slot, ":faction_of_party_party_400", ":faction_of_party_party", 400),
				(party_get_slot, ":party_400", ":party", 400),
				(party_get_slot, ":party_town_lord", ":party", slot_town_lord),
				(party_get_slot, ":party_town_prosperity", ":party", slot_town_prosperity),
				(assign, reg1, ":party_town_prosperity"),
				(try_begin),
					(eq, ":faction_of_party_party_400", 0),
					(call_script, "script_change_center_prosperity", ":party", 20),
				(try_end),
				(call_script, "script_change_center_prosperity", ":party", 5),
				(store_mul, ":value", ":party_400", -1),
				(call_script, "script_change_center_prosperity", ":party", ":value"),
				(val_add, ":party_town_prosperity", ":value"),
				(neq, ":party_town_lord", "trp_player"),
				(try_begin),
					(le, ":party_town_prosperity", 20),
					(gt, ":party_400", -2),
					(val_sub, ":party_400", 1),
					(party_set_slot, ":party", 400, ":party_400"),
				(else_try),
					(ge, ":party_town_prosperity", 99),
					(lt, ":party_400", 2),
					(val_add, ":party_400", 1),
					(party_set_slot, ":party", 400, ":party_400"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_10", 0, 10),
					(eq, ":random_in_range_0_10", 0),
					(store_random_in_range, ":random_in_range_0_10", -2, 3),
					(party_set_slot, ":party", 400, ":random_in_range_0_10"),
				(try_end),
			(try_end)
		]),

	(24.0,
		[
			(item_set_slot, "itm_bread", slot_item_food_bonus, 8),
			(item_set_slot, "itm_grain", slot_item_food_bonus, 2),
			(item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 4),
			(item_set_slot, "itm_dried_meat", slot_item_food_bonus, 5),
			(item_set_slot, "itm_cheese", slot_item_food_bonus, 5),
			(item_set_slot, "itm_sausages", slot_item_food_bonus, 5),
			(item_set_slot, "itm_butter", slot_item_food_bonus, 4),
			(item_set_slot, "itm_chicken", slot_item_food_bonus, 8),
			(item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 7),
			(item_set_slot, "itm_pork", slot_item_food_bonus, 6),
			(item_set_slot, "itm_raw_olives", slot_item_food_bonus, 1),
			(item_set_slot, "itm_cabbages", slot_item_food_bonus, 2),
			(item_set_slot, "itm_raw_grapes", slot_item_food_bonus, 3),
			(item_set_slot, "itm_apples", slot_item_food_bonus, 4),
			(item_set_slot, "itm_raw_date_fruit", slot_item_food_bonus, 4),
			(item_set_slot, "itm_honey", slot_item_food_bonus, 6),
			(item_set_slot, "itm_wine", slot_item_food_bonus, 5),
			(item_set_slot, "itm_ale", slot_item_food_bonus, 4)
		]),
		##Envfix BEGIN EVENTS CODE, REMOVE IF ISSUE OCCURS, INTRODUCED V0.996B
####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################



  #ramdon events chief
  ## Abhuva Random Events
   #---BEGIN LYX RANDOM EVENTS---
(21 * 24,[   # interval currently set to 6 hours for testing  - should be 14 * 24 for normal play, 1 * 6 for testing

   # Init
   # ---------------------------------------------------------------------------
#   (eq,"$random_events",1), ## abhuva, 1 = use random events, 0 = dont use them
   ##   (display_message, "@_Random Events Trigger fired.", 0xFF8000),  ## for bugfix
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_icon_state", pis_ship),
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief

            (neq, "$g_player_is_captive", 1),
       (assign, ":total_events", 11),   # update this when adding/removing events!
   (val_add, ":total_events", 1),   # MnB has weird ideas of ranges
   (store_random_in_range, ":curr_event", 0, ":total_events"),
   (neq, ":curr_event", "$g_lyx_last_random_event"),   # ignore event if same as last
   (assign, "$g_lyx_last_random_event", ":curr_event"),
   (assign, ":pos", 0),
   (try_begin), (eq,1,2),   # dummy


   # Events
   # ---------------------------------------------------------------------------

   # --- PLAYER INJURED --- 15
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@During today's training, you were accidently injured. While the wounds aren't severe, it may take some time for them to heal."),
      (else_try),
           (dialog_box, "@During today's training, you were accidently injured. While the wounds aren't severe, it may take some time for them to heal.", "@Training accident:"),
     (try_end),
     (call_script, "script_change_troop_health", "trp_player", -20),
  
   # --- PLAYER INJURED --- 16
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Today, you awoke with a horrible toothache and now you can no longer hide the pain."),
      (else_try),
           (dialog_box, "@Today, you awoke with a horrible toothache and now you can no longer hide the pain.", "@Toothache:"),
     (try_end),
     (call_script, "script_change_troop_health", "trp_player", -5),

  # --- PLAYER INJURED --- 17
  (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
     (try_begin),
#       (eq,"$random_events_box",0),
      (display_message, "@You slipped on wet ground, and you were injured."),
     (else_try),
          (dialog_box, "@You slipped on wet ground, and you were injured.", "@Injured."),
    (try_end),
    (call_script, "script_change_troop_health", "trp_player", -5),

   # --- PLAYER INJURED --- 18
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@(While travelling) You happen to find an abandoned house. You found some loot."),
      (else_try),
           (dialog_box, "@(While travelling) You happen to find an abandoned house. You found some loot.", "@Abandoned house."),
     (try_end),
     (troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_sword_type_xii", 0), #chief cambiado premio por eliminar al borracho
	(troop_add_item, "trp_player", "itm_smoked_fish", 0), #chief cambiado premio por eliminar al borracho


   # --- PLAYER strong ---19
##   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
##     (try_begin),
#       (eq,"$random_events_box",0),
##       (display_message, "@The adventure, life in the field, the constant training makes you feel strong and well, you are ready to face any challenge."),
##     (else_try),
##      (dialog_box, "@The adventure, life in the field, the constant training makes you feel strong and well, you are ready to face any challenge.", "@Heal improved:"),
##    (try_end),
##      (call_script, "script_change_troop_health", "trp_player", 40),
# = Two ## means that that part was not commented, one # means that part was commented and should not be uncommented if you want to use this feature again.
	    
	  
   # --- GOLD FOUND --- 20
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Today you got lucky and found a small bag hidden behind a bush. Inside the bag was 300 denars."),
      (else_try),
          (dialog_box, "@Today you got lucky and found a small bag hidden behind a bush. Inside the bag was 300 denars.", "@Found Gold bag:"),
     (try_end),
     (troop_add_gold, "trp_player", 300),

  # --- WORTHLESS METAL FOUND --- 21
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@During a small rest you noticed a shiny object in the ground caught your eye. You took a closer look, thinking it may be some denars. Unfortunately it was only a small piece of rusted metal lying on the ground, totally worthless."),
       (else_try),
           (dialog_box, "@During a small rest you noticed a shiny object in the ground caught your eye. You took a closer look, thinking it may be some denars. Unfortunately it was only a small piece of rusted metal lying on the ground, totally worthless.", "@Found some crap:"),
      (try_end),

  # --- Reservas de agua contaminadas --- 22
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@The water reserves have been contaminated and it must be rationed until you reach the next town."),
       (else_try),
           (dialog_box, "@The water reserves have been contaminated and it must be rationed until you reach the next town.", "@Water Reserves contaminated."),
      (try_end),
     (call_script, "script_change_troop_health", "trp_player", -15),
     (call_script, "script_change_player_party_morale", -15),
   
  # --- Encuentra cargamento de hidromiel --- 23
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@You and your party have come across an abandoned wagon of full of mead, and you gift it to your men."),
       (else_try),
           (dialog_box, "@You and your party have come across an abandoned wagon of full of mead, and you gift it to your men.", "@Wagon of Mead."),
      (try_end),
     (call_script, "script_change_player_party_morale", 10),
      
  # --- leales regalan a la party del heroe --- 24
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Loyalist supporters from a nearby village have gathered a bounty of food for your troops."),
       (else_try),
           (dialog_box, "@Loyalist supporters from a nearby village have gathered a bounty of food for your troops.", "@Bounty of food."),
      (try_end),
     (call_script, "script_change_player_party_morale", 10),

## # --- PLAYER INJURED/GOLD LOSS --- 25  needs editing
##   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
##      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,40),   # abort if player is already weak
##      #(call_script, "script_get_player_gold", "trp_player"), (ge, reg0, 120), # abort if too less money left on player
##      (try_begin),
##       (eq,"$random_events_box",0),
##       (display_message, "@Today you were injured by stumbling across a hidden stone. Your wounds are minor but later you discovered that you have lossed a bag of denar during the incident. DEBUG MESSAGE: Needs editing"),
##      (else_try),
##             (dialog_box, "@Today you were injured by stumbling across a hidden stone. Your wounds are minor but later you discovered that you have lossed a bag of denar during the incident.", "@Minor accident:"),
##     (try_end),
##     (call_script, "script_change_troop_health", "trp_player", -25),
##     #(troop_add_gold, "trp_player", -120),

#Griggs additional events
  # --- BATTLE LEFTOVERS --- 25  
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@You have found leftovers of a recent battle. Searching the bodies, you managed to find 200 denars."),
      (else_try),
             (dialog_box, "@You have found leftovers of a recent battle. Searching the bodies, you managed to find 200 denars.", "@Minor accident:"),
     (try_end),
     (troop_add_gold, "trp_player", 200),
#Griggs additional events end
     # Closing
   # --------------------------------------
   ## ideas for future events: morale of troops +/-, adding inventory items (food, maybe armour etc with smaller chance)
   (try_end),
] ),
#---END LYX RANDOM EVENTS---
## Abhuva Random Events ends chief acaba
      #x############################################
# EVENTS WITHOUT PREQUISITES ARE SPAWNED BY THIS TRIGGER 
#x############################################ 
#Works
(441, #Everything 1.5xed.
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 270),
          (store_random_in_range, ":rand", 0, 13),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_01"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_23"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_24"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_26"),
                                          (else_try),
                                            (eq, ":rand", 4),
                        (jump_to_menu,"mnu_event_02"),
                                           (else_try),
                                            (eq, ":rand", 5),
                        (jump_to_menu,"mnu_event_03"),
                                          (else_try),
                                            (eq, ":rand", 6),
                        (jump_to_menu,"mnu_event_05"),
                                          (else_try),
                                            (eq, ":rand", 7),
                        (jump_to_menu,"mnu_event_07"),
                                          (else_try),
						(display_message,"@ "),
					(try_end),
					]),

(615,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 140),
          (store_random_in_range, ":rand", 0, 15),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_04"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_11"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_27"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_28"),
                                          (else_try),
                                            (eq, ":rand", 4),
                        (jump_to_menu,"mnu_event_12"),
                                           (else_try),
                                            (eq, ":rand", 5),
                        (jump_to_menu,"mnu_event_13"),
                                          (else_try),
                                            (eq, ":rand", 6),
                        (jump_to_menu,"mnu_event_14"),
                                          (else_try),
                                            (eq, ":rand", 7),
                        (jump_to_menu,"mnu_event_101"),
                                          (else_try),
                                            (eq, ":rand", 8),
                        (jump_to_menu,"mnu_event_102"),
                                          (else_try),
                                            (eq, ":rand", 9),
                        (jump_to_menu,"mnu_event_103"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

(576,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_player_icon_state", pis_ship),
(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 300),
          (store_random_in_range, ":rand", 0, 12),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_29"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_30"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_31"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_36"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_37"),
                                           (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_32"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_33"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_34"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

    (540,
	[

         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
   (assign, ":has_fief1", 0),
    (try_for_range, ":party", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":party", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief1", 1),
    (try_end),
    (eq, ":has_fief1", 1),

(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_player_icon_state", pis_ship),
	(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 140),
          (store_random_in_range, ":rand", 0, 10),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_06"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_08"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_18"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_19"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_22"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

(486,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_player_icon_state", pis_ship),
(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 220),
          (store_random_in_range, ":rand", 0, 12),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_35"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_37"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_40"),
                                           (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_42"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_41"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  (405,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_player_icon_state", pis_ship),
	(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
          (store_random_in_range, ":rand", 0, 13),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_10"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_09"), #Good
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_25"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_15"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_16"),
                                           (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_20"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_21"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_17"), #Works
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  #chief eventos de king rey
  (622,
	[
   (assign, ":has_fief1", 0),
    (try_for_range, ":party", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":party", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief1", 1),
    (try_end),
    (eq, ":has_fief1", 1),
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (gt, ":player_renown", 180),
                                          (try_begin),
                                            (eq, "$g_juicio", 0), 
			(jump_to_menu,"mnu_event_01_juicio"),
                                            (assign, "$g_juicio", 1), 
                                          (else_try),
                                            (eq, "$g_juicio", 1), 
			(jump_to_menu,"mnu_event_02_juicio"),
                                            (assign, "$g_juicio", 2), 
                                          (else_try),
                                            (eq, "$g_juicio", 2), 
			(jump_to_menu,"mnu_event_03_juicio"),
                                            (assign, "$g_juicio", 3), 
                                          (else_try),
                                            (eq, "$g_juicio", 3), 
			(jump_to_menu,"mnu_event_04_juicio"),
                                            (assign, "$g_juicio", 4), 
                                          (else_try),
                                            (eq, "$g_juicio", 4), 
			(jump_to_menu,"mnu_event_06_juicio"),
                                            (assign, "$g_juicio", 5), 
                                           (else_try),
                                            (eq, "$g_juicio", 5), 
			(jump_to_menu,"mnu_event_07_juicio"),
                                            (assign, "$g_juicio", 6), 
                                          (else_try),
                                            (eq, "$g_juicio", 6), 
			(jump_to_menu,"mnu_event_08_juicio"),
                                            (assign, "$g_juicio", 7), 
                                          (else_try),
                                            (eq, "$g_juicio", 7), 
			(jump_to_menu,"mnu_event_09_juicio"),
                                            (assign, "$g_juicio", 8), 
                                          (else_try),
                                            (eq, "$g_juicio", 8), 
			(jump_to_menu,"mnu_event_11_juicio"),
                                            (assign, "$g_juicio", 9), 
                                          (else_try),
                                            (eq, "$g_juicio", 9), 
			(jump_to_menu,"mnu_event_12_juicio"),
                                            (assign, "$g_juicio", 10), 
                                          (else_try),
                                            (eq, "$g_juicio", 10), 
			(jump_to_menu,"mnu_event_13_juicio"),
                                            (assign, "$g_juicio", 11), 
                                          (else_try),
                                            (eq, "$g_juicio", 11), 
			(jump_to_menu,"mnu_event_14_juicio"),
                                            (assign, "$g_juicio", 12), 
                                           (else_try),
                                            (eq, "$g_juicio", 12), 
			(jump_to_menu,"mnu_event_15_juicio"),
                                            (assign, "$g_juicio", 13), 
                                          (else_try),
                                            (eq, "$g_juicio", 13), 
			(jump_to_menu,"mnu_event_16_juicio"),
                                            (assign, "$g_juicio", 14), 
                                          (else_try),
                                            (eq, "$g_juicio", 14), 
			(jump_to_menu,"mnu_event_17_juicio"),
                                            (assign, "$g_juicio", 15), 
                                          (else_try),
                                            (eq, "$g_juicio", 15), 
			(jump_to_menu,"mnu_event_18_juicio"),
                                            (assign, "$g_juicio", 16), 
                                          (else_try),
                                            (eq, "$g_juicio", 16), 
			(jump_to_menu,"mnu_event_19_juicio"),
                                            (assign, "$g_juicio", 17), 
                                          (else_try),
                                            (eq, "$g_juicio", 18), 
			(jump_to_menu,"mnu_event_21_juicio"),
                                            (assign, "$g_juicio", 19), 
                                           (else_try),
                                            (eq, "$g_juicio", 19), 
			(jump_to_menu,"mnu_event_22_juicio"),
                                            (assign, "$g_juicio", 20), 
                                          (else_try),
                                            (eq, "$g_juicio", 20), 
			(jump_to_menu,"mnu_event_23_juicio"),
                                            (assign, "$g_juicio", 21), 
                                          (else_try),
                                            (eq, "$g_juicio", 21), 
			(jump_to_menu,"mnu_event_24_juicio"),
                                            (assign, "$g_juicio", 22), 
                                          (else_try),
                                            (eq, "$g_juicio", 22), 
			(jump_to_menu,"mnu_event_05_juicio"),
                                            (assign, "$g_juicio", 23), 
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),
	############################################################################################################################
## Recruiter kit begin troop recruiter
############################################################################################################################
## This trigger keeps the recruiters moving by assigning them targets.
# (24.5, #0.5 to 6.5.
#   [
#   (try_for_parties, ":troop_leaded_party"),
#      (party_slot_eq,":troop_leaded_party", slot_party_type, spt_recruiter),
#      
#      (party_get_slot, ":needed", ":troop_leaded_party", slot_party_recruiter_needed_recruits),
#      
#      (party_get_num_companion_stacks, ":num_companion_stacks_encountered_party_backup", ":troop_leaded_party"),
#      (assign, ":destruction", 1),
#      (assign, ":quit", 0),
#      (try_for_range, ":localvariable", 0, ":num_companion_stacks_encountered_party_backup"),
#         (party_stack_get_troop_id, ":troop_4", ":troop_leaded_party", ":localvariable"),
#         (eq, ":troop_4", "trp_recruiter"),
#         (assign, ":destruction",0),
#      (try_end),
#      (try_begin),
#         (party_get_battle_opponent, ":battle_opponent_var_4", ":troop_leaded_party"),
#         (lt, ":battle_opponent_var_4", 0),
#         (eq, ":destruction", 1),
#         (party_get_slot, ":party_origin", ":troop_leaded_party", slot_party_recruiter_origin),
#         (str_store_party_name_link, s13, ":party_origin"),
#         (assign, reg10, ":needed"),
#         #(display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated!", 0xFF0000),
#         (remove_party, ":troop_leaded_party"),
#         (assign, ":quit", 1),
#      (try_end),
#      (eq, ":quit", 0),            
#      
#      (party_get_num_companions, ":script_param_3", ":troop_leaded_party"),
#      (val_sub, ":script_param_3", 1),   #the recruiter himself doesn't count.
#      
#   #daedalus begin
#      (party_get_slot, ":recruit_faction", ":troop_leaded_party", slot_party_recruiter_needed_recruits_faction),
#   #daedalus end
#      (lt, ":script_param_3", ":needed"),  #If the recruiter has less troops than player ordered, new village will be set as target.
#      (try_begin),
#         #(get_party_ai_current_behavior, ":ai_bhvr", ":troop_leaded_party"),
#         #(eq, ":ai_bhvr", ai_bhvr_hold),
#         (get_party_ai_object, ":previous_target", ":troop_leaded_party"),
#         (get_party_ai_behavior, ":previous_behavior", ":troop_leaded_party"),
#         (try_begin),
#            (neq, ":previous_behavior", ai_bhvr_hold),
#            (neq, ":previous_target", -1),
#            (party_set_slot, ":previous_target", slot_village_reserved_by_recruiter, 0),
#         (try_end),
#         (assign, ":value", 999999),
#         (assign, ":closest_village", -1),
#         (try_for_range, ":party_2", villages_begin, villages_end),
#            (store_distance_to_party_from_party, ":distance_between_positions_in_meters_0_1", ":troop_leaded_party", ":party_2"),
#            (lt, ":distance_between_positions_in_meters_0_1", ":value"),
#            (try_begin),
#               (store_faction_of_party, ":village_current_faction", ":party_2"),
#               (assign, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", 100),
#               (try_begin),
#                  (neq, ":village_current_faction", "$players_kingdom"),    # faction relation will be checked only if the village doesn't belong to the player's current faction
#                  (store_relation, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", "$players_kingdom", ":village_current_faction"),
#               (try_end),
#               (ge, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", 0),
#               (party_get_slot, ":village_relation", ":party_2", slot_center_player_relation),
#               (ge, ":village_relation", 0),
#               (party_get_slot, ":volunteers_in_village", ":party_2", slot_center_volunteer_troop_amount),
#               (gt, ":volunteers_in_village", 0),
#            #daedalus begin
#               (party_get_slot, ":faction_of_party_party_2", ":party_2", slot_center_original_faction),
#               (assign,":stop",1),
#               (try_begin),
#                  (eq,":recruit_faction",-1),
#                  (assign,":stop",0),
#               (else_try),
#                  (eq, ":faction_of_party_party_2", ":recruit_faction"),
#                  (assign,":stop",0),
#               (try_end),
#               (neq,":stop",1),
#            #daedalus end
#               (neg|party_slot_eq, ":party_2", slot_village_state, svs_looted),
#               (neg|party_slot_eq, ":party_2", slot_village_state, svs_being_raided),
#               (neg|party_slot_ge, ":party_2", slot_village_infested_by_bandits, 1),
#               (neg|party_slot_eq, ":party_2", slot_village_reserved_by_recruiter, 1),
#               (assign, ":value", ":distance_between_positions_in_meters_0_1"),
#               (assign, ":closest_village", ":party_2"),
#            (try_end),
#         (try_end),
#         (gt, ":closest_village", -1),
#         (party_set_ai_behavior, ":troop_leaded_party", ai_bhvr_travel_to_party),
#         (party_set_ai_object, ":troop_leaded_party", ":closest_village"),
#         (party_set_slot, ":troop_leaded_party", slot_party_ai_object, ":closest_village"),
#         (party_set_slot, ":closest_village", slot_village_reserved_by_recruiter, 1),
#      (try_end),
#      (party_get_slot, ":target", ":troop_leaded_party", slot_party_ai_object),
#      (gt, ":target", -1),
#      (store_distance_to_party_from_party, ":distance_from_target", ":troop_leaded_party", ":target"),
#      (try_begin),
#         (store_faction_of_party, ":target_current_faction", ":target"),
#         (assign, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", 100),
#         (try_begin),
#            (neq, ":target_current_faction", "$players_kingdom"),    # faction relation will be checked only if the target doesn't belong to the player's current faction
#            (store_relation, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", "$players_kingdom", ":target_current_faction"),
#         (try_end),
#         (ge, ":relation_faction_of_party_battle_opponent_l_current_town_player_supporters_faction", 0),
#         (party_get_slot, ":target_relation", ":target", slot_center_player_relation),
#         (ge, ":target_relation", 0),
#      #daedalus begin
#            (party_get_slot, ":script_param_2", ":target", slot_center_original_faction),
#            (assign,":stop",1),
#            (try_begin),
#            (eq,":recruit_faction",-1),
#            (assign,":stop",0),
#        (else_try),
#            (eq, ":script_param_2", ":recruit_faction"),
#            (assign,":stop",0),
#            (try_end),
#            (neq,":stop",1),
#      #daedalus end
#         (neg|party_slot_eq, ":target", slot_village_state, svs_looted),
#            (neg|party_slot_eq, ":target", slot_village_state, svs_being_raided),
#            (neg|party_slot_ge, ":target", slot_village_infested_by_bandits, 1),
#         (le, ":distance_from_target", 0),
#         (party_get_slot, ":volunteers_in_target", ":target", slot_center_volunteer_troop_amount),
#         (party_get_slot, ":target_volunteer_type", ":target", slot_center_volunteer_troop_type),
#         (assign, ":still_needed", ":needed"),
#         (val_sub, ":still_needed", ":script_param_3"),
#         (try_begin),
#            (gt, ":volunteers_in_target", ":still_needed"),
#            (assign, ":santas_little_helper", ":volunteers_in_target"),
#            (val_sub, ":santas_little_helper", ":still_needed"),
#            (assign, ":amount_to_recruit", ":volunteers_in_target"),
#            (val_sub, ":amount_to_recruit", ":santas_little_helper"),
#            (assign, ":new_target_volunteer_amount", ":volunteers_in_target"),
#            (val_sub, ":new_target_volunteer_amount", ":amount_to_recruit"),
#            (party_set_slot, ":target", slot_center_volunteer_troop_amount, ":new_target_volunteer_amount"),
#            (party_add_members, ":troop_leaded_party", ":target_volunteer_type", ":amount_to_recruit"),
#            (party_set_ai_behavior, ":troop_leaded_party", ai_bhvr_hold),
#            (party_set_slot, ":target", slot_village_reserved_by_recruiter, 0),
#         (else_try),
#            (le, ":volunteers_in_target", ":still_needed"),
#            (gt, ":volunteers_in_target", 0),
#            (party_set_slot, ":target", slot_center_volunteer_troop_amount, -1),
#            (party_add_members, ":troop_leaded_party", ":target_volunteer_type", ":volunteers_in_target"),
#            (party_set_ai_behavior, ":troop_leaded_party", ai_bhvr_hold),
#            (party_set_slot, ":target", slot_village_reserved_by_recruiter, 0),
#         (else_try),
#            (le, ":volunteers_in_target", 0),
#            (party_set_ai_behavior, ":troop_leaded_party", ai_bhvr_hold),
#            (party_set_slot, ":target", slot_village_reserved_by_recruiter, 0),
#         (else_try),
#            (display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!",0xFF2222),
#            (party_set_slot, ":target", slot_village_reserved_by_recruiter, 0),
#         (try_end),
#      (try_end),
#   (try_end),
#   (try_for_parties, ":troop_leaded_party"),
#      (party_slot_eq,":troop_leaded_party", slot_party_type, spt_recruiter),
#      (party_get_num_companions, ":script_param_3", ":troop_leaded_party"),
#      (val_sub, ":script_param_3", 1),   #the recruiter himself doesn't count
#      (party_get_slot, ":needed", ":troop_leaded_party", slot_party_recruiter_needed_recruits),
#      (eq, ":script_param_3", ":needed"),
#      (party_get_slot, ":party_origin", ":troop_leaded_party", slot_party_recruiter_origin),
#      (try_begin),
#         (neg|party_slot_eq, ":troop_leaded_party", slot_party_ai_object, ":party_origin"),
#         (party_set_slot, ":troop_leaded_party", slot_party_ai_object, ":party_origin"),
#         (party_set_ai_behavior, ":troop_leaded_party", ai_bhvr_travel_to_party),
#         (party_set_ai_object, ":troop_leaded_party", ":party_origin"),
#      (try_end),
#      (store_distance_to_party_from_party, ":distance_from_origin", ":troop_leaded_party", ":party_origin"),
#      (try_begin),
#         (le, ":distance_from_origin", 0),
#         (party_get_num_companion_stacks, ":num_companion_stacks_encountered_party_backup", ":troop_leaded_party"),
#         (try_for_range, ":localvariable", 1, ":num_companion_stacks_encountered_party_backup"),
#            (party_stack_get_size, ":party_stack_size_script_param_1_localvariable", ":troop_leaded_party", ":localvariable"),
#            (party_stack_get_troop_id, ":troop_4", ":troop_leaded_party", ":localvariable"),
#            (party_add_members, ":party_origin", ":troop_4", ":party_stack_size_script_param_1_localvariable"),
#         (try_end),
#         (str_store_party_name_link, s13, ":party_origin"),
#         (assign, reg10, ":script_param_3"),
#         (display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", 0x00FF00),
#         (remove_party, ":troop_leaded_party"),
#      (try_end),   
#   (try_end),
#   ]),
 
#This trigger makes sure that no village is left reserved forever.
#(12,
#   [
#   (try_for_range, ":party_2", villages_begin, villages_end),
#      (party_set_slot, ":party_2", slot_village_reserved_by_recruiter, 0),
#   (try_end),
#   ]),

############################################################################################################################
## Recruiter kit end
############################################################################################################################ 
## Envfix END EVENTS CODE, REMOVE IF ISSUE OCCURS, INTRODUCED V0.996B
#https://code.google.com/archive/p/dev1257/ 1257AD Developers

#		#####Patch Emoticons OSP
#		(3,
#        [
#		#Extension Begin
#		#(try_begin),
#		#(eq, "$g_disable_emoticons", 0),
#		#(assign, "$g_emoticons_hidden", 0),
#		#(try_end),
#		#Extension End
#						#(eq, "$g_emoticons_hidden", 0), #default
#					    #(assign, "$g_emoticons_hidden", 1), #default
#		#####Emoticons Enable instead of Disable Presentation Begin
#        (eq, "$g_disable_emoticons", 0),
#		(eq, "$g_emoticons_hidden", 0), #New
#	    (call_script, "script_hide_emoticons"),
#		(assign, "$g_emoticons_hidden", 1), #New
#		#####Emoticons Enable instead of Disable Presentation End
#		################################################################
#		#####Emoticons Disable instead of Enable Presentation Begin
#		#(eq, "$g_disable_emoticons", 1),
#		#(eq, "$g_emoticons_hidden", 1), #New
#	    #(call_script, "script_hide_emoticons"),
#		#(assign, "$g_emoticons_hidden", 0), #New
#		#####Emoticons Disable instead of Enable Presentation End
#        ]),
#		#####End Patch OSP

		
	

####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################

    (0,
        [
            (map_free),
            (this_or_next|key_clicked, key_o),
            (neq, "$g_lco_operation", 0),
            (try_begin),
                (this_or_next|key_clicked, key_o),
                (eq, "$g_lco_operation", lco_run_presentation),
                (assign, "$g_lco_operation", 0),
                (jump_to_menu, "mnu_lco_presentation"),
            (else_try),
                (eq, "$g_lco_operation", lco_view_character),
                (jump_to_menu, "mnu_lco_view_character"),
            (try_end),
        ]

    ),

####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
#KAOS Begin
#####Kaos Safe Begin
	#KAOS  (POLITICAL)
	#########################################################################################################################
	#Start Faction Rebellion triggers																						#
	#########################################################################################################################  
	#
	# Simple trigger to check the rebel faction and initiate rebellion if 
	# the required paramaters of date and rebellion chance 
	# NOTE: maybe change it to once a week. 
	#
	(168, #24 default
	[   
		(assign, ":random_chance", 0),
		(try_for_range, ":faction_of_troop_troop_4", rebel_factions_begin, rebel_factions_end),
		    (faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 2),
		    (neg|faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 1),
	        (faction_get_slot,  ":rebellion_date", ":faction_of_troop_troop_4", slot_rebellion_date),
	        (store_current_day, ":current_day"),
			(store_random_in_range, ":centers_in_range", 0, 16), #Used for things that I intend to make capitals out of.
			(store_random_in_range, ":centers_in_range_lite", 0, 10), #For those I did not completly make every possible fief a capital for.
 #####Kaos begin add factions Can subtitue towns for castles. rebel factions only. this needs to be changed for correct major factions 
	        (try_begin),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_43"),
	            (assign, ":rebel_lord", "trp_kingdom_1_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_1"),
		     	(try_begin),
		      		(eq, "$kaos_rebellion_home", 1), #This means use the assigned ones below if that thing is enabled, otherwise use the ones in (else_else) in this case, only two towns will be acquired, can add more tho.
		      		(assign, ":rebel_center", "p_town_1_1"), #SUNO
		      		(assign, ":rebel_claimed", "p_town_1_2"),#Praven
		     	(else_try),
				(eq, ":centers_in_range", 0), #New
		      		(assign, ":rebel_center", "p_town_1_1"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_town_1_2"),#Suno
				(else_try),
					(eq, ":centers_in_range", 1), #New
					(assign, ":rebel_center", "p_town_1_2"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_town_1_1"),#Suno
					(else_try),
					(eq, ":centers_in_range", 2), #New
					(assign, ":rebel_center", "p_town_1_3"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_town_1_4"),#Suno
						(else_try),
					(eq, ":centers_in_range", 3), #New
					(assign, ":rebel_center", "p_town_1_4"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_town_1_3"),#Suno
						(else_try),
					(eq, ":centers_in_range", 4), #New
					(assign, ":rebel_center", "p_castle_1_1"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_2"),#Suno
					(else_try),
					(eq, ":centers_in_range", 5), #New
					(assign, ":rebel_center", "p_castle_1_2"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_1"),#Suno
										(else_try),
					(eq, ":centers_in_range", 6), #New
					(assign, ":rebel_center", "p_castle_1_3"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_2"),#Suno
										(else_try),
					(eq, ":centers_in_range", 7), #New
					(assign, ":rebel_center", "p_castle_1_2"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_3"),#Suno
										(else_try),
					(eq, ":centers_in_range", 8), #New
					(assign, ":rebel_center", "p_castle_1_4"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_3"),#Suno
										(else_try),
					(eq, ":centers_in_range", 9), #New
					(assign, ":rebel_center", "p_castle_1_3"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_4"),#Suno
										(else_try),
					(eq, ":centers_in_range", 10), #New
					(assign, ":rebel_center", "p_castle_1_5"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_6"),#Suno
										(else_try),
					(eq, ":centers_in_range", 11), #New
					(assign, ":rebel_center", "p_castle_1_6"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_5"),#Suno
										(else_try),
					(eq, ":centers_in_range", 12), #New
					(assign, ":rebel_center", "p_castle_1_7"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_8"),#Suno
															(else_try),
					(eq, ":centers_in_range", 13), #New
					(assign, ":rebel_center", "p_castle_1_8"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_7"),#Suno
															(else_try),
					(eq, ":centers_in_range", 14), #New
					(assign, ":rebel_center", "p_castle_1_9"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_8"),#Suno
															(else_try),
					(ge, ":centers_in_range", 15), #New
					(assign, ":rebel_center", "p_castle_1_8"),#Uxkhal
		      		(assign, ":rebel_claimed", "p_castle_1_9"),#Suno
		 		(try_end),
	        (else_try),
			#####Checkpoint
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_44"),
	            (assign, ":rebel_lord", "trp_kingdom_2_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_2"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_2_1"),#Rivacheg
					(assign, ":rebel_claimed", "p_town_2_2"),#Reyvadin
				(else_try),
				(eq, ":centers_in_range", 0), #New
					(assign, ":rebel_center", "p_town_2_1"),#Curaw
					(assign, ":rebel_claimed", "p_town_2_2"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 1), #New
					(assign, ":rebel_center", "p_town_2_2"),#Curaw
					(assign, ":rebel_claimed", "p_town_2_1"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 2), #New
					(assign, ":rebel_center", "p_town_2_3"),#Curaw
					(assign, ":rebel_claimed", "p_town_2_4"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 3), #New
					(assign, ":rebel_center", "p_town_2_4"),#Curaw
					(assign, ":rebel_claimed", "p_town_2_3"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 4), #New
					(assign, ":rebel_center", "p_castle_2_1"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_2"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 5), #New
					(assign, ":rebel_center", "p_castle_2_2"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_1"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 6), #New
					(assign, ":rebel_center", "p_castle_2_3"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_4"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 7), #New
					(assign, ":rebel_center", "p_castle_2_4"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_3"),#Rivacheg
									(else_try),
				(eq, ":centers_in_range", 8), #New
					(assign, ":rebel_center", "p_castle_2_5"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_6"),#Rivacheg
														(else_try),
				(eq, ":centers_in_range", 9), #New
					(assign, ":rebel_center", "p_castle_2_6"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_5"),#Rivacheg
														(else_try),
				(eq, ":centers_in_range", 10), #New
					(assign, ":rebel_center", "p_castle_2_7"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_8"),#Rivacheg
														(else_try),
				(ge, ":centers_in_range", 11), #New
					(assign, ":rebel_center", "p_castle_2_8"),#Curaw
					(assign, ":rebel_claimed", "p_castle_2_7"),#Rivacheg
				(try_end),
	        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_45"),
	            (assign, ":rebel_lord", "trp_kingdom_3_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_3"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_3_1"), #Ichamur
					(assign, ":rebel_claimed", "p_town_3_2"),#Tulga
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_3_1"),#Halmar
					(assign, ":rebel_claimed", "p_town_3_2"),#Ichamur
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_3_3"),#Halmar
					(assign, ":rebel_claimed", "p_town_3_4"),#Ichamur
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_3_3"),#Halmar
					(assign, ":rebel_claimed", "p_town_3_4"),#Ichamur
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_3_1"),#Halmar
					(assign, ":rebel_claimed", "p_castle_3_2"),#Ichamur
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_3_3"),#Halmar
					(assign, ":rebel_claimed", "p_castle_3_4"),#Ichamur
									(else_try),
				(eq, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_3_5"),#Halmar
					(assign, ":rebel_claimed", "p_castle_3_6"),#Ichamur
									(else_try),
				(ge, ":centers_in_range_lite", 6), #New
					(assign, ":rebel_center", "p_castle_3_7"),#Halmar
					(assign, ":rebel_claimed", "p_castle_3_8"),#Ichamur
				(try_end),
	        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_46"),
	            (assign, ":rebel_lord", "trp_kingdom_4_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_4"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_4_1"), #Tihr
					(assign, ":rebel_claimed", "p_town_4_2"),#Sargoth
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_4_1"),#Wercheg
					(assign, ":rebel_claimed", "p_town_4_2"),#Tihr
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_4_3"),#Wercheg
					(assign, ":rebel_claimed", "p_town_4_4"),#Tihr
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_4_1"),#Wercheg
					(assign, ":rebel_claimed", "p_castle_4_2"),#Tihr
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_4_3"),#Wercheg
					(assign, ":rebel_claimed", "p_castle_4_4"),#Tihr
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_4_5"),#Wercheg
					(assign, ":rebel_claimed", "p_castle_4_6"),#Tihr
									(else_try),
				(ge, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_4_7"),#Wercheg
					(assign, ":rebel_claimed", "p_castle_4_8"),#Tihr
				(try_end),
	        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_47"),
	            (assign, ":rebel_lord", "trp_kingdom_5_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_5"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_5_1"), #Yalen
					(assign, ":rebel_claimed", "p_town_5_2"),#Jelkala
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_5_1"),#Veluca
					(assign, ":rebel_claimed", "p_town_5_2"),#Yalen
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_5_3"),#Veluca
					(assign, ":rebel_claimed", "p_town_5_4"),#Yalen
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_5_1"),#Veluca
					(assign, ":rebel_claimed", "p_castle_5_2"),#Yalen
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_5_3"),#Veluca
					(assign, ":rebel_claimed", "p_castle_5_4"),#Yalen
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_5_5"),#Veluca
					(assign, ":rebel_claimed", "p_castle_5_6"),#Yalen
									(else_try),
				(ge, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_5_7"),#Veluca
					(assign, ":rebel_claimed", "p_castle_5_8"),#Yalen
				(try_end),
	        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_48"),
	            (assign, ":rebel_lord", "trp_kingdom_6_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_6"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_6_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_6_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_6_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_6_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_6_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_6_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_6_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_6_6"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_6_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_6_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_6_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_6"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 6), #New
					(assign, ":rebel_center", "p_castle_6_7"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_8"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 7), #New
					(assign, ":rebel_center", "p_castle_6_9"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_10"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 8), #New
					(assign, ":rebel_center", "p_castle_6_11"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_12"),#Durquba
														(else_try),
				(ge, ":centers_in_range_lite", 9), #New
					(assign, ":rebel_center", "p_castle_6_12"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_6_13"),#Durquba
				(try_end),
				
				(else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_49"),
	            (assign, ":rebel_lord", "trp_kingdom_7_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_7"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_7_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_7_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_7_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_7_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_7_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_7_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_7_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_7_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_7_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_7_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_7_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_7_6"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_7_7"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_7_8"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 6), #New
					(assign, ":rebel_center", "p_castle_7_8"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_7_9"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_50"),
	            (assign, ":rebel_lord", "trp_kingdom_8_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_8"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_8_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_8_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_8_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_8_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_8_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_8_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_8_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_8_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_51"),
	            (assign, ":rebel_lord", "trp_kingdom_9_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_9"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_9_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_9_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_9_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_9_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_9_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_9_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_9_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_9_6"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_9_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_9_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_9_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_9_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_9_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_9_6"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 6), #New
					(assign, ":rebel_center", "p_castle_9_7"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_9_8"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 7), #New
					(assign, ":rebel_center", "p_castle_9_8"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_9_9"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_52"),
	            (assign, ":rebel_lord", "trp_kingdom_10_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_10"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_10_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_10_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_10_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_10_2"),#Durquba
					(else_try), #New
					(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_10_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_10_4"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_10_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_10_6"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_10_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_2"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_10_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_4"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_10_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_6"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 6), #New
					(assign, ":rebel_center", "p_castle_10_7"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_8"),#Durquba
										(else_try), #New
					(eq, ":centers_in_range_lite", 7), #New
					(assign, ":rebel_center", "p_castle_10_9"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_10"),#Durquba
										(else_try), #New
					(ge, ":centers_in_range_lite", 8), #New
					(assign, ":rebel_center", "p_castle_10_11"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_10_12"),#Durquba		
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_53"),
	            (assign, ":rebel_lord", "trp_kingdom_11_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_11"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_11_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_11_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_11_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_11_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_11_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_11_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_11_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_11_3"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_11_4"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_11_5"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_11_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_11_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_54"),
	            (assign, ":rebel_lord", "trp_kingdom_12_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_12"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_12_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_12_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_12_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_12_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_12_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_12_2"),#Durquba
														(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_12_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_12_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_55"),
	            (assign, ":rebel_lord", "trp_kingdom_13_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_13"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_13_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_13_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_13_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_13_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_13_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_13_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_13_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_13_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_56"),
	            (assign, ":rebel_lord", "trp_kingdom_14_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_14"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_14_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_14_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_14_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_14_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_14_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_14_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_14_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_14_3"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_14_4"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_14_5"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_14_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_14_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_57"),
	            (assign, ":rebel_lord", "trp_kingdom_15_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_15"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_15_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_15_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_15_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_15_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_15_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_15_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_15_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_15_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_15_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_15_4"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_15_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_15_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_58"),
	            (assign, ":rebel_lord", "trp_kingdom_16_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_16"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_16_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_16_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_16_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_16_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_16_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_16_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_16_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_16_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_59"),
	            (assign, ":rebel_lord", "trp_kingdom_17_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_17"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_17_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_17_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_17_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_17_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_17_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_17_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_17_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_17_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_17_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_17_6"),#Durquba
														(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_17_6"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_17_7"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_60"),
	            (assign, ":rebel_lord", "trp_kingdom_18_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_18"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_18_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_18_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_18_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_18_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_18_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_18_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_18_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_18_4"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_18_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_18_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_61"), #Faction too small, so only rebel with one fief.
	            (assign, ":rebel_lord", "trp_kingdom_19_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_19"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_19_1"), #Durquba
					(assign, ":rebel_claimed", "p_castle_19_1"),# In this case its the same as above because faction too small.
				(else_try),
				(ge, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_castle_19_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_19_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_62"),
	            (assign, ":rebel_lord", "trp_kingdom_20_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_20"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_20_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_20_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_20_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_20_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_20_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_20_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_20_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_20_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_20_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_20_6"),#Durquba
														(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_20_6"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_20_7"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_63"),
	            (assign, ":rebel_lord", "trp_kingdom_21_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_papacy"), #Papacy too small, don't use roma for rebellions, only one fief.
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_21_2"), #Durquba
					#(assign, ":rebel_claimed", "p_town_21_2"),#Shariz
				(else_try),
				(ge, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_21_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_21_2"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_64"),
	            (assign, ":rebel_lord", "trp_kingdom_22_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_22"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_22_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_22_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_22_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_22_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_22_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_22_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_22_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_22_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_22_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_22_4"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_22_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_22_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_65"),
	            (assign, ":rebel_lord", "trp_kingdom_23_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_23"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_23_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_23_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_23_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_23_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_23_4"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_23_5"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_23_6"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_23_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_23_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_23_3"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_66"),
	            (assign, ":rebel_lord", "trp_kingdom_24_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_24"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_24_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_24_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_24_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_24_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_24_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_24_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_24_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_24_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_67"),
	            (assign, ":rebel_lord", "trp_kingdom_25_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_25"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_25_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_25_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_25_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_25_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_25_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_25_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_25_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_25_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_25_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_25_3"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_25_4"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_25_5"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 5), #New
					(assign, ":rebel_center", "p_castle_25_6"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_25_7"),#Durquba
				(try_end),
				(else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_68"),
	            (assign, ":rebel_lord", "trp_kingdom_26_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_26"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_26_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_26_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_26_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_26_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_26_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_26_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_26_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_26_4"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_69"),
	            (assign, ":rebel_lord", "trp_kingdom_27_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_27"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_27_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_27_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_27_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_27_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_27_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_27_4"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_27_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_27_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_27_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_27_4"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 4), #New
					(assign, ":rebel_center", "p_castle_27_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_27_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_70"),
	            (assign, ":rebel_lord", "trp_kingdom_28_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_28"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_28_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_28_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_28_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_28_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_28_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_28_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_28_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_28_4"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_28_5"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_28_6"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_71"),
	            (assign, ":rebel_lord", "trp_kingdom_29_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_29"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_29_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_29_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_29_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_29_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_29_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_29_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_29_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_29_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_29_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_29_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_72"),
	            (assign, ":rebel_lord", "trp_kingdom_30_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_30"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_30_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_30_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_30_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_30_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_30_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_30_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_30_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_30_2"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_73"),
	            (assign, ":rebel_lord", "trp_kingdom_31_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_31"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_31_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_31_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_31_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_31_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_31_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_31_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_town_31_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_31_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_31_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_31_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_74"),
	            (assign, ":rebel_lord", "trp_kingdom_32_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_32"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_32_1"), #Durquba
					(assign, ":rebel_claimed", "p_town_32_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_32_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_town_32_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_32_3"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_32_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_32_1"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_32_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 3), #New
					(assign, ":rebel_center", "p_castle_32_2"),#Ahmerrad
					(assign, ":rebel_claimed", "p_castle_32_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_75"),
	            (assign, ":rebel_lord", "trp_kingdom_33_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_33"), #Faction too small
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_castle_33_1"), #Durquba
					#(assign, ":rebel_claimed", "p_castle_33_1"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_castle_33_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_33_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_33_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_33_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_33_3"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_33_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_76"),
	            (assign, ":rebel_lord", "trp_kingdom_34_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_34"), #Faction too small
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_castle_34_1"), #Durquba
					#(assign, ":rebel_claimed", "p_castle_34_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_castle_34_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_34_2"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_34_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_34_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_34_3"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_34_2"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_77"),
	            (assign, ":rebel_lord", "trp_kingdom_35_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_35"), #faction too small
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_castle_35_1"), #Durquba
					(assign, ":rebel_claimed", "p_castle_35_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_castle_35_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_35_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_35_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_35_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_35_3"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_35_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_78"),
	            (assign, ":rebel_lord", "trp_kingdom_36_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_36"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_castle_36_1"), #Durquba
					#(assign, ":rebel_claimed", "p_castle_36_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_castle_36_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_36_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_36_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_36_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_36_3"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_36_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_79"),
	            (assign, ":rebel_lord", "trp_kingdom_37_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_37"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_37_1"), #Durquba
					#(assign, ":rebel_claimed", "p_castle_37_1"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
				#Principality of wales, no need for town to turn rebel in my opinion.
					(assign, ":rebel_center", "p_town_37_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_37_1"),#Durquba
				(else_try),
				(ge, ":centers_in_range_lite", 1), #New
				#Principality of wales, no need for town to turn rebel in my opinion.
					(assign, ":rebel_center", "p_castle_37_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_37_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_80"),
	            (assign, ":rebel_lord", "trp_kingdom_38_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_38"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_38_1"), #Durquba
					#(assign, ":rebel_claimed", "p_town_38_1"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_38_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_38_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_38_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_38_1"),#Durquba
														(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_38_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_38_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_81"),
	            (assign, ":rebel_lord", "trp_kingdom_39_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_39"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_39_1"), #Durquba
					#(assign, ":rebel_claimed", "p_castle_39_1"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_39_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_39_1"),#Durquba
									(else_try),
				(eq, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_castle_39_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_39_1"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 2), #New
					(assign, ":rebel_center", "p_castle_39_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_castle_39_1"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_82"),
	            (assign, ":rebel_lord", "trp_kingdom_40_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_40"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_40_1"), #Durquba
					#(assign, ":rebel_claimed", "p_town_40_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_40_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_40_2"),#Durquba
				(else_try),
				(ge, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_40_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_40_2"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_83"),
	            (assign, ":rebel_lord", "trp_kingdom_41_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_41"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_41_1"), #Durquba
					#(assign, ":rebel_claimed", "p_town_41_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_41_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_41_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_41_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_41_2"),#Durquba
				(try_end),
					        (else_try),
	            (eq, ":faction_of_troop_troop_4", "fac_kingdom_84"),
	            (assign, ":rebel_lord", "trp_kingdom_42_pretender"),
	            (assign, ":faction_of_troop_script_param_1", "fac_kingdom_42"),
				(try_begin),
					(eq, "$kaos_rebellion_home", 1),
					(assign, ":rebel_center", "p_town_42_1"), #Durquba
					#(assign, ":rebel_claimed", "p_town_42_2"),#Shariz
				(else_try),
				(eq, ":centers_in_range_lite", 0), #New
					(assign, ":rebel_center", "p_town_42_1"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_42_2"),#Durquba
									(else_try),
				(ge, ":centers_in_range_lite", 1), #New
					(assign, ":rebel_center", "p_town_42_2"),#Ahmerrad
					#(assign, ":rebel_claimed", "p_town_42_2"),#Durquba
				(try_end),
	        (try_end),
#####Kaos end add factions

#OLD
	        (try_begin),
	        	(eq, "$background_answer_3", cb_king),
	            (assign, ":faction_of_troop_script_param_1", "fac_player_supporters_faction"),
	        (try_end),
#OLD

#NEW
#	            (assign, ":faction_of_troop_script_param_1", "fac_player_supporters_faction"),
#NEW


	        #Check that the current date is greater than the minimum day for rebellion to start
	        (ge, ":current_day", ":rebellion_date"), 
	        (try_begin),
	        	(neg|main_party_has_troop, ":rebel_lord"), 
		        (call_script, "script_rebelion_assesment", ":faction_of_troop_script_param_1"),
		        (faction_get_slot,  ":rebellion_chance", ":faction_of_troop_script_param_1", slot_faction_has_rebellion_chance),
		        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
				(store_sub, ":lower_limit", 9, ":rebellion_chance"),
				(store_random_in_range, ":random_chance", ":lower_limit", 9),

#New
		        (try_begin),
		            #Could change this conditional check to ge for a easier activation of rebellion
					#Independence patch begin forces rebellions to occur at certain date regardless of whatever.
					#(this_or_next|le, ":rebellion_chance", ":random_chance"), #Enforce rebellion
					#Independce patch end
					#Gt for default, GE for easier activation
					#(this_or_next|le, ":rebellion_chance", ":random_chance"), #Time-based rebellions rather than prosperity based.
					(try_begin),
					(eq, "$enforce_rebellions", 0),
		            (ge, ":rebellion_chance", ":random_chance"), #Disable the above line if you can get it to work properly.
					#Gt for default, GE for easier activation
					(call_script, "script_rebellion_faction_call", ":faction_of_troop_script_param_1", ":rebel_center", ":rebel_lord", ":faction_of_troop_troop_4", ":rebel_claimed"),
					(else_try),
					(eq, "$enforce_rebellions", 1),
					(this_or_next|le, ":rebellion_chance", ":random_chance"), #Time-based rebellions rather than prosperity based.
					(ge, ":rebellion_chance", ":random_chance"),
					#Gt for default, GE for easier activation
		            (call_script, "script_rebellion_faction_call", ":faction_of_troop_script_param_1", ":rebel_center", ":rebel_lord", ":faction_of_troop_troop_4", ":rebel_claimed"),
					(try_end),
		        (try_end),
#New				

#Old
#		        (try_begin),
#		            #Could change this conditional check to ge for a easier activation of rebellion
#					#Independence patch begin forces rebellions to occur at certain date regardless of whatever.
#					#(this_or_next|le, ":rebellion_chance", ":random_chance"), #Enforce rebellion
#					#Independce patch end
#					#Gt for default, GE for easier activation
#					#(this_or_next|le, ":rebellion_chance", ":random_chance"), #Time-based rebellions rather than prosperity based.
#		            (ge, ":rebellion_chance", ":random_chance"), #Disable the above line if you can get it to work properly.
#					#Gt for default, GE for easier activation
#		            (call_script, "script_rebellion_faction_call", ":faction_of_troop_script_param_1", ":rebel_center", ":rebel_lord", ":faction_of_troop_troop_4", ":rebel_claimed"),
#		        (try_end),
				#Old
	        (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":faction_of_troop_script_param_1"),
	          (assign, reg53, ":random_chance"),
	          (assign, reg54, ":rebellion_chance"),
	          (faction_get_slot, ":leader_no", ":faction_of_troop_troop_4", slot_faction_leader),
	          (str_store_troop_name, s55, ":leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
		(try_end),
	]
	),
	
	#########################################################################################################################
	#Faction Rebellion trigger for multiple claimants in the one center 													#
	#########################################################################################################################  
	#
	# Simple trigger for multiple claimants in the one center 
	# NOTE: maybe change it to once a week. 
	#
	(168, #72 default
	[   
		(store_current_day, ":current_day"),
		(assign, ":main_faction", 0),
		(assign, ":main_center", 0),
		(assign, ":sub_faction", 0),
		(assign, ":sub_center", 0),

		(assign, ":bonus", 3),
		(try_for_range, ":main_npc", pretenders_begin, pretenders_end),
            (troop_get_slot, ":main_center", ":main_npc", slot_troop_cur_center),
			#possibly useless patch start part 1
			(store_troop_faction, ":faction_of_party_var_6", ":main_npc"),
			(str_store_faction_name, ":main_faction", ":faction_of_party_var_6"),
			#possibly useless patch end
			 #   (str_store_faction_name, ":main_faction", ":main_npc"), #Patch part 1 disable
				
				
				(try_for_range, ":sub_npc", pretenders_begin, pretenders_end),
	            (troop_get_slot, ":sub_center", ":sub_npc", slot_troop_cur_center),
				#Possibly useless patch	start	 part 2	
				(store_troop_faction, ":partb_faction", ":sub_npc"),
				(str_store_faction_name, ":sub_faction", ":partb_faction"),
				#Possibly useless patch end
				#(str_store_faction_name, ":sub_faction", ":sub_npc"), #patch part 2 disable
				
	            (neq, ":main_npc", ":sub_npc"), 
	            (eq, ":main_center", ":sub_center"),
	            (try_begin),
				    (faction_slot_eq, ":main_faction", slot_faction_state, 2),
				    (neg|faction_slot_eq, ":main_faction", slot_faction_state, 1),
			        (faction_get_slot,  ":main_date", ":main_faction", slot_rebellion_date),
			        #Check that the current date is greater than the minimum day for rebellion to start
			        (ge, ":current_day", ":main_date"), 
		        	(neg|main_party_has_troop, ":main_npc"), 
			        (call_script, "script_rebelion_assesment", ":main_faction"),
			        (faction_get_slot,  ":main_chance", ":main_faction", slot_faction_has_rebellion_chance),
			        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
			        (val_add, ":main_chance", ":bonus"),
					(store_sub, ":lower_limit", 9, ":main_chance"),   
					(store_random_in_range, ":main_random_chance", ":lower_limit", 9), 
			        (try_begin),
			            #Could change this conditional check to ge for a easier activation of rebellion
			            (ge, ":main_chance", ":main_random_chance"),
			            (call_script, "script_rebellion_faction_call", ":main_faction"),
			        (try_end),
	            (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":main_faction"),
	          (assign, reg53, ":main_random_chance"),
	          (assign, reg54, ":main_chance"),
	          (faction_get_slot, ":main_leader_no", ":main_faction", slot_faction_leader),
	          (str_store_troop_name, s55, ":main_leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
	            (try_begin),
				    (faction_slot_eq, ":sub_faction", slot_faction_state, 2),
				    (neg|faction_slot_eq, ":sub_faction", slot_faction_state, 1),
			        (faction_get_slot,  ":sub_date", ":sub_faction", slot_rebellion_date),
			        #Check that the current date is greater than the minimum day for rebellion to start
			        (ge, ":current_day", ":sub_date"), 
		        	(neg|main_party_has_troop, ":sub_npc"), 
			        (call_script, "script_rebelion_assesment", ":sub_faction"),
			        (faction_get_slot,  ":sub_chance", ":sub_faction", slot_faction_has_rebellion_chance),
			        #Modify the random chance generation so that low fracturing makes it harder for a rebellion
			        (val_add, ":sub_chance", ":bonus"),
					(store_sub, ":lower_limit", 9, ":sub_chance"),   
					(store_random_in_range, ":sub_random_chance", ":lower_limit", 9), 
			        (try_begin),
			            #Could change this conditional check to ge for a easier activation of rebellion
			            (ge, ":sub_chance", ":sub_random_chance"),
			            (call_script, "script_rebellion_faction_call", ":sub_faction"),
			        (try_end),
	            (try_end),
	        #####################  debugging messages ################################
	        (try_begin),    
	          (eq, "$kaos_debug_mode", 1),  
	          (str_store_faction_name, s52, ":sub_faction"),
	          (assign, reg53, ":sub_random_chance"),
	          (assign, reg54, ":sub_chance"),
	          (faction_get_slot, ":sub_leader_no", ":sub_faction", slot_faction_leader),
	          (str_store_troop_name, s55, ":sub_leader_no"),
	          (display_log_message, "@{!} {s52} has a rebelion chance of {reg54} must be gt than {reg53} for rebel leader {s55}", 0xFF0000),
	        (try_end),    
	        #####################  debugging messages ################################
			(try_end),    
		(try_end),
	]
	),	

	#########################################################################################################################
	#Start Faction Civil war triggers																						#
	#########################################################################################################################  
	#
	# Simple trigger to check for civil war paramaters
	# NOTE: maybe change it to once a week. 
	#
#	(168, #24 default
#	[   
#	  (try_begin),
#		  (eq, "$kaos_civil_war", 1),
#	      (try_for_range, ":faction_of_troop_troop_4", "fac_player_supporters_faction", "fac_kingdom_43"),
#		  #Default: 	      	      (try_for_range, ":faction_of_troop_troop_4", kingdoms_begin, "fac_kingdom_43"),
#		      (faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 0),
#		      (neg|faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 1),
#		      (assign, ":var_2", 0),
#		      (assign, ":var_4", 0),
#			  (call_script, "script_evaluate_realm_stability", ":faction_of_troop_troop_4"),
#		        #####################  debugging messages ################################
#		        (try_begin),    
#		          (eq, "$kaos_debug_mode", 1),  
#		          (str_store_faction_name, s52, ":faction_of_troop_troop_4"),
#		          (assign, reg53, ":var_2"),
#		          (assign, reg54, ":var_4"),
#		          (faction_get_slot, ":script_param_1_leader", ":faction_of_troop_troop_4", slot_faction_leader),
#		          (str_store_troop_name, s55, ":script_param_1_leader"),
#		          (display_log_message, "@{!} {s52} leader {s55} total lords {reg53} angry lords {reg54}", 0xFF0000),
#		        (try_end),    
#		        #####################  debugging messages ################################  
#		      (try_begin),
#		          (ge, reg0, 40),
#		          (call_script, "script_rebellion_faction_civil_war", ":faction_of_troop_troop_4"),
#		      (try_end),
#	      (try_end),
#	  (try_end),
#	]
#	),	

	# Rename Rebell factions to original faction name if the original faction is defeated
	(168, #24 default
		[   
	        
			(try_for_range, ":faction_of_troop_troop_4", rebel_factions_begin, rebel_factions_end),
			    #(faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 2),
			    (faction_slot_eq, ":faction_of_troop_troop_4", slot_faction_state, 1),
		        (try_begin),
				#####Kaos begin add factions renames defeated faction to old faction if rebels win, rebel factions only allowed in here it seems. *This needs to be changed for correct major faction
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_1"),
				    (faction_slot_eq, "fac_kingdom_43", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_43", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom1_king"),
				    (faction_set_name, "fac_kingdom_43", s1),
		        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_2"),
				    (faction_slot_eq, "fac_kingdom_44", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_44", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom2_king"),
				    (faction_set_name, "fac_kingdom_44", s1),
		        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_3"),
				    (faction_slot_eq, "fac_kingdom_45", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_45", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom3_king"),
				    (faction_set_name, "fac_kingdom_45", s1),
		        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_4"),
				    (faction_slot_eq, "fac_kingdom_46", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_46", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom4_king"),
				    (faction_set_name, "fac_kingdom_46", s1),
		        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_5"),
				    (faction_slot_eq, "fac_kingdom_47", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_47", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom5_king"),
				    (faction_set_name, "fac_kingdom_47", s1),
		        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_6"),
				    (faction_slot_eq, "fac_kingdom_48", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_48", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom6_king"),
				    (faction_set_name, "fac_kingdom_48", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_7"),
				    (faction_slot_eq, "fac_kingdom_49", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_49", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom7_king"),
				    (faction_set_name, "fac_kingdom_49", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_8"),
				    (faction_slot_eq, "fac_kingdom_50", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_50", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom8_king"),
				    (faction_set_name, "fac_kingdom_50", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_9"),
				    (faction_slot_eq, "fac_kingdom_51", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_51", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom9_king"),
				    (faction_set_name, "fac_kingdom_51", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_10"),
				    (faction_slot_eq, "fac_kingdom_52", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_52", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom10_king"),
				    (faction_set_name, "fac_kingdom_52", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_11"),
				    (faction_slot_eq, "fac_kingdom_53", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_53", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom11_king"),
				    (faction_set_name, "fac_kingdom_53", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_12"),
				    (faction_slot_eq, "fac_kingdom_54", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_54", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom12_king"),
				    (faction_set_name, "fac_kingdom_54", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_13"),
				    (faction_slot_eq, "fac_kingdom_55", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_55", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom13_king"),
				    (faction_set_name, "fac_kingdom_55", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_14"),
				    (faction_slot_eq, "fac_kingdom_56", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_56", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom14_king"),
				    (faction_set_name, "fac_kingdom_56", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_15"),
				    (faction_slot_eq, "fac_kingdom_57", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_57", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom15_king"),
				    (faction_set_name, "fac_kingdom_57", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_16"),
				    (faction_slot_eq, "fac_kingdom_58", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_58", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom16_king"),
				    (faction_set_name, "fac_kingdom_58", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_17"),
				    (faction_slot_eq, "fac_kingdom_59", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_59", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom17_king"),
				    (faction_set_name, "fac_kingdom_59", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_18"),
				    (faction_slot_eq, "fac_kingdom_60", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_60", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom18_king"),
				    (faction_set_name, "fac_kingdom_60", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_19"),
				    (faction_slot_eq, "fac_kingdom_61", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_61", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom19_king"),
				    (faction_set_name, "fac_kingdom_61", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_20"),
				    (faction_slot_eq, "fac_kingdom_62", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_62", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom20_king"),
				    (faction_set_name, "fac_kingdom_62", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_papacy"),
				    (faction_slot_eq, "fac_kingdom_63", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_63", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom21_king"),
				    (faction_set_name, "fac_kingdom_63", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_22"),
				    (faction_slot_eq, "fac_kingdom_64", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_64", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom22_king"),
				    (faction_set_name, "fac_kingdom_64", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_23"),
				    (faction_slot_eq, "fac_kingdom_65", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_65", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom23_king"),
				    (faction_set_name, "fac_kingdom_65", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_24"),
				    (faction_slot_eq, "fac_kingdom_66", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_66", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom24_king"),
				    (faction_set_name, "fac_kingdom_66", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_25"),
				    (faction_slot_eq, "fac_kingdom_67", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_67", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom25_king"),
				    (faction_set_name, "fac_kingdom_67", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_26"),
				    (faction_slot_eq, "fac_kingdom_68", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_68", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom26_king"),
				    (faction_set_name, "fac_kingdom_68", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_27"),
				    (faction_slot_eq, "fac_kingdom_69", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_69", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom27_king"),
				    (faction_set_name, "fac_kingdom_69", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_28"),
				    (faction_slot_eq, "fac_kingdom_70", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_70", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom28_king"),
				    (faction_set_name, "fac_kingdom_70", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_29"),
				    (faction_slot_eq, "fac_kingdom_71", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_71", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom29_king"),
				    (faction_set_name, "fac_kingdom_71", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_30"),
				    (faction_slot_eq, "fac_kingdom_72", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_72", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom30_king"),
				    (faction_set_name, "fac_kingdom_72", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_31"),
				    (faction_slot_eq, "fac_kingdom_73", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_73", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom31_king"),
				    (faction_set_name, "fac_kingdom_73", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_32"),
				    (faction_slot_eq, "fac_kingdom_74", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_74", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom32_king"),
				    (faction_set_name, "fac_kingdom_74", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_33"),
				    (faction_slot_eq, "fac_kingdom_75", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_75", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom33_king"),
				    (faction_set_name, "fac_kingdom_75", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_34"),
				    (faction_slot_eq, "fac_kingdom_76", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_76", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom34_king"),
				    (faction_set_name, "fac_kingdom_76", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_35"),
				    (faction_slot_eq, "fac_kingdom_77", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_77", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom35_king"),
				    (faction_set_name, "fac_kingdom_77", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_36"),
				    (faction_slot_eq, "fac_kingdom_78", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_78", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom36_king"),
				    (faction_set_name, "fac_kingdom_78", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_37"),
				    (faction_slot_eq, "fac_kingdom_79", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_79", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom37_king"),
				    (faction_set_name, "fac_kingdom_79", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_38"),
				    (faction_slot_eq, "fac_kingdom_80", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_80", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom38_king"),
				    (faction_set_name, "fac_kingdom_80", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_39"),
				    (faction_slot_eq, "fac_kingdom_81", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_81", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom39_king"),
				    (faction_set_name, "fac_kingdom_81", s1),
					
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_40"),
				    (faction_slot_eq, "fac_kingdom_82", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_82", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom40_king"),
				    (faction_set_name, "fac_kingdom_82", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_41"),
				    (faction_slot_eq, "fac_kingdom_83", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_83", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom41_king"),
				    (faction_set_name, "fac_kingdom_83", s1),
							        (else_try),
		        	(eq, ":faction_of_troop_troop_4", "fac_kingdom_42"),
				    (faction_slot_eq, "fac_kingdom_84", slot_faction_state, 0),
				    (neg|faction_slot_eq, "fac_kingdom_84", slot_faction_state, 1),
				    (str_store_string, s1, "str_kaos_kingdom42_king"),
				    (faction_set_name, "fac_kingdom_84", s1),
		        (try_end),
			#####Kaos end add faction #####Above might be the culprit for the names issue.
			(try_end),
		]
	),	

#rubik Source code of Restoration
# restoration begin
  # Note: make sure there is a comma in the entry behind this one
  (168, #Kingdom restoration check, 24 default
    [
	
	  (try_begin),
		  (eq, "$kaos_restore", 1),
		  (assign, ":value_4", 1),
		  (try_for_range, ":troop_2", active_npcs_begin, "trp_knight_1_1_wife"),
	        (troop_slot_eq, ":troop_2", slot_troop_occupation, 2),
	        (troop_get_slot, ":faction_of_party_party_2", ":troop_2", slot_troop_original_faction),
	        (neg|faction_slot_eq, ":faction_of_party_party_2", slot_faction_state, 0),
	        (try_begin),
			#####Kaos begin add factions (for playing as king)
            	(eq,"$background_answer_3",cb_king),
			     (try_begin),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_1"),
			          (eq, "$kaos_kings_kingdom", 1),
			  		  (assign, ":value_4", 0),
			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_2"),
			          (eq, "$kaos_kings_kingdom", 2),
			  		  (assign, ":value_4", 0),
			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_3"),
			          (eq, "$kaos_kings_kingdom", 3),
			  		  (assign, ":value_4", 0),
			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_4"),
			          (eq, "$kaos_kings_kingdom", 4),
			  		  (assign, ":value_4", 0),
			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_5"),
			          (eq, "$kaos_kings_kingdom", 5),
			  		  (assign, ":value_4", 0),
			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_6"),
			          (eq, "$kaos_kings_kingdom", 6),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_7"),
			          (eq, "$kaos_kings_kingdom", 7),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_8"),
			          (eq, "$kaos_kings_kingdom", 8),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_9"),
			          (eq, "$kaos_kings_kingdom", 9),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_10"),
			          (eq, "$kaos_kings_kingdom", 10),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_11"),
			          (eq, "$kaos_kings_kingdom", 11),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_12"),
			          (eq, "$kaos_kings_kingdom", 12),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_13"),
			          (eq, "$kaos_kings_kingdom", 13),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_14"),
			          (eq, "$kaos_kings_kingdom", 14),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_15"),
			          (eq, "$kaos_kings_kingdom", 15),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_16"),
			          (eq, "$kaos_kings_kingdom", 16),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_17"),
			          (eq, "$kaos_kings_kingdom", 17),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_18"),
			          (eq, "$kaos_kings_kingdom", 18),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_19"),
			          (eq, "$kaos_kings_kingdom", 19),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_20"),
			          (eq, "$kaos_kings_kingdom", 20),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_papacy"),
			          (eq, "$kaos_kings_kingdom", 21),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_22"),
			          (eq, "$kaos_kings_kingdom", 22),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_23"),
			          (eq, "$kaos_kings_kingdom", 23),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_24"),
			          (eq, "$kaos_kings_kingdom", 24),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_25"),
			          (eq, "$kaos_kings_kingdom", 25),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_26"),
			          (eq, "$kaos_kings_kingdom", 26),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_27"),
			          (eq, "$kaos_kings_kingdom", 27),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_28"),
			          (eq, "$kaos_kings_kingdom", 28),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_29"),
			          (eq, "$kaos_kings_kingdom", 29),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_30"),
			          (eq, "$kaos_kings_kingdom", 30),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_31"),
			          (eq, "$kaos_kings_kingdom", 31),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_32"),
			          (eq, "$kaos_kings_kingdom", 32),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_33"),
			          (eq, "$kaos_kings_kingdom", 33),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_34"),
			          (eq, "$kaos_kings_kingdom", 34),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_35"),
			          (eq, "$kaos_kings_kingdom", 35),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_36"),
			          (eq, "$kaos_kings_kingdom", 36),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_37"),
			          (eq, "$kaos_kings_kingdom", 37),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_38"),
			          (eq, "$kaos_kings_kingdom", 38),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_39"),
			          (eq, "$kaos_kings_kingdom", 39),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_40"),
			          (eq, "$kaos_kings_kingdom", 40),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_41"),
			          (eq, "$kaos_kings_kingdom", 41),
			  		  (assign, ":value_4", 0),
					  			     (else_try),
			          (eq, ":faction_of_party_party_2", "fac_kingdom_42"),
			          (eq, "$kaos_kings_kingdom", 42),
			  		  (assign, ":value_4", 0),
			     (try_end),
	        (else_try),
			#####Kaos end add faction
	        	#(is_between, ":faction_of_party_party_2", "fac_player_supporters_faction", "fac_kingdom_43"), #New
				(is_between, ":faction_of_party_party_2", "fac_player_supporters_faction", "fac_kingdom_43"),
					        	#Default (is_between, ":faction_of_party_party_2", kingdoms_begin, "fac_kingdom_43"),
	        	(assign, ":value_4", 1),
	        (try_end),
			#####Kaos begin edit
			#####Kingdom restoration begin
			(try_begin),
				(eq, ":value_4", 1),
		        (store_troop_faction, ":script_param_2", ":troop_2"),
		        (neq, ":script_param_2", ":faction_of_party_party_2"),
		       
		        (assign, ":num_walled_centers", 0),
		        (try_for_range, ":party", walled_centers_begin, walled_centers_end),
		          (party_slot_eq, ":party", slot_town_lord, ":troop_2"),
		          (val_add, ":num_walled_centers", 1),
		        (try_end),
		        (gt, ":num_walled_centers", 0), ## has a walled center
		       
		        (store_sub, ":original_king", ":faction_of_party_party_2", fac_kingdom_1),
		        (val_add, ":original_king", "trp_kingdom_1_lord"),
		        (faction_set_slot, ":faction_of_party_party_2", slot_faction_leader, ":original_king"),
		       
		        (call_script, "script_change_troop_faction", ":troop_2", ":faction_of_party_party_2"),
		        (try_for_range, ":troop_2", active_npcs_begin, "trp_knight_1_1_wife"),
		          (troop_slot_eq, ":troop_2", slot_troop_occupation, 2),
		          (neg|is_between, ":troop_2", pretenders_begin, pretenders_end),
		          (neq, ":troop_2", ":troop_2"),
		          (troop_get_slot, ":original_faction_2", ":troop_2", slot_troop_original_faction),
		          (store_troop_faction, ":script_param_2", ":troop_2"),
		          (eq, ":original_faction_2", ":faction_of_party_party_2"),
		          (neq, ":script_param_2", ":faction_of_party_party_2"),
		          (troop_set_slot, ":troop_2", slot_troop_change_to_faction, ":faction_of_party_party_2"),
		        (try_end),
		        (call_script, "script_add_notification_menu", "mnu_notification_kingdom_restoration", ":troop_2", ":script_param_2"),
				#(call_script, "script_kaos_update_titles"), #Update titles on civil war.

		      (try_end),
			(try_end),
			#####Kingdom restoration end
#####Kaos end edit


	  (try_end),
    ]),
  ## restoration end
#rubik Source code of Restoration
#rubik Source code of Restoration
		#Kaos end
		######Kaos Safe end
#		  (-2.0, #Kingdom restoration check, 24 default
#    [
#(call_script, "script_kaos_update_titles"),
#
#]),




  
#  
  #Begin additional simple triggers for disasters
  (1, #Adjust timer for firing hour count script
  [ 
  #Begin choose faction-based interfaces if using WSE
#	(try_begin),
#    (neg|is_vanilla_warband), #Using WSE (neg means player must be using WSE, if the operation is only is_vanilla_warband that means only run tihs operation if the player is in vanilla mode.)
#    (try_begin),
#  	(this_or_next|key_is_down, key_v),
#	(key_clicked, key_v),
#	(val_add, "$g_mod_user_interface", 1),
#	      (assign, reg10, "$g_mod_user_interface"),
#          (str_clear, s10),
#          (str_store_string, s10, "@$g_mod_user_interface static value: {reg10}"),
#		  (display_message, s10),
#		  #(call_script, "script_sa_mod_replacement_materials"),
#	(try_end),
#	(try_begin),
#	(this_or_next|key_is_down, key_z),
#	(key_clicked, key_z),
#	(val_sub, "$g_mod_user_interface", 1),
#		  (assign, reg10, "$g_mod_user_interface"),
#          (str_clear, s10),
#          (str_store_string, s10, "@$g_mod_user_interface static value: {reg10}"),
#		  (display_message, s10),
#		  #(call_script, "script_sa_mod_replacement_materials"),
#	(try_end),
#	(try_end),
	#End choose faction-based interfaces if using WSE.
#####Debug begin
#          (assign, reg10, "$g_start_faction"),
#          (str_clear, s10),
#          (str_store_string, s10, "@$g_start_faction static value: {reg10}"),
#		  		  (display_message, s10),
#				  
#		  (store_faction_of_party, ":destnew", "p_main_party"),
#		  (assign, reg11, ":destnew"),
#          (str_clear, s11),
#          (str_store_string, s11, "@STORE FACTION OF PARTY p_main_party VALUE: {reg11}"),
#		  (display_message, s11),
#		  (assign, reg12, "$players_kingdom"),
#          (str_clear, s12),
#          (str_store_string, s12, "@$players_kingdom DYNAMIC Value: {reg12}"),
#		  (display_message, s12),
#####Debug End
#(try_begin),
#(lt, "$test1", 4),
#(val_add, "$test1", 1),
#(jump_to_menu, "mnu_event_27"),
#(try_end),

  ##(stop_all_sounds, 1), #Used to be value of 11new #Patch to fix looping sounds. moved to 24 hour trigger for performance.
     (try_begin),
      (ge, "$hourr_count", 24),
      (assign, "$hourr_count", 1),
	  (assign, "$lav_manor_fix", 0), #Disable manor fix once a day.
    (else_try),
      (val_add, "$hourr_count", 1),
    (try_end),
  
   (try_begin),
      (eq, "$hourr_count", 15),
      (store_random_in_range, "$disaster_occur_time", 1, 25),
    (try_end),
	
	
    (try_begin),
	(eq, "$player_disasters", 1),
      (eq, "$hourr_count", "$disaster_occur_time"),
	  #(this_or_next|ge, "$hourr_count", "$disaster_occur_time"), #For debug forces disasters to occur
	  #(le, "$hourr_count", "$disaster_occur_time"), #For debug forces disasters to occur
	  
      (party_get_current_terrain, ":terrain", "p_main_party"),
      (store_random_in_range, ":chance", 0, 20), #20 default #Adjust chance for player chance
      (try_begin),
        (this_or_next|eq, ":terrain", 4), #If snow
		(this_or_next|eq, ":terrain", 7), #If Bridge (Water I think)
		(this_or_next|eq, ":terrain", 0), #If Water
		(this_or_next|eq, ":terrain", 8), #If River
		(eq, ":terrain", 12), #If snow forest
        (eq, ":chance", 0),
        #(neq, "$g_starting_faction", "fac_kingdom_1"),
        #(neq, "$g_starting_faction", "fac_kingdom_10"),
        #(neq, "$g_starting_faction", "fac_kingdom_12"),
        #(neq, "$g_starting_faction", "fac_kingdom_16"),
        #(neq, "$g_starting_faction", "fac_kingdom_29"),
        #(neq, "$g_starting_faction", "fac_kingdom_30"),
        #(neq, "$g_starting_faction", "fac_kingdom_47"),
        #(neq, "$g_starting_faction", "fac_kingdom_48"),
        #(neq, "$g_starting_faction", "fac_kingdom_50"),
        #(neq, "$g_starting_faction", "fac_kingdom_52"),
        #(neq, "$g_starting_faction", "fac_kingdom_53"),
        #(neq, "$g_starting_faction", "fac_kingdom_54"),
		
		
		##CHECK IF PLAYER IS IN TOWN BEGIN
		(le, "$g_last_rest_center", 0), #0 & -1 = Player not resting.
		#	(assign, reg10, "$g_last_rest_center"), #Value of -1 when not resting
		#	 (str_clear, s10),
		#  (str_store_string, s10, "@New agent: {reg10}"),
		#  (display_message, s10),
		##CHECK IF PLAYER IS IN TOWN END
		
		
        (party_relocate_near_party, "p_disaster_ice_ply", "p_main_party", 0),
        (party_set_flags, "p_disaster_ice_ply", pf_disabled, 0),
        (display_message, "str_disaster_coldbringer", 0x00FF0000),
        (play_sound, "snd_Typhoon"),
        (assign, "$ply_timer_fall_disaster", 24),
		
		
		  (party_get_skill_level, ":skill_slot", "p_main_party", "skl_pathfinding"),
  (party_get_skill_level, ":skill_spotting", "p_main_party", "skl_spotting"),
  #(store_skill_level, ":skill_slot", "skl_pathfinding", "trp_player"),
  #(store_skill_level, ":skill_spotting", "skl_spotting", "trp_player"),
        (val_add, ":skill_slot", ":skill_spotting"),

#	Debug Mode Begin
#          (assign, reg10, ":skill_slot"),
#          (str_clear, s10),
#          (str_store_string, s10, "@LEVELS: {reg10}"),
#		  (display_message, s10),
#	Debug Mode End

        (store_random_in_range, ":chance_skill", 0, 12),
		(try_begin), #Can be used to disallow chance of death
          (lt, ":chance_skill", ":skill_slot"),
          (display_message, "str_logistics_avoid", 0x0000FF00), 
	        (else_try), #Previously else_try
          (call_script, "script_party_army_size_execute", "p_main_party", 2, 3),
		  (call_script, "script_change_player_party_morale", -20),
          #(call_script, "script_moral_level_diff", "p_main_party", -30),
          #(call_script, "script_wm_after_battle_health_result"),
         # (call_script, "script_stack_kill_sc", 25, 0, 1, 1),
        (try_end),

		
      (else_try),
        (this_or_next|eq, ":terrain", 5), #If desert
		(eq, ":terrain", 13), #If desert forest
        (eq, ":chance", 0),
        #(neq, "$g_starting_faction", "fac_kingdom_2"),
        #(neq, "$g_starting_faction", "fac_kingdom_3"),
        #(neq, "$g_starting_faction", "fac_kingdom_4"),
        #(neq, "$g_starting_faction", "fac_kingdom_6"),
        #(neq, "$g_starting_faction", "fac_kingdom_9"),
        #(neq, "$g_starting_faction", "fac_kingdom_13"),
        #(neq, "$g_starting_faction", "fac_kingdom_14"),
        #(neq, "$g_starting_faction", "fac_kingdom_21"),
        #(neq, "$g_starting_faction", "fac_kingdom_22"),
        #(neq, "$g_starting_faction", "fac_kingdom_30"),
        #(neq, "$g_starting_faction", "fac_kingdom_31"),
        #(neq, "$g_starting_faction", "fac_kingdom_32"),
        #(neq, "$g_starting_faction", "fac_kingdom_34"),
        #(neq, "$g_starting_faction", "fac_kingdom_40"),
        #(neq, "$g_starting_faction", "fac_kingdom_41"),
        #(neq, "$g_starting_faction", "fac_kingdom_44"),
        #(neq, "$g_starting_faction", "fac_kingdom_49"),
        #(neq, "$g_starting_faction", "fac_kingdom_51"),
        #(neq, "$g_starting_faction", "fac_kingdom_52"),
        #(neq, "$g_starting_faction", "fac_africa_people"),
        #(neq, "$g_starting_faction", "fac_hindu_people"),
        #(neq, "$g_starting_faction", "fac_arabian_people"),
				
		
		##CHECK IF PLAYER IS IN TOWN BEGIN
		(le, "$g_last_rest_center", 0), #0 & -1 = Player not resting.
		#	(assign, reg10, "$g_last_rest_center"), #Value of -1 when not resting
		#	 (str_clear, s10),
		#  (str_store_string, s10, "@New agent: {reg10}"),
		#  (display_message, s10),
		##CHECK IF PLAYER IS IN TOWN END
		
		
        (party_relocate_near_party, "p_disaster_sand_ply", "p_main_party", 0),
        (party_set_flags, "p_disaster_sand_ply", pf_disabled, 0),
        (display_message, "str_disaster_sand_storm", 0x00FF0000),
        (play_sound, "snd_Typhoon"),
        (assign, "$ply_timer_fall_disaster", 24),

		
		  (party_get_skill_level, ":skill_slot", "p_main_party", "skl_pathfinding"),
  (party_get_skill_level, ":skill_spotting", "p_main_party", "skl_spotting"),
  
#		  (store_skill_level, ":skill_slot", "skl_pathfinding", "trp_player"),
 # (store_skill_level, ":skill_spotting", "skl_spotting", "trp_player"),
        (val_add, ":skill_slot", ":skill_spotting"),

#	Debug Mode Begin
#          (assign, reg10, ":skill_slot"),
#          (str_clear, s10),
#          (str_store_string, s10, "@LEVELS: {reg10}"),
#		  (display_message, s10),
#	Debug Mode End
        (store_random_in_range, ":chance_skill", 0, 12),
		
			 (try_begin),
          (lt, ":chance_skill", ":skill_slot"),
          (display_message, "str_logistics_avoid", 0x0000FF00),
			        (else_try), #Previously else_try
          (call_script, "script_party_army_size_execute", "p_main_party", 3, 3),
		  (call_script, "script_change_player_party_morale", -30),
          #(call_script, "script_moral_level_diff", "p_main_party", -30),
          #(call_script, "script_wm_after_battle_health_result"),
         # (call_script, "script_stack_kill_sc", 25, 0, 1, 1),
        (try_end),

	
		
      (else_try),
	  		(this_or_next|eq, ":terrain", 1), #If mountain
        (this_or_next|eq, ":terrain", 2), #If steppe
		(this_or_next|eq, ":terrain", 3), #If plain
		(this_or_next|eq, ":terrain", 9), #If Mountain Forest
		(this_or_next|eq, ":terrain", 10), #If Steppe Forest
        (eq, ":terrain", 11), #If Plain Forest
        (eq, ":chance", 0),
				
		
		##CHECK IF PLAYER IS IN TOWN BEGIN
		(le, "$g_last_rest_center", 0), #0 & -1 = Player not resting.
		#	(assign, reg10, "$g_last_rest_center"), #Value of -1 when not resting
		#	 (str_clear, s10),
		#  (str_store_string, s10, "@New agent: {reg10}"),
		#  (display_message, s10),
		##CHECK IF PLAYER IS IN TOWN END
		
		
        (party_relocate_near_party, "p_disaster_storm_ply", "p_main_party", 0),
        (party_set_flags, "p_disaster_storm_ply", pf_disabled, 0),
        (display_message, "str_disaster_storm", 0x00FF0000),
        (play_sound, "snd_Flood"),
        (assign, "$ply_timer_fall_disaster", 24),
        
  (party_get_skill_level, ":skill_slot", "p_main_party", "skl_pathfinding"),
  (party_get_skill_level, ":skill_spotting", "p_main_party", "skl_spotting"),
  #(store_skill_level, ":skill_slot", "skl_pathfinding", "trp_player"),
  #(store_skill_level, ":skill_spotting", "skl_spotting", "trp_player"),
  (val_add, ":skill_slot", ":skill_spotting"),

#	Debug Mode Begin
#          (assign, reg10, ":skill_slot"),
#          (str_clear, s10),
#          (str_store_string, s10, "@LEVELS: {reg10}"),
#		  (display_message, s10),
#	Debug Mode End
        (store_random_in_range, ":chance_skill", 0, 12),
	
	        (try_begin),
          (lt, ":chance_skill", ":skill_slot"),
          (display_message, "str_navigation_avoid", 0x0000FF00),
		   (else_try), #Previously else_try
          (call_script, "script_party_army_size_execute", "p_main_party", 1, 3),
		  (call_script, "script_change_player_party_morale", -10),
          #(call_script, "script_moral_level_diff", "p_main_party", -30),
          #(call_script, "script_wm_after_battle_health_result"),
         # (call_script, "script_stack_kill_sc", 25, 0, 1, 1),
        (try_end),

	

        (try_end),
      (try_end),
    #(try_end),

    (try_begin),

      (gt, "$ply_timer_fall_disaster", 0),
      (val_sub, "$ply_timer_fall_disaster", 1),
    (else_try),
      (eq, "$ply_timer_fall_disaster", 0),
      (party_set_flags, "p_disaster_storm_ply", pf_disabled, 1),
      (party_set_flags, "p_disaster_sand_ply", pf_disabled, 1),
      (party_set_flags, "p_disaster_ice_ply", pf_disabled, 1),
    (try_end),
	(eq, "$player_disasters", 1),
    (call_script, "script_morale_train_event", "p_main_party"), #TRY_END ERROR!!!

 #If we wish to include provinces
  #try_for_range, ":var4", "fac_kingdom_1", "fac_kingdoms_end"), #C
  #(faction_slot_eq, ":var4", 30, 0), #Is faction Active? #C
  ##(display_message, "@#AI MODULE_SCRIPTS TEST"),
	#  (try_for_range, ":var22", 56, 76),
	##  (display_message, "@#AI MODULE_SCRIPTS TESXXXXXXXX"),
  #(faction_get_slot, ":var0", ":var4", ":var22"), #C
	## (display_message, "@#AI MODULE_SCRIPTS TESTGGGGGGGGGGGG"),
	##If we wish to include
	
  #Kalarhan code begin

  
  #Optimization
  (store_random_in_range, ":optimize", 0, 10), #40 #10% chance of AI being struck, thus increase chance 10-fold to counter, now in batches.
  (eq, "$ai_disasters", 1),
  (eq, ":optimize", 0),
   #(display_message, "@Firing the try for parties."),
  #Optimization
  
  (try_for_parties, ":var0"), # all parties at that moment: towns, armies, bridges, armies destroyed but still not deleted from memory, etc
  (party_is_active, ":var0"), # makes sure this party is not about to be deleted, like a army that lost all troops and its just waiting the engine to remove it
  (party_slot_eq, ":var0", slot_party_type, spt_kingdom_hero_party), # is a army leaded by a hero unit, like a faction lord
  (party_stack_get_troop_id, ":leader", ":var0", 0), # as said above, the first troop is the leader
  (is_between, ":leader", "trp_kingdom_1_lord", "trp_knight_1_1_wife"), # here you can put a filter to what kind of troops. Just kings, kings and lords, kings/lords/pretenders, etc. See module_constants and module_troops
  # use this_or_next if you need to test multiple ranges
  #... do stuff with the party
  # remember that a lord party may be inside a town (attached), in case it matters or not, can be in a battle, etc
  #Kalarhan code end
  (party_get_attached_to, ":attached_party", ":var0"),
  (eq, ":attached_party", -1),
        (party_get_battle_opponent, ":var23", ":var0"),
		(try_begin),
		(eq, ":var23", -1), #Party not in battle
		(call_script, "script_morale_train_event", ":var0"),
		(try_end),
		(try_begin),
          (eq, ":var23", -1), #Party not in battle
          (store_random_in_range, ":var19", 0, 120), #30 #Old chance pre-optimize = 1200, new chance = 120 300 chance of AI being affected DEFAULT #Adjust chance for AI.
          (try_begin),
            (eq, ":var19", 0),
			(call_script, "script_ai_suffer_storm", ":var0", 1),
            #(call_script, "script_ai_suffer_storm", ":var0", 1, ":var4"),
		  #(display_message, s10),
          (else_try),
            (eq, ":var19", 1),
			(call_script, "script_ai_suffer_storm", ":var0", 2),
            #(call_script, "script_ai_suffer_storm", ":var0", 2, ":var4"),
          (else_try),
            (eq, ":var19", 2),
			(call_script, "script_ai_suffer_storm", ":var0", 3),
            #(call_script, "script_ai_suffer_storm", ":var0", 3, ":var4"), #If we wish to include provinces we use this and uncomment: #(store_script_param, ":var2", 3), in module_scripts ai_suffer_storm
          (try_end),
        (try_end),
		(try_end), #Tryforparties
  ]),




]