from header_common import *
from header_operations import *
from header_presentations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *
from module_items import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

coop_scripts = [

   ("coop_troop_can_use_item",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
      (store_script_param, ":troop", 1),
      (store_script_param, ":item", 2),
      (store_script_param, ":item_modifier", 3),

      (item_get_difficulty, ":difficulty", ":item"),
      (item_get_type, ":type", ":item"),

      (try_begin),
        (eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
      (else_try),
        (eq, ":item_modifier", imod_stubborn),
        (val_add, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_timid),
        (val_sub, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_heavy),
        (neq, ":type", itp_type_horse),
        (val_add, ":difficulty", 1),	  
      (else_try),
        (eq, ":item_modifier", imod_strong),
        (val_add, ":difficulty", 2),	  
      (else_try),
        (eq, ":item_modifier", imod_masterwork),
        (val_add, ":difficulty", 4),	  
      (try_end),
	  	  
      (try_begin),
        (eq, ":type", itp_type_horse),
        (store_skill_level, ":skill_level_leadership_var_1", skl_riding, ":troop"),
      (else_try),
        (eq, ":type", itp_type_shield),
        (store_skill_level, ":skill_level_leadership_var_1", skl_shield, ":troop"),
      (else_try),
        (eq, ":type", itp_type_bow),
        (store_skill_level, ":skill_level_leadership_var_1", skl_power_draw, ":troop"),
      (else_try),
        (eq, ":type", itp_type_thrown),
        (store_skill_level, ":skill_level_leadership_var_1", skl_power_throw, ":troop"),
      (else_try),
        (store_attribute_level, ":skill_level_leadership_var_1", ":troop", ca_strength),
      (try_end),
      
      (try_begin),
        (lt, ":skill_level_leadership_var_1", ":difficulty"),
        (assign, reg0, 0),
      (else_try),
        (assign, reg0, 1),
      (try_end),

    (try_end),
   ]),


 #
 # script_coop_on_admin_panel_load
  ("coop_on_admin_panel_load",
    [
        # (assign, "$coop_battle_state", coop_battle_state_setup_mp), #debug
        # (assign, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
      (try_begin), 
        (neg|is_vanilla_warband),
        (dict_create, "$coop_dict"),
        (dict_load_file, "$coop_dict", "@coop_battle", 2),

        (dict_get_int, "$coop_battle_state", "$coop_dict", "@battle_state"), # 0 = no battle 1 = is setup 2 = is done
        (eq, "$coop_battle_state", coop_battle_state_setup_sp),
        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_setup_mp), # disable starting twice
        (assign, "$coop_battle_state", coop_battle_state_setup_mp),
        (dict_save, "$coop_dict", "@coop_battle"),

#PREPARE TO CREATE PARTIES
        #assigning constants before copy reg to parties
        (assign, "$coop_cur_temp_party_enemy", coop_temp_party_enemy_begin), #store current spawn party
        (assign, "$coop_cur_temp_party_ally", coop_temp_party_ally_begin), #store current spawn party
        (assign, "$coop_main_party_spawn", coop_temp_party_ally_begin), #main party spawn party

        (call_script, "script_coop_copy_file_to_parties_mp"),	#also copies admin settings to variables

#CHANGE ADMIN PANEL

        (dict_get_int, ":garrison_commander_party", "$coop_dict", "@p_castle_lord"),
        (dict_get_int, ":garrison_party", "$coop_dict", "@p_garrison"),
        (dict_get_int, "$coop_castle_banner", "$coop_dict", "@p_garrison_banner"),
        (dict_get_int, "$coop_battle_type", "$coop_dict", "@map_type"),

        (try_begin),
          (eq, "$coop_battle_type", coop_battle_type_field_battle), #field battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_village_player_attack), #village battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_enemy_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_enemy_begin, ":garrison_party"), #garrison is first enemy party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_village_player_defend), #village battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_ally_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_ally_begin, ":garrison_party"), #garrison is first ally party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_siege_player_attack),#player attacking siege
          (assign, ":coop_game_type", multiplayer_game_type_coop_siege),
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_enemy_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_enemy_begin, ":garrison_party"), #garrison is first enemy party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_siege_player_defend), #player defending siege
          (assign, ":coop_game_type", multiplayer_game_type_coop_siege), 
          (assign, "$attacker_team", 0),
          (assign, "$defender_team", 1),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_ally_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_ally_begin, ":garrison_party"), #garrison is first ally party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_bandit_lair), #bandit lair battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          # (mission_tpl_entry_set_override_flags, "mt_coop_battle", 0, af_override_horse), #NEW
        (else_try),
          (assign, ":coop_game_type", multiplayer_game_type_deathmatch), #cant find type
        (try_end),
        (assign, "$g_multiplayer_game_type", ":coop_game_type"),

        (assign, "$g_multiplayer_selected_map", "scn_random_multi_plain_medium"),
        (dict_get_int, "$coop_battle_scene", "$coop_dict", "@map_scn"),
        (dict_get_int, "$coop_castle_scene", "$coop_dict", "@map_castle"),
        (dict_get_int, "$coop_street_scene", "$coop_dict", "@map_street"),
        (dict_get_int, "$coop_map_party", "$coop_dict", "@map_party_id"),
      #set weather
        (dict_get_int, "$coop_time_of_day", "$coop_dict", "@map_time"),
        (dict_get_int, "$coop_cloud", "$coop_dict", "@map_cloud"),
        (dict_get_int, "$coop_haze", "$coop_dict", "@map_haze"),
        (dict_get_int, "$coop_rain", "$coop_dict", "@map_rain"),#0=none 1=rain 2=snow

        (assign, "$g_multiplayer_ready_for_spawning_agent", 0), #dont start battle yet
        (assign, "$coop_round", coop_round_battle),

        (assign, "$coop_team_1_troop_num", "$coop_num_bots_team_1"),
        (assign, "$coop_team_2_troop_num", "$coop_num_bots_team_2"),

        #set team ratios
        (assign, ":num_bots_team_1", "$coop_num_bots_team_1"),
        (assign, ":num_bots_team_2", "$coop_num_bots_team_2"),
        (val_max, ":num_bots_team_1", 1),

        (dict_get_int, ":battle_advantage", "$coop_dict", "@battle_adv"),#clamp(((15.0f + advantage) / 15.0f), 0.2f, 2.5f) * number of allies

        (val_mul, ":battle_advantage", 1000),
        (val_add, ":battle_advantage", 15000),
        (val_div, ":battle_advantage", 15),
        (val_clamp, ":battle_advantage", 200, 2500),
        # (val_clamp, ":battle_advantage", 700, 1500),

        (try_begin),
          (eq, "$coop_battle_type", coop_battle_type_bandit_lair), #ignore advantage for bandit lair battle
          (assign, ":battle_advantage", 200),
        (try_end),
        (val_mul, ":num_bots_team_2", ":battle_advantage"),
        (store_div, "$coop_team_ratio", ":num_bots_team_2", ":num_bots_team_1"), #(ratio / 1000) * team 1 = team 2
        (val_clamp, "$coop_team_ratio", 500, 2000), #clamp to 0.5 ~ 2.0 (this ends up reducing the effect of battle advantage)

        (dict_get_str, s0, "$coop_dict", "@tm1_name"),
        (faction_set_name, "fac_player_supporters_faction", s0),
        (dict_get_int, "$coop_team_1_faction", "$coop_dict", "@tm0_fac"),
        (dict_get_int, "$coop_team_2_faction", "$coop_dict", "@tm1_fac"),

        #battle size limit
        (try_begin),
          (lt, "$coop_battle_size", coop_min_battle_size), #min setting
          (assign, "$coop_battle_size",  coop_def_battle_size), #default battle size
        (try_end),
		
#Numerical settings template step 2 begin
        (try_begin),
          (lt, "$torch_chance_coop", coop_torch_chance_min), #min setting
          (assign, "$torch_chance_coop",  coop_torch_chance_max), #default battle size
        (try_end),
#Numerical settings template step 2 end

#Numerical settings template step 2 begin
        (try_begin),
          (lt, "$tom_sand_storm_chance", coop_sandstorm_chance_min), #min setting
          (assign, "$tom_sand_storm_chance",  coop_sandstorm_chance_max), #default battle size
        (try_end),
#Numerical settings template step 2 end

      (try_for_range, reg1, 0, 9),
        (dict_get_str, s1, "$coop_dict", "@cls{reg1}_name"),
        (class_set_name, reg1, s1),
      (try_end),

        (assign, "$g_multiplayer_respawn_period", 0), 
        (assign, "$g_multiplayer_factions_voteable", 0), #dont allow these
        (assign, "$g_multiplayer_maps_voteable", 0),    #dont allow these
        (assign, "$g_multiplayer_auto_team_balance_limit", 1000), #set for some scripts but dont show in admin panel
        (assign, "$g_multiplayer_num_bots_voteable", -1), 
		#(assign, "$ai_crouch_mode", 0), #Value 0 to 2, 0 = Crouch & Low Walk, 1 = Crouch only, 2 = No crouching & no low walk
		#
		   # (assign, "$setting_use_dmod", 1), #Commented out in V1.001
			#(call_script, "script_init_item_score"), #No Clue what this is either #Commented out in V1.001
			#(item_set_slot, 20, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(item_set_slot, 11, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(item_set_slot, 19, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(set_fixed_point_multiplier, 100), #Not sure what this is for #Commented out in V1.001
		#	#(set_shader_param_float, "@vFresnelMultiplier", 15),
		#	#(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, 2),
			#(assign, "$g_player_luck", 200), #Not sure what this is #Commented out in V1.001
		#	#(troop_set_slot, "trp_player", slot_troop_occupation, 2),
		#	#(store_random_in_range, ":random_in_range_training_ground_bridge_1", "p_training_ground", "p_bridge_1"),
		#	#(party_relocate_near_party, "p_main_party", ":random_in_range_training_ground_bridge_1", 3),
		#	#(str_store_troop_name, 5, "trp_player"),
		#	#(party_set_name, "p_main_party", 5),
		#	#(call_script, "script_update_party_creation_random_limits"),
		#	#Global variables added below
		#	#Begin add AI Crouching
			#(assign, "$key_crouch", key_caps_lock),
			(assign, "$key_crouch", key_z),
            (assign,"$key_crouch_command", key_comma),
            (assign,"$key_stand_command", key_period),
			(assign,"$g_crouch_speed_limiter", 1),
			#END AI Crouching, files affected: Module_Constants, Module_Scripts (Here and below), module_mission_templates, module_animations, and animacoins.brf last mesh, also probably ani_sneak was removed
			#from load_mod_resource, and instead load_resource ani_crouch and ani_low_walk were probably added.
			#Disable/Enable variables below
			# Not needed (assign, "$battle_time", 1), # look for (eq, "$battle_time", 1), # only shows this if the global is 1 in module_game_menus.
			#(assign, "$ai_crouch_mode", 0), #Commented out in V1.001 #Value 0 to 2, 0 = Crouch & Low Walk, 1 = Crouch only, 2 = No crouching & no low walk
			#(assign, "$coop_desertv3", 0), #Example on how to generate terrain must make it (1) when its scene is set below.
			#1 = Enabled, 0 = disabled (at start if mod option exist in module_presentations)
			#(assign, "$g_player_party_icon", -1), #Not sure if needed #Commented out in V1.001
			#(assign, "$crusade_time", 0), #SP Only
			#(assign, "$g_travel_speed", 75),
			#(assign, "$g_last_payday", 0),
			#(assign, "$g_player_crusading", 0),
			#(assign, "$sp_shield_bash_coop", 1),
			#(assign, "$sp_shield_bash_ai_coop", 0),
			#(assign, "$setting_use_spearwall", 1),

			#(assign, "$g_battle_preparation", -1), # Not sure #Commented out in V1.001
			#(assign, "$g_battle_preparation_phase", 0), # Not sure #Commented out in V1.001
			(assign, "$g_rand_rain_limit", 30), #Commented out in V1.001
			#(assign, "$belfry_sound", 0), #Commented out in V1.001
			#(assign, "$g_reinforcement_waves", 2), #Keep it and see how it goes #Commented out in V1.001
			#Numerical Settings Template Extension begin make sure to edit module_constants def value as well, as the other one here.
			#(assign, "$tom_sand_storm_chance", 20), # Default 20, 100 for testing only.
			#(assign, "$torch_chance_coop", 3), #25% Chance = 25
			#Numerical Settings Template Extension end
			#Must add weapon break, sandstorms, scene effects to Multiplayer as well.
		#	(assign, "$g_faction_names", 0), #SP Only
		#	(assign, "$g_unit_names", 0), #SP Only
			(assign, "$tom_use_banners", 1),
			(assign, "$tom_bonus_banners", 1),
			(assign, "$tom_use_battlefields", 1),
			#(assign, "$tom_weapon_break", 1),
			#(assign, "$tom_lance_breaking", 1),
			(assign, "$coop_generate_reduction", 1),
		#	(assign, "$tom_difficulty_wages", 1),
		#	(assign, "$tom_difficulty_fief", 1),
		#	(assign, "$tom_difficulty_enterprise", 1),
		#	(assign, "$feudal_inefficency", 0),
		#	(assign, "$start_player_crusade", 0),
			#(assign, "$crusader_faction", -5), ##Commented out in V1.001
		#	(assign, "$crusade_start", 0),
		#	(assign, "$crusade_target", 0),
		##	(assign, "$crusade_target_faction", 0),
			#(assign, "$crusader_party_id", -1), #Commented out in V1.001
			#(assign, "$crusader_state", -1), #Commented out in V1.001
			#(assign, "$freelancer_state", 0), #Commented out in V1.001
			#(assign, "$men_are_pleased", 0), #Commented out in V1.001
			#(assign, "$tom_use_longships", 1), #Commented out in V1.001
			#(assign, "$use_feudal_lance", 1), #Commented out in V1.001
		#	(assign, "$use_player_auxiliary", 1), #Not needed for MP
		#	(assign, "$retinue_noble_balt", 0),
		#	(assign, "$retinue_noble_west", 0),
		#	(assign, "$retinue_noble_orthodox", 0),
		#	(assign, "$retinue_noble_muslim", 0),
		#	(assign, "$retinue_noble_mongol", 0),
		#	(assign, "$lance_troop_serving", 0),
		#	(assign, "$lance_troop_reserve", 0),
		#	(assign, "$crusader_order_joined", 0),
		#	(assign, "$culture_pool", 0),
		#	(assign, "$culture_pool_initialized", 0),
		
			
			(assign, "$historical_banners", 1),
			(assign, "$randomize_player_shield", 1),
		#	(assign, "$disable_sisterly_advice", 1),
		#	(assign, "$disable_local_histories", 1),
		#	(assign, "$player_crowned", 0),
		#	(assign, "$default_battle_size", 0),
		#	(assign, "$default_orignal_battle_size", 0),
#
#
#
#
#
#
#
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_add_to_servers_list, "$coop_set_add_to_servers_list"),
        # (multiplayer_send_int_to_server, multiplayer_event_admin_set_anti_cheat, "$coop_set_anti_cheat"),
		(multiplayer_send_int_to_server, multiplayer_event_admin_set_max_num_players, "$coop_set_max_num_players"),
        #(multiplayer_send_int_to_server, multiplayer_event_admin_set_max_num_players, "$coop_set_max_num_players"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_melee_friendly_fire, "$coop_set_melee_friendly_fire"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire, "$coop_set_friendly_fire"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire_damage_self_ratio, "$coop_set_friendly_fire_damage_self_ratio"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire_damage_friend_ratio, "$coop_set_friendly_fire_damage_friend_ratio"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_ghost_mode, "$coop_set_ghost_mode"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_control_block_dir, "$coop_set_control_block_dir"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_combat_speed, "$coop_set_combat_speed"),
#Extend


#End Extension
        #these are only set in script_coop_copy_reg_to_settings
        # (assign, "$g_multiplayer_kick_voteable", 1),
        # (assign, "$g_multiplayer_ban_voteable", 1),
        # (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
        # (assign, "$g_multiplayer_player_respawn_as_bot", 0),
      (dict_save, "$coop_dict", "@coop_battle"),
      (dict_free, "$coop_dict"),

	  (display_message, "@Protip: Some of the settings are grabbed from Single Player, and some settings are saved from Co-Op into future Co-Op sessions in your save.", 0x0016fc07),
	  (display_message, "@Make sure the following ports are forwarded so other players can join: 7240, 7241, 7242 TCP & UDP.", 0x0016fc07),
	  (display_message, "@Only the host needs to use WSE, joining players can join without using WSE!", 0x0016fc07),
        #Edited Message ENVFIX(display_message, "@Admin panel set."),

      (try_end),
     ]),	
  

  # script_coop_copy_settings_to_file
  ("coop_copy_settings_to_file",
   [
#SP: setup battle
#MP: at battle end
    (try_begin), 
      (neg|is_vanilla_warband),
      (try_begin),
        (game_in_multiplayer_mode),#copy setting at end of battle (only ones that use native variables that may be changed in other modes)
        (server_get_add_to_game_servers_list, "$coop_set_add_to_servers_list"),
        # (server_get_anti_cheat, "$coop_set_anti_cheat"),
        (server_get_max_num_players, "$coop_set_max_num_players"),
        (server_get_friendly_fire, "$coop_set_friendly_fire"),
        (server_get_melee_friendly_fire, "$coop_set_melee_friendly_fire"),
        (server_get_friendly_fire_damage_self_ratio, "$coop_set_friendly_fire_damage_self_ratio"),
        (server_get_friendly_fire_damage_friend_ratio, "$coop_set_friendly_fire_damage_friend_ratio"),
        (server_get_ghost_mode, "$coop_set_ghost_mode"),
        (server_get_control_block_dir, "$coop_set_control_block_dir"),
        (server_get_combat_speed, "$coop_set_combat_speed"),
      (try_end),

      (dict_set_int, "$coop_dict", "@srvr_set0", "$coop_set_add_to_servers_list"),
      # (dict_set_int, "$coop_dict", "@srvr_set1", "$coop_set_anti_cheat"),
      (dict_set_int, "$coop_dict", "@srvr_set2", "$coop_set_max_num_players"),
      (dict_set_int, "$coop_dict", "@srvr_set3", "$coop_battle_size"),
      (dict_set_int, "$coop_dict", "@srvr_set4", "$coop_set_melee_friendly_fire"),
      (dict_set_int, "$coop_dict", "@srvr_set5", "$coop_set_friendly_fire"),
      (dict_set_int, "$coop_dict", "@srvr_set6", "$coop_set_friendly_fire_damage_self_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set7", "$coop_set_friendly_fire_damage_friend_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set8", "$coop_set_ghost_mode"),
      (dict_set_int, "$coop_dict", "@srvr_set9", "$coop_set_control_block_dir"),
      (dict_set_int, "$coop_dict", "@srvr_set10", "$coop_set_combat_speed"),
      (dict_set_int, "$coop_dict", "@srvr_set11", "$coop_battle_spawn_formation"),
      (dict_set_int, "$coop_dict", "@srvr_set12", "$g_multiplayer_kick_voteable"),
      (dict_set_int, "$coop_dict", "@srvr_set13", "$g_multiplayer_ban_voteable"),
      (dict_set_int, "$coop_dict", "@srvr_set14", "$g_multiplayer_valid_vote_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set15", "$g_multiplayer_player_respawn_as_bot"),
      (dict_set_int, "$coop_dict", "@srvr_set16", "$coop_skip_menu"),
      (dict_set_int, "$coop_dict", "@srvr_set17", "$coop_disable_inventory"),
      (dict_set_int, "$coop_dict", "@srvr_set18", "$coop_reduce_damage"),
      (dict_set_int, "$coop_dict", "@srvr_set19", "$coop_no_capture_heroes"),


		#Extend to further commands

				(dict_set_int, "$coop_dict", "@srvr_set20", "$sp_shield_bash_coop"),
				#(dict_set_int, "$coop_dict", "@srvr_set21", "$historical_banners"),
				#(dict_set_int, "$coop_dict", "@srvr_set22", "$randomize_player_shield"),
				(dict_set_int, "$coop_dict", "@srvr_set23", "$coop_extended_camera"),
				(dict_set_int, "$coop_dict", "@srvr_set24", "$sp_shield_bash_ai_coop"),
				#####Begin torch data from save game
				(dict_set_int, "$coop_dict", "@srvr_set25", "$torch_chance_coop"),
				#####End torch data from save game
				(dict_set_int, "$coop_dict", "@srvr_set26", "$tom_sand_storm_chance"),
				(dict_set_int, "$coop_dict", "@srvr_set27", "$tom_sand_storm"),
				(dict_set_int, "$coop_dict", "@srvr_set28", "$voice_set"),
				(dict_set_int, "$coop_dict", "@srvr_set29", "$experimental_archers"),
				(dict_set_int, "$coop_dict", "@srvr_set30", "$g_doghotel_enable_brainy_bots"),
				###Dict Get & Dict Set changes the options in SP after using multiplayer results
	#Dosen't seem to be needed!	

		
		###End extension
		#Might need optimization..
		
		
		
		
		
		
    (try_end),
     ]),	


  # script_coop_copy_file_to_settings
  ("coop_copy_file_to_settings",
   [
#MP: before admin panel
#SP: when use results
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_get_int, "$coop_set_add_to_servers_list", "$coop_dict", "@srvr_set0"),
      # (dict_get_int, "$coop_set_anti_cheat", "$coop_dict", "@srvr_set1"),
      (dict_get_int, "$coop_set_max_num_players", "$coop_dict", "@srvr_set2"),
      (dict_get_int, "$coop_battle_size", "$coop_dict", "@srvr_set3"),
      (dict_get_int, "$coop_set_melee_friendly_fire", "$coop_dict", "@srvr_set4"),
      (dict_get_int, "$coop_set_friendly_fire", "$coop_dict", "@srvr_set5"),
      (dict_get_int, "$coop_set_friendly_fire_damage_self_ratio", "$coop_dict", "@srvr_set6"),
      (dict_get_int, "$coop_set_friendly_fire_damage_friend_ratio", "$coop_dict", "@srvr_set7"),
      (dict_get_int, "$coop_set_ghost_mode", "$coop_dict", "@srvr_set8"),
      (dict_get_int, "$coop_set_control_block_dir", "$coop_dict", "@srvr_set9"),
      (dict_get_int, "$coop_set_combat_speed", "$coop_dict", "@srvr_set10"),
      (dict_get_int, "$coop_battle_spawn_formation", "$coop_dict", "@srvr_set11"),
      (dict_get_int, "$g_multiplayer_kick_voteable", "$coop_dict", "@srvr_set12"),
      (dict_get_int, "$g_multiplayer_ban_voteable", "$coop_dict", "@srvr_set13"),
      (dict_get_int, "$g_multiplayer_valid_vote_ratio", "$coop_dict", "@srvr_set14"),
      (dict_get_int, "$g_multiplayer_player_respawn_as_bot", "$coop_dict", "@srvr_set15"),
      (dict_get_int, "$coop_skip_menu", "$coop_dict", "@srvr_set16"),
      (dict_get_int, "$coop_disable_inventory", "$coop_dict", "@srvr_set17"),
      (dict_get_int, "$coop_reduce_damage", "$coop_dict", "@srvr_set18"),
      (dict_get_int, "$coop_no_capture_heroes", "$coop_dict", "@srvr_set19"),
	        (dict_get_int, "$sp_shield_bash_coop", "$coop_dict", "@srvr_set20"),
					#(dict_get_int, "$historical_banners", "$coop_dict", "@srvr_set21"),
			     # (dict_get_int, "$randomize_player_shield", "$coop_dict", "@srvr_set22"),
				  (dict_get_int, "$coop_extended_camera", "$coop_dict", "@srvr_set23"),
			      (dict_get_int, "$sp_shield_bash_ai_coop", "$coop_dict", "@srvr_set24"),
				  #####Torch use data from save game begin
				  (dict_get_int, "$torch_chance_coop", "$coop_dict", "@srvr_set25"),
				#####Torch use data from save game end
				(dict_get_int, "$tom_sand_storm_chance", "$coop_dict", "@srvr_set26"),
				(dict_get_int, "$tom_sand_storm", "$coop_dict", "@srvr_set27"),
				(dict_get_int, "$voice_set", "$coop_dict", "@srvr_set28"),
				(dict_get_int, "$experimental_archers", "$coop_dict", "@srvr_set29"),
				(dict_get_int, "$g_doghotel_enable_brainy_bots", "$coop_dict", "@srvr_set30"),

###Dict Get & Dict Set changes the options in SP after using multiplayer results
#Might need optimization
    (try_end),

     ]),	



  # script_coop_set_default_admin_settings
  ("coop_set_default_admin_settings",
   [
    #this should be set to run once at game_start
	#Edit game settings here such as default battle_size, default options (Probably set access inventory as disabled by default), and other things, max players 20 > 200.
	#This file is the module_coop_scripts.py file set settings here!
	#Settings changed by Env at 8th April.
	#Todo: Change spawnformations from default to none default (No longer enable in default) after you implement formations to multiplayer
	#skip_menu is pretty good to have it set as default but if you want to set it as off default then so be it.
	#Parameters for searching (Don't mind this): battlesize battle_size size skip menu Skip_Menu battle_size MP Formation, 20 to 200 max players.
     (try_begin),    #set this first as default, then use saved setting
      (assign, "$coop_set_add_to_servers_list", 1),
      # (assign, "$coop_set_anti_cheat", 0),
	  #COOP WSE BEGIN CUSTOM MAX PLAYERS CODE
      (assign, "$coop_set_max_num_players", 200),
	  #COOP WSE END CUSTOM MAX PLAYERS CODE BY ENVIOUS
	  #(assign, "$coop_set_max_num_players", 64),
      (assign, "$coop_battle_size", coop_def_battle_size), 
	  #Numerical Settings Template step 3 begin make sure to edit module_constants def value as well, as the other one here.
	  			(assign, "$torch_chance_coop", 3), #25% Chance = 25
     (assign, "$tom_sand_storm_chance", coop_sandstorm_chance_def), 
	 (assign, "$torch_chance_coop", coop_torch_chance_def), 
	 #Numerical Settings Template step 3 end
	  #COOP WSE CUSTOM CODE, Change settings here!
	 
      (assign, "$coop_set_melee_friendly_fire", 1),
      (assign, "$coop_set_friendly_fire", 1),
      (assign, "$coop_set_friendly_fire_damage_self_ratio", 0),
      (assign, "$coop_set_friendly_fire_damage_friend_ratio", 3),
      (assign, "$coop_set_ghost_mode", 0),
      (assign, "$coop_set_control_block_dir", 1),
      (assign, "$coop_set_combat_speed", 2), #Default = 0 AKA Slowest
      (assign, "$coop_battle_spawn_formation", 0),
      (assign, "$coop_skip_menu", 1),
      (assign, "$coop_disable_inventory", 1),
      (assign, "$coop_reduce_damage", 0),
	  #Terrain generation, setting default value.
		   # (assign, "$setting_use_dmod", 1), #Commented out in V1.001
			#(call_script, "script_init_item_score"), #No Clue what this is either #Commented out in V1.001
			#(item_set_slot, 20, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(item_set_slot, 11, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(item_set_slot, 19, 1506, 1), #Not sure what this is #Commented out in V1.001
			#(set_fixed_point_multiplier, 100), #Not sure what this is for #Commented out in V1.001
			#(set_shader_param_float, "@vFresnelMultiplier", 15),
			#(faction_set_slot, "fac_player_supporters_faction", slot_faction_state, 2),
			#(assign, "$g_player_luck", 200), #Not sure what this is #Commented out in V1.001
			#(troop_set_slot, "trp_player", slot_troop_occupation, 2),
			#(store_random_in_range, ":random_in_range_training_ground_bridge_1", "p_training_ground", "p_bridge_1"),
			#(party_relocate_near_party, "p_main_party", ":random_in_range_training_ground_bridge_1", 3),
			#(str_store_troop_name, 5, "trp_player"),
			#(party_set_name, "p_main_party", 5),
			#(call_script, "script_update_party_creation_random_limits"),
			#Global variables added below
			#Begin add AI Crouching
			#(assign, "$key_crouch", key_caps_lock),
			(assign, "$key_crouch", key_z),
            (assign,"$key_crouch_command", key_comma),
            (assign,"$key_stand_command", key_period),
			(assign,"$g_crouch_speed_limiter", 1),
			#END AI Crouching, files affected: Module_Constants, Module_Scripts (Here and below), module_mission_templates, module_animations, and animacoins.brf last mesh, also probably ani_sneak was removed
			#from load_mod_resource, and instead load_resource ani_crouch and ani_low_walk were probably added.
			#Disable/Enable variables below
			# Not needed (assign, "$battle_time", 1), # look for (eq, "$battle_time", 1), # only shows this if the global is 1 in module_game_menus.
			(assign, "$ai_crouch_mode", 0), #Value 0 to 2, 0 = Crouch & Low Walk, 1 = Crouch only, 2 = No crouching & no low walk
			#(assign, "$coop_desertv3", 0), #Example on how to generate terrain must make it (1) when its scene is set below.
			#1 = Enabled, 0 = disabled (at start if mod option exist in module_presentations)
			#(assign, "$g_player_party_icon", -1), #Not sure if needed #Commented out in V1.001
			#(assign, "$crusade_time", 0), #SP Only
			#(assign, "$g_travel_speed", 75),
			#(assign, "$g_last_payday", 0),
			#(assign, "$g_player_crusading", 0),
			(assign, "$sp_shield_bash_coop", 0),
			(assign, "$sp_shield_bash_ai_coop", 0),
			(assign, "$experimental_archers", 0),
			 (assign, "$g_doghotel_enable_brainy_bots", -1),
			#(assign, "$setting_use_spearwall", 1),

			#(assign, "$g_battle_preparation", -1), # Not sure  #Commented out in V1.001
			#(assign, "$g_battle_preparation_phase", 0), # Not sure #Commented out in V1.001
			(assign, "$g_rand_rain_limit", 30), #Commented out in V1.001
			#(assign, "$belfry_sound", 0),
			#(assign, "$g_reinforcement_waves", 2), #Keep it and see how it goes #Commented out in V1.001
			#Numerical Settings Template Extension
			#(assign, "$tom_sand_storm_chance", 20), # Default 20, 100 for testing only.

			#Numerical Settings Template Extension
			#Must add weapon break, sandstorms, scene effects to Multiplayer as well.
		#	(assign, "$g_faction_names", 0), #SP Only
		#	(assign, "$g_unit_names", 0), #SP Only
			(assign, "$tom_use_banners", 1),
			(assign, "$tom_bonus_banners", 1),
			(assign, "$tom_use_battlefields", 1),
			#(assign, "$tom_weapon_break", 1),
			#(assign, "$tom_lance_breaking", 1),
			(assign, "$coop_generate_reduction", 1),
		#	(assign, "$tom_difficulty_wages", 1),
		#	(assign, "$tom_difficulty_fief", 1),
		#	(assign, "$tom_difficulty_enterprise", 1),
		#	(assign, "$feudal_inefficency", 0),
		#	(assign, "$start_player_crusade", 0),
			#(assign, "$crusader_faction", -5), #Commented out in V1.001
		#	(assign, "$crusade_start", 0),
		#	(assign, "$crusade_target", 0),
		#	(assign, "$crusade_target_faction", 0),
			#(assign, "$crusader_party_id", -1), #Commented out in V1.001
			#(assign, "$crusader_state", -1), #Commented out in V1.001
			#(assign, "$freelancer_state", 0), #Commented out in V1.001
			#(assign, "$men_are_pleased", 0), #Commented out in V1.001
		#	(assign, "$tom_use_longships", 1), #
		#	(assign, "$use_feudal_lance", 1), #Commented out in V1.001
		#	(assign, "$use_player_auxiliary", 1), #Not needed for MP
		#	(assign, "$retinue_noble_balt", 0),
		#	(assign, "$retinue_noble_west", 0),
		#	(assign, "$retinue_noble_orthodox", 0),
		#	(assign, "$retinue_noble_muslim", 0),
		#	(assign, "$retinue_noble_mongol", 0),
		#	(assign, "$lance_troop_serving", 0),
		#	(assign, "$lance_troop_reserve", 0),
		#	(assign, "$crusader_order_joined", 0),
		#	(assign, "$culture_pool", 0),
		#	(assign, "$culture_pool_initialized", 0),
			(assign, "$historical_banners", 1),
			(assign, "$randomize_player_shield", 1),
		#	(assign, "$disable_sisterly_advice", 1),
		#	(assign, "$disable_local_histories", 1),
		#	(assign, "$player_crowned", 0),
		#	(assign, "$default_battle_size", 0),
		#	(assign, "$default_orignal_battle_size", 0),
	    #(assign, "$coop_generate_swamp", 0),
		#(assign, "$coop_extended_camera", 0),
		#(assign, "$coop_generate_desert", 0), # STEP 4
		#(assign, "$coop_generate_desertv2", 0),
		#(assign, "$coop_generate_desertv3", 0),
		#(assign, "$coop_generate_iberian", 0),
		#(assign, "$coop_generate_iberian2", 0),
		#(assign, "$coop_generate_snow", 0),
		#(assign, "$coop_generate_euro_hillside", 0),
		#End terrain generation
      (assign, "$coop_no_capture_heroes", 1),
      (assign, "$g_multiplayer_kick_voteable", 1),
      (assign, "$g_multiplayer_ban_voteable", 0),
      (assign, "$g_multiplayer_valid_vote_ratio", 63),#more than 50 percent
      (assign, "$g_multiplayer_player_respawn_as_bot", 1),
    (try_end),
     ]),	
#COOP WSE CUSTOM CODE, END CHANGE SETTINGS HERE, BY ENVIOUS.


  # script_coop_get_battle_state
  ("coop_get_battle_state",
   [
    (store_script_param, ":option", 1),
    (try_begin),
      (neg|is_vanilla_warband), #Using WSE (neg means player must be using WSE, if the operation is only is_vanilla_warband that means only run tihs operation if the player is in vanilla mode.)
      (dict_create, ":dict"),
      (dict_load_file, ":dict", "@coop_battle", 2),
      (try_begin), 
        (eq, ":option", 1),
        (dict_get_int, "$coop_battle_state", ":dict", "@battle_state"), # 0 = no battle 1 = is setup 2 = is done
      (else_try),
        (eq, ":option", 2),
        # (dict_set_int, ":dict", "@battle_state",coop_battle_state_none),
        # (dict_save, ":dict", "@coop_battle"),
        (dict_delete_file, "@coop_battle"),
      (else_try),
        (eq, ":option", 3),
        (dict_set_int, ":dict", "@battle_state",coop_battle_state_started),
        (dict_save, ":dict", "@coop_battle"),

      (try_end),
      (dict_free, ":dict"),
    #(else_try),
      #(display_message, "@Error: WSE is not running."),
	  #Uncomment top two lines to re-enable the WSE error message "WSE ERROR: WSE is not running." when not using WSE, this isn't necessary to uncomment but might be a good idea to after we implement Battle_Time to
	  #Game Mod Options.
    (try_end),
     ]),	



  # script_coop_init_mission_variables
  # This is called EVERY ROUND on ti_before_mission_start
  ("coop_init_mission_variables",
   [
    (assign, "$coop_string_received", 0), #init this global before we get names
    (assign, "$coop_class_string_received", 0), #init this global before we get class names

    (get_max_players, ":num_players"),
    (try_for_range, ":all_player_no", 0, ":num_players"),
      (player_is_active, ":all_player_no"),
      (player_set_slot, ":all_player_no", slot_player_coop_selected_troop, 0), #clear these slots every round
    (try_end),
    (try_begin),
      (neg|multiplayer_is_server),
      # (try_for_range, ":slot", 100, 200),
        # (troop_set_slot, "trp_temp_array_a", ":slot", -1),
        # (troop_set_slot, "trp_temp_array_b", ":slot", -1),
      # (try_end),

        (party_clear, coop_temp_party_enemy_heroes),
        (party_clear, coop_temp_party_ally_heroes),

      (try_for_range, ":slot", 0, 250),
        (troop_set_slot, "trp_temp_troop", ":slot", -1),
      (try_end),
    (try_end),

     ]),	


	#script_coop_get_scene_name
  # INPUT: arg1 = option_index, arg2 = option_value
  ("coop_get_scene_name",
    [
     (store_script_param, ":scene_no", 1),

      (str_store_string, s0, "@Unknown"),
      (try_begin),
        (gt, "$coop_map_party", 0), #if we know the party use it first
        (str_store_party_name, s0,  "$coop_map_party"),
      (else_try),
        (assign, ":scene_party", 0),
        (try_begin),
          (assign, ":end", castles_end),
          (try_for_range, ":castle_no", castles_begin, ":end"),
            (store_sub, ":offset", ":castle_no", castles_begin),
            (val_mul, ":offset", 3),
            (store_add, ":exterior_scene_no", "scn_castle_1_exterior", ":offset"),
            (store_add, ":interior_scene_no", "scn_castle_1_interior", ":offset"),
            (this_or_next|eq, ":scene_no", ":exterior_scene_no"),
            (eq, ":scene_no", ":interior_scene_no"),
            (assign, ":scene_party", ":castle_no"),
            (assign, ":end", 0),
          (try_end),

          (gt, ":end", 0),
          (assign, ":end", towns_end),
          (try_for_range, ":town_no", towns_begin, ":end"),
            (store_sub, ":offset", ":town_no", towns_begin),
            #EnvFix Remove if constant issue (store_add, ":town_center", "scn_town_1_center", ":offset"),
			(store_add, ":town_center", "scn_town_arab_center", ":offset"),
            #Envfix Remove if constant issue (store_add, ":town_castle", "scn_town_1_castle", ":offset"),
			(store_add, ":town_castle", "scn_town_arab_castle", ":offset"),
            #ENvfix Remove if constant issue (store_add, ":town_walls", "scn_town_1_walls", ":offset"),
			(store_add, ":town_walls", "scn_town_arab_walls", ":offset"),
            #Envfix remove if constant issue (store_add, ":town_arena", "scn_town_1_arena", ":offset"),
			(store_add, ":town_arena", "scn_town_arab_arena", ":offset"),

            (this_or_next|eq, ":scene_no", ":town_arena"),
            (this_or_next|eq, ":scene_no", ":town_walls"),
            (this_or_next|eq, ":scene_no", ":town_castle"),
            (eq, ":scene_no", ":town_center"),
            (assign, ":scene_party", ":town_no"),
            (assign, ":end", 0),
          (try_end),
            
          (gt, ":end", 0),
          (assign, ":end", villages_end),
          (try_for_range, ":party_2", villages_begin, ":end"),
            (store_sub, ":offset", ":party_2", villages_begin),
            #ENVFIX (store_add, ":village_scene_no", "scn_village_1", ":offset"),
			(store_add, ":village_scene_no", "trp_village_1_elder", ":offset"),
            (eq, ":village_scene_no", ":scene_no"),
            (assign, ":scene_party", ":party_2"),
            (assign, ":end", 0),
          (try_end),
        (try_end),

        (try_begin),
          (eq, ":end", 0), #if center was found
          (str_store_party_name, s0,  ":scene_party"),
        (else_try),
          (try_begin),
            (eq, ":scene_no", "scn_lair_steppe_bandits"),
            (str_store_string, s0, "@Steppe Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_taiga_bandits"),
            (str_store_string, s0, "@Tundra Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_desert_bandits"),
            (str_store_string, s0, "@Desert Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_forest_bandits"),
            (str_store_string, s0, "@Forest Bandit Camp"),
          (else_try),
            (eq, ":scene_no", "scn_lair_mountain_bandits"),
            (str_store_string, s0, "@Mountain Bandit Hideout"),
          (else_try),
            (eq, ":scene_no", "scn_lair_sea_raiders"),
            (str_store_string, s0, "@Sea Raider Landing"),
          (try_end),
        (try_end),

      (try_end),  

   ]),	


######## 
 #set_trigger_result tells game to add one to option_index and call script again
	#script_coop_server_send_data_before_join
  # INPUT: arg1 = option_index
  ("coop_server_send_data_before_join",
    [
     (store_script_param, ":option_index", 1),
    
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg0, "$coop_team_1_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg0, "$coop_team_2_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg0, "$coop_team_1_troop_num"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg0, "$coop_team_2_troop_num"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 4),
       (server_get_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 5),
       (server_get_melee_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 6),
       (server_get_friendly_fire_damage_self_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 7),
       (server_get_friendly_fire_damage_friend_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 8),
       (server_get_ghost_mode, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 9),
       (server_get_control_block_dir, reg0),       
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 10),
       (server_get_combat_speed, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 11),
       (assign, reg0, "$g_multiplayer_player_respawn_as_bot"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 12),
       (assign, reg0, "$coop_time_of_day"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 13),
       (assign, reg0, "$coop_rain"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 14),
       (assign, reg0, "$coop_cloud"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 15),
       (assign, reg0, "$coop_haze"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 16),
       (assign, reg0, "$coop_castle_banner"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 17),
       (assign, reg0, "$key_crouch"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 18),
       (assign, reg0, "$key_crouch_command"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 19),
       (assign, reg0, "$key_stand_command"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 20),
       (assign, reg0, "$g_crouch_speed_limiter"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 21),
       (assign, reg0, "$ai_crouch_mode"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 22),
       (assign, reg0, "$sp_shield_bash_coop"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 23),
       (assign, reg0, "$sp_shield_bash_ai_coop"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 24),
       (assign, reg0, "$tom_use_banners"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 25),
       (assign, reg0, "$tom_bonus_banners"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 26),
       (assign, reg0, "$tom_use_battlefields"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 27),
       (assign, reg0, "$historical_banners"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 28),
       (assign, reg0, "$randomize_player_shield"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 29),
       (assign, reg0, "$tom_sand_storm_chance"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 30),
       (assign, reg0, "$tom_sand_storm"),
       (set_trigger_result, 1),
	        (else_try),
       (eq, ":option_index", 31),
       (assign, reg0, "$coop_extended_camera"),
       (set_trigger_result, 1),
	   	        (else_try),
       (eq, ":option_index", 32),
       (assign, reg0, "$g_rand_rain_limit"),
       (set_trigger_result, 1),
	   	   	        (else_try),
       (eq, ":option_index", 33),
       (assign, reg0, "$voice_set"),
       (set_trigger_result, 1),
	   #	   	   	        (else_try),
       #(eq, ":option_index", 33),
       #(assign, reg0, "$belfry_positioned"),
       #(set_trigger_result, 1),
	   #	   	        (else_try),
       #(eq, ":option_index", 34),
       #(assign, reg0, "$belfry_sound"),
       #(set_trigger_result, 1),
	   #	   	   	        (else_try),
       #(eq, ":option_index", 35),
       #(assign, reg0, "$coop_use_belfry"),
       #(set_trigger_result, 1),
	  # 	   	   	        (else_try),
      # (eq, ":option_index", 34),
      # (assign, reg0, "$tom_lance_breaking"),
      # (set_trigger_result, 1),
     (try_end),     
       # (assign, reg1, ":option_index"),
       # (display_message, "@server send {reg1} {reg0}"),

   ]),	

	#script_coop_client_receive_data_before_join
  # INPUT: arg1 = option_index, arg2 = option_value
  ("coop_client_receive_data_before_join",
    [
     (store_script_param, ":option_index", 1),
     (store_script_param, ":option_value", 2),

       # (assign, reg1, ":option_index"),
       # (assign, reg2, ":option_value"),
       # (display_message, "@client get {reg1} {reg2}"),
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg1, 1),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg1, 2),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg1, 1),
       (str_store_string, s0, "@Number of troops on team {reg1}:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg1, 2),
       (str_store_string, s0, "@Number of troops on team {reg1}:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 4),
       (str_store_string, s0, "str_allow_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 5),
       (str_store_string, s0, "str_allow_melee_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 6),
       (str_store_string, s0, "str_friendly_fire_damage_self_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 7),
       (str_store_string, s0, "str_friendly_fire_damage_friend_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 8),
       (str_store_string, s0, "str_spectator_camera"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_free"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_stick_to_any_player"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_stick_to_team_members"),
       (else_try),
         (str_store_string, s1, "str_stick_to_team_members_view"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 9),
       (str_store_string, s0, "str_control_block_direction"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_automatic"),
       (else_try),
         (str_store_string, s1, "str_by_mouse_movement"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 10),
       (str_store_string, s0, "str_combat_speed"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_combat_speed_0"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_combat_speed_1"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_combat_speed_2"),
       (else_try),
         (eq, ":option_value", 3),
         (str_store_string, s1, "str_combat_speed_3"),
       (else_try),
         (str_store_string, s1, "str_combat_speed_4"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 11),
       (str_store_string, s0, "str_players_take_control_of_a_bot_after_death"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 12),
       (assign, "$coop_time_of_day", ":option_value"),
       (str_store_string, s0, "@Time of day:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 13),
       (assign, "$coop_rain", ":option_value"),
     (else_try),
       (eq, ":option_index", 14),
       (assign, "$coop_cloud", ":option_value"),
     (else_try),
       (eq, ":option_index", 15),
       (assign, "$coop_haze", ":option_value"),
     (else_try),
       (eq, ":option_index", 16),
       (assign, "$coop_castle_banner", ":option_value"),
       (display_message, "@Recieved Scene Data."),
	        (else_try),
       (eq, ":option_index", 17),
       (assign, "$key_crouch", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 18),
       (assign, "$key_crouch_command", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 19),
       (assign, "$key_stand_command", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 20),
       (assign, "$g_crouch_speed_limiter", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 21),
       (assign, "$ai_crouch_mode", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 22),
       (assign, "$sp_shield_bash_coop", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 23),
       (assign, "$sp_shield_bash_ai_coop", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 24),
       (assign, "$tom_use_banners", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 25),
       (assign, "$tom_bonus_banners", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 26),
       (assign, "$tom_use_battlefields", ":option_value"),
       (eq, ":option_index", 27),
       (assign, "$historical_banners", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 28),
       (assign, "$randomize_player_shield", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 29),
       (assign, "$tom_sand_storm_chance", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 30),
       (assign, "$tom_sand_storm", ":option_value"),
	   	        (else_try),
       (eq, ":option_index", 31),
       (assign, "$coop_extended_camera", ":option_value"),
	   	   	        (else_try),
       (eq, ":option_index", 32),
       (assign, "$g_rand_rain_limit", ":option_value"),
	   	   	   	        (else_try),
       (eq, ":option_index", 33),
       (assign, "$voice_set", ":option_value"),
	  # 	   	   	   	        (else_try),
      # (eq, ":option_index", 33),
      # (assign, "$belfry_positioned", ":option_value"),
	  #	   	   	        (else_try),
      #(eq, ":option_index", 34),
      #(assign, "$belfry_sound", ":option_value"),
	  #	  	   	   	        (else_try),
      #(eq, ":option_index", 35),
      #(assign, "$coop_use_belfry", ":option_value"),
	   #	   	   	        (else_try),
       #(eq, ":option_index", 33),
       #(assign, "$tom_weapon_break", ":option_value"),
	   #	   	   	        (else_try),
       #(eq, ":option_index", 34),
       #(assign, "$tom_lance_breaking", ":option_value"),
     (try_end),  

   ]),	


######## 
	 # script_coop_server_player_joined_common
  # Input: arg1 
  # Output: none
  ("coop_server_player_joined_common",
   [
    (store_script_param, ":player_no", 1),

    (try_begin),
      (gt, ":player_no", 0), #dont send stats to server
#	  #Works but could be better
#DEBUG FOR Co-Op display messages Begin
#(display_message, "@TESTING Multiplayer int_2 event coop_scripts A1 - only connecting player should see this."),
		#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_dmod, "$setting_use_dmod"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch, "$key_crouch"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch_command, "$key_crouch_command"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_stand_command, "$key_stand_command"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_crouch_speed_limiter, "$g_crouch_speed_limiter"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_ai_crouch_mode, "$ai_crouch_mode"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_player_party_icon, "$g_player_party_icon"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash, "$sp_shield_bash_coop"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash_ai, "$sp_shield_bash_ai_coop"), #Step 4
					#	(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_spearwall, "$setting_use_spearwall"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation, "$g_battle_preparation"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation_phase, "$g_battle_preparation_phase"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_rand_rain_limit, "$g_rand_rain_limit"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_position, "$belfry_positioned"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_sound, "$belfry_sound"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_use_belfry, "$coop_use_belfry"), #Step 4

			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_reinforcement_waves, "$g_reinforcement_waves"),



			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_banners, "$tom_use_banners"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_bonus_banners, "$tom_bonus_banners"), #Step 4
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_battlefields, "$tom_use_battlefields"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_weapon_break, "$tom_weapon_break"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_lance_breaking, "$tom_lance_breaking"),
			###((multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_coop_generate_reduction, "$coop_generate_reduction"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_faction, "$crusader_faction"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_party_id, "$crusader_party_id"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_state, "$crusader_state"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_freelancer_state, "$freelancer_state"), #Step 4
			
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_men_are_pleased, "$men_are_pleased"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_longships, "$tom_use_longships"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_use_feudal_lance, "$use_feudal_lance"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_historical_banners, "$historical_banners"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_randomize_player_shield, "$randomize_player_shield"),
						#Numerical Settings Template Step 5 Begin (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_sand_storm_chance, "$tom_sand_storm_chance"),
						###((multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_torch_chance, "$torch_chance_coop"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_camera_mode, "$coop_extended_camera"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_voiceset, "$voice_set"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_sand_storm, "$tom_sand_storm"),
						#Numerical Settings Template Step 5 End (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
			#End Extension
			#If adding additional features all you need is to add send to player above and event_subtype, as well as make a new constant in module_constants similiar to coop_set_ right here.
			#If you wish to extend to the menu, you'll have to do more, just read module_coop_presentations.
			
			
      (str_store_faction_name, s0, "fac_player_supporters_faction"),
      (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

      #send names of main party troop classes
      (try_for_range, ":class", 0, 9),
        (str_store_class_name, s0, ":class"), 
        (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
      (try_end),

      (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
      (get_max_players, ":num_players"),
      (try_for_range, ":all_player_no", 0, ":num_players"),
        (player_is_active, ":all_player_no"),
        (player_get_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
        (gt, ":other_player_selected_troop", 0),
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
      (try_end),

      #send list of heroes in battle (since client cannot upgrade character, only send fighting skills)
      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_enemy_heroes),
      (try_for_range, ":stack", 0, ":num_heroes"),
        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_enemy_heroes, ":stack"),	
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_enemy_heroes),
#NEW
        (try_begin),
          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
          (str_store_troop_name, s0, ":hero_troop"),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

          #(troop_get_face_keys, reg1, ":hero_troop"),
          #(str_store_face_keys, s0, reg1),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
        (try_end),

        #(try_for_range, ":attribute", ca_strength, ca_intelligence),#0,1 #Def
		(try_for_range, ":attribute", 0, 2),#0,1
          (store_attribute_level,":value",":hero_troop",":attribute"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
        (try_end),
        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
          (gt,":value",0),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
        (try_end),
        #(try_for_range, ":wprof", wpt_one_handed_weapon, 7),#DEF
		(try_for_range, ":wprof", 0, 7),
          (store_proficiency_level,":value",":hero_troop",":wprof"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
        (try_end),
      (try_end),

      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_ally_heroes),
      (try_for_range, ":stack", 0, ":num_heroes"),
        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_ally_heroes, ":stack"),	
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_ally_heroes),
#NEW


        (try_begin),
          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
          (str_store_troop_name, s0, ":hero_troop"),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

          #(troop_get_face_keys, reg1, ":hero_troop"),
          #(str_store_face_keys, s0, reg1),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
        (try_end),

        #(try_for_range, ":attribute", ca_strength, ca_intelligence),#0,1 #Def
		(try_for_range, ":attribute", 0, 2),#0,1
          (store_attribute_level,":value",":hero_troop",":attribute"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
        (try_end),
        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
          (gt,":value",0),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
        (try_end),
        #(try_for_range, ":wprof", wpt_one_handed_weapon, 7), #Def
		(try_for_range, ":wprof", 0, 7),
          (store_proficiency_level,":value",":hero_troop",":wprof"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
        (try_end),
      (try_end),

    (try_end),
    #do send this to server
#Maybe send more data in here when player joins??

    (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_round, "$coop_round", "$coop_battle_started"), #start welcome message after getting team data
#	 #(display_message, "str_revision"),
#	 (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, "str_revision"), #New
#			#Begin terrain generation
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_swamp, "$coop_generate_swamp"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desert, "$coop_generate_desert"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desertv2, "$coop_generate_desertv2"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desertv3, "$coop_generate_desertv3"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_iberian, "$coop_generate_iberian"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_iberian2, "$coop_generate_iberian2"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_snow, "$coop_generate_snow"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_euro_hillside, "$coop_generate_euro_hillside"), #Step 4
#			#End terrain generation
#			
#			#Extend to all Co-Op Cmds for MP
#			
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_dmod, "$setting_use_dmod"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch, "$key_crouch"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch_command, "$key_crouch_command"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_stand_command, "$key_stand_command"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_crouch_speed_limiter, "$g_crouch_speed_limiter"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_ai_crouch_mode, "$ai_crouch_mode"),
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_player_party_icon, "$g_player_party_icon"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash, "$sp_shield_bash_coop"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash_ai, "$sp_shield_bash_ai_coop"), #Step 4
#					#	(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_spearwall, "$setting_use_spearwall"),
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation, "$g_battle_preparation"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation_phase, "$g_battle_preparation_phase"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_rand_rain_limit, "$g_rand_rain_limit"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_reinforcement_waves, "$g_reinforcement_waves"),
#
#
#
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_banners, "$tom_use_banners"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_bonus_banners, "$tom_bonus_banners"), #Step 4
#						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_battlefields, "$tom_use_battlefields"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_weapon_break, "$tom_weapon_break"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_lance_breaking, "$tom_lance_breaking"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_coop_generate_reduction, "$coop_generate_reduction"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_faction, "$crusader_faction"),
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_party_id, "$crusader_party_id"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_state, "$crusader_state"),
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_freelancer_state, "$freelancer_state"), #Step 4
#			
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_men_are_pleased, "$men_are_pleased"),
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_longships, "$tom_use_longships"), #Step 4
#			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_use_feudal_lance, "$use_feudal_lance"),
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_historical_banners, "$historical_banners"), #Step 4
#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_randomize_player_shield, "$randomize_player_shield"),
#						#Numerical Settings Template Step 5 Begin (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
#						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_sand_storm_chance, "$tom_sand_storm_chance"),
#						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_torch_chance, "$torch_chance_coop"),
#						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_camera_mode, "$coop_extended_camera"),
#						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_sand_storm, "$tom_sand_storm"),
#						#Numerical Settings Template Step 5 End (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
#			#End Extension
#			#If adding additional features all you need is to add send to player above and event_subtype, as well as make a new constant in module_constants similiar to coop_set_ right here.
#			#If you wish to extend to the menu, you'll have to do more, just read module_coop_presentations.
	 
   ]),	


#  # script_coop_server_player_joined_common
#  # Input: arg1 
#  # Output: none
#  ("coop_server_player_joined_common",
#   [
#    (store_script_param, ":player_no", 1),
#
#    (try_begin),
#      (gt, ":player_no", 0), #dont send stats to server
#
#      (str_store_faction_name, s0, "fac_player_supporters_faction"),
#      (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#
#      #send names of main party troop classes
#      (try_for_range, ":class", 0, 9),
#        (str_store_class_name, s0, ":class"), 
#        (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#      (try_end),
#
#      (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
#      (get_max_players, ":num_players"),
#      (try_for_range, ":all_player_no", 0, ":num_players"),
#        (player_is_active, ":all_player_no"),
#        (player_get_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
#        (gt, ":other_player_selected_troop", 0),
#        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
#      (try_end),
#
#      #send list of heroes in battle (since client cannot upgrade character, only send fighting skills)
#      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_enemy_heroes),
#      (try_for_range, ":stack", 0, ":num_heroes"),
#        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_enemy_heroes, ":stack"),	
#        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_enemy_heroes),
##NEW
#        (try_begin),
#          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
#          (str_store_troop_name, s0, ":hero_troop"),
#          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#
#          #(troop_get_face_keys, reg1, ":hero_troop"),
#          #(str_store_face_keys, s0, reg1),
#          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#        (try_end),
#
#        (try_for_range, ":attribute", ca_strength, ca_intelligence),#0,1
#          (store_attribute_level,":value",":hero_troop",":attribute"),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
#        (try_end),
#        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
#          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
#          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
#          (gt,":value",0),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
#        (try_end),
#        (try_for_range, ":wprof", wpt_one_handed_weapon, 7),
#          (store_proficiency_level,":value",":hero_troop",":wprof"),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
#        (try_end),
#      (try_end),
#
#      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_ally_heroes),
#      (try_for_range, ":stack", 0, ":num_heroes"),
#        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_ally_heroes, ":stack"),	
#        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_ally_heroes),
##NEW
#        (try_begin),
#          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
#          (str_store_troop_name, s0, ":hero_troop"),
#          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#
#          #(troop_get_face_keys, reg1, ":hero_troop"),
#          #(str_store_face_keys, s0, reg1),
#          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
#        (try_end),
#
#        (try_for_range, ":attribute", ca_strength, ca_intelligence),#0,1
#          (store_attribute_level,":value",":hero_troop",":attribute"),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
#        (try_end),
#        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
#          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
#          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
#          (gt,":value",0),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
#        (try_end),
#        (try_for_range, ":wprof", wpt_one_handed_weapon, 7),
#          (store_proficiency_level,":value",":hero_troop",":wprof"),
#          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
#        (try_end),
#      (try_end),
#
#    (try_end),
#    #do send this to server
##Maybe send more data in here when player joins??
#    (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_round, "$coop_round", "$coop_battle_started"), #start welcome message after getting team data
#   ]),	
#   
#   
#####BUGGY BEGIN
######## 
#	
#  # script_coop_server_player_joined_common
#  # Input: arg1 
#  # Output: none
#  ("coop_server_player_joined_common",
#   [
#    (store_script_param, ":script_param_1", 1),
#
#    (try_begin),
#      (gt, ":script_param_1", 0), #dont send stats to server
#
#      (str_store_faction_name, s0, "fac_player_supporters_faction"),
#      (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#
#      #send names of main party troop classes
#      (try_for_range, ":class", 0, 9),
#        (str_store_class_name, s0, ":class"), 
#        (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#      (try_end),
#
#      (multiplayer_send_2_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
#      (get_max_players, ":max_players"),
#      (try_for_range, ":all_player_no", 0, ":max_players"),
#        (player_is_active, ":all_player_no"),
#        (player_get_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
#        (gt, ":other_player_selected_troop", 0),
#        (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":other_player_selected_troop", ":all_player_no", slot_player_coop_selected_troop),
#      (try_end),
#
#      #send list of heroes in battle (since client cannot upgrade character, only send fighting skills)
#      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_enemy_heroes),
#      (try_for_range, ":localvariable", 0, ":num_heroes"),
#        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_enemy_heroes, ":localvariable"),	
#        (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_enemy_heroes),
##NEW
#        (try_begin),
#          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
#          (str_store_troop_name, s0, ":hero_troop"),
#          (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#
#          #(troop_get_face_keys, reg1, ":hero_troop"),
#          #(str_store_face_keys, s0, reg1),
#          (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#        (try_end),
#
#        (try_for_range, ":attribute", 0, 2),#0,1
#          (store_attribute_level,":value",":hero_troop",":attribute"),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
#        (try_end),
#        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
#          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
#          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
#          (gt,":value",0),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
#        (try_end),
#        (try_for_range, ":wprof", 0, 7),
#          (store_proficiency_level,":value",":hero_troop",":wprof"),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
#        (try_end),
#      (try_end),
#
#      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_ally_heroes),
#      (try_for_range, ":localvariable", 0, ":num_heroes"),
#        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_ally_heroes, ":localvariable"),	
#        (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_ally_heroes),
##NEW
#        (try_begin),
#          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
#          (str_store_troop_name, s0, ":hero_troop"),
#          (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#
#          #(troop_get_face_keys, reg1, ":hero_troop"),
#          #(str_store_face_keys, s0, reg1),
#          (multiplayer_send_string_to_player, ":script_param_1", multiplayer_event_coop_send_to_player_string, s0),
#        (try_end),
#
#        (try_for_range, ":attribute", 0, 2),#0,1
#          (store_attribute_level,":value",":hero_troop",":attribute"),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribute"),
#        (try_end),
#        (try_for_range, ":skill_level_leadership_var_1", skl_horse_archery, skl_reserved_14),
#          (neg|is_between, ":skill_level_leadership_var_1", "skl_reserved_9", "skl_power_draw"), #skip these skills
#          (store_skill_level,":value",":skill_level_leadership_var_1",":hero_troop"),
#          (gt,":value",0),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill_level_leadership_var_1"),
#        (try_end),
#        (try_for_range, ":wprof", 0, 7),
#          (store_proficiency_level,":value",":hero_troop",":wprof"),
#          (multiplayer_send_4_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
#        (try_end),
#      (try_end),
#
#    (try_end),
#    #do send this to server
#	#Maybe send more data in here when player joins??
#    (multiplayer_send_3_int_to_player, ":script_param_1", multiplayer_event_coop_send_to_player, coop_event_round, "$coop_round", "$coop_battle_started"), #start welcome message after getting team data
#   ]),	

#####BUGGY END

######## 
	#script_coop_receive_network_message
  # This script is called from the game engine when a new network message is received.
  # INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
  ("coop_receive_network_message",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":event_type", 2),
    #ENVFIX (store_script_param, ":player_no", 1),
	#ENVFIX (store_script_param, ":event_type", 2),
    (try_begin),
      #(multiplayer_is_server),
      (try_begin),
        #SERVER EVENTS#
        (eq, ":event_type", multiplayer_event_change_troop_id), #receive player chosen troop
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":troop", 3),
        (try_begin),
          (gt, ":troop", 0),
          (player_get_agent_id, ":player_agent", ":player_no"),
          (this_or_next|eq, ":player_agent", -1),#if spectator
          (neg|agent_is_alive, ":player_agent"), #if dead

          #only continue if hero is not dead yet
          (player_get_team_no, ":player_team", ":player_no"),
          (assign, ":num", 0),
          (try_begin),
            (eq, ":player_team", 0),
            (party_count_members_of_type, ":num", coop_temp_party_enemy_heroes, ":troop"),
          (else_try),
            (eq, ":player_team", 1),
            (party_count_members_of_type, ":num", coop_temp_party_ally_heroes, ":troop"),
          (try_end),
          (eq, ":num", 1),

          (try_begin),
            (eq, "$coop_battle_started", 1),
            (assign, ":end_cond", 0),
            (try_for_agents, ":cur_agent"),
              (eq, ":end_cond", 0),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_non_player, ":cur_agent"),
              (agent_get_troop_id,":script_param_1", ":cur_agent"),
              (eq, ":troop", ":script_param_1"),
              #(troop_is_hero, ":script_param_1"),
              (player_set_troop_id, ":player_no", ":script_param_1"),#NEW
              (player_control_agent, ":player_no", ":cur_agent"),

              (assign, ":end_cond", 1), #break
            (try_end),
          (else_try),
            #only tell other players before spawn, after spawn other players check agents if troop is in use
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":troop", ":player_no", slot_player_coop_selected_troop),
            (try_end),
          (try_end),
          (player_set_slot, ":player_no", slot_player_coop_selected_troop, ":troop"), #server always save to player slot

        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_team_no),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":team", 3),
        (try_begin),
          (eq, ":team", multi_team_spectator),
          (try_begin),
            (eq, "$coop_battle_started", 0), #only send to players before spawn if already picked
            (player_get_slot,  ":player_troop", ":player_no", slot_player_coop_selected_troop),
            (gt, ":player_troop", 0),
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, 0, ":player_no", slot_player_coop_selected_troop),
            (try_end),
          (try_end),
          (player_set_slot, ":player_no", slot_player_coop_selected_troop, 0),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_set_bot_selection), #also called from native script for slot_player_bot_type_1_wanted, slot_player_bot_type_4_wanted
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          (is_between, ":slot_no", slot_player_coop_class_0_wanted, slot_player_coop_class_8_wanted + 1), # coop only slots
          (is_between, ":value", 0, 2),
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_admin_panel), 
        (try_begin),
          (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
          (call_script, "script_game_quick_start"), #add this to native event when switching back to native game type
        (try_end),


      # COOP EVENTS#
      (else_try),
        (eq, ":event_type", multiplayer_event_coop_send_to_server),
        (store_script_param, ":event_subtype", 3),

        (try_begin),
          (eq, ":event_subtype", coop_event_start_map),
          (try_begin),
            (player_is_admin, ":player_no"),
            (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_1, "$coop_time_of_day"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_2, "$coop_rain"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_3, "$coop_cloud"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_4, "$coop_haze"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_5, "$coop_castle_banner"),
            (try_end),
            (call_script, "script_coop_get_battle_state", 3), #sets state to started
            (team_set_faction, 0, "$coop_team_1_faction"),
            (team_set_faction, 1, "$coop_team_2_faction"),
            (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
            (start_multiplayer_mission, reg0, "$coop_battle_scene", 1),
          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_setup_battle), #have server load saved battle
          (try_begin),
            (player_is_admin, ":player_no"),
            (call_script, "script_coop_on_admin_panel_load"),
            (eq, "$coop_battle_state", coop_battle_state_setup_mp),#only if coop battle is setup
            (call_script, "script_coop_server_send_admin_settings_to_player", ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_receive_next_string, 3),
            (str_store_server_password, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
            (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_skip_menu, "$coop_skip_menu"),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_start_battle), 
          (try_begin),
            (eq, "$coop_battle_started", 0),
            (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
            (reset_mission_timer_a),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_end_battle),
          (try_begin),
            (eq, "$coop_battle_started", 1),
            (call_script, "script_coop_copy_parties_to_file_mp"),
          (try_end),
          (try_begin),
            (neg|multiplayer_is_dedicated_server),
            (finish_mission,0), #alway end
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_open_admin_panel),
          (try_begin),
            (player_is_admin, ":player_no"),
            (call_script, "script_coop_server_send_admin_settings_to_player", ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_receive_next_string, 3),
            (str_store_server_password, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

            (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_skip_menu, "$coop_skip_menu"),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_open_game_rules),
          (call_script, "script_coop_server_send_admin_settings_to_player", ":player_no"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_open_game_rules),
        (else_try),
          (eq, ":event_subtype", coop_event_battle_size),
          (store_script_param, ":value", 4),
          (try_begin),
            (ge, ":value", coop_min_battle_size),
            (assign, "$coop_battle_size", ":value"), #store current battle size setting
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_spawn_formation),
          (store_script_param, ":value", 4),
          (assign, "$coop_battle_spawn_formation", ":value"),
		  #Begin terrain generation
	#	 (else_try),
	#	 ####Extend to all
	#	 
	#	         (eq, ":event_subtype", coop_set_setting_use_dmod),
    #    (store_script_param, ":value", 4),
    #    (assign, "$setting_use_dmod", ":value"),
		
		      (else_try),
        (eq, ":event_subtype", coop_set_key_crouch),
        (store_script_param, ":value", 4),
        (assign, "$key_crouch", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_key_crouch_command),
        (store_script_param, ":value", 4),
        (assign, "$key_crouch_command", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_key_stand_command),
        (store_script_param, ":value", 4),
        (assign, "$key_stand_command", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_g_crouch_speed_limiter),
        (store_script_param, ":value", 4),
        (assign, "$g_crouch_speed_limiter", ":value"),
				      (else_try),			  
        (eq, ":event_subtype", coop_set_ai_crouch_mode),
        (store_script_param, ":value", 4),
        (assign, "$ai_crouch_mode", ":value"),
	#			      (else_try),
	#				  
    #    (eq, ":event_subtype", coop_set_g_player_party_icon),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_player_party_icon", ":value"),
				      (else_try),			  
        (eq, ":event_subtype", coop_set_sp_shield_bash),
        (store_script_param, ":value", 4),
        (assign, "$sp_shield_bash_coop", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_sp_shield_bash_ai),
        (store_script_param, ":value", 4),
        (assign, "$sp_shield_bash_ai_coop", ":value"),
		
						      (else_try),
					  
        (eq, ":event_subtype", coop_set_archerpos),
        (store_script_param, ":value", 4),
        (assign, "$experimental_archers", ":value"),
								      (else_try),
					  
        (eq, ":event_subtype", coop_set_ai_mode),
        (store_script_param, ":value", 4),
        (assign, "$g_doghotel_enable_brainy_bots", ":value"),
	#			      (else_try),
	#				  
    #    (eq, ":event_subtype", coop_set_setting_use_spearwall),
    #    (store_script_param, ":value", 4),
    #    (assign, "$setting_use_spearwall", ":value"),
	#			      (else_try),
	#				  
    #    (eq, ":event_subtype", coop_set_g_battle_preparation),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_battle_preparation", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_set_g_battle_preparation_phase),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_battle_preparation_phase", ":value"),
				      (else_try),
        (eq, ":event_subtype", coop_set_g_rand_rain_limit),
        (store_script_param, ":value", 4),
        (assign, "$g_rand_rain_limit", ":value"),
		#						      (else_try),
        #(eq, ":event_subtype", coop_set_belfry_position),
        #(store_script_param, ":value", 4),
        #(assign, "$belfry_positioned", ":value"),
		#				      (else_try),
        #(eq, ":event_subtype", coop_set_belfry_sound),
        #(store_script_param, ":value", 4),
        #(assign, "$belfry_sound", ":value"),
		#						      (else_try),
        #(eq, ":event_subtype", coop_use_belfry),
        #(store_script_param, ":value", 4),
        #(assign, "$coop_use_belfry", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_set_g_reinforcement_waves),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_reinforcement_waves", ":value"),
						      (else_try),
#        (eq, ":event_subtype", coop_set_tom_sand_storm_chance),
#        (store_script_param, ":value", 4),
#        (assign, "$tom_sand_storm_chance", ":value"),
#						      (else_try),
        (eq, ":event_subtype", coop_set_tom_use_banners),
        (store_script_param, ":value", 4),
        (assign, "$tom_use_banners", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_tom_bonus_banners),
        (store_script_param, ":value", 4),
        (assign, "$tom_bonus_banners", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_tom_use_battlefields),
        (store_script_param, ":value", 4),
        (assign, "$tom_use_battlefields", ":value"),
		#				      (else_try),
       #(eq, ":event_subtype", coop_set_tom_weapon_break),
       #(store_script_param, ":value", 4),
       #(assign, "$tom_weapon_break", ":value"),
		#				      (else_try),
       #(eq, ":event_subtype", coop_set_tom_lance_breaking),
       #(store_script_param, ":value", 4),
       #(assign, "$tom_lance_breaking", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_coop_generate_reduction),
        (store_script_param, ":value", 4),
        (assign, "$coop_generate_reduction", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_faction),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_faction", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_party_id),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_party_id", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_state),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_state", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_freelancer_state),
    #    (store_script_param, ":value", 4),
    #    (assign, "$freelancer_state", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_men_are_pleased),
    #    (store_script_param, ":value", 4),
    #    (assign, "$men_are_pleased", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_tom_use_longships),
    #    (store_script_param, ":value", 4),
    #    (assign, "$tom_use_longships", ":value"),	
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_use_feudal_lance),
    #    (store_script_param, ":value", 4),
    #    (assign, "$use_feudal_lance", ":value"),
		      (else_try),
		 
		 
		 ####End Extension

		(eq, ":event_subtype", coop_set_historical_banners),
		(store_script_param, ":value", 4),
		(assign, "$historical_banners", ":value"),
					(else_try),
		(eq, ":event_subtype", coop_set_randomize_player_shield),
		(store_script_param, ":value", 4),
		(assign, "$randomize_player_shield", ":value"),
				  #numerical settings template step 1 begin
					(else_try),
          (eq, ":event_subtype", coop_set_tom_sand_storm_chance),
          (store_script_param, ":value", 4),
          (try_begin),
            (ge, ":value", coop_sandstorm_chance_min),
            (assign, "$tom_sand_storm_chance", ":value"), #store current battle size setting
          (try_end),
		  #numerical settings template step 1 end
		  					(else_try),		
		(eq, ":event_subtype", coop_sand_storm),
		(store_script_param, ":value", 4),
		(assign, "$tom_sand_storm", ":value"),
		(else_try),
          (eq, ":event_subtype", coop_set_torch_chance),
          (store_script_param, ":value", 4),
          (try_begin),
            (ge, ":value", coop_torch_chance_min),
            (assign, "$torch_chance_coop", ":value"), #store current battle size setting
          (try_end),
		  		(else_try),
						(eq, ":event_subtype", coop_voiceset),
          (store_script_param, ":value", 4),
          (assign, "$voice_set", ":value"),
		  		(else_try),
						(eq, ":event_subtype", coop_set_camera_mode),
          (store_script_param, ":value", 4),
          (assign, "$coop_extended_camera", ":value"),
	#	  		  		 (else_try),
	#	(eq, ":event_subtype", coop_generate_swamp),
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_swamp", ":value"),
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_desert), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_desert", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_desertv2), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_desertv2", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_desertv3), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_desertv3", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_iberian), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_iberian", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_iberian2), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_iberian2", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_snow), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_snow", ":value"), 
	#	  		  		 (else_try),
    #      (eq, ":event_subtype", coop_generate_euro_hillside), #STEP 4
    #      (store_script_param, ":value", 4),
    #      (assign, "$coop_generate_euro_hillside", ":value"), 
	#	  
	#	  #End terrain generation
        (else_try),
          (eq, ":event_subtype", coop_event_skip_admin_panel),
          (store_script_param, ":value", 4),
          (assign, "$coop_skip_menu", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_disable_inventory),
          (store_script_param, ":value", 4),
          (assign, "$coop_disable_inventory", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_reduce_damage),
          (store_script_param, ":value", 4),
          (assign, "$coop_reduce_damage", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_no_capture_heroes),
          (store_script_param, ":value", 4),
          (assign, "$coop_no_capture_heroes", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_player_open_inventory_before_spawn),
          (try_begin),
            (eq, "$coop_disable_inventory", 0),#inventory access is optional
            (player_get_slot,  ":player_troop", ":player_no", slot_player_coop_selected_troop),
            (gt, ":player_troop", 0),
            (party_count_members_of_type,":num","$coop_main_party_spawn",":player_troop"),
            (eq,":num",1),
            (try_for_range, ":slot", 0, 9),
              (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":slot"),
              (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":slot"),
              (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":slot", ":player_cur_item", ":player_cur_imod"),
            (try_end),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done
          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_player_get_selected_item_types),
          (store_script_param, ":itm_type_1", 4),
          (store_script_param, ":itm_type_2", 5),

          (player_get_slot,  ":player_troop", ":player_no", slot_player_coop_selected_troop),
          (try_begin),
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (troop_get_inventory_capacity, ":end", "trp_temp_troop"),
          (val_add,":end", 1), 
          (try_for_range, ":slot", 10, ":end"),
            (troop_get_inventory_slot, ":item", "trp_temp_troop", ":slot"), #inventory troop
            (troop_get_inventory_slot_modifier, ":imod", "trp_temp_troop", ":slot"),
            #  (troop_inventory_slot_get_item_amount, ":item_quant", ":troop_2", ":slot"),
            (gt, ":item", 0),
            (item_get_type, ":item_class", ":item"),

            (assign, ":continue_2", 0),
            (try_begin),
              (eq, ":itm_type_1", itp_type_one_handed_wpn),
              (is_between, ":item_class", itp_type_pistol, itp_type_animal), #add firearms here
              (assign, ":continue_2", 1),
            (else_try),
              (is_between, ":item_class", ":itm_type_1", ":itm_type_2"),
              (assign, ":continue_2", 1),
            (try_end),
            (eq, ":continue_2", 1),
            (call_script, "script_coop_troop_can_use_item",":player_troop", ":item", ":imod"),
            (eq, reg0, 1),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_send_inventory, ":slot", ":item", ":imod"),
          # (assign, reg1, ":slot"), 
          # (str_store_item_name, s40, ":item"),
          # (display_message, "@sending inv slot {reg1}  = {reg0} {s40} "),
          (try_end),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done

        (else_try),
          (eq, ":event_subtype", coop_event_player_ask_for_selected_item),
          (store_script_param, ":equip_slot", 4),
          (store_script_param, ":item_id", 5),
          (store_script_param, ":party_inv_slot", 6),
          (player_get_slot,  ":player_troop", ":player_no", slot_player_coop_selected_troop),
          (try_begin),
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (try_begin),
            (gt, ":item_id", 0),
            (ge, ":party_inv_slot", 10),

            (troop_get_inventory_slot, ":cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":cur_imod", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot, ":new_item", "trp_temp_troop", ":party_inv_slot"),
            (troop_get_inventory_slot_modifier, ":new_imod", "trp_temp_troop", ":party_inv_slot"),

            (try_begin),
              (eq, ":item_id", ":new_item"),
              (call_script, "script_coop_troop_can_use_item",":player_troop", ":new_item", ":new_imod"),
              (eq, reg0, 1),
              (troop_set_inventory_slot, ":player_troop", ":equip_slot", ":new_item"),
              (troop_set_inventory_slot_modifier, ":player_troop", ":equip_slot", ":new_imod"),
              (troop_set_inventory_slot, "trp_temp_troop", ":party_inv_slot", ":cur_item"),
              (troop_set_inventory_slot_modifier, "trp_temp_troop", ":party_inv_slot", ":cur_imod"),
#FIX
              #change item on agent
              # (try_begin),
                # (player_get_agent_id, ":player_agent", ":player_no"),
                # (ge, ":player_agent", 0),
                # (lt, ":equip_slot", 4),
                # (neg|is_vanilla_warband),
                # (agent_set_item_slot, ":player_agent", ":equip_slot", ":new_item", ":new_imod"),# removed in WSE 3 
              # (try_end),

              (try_begin),
                (player_get_agent_id, ":player_agent", ":player_no"),
                (ge, ":player_agent", 0),
                (lt, ":equip_slot", 4),
                (try_begin), 
                  (gt, ":cur_item", 0),
                  (agent_unequip_item,":player_agent",":cur_item",":equip_slot"),
                (try_end),
                (agent_equip_item,":player_agent",":new_item",":equip_slot"),

                (neg|is_vanilla_warband),
                (agent_set_item_slot_modifier, ":player_agent",":equip_slot", ":new_imod"), #Sets <agent_no>'s <item_slot_no> modifier to <item_modifier_no>
              (try_end),



            (else_try),
              (display_message, "@Trade failed."),
            (try_end),
            #after trade refresh that equip slot
            (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":equip_slot"),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":equip_slot", ":player_cur_item", ":player_cur_imod"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done


            (try_begin), 
              (gt, ":new_item", 0),
              (str_store_item_name, s40, ":new_item"),
            (else_try),
              (str_store_string, s40, "@none"),
            (try_end),
            (try_begin), 
              (gt, ":cur_item", 0),
              (str_store_item_name, s42, ":cur_item"),
            (else_try),
              (str_store_string, s42, "@none"),
            (try_end),
            (str_store_troop_name, s41, ":player_troop"),
            (display_message, "@{s41} traded {s42} for {s40}."),

          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_player_remove_selected_item),
          (store_script_param, ":equip_slot", 4),
          (store_script_param, ":item_remove", 5),
          (player_get_slot,  ":player_troop", ":player_no", slot_player_coop_selected_troop),
          (try_begin), #if agent has spawned already
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (try_begin),
            (gt, ":item_remove", 0),
            (troop_get_inventory_slot, ":cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":cur_imod", ":player_troop", ":equip_slot"),
            (eq, ":item_remove", ":cur_item"),

            (troop_get_inventory_capacity, ":end", "trp_temp_troop"),
            (val_add,":end", 1), 
            (try_for_range, ":party_inv_slot", 10, ":end"),
              (troop_get_inventory_slot, ":party_inv_item", "trp_temp_troop", ":party_inv_slot"),
              (lt, ":party_inv_item", 1),
              (troop_set_inventory_slot, ":player_troop", ":equip_slot", -1),
              (troop_set_inventory_slot_modifier, ":player_troop", ":equip_slot", -1),
              (troop_set_inventory_slot, "trp_temp_troop", ":party_inv_slot", ":cur_item"),
              (troop_set_inventory_slot_modifier, "trp_temp_troop", ":party_inv_slot", ":cur_imod"),

              (try_begin),
                (lt, ":equip_slot", 4),
                (player_get_agent_id, ":player_agent", ":player_no"),
                (ge, ":player_agent", 0),
                (agent_unequip_item, ":player_agent", ":cur_item", ":equip_slot"), #(agent_unequip_item, <agent_id>, <item_id>, [weapon_slot_no]),
              (try_end),
              (assign, ":end", 0),
            (try_end),
          (try_end),

        (try_end),


      (try_end),
    (try_end),


## CLIENT EVENTS ##
  (try_begin),
    (neg|multiplayer_is_dedicated_server),
    (try_begin),
      (eq, ":event_type", multiplayer_event_coop_send_to_player_string),

      (try_begin),
        (eq, "$coop_string_received", 0), 
        (faction_set_name, "fac_player_supporters_faction", s0),
        (assign, "$coop_string_received", 1), 
      (else_try),
        (eq, "$coop_string_received", 1), 
        (class_set_name, "$coop_class_string_received", s0), #store 8 strings for troop class names
        (val_add, "$coop_class_string_received", 1),

        (try_begin),
          (eq, "$coop_class_string_received", 9), # 8 strings, add one after each = 9
          (assign, "$coop_string_received", 2), 
        (try_end),
      (else_try),
#NEW
        (eq, "$coop_string_received", 2), 
        (troop_set_name, "$coop_last_hero_received", s0),
        (assign, "$coop_string_received", 3), 
      (else_try),
        (eq, "$coop_string_received", 3), 
        (try_begin),
          (neg|is_vanilla_warband),
          (face_keys_store_string, reg1, s0),
          #ENVFIX(troop_set_face_keys, "$coop_last_hero_received", reg1),
        (try_end),
        (assign, "$coop_string_received", 2), 

      (else_try),
        (eq, "$coop_string_received", 4), #set by coop_event_round
        (server_set_password, s0),
      (try_end),

    (else_try),
      (eq, ":event_type", multiplayer_event_coop_send_to_player), 
      (store_script_param, ":event_subtype", 3),

      (try_begin),
        (eq, ":event_subtype", coop_event_store_hero_troops), 
        (store_script_param, ":hero_troop", 4),
        (store_script_param, ":var_6", 5),
        (try_begin),
          (neg|multiplayer_is_server), #server already added heroes to this party
          (party_add_members, ":var_6", ":hero_troop", 1),
        (try_end),
        (assign, "$coop_last_hero_received", ":hero_troop"), #remember troop to receive name
      (else_try),
        (eq, ":event_subtype", coop_event_round), 
        (store_script_param, ":value", 4),
        (store_script_param, ":value2", 5),
        (assign, "$coop_battle_started", ":value2"),
        (assign, "$coop_round", ":value"), #assign siege round
#NEW
#ADd events here

#End add events here
        (assign, "$coop_string_received", 4), #set this after client has received all data
        (neq, "$coop_battle_started", -1),
		#DEBUG FOR Co-Op display messages Begin
		#(display_message, "@Set this after client has received ALL data."),
#		#(multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, "str_revision"), #New #REVISION VERSION
          # player remembers troop selections, send to server when player joins (player id will change between rounds)
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_bot_type_1_wanted, "$g_multiplayer_bot_type_1_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_bot_type_2_wanted, "$g_multiplayer_bot_type_2_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_bot_type_3_wanted, "$g_multiplayer_bot_type_3_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_bot_type_4_wanted, "$g_multiplayer_bot_type_4_wanted"),

          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_0_wanted, "$coop_class_0_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_1_wanted, "$coop_class_1_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_2_wanted, "$coop_class_2_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_3_wanted, "$coop_class_3_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_4_wanted, "$coop_class_4_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_5_wanted, "$coop_class_5_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_6_wanted, "$coop_class_6_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_7_wanted, "$coop_class_7_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, slot_player_coop_class_8_wanted, "$coop_class_8_wanted"),
		#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_dmod, "$setting_use_dmod"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch, "$key_crouch"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch_command, "$key_crouch_command"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_stand_command, "$key_stand_command"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_crouch_speed_limiter, "$g_crouch_speed_limiter"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_ai_crouch_mode, "$ai_crouch_mode"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_player_party_icon, "$g_player_party_icon"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash, "$sp_shield_bash_coop"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash_ai, "$sp_shield_bash_ai_coop"), #Step 4
					#	(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_spearwall, "$setting_use_spearwall"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation, "$g_battle_preparation"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation_phase, "$g_battle_preparation_phase"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_rand_rain_limit, "$g_rand_rain_limit"), #Step 4
			#			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_position, "$belfry_positioned"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_sound, "$belfry_sound"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_use_belfry, "$coop_use_belfry"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_reinforcement_waves, "$g_reinforcement_waves"),



			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_banners, "$tom_use_banners"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_bonus_banners, "$tom_bonus_banners"), #Step 4
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_battlefields, "$tom_use_battlefields"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_weapon_break, "$tom_weapon_break"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_lance_breaking, "$tom_lance_breaking"),
			###((multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_coop_generate_reduction, "$coop_generate_reduction"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_faction, "$crusader_faction"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_party_id, "$crusader_party_id"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_state, "$crusader_state"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_freelancer_state, "$freelancer_state"), #Step 4
			
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_men_are_pleased, "$men_are_pleased"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_longships, "$tom_use_longships"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_use_feudal_lance, "$use_feudal_lance"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_historical_banners, "$historical_banners"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_randomize_player_shield, "$randomize_player_shield"),
						#Numerical Settings Template Step 5 Begin (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_sand_storm_chance, "$tom_sand_storm_chance"),
						###((multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_torch_chance, "$torch_chance_coop"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_camera_mode, "$coop_extended_camera"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_voiceset, "$voice_set"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_sand_storm, "$tom_sand_storm"),
						#Numerical Settings Template Step 5 End (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
			#End Extension
        (try_begin), 
          (eq, "$coop_round", coop_round_battle),
          (assign, "$coop_my_team", multi_team_unassigned),  
          (start_presentation, "prsnt_coop_welcome_message"), #start welcome message after getting team data
        (else_try),
          (multiplayer_get_my_player, ":my_player_no"), #change my team in later rounds
          (ge, ":my_player_no", 0),
          (player_set_team_no, ":my_player_no", "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_team_no, "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, "$coop_my_troop_no"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_banner), 
        (store_script_param, ":value", 4),
        (assign, "$coop_agent_banner", ":value"), #assign spawning troops banner
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_attribute),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":attribute", 6),
        (troop_raise_attribute, ":selected_troop", ":attribute", -1000),
        (troop_raise_attribute, ":selected_troop", ":attribute", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_skill),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":skill_level_leadership_var_1", 6),
        (troop_raise_skill, ":selected_troop", ":skill_level_leadership_var_1", -1000),
        (troop_raise_skill, ":selected_troop", ":skill_level_leadership_var_1", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_proficiency_linear),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":prof", 6),
        (troop_raise_proficiency_linear, ":selected_troop", ":prof", -1000),
        (troop_raise_proficiency_linear, ":selected_troop", ":prof", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_set_slot),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":slot", 6),
        (troop_set_slot, ":selected_troop", ":slot", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_player_set_slot),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_player", 5),
        (store_script_param, ":slot", 6),
        (player_set_slot, ":selected_player", ":slot", ":value"),
        (try_begin), #if receiving other player spawn choice, refresh presentation
          (eq, ":slot", slot_player_coop_selected_troop),
          (assign, "$coop_refresh_troop_select_presentation", 1),

          (try_begin),
            (gt, ":value", 0),
            (str_store_player_username, s40, ":selected_player"),
            (str_store_troop_name, s41, ":value"),
            (display_message, "@{s40} has picked {s41}. "), #tell server when player picks troop
          (try_end), 
        (try_end), 
      (else_try),
        (eq, ":event_subtype", coop_event_inv_troop_set_slot),
        (store_script_param, ":slot", 4),
        (store_script_param, ":item", 5),
        (store_script_param, ":imod", 6),
        (troop_set_slot, "trp_temp_troop", ":slot", ":item"), #item slot 0..8
        (val_add, ":slot", 10),
        (troop_set_slot, "trp_temp_troop", ":slot", ":imod"),#imod slot 10..18


      (else_try),
        (eq, ":event_subtype", coop_event_send_inventory), #receive items of type for equipment slot
        (store_script_param, ":inv_slot", 4),
        (store_script_param, ":item", 5),
        (store_script_param, ":imod", 6),
        #  (store_script_param, ":item_quant", 6), #would need its own message type
        (store_add, ":cur_slot_index", "$coop_num_available_items", multi_data_item_button_indices_begin),
        (store_add, ":cur_imod_index",":cur_slot_index",100),
        (troop_set_slot, "trp_multiplayer_data", ":cur_slot_index", ":item"),
        (troop_set_slot, "trp_temp_troop", ":cur_slot_index", ":inv_slot"), #slot matching multi_data_item_button_indices_begin stores which inventory slot this item is from
        (troop_set_slot, "trp_temp_troop", ":cur_imod_index", ":imod"),
        (val_add, "$coop_num_available_items", 1),
      (else_try),
        (eq, ":event_subtype", coop_event_prsnt_coop_item_select),
        (start_presentation, "prsnt_coop_item_select"), #start presentation after we recieve all inventory
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_1),
        (store_script_param, ":value", 4),
        (assign, "$coop_time_of_day", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_2),
        (store_script_param, ":value", 4),
        (assign, "$coop_rain", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_3),
        (store_script_param, ":value", 4),
        (assign, "$coop_cloud", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_4),
        (store_script_param, ":value", 4),
        (assign, "$coop_haze", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_5),
        (store_script_param, ":value", 4),
        (assign, "$coop_castle_banner", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_team_faction),
        (store_script_param, ":team", 4),
        (store_script_param, ":value", 5),
        (try_begin), 
          (eq, ":team", 1),
          (assign, "$coop_team_1_faction", ":value"),
        (else_try),
          (eq, ":team", 2),
          (assign, "$coop_team_2_faction", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_return_team_troop_num),
        (store_script_param, ":team", 4),
        (store_script_param, ":value", 5),
        (try_begin), 
          (eq, ":team", 1),
          (assign, "$coop_team_1_troop_num", ":value"),
        (else_try),
          (eq, ":team", 2),
          (assign, "$coop_team_2_troop_num", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_return_spawn_formation),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_spawn_formation", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_set_setting_use_dmod),
    #    (store_script_param, ":value", 4),
    #    (assign, "$setting_use_dmod", ":value"),
		
		      (else_try),
        (eq, ":event_subtype", coop_set_key_crouch),
        (store_script_param, ":value", 4),
        (assign, "$key_crouch", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_key_crouch_command),
        (store_script_param, ":value", 4),
        (assign, "$key_crouch_command", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_key_stand_command),
        (store_script_param, ":value", 4),
        (assign, "$key_stand_command", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_g_crouch_speed_limiter),
        (store_script_param, ":value", 4),
        (assign, "$g_crouch_speed_limiter", ":value"),
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_ai_crouch_mode),
        (store_script_param, ":value", 4),
        (assign, "$ai_crouch_mode", ":value"),
				      (else_try),				  
    #    (eq, ":event_subtype", coop_set_g_player_party_icon),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_player_party_icon", ":value"),
	#			      (else_try),
					  
        (eq, ":event_subtype", coop_set_sp_shield_bash),
        (store_script_param, ":value", 4),
        (assign, "$sp_shield_bash_coop", ":value"),
						      (else_try),
					  
        (eq, ":event_subtype", coop_set_archerpos),
        (store_script_param, ":value", 4),
        (assign, "$experimental_archers", ":value"),
		
								      (else_try),
					  
        (eq, ":event_subtype", coop_set_ai_mode),
        (store_script_param, ":value", 4),
        (assign, "$g_doghotel_enable_brainy_bots", ":value"),
		
				      (else_try),
					  
        (eq, ":event_subtype", coop_set_sp_shield_bash_ai),
        (store_script_param, ":value", 4),
        (assign, "$sp_shield_bash_ai_coop", ":value"),
		#		      (else_try),
		#			  
      #(eq, ":event_subtype", coop_set_setting_use_spearwall),
      #(store_script_param, ":value", 4),
      #(assign, "$setting_use_spearwall", ":value"),
	#			      (else_try),
	#				  
    #    (eq, ":event_subtype", coop_set_g_battle_preparation),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_battle_preparation", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_set_g_battle_preparation_phase),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_battle_preparation_phase", ":value"),
				      (else_try),
        (eq, ":event_subtype", coop_set_g_rand_rain_limit),
        (store_script_param, ":value", 4),
        (assign, "$g_rand_rain_limit", ":value"),
		#						      (else_try),
        #(eq, ":event_subtype", coop_set_belfry_position),
        #(store_script_param, ":value", 4),
        #(assign, "$belfry_positioned", ":value"),
		#				      (else_try),
        #(eq, ":event_subtype", coop_set_belfry_sound),
        #(store_script_param, ":value", 4),
        #(assign, "$belfry_sound", ":value"),
		#						      (else_try),
        #(eq, ":event_subtype", coop_use_belfry),
        #(store_script_param, ":value", 4),
        #(assign, "$coop_use_belfry", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_set_g_reinforcement_waves),
    #    (store_script_param, ":value", 4),
    #    (assign, "$g_reinforcement_waves", ":value"),
#						      (else_try),
#        (eq, ":event_subtype", coop_set_tom_sand_storm_chance),
#        (store_script_param, ":value", 4),
#        (assign, "$tom_sand_storm_chance", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_tom_use_banners),
        (store_script_param, ":value", 4),
        (assign, "$tom_use_banners", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_tom_bonus_banners),
        (store_script_param, ":value", 4),
        (assign, "$tom_bonus_banners", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_tom_use_battlefields),
        (store_script_param, ":value", 4),
        (assign, "$tom_use_battlefields", ":value"),
		#				      (else_try),
       #(eq, ":event_subtype", coop_set_tom_weapon_break),
       #(store_script_param, ":value", 4),
       #(assign, "$tom_weapon_break", ":value"),
		#				      (else_try),
       #(eq, ":event_subtype", coop_set_tom_lance_breaking),
       #(store_script_param, ":value", 4),
       #(assign, "$tom_lance_breaking", ":value"),
						      (else_try),
        (eq, ":event_subtype", coop_set_coop_generate_reduction),
        (store_script_param, ":value", 4),
        (assign, "$coop_generate_reduction", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_faction),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_faction", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_party_id),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_party_id", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_crusader_state),
    #    (store_script_param, ":value", 4),
    #    (assign, "$crusader_state", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_freelancer_state),
    #    (store_script_param, ":value", 4),
    #    (assign, "$freelancer_state", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_men_are_pleased),
    #    (store_script_param, ":value", 4),
    #    (assign, "$men_are_pleased", ":value"),
		#				      (else_try),
       #(eq, ":event_subtype", coop_set_tom_use_longships),
       #(store_script_param, ":value", 4),
       #(assign, "$tom_use_longships", ":value"),
	#					      (else_try),
    #    (eq, ":event_subtype", coop_set_use_feudal_lance),
    #    (store_script_param, ":value", 4),
    #    (assign, "$use_feudal_lance", ":value"),
		      (else_try),
        (eq, ":event_subtype", coop_set_historical_banners),
        (store_script_param, ":value", 4),
        (assign, "$historical_banners", ":value"),
				      (else_try),
        (eq, ":event_subtype", coop_set_randomize_player_shield),
        (store_script_param, ":value", 4),
        (assign, "$randomize_player_shield", ":value"),
		#Numerical Settings Template Step 4 begin
		      (else_try),
			          (eq, ":event_subtype", coop_set_tom_sand_storm_chance),
        (store_script_param, ":value", 4),
        (assign, "$tom_sand_storm_chance", ":value"),
				      (else_try),
			          (eq, ":event_subtype", coop_sand_storm),
        (store_script_param, ":value", 4),
        (assign, "$tom_sand_storm", ":value"),
						      (else_try),
			          (eq, ":event_subtype", coop_voiceset),
        (store_script_param, ":value", 4),
        (assign, "$voice_set", ":value"),
		#Numerical Settings Template Step 4 end
				      (else_try),
			          (eq, ":event_subtype", coop_set_torch_chance),
        (store_script_param, ":value", 4),
        (assign, "$torch_chance_coop", ":value"),
		#Numerical Settings Template Step 4 end
      (else_try),
	  			  #Begin terrain generation
        (eq, ":event_subtype", coop_set_camera_mode), # STEP 4
        (store_script_param, ":value", 4),
        (assign, "$coop_extended_camera", ":value"),
				      (else_try),
	#		  #Begin terrain generation
    #    (eq, ":event_subtype", coop_generate_swamp), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_swamp", ":value"),
	#			      (else_try),
    #    (eq, ":event_subtype", coop_generate_desert), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_desert", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_desertv2), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_desertv2", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_desertv3), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_desertv3", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_iberian), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_iberian", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_iberian2), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_iberian2", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_snow), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_snow", ":value"),
    #  (else_try),
	#          (eq, ":event_subtype", coop_generate_euro_hillside), # STEP 4
    #    (store_script_param, ":value", 4),
    #    (assign, "$coop_generate_euro_hillside", ":value"),
    #  (else_try),
	 #Emd terrain generaiton
        (eq, ":event_subtype", coop_event_return_battle_size),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_size", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_game_type),
        (store_script_param, ":value", 4),
        (assign, "$g_multiplayer_game_type", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_castle_party),
        (store_script_param, ":value", 4),
        (assign, "$coop_map_party", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_battle_scene),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_scene", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_disable_inventory),
        (store_script_param, ":value", 4),
        (assign, "$coop_disable_inventory", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_reduce_damage),
        (store_script_param, ":value", 4),
        (assign, "$coop_reduce_damage", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_no_capture_heroes),
        (store_script_param, ":value", 4),
        (assign, "$coop_no_capture_heroes", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_skip_menu),
        (store_script_param, ":value", 4),
        (assign, "$coop_skip_menu", ":value"),
        (start_presentation, "prsnt_coop_admin_panel"),#this is the last option in admin panel, so start the presentation
      (else_try),
        (eq, ":event_subtype", coop_event_return_open_game_rules),
        #this is the last message for open rules
        (assign, "$g_multiplayer_show_server_rules", 1),
        (start_presentation, "prsnt_coop_welcome_message"),
      (else_try),
        (eq, ":event_subtype", coop_event_receive_next_string),
        (store_script_param, ":value", 4),
        (assign, "$coop_string_received", ":value"), 
      (else_try),
        (eq, ":event_subtype", coop_event_return_num_reserves),
        (store_script_param, ":team", 4),
        (store_script_param, ":value", 5),
        (try_begin), 
          (eq, ":team", 1),
          (assign, "$coop_num_bots_team_1", ":value"),
        (else_try),
          (eq, ":team", 2),
          (assign, "$coop_num_bots_team_2", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_return_battle_state),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_state", ":value"), 
      (else_try),
        (eq, ":event_subtype", coop_event_result_saved),
        (assign, "$coop_battle_started", -1),
        (display_message, "@Battle result saved.", 0x000730fc),
		(display_message, "@You can now load back your save and reach the same encounter then hit (Use Multiplayer Battle Results)", 0x000730fc),
		#####MUSICBOX
		(neg|multiplayer_is_dedicated_server),
		##(stop_all_sounds, 1), #Used to be value of 11new
      (try_end), 





    (try_end),  
  (try_end),  

      ]),





#script_coop_server_send_admin_settings_to_player
  # Input: arg1 = player_agent
  # Output: none
  ("coop_server_send_admin_settings_to_player",
    [
     (store_script_param, ":player_no", 1),
            (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
            (server_get_max_num_players, ":max_num_players"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
            # (server_get_anti_cheat, ":server_anti_cheat"),
            # (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
            (server_get_friendly_fire, ":server_friendly_fire"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
            (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
            (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
            (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
            (server_get_ghost_mode, ":server_ghost_mode"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
            (server_get_control_block_dir, ":server_control_block_dir"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
            (server_get_combat_speed, ":server_combat_speed"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
            (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
            (str_store_server_name, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_receive_next_string, 0),
            (str_store_faction_name, s0, "fac_player_supporters_faction"),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_faction, 1, "$coop_team_1_faction"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_faction, 2, "$coop_team_2_faction"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_troop_num, 1, "$coop_team_1_troop_num"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_troop_num, 2, "$coop_team_2_troop_num"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_spawn_formation, "$coop_battle_spawn_formation"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_size, "$coop_battle_size"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_game_type, "$g_multiplayer_game_type"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_scene, "$coop_battle_scene"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_disable_inventory, "$coop_disable_inventory"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_reduce_damage, "$coop_reduce_damage"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_no_capture_heroes, "$coop_no_capture_heroes"),
			#Begin terrain generation
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_swamp, "$coop_generate_swamp"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desert, "$coop_generate_desert"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desertv2, "$coop_generate_desertv2"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_desertv3, "$coop_generate_desertv3"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_iberian, "$coop_generate_iberian"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_iberian2, "$coop_generate_iberian2"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_snow, "$coop_generate_snow"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_generate_euro_hillside, "$coop_generate_euro_hillside"), #Step 4
			#End terrain generation
			
			#Extend to all Co-Op Cmds for MP
			#DEBUG FOR Co-Op display messages Begin
			#(display_message, "@TESTING Multiplayer int_2 event coop_scripts ADMINONLY - only connecting player should see this."),
			#DEBUG FOR Co-Op display messages End
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_dmod, "$setting_use_dmod"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch, "$key_crouch"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_crouch_command, "$key_crouch_command"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_key_stand_command, "$key_stand_command"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_crouch_speed_limiter, "$g_crouch_speed_limiter"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_ai_crouch_mode, "$ai_crouch_mode"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_player_party_icon, "$g_player_party_icon"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash, "$sp_shield_bash_coop"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_archerpos, "$experimental_archers"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_ai_mode, "$g_doghotel_enable_brainy_bots"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_sp_shield_bash_ai, "$sp_shield_bash_ai_coop"), #Step 4
					#	(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_setting_use_spearwall, "$setting_use_spearwall"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation, "$g_battle_preparation"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_battle_preparation_phase, "$g_battle_preparation_phase"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_rand_rain_limit, "$g_rand_rain_limit"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_position, "$belfry_positioned"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_belfry_sound, "$belfry_sound"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_use_belfry, "$coop_use_belfry"), #Step 4
			
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_g_reinforcement_waves, "$g_reinforcement_waves"),



			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_banners, "$tom_use_banners"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_bonus_banners, "$tom_bonus_banners"), #Step 4
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_battlefields, "$tom_use_battlefields"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_weapon_break, "$tom_weapon_break"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_lance_breaking, "$tom_lance_breaking"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_coop_generate_reduction, "$coop_generate_reduction"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_faction, "$crusader_faction"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_party_id, "$crusader_party_id"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_crusader_state, "$crusader_state"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_freelancer_state, "$freelancer_state"), #Step 4
			
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_men_are_pleased, "$men_are_pleased"),
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_use_longships, "$tom_use_longships"), #Step 4
			#(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_use_feudal_lance, "$use_feudal_lance"),
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_historical_banners, "$historical_banners"), #Step 4
			(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_randomize_player_shield, "$randomize_player_shield"),
						#Numerical Settings Template Step 5 Begin (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_tom_sand_storm_chance, "$tom_sand_storm_chance"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_torch_chance, "$torch_chance_coop"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_set_camera_mode, "$coop_extended_camera"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_voiceset, "$voice_set"),
						(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_sand_storm, "$tom_sand_storm"),
						#Numerical Settings Template Step 5 End (Note: if you wish to extend so that it allows you to save the changes into the campaign - set dict_get_int and dict_set_int).
			#End Extension
			#If adding additional features all you need is to add send to player above and event_subtype, as well as make a new constant in module_constants similiar to coop_set_ right here.
			#If you wish to extend to the menu, you'll have to do more, just read module_coop_presentations.
      ]),


#script_coop_player_access_inventory
  # Input: arg1 = player_agent
  # Output: none
  ("coop_player_access_inventory",
    [
     (store_script_param, ":player_agent", 1),
        (try_begin),
          (eq, "$coop_disable_inventory", 0),#inventory access is optional
          (agent_get_player_id,":player_no",":player_agent"),#only let troops from main party use box
          (agent_get_troop_id,":player_troop", ":player_agent"),
          (agent_get_slot, ":player_agent_party",":player_agent", slot_agent_coop_spawn_party), #SP party
          (eq, ":player_agent_party", "$coop_main_party_spawn"),
          (troop_is_hero, ":player_troop"),
          
          #first add agent items to troop
          (call_script, "script_coop_player_agent_save_items", ":player_agent"),

          #then send what troop has
          (try_for_range, ":slot", 0, 9),
            (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":slot"),
            (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":slot"),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":slot", ":player_cur_item", ":player_cur_imod"),
          (try_end),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done
        (try_end),

      ]),

#NEW
#script_coop_player_agent_save_items
  # Input: arg1 = player_agent
  # Output: none
  ("coop_player_agent_save_items",
    [
     (store_script_param, ":player_agent", 1),
      (agent_get_troop_id, ":agent_troop_id", ":player_agent"),
      #store items from agents
      (try_begin), 
        (neg|is_vanilla_warband),
        (try_for_range, ":slot", 0, 4), #weapons only
          (agent_get_item_slot, ":agent_item_id", ":player_agent", ":slot"), 
          (agent_get_item_slot_modifier, ":agent_imod", ":player_agent", ":slot"),
          (troop_set_inventory_slot, ":agent_troop_id", ":slot", ":agent_item_id"),
          (troop_set_inventory_slot_modifier, ":agent_troop_id", ":slot", ":agent_imod"),
        (try_end),
      (try_end),
      ]),



#ITEM BUG WORKAROUND BEGIN#####################################################
# these scripts avoid a bug that removes ranged weapons when certain thrown weapons are equiped
#script_coop_equip_player_agent
  # Input: arg1 = player_agent
  # Output: none
  ("coop_equip_player_agent",
    [
     (store_script_param, ":player_agent", 1),
        (try_begin),
          (agent_get_troop_id,":troop_2", ":player_agent"),
          (troop_is_hero, ":troop_2"),
          (troop_slot_eq, ":troop_2", 19, 1), 

          (try_for_range, ":slot", 0, 4), #only check weapons
            (store_add, ":itm_slot", ":slot", 20),
            (troop_get_slot, ":item", ":troop_2", ":itm_slot"), 
            (troop_set_inventory_slot, ":troop_2", ":slot", ":item"),

            (store_add, ":imod_slot", ":slot", 30),
            (troop_get_slot, ":imod", ":troop_2", ":imod_slot"), 
            (troop_set_inventory_slot_modifier, ":troop_2", ":slot", ":imod"),
            # (agent_set_item_slot, ":player_agent", ":slot", ":item", ":imod"),# removed in WSE 3
 #FIX
            (try_begin), 
              (gt, ":item", 0),
              (agent_unequip_item,":player_agent",":item",":slot"),
            (try_end),
            (agent_equip_item,":player_agent",":item",":slot"),
            (neg|is_vanilla_warband),
            (agent_set_item_slot_modifier, ":player_agent",":slot", ":imod"), #Sets <agent_no>'s <item_slot_no> modifier to <item_modifier_no>
          (try_end),
        (try_end),
      ]),
#script_coop_check_item_bug
  ("coop_check_item_bug",
    [
     (store_script_param, ":troop_4", 1),
      (try_begin),
        (troop_is_hero, ":troop_4"),
        (try_for_range, ":slot", 19, 34), #clear slots here
          (troop_set_slot, ":troop_4", ":slot", 0), 
        (try_end),
        (assign, ":has_throw",0),
        (assign, ":has_ranged",0),

        (try_for_range, ":slot", 0, 4), #weapon slots
          (troop_get_inventory_slot, ":item", ":troop_4", ":slot"),
          (troop_get_inventory_slot_modifier, ":imod", ":troop_4", ":slot"),
          (gt, ":item", 0),
          (store_add, ":itm_slot", ":slot", 20),
          (store_add, ":imod_slot", ":slot", 30),
          (troop_set_slot, ":troop_4", ":itm_slot", ":item"), 
          (troop_set_slot, ":troop_4", ":imod_slot", ":imod"), 
          (item_get_type, ":type", ":item"),
          (try_begin),
            (eq, ":type", itp_type_thrown),
            (assign, ":has_throw", 1),
          (else_try),
            (this_or_next|eq, ":type", itp_type_pistol),
            (this_or_next|eq, ":type", itp_type_musket),
            (this_or_next|eq, ":type", itp_type_bow),
            (eq, ":type", itp_type_crossbow),
            (assign, ":has_ranged",1),
          (try_end),
        (try_end),
        (eq, ":has_throw", 1),
        (eq, ":has_ranged", 1),
        (troop_set_slot, ":troop_4", 19, 1), #troop has thrown and ranged
      (try_end),
      ]),
#ITEM BUG WORKAROUND END#####################################################



  #script_coop_display_available_items_from_inventory
  # Input: arg1 = troop_no, arg2 = item_classes_begin, arg3 = item_classes_end, arg4 = pos_x_begin, arg5 = pos_y_begin
  # Output: none
  ("coop_display_available_items_from_inventory",
   [
     #sorting
      (store_add, ":item_slots_end", "$coop_num_available_items", multi_data_item_button_indices_begin),
     (store_sub, ":item_slots_end_minus_one", ":item_slots_end", 1),
     (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end_minus_one"),
       (store_add, ":cur_slot_2_begin", ":cur_slot", 1),
       (try_for_range, ":cur_slot_2", ":cur_slot_2_begin", ":item_slots_end"),
         (troop_get_slot, ":item_1", "trp_multiplayer_data", ":cur_slot"),
         (troop_get_slot, ":item_2", "trp_multiplayer_data", ":cur_slot_2"),

         (store_item_value, ":item_1_point", ":item_1"),
         (store_item_value, ":item_2_point", ":item_2"),
         (item_get_type, ":item_1_class", ":item_1"),
         (item_get_type, ":item_2_class", ":item_2"),

         (try_begin),
           (eq, ":item_1_class", 7),
           (assign, ":item_1_class", 12),
         (try_end),
         (try_begin),
           (eq, ":item_2_class", 7),
           (assign, ":item_2_class", 12),
         (try_end),

         (val_mul, ":item_1_class", 1000000), #assuming maximum item price is 1000000
         (val_mul, ":item_2_class", 1000000), #assuming maximum item price is 1000000
         (val_sub, ":item_1_point", ":item_1_class"),
         (val_sub, ":item_2_point", ":item_2_class"),

         (gt, ":item_2_point", ":item_1_point"),
         (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":item_2"),
         (troop_set_slot, "trp_multiplayer_data", ":cur_slot_2", ":item_1"),

         (troop_get_slot, ":inv_slot_1", "trp_temp_troop", ":cur_slot"), #also sort other data slots
         (troop_get_slot, ":inv_slot_2", "trp_temp_troop", ":cur_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":cur_slot", ":inv_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":cur_slot_2", ":inv_slot_1"),

         (store_add, ":imod_slot", ":cur_slot", 100),
         (store_add, ":imod_slot_2", ":cur_slot_2", 100),
         (troop_get_slot, ":imod_1", "trp_temp_troop", ":imod_slot"),
         (troop_get_slot, ":imod_2", "trp_temp_troop", ":imod_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":imod_slot", ":imod_2"),
         (troop_set_slot, "trp_temp_troop", ":imod_slot_2", ":imod_1"),

       (try_end),
     (try_end),

      (str_clear, s0),
      (create_text_overlay, reg0, s0, tf_scrollable_style_2),
      (position_set_x, pos1, 200),#260
      (position_set_y, pos1, 75),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 604),
      (position_set_y, pos1, 604),
      (overlay_set_area_size, reg0, pos1),
      (set_container_overlay, reg0),

     (assign, ":x_adder", 100),
     (assign, ":pos_x_begin", 0),
     (store_sub, ":pos_y_begin", "$coop_num_available_items", 1),  #number of items / 6 = number of rows
     (val_div, ":pos_y_begin", 6),
     (val_mul, ":pos_y_begin", 100),
     (val_add, ":pos_y_begin", 10),

     (assign, ":cur_x", ":pos_x_begin"),
     (assign, ":cur_y", ":pos_y_begin"),
     (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
       (troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),

       (create_image_button_overlay, ":cur_obj", "mesh_mp_inventory_choose", "mesh_mp_inventory_choose"),
       (position_set_x, pos1, 800),#800
       (position_set_y, pos1, 800),#800
       (overlay_set_size, ":cur_obj", pos1),
       (position_set_x, pos1, ":cur_x"),
       (position_set_y, pos1, ":cur_y"),
       (overlay_set_position, ":cur_obj", pos1),
       (create_mesh_overlay_with_item_id, reg0, ":item_no"),
       (store_add, ":item_x", ":cur_x", 50),
       (store_add, ":item_y", ":cur_y", 50),
       (position_set_x, pos1, ":item_x"),
       (position_set_y, pos1, ":item_y"),
       (overlay_set_position, reg0, pos1),

       (val_add, ":cur_x", ":x_adder"),
       (try_begin),
         (gt, ":cur_x", 500),
         (val_sub, ":cur_y", 100),
         (assign, ":cur_x", ":pos_x_begin"),
       (try_end),
     (try_end),
     ]),



  #script_coop_move_belfries_to_their_first_entry_point
  # INPUT: none
  # OUTPUT: none
  ("coop_move_belfries_to_their_first_entry_point",
   [
    (store_script_param, ":belfry_body_scene_prop", 1),
     
    (set_fixed_point_multiplier, 100),    
    (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
    
    (try_for_range, ":belfry_no", 0, ":num_belfries"),
      #belfry 
      (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
      (prop_instance_get_position, pos0, ":belfry_scene_prop_id"),

      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_a"),
        #belfry platform_a
        (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
        #belfry platform_b
        (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
      (else_try),
        #belfry platform_a
        (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
      (try_end),
    
      #belfry wheel_1
      (store_mul, ":wheel_no", ":belfry_no", 3),
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
        (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
        (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
      (try_end),    
      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
      #belfry wheel_2
      (val_add, ":wheel_no", 1),
      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
      #belfry wheel_3
      (val_add, ":wheel_no", 1),
      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),


#      (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
      (store_add, ":belfry_first_entry_point_id", 5, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139


      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
        (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
      (try_end),    
      (val_mul, ":belfry_first_entry_point_id", 10),
      (entry_point_get_position, pos1, ":belfry_first_entry_point_id"),

      #this code block is taken from module_mission_templates.py (multiplayer_server_check_belfry_movement)
      #up down rotation of belfry's next entry point
      (init_position, pos9),
      (position_set_y, pos9, -500), #go 5.0 meters back
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), 
      (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry

      (init_position, pos9),
      (position_set_y, pos9, -500), #go 5.0 meters back
      (position_set_x, pos9, 300), #go 3.0 meters right
      (position_transform_position_to_parent, pos10, pos1, pos9), 
      (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

      (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
      (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

      (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
      (init_position, pos20),    
      (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
      (position_transform_position_to_parent, pos23, pos1, pos20),

      #right left rotation of belfry's next entry point
      (init_position, pos9),
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
      (init_position, pos9),
      (position_set_x, pos9, 300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
      (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

      (init_position, pos9),
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_set_y, pos9, -500), #go 5.0 meters forward
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
      (init_position, pos9),
      (position_set_x, pos9, 300), #go 3.0 meters left
      (position_set_y, pos9, -500), #go 5.0 meters forward
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
      (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

      (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),    
      (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
      (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees. 
      (val_mul, ":rotate_angle_of_next_entry_point", -1),

      (init_position, pos20),
      (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
      (position_transform_position_to_parent, pos22, pos23, pos20),

      (copy_position, pos1, pos22),
      #end of code block

      #belfry 
      (prop_instance_stop_animating, ":belfry_scene_prop_id"),
      (prop_instance_set_position, ":belfry_scene_prop_id", pos1),
      # (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos1,1), #NEW
    
      #belfry platforms
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_a"),

        #belfry platform_a
        (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (try_begin),
          (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", slot_scene_prop_belfry_platform_moved, 0),
     
          (init_position, pos20),
          (position_rotate_x, pos20, 90),
          (position_transform_position_to_parent, pos8, pos8, pos20),
        (try_end),
        (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),  
        (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8,1), #NEW
        #belfry platform_b
        (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_b_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8,1), #NEW
      (else_try),
        #belfry platform_a
        (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (try_begin),
          (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", slot_scene_prop_belfry_platform_moved, 0),
     
          (init_position, pos20),
          (position_rotate_x, pos20, 50),
          (position_transform_position_to_parent, pos8, pos8, pos20),
        (try_end),
        (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),    
      (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8,1), #NEW
      (try_end),
    
      #belfry wheel_1
      (store_mul, ":wheel_no", ":belfry_no", 3),
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
        (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
        (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
      (try_end),
      (prop_instance_get_position, pos6, ":belfry_wheel_1_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_1_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_1_scene_prop_id", pos8,1), #NEW
      #belfry wheel_2
      (prop_instance_get_position, pos6, ":belfry_wheel_2_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_2_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_2_scene_prop_id", pos8,1), #NEW
      #belfry wheel_3
      (prop_instance_get_position, pos6, ":belfry_wheel_3_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_3_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_3_scene_prop_id", pos8,1), #NEW
    (try_end),
    ]),


  # script_cf_coop_siege_assign_men_to_belfry
  # Input: none
  # Output: none (required for siege mission templates)
  ("cf_coop_siege_assign_men_to_belfry",
   [
    (store_script_param, ":pos_no", 1),

    (try_begin),
      (lt, "$belfry_positioned", 3),

      (copy_position, pos42, ":pos_no"),
      (assign, ":belfry_num_men", 0),
        (try_for_agents, ":cur_agent"),#count how many targeting belfry
          (agent_is_alive, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_get_team, ":cur_agent_team", ":cur_agent"),
          (eq, "$attacker_team", ":cur_agent_team"),
          # (agent_get_group, ":agent_group", ":cur_agent"),
          # (eq, ":agent_group", -1),#not player commanded
          (try_begin),
            (agent_get_slot, ":x_pos", ":cur_agent", slot_agent_target_x_pos),
            (neq, ":x_pos", 0),
            (agent_get_slot, ":y_pos", ":cur_agent", slot_agent_target_y_pos),
            (val_add, ":belfry_num_men", 1),
            (init_position, pos41),
            (position_move_x, pos41, ":x_pos"),
            (position_move_y, pos41, ":y_pos"),
            (init_position, pos43),
            (val_mul, ":x_pos", 3),
            (position_move_x, pos43, ":x_pos"),
            (position_move_y, pos43, -1100),
            (position_transform_position_to_parent, pos44, pos42, pos41),
            (position_transform_position_to_parent, pos45, pos42, pos43),
            (agent_get_position, pos46, ":cur_agent"),
            (get_distance_between_positions, ":target_distance", pos46, pos44),
            (get_distance_between_positions, ":waypoint_distance", pos46, pos45),
            (try_begin),
              (this_or_next|lt, ":target_distance", ":waypoint_distance"),
              (lt, ":waypoint_distance", 1600), # > 1/2 pos1 - pos4
              (agent_set_scripted_destination, ":cur_agent", pos44, 1),
            (else_try),
              (agent_set_scripted_destination, ":cur_agent", pos45, 1),
              #(display_message, "@assigned to waypoint"),
            (try_end),

          (try_end),
        (try_end),

      (try_begin),
        (lt, ":belfry_num_men", 20), 


          (try_for_agents, ":cur_agent"), #add more troops if low
            (lt, ":belfry_num_men", 20), #stop adding when max number to push
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (eq, "$attacker_team", ":cur_agent_team"),
            (agent_get_slot, ":x_pos", ":cur_agent", slot_agent_target_x_pos),
            (eq, ":x_pos", 0),
            (assign, ":y_pos", 0),
            (store_random_in_range, ":side", 0, 2),
            (try_begin),
              (eq, ":side", 1),
              (assign, ":x_pos", -400),
            (else_try),
              (assign, ":x_pos", 400),
            (try_end),
            (val_add, ":belfry_num_men", 1),
            (agent_set_slot, ":cur_agent", slot_agent_target_x_pos, ":x_pos"),
            (agent_set_slot, ":cur_agent", slot_agent_target_y_pos, ":y_pos"),
          (try_end),
      (try_end),
    # (else_try), #we already clear scripted in mission template
      # (try_for_agents, ":cur_agent"),
        # (agent_get_team, ":cur_agent_team", ":cur_agent"),
        # (eq, "$attacker_team", ":cur_agent_team"),
        # (agent_clear_scripted_mode, ":cur_agent"),
      # (try_end),
    (try_end),

  ]),

######## 	
  # script_coop_spawn_formation
  # Input: arg1 = agent_no
  # Output: none
  ("coop_spawn_formation",
    [
      (store_script_param, ":agent_no", 1),
      (try_begin),

        (try_begin),
          (agent_is_human, ":agent_no"), #horse spawns after rider
          (assign, ":human_agent", ":agent_no"), 
        (else_try),
          (agent_get_rider, ":human_agent", ":agent_no"),
        (try_end),

        (agent_get_team, ":agent_team", ":human_agent"),
        (agent_get_division, ":agent_class", ":human_agent"), #agent_get_class only works after horsemen have horses

        (try_begin),
          (neg|agent_is_human, ":agent_no"),
          (assign, ":pos", "$coop_form_line_last_pos"),
        (else_try),
          (eq, ":agent_team", 0),
          (try_begin),
            (eq, ":agent_class", grc_archers),   
            (assign, ":pos", pos25),
            (try_begin),
              (eq, "$coop_form_line_grp_1", 1),  
              (assign, "$coop_form_line_grp_1", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_1", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_infantry), 
            (assign, ":pos", pos26), 
            (try_begin),
              (eq, "$coop_form_line_grp_2", 1),  
              (assign, "$coop_form_line_grp_2", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_2", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_cavalry),   
            (assign, ":pos", pos27),
            (try_begin),
              (eq, "$coop_form_line_grp_3", 1),  
              (assign, "$coop_form_line_grp_3", 0),    
              (position_move_y, ":pos", -300),
            (else_try),
              (assign, "$coop_form_line_grp_3", 1),   
              (position_move_y, ":pos", 300),
              (position_move_x, ":pos", 100),
            (try_end),
          (try_end),

        (else_try),
          (eq, ":agent_team", 1),
          (try_begin),
            (eq, ":agent_class", grc_archers),   
            (assign, ":pos", pos30),
            (try_begin),
              (eq, "$coop_form_line_grp_4", 1),  
              (assign, "$coop_form_line_grp_4", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_4", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_infantry), 
            (assign, ":pos", pos31), 
            (try_begin),
              (eq, "$coop_form_line_grp_5", 1),  
              (assign, "$coop_form_line_grp_5", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_5", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_cavalry),  
            (assign, ":pos", pos32),
            (try_begin),
              (eq, "$coop_form_line_grp_6", 1),  
              (assign, "$coop_form_line_grp_6", 0),    
              (position_move_y, ":pos", -300),
            (else_try),
              (assign, "$coop_form_line_grp_6", 1),   
              (position_move_y, ":pos", 300),
              (position_move_x, ":pos", 100),
            (try_end),
          (try_end),
        (try_end),

        # (try_begin),
          # (agent_is_human, ":agent_no"),
          # (position_move_x, ":pos", 100),
        # (try_end),
        (assign, "$coop_form_line_last_pos", ":pos"), #store last pos for horses
        (agent_set_position, ":agent_no", ":pos"),
        (agent_set_scripted_destination, ":agent_no", ":pos", 1),

      (try_end),

      ]),

######## 	
  # script_coop_form_line
  # Input: arg1 = agent_no
  # Output: none
  ("coop_form_line",
    [
      (store_script_param, ":pos_no", 1),
      (store_script_param, ":team", 2),
      (store_script_param, ":class", 3),
      (store_script_param, ":dist_to_next_row", 4),
      (store_script_param, ":dist_to_next_troop", 5),
      (store_script_param, ":num_rows", 6),
      (store_script_param, ":move_to_pos", 7),#set agent at position like spawning

      (store_sub, ":dist_to_first_row", 1, ":num_rows"),
      (val_mul, ":dist_to_first_row", ":dist_to_next_row"),

      (init_position, pos35),
      (copy_position, pos35, ":pos_no"),
      (assign, ":row", 1),
      (try_for_agents, ":agent_no"),
        (agent_is_alive, ":agent_no"),
        (agent_is_human, ":agent_no"),
        (agent_get_team, ":agent_team", ":agent_no"),
        (eq, ":agent_team", ":team"),
        (agent_get_slot, ":x_pos", ":agent_no", slot_agent_target_x_pos), #if agent is not pushing belfry
        (eq, ":x_pos", 0),
        # (agent_get_group, ":agent_group", ":agent_no"),
        # (eq, ":agent_group", -1),
        (agent_get_class, ":agent_class", ":agent_no"),
        (this_or_next|eq, ":class", grc_everyone),   
        (eq, ":agent_class", ":class"),   
        (try_begin),
          (eq, ":move_to_pos", 1), #set agent at position like spawning
          (agent_get_horse, ":agent_horse", ":agent_no"),
          (agent_set_position, ":agent_horse", pos35),
          (agent_set_position, ":agent_no", pos35),
        (try_end),
        (agent_set_scripted_destination, ":agent_no", pos35, 1),
        (try_begin),
          (eq, ":row", ":num_rows"),
          (assign, ":row", 1),
          (position_move_x, pos35, ":dist_to_next_troop"),
          (position_move_y, pos35, ":dist_to_first_row"),
        (else_try),
          (position_move_y, pos35, ":dist_to_next_row"),
          (val_add, ":row", 1),
        (try_end),
      (try_end),

      ]),

######## 	all in party doesnot include castle garrison, by type includes allies
  # script_coop_change_leader_of_bot
  # Input: arg1 = agent_no
  # Output: none
  ("coop_change_leader_of_bot",
    [
      (store_script_param, ":agent_no", 1),

      (agent_get_team, ":team_no", ":agent_no"),
      (agent_get_troop_id,":agent_troop", ":agent_no"),
      (troop_get_slot, ":troop_class", ":agent_troop", slot_troop_current_rumor), #use to store class in MP (so we dont affect ai classes too)
      # (troop_get_class, ":troop_class", ":agent_troop"),
      (agent_get_class, ":agent_class", ":agent_no"),
      (agent_get_slot, ":agent_party_no",":agent_no", slot_agent_coop_spawn_party),# coop party
      (agent_get_group, ":agent_group", ":agent_no"),

      (assign, ":leader_player", -1),
      (get_max_players, ":num_players"),
      (assign, ":end_cond", ":num_players"),
      (try_for_range, ":cur_player", 0, ":end_cond"), #try players till we find one, server gets first pick
        (player_is_active, ":cur_player"),
        (player_get_team_no, ":player_team", ":cur_player"),
        (eq, ":team_no", ":player_team"),
        (player_get_agent_id, ":player_agent", ":cur_player"),
        (ge, ":player_agent", 0),
        (agent_is_alive, ":player_agent"),
        (agent_get_slot, ":player_party_no",":player_agent", slot_agent_coop_spawn_party),# coop party

        (try_begin),#check if players party is garrison commander party
          (eq, ":agent_party_no", "$coop_garrison_party"), #if bot is part of garrison
          (eq, ":player_party_no", "$coop_garrison_commander_party"), #and player is commander of garrison
          (assign, ":player_party_no", ":agent_party_no"), #then player is also part of garrison party
        (try_end),
        (eq, ":agent_party_no", ":player_party_no"), #remove this if hero should command troops in other parties
        (try_begin),
          (eq, ":agent_class", grc_infantry),
          (player_get_slot, ":type_2_wanted", ":cur_player", slot_player_bot_type_2_wanted),
          (eq, ":type_2_wanted", 1), #player wants type 2
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (else_try),
          (eq, ":agent_class", grc_archers),
          (player_get_slot, ":type_3_wanted", ":cur_player", slot_player_bot_type_3_wanted),
          (eq, ":type_3_wanted", 1), #player wants type 3
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0), 
        (else_try),
          (eq, ":agent_class", grc_cavalry),
          (player_get_slot, ":type_4_wanted", ":cur_player", slot_player_bot_type_4_wanted),
          (eq, ":type_4_wanted", 1), #player wants type 4
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (else_try),

          (eq, ":agent_party_no", "$coop_main_party_spawn"), #if agent is from main party
          (try_begin),
            (eq, ":troop_class", 0),
            (player_get_slot, ":class_0_wanted", ":cur_player", slot_player_coop_class_0_wanted),
            (eq, ":class_0_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 1),
            (player_get_slot, ":class_1_wanted", ":cur_player", slot_player_coop_class_1_wanted),
            (eq, ":class_1_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 2),
            (player_get_slot, ":class_2_wanted", ":cur_player", slot_player_coop_class_2_wanted),
            (eq, ":class_2_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 3),
            (player_get_slot, ":class_3_wanted", ":cur_player", slot_player_coop_class_3_wanted),
            (eq, ":class_3_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 4),
            (player_get_slot, ":class_4_wanted", ":cur_player", slot_player_coop_class_4_wanted),
            (eq, ":class_4_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 5),
            (player_get_slot, ":class_5_wanted", ":cur_player", slot_player_coop_class_5_wanted),
            (eq, ":class_5_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 6),
            (player_get_slot, ":class_6_wanted", ":cur_player", slot_player_coop_class_6_wanted),
            (eq, ":class_6_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 7),
            (player_get_slot, ":class_7_wanted", ":cur_player", slot_player_coop_class_7_wanted),
            (eq, ":class_7_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 8),
            (player_get_slot, ":class_8_wanted", ":cur_player", slot_player_coop_class_8_wanted),
            (eq, ":class_8_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (try_end),
        (try_end),
      (try_end),

  # if nobody wants agent check for someone who wants all in party
      (try_begin),
        (eq, ":leader_player", -1),
        (get_max_players, ":num_players"),
        (assign, ":end_cond", ":num_players"),
        (try_for_range, ":cur_player", 0, ":end_cond"), #try players till we find one, server gets first pick
          (player_is_active, ":cur_player"),
          (player_get_team_no, ":player_team", ":cur_player"),
          (eq, ":team_no", ":player_team"),
          (player_get_agent_id, ":player_agent", ":cur_player"),
          (ge, ":player_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_get_slot, ":player_party_no",":player_agent", slot_agent_coop_spawn_party),# coop party
          (try_begin),#check if players party is garrison commander party
            (eq, ":agent_party_no", "$coop_garrison_party"), #if bot is part of garrison
            (eq, ":player_party_no", "$coop_garrison_commander_party"), #and player is commander of garrison
            (assign, ":player_party_no", ":agent_party_no"), #then player is also part of garrison party
          (try_end),
          (eq, ":player_party_no",":agent_party_no"), #remove this if hero should command troops in other parties
          (this_or_next|eq, ":agent_group", -1),#not already commanded
          (eq, ":agent_group", ":cur_player"),#commanded by me
          (player_get_slot, ":type_1_wanted", ":cur_player", slot_player_bot_type_1_wanted),
          (eq, ":type_1_wanted", 1), #player wants type 1
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (try_end),
      (try_end),
      (agent_set_group, ":agent_no", ":leader_player"),

    # (assign, reg13, ":agent_no"), 
    # (str_store_troop_name, s40, ":agent_troop"),
    # (assign, reg10, ":leader_player"), 
    # (assign, reg11, ":team_no"), 
    # (display_message, "@{reg11} leader {reg10} agent{reg13}   {s40}"),


      ]),


#
  # script_coop_find_bot_troop_for_spawn
  # Input: arg1 = team_no
  # Output: reg0 = troop_id, reg1 = group_id
  ("coop_find_bot_troop_for_spawn",
    [
      (store_script_param, ":team_no", 1),


      (assign, ":selected_troop", 0), #if no troop is found (error) spawn trp_player
      (try_begin),	  
        (eq, ":team_no", 0), #enemy team

        (assign, ":end", 40), 
        (try_for_range, ":unused", 0, ":end"),
          (party_stack_get_troop_id, ":selected_troop", "$coop_cur_temp_party_enemy", 0), #get one troop from each party per cycle

          (try_begin),
            (gt, ":selected_troop", 0), 
            (assign, ":party", "$coop_cur_temp_party_enemy"), 
            (party_remove_members, ":party", ":selected_troop", 1),	
            (store_sub, ":slot_pos", ":party", coop_temp_party_enemy_begin), 
            (troop_get_slot, "$coop_agent_banner", "trp_temp_array_a", ":slot_pos"),
            (assign, "$coop_agent_party", ":party"),
            (assign, ":end", 0), 
          (try_end),
          (try_begin),
            (store_add, ":last_party", coop_temp_party_enemy_begin, "$coop_no_enemy_parties"), 
            (val_sub, ":last_party", 1), 
            (eq, "$coop_cur_temp_party_enemy", ":last_party"),
            (assign, "$coop_cur_temp_party_enemy", coop_temp_party_enemy_begin),
          (else_try),
            (val_add, "$coop_cur_temp_party_enemy", 1),
          (try_end),
        (try_end),


      (else_try),
	  	  (eq, ":team_no", 1), #player team + allies

        (assign, ":end", 40), 
        (try_for_range, ":unused", 0, ":end"),
          (party_stack_get_troop_id, ":selected_troop", "$coop_cur_temp_party_ally", 0), #get one troop from each party per cycle
          (try_begin),
            (gt, ":selected_troop", 0), 
            (assign, ":party", "$coop_cur_temp_party_ally"), 
            (party_remove_members, ":party", ":selected_troop", 1),	
            (store_sub, ":slot_pos", ":party", coop_temp_party_ally_begin), 
            (troop_get_slot, "$coop_agent_banner", "trp_temp_array_b", ":slot_pos"),
            (assign, "$coop_agent_party", ":party"),
            (assign, ":end", 0), 
          (try_end),
          (try_begin),
            (store_add, ":last_party", coop_temp_party_ally_begin, "$coop_no_ally_parties"), #= one more than total
            (val_sub, ":last_party", 1), 
            (eq, "$coop_cur_temp_party_ally", ":last_party"),
            (assign, "$coop_cur_temp_party_ally", coop_temp_party_ally_begin),
          (else_try),
            (val_add, "$coop_cur_temp_party_ally", 1),
          (try_end),
        (try_end),

      (try_end), 


      #send banner for troop
      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
        (player_is_active, ":player_no"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_banner, "$coop_agent_banner"),
      (try_end),
      (call_script, "script_coop_check_item_bug", ":selected_troop"), #ITEM BUG WORKAROUND

      #  debug
      # (assign, reg4, "$coop_agent_banner"), 
      # (str_store_troop_name, s41, ":selected_troop"),
      # (assign, reg6, ":party"), 
      # (display_message, "@spawn {s41} from party {reg6} banner {reg4}"),

      (assign, reg0, ":selected_troop"),
    ]),	


  
    # 
   # script_coop_server_on_agent_killed_or_wounded_common
  # Input: arg1 = dead_agent_no
  ("coop_server_on_agent_killed_or_wounded_common",
   [
    (store_script_param, ":dead_agent_no", 1),
    (store_script_param, ":killer_agent_no", 2),

    (try_begin),
      (ge, ":dead_agent_no", 0),
      (ge, ":killer_agent_no", 0),
      (agent_is_human, ":dead_agent_no"),
      #(agent_is_human, ":killer_agent_no"), #comment if horse can kill human?
      (agent_get_troop_id, ":killer_troop_id", ":killer_agent_no"),
      (agent_get_troop_id, ":dead_troop_id", ":dead_agent_no"),
      (agent_get_team, ":dead_agent_team", ":dead_agent_no"),

      #xp function = (x*x/10 + x*2 + 10)* 2
      (store_character_level,":dead_troop_level",":dead_troop_id"),
      (store_mul, ":xp_gain", ":dead_troop_level", ":dead_troop_level"), 
      (val_div, ":xp_gain", 10), 
      (val_add, ":xp_gain", ":dead_troop_level"),
      (val_add, ":xp_gain", ":dead_troop_level"),
      (val_add, ":xp_gain", 10),
      (val_mul, ":xp_gain", 2),

      #xp message
      (try_begin),
        (eq, ":killer_troop_id", "$coop_my_troop_no"),
        (troop_is_hero, ":killer_troop_id"),
        (eq, "$coop_toggle_messages", 0),
        (assign, reg1, ":xp_gain"), 
        (display_message, "@You got {reg1} experience.", 0x00a4d9a2), #Added colored_message to xp gain in Co-Op.
      (try_end), 

      (try_begin),
        (troop_is_hero, ":dead_troop_id"),
        (try_begin),
          (eq, ":dead_agent_team", 0),
          (party_remove_members, coop_temp_party_enemy_heroes, ":dead_troop_id", 1),	
        (else_try),
          (eq, ":dead_agent_team", 1),
          (party_remove_members, coop_temp_party_ally_heroes, ":dead_troop_id", 1),
        (try_end),
      (try_end),

#only server continue
      (multiplayer_is_server),
      (agent_get_slot, ":killer_agent_party",":killer_agent_no", slot_agent_coop_spawn_party), #slot_agent_coop_spawn_party = SP party
      (agent_get_slot, ":dead_agent_party",":dead_agent_no", slot_agent_coop_spawn_party), #slot_agent_coop_spawn_party = SP party

      (try_begin),
        (eq, ":dead_agent_team", 0),
        (store_sub, ":casualties_party", ":dead_agent_party", coop_temp_party_enemy_begin),
        (val_add, ":casualties_party", coop_temp_casualties_enemy_begin),
      (else_try),
        (eq, ":dead_agent_team", 1),
        (store_sub, ":casualties_party", ":dead_agent_party", coop_temp_party_ally_begin),
        (val_add, ":casualties_party", coop_temp_casualties_ally_begin),
      (try_end),

      (try_begin), #store xp earned from kill for regular troops (heros copy directly from troop stats)
        (eq, ":killer_agent_party", "$coop_main_party_spawn"),
        (neg|troop_is_hero,":killer_troop_id"),#only regular troops in main party
        (store_mul, ":xp_for_regulars", ":xp_gain", 71), #regular troops get 71% of heroes
        (val_div, ":xp_for_regulars", 100),
        (troop_get_slot, ":temp_xp", ":killer_troop_id", slot_troop_temp_slot),
        (store_add, ":new_xp", ":temp_xp", ":xp_for_regulars"),
        (troop_set_slot, ":killer_troop_id", slot_troop_temp_slot, ":new_xp"),
      (try_end), 

      (party_add_members, ":casualties_party", ":dead_troop_id", 1),
      (try_begin),
        (this_or_next|troop_is_hero,":dead_troop_id"),
        (agent_is_wounded, ":dead_agent_no"),
        (party_wound_members, ":casualties_party", ":dead_troop_id", 1),
      (try_end),

      (try_begin), #save hit points for dead heroes (15% of pre battle health)
        (troop_is_hero, ":dead_troop_id"),   
        (store_troop_health, ":old_health", ":dead_troop_id"),
        (val_div, ":old_health", 6),
        (troop_set_health, ":dead_troop_id", ":old_health"),
      (try_end), 

#moved from multiplayer_server_on_agent_killed_or_wounded_common for this game type only
      (agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
      (try_begin),
        (ge, ":dead_player_no", 0),
        (player_is_active, ":dead_player_no"),
        (neg|agent_is_non_player, ":dead_agent_no"), #dead agent was player    
        (try_for_agents, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"), #agent is bot
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_group, ":agent_group", ":cur_agent"),
          (try_begin),
            (eq, ":dead_player_no", ":agent_group"),
            (agent_set_group, ":cur_agent", -1),                 
          (try_end),
        (try_end),
      (try_end),
    (try_end),  


#CLIENT CRASH BUG WORKAROUND BEGIN ################################################################
    (try_begin), #do this so client doesnt crash when rejoining, remove weapons from agent when his player quits
      (ge, ":dead_agent_no", 0),
      (lt, ":killer_agent_no", 0),
      (agent_is_human, ":dead_agent_no"),
      (position_move_y, pos0, 0),
      (position_move_x, pos0, 0),
      (agent_set_position, ":dead_agent_no", pos0),

      (try_for_range, ":slot", 0, 8),
        (agent_get_item_slot, ":cur_item", ":dead_agent_no", ":slot"), 
        (ge, ":cur_item", 0),
        (agent_unequip_item,":dead_agent_no",":cur_item"),
      (try_end),
      (remove_agent, ":dead_agent_no"),
      (agent_fade_out, ":dead_agent_no"),
    (try_end), 
#CLIENT CRASH BUG WORKAROUND END ################################################################
   ]),	

  # 
  # script_coop_sort_party
  # copies heroes first then troops to p_temp_party, and copies back to original party
  # Input: arg1 = dead_agent_no
  ("coop_sort_party",
   [
    (store_script_param, ":var_6", 1),
 

        (party_clear, "p_temp_party"), 
        (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
        (try_for_range, ":stack", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable",":var_6",":stack"),	
	        (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", ":var_6", ":stack"),
          (party_add_members, "p_temp_party", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
        (try_end),

        (try_for_range, ":stack", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", ":stack"),	
	        (neg|troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", ":var_6", ":stack"),
          (party_add_members, "p_temp_party", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
        (try_end),


		    (party_clear, ":var_6"), 
        (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", "p_temp_party"),
        (try_for_range, ":stack", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", "p_temp_party", ":stack"),	
          (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", "p_temp_party", ":stack"),
          (party_add_members, ":var_6", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
        (try_end),

   ]),	

   #####PROBABLY BUGGY
#    # 
# # script_coop_sort_party
# # copies heroes first then troops to p_temp_party, and copies back to original party
# # Input: arg1 = dead_agent_no
# ("coop_sort_party",
#  [
#   (store_script_param, ":var_6", 1),
#
#
#       (party_clear, "p_temp_party"), 
#       (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
#       (try_for_range, ":localvariable", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
#         (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable",":var_6",":localvariable"),	
#	        (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
#         (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", ":var_6", ":localvariable"),
#         (party_add_members, "p_temp_party", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
#       (try_end),
#
#       (try_for_range, ":localvariable", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
#         (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", ":localvariable"),	
#	        (neg|troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
#         (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", ":var_6", ":localvariable"),
#         (party_add_members, "p_temp_party", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
#       (try_end),
#
#
#		    (party_clear, ":var_6"), 
#       (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", "p_temp_party"),
#       (try_for_range, ":localvariable", 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
#         (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", "p_temp_party", ":localvariable"),	
#         (party_stack_get_size, ":party_prisoner_stack_size_var_6_var_9", "p_temp_party", ":localvariable"),
#         (party_add_members, ":var_6", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"),
#       (try_end),
#
#  ]),	
   


###### DATA SCRIPTS ##########################################################################################################

   # 
  # used to copy parties from SP to registers and temp casualty parties from MP to registers 
  # script_coop_copy_parties_to_file_sp
  # Input: arg1 = party_no
  ("coop_copy_parties_to_file_sp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
        (dict_create, "$coop_dict"),
        (dict_save, "$coop_dict", "@coop_battle"), #clear battle file

        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_setup_sp),

        (call_script, "script_coop_copy_settings_to_file"),	#copy game settings here

#SP ONLY MISC DATA

      #store scene
      (assign, ":scene_to_use", 0),
      (assign, ":scene_castle", 0),
      (assign, ":scene_street", 0),
      (assign, ":scene_party", 0),
      (assign, ":encountered_party", "$g_encountered_party"),
      (try_begin),
        (this_or_next|eq, "$coop_battle_type", coop_battle_type_siege_player_defend),
        (eq, "$coop_battle_type", coop_battle_type_siege_player_attack),
        (try_begin),
          (party_slot_eq, ":encountered_party", slot_party_type, spt_town),
          (party_get_slot, ":scene_to_use", ":encountered_party", slot_town_walls),
          (party_get_slot, ":scene_castle", ":encountered_party", slot_town_castle),
          (party_get_slot, ":scene_street", ":encountered_party", slot_town_center),
          (assign, ":scene_party", ":encountered_party"),
        (else_try),
          (party_slot_eq, ":encountered_party", slot_party_type, spt_castle),
          (party_get_slot, ":scene_to_use", ":encountered_party", slot_castle_exterior),
          (party_get_slot, ":scene_castle", ":encountered_party", slot_town_castle),
          (assign, ":scene_party", ":encountered_party"),
        (try_end),

      (else_try),
        (this_or_next|eq, "$coop_battle_type", coop_battle_type_village_player_attack),
        (eq, "$coop_battle_type", coop_battle_type_village_player_defend),
        (try_begin),
          (party_slot_eq, ":encountered_party", slot_party_type, spt_village),
          (party_get_slot, ":scene_to_use", ":encountered_party", slot_castle_exterior),
          (assign, ":scene_party", ":encountered_party"),
        (else_try),
          (assign, ":encountered_party", "$g_encounter_is_in_village"),
          (party_get_slot, ":scene_to_use", ":encountered_party", slot_castle_exterior),
          (assign, ":scene_party", ":encountered_party"),
        (try_end),

      (else_try),
        (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
        (party_slot_eq, ":encountered_party", slot_party_type, spt_bandit_lair),
        (party_stack_get_troop_id, ":bandit_type", "$g_encountered_party", 0),
        (try_begin),
          (eq, ":bandit_type", "trp_desert_bandit"),
          (assign, ":scene_to_use", "scn_lair_desert_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_mountain_bandit"),
          (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_forest_bandit"),
          (assign, ":scene_to_use", "scn_lair_forest_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_taiga_bandit"),
          (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_steppe_bandit"),
          (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_sea_raider"),
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (try_end),

      (else_try),
	  #ASSIGN VARIABLES
	  			
				
		# if field battle or we did not find one
		(party_get_current_terrain, ":terrain_type", "p_main_party"),
		#(assign, ":scene_to_use", "scn_coop_random_med_plain"), # Safeguard for none-existant scene (Sea, etc)
	    #(store_random_in_range, ":offset", 0, 12), # Actual index of the random scene (returns 0-11) (0 Counts as well) so count from 0 and up, which means 4 is 5 if you are counting from 1.
		#(assign, ":scene_to_use_large", "scn_1257_combat_swamp_0"), # Safeguard for sea battles etc does not require terrain type.
		#(val_add, ":scene_to_use_large", ":offset"), 
		###BEGIN SEA SCENES
		(store_random_in_range, ":offset", 0, 7), # Actual index of the random scene (returns 0-11) (0 Counts as well) so count from 0 and up, which means 4 is 5 if you are counting from 1.
		(assign, ":scene_to_use_large", "scn_scene_sea"), # Safeguard for sea battles etc does not require terrain type.
		(val_add, ":scene_to_use_large", ":offset"), 
		###END SEA SCENES
		
		    (store_random_in_range, ":offset", 0, 7), # Changed from 0, 3 to 0,7 to add Nile.
		    (try_begin),
			(eq, ":terrain_type", rt_desert),
		    #(assign, ":scene_to_use", "scn_1257_combat_rocky_desert_0"),
			(assign, ":scene_to_use_large", "scn_1257_combat_rocky_desert_0"),
			(val_add, ":scene_to_use_large", ":offset"), 
			(else_try),
			
			#Add scenes using 
			#(store_random_in_range, ":offset", 0, 3), # Actual index of the random scene (returns 0-9) (0 Counts as well)
			#Then finally
			#(val_add, ":scene_to_use_large", ":offset"), 
			#After (assign, ":scene_to_use_large", "scn_1257_combat_rocky_desert_0 "),
			#Add multiple scenes by  editing  
			# 		(assign, ":scene_to_use_large)", "scn_coop_random_lrg_plain"), # Safeguard
		    #           (store_random_in_range, ":offsetsnow", 0, 10), # Actual index of the random scene (returns 0-9) (0 Counts as well)
			#       (val_add, ":scene_to_use_large", ":offset"),
			# If you got 9 scenes, then use 0, 10 if you got 6 scenes then use 0, 7 always one number is spare.

           (store_random_in_range, ":offset", 0, 16), # Actual index of the random scene (returns 0-9) (0 Counts as well)
			(eq, ":terrain_type", rt_steppe),
			#(assign, ":scene_to_use", "scn_coop_random_lrg_steppe"),
			(assign, ":scene_to_use_large", "scn_random_scene_steppe"),
					(val_add, ":scene_to_use_large", ":offset"), 
			# ... "And on and on and on..." -- Blind Guardian, "Precious Jerusalem"
			# In other words, repeat these for all terrain types you've got covered.
		# READY SET GO
		(else_try),
		(store_random_in_range, ":offset", 0, 18), # Actual index of the random scene (returns 0-9) (0 Counts as well)
			(eq, ":terrain_type", rt_plain),
			#(assign, ":scene_to_use", "scn_1257_combat_euro_0"),
			(assign, ":scene_to_use_large", "scn_random_scene_plain"),
			(val_add, ":scene_to_use_large", ":offset"), 
		(else_try),
				(store_random_in_range, ":offset", 0, 12), # Actual index of the random scene (returns 0-9) (0 Counts as well)
			(eq, ":terrain_type", rt_snow),
			#(assign, ":scene_to_use", "scn_coop_random_med_snow"),
			(assign, ":scene_to_use_large", "scn_random_scene_snow"),
			(val_add, ":scene_to_use_large", ":offset"), 
        (else_try),
						(store_random_in_range, ":offset", 0, 16), # Actual index of the random scene (returns 0-9) (0 Counts as well)
          (eq, ":terrain_type", rt_steppe_forest),
         # (assign, ":scene_to_use", "scn_coop_random_med_steppe_forest"),
          (assign, ":scene_to_use_large", "scn_random_scene_steppe"),
		  (val_add, ":scene_to_use_large", ":offset"), 
        (else_try),
						(store_random_in_range, ":offset", 0, 13), # Actual index of the random scene (returns 0-9) (0 Counts as well)
          (eq, ":terrain_type", rt_forest),
        #  (assign, ":scene_to_use", "scn_coop_random_med_plain_forest"),
          (assign, ":scene_to_use_large", "scn_random_scene_plain_forest"),
		  (val_add, ":scene_to_use_large", ":offset"), 
        (else_try),
						(store_random_in_range, ":offset", 0, 12), # Actual index of the random scene (returns 0-9) (0 Counts as well)
          (eq, ":terrain_type", rt_snow_forest),
        #  (assign, ":scene_to_use", "scn_coop_random_med_snow_forest"),
          (assign, ":scene_to_use_large", "scn_random_scene_snow"),
		  (val_add, ":scene_to_use_large", ":offset"), 
        (else_try),
						(store_random_in_range, ":offset", 0, 7), # Edited from 0, 3 to add Nile.
          (eq, ":terrain_type", rt_desert_forest),
        #  (assign, ":scene_to_use", "scn_coop_random_med_desert_forest"),
          (assign, ":scene_to_use_large", "scn_1257_combat_rocky_desert_0"),
		  (val_add, ":scene_to_use_large", ":offset"), 
		  #V1.000 Added
        (else_try),
          (eq, ":terrain_type", rt_water),
          (assign, ":scene_to_use", "scn_water"),
		            (assign, ":scene_to_use_large", "scn_water"),
		  		  	(else_try),
				
          (eq, ":terrain_type", rt_bridge),
          (assign, ":scene_to_use", "scn_scene_sea"),
		  (assign, ":scene_to_use_large", "scn_scene_sea"),
		  #	(else_try),
		 #(eq, ":current_terrain_main_party", 7), #try to add sea battles
		#	(assign, ":value", "scn_scene_sea"),
		#End V1.000
		  		(try_end),



        (try_begin),
          (store_add, ":total_fit_for_battle", "$g_enemy_fit_for_battle", "$g_friend_fit_for_battle"), #get number of troops for large or medium scene size
          #(gt, ":total_fit_for_battle", 80),
		  (gt, ":total_fit_for_battle", 2),
          (assign, ":scene_to_use", ":scene_to_use_large"), #switch to larger scene 
        (try_end),
      (try_end),

      (dict_set_int, "$coop_dict", "@map_type", "$coop_battle_type"),
      (dict_set_int, "$coop_dict", "@map_scn", ":scene_to_use"),
      (dict_set_int, "$coop_dict", "@map_castle", ":scene_castle"),
      (dict_set_int, "$coop_dict", "@map_street", ":scene_street"),
      (dict_set_int, "$coop_dict", "@map_party_id", ":scene_party"),


      #find which party is castle garrison and which party is commander of garrison
      (dict_set_int, "$coop_dict", "@p_castle_lord", -1), #store null (0 could be a valid number for this variable)
      (assign, ":garrison_lord_party", -1),
      (try_begin), 
        (this_or_next|party_slot_eq, ":encountered_party", slot_party_type, spt_village),
        (this_or_next|party_slot_eq, ":encountered_party", slot_party_type, spt_town),
        (party_slot_eq, ":encountered_party", slot_party_type, spt_castle),
        (party_get_slot, ":cur_leader", ":encountered_party", slot_town_lord),
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":troop_leaded_party", ":cur_leader", slot_troop_leaded_party),
        (ge, ":troop_leaded_party", 0),
        (assign, ":garrison_lord_party", ":troop_leaded_party"),
      (try_end),


      #decide weather
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (try_begin),
        (this_or_next|eq, ":terrain_type", rt_plain),
        (this_or_next|eq, ":terrain_type", rt_steppe_forest),
        (this_or_next|eq, ":terrain_type", rt_forest),
        (this_or_next|eq, ":terrain_type", rt_water),
        (this_or_next|eq, ":terrain_type", rt_bridge),
        (eq, ":terrain_type", rt_steppe),

        (assign, ":rain", 1),
      (else_try),
        (this_or_next|eq, ":terrain_type", rt_snow_forest),
        (eq, ":terrain_type", rt_snow),

        (assign, ":rain", 2),
      (else_try),        
        (this_or_next|eq, ":terrain_type", rt_desert_forest),
        (eq, ":terrain_type", rt_desert),

        (assign, ":rain", 0),
      (try_end),

      (store_time_of_day, ":time"),
	    (get_global_cloud_amount, ":cloud"),
	    (get_global_haze_amount, ":haze"),
      (dict_set_int, "$coop_dict", "@map_time", ":time"),
      (dict_set_int, "$coop_dict", "@map_cloud", ":cloud"),
      (dict_set_int, "$coop_dict", "@map_haze", ":haze"),
      (dict_set_int, "$coop_dict", "@map_rain", ":rain"),



      (call_script, "script_calculate_battle_advantage"),
           # (val_mul, reg0, 2),
           # (val_div, reg0, 3), #scale down the advantage a bit in sieges.
      (dict_set_int, "$coop_dict", "@battle_adv", reg0),



      #store faction of parties
      (store_faction_of_party, ":team_faction", "$coop_encountered_party"),
      (dict_set_int, "$coop_dict", "@tm0_fac", ":team_faction"),


      (try_begin),
        (gt, "$g_ally_party", 0),
        (store_faction_of_party, ":team_faction", "$g_ally_party"),
      (else_try),
        (gt, "$players_kingdom", 0),
        (assign, ":team_faction", "$players_kingdom"),
      (else_try),
        (assign, ":team_faction", "fac_player_faction"),
      (try_end),
      (dict_set_int, "$coop_dict", "@tm1_fac", ":team_faction"),

      (str_store_faction_name, s0, "$players_kingdom"),
      (dict_set_str, "$coop_dict", "@tm1_name", s0),

      (try_for_range, reg1, 0, 9),
        (str_store_class_name, s0, reg1), #(str_store_class_name,<string_register>,<class_id>)
        (dict_set_str, "$coop_dict", "@cls{reg1}_name", s0),
      (try_end),


##COPY PARTIES TO REG##


#ADD ENEMY PARTIES

    (assign, reg22, 0), #count heroes

    (party_get_num_attached_parties, ":no_enemy_parties", "$coop_encountered_party"),
    (val_add, ":no_enemy_parties", 1), 
    (dict_set_int, "$coop_dict", "@num_parties_enemy", ":no_enemy_parties"),

    (try_for_range, reg20, 0, ":no_enemy_parties"),
      (try_begin),
        (eq, reg20, 0),#first party
        (assign, ":var_6", "$coop_encountered_party"),
      (else_try),
        (store_sub, ":attached_party_rank", reg20, 1), #sub 1 so rank starts from 0
        (party_get_attached_party_with_rank, ":var_6", "$coop_encountered_party", ":attached_party_rank"),
      (try_end),

      (assign, ":banner_spr", 0), 
	  	    (store_random_in_range, ":offset", 0, 520), # Actual index of the random scene (returns 0-11) (0 Counts as well) so count from 0 and up, which means 4 is 5 if you are counting from 1.
		(assign, ":banner_mesh", "mesh_banner_a01"), # Safeguard for sea battles etc does not require terrain type.
		(val_add, ":banner_mesh", ":offset"), 
      (try_begin),
        (this_or_next|party_slot_eq, ":var_6", slot_party_type, spt_village),
        (this_or_next|party_slot_eq, ":var_6", slot_party_type, spt_town),
        (party_slot_eq, ":var_6", slot_party_type, spt_castle),
        (dict_set_int, "$coop_dict", "@p_garrison", reg20), #store rank of garrison party
        (party_get_slot, ":cur_leader", ":var_6", slot_town_lord), #can't store index of leader party here because we don't know it yet
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":banner_spr", ":cur_leader", slot_troop_banner_scene_prop),
        (dict_set_int, "$coop_dict", "@p_garrison_banner", ":banner_spr"),
      (else_try),
        (party_stack_get_troop_id, ":leader_troop", ":var_6", 0),
        (troop_slot_eq, ":leader_troop", slot_troop_occupation, 2),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
      (try_end),
      (try_begin),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),	
      (try_end),
      (try_begin), #store which party is garrison commander
        (eq, ":var_6", ":garrison_lord_party"),
        (dict_set_int, "$coop_dict", "@p_castle_lord", reg20), #store INDEX of garrison party (not party id)
      (try_end),
	
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_banner", ":banner_mesh"),
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_partyid", ":var_6"),


      (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_numstacks", ":num_prisoner_stacks_script_param_1_leaded_party_2"),

      (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", reg21),
        (party_stack_get_size, ":total_stack_size", ":var_6", reg21),
        (party_stack_get_num_wounded, ":num_wounded",":var_6", reg21),

        (try_begin),
          (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (store_troop_health, ":hero_health", ":party_stack_troop_id_temp_party_localvariable"),
          (le, ":hero_health", 15),
          (assign, ":num_wounded", 1),  
        (try_end),
        (store_sub, ":party_prisoner_stack_size_var_6_var_9", ":total_stack_size", ":num_wounded"), 
        (ge, ":party_prisoner_stack_size_var_6_var_9",1), #if alive
        (try_begin),
          (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (dict_set_int, "$coop_dict", "@hero_{reg22}_trp", ":party_stack_troop_id_temp_party_localvariable"),
          (val_add, reg22, 1), 
        (try_end),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_trp", ":party_stack_troop_id_temp_party_localvariable"),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_num", ":party_prisoner_stack_size_var_6_var_9"),
      (try_end),
    (try_end),



#ADD ALLY PARTIES
      (assign, ":no_ally_parties", 1), # start from 1 because main party
      (try_begin),
        (gt, "$g_ally_party", 0), #if allies are attached to ally party
        (assign, ":ally_party", "$g_ally_party"),
        (assign, ":rank_start", 2),
        (val_add, ":no_ally_parties", 1), #add one for ally
      (else_try),
        (assign, ":rank_start", 1),
        (assign, ":ally_party", "p_main_party"), #if allies are attached to us
      (try_end),

    (party_get_num_attached_parties, ":num_attached_parties", ":ally_party"),
    (val_add, ":no_ally_parties", ":num_attached_parties"), 
    (dict_set_int, "$coop_dict", "@num_parties_ally", ":no_ally_parties"),

    (try_for_range, reg20, 0, ":no_ally_parties"),
      (try_begin),
        (eq, reg20, 0),#first party
        (assign, ":var_6", "p_main_party"),
      (else_try),
        (gt, "$g_ally_party", 0),
        (eq, reg20, 1),#second party
        (assign, ":var_6", "$g_ally_party"),
      (else_try),
        (store_sub, ":attached_party_rank", reg20, ":rank_start"), #sub 1 or 2 so rank starts from 0
        (party_get_attached_party_with_rank, ":var_6", ":ally_party", ":attached_party_rank"),
      (try_end),

      (assign, ":banner_spr", 0), 
	  	    (store_random_in_range, ":offset", 0, 520), # Actual index of the random scene (returns 0-11) (0 Counts as well) so count from 0 and up, which means 4 is 5 if you are counting from 1.
		(assign, ":banner_mesh", "mesh_banner_a01"), # Safeguard for sea battles etc does not require terrain type.
		(val_add, ":banner_mesh", ":offset"), 
      (try_begin),
        (eq, ":var_6", "p_main_party"),
	  	    (store_random_in_range, ":offset", 0, 520), # Actual index of the random scene (returns 0-11) (0 Counts as well) so count from 0 and up, which means 4 is 5 if you are counting from 1.
		(assign, ":banner_mesh", "mesh_banner_a01"), # Safeguard for sea battles etc does not require terrain type.
		(val_add, ":banner_mesh", ":offset"), 
      (try_end),
      (try_begin),
        (this_or_next|party_slot_eq, ":var_6", slot_party_type, spt_village),
        (this_or_next|party_slot_eq, ":var_6", slot_party_type, spt_town),
        (party_slot_eq, ":var_6", slot_party_type, spt_castle),
        (dict_set_int, "$coop_dict", "@p_garrison", reg20), #store rank of garrison party
        (party_get_slot, ":cur_leader", ":var_6", slot_town_lord), #can't store index of leader party here because we don't know it yet
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":banner_spr", ":cur_leader", slot_troop_banner_scene_prop),
        (dict_set_int, "$coop_dict", "@p_garrison_banner", ":banner_spr"),
      (else_try),
        (party_stack_get_troop_id, ":leader_troop", ":var_6", 0),
        (troop_is_hero, ":leader_troop"),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
      (try_end),
      (try_begin),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),	
      (try_end),

      (try_begin), #store which party is garrison commander
        (eq, ":var_6", ":garrison_lord_party"),
        (dict_set_int, "$coop_dict", "@p_castle_lord", reg20),  #store INDEX of garrison party (not party id)
      (try_end),
	
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_banner", ":banner_mesh"),
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_partyid", ":var_6"), #store party id for SP



      (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_numstacks", ":num_prisoner_stacks_script_param_1_leaded_party_2"),
      (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", reg21),
        (party_stack_get_size, ":total_stack_size", ":var_6", reg21),
        (party_stack_get_num_wounded, ":num_wounded",":var_6", reg21),
        (try_begin),
          (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (store_troop_health, ":hero_health", ":party_stack_troop_id_temp_party_localvariable"),
          (le, ":hero_health", 15),
          (assign, ":num_wounded", 1),  
        (try_end),
        (store_sub, ":party_prisoner_stack_size_var_6_var_9", ":total_stack_size", ":num_wounded"), 
        (ge, ":party_prisoner_stack_size_var_6_var_9",1), #if alive

        (try_begin), #if storing main party
          (eq, ":var_6", "p_main_party"),
          (troop_get_class, ":troop_class", ":party_stack_troop_id_temp_party_localvariable"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_cls", ":troop_class"),
          (eq, ":party_stack_troop_id_temp_party_localvariable", "trp_player"), 
          (troop_get_type, ":type_script_param_1", "trp_player"),
          (try_begin),
            (eq, ":type_script_param_1", 1),
            (assign, ":party_stack_troop_id_temp_party_localvariable",  "trp_multiplayer_profile_troop_female"),  
          (else_try),
            (assign, ":party_stack_troop_id_temp_party_localvariable",  "trp_multiplayer_profile_troop_male"),  
          (try_end),
        (try_end),

        (try_begin),
          (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
          (dict_set_int, "$coop_dict", "@hero_{reg22}_trp", ":party_stack_troop_id_temp_party_localvariable"),
          (val_add, reg22, 1), 
        (try_end),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_trp", ":party_stack_troop_id_temp_party_localvariable"),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_num", ":party_prisoner_stack_size_var_6_var_9"),
      (try_end),
    (try_end),

    (dict_set_int, "$coop_dict", "@hero_num", reg22),

    (call_script, "script_coop_copy_hero_to_file"), 



    (dict_save, "$coop_dict", "@coop_battle"), #save new data
    (dict_free, "$coop_dict"),
    (display_message, "@Battle setup complete.", 0x00a2d9ce),
	(display_message, "@You may now click on Multiplayer in the Main Menu > Host Game > Start Map if things look right.", 0x00a2d9ce),
	(display_message, "@If you are using a Dedicated Server you can upload the data from the WSE Folder at My Documents > Mount&Blade Warband/WSE/Medieval_Conquests then load it from the Dedicated Server Administrator Panel, you can upload the file using FTP or PHP Scripts, you would also need to adjust wse_settings.txt path to aim for the .dict files.", 0x00a2d9ce), #0x00 is always necessary before color.
    (try_end),

    ]),	
##B


##E
  # 
   #script_coop_copy_file_to_parties_mp
  # Input: arg1 = party_no
  ("coop_copy_file_to_parties_mp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),

      (dict_get_int, "$coop_no_enemy_parties", "$coop_dict", "@num_parties_enemy"),
      (dict_get_int, "$coop_no_ally_parties", "$coop_dict", "@num_parties_ally"),

  #BOTH MODES
      (call_script, "script_coop_copy_file_to_settings"),	#copy game settings here
      (call_script, "script_coop_copy_file_to_hero"),

  #CLEAR casualty parties
      (try_for_range, ":party_rank", 0, "$coop_no_enemy_parties"),
        (store_add, ":var_6", ":party_rank", coop_temp_casualties_enemy_begin), 
        (party_clear, ":var_6"),
      (try_end),
      (try_for_range, ":party_rank", 0, "$coop_no_ally_parties"),
        (store_add, ":var_6", ":party_rank", coop_temp_casualties_ally_begin), 
        (party_clear, ":var_6"),
      (try_end),

  #ADD TROOPS TO TEMP SPAWN PARTIES 
  #ENEMY TEAM
      (assign, ":total_enemy_troops", 0),
      # (assign, ":cur_slot", 101),
        (party_clear, coop_temp_party_enemy_heroes),
      (try_for_range, reg20, 0, "$coop_no_enemy_parties"), #number of enemy parties
        (dict_get_int, ":num_prisoner_stacks_script_param_1_leaded_party_2", "$coop_dict", "@p_enemy{reg20}_numstacks"),
        (dict_get_int, ":banner_mesh", "$coop_dict", "@p_enemy{reg20}_banner"),
        (troop_set_slot, "trp_temp_array_a", reg20, ":banner_mesh"),#encountered party banner
        (store_add, ":var_6", reg20, coop_temp_party_enemy_begin), 
        (party_clear, ":var_6"),
        (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_enemy{reg20}_{reg21}_trp"),
          (dict_get_int, ":party_prisoner_stack_size_var_6_var_9", "$coop_dict", "@p_enemy{reg20}_{reg21}_num"),
          (party_add_members, ":var_6", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"), #when copy to MP wounded troops have already been removed
          (val_add, ":total_enemy_troops", ":party_prisoner_stack_size_var_6_var_9"),

          (try_begin),
            (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
            (eq, ":party_prisoner_stack_size_var_6_var_9",1), #if alive
            (party_add_members, coop_temp_party_enemy_heroes, ":party_stack_troop_id_temp_party_localvariable", 1),
          (try_end),
        (try_end),
      (try_end), #end enemy parties
      # (troop_set_slot, "trp_temp_array_a", 100, ":cur_slot"),# slot 100 = 100 + number heroes + 1
      (assign, "$coop_num_bots_team_1", ":total_enemy_troops"), #count troops in battle




  #PLAYER TEAM  
      (assign, ":total_ally_troops", 0),
      # (assign, ":cur_slot", 101),
        (party_clear, coop_temp_party_ally_heroes),


      (try_for_range, reg20, 0, "$coop_no_ally_parties"), 
        (dict_get_int, ":num_prisoner_stacks_script_param_1_leaded_party_2", "$coop_dict", "@p_ally{reg20}_numstacks"),
        (dict_get_int, ":banner_mesh", "$coop_dict", "@p_ally{reg20}_banner"),
        (troop_set_slot, "trp_temp_array_b", reg20, ":banner_mesh"),#encountered party banner
        (store_add, ":var_6", reg20, coop_temp_party_ally_begin),
        (party_clear, ":var_6"),
        (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_ally{reg20}_{reg21}_trp"),
          (dict_get_int, ":party_prisoner_stack_size_var_6_var_9", "$coop_dict", "@p_ally{reg20}_{reg21}_num"),
          (party_add_members, ":var_6", ":party_stack_troop_id_temp_party_localvariable", ":party_prisoner_stack_size_var_6_var_9"), #when copy to MP wounded troops have already been removed
          (val_add, ":total_ally_troops", ":party_prisoner_stack_size_var_6_var_9"),
          (try_begin),
            (eq, reg20, 0), #main party
            (dict_get_int, ":troop_class", "$coop_dict", "@p_ally0_{reg21}_cls"),
            (troop_set_slot, ":party_stack_troop_id_temp_party_localvariable", slot_troop_current_rumor, ":troop_class"), #store main party troop class in this slot
          (try_end),
          (try_begin),
            (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
            (eq, ":party_prisoner_stack_size_var_6_var_9",1), #if alive
            (party_add_members, coop_temp_party_ally_heroes, ":party_stack_troop_id_temp_party_localvariable", 1),
          (try_end),

        (try_end),
      (try_end), #end ally parties
      # (troop_set_slot, "trp_temp_array_b", 100, ":cur_slot"),# slot 100 = 100 + number heroes + 1
      (assign, "$coop_num_bots_team_2", ":total_ally_troops"), #count troops in battle

    (try_end),

      ]),




  # 
   #script_coop_copy_parties_to_file_mp
  # Input: arg1 = party_no
  ("coop_copy_parties_to_file_mp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_create, "$coop_dict"),
      (dict_load_file, "$coop_dict", "@coop_battle", 2),

        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_end_mp),

        (call_script, "script_coop_copy_settings_to_file"),	

#At end of MP battle:

      #copy health from ALIVE agents to hero troops here before copying to registers (dead agents health is copied at coop_server_on_agent_killed_or_wounded_common)
      (try_for_agents, ":cur_agent"),
        (agent_is_human, ":cur_agent"),  
        (agent_is_alive, ":cur_agent"),
        (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
        (troop_is_hero, ":agent_troop_id"),   
        (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
        (troop_set_health, ":agent_troop_id", ":agent_hit_points"),

        # store items from agents
        (call_script, "script_coop_player_agent_save_items", ":cur_agent"),
      (try_end),

      (try_begin), 
        (eq, "$coop_winner_team", 0),#0 = enemy won
        (dict_set_int, "$coop_dict", "@battle_result", -1), # = battle_result
      (else_try),
        (eq, "$coop_winner_team", 1), #1 = player won
        (dict_set_int, "$coop_dict", "@battle_result", 1),
      (else_try),
        (dict_set_int, "$coop_dict", "@battle_result", 0),
      (try_end),


#ENEMY TEAM
      (try_for_range, reg20, 0, "$coop_no_enemy_parties"),
        (store_add, ":var_6", reg20, coop_temp_casualties_enemy_begin), 
        (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_numstacks_cas", ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", reg21),
          (party_stack_get_size, ":total_stack_size", ":var_6", reg21),
          (party_stack_get_num_wounded, ":num_wounded",":var_6", reg21),
          (try_begin),
            (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
            (store_troop_health, ":hero_health", ":party_stack_troop_id_temp_party_localvariable"),
            (le, ":hero_health", 15),
            (assign, ":num_wounded", 1),  
          (try_end),
          (store_sub, ":dead_size", ":total_stack_size", ":num_wounded"), 
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_trp_cas", ":party_stack_troop_id_temp_party_localvariable"),
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_ded", ":dead_size"),
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_wnd", ":num_wounded"),
        (try_end),
      (try_end),




#ADD PARTIES ATTACHED TO MAIN PARTY
      (try_for_range, reg20, 0, "$coop_no_ally_parties"),
        (store_add, ":var_6", reg20, coop_temp_casualties_ally_begin), 
        (party_get_num_companion_stacks, ":num_prisoner_stacks_script_param_1_leaded_party_2", ":var_6"),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_numstacks_cas", ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
          (party_stack_get_troop_id, ":party_stack_troop_id_temp_party_localvariable", ":var_6", reg21),
          (party_stack_get_size, ":total_stack_size", ":var_6", reg21),
          (party_stack_get_num_wounded, ":num_wounded",":var_6", reg21),
          (try_begin),
            (troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
            (store_troop_health, ":hero_health", ":party_stack_troop_id_temp_party_localvariable"),
            (le, ":hero_health", 15),
            (assign, ":num_wounded", 1),  
          (try_end),
          (store_sub, ":dead_size", ":total_stack_size", ":num_wounded"), 
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_trp_cas", ":party_stack_troop_id_temp_party_localvariable"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_ded", ":dead_size"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_wnd", ":num_wounded"),
        (try_end),
      (try_end),



#store xp for regular troop stacks in main party
      (dict_get_int, ":num_prisoner_stacks_script_param_1_leaded_party_2", "$coop_dict", "@p_ally0_numstacks"), #num stacks from spawn party
      (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_ally0_{reg21}_trp"),
        (neg|troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
        (troop_get_slot, ":stack_xp", ":party_stack_troop_id_temp_party_localvariable", slot_troop_temp_slot),
        (dict_set_int, "$coop_dict", "@p_ally0_{reg21}_stk_xp", ":stack_xp"),
      (try_end),

      (call_script, "script_coop_copy_hero_to_file"), 

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"), 
        (player_is_active, ":player_no"),
        (player_is_admin, ":player_no"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_result_saved),
      (try_end),
      (assign, "$coop_battle_started", -1),

      (dict_save, "$coop_dict", "@coop_battle"),
      (dict_free, "$coop_dict"),
    (try_end),
    ]),	




  #
   #script_coop_copy_file_to_parties_sp
  # Input: arg1 = party_no
  ("coop_copy_file_to_parties_sp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
    (dict_create, "$coop_dict"),
    (dict_load_file, "$coop_dict", "@coop_battle", 2),

    (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_none),
    (dict_save, "$coop_dict", "@coop_battle"),

    (dict_get_int, "$coop_no_enemy_parties", "$coop_dict", "@num_parties_enemy"),
    (dict_get_int, "$coop_no_ally_parties", "$coop_dict", "@num_parties_ally"),

#BOTH MODES
    (call_script, "script_coop_copy_file_to_settings"),	#copy game settings here before heroes
    (call_script, "script_coop_copy_file_to_hero"), #this sets hero health from battle

#create temp parties or wound parties
    (party_clear, "p_total_enemy_casualties"),
    (party_clear, "p_enemy_casualties"),

    (try_for_range, reg20, 0, "$coop_no_enemy_parties"), #number of enemy parties
      (dict_get_int, ":num_casualty_stacks", "$coop_dict", "@p_enemy{reg20}_numstacks_cas"),
      (dict_get_int, ":party_to_kill", "$coop_dict", "@p_enemy{reg20}_partyid"),

      (try_for_range, reg21, 0, ":num_casualty_stacks"),
        (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_enemy{reg20}_{reg21}_trp_cas"),
        (dict_get_int, ":stack_dead", "$coop_dict", "@p_enemy{reg20}_{reg21}_ded"),
        (dict_get_int, ":stack_wounded", "$coop_dict", "@p_enemy{reg20}_{reg21}_wnd"),

          (store_add, ":stack_total_casualties", ":stack_dead", ":stack_wounded"), 
          (try_begin),
            (troop_is_hero,":party_stack_troop_id_temp_party_localvariable"),
            (store_random_in_range, ":rand_wound", 40, 71),
            (store_troop_health, ":troop_hp",":party_stack_troop_id_temp_party_localvariable"),
            (val_sub, ":troop_hp", ":rand_wound"),
            (val_max, ":troop_hp", 1),
            (troop_set_health, ":party_stack_troop_id_temp_party_localvariable", ":troop_hp"),
          (else_try),
            (party_remove_members, ":party_to_kill", ":party_stack_troop_id_temp_party_localvariable", ":stack_dead"),#remove from parties
          (try_end),
          (party_wound_members, ":party_to_kill", ":party_stack_troop_id_temp_party_localvariable", ":stack_wounded"),
          (party_add_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_party_localvariable", ":stack_total_casualties"), #add casualties for loot
          (party_wound_members, "p_total_enemy_casualties", ":party_stack_troop_id_temp_party_localvariable", ":stack_wounded"),
          (party_add_members, "p_enemy_casualties", ":party_stack_troop_id_temp_party_localvariable", ":stack_total_casualties"), #add casualties for reports/morale
          (party_wound_members, "p_enemy_casualties", ":party_stack_troop_id_temp_party_localvariable", ":stack_wounded"),
      (try_end),
    (try_end), #end enemy parties




#PLAYER TEAM  

     #add regular troop xp BEFORE removing dead troops from party
      (dict_get_int, ":num_prisoner_stacks_script_param_1_leaded_party_2", "$coop_dict", "@p_ally0_numstacks"), #num stacks from spawn party
      (try_for_range, reg21, 0, ":num_prisoner_stacks_script_param_1_leaded_party_2"),
        (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_ally0_{reg21}_trp"),
        (neg|troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
        (dict_get_int, ":stack_xp", "$coop_dict", "@p_ally0_{reg21}_stk_xp"),
        (party_add_xp_to_stack, "p_main_party", reg21, ":stack_xp"),
      (try_end),

    (assign, "$any_allies_at_the_last_battle", 0),
    (party_clear, "p_player_casualties"),
    (party_clear, "p_ally_casualties"),
    (try_for_range, reg20, 0, "$coop_no_ally_parties"), 
      (dict_get_int, ":num_casualty_stacks", "$coop_dict", "@p_ally{reg20}_numstacks_cas"),
      (dict_get_int, ":party_to_kill", "$coop_dict", "@p_ally{reg20}_partyid"),

      (try_begin),
        (eq, ":party_to_kill", "p_main_party"),
        (assign, ":casualties_party", "p_player_casualties"),
        (party_get_skill_level, ":player_party_surgery", "p_main_party", "skl_surgery"),
        (val_mul, ":player_party_surgery", 4),    #4% per skill level
      (else_try),
        (assign, "$any_allies_at_the_last_battle", 1),
        (assign, ":casualties_party", "p_ally_casualties"),
      (try_end),

      (try_for_range, reg21, 0, ":num_casualty_stacks"),
        (dict_get_int, ":party_stack_troop_id_temp_party_localvariable", "$coop_dict", "@p_ally{reg20}_{reg21}_trp_cas"),
        (dict_get_int, ":stack_dead", "$coop_dict", "@p_ally{reg20}_{reg21}_ded"),
        (dict_get_int, ":stack_wounded", "$coop_dict", "@p_ally{reg20}_{reg21}_wnd"),
        (store_add, ":stack_total_casualties", ":stack_dead", ":stack_wounded"), 

        (try_begin), 
          (eq, ":party_to_kill", "p_main_party"),
          (try_begin),
            (this_or_next|eq, ":party_stack_troop_id_temp_party_localvariable",  "trp_multiplayer_profile_troop_female"),  
            (eq, ":party_stack_troop_id_temp_party_localvariable",  "trp_multiplayer_profile_troop_male"),  
            (assign, ":party_stack_troop_id_temp_party_localvariable", "trp_player"),
          (try_end),
          (try_begin),#use surgey to heal regular troops in stack
            (neg|troop_is_hero, ":party_stack_troop_id_temp_party_localvariable"),
            (assign, ":end", ":stack_dead"),
            (try_for_range, ":unused", 0, ":end"),#try each dead troop in stack
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", ":player_party_surgery"),
              (val_add, ":stack_wounded", 1),
              (val_sub, ":stack_dead", 1),
            (try_end),
          (try_end),
        (else_try), #ally party
          (troop_is_hero,":party_stack_troop_id_temp_party_localvariable"),#ally lord
          (store_random_in_range, ":rand_wound", 40, 71),
          (store_troop_health, ":troop_hp",":party_stack_troop_id_temp_party_localvariable"),
          (val_sub, ":troop_hp", ":rand_wound"),
          (val_max, ":troop_hp", 1),
          (troop_set_health, ":party_stack_troop_id_temp_party_localvariable", ":troop_hp"),
        (try_end),

        (party_wound_members, ":party_to_kill", ":party_stack_troop_id_temp_party_localvariable", ":stack_wounded"), #wound regular and heroes
        (try_begin),
          (neg|troop_is_hero,":party_stack_troop_id_temp_party_localvariable"),
          (party_remove_members, ":party_to_kill", ":party_stack_troop_id_temp_party_localvariable", ":stack_dead"), #kill regulars
        (try_end),

        #add dead and wounded for casualty report
        (party_add_members, ":casualties_party", ":party_stack_troop_id_temp_party_localvariable", ":stack_total_casualties"),#dead
        (party_wound_members, ":casualties_party", ":party_stack_troop_id_temp_party_localvariable", ":stack_wounded"),#wounded
      (try_end),
    (try_end),


#SP USE RESULT needs to be after troops are healed to count them as routed

      (dict_get_int, "$g_battle_result", "$coop_dict", "@battle_result"),  #-1 = enemy won, 1 = player won
      (try_begin),
        (eq, "$g_battle_result", -1), #enemy won
        (call_script, "script_party_count_members_with_full_health", "p_main_party"), 
        (assign, "$num_routed_us", reg0), 
        (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),        
        (assign, "$num_routed_allies", reg0), #use routed troops to avoid a 2nd round of battle
      (else_try),
        (eq, "$g_battle_result", 1), #player won
        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, "$num_routed_enemies", reg0), #use routed troops to avoid a 2nd round of battle
      (else_try),
        (eq, "$g_battle_result", 0), #retreat
      (try_end),


    (dict_free, "$coop_dict"),
    (try_end),
    ]),	




 # 
   # script_coop_copy_register_to_hero_xp
  ("coop_copy_register_to_hero_xp",
    [
      (store_script_param, ":troop", 1),
      (store_script_param, ":troop_xp", 2),
      (try_begin),
        (troop_get_xp, ":troop_default_xp", ":troop"),
        (store_sub, ":xp_to_add", ":troop_xp", ":troop_default_xp"), 

         # (str_store_troop_name, s40, ":troop"),
         # (assign, reg1, ":xp_to_add"),
         # (assign, reg2, ":troop_default_xp"),
         # (assign, reg3, ":troop_xp"),
         # (display_message, "@Adding {reg1} xp to {s40}   {reg2} / {reg3}"),

        (try_begin),
          (gt, ":xp_to_add", 29999),
          (store_div, ":num_times", ":xp_to_add", 29999), 
          (try_for_range, ":unused", 0, ":num_times"),
            (add_xp_to_troop, 29999, ":troop"),
            (val_sub, ":xp_to_add", 29999), 
          (try_end),		 
        (try_end),		 
        (add_xp_to_troop, ":xp_to_add", ":troop"),		 #add leftover xp
      (try_end),	




    ]),	 

   
#pavise_related_things BEGIN   
#("cf_is_behind_pavise",
# [(store_script_param, ":agent_no", 1),   
#  (store_script_param, ":pavise", 2),   
#  (set_fixed_point_multiplier, 100),
#  (assign, ":behind", 0),
#  (agent_get_position, pos5, ":agent_no"),
#  (scene_prop_get_num_instances, ":num_pavises", ":pavise"),
#  (try_for_range, ":pavise_no", 0, ":num_pavises"),
#     (eq, ":behind", 0),
#     (scene_prop_get_instance, ":pavise_prop_id", ":pavise", ":pavise_no"),
#     (prop_instance_is_valid, ":pavise_prop_id"),
#     (scene_prop_get_hit_points, ":hp", ":pavise_prop_id"),
#     (gt, ":hp", 0),
#     (prop_instance_get_position, pos2, ":pavise_prop_id"),
#     (position_transform_position_to_local, pos3, pos5, pos2),
#     (position_get_y, ":posy", pos3),
#     (is_between, ":posy", 0, 100),
#     (position_get_x, ":posx", pos3),
#     (is_between, ":posx", -70, 70),
#     (assign, ":behind", 1),
#   (try_end), 
#   (eq, ":behind", 1), ]),     
#
# 
#("deploy_pavise",
# [(store_script_param, ":agent_no", 1), 
#  (agent_get_wielded_item, ":shield_item", ":agent_no", 1),
#  (try_begin),
#     (is_between, ":shield_item", "itm_tab_shield_pavise_a", "itm_tab_shield_pavise_c"),
#     (assign, ":pavise_shield","spr_pavise_shield3"),
#  (else_try),
#     (is_between, ":shield_item", "itm_tab_shield_pavise_c", "itm_tab_shield_small_round_a"),
#     (assign, ":pavise_shield","spr_pavise_shield1"),
#  (else_try),
#     (assign, ":pavise_shield", 0),
#  (try_end),
#  (try_begin), 
#    (gt, ":pavise_shield", 0),
#    (call_script, "script_cf_agent_pushed_to_crouch",":agent_no"),
#    (set_fixed_point_multiplier, 100),
#    (agent_get_position, pos2, ":agent_no"),
#    (position_move_y, pos2, 75, 0),
#    (position_set_z_to_ground_level, pos2),
#    (set_spawn_position, pos2),
#    (spawn_scene_prop, ":pavise_shield"),
#    (agent_unequip_item, ":agent_no", ":shield_item"),
#  (try_end), ]),   
#pavise_related_things END

# SET heroes SKILL/EQUIPMENT 
  # script_coop_copy_hero_to_file
  # Input: arg1 = hero troop
  # Output: none
  ("coop_copy_hero_to_file",
    [
    (try_begin), 
      (neg|is_vanilla_warband),

      (dict_get_int, ":number_heroes", "$coop_dict", "@hero_num"),
      (try_for_range, reg21, 0, ":number_heroes"),
        (dict_get_int, ":troop_2", "$coop_dict", "@hero_{reg21}_trp"),
        (try_begin),
          (neg|game_in_multiplayer_mode),
          (this_or_next|eq, ":troop_2",  "trp_multiplayer_profile_troop_female"),  
          (eq, ":troop_2",  "trp_multiplayer_profile_troop_male"),  
          (assign, ":troop_2", "trp_player"),
         # (store_troop_gold, ":gold", ":troop_2"), #use this if needed
          # (dict_set_int, "$coop_dict", "@hero_{reg21}_gld", ":gold"),
        (try_end),

				(str_store_troop_name, s0, ":troop_2"),
        (troop_get_xp, ":xp", ":troop_2"),
        (store_troop_health, ":health", ":troop_2"),
        (dict_set_str, "$coop_dict", "@hero_{reg21}_name", s0),
        (dict_set_int, "$coop_dict", "@hero_{reg21}_xp", ":xp"),
        (dict_set_int, "$coop_dict", "@hero_{reg21}_hp", ":health"),

#NEW
        (face_keys_init, reg1),
        #(troop_get_face_keys, reg1, ":troop_2"),
        #(str_store_face_keys, s0, reg1),
        (dict_set_str, "$coop_dict", "@hero_{reg21}_face", s0),
#####PROBABLY BUGGY BEGIN
#        (store_attribute_level, ":0", ":troop_2", 0),
#        (store_attribute_level, ":1", ":troop_2", 1),
#        # (store_attribute_level, ":2", ":troop_2", 2),
#        # (store_attribute_level, ":3", ":troop_2", 3),
#
#        (dict_set_int, "$coop_dict", "@hero_{reg21}_str", ":0"),
#        (dict_set_int, "$coop_dict", "@hero_{reg21}_agi", ":1"),
#        # (dict_set_int, "$coop_dict", "@hero_{reg21}_int", ":2"),
#        # (dict_set_int, "$coop_dict", "@hero_{reg21}_cha", ":3"),
#
#
#        (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed
#          (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills
#          (store_skill_level, ":skill_level_leadership_var_1", reg20, ":troop_2"),
#          (dict_set_int, "$coop_dict", "@hero_{reg21}_skl{reg20}", ":skill_level_leadership_var_1"),
#        (try_end),
#
#        (try_for_range, reg20, 0, 7),  #wpt_firearm = 6 
		#####PROBABLY BUGGY END
		(store_attribute_level, ":0", ":troop_2", 0),
		(store_attribute_level, ":1", ":troop_2", 1),
		
        #(store_attribute_level, ":ca_strength", ":troop_2", ca_strength),          #DEF
        #(store_attribute_level, ":ca_agility", ":troop_2", ca_agility),            #DEF
        # (store_attribute_level, ":ca_intelligence", ":troop_2", ca_intelligence),
        # (store_attribute_level, ":ca_charisma", ":troop_2", ca_charisma),

		  (dict_set_int, "$coop_dict", "@hero_{reg21}_str", ":0"),
		  (dict_set_int, "$coop_dict", "@hero_{reg21}_agi", ":1"),
       #(dict_set_int, "$coop_dict", "@hero_{reg21}_str", ":ca_strength"),        # DEF
       #(dict_set_int, "$coop_dict", "@hero_{reg21}_agi", ":ca_agility"),         # DEF
        # (dict_set_int, "$coop_dict", "@hero_{reg21}_int", ":ca_intelligence"),
        # (dict_set_int, "$coop_dict", "@hero_{reg21}_cha", ":ca_charisma"),


        (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed
          (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level, ":skill_level_leadership_var_1", reg20, ":troop_2"),
          (dict_set_int, "$coop_dict", "@hero_{reg21}_skl{reg20}", ":skill_level_leadership_var_1"),
        (try_end),
		
		(try_for_range, reg20, 0, 7),  #wpt_firearm = 6 
       # (try_for_range, reg20, wpt_one_handed_weapon, 7),  #wpt_firearm = 6  #Def
          (store_proficiency_level, ":prof", ":troop_2", reg20),
          (dict_set_int, "$coop_dict", "@hero_{reg21}_wp{reg20}", ":prof"),
        (try_end),

        (try_begin),
          (neg|is_between, ":troop_2", kings_begin, pretenders_end), #need this so we dont equip lords with civilian clothes in battle
          (try_for_range, reg20, ek_item_0, ek_food), 
            (troop_get_inventory_slot, ":item", ":troop_2", reg20),
            (troop_get_inventory_slot_modifier, ":imod", ":troop_2", reg20),
            (dict_set_int, "$coop_dict", "@hero_{reg21}_itm{reg20}", ":item"),
            (dict_set_int, "$coop_dict", "@hero_{reg21}_imd{reg20}", ":imod"),
          (try_end),

        (try_end),

      (try_end), #end of hero loop


      (try_begin),
        (game_in_multiplayer_mode),
        (assign, ":troop_2", "trp_temp_troop"),
      (else_try),
        (assign, ":troop_2", "trp_player"),
        (store_skill_level, ":skill_level_leadership_var_1", "skl_inventory_management", ":troop_2"),
        (dict_set_int, "$coop_dict", "@player_inv_mgt", ":skill_level_leadership_var_1"),
      (try_end),
      (troop_get_inventory_capacity, ":end", ":troop_2"),
      (val_add,":end", 1), 
      (try_for_range, reg20, 10, ":end"),
        (troop_get_inventory_slot, ":item", ":troop_2", reg20),
        (troop_get_inventory_slot_modifier, ":imod", ":troop_2", reg20),
        (dict_set_int, "$coop_dict", "@party_inv{reg20}_itm", ":item"),
        (dict_set_int, "$coop_dict", "@party_inv{reg20}_imd", ":imod"),
        # (troop_inventory_slot_get_item_amount, ":number", ":troop_2", reg20),
        # (dict_set_int, "$coop_dict", "@party_inv{reg20}_num", ":number"),
      (try_end),
    (try_end),
    ]),	 



# SET heroes SKILL/EQUIPMENT 
  # script_coop_copy_file_to_hero
  # Input: arg1 = hero troop
  # Output: none
  ("coop_copy_file_to_hero",
    [
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_get_int, ":number_heroes", "$coop_dict", "@hero_num"),
      (try_for_range, reg21, 0, ":number_heroes"),
        (dict_get_int, ":troop_2", "$coop_dict", "@hero_{reg21}_trp"),
        (try_begin),
          (neg|game_in_multiplayer_mode), 
          (this_or_next|eq, ":troop_2",  "trp_multiplayer_profile_troop_female"),  
          (eq, ":troop_2",  "trp_multiplayer_profile_troop_male"),  
          (assign, ":troop_2", "trp_player"),  #in SP use player instead of profile
        (try_end),
#####PROBABLY BUGGY BEGIN
        (dict_get_int, ":0", "$coop_dict", "@hero_{reg21}_str"),
        (dict_get_int, ":1", "$coop_dict", "@hero_{reg21}_agi"),
        # (dict_get_int, ":2", "$coop_dict", "@hero_{reg21}_int"),
        # (dict_get_int, ":3", "$coop_dict", "@hero_{reg21}_cha"),

        (store_attribute_level, ":value", ":troop_2", 0),
        (val_sub, ":0", ":value"),
        (store_attribute_level, ":value", ":troop_2", 1),
        (val_sub, ":1", ":value"),

        (troop_raise_attribute, ":troop_2", 0, ":0"),
        (troop_raise_attribute, ":troop_2", 1, ":1"),
        # (troop_raise_attribute, ":troop_2", 2, ":2"),
        # (troop_raise_attribute, ":troop_2", 3, ":3"),

        (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed
          (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills
          (dict_get_int, ":skill_level_leadership_var_1", "$coop_dict", "@hero_{reg21}_skl{reg20}"),
          (store_skill_level, ":value", reg20,":troop_2"),
          (val_sub, ":skill_level_leadership_var_1", ":value"),
          (troop_raise_skill, ":troop_2", reg20, ":skill_level_leadership_var_1"),
          # (try_begin), #NEW
            # (eq, reg20, "skl_ironflesh"),
            # (store_mul, ":added_ironflesh", ":skill_level_leadership_var_1", 2), #get number of hit point that will be added when spawning
          # (try_end),
        (try_end),

        (try_for_range, reg20, 0, 7),  #wpt_firearm = 6 
#####PROBABLY BUGGY END

 #       (dict_get_int, ":ca_strength", "$coop_dict", "@hero_{reg21}_str"),                                                                                #DEF
 #       (dict_get_int, ":ca_agility", "$coop_dict", "@hero_{reg21}_agi"),                                                                                 #DEF
 #       # (dict_get_int, ":ca_intelligence", "$coop_dict", "@hero_{reg21}_int"),                                                                          #DEF
 #       # (dict_get_int, ":ca_charisma", "$coop_dict", "@hero_{reg21}_cha"),                                                                              #DEF
 #                                                                                                                                                         #DEF
 #       (store_attribute_level, ":value", ":troop_2", ca_strength),                                                                                       #DEF
 #       (val_sub, ":ca_strength", ":value"),                                                                                                              #DEF
 #       (store_attribute_level, ":value", ":troop_2", ca_agility),                                                                                        #DEF
 #       (val_sub, ":ca_agility", ":value"),                                                                                                               #DEF
 #                                                                                                                                                         #DEF
 #       (troop_raise_attribute, ":troop_2", ca_strength, ":ca_strength"),                                                                                 #DEF
 #       (troop_raise_attribute, ":troop_2", ca_agility, ":ca_agility"),                                                                                   #DEF
 #       # (troop_raise_attribute, ":troop_2", ca_intelligence, ":ca_intelligence"),                                                                       #DEF
 #       # (troop_raise_attribute, ":troop_2", ca_charisma, ":ca_charisma"),                                                                               #DEF
 #                                                                                                                                                         #DEF
 #       (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed                                  #DEF
 #         (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills                                                                 #DEF
 #         (dict_get_int, ":skill_level_leadership_var_1", "$coop_dict", "@hero_{reg21}_skl{reg20}"),                                                      #DEF
 #         (store_skill_level, ":value", reg20,":troop_2"),                                                                                                #DEF
 #         (val_sub, ":skill_level_leadership_var_1", ":value"),                                                                                           #DEF
 #         (troop_raise_skill, ":troop_2", reg20, ":skill_level_leadership_var_1"),                                                                        #DEF
 #         # (try_begin), #NEW                                                                                                                             #DEF
 #           # (eq, reg20, "skl_ironflesh"),                                                                                                               #DEF
 #           # (store_mul, ":added_ironflesh", ":skill_level_leadership_var_1", 2), #get number of hit point that will be added when spawning              #DEF
 #         # (try_end),                                                                                                                                    #DEF
 #       (try_end),                                                                                                                                        #DEF
 #                                                                                                                                                         #DEF
 #       (try_for_range, reg20, wpt_one_handed_weapon, 7),  #wpt_firearm = 6                                                                               #DEF
          (dict_get_int, ":wprof", "$coop_dict", "@hero_{reg21}_wp{reg20}"),
          (store_proficiency_level, ":value", ":troop_2", reg20),
          (val_sub, ":wprof", ":value"),
          (troop_raise_proficiency_linear, ":troop_2", reg20, ":wprof"),
        (try_end),

        (try_begin),
          (neg|is_between, ":troop_2", kings_begin, pretenders_end), #need this so we dont equip lords with civilian clothes in battle
          (dict_get_str, s0, "$coop_dict", "@hero_{reg21}_name"),
          (try_begin),
            (str_is_empty, s0),
            (str_store_string, s0, "@Player"), #set default name
          (try_end),
          (troop_set_name, ":troop_2", s0),
      
          (try_begin),#only copy inventory to SP when optional
            (this_or_next|game_in_multiplayer_mode), 
            (eq, "$coop_disable_inventory", 0),
            (try_for_range, reg20, ek_item_0, ek_food), 
              (dict_get_int, ":item", "$coop_dict", "@hero_{reg21}_itm{reg20}"),
              (dict_get_int, ":imod", "$coop_dict", "@hero_{reg21}_imd{reg20}"),
              (troop_set_inventory_slot, ":troop_2", reg20, ":item"),
              (troop_set_inventory_slot_modifier, ":troop_2", reg20, ":imod"),
            (try_end),
          (try_end),
        (try_end),
#NEW
        (try_begin),#only set face in MP
          (game_in_multiplayer_mode),
          (dict_get_str, s0, "$coop_dict", "@hero_{reg21}_face"),
          (face_keys_store_string, reg1, s0),
          #ENVFIX(troop_set_face_keys, ":troop_2", reg1),
        (try_end),

        (dict_get_int, ":xp", "$coop_dict", "@hero_{reg21}_xp"),
        (call_script, "script_coop_copy_register_to_hero_xp", ":troop_2", ":xp"),

        (dict_get_int, ":battle_health", "$coop_dict", "@hero_{reg21}_hp"),
        (try_begin),#set health after attributes
          (neg|game_in_multiplayer_mode),
          (main_party_has_troop, ":troop_2"),
          (party_get_skill_level, ":player_party_first_aid", "p_main_party", "skl_first_aid"), #currently we get medic skill before wounding heroes
          (val_mul, ":player_party_first_aid", 5),  #5% per skill level
          (store_troop_health, ":old_health", ":troop_2"),
          (store_sub, ":lost_health", ":old_health",":battle_health"),
          (val_max, ":lost_health", 0), # if <0 we would gain health
          (val_mul, ":lost_health", ":player_party_first_aid"),
          (val_div, ":lost_health", 100),
          (val_add, ":battle_health", ":lost_health"), #add recovered percentage
          (troop_set_health, ":troop_2", ":battle_health"),
        (else_try),
          #NEW not getting this bug anymore 
          #  when setup MP: ironflesh will add alive hitpoint later when troop spawns, so find what % troop should be now to compensate
          # (troop_set_health, ":troop_2", ":battle_health"), 
          # (store_mul, ":hp_x10", ":battle_health",10), 
          # (store_troop_health, ":hp", ":troop_2",1),
          # (val_max, ":hp", 1),
          # (val_div, ":hp_x10", ":hp"), 
          # (val_mul, ":hp_x10", ":added_ironflesh"), 
          # (val_div, ":hp_x10", 10), 
          # (val_sub, ":battle_health", ":hp_x10"), 
          (troop_set_health, ":troop_2", ":battle_health"), 
        (try_end),

        #use this if needed
        # (try_begin),
          # (dict_get_int, ":new_gold", "$coop_dict", "@hero_{reg21}_gld"),
          # (store_troop_gold, ":cur_gold", ":troop_2"), 
          # (gt, ":new_gold", ":cur_gold"),
          # (val_sub, ":new_gold", ":cur_gold"),
          # (troop_add_gold,":troop_2",":new_gold"),
        # (try_end),

      (try_end), #end of hero loop

    
      (try_begin),
        (this_or_next|game_in_multiplayer_mode), 
        (eq, "$coop_disable_inventory", 0),  #inventory is optional
        (try_begin),
          (game_in_multiplayer_mode),
          (assign, ":troop_2", "trp_temp_troop"),
          (dict_get_int, ":skill_level_leadership_var_1", "$coop_dict", "@player_inv_mgt"),
          (store_skill_level, ":value", "skl_inventory_management",":troop_2"),
          (val_sub, ":skill_level_leadership_var_1", ":value"),
          (troop_raise_skill, ":troop_2", "skl_inventory_management", ":skill_level_leadership_var_1"),
        (else_try),
          (assign, ":troop_2", "trp_player"),
        (try_end),
        (troop_get_inventory_capacity, ":end", ":troop_2"),
        (val_add,":end", 1), 
        (try_for_range, reg20, 10, ":end"),
          (dict_get_int, ":item", "$coop_dict", "@party_inv{reg20}_itm"),
          (dict_get_int, ":imod", "$coop_dict", "@party_inv{reg20}_imd"),

          (assign, ":skip",0),
          (try_begin),
            (neg|game_in_multiplayer_mode),
            (is_between, ":item", trade_goods_begin, trade_goods_end), #these items would need to copy correct quantity still need to copy to MP to take up inv capacity 
            (assign, ":skip",1),
          (try_end),

          (eq, ":skip",0),
          (troop_set_inventory_slot, ":troop_2", reg20, ":item"),
          (troop_set_inventory_slot_modifier, ":troop_2", reg20, ":imod"),

          # (dict_get_int, ":number", "$coop_dict", "@party_inv{reg20}_num"),
          # (try_begin),
            # (gt, ":number", 0), 
            # (troop_inventory_slot_set_item_amount, ":troop_2", reg20, ":number"),
          # (try_end),

        (try_end),
      (try_end),

    (try_end),
    ]),	 

##Doghotel begin
#  ("doghotel_initialize_bot_globals",
#  [
#    (store_script_param, ":var0", 1),
#    (assign, "$g_doghotel_batch_offset", 0),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_enable_brainy_bots", 0),
#      (assign, "$g_doghotel_enable_brainy_bots", 1),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_movement_actions_enabled", 0),
#      (assign, "$g_doghotel_movement_actions_enabled", 1),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_batch_size", 0),
#      (assign, "$g_doghotel_batch_size", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_nearby_enemy_radius", 0),
#      (assign, "$g_doghotel_nearby_enemy_radius", 1000),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_nearby_neutral_radius", 0),
#      (assign, "$g_doghotel_nearby_neutral_radius", 5000),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_nearby_ally_radius", 0),
#      (assign, "$g_doghotel_nearby_ally_radius", 5000),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_block_chance", 0),
#      (assign, "$g_doghotel_min_block_chance", 70),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_block_chance", 0),
#      (assign, "$g_doghotel_max_block_chance", 90),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_hold_chance", 0),
#      (assign, "$g_doghotel_min_hold_chance", 20),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_hold_chance", 0),
#      (assign, "$g_doghotel_max_hold_chance", 40),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_feint_chance", 0),
#      (assign, "$g_doghotel_min_feint_chance", 20),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_feint_chance", 0),
#      (assign, "$g_doghotel_max_feint_chance", 40),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_chamber_chance", 0),
#      (assign, "$g_doghotel_min_chamber_chance", 15),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_chamber_chance", 0),
#      (assign, "$g_doghotel_max_chamber_chance", 25),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_weapon_prof", 0),
#      (assign, "$g_doghotel_min_weapon_prof", 100),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_weapon_prof", 0),
#      (assign, "$g_doghotel_max_weapon_prof", 200),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_hold_msec", 0),
#      (assign, "$g_doghotel_min_hold_msec", 250),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_hold_msec", 0),
#      (assign, "$g_doghotel_max_hold_msec", 750),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_consecutive_feints", 0),
#      (assign, "$g_doghotel_max_consecutive_feints", 2),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_poor_block_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_poor_block_reduction", 20),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_poor_hold_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_poor_hold_reduction", 10),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_poor_feint_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_poor_feint_reduction", 10),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_poor_chamber_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_poor_chamber_reduction", 10),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_average_block_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_average_block_reduction", 10),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_average_hold_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_average_hold_reduction", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_average_feint_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_average_feint_reduction", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_ai_average_chamber_reduction", 0),
#      (assign, "$g_doghotel_combat_ai_average_chamber_reduction", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_renown_block_bonus", 0),
#      (assign, "$g_doghotel_renown_block_bonus", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_renown_feint_bonus", 0),
#      (assign, "$g_doghotel_renown_feint_bonus", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_renown_hold_bonus", 0),
#      (assign, "$g_doghotel_renown_hold_bonus", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_renown_chamber_bonus", 0),
#      (assign, "$g_doghotel_renown_chamber_bonus", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_renown_min", 0),
#      (assign, "$g_doghotel_renown_min", 100),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_combat_difficulty", 0),
#      (assign, "$g_doghotel_combat_difficulty", 1),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_anti_autoblock", 0),
#      (assign, "$g_doghotel_anti_autoblock", 1),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_enable_only_for_heroes", 0),
#      (assign, "$g_doghotel_enable_only_for_heroes", 0),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_version_id_netcode", 0),
#      (assign, "$g_doghotel_version_id_netcode", 2),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_version_id", 0),
#      (assign, "$g_doghotel_version_id", 3),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_min_kick_chance", 0),
#      (assign, "$g_doghotel_min_kick_chance", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_max_kick_chance", 0),
#      (assign, "$g_doghotel_max_kick_chance", 20),
#    (try_end),
#  ]),
#
#  ("doghotel_initialize_mp_globals",
#  [
#    (store_script_param, ":var0", 1),
#    (try_begin),
#      (multiplayer_is_server),
#      (assign, "$g_doghotel_multiplayer_brainy_bots_installed_on_server", 1),
#    (else_try),
#      (assign, "$g_doghotel_multiplayer_brainy_bots_installed_on_server", 0),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_ping_limit", 0),
#      (assign, "$g_doghotel_ping_limit", 200),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_stop_test_server_timer", 0),
#      (assign, "$g_doghotel_stop_test_server_timer", 0),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_stop_test_server_after", 0),
#      (assign, "$g_doghotel_stop_test_server_after", 5),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_brainy_message_interval", 0),
#      (assign, "$g_doghotel_brainy_message_interval", 600),
#    (try_end),
#    (try_begin),
#      (this_or_next|eq, ":var0", 1),
#      (eq, "$g_doghotel_duel_add_bots", 0),
#      (assign, "$g_doghotel_duel_add_bots", 1),
#    (try_end),
#  ]),
#
#  ("doghotel_item_get_wpt",
#  [
#    (store_script_param, ":var0", 1),
#    (try_begin),
#      (ge, ":var0", 0),
#      (item_get_type, ":var1", ":var0"),
#    (else_try),
#      (assign, ":var1", 0),
#    (try_end),
#    (try_begin),
#      (eq, ":var1", 2),
#      (assign, reg0, 0),
#    (else_try),
#      (eq, ":var1", 3),
#      (assign, reg0, 1),
#    (else_try),
#      (eq, ":var1", 4),
#      (assign, reg0, 2),
#    (else_try),
#      (this_or_next|eq, ":var1", 8),
#      (eq, ":var1", 5),
#      (assign, reg0, 3),
#    (else_try),
#      (this_or_next|eq, ":var1", 9),
#      (eq, ":var1", 6),
#      (assign, reg0, 4),
#    (else_try),
#      (eq, ":var1", 10),
#      (assign, reg0, 5),
#    (else_try),
#      (this_or_next|eq, ":var1", 16),
#      (this_or_next|eq, ":var1", 17),
#      (eq, ":var1", 18),
#      (assign, reg0, 6),
#    (try_end),
#  ]),
#
#  ("doghotel_reset_bots",
#  [
#    (try_for_agents, ":var0"),
#      (agent_is_active, ":var0"),
#      (agent_is_non_player, ":var0"),
#      (agent_is_human, ":var0"),
#      (agent_is_alive, ":var0"),
#      (agent_set_attack_action, ":var0", -2, 0),
#      (agent_set_attack_action, ":var0", -2, 1),
#      (agent_set_defend_action, ":var0", -2, 1),
#    (try_end),
#  ]),
#
#  ("doghotel_error_message",
#  [
#    (store_script_param, ":var0", 1),
#    (display_message, ":var0", 0x00AB1313),
#    (try_begin),
#      (multiplayer_is_dedicated_server),
#      (server_add_message_to_log, ":var0"),
#    (try_end),
#  ]),
#
#  ("doghotel_kick_agent",
#  [
#    (store_script_param, ":var0", 1),
#    (store_script_param, ":var1", 2),
#    (try_begin),
#      (agent_get_wielded_item, ":var2", ":var0", 0),
#      (eq, ":var2", -1),
#      (agent_get_troop_id, ":var3", ":var0"),
#      (store_attribute_level, ":var4", ":var3", 0),
#      (val_div, ":var4", 3),
#      (val_add, ":var4", 3),
#      (agent_deliver_damage_to_agent_advanced, reg0, ":var0", ":var1", ":var4"),
#    (try_end),
#    (agent_play_sound, ":var0", "snd_blunt_hit"),
#    (agent_set_animation, ":var1", 425),
#  ]),
#
#  ("doghotel_kick_anim",
#  [
#    (store_script_param, ":var0", 1),
#    (agent_set_animation, ":var0", 23),
#  ]),
#
#  ("doghotel_combat_loop",
#  [
#    (store_mission_timer_a_msec, ":var0"),
#    (try_for_agents, ":var1"),
#      (agent_is_active, ":var1"),
#      (agent_is_non_player, ":var1"),
#      (agent_is_human, ":var1"),
#      (agent_is_alive, ":var1"),
#      (agent_get_troop_id, ":var2", ":var1"),
#      (this_or_next|neq, "$g_doghotel_enable_only_for_heroes", 1),
#      (troop_is_hero, ":var2"),
#      (agent_get_slot, ":var3", ":var1", 40),
#      (agent_get_slot, ":var4", ":var1", 36),
#      (agent_get_slot, ":var5", ":var1", 37),
#      (agent_get_attack_action, ":var6", ":var1"),
#      (agent_get_defend_action, ":var7", ":var1"),
#      (agent_get_wielded_item, ":var8", ":var1", 0),
#      (agent_get_wielded_item, ":var9", ":var1", 1),
#      (agent_get_position, pos1, ":var1"),
#      (agent_get_horse, ":var10", ":var1"),
#      (agent_get_slot, ":var11", ":var1", 38),
#      (try_begin),
#        (multiplayer_is_server),
#        (store_skill_level, ":var12", "skl_trainer", ":var2"),
#        (eq, ":var12", 10),
#        (assign, ":var11", 0),
#      (try_end),
#      (try_begin),
#        (ge, ":var8", 0),
#        (item_get_weapon_length, ":var13", ":var8"),
#      (else_try),
#        (assign, ":var13", 100),
#      (try_end),
#      (store_add, ":var14", ":var13", 100),
#      (agent_get_animation, ":var15", ":var1", 0),
#      (agent_get_slot, ":var16", ":var1", 52),
#      (store_sub, ":var17", ":var4", ":var0"),
#      (assign, ":var18", 0),
#      (assign, ":var19", -1),
#      (assign, ":var20", 0),
#      (assign, ":var21", -1),
#      (assign, ":var22", -1),
#      (try_begin),
#        (gt, ":var3", 0),
#        (agent_is_alarmed, ":var1"),
#        (agent_get_troop_id, ":var2", ":var1"),
#        (this_or_next|neq, "$g_doghotel_enable_only_for_heroes", 1),
#        (troop_is_hero, ":var2"),
#        (agent_get_simple_behavior, ":var23", ":var1"),
#        (neq, ":var23", 5),
#        (neq, ":var23", 6),
#        (neq, ":var23", 7),
#        (try_for_range, ":var24", 43, 46),
#          (try_begin),
#            (eq, ":var24", 43),
#            (agent_get_slot, ":var25", ":var1", 43),
#          (else_try),
#            (eq, ":var24", 44),
#            (agent_get_slot, ":var25", ":var1", 44),
#          (else_try),
#            (eq, ":var24", 45),
#            (agent_get_slot, ":var25", ":var1", 45),
#          (else_try),
#            (agent_get_slot, ":var25", ":var1", ":var24"),
#          (try_end),
#          (ge, ":var25", 0),
#          (agent_is_active, ":var25"),
#          (agent_is_human, ":var25"),
#          (agent_is_alive, ":var25"),
#          (agent_get_position, pos2, ":var25"),
#          (agent_get_wielded_item, ":var26", ":var25", 0),
#          (get_distance_between_positions, ":var27", pos1, pos2),
#          (position_transform_position_to_local, pos3, pos1, pos2),
#          (position_get_y, ":var28", pos3),
#          (ge, ":var28", 0),
#          (position_get_rotation_around_z, ":var29", pos3),
#          (set_fixed_point_multiplier, 100),
#          (position_get_x, ":var30", pos3),
#          (assign, ":var31", 150),
#          (try_begin),
#            (ge, ":var26", 0),
#            (item_get_weapon_length, ":var32", ":var26"),
#            (val_add, ":var31", ":var32"),
#          (try_end),
#          (try_begin),
#            (eq, ":var15", 24),
#            (neq, ":var16", 2),
#            (eq, ":var10", -1),
#            (agent_get_horse, ":var33", ":var25"),
#            (eq, ":var33", -1),
#            (copy_position, 4, 2),
#            (position_set_z, pos4, 0),
#            (agent_get_bone_position, pos5, ":var1", 6, 1),
#            (position_get_z, ":var34", pos5),
#            (position_set_z, pos5, 0),
#            (get_distance_between_positions, ":var35", pos4, pos5),
#            (le, ":var35", 30),
#            (agent_get_bone_position, pos6, ":var25", 3, 1),
#            (agent_get_bone_position, pos7, ":var25", 6, 1),
#            (agent_get_bone_position, pos8, ":var25", 9, 1),
#            (position_get_z, ":var36", pos6),
#            (position_get_z, ":var37", pos7),
#            (position_get_z, ":var38", pos8),
#            (assign, ":var39", ":var38"),
#            (assign, ":var40", ":var36"),
#            (val_min, ":var40", ":var37"),
#            (is_between, ":var34", ":var40", ":var39"),
#            (call_script, "script_doghotel_kick_agent", ":var1", ":var25"),
#            (agent_set_slot, ":var1", 36, 0),
#            (agent_set_slot, ":var1", 37, 0),
#            (agent_set_slot, ":var1", 52, 2),
#          (try_end),
#          (try_begin),
#            (neq, ":var18", 6),
#            (try_begin),
#              (eq, ":var16", 1),
#              (eq, ":var10", -1),
#              (le, ":var27", 100),
#              (is_between, ":var30", 0, 10),
#              (neg|is_between, ":var15", 20, 26),
#              (agent_get_animation, ":var41", ":var25", 0),
#              (neg|is_between, ":var41", 20, 24),
#              (agent_get_speed, pos4, ":var25"),
#              (set_fixed_point_multiplier, 100),
#              (position_get_x, ":var42", pos4),
#              (is_between, ":var42", -100, 100),
#              (position_get_y, ":var43", pos4),
#              (ge, ":var43", 0),
#              (assign, ":var18", 6),
#            (try_end),
#            (neq, ":var18", 6),
#            (neq, ":var18", 1),
#            (try_begin),
#              (agent_get_attack_action, ":var44", ":var25"),
#              (eq, ":var44", 2),
#              (neq, ":var6", 2),
#              (le, ":var27", ":var31"),
#              (assign, ":var45", 1),
#              (try_begin),
#                (ge, ":var9", 0),
#                (item_get_type, ":var46", ":var9"),
#                (eq, ":var46", 7),
#              (else_try),
#                (agent_get_slot, ":var47", ":var1", 43),
#                (eq, ":var25", ":var47"),
#              (else_try),
#                (assign, ":var45", 0),
#              (try_end),
#              (try_begin),
#                (agent_is_non_player, ":var25"),
#                (try_begin),
#                  (agent_ai_get_behavior_target, ":var48", ":var25"),
#                  (eq, ":var48", ":var1"),
#                  (is_between, ":var29", 135, 225),
#                (else_try),
#                  (agent_ai_get_look_target, ":var49", ":var25"),
#                  (eq, ":var49", ":var1"),
#                  (is_between, ":var29", 135, 225),
#                (else_try),
#                  (assign, ":var45", 0),
#                (try_end),
#              (else_try),
#                (neg|agent_is_non_player, ":var25"),
#                (is_between, ":var29", 90, 270),
#              (else_try),
#                (assign, ":var45", 0),
#              (try_end),
#              (eq, ":var45", 1),
#              (eq, ":var11", 0),
#              (assign, ":var18", 1),
#              (assign, ":var19", ":var25"),
#            (try_end),
#            (neq, ":var18", 1),
#            (neq, ":var18", 5),
#            (try_begin),
#              (this_or_next|is_between, ":var15", 20, 26),
#              (gt, ":var17", 0),
#              (assign, ":var18", 5),
#              (assign, ":var19", ":var25"),
#            (try_end),
#            (neq, ":var18", 5),
#            (neq, ":var18", 4),
#            (try_begin),
#              (ge, ":var5", 1),
#              (le, ":var27", ":var14"),
#              (assign, ":var18", 4),
#              (assign, ":var19", ":var25"),
#            (try_end),
#            (neq, ":var18", 4),
#            (neq, ":var18", 2),
#            (try_begin),
#              (le, ":var27", ":var14"),
#              (assign, ":var18", 2),
#              (assign, ":var19", ":var25"),
#            (try_end),
#          (try_end),
#          (try_begin),
#            (eq, "$g_doghotel_movement_actions_enabled", 1),
#            (eq, ":var10", -1),
#            (neq, ":var20", 1),
#            (try_begin),
#              (is_between, ":var30", -5, 15),
#              (lt, ":var27", 200),
#              (agent_get_animation, ":var50", ":var25", 0),
#              (is_between, ":var50", 20, 26),
#              (try_begin),
#                (ge, ":var27", 150),
#                (ge, ":var50", 24),
#              (else_try),
#                (ge, ":var27", 150),
#                (set_fixed_point_multiplier, 100),
#                (agent_get_speed, pos4, ":var1"),
#                (position_get_y, ":var51", pos4),
#                (le, ":var51", 50),
#              (else_try),
#                (assign, ":var20", 1),
#                (assign, ":var21", ":var25"),
#              (try_end),
#              (neq, ":var20", 1),
#            (else_try),
#              (eq, ":var18", 1),
#              (ge, ":var26", 0),
#              (item_has_property, ":var26", itp_crush_through),
#              (agent_get_action_dir, ":var52", ":var25"),
#              (eq, ":var52", 3),
#              (is_between, ":var30", -10, 20),
#              (agent_get_wielded_item, ":var53", ":var25", 0),
#              (item_get_weapon_length, ":var54", ":var53"),
#              (store_add, ":var55", ":var54", 150),
#              (lt, ":var27", ":var55"),
#              (try_begin),
#                (neq, ":var16", 1),
#                (agent_set_slot, ":var1", 52, 1),
#              (try_end),
#              (assign, ":var20", 1),
#              (assign, ":var21", ":var25"),
#            (try_end),
#          (try_end),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (ge, ":var19", 0),
#        (agent_get_action_dir, ":var52", ":var19"),
#        (agent_get_wielded_item, ":var26", ":var19", 0),
#      (else_try),
#        (assign, ":var52", -1),
#        (assign, ":var26", -1),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", 6),
#        (call_script, "script_doghotel_kick_anim", ":var1"),
#        (agent_set_slot, ":var1", 52, 0),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", 0),
#        (try_begin),
#          (gt, ":var4", 0),
#          (agent_set_slot, ":var1", 36, 0),
#          (assign, ":var18", -2),
#        (try_end),
#        (try_begin),
#          (gt, ":var5", 0),
#          (agent_set_slot, ":var1", 37, ":var5"),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", 3),
#        (try_begin),
#          (ge, ":var26", 0),
#          (item_get_speed_rating, ":var56", ":var26"),
#        (else_try),
#          (assign, ":var56", 100),
#        (try_end),
#        (try_begin),
#          (ge, ":var56", 95),
#          (store_sub, ":var57", 120, ":var56"),
#          (val_clamp, ":var57", 10, 30),
#          (le, ":var22", ":var57"),
#          (neq, ":var6", 2),
#          (assign, ":var58", -1),
#          (try_begin),
#            (eq, ":var52", 0),
#            (this_or_next|eq, ":var8", -1),
#            (item_has_capability, ":var8", itc_pike|itcf_thrust_onehanded|itcf_thrust_twohanded|itcf_horseback_thrust_onehanded|itcf_thrust_musket),
#            (assign, ":var58", 0),
#          (else_try),
#            (eq, ":var52", 1),
#            (this_or_next|eq, ":var8", -1),
#            (item_has_capability, ":var8", itcf_slashright_onehanded|itcf_slashright_twohanded|itcf_slashright_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slash_polearm),
#            (assign, ":var58", 2),
#          (else_try),
#            (eq, ":var52", 2),
#            (this_or_next|eq, ":var8", -1),
#            (item_has_capability, ":var8", itcf_slashleft_onehanded|itcf_slashleft_twohanded|itcf_slashleft_polearm|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm),
#            (assign, ":var58", 1),
#          (else_try),
#            (eq, ":var52", 3),
#            (this_or_next|eq, ":var8", -1),
#            (item_has_capability, ":var8", itcf_overswing_onehanded|itcf_overswing_twohanded|itcf_overswing_polearm|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_overswing_spear|itcf_overswing_musket),
#            (assign, ":var58", 3),
#          (try_end),
#          (ge, ":var58", 0),
#          (agent_set_defend_action, ":var1", -2, 0),
#          (agent_set_defend_action, ":var1", -2, 1),
#          (agent_set_attack_action, ":var1", ":var58", 0),
#        (else_try),
#          (assign, ":var18", 1),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", 1),
#        (assign, ":var45", 0),
#        (try_begin),
#          (eq, ":var8", -1),
#          (eq, ":var26", -1),
#          (assign, ":var45", 1),
#        (else_try),
#          (ge, ":var9", 0),
#          (item_get_type, ":var46", ":var9"),
#          (eq, ":var46", 7),
#          (assign, ":var45", 1),
#        (else_try),
#          (ge, ":var8", 0),
#          (try_begin),
#            (eq, ":var52", 0),
#            (item_has_capability, ":var8", itcf_parry_forward_onehanded|itcf_parry_forward_twohanded|itcf_parry_forward_polearm),
#            (assign, ":var45", 1),
#          (else_try),
#            (eq, ":var52", 1),
#            (item_has_capability, ":var8", itcf_parry_right_onehanded|itcf_parry_right_twohanded|itcf_parry_right_polearm),
#            (assign, ":var45", 1),
#          (else_try),
#            (eq, ":var52", 2),
#            (item_has_capability, ":var8", itcf_parry_left_onehanded|itcf_parry_left_twohanded|itcf_parry_left_polearm),
#            (assign, ":var45", 1),
#          (else_try),
#            (eq, ":var52", 3),
#            (item_has_capability, ":var8", itcf_parry_up_onehanded|itcf_parry_up_twohanded|itcf_parry_up_polearm),
#            (assign, ":var45", 1),
#          (try_end),
#        (try_end),
#        (try_begin),
#          (eq, ":var45", 1),
#          (agent_set_attack_action, ":var1", -2, 0),
#          (try_begin),
#            (this_or_next|eq, ":var52", 0),
#            (eq, ":var52", 3),
#            (agent_set_defend_action, ":var1", ":var52", 1),
#          (else_try),
#            (eq, ":var52", 1),
#            (agent_set_defend_action, ":var1", 2, 1),
#          (else_try),
#            (eq, ":var52", 2),
#            (agent_set_defend_action, ":var1", 1, 1),
#          (try_end),
#        (else_try),
#          (assign, ":var18", 2),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", 4),
#        (try_begin),
#          (eq, ":var6", 1),
#          (agent_set_attack_action, ":var1", -2, 1),
#        (else_try),
#          (agent_set_attack_action, ":var1", -2, 0),
#        (try_end),
#        (try_begin),
#          (eq, ":var7", 2),
#          (agent_set_defend_action, ":var1", 1, 0),
#          (agent_set_defend_action, ":var1", -2, 1),
#          (assign, ":var18", 2),
#          (val_sub, ":var5", 1),
#          (agent_set_slot, ":var1", 37, ":var5"),
#        (else_try),
#          (agent_set_defend_action, ":var1", 3, 1),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (assign, ":var59", -1),
#        (try_begin),
#          (eq, ":var18", 2),
#          (assign, ":var59", 0),
#        (else_try),
#          (eq, ":var18", 5),
#          (assign, ":var59", 1),
#        (try_end),
#        (ge, ":var59", 0),
#        (try_begin),
#          (ge, ":var8", 0),
#          (assign, reg0, -1),
#          (assign, reg1, -1),
#          (assign, reg2, -1),
#          (assign, reg3, -1),
#          (try_begin),
#            (item_has_capability, ":var8", itcf_slashright_onehanded|itcf_slashright_twohanded|itcf_slashright_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slash_polearm),
#            (assign, reg1, 1),
#          (try_end),
#          (try_begin),
#            (item_has_capability, ":var8", itcf_slashleft_onehanded|itcf_slashleft_twohanded|itcf_slashleft_polearm|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm),
#            (assign, reg2, 2),
#          (try_end),
#          (try_begin),
#            (item_has_capability, ":var8", itcf_overswing_onehanded|itcf_overswing_twohanded|itcf_overswing_polearm|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_overswing_spear|itcf_overswing_musket),
#            (assign, reg3, 3),
#          (try_end),
#          (try_begin),
#            (item_has_capability, ":var8", itc_pike|itcf_thrust_onehanded|itcf_thrust_twohanded|itcf_horseback_thrust_onehanded|itcf_thrust_musket),
#            (try_begin),
#              (eq, reg1, -1),
#              (eq, reg2, -1),
#              (eq, reg3, -1),
#              (assign, reg0, 0),
#            (else_try),
#              (try_begin),
#                (item_get_type, ":var60", ":var8"),
#                (eq, ":var60", 4),
#                (ge, ":var9", 0),
#                (assign, reg0, 0),
#              (else_try),
#                (agent_get_position, pos2, ":var19"),
#                (get_distance_between_positions, ":var27", pos1, pos2),
#                (this_or_next|gt, ":var27", ":var13"),
#                (gt, ":var27", 200),
#                (assign, reg0, 0),
#              (else_try),
#                (store_random_in_range, ":var61", 1, 4),
#                (eq, ":var61", 1),
#                (assign, reg0, 0),
#              (try_end),
#            (try_end),
#          (try_end),
#        (else_try),
#          (eq, ":var8", -1),
#          (assign, reg0, 0),
#          (assign, reg1, 1),
#          (assign, reg2, 2),
#          (assign, reg3, 3),
#        (try_end),
#        (shuffle_range, 0, 4),
#        (try_begin),
#          (ge, reg0, 0),
#          (agent_set_attack_action, ":var1", reg0, ":var59"),
#        (else_try),
#          (ge, reg1, 0),
#          (agent_set_attack_action, ":var1", reg1, ":var59"),
#        (else_try),
#          (ge, reg2, 0),
#          (agent_set_attack_action, ":var1", reg2, ":var59"),
#        (else_try),
#          (ge, reg3, 0),
#          (agent_set_attack_action, ":var1", reg3, ":var59"),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":var18", -2),
#        (agent_set_attack_action, ":var1", -2, 0),
#        (agent_set_attack_action, ":var1", -2, 1),
#        (agent_set_defend_action, ":var1", -2, 1),
#      (try_end),
#      (try_begin),
#        (eq, ":var20", 1),
#        (ge, ":var21", 0),
#        (agent_is_active, ":var21"),
#        (agent_is_human, ":var21"),
#        (agent_is_alive, ":var21"),
#        (copy_position, 4, 1),
#        (position_move_y, pos4, -150, 0),
#        (agent_set_slot, ":var1", 51, 1),
#        (agent_set_scripted_destination, ":var1", pos4, 1),
#      (try_end),
#      (try_begin),
#        (eq, ":var20", 0),
#        (agent_get_slot, ":var62", ":var1", 51),
#        (gt, ":var62", 0),
#        (agent_is_in_special_mode, ":var1"),
#        (agent_clear_scripted_mode, ":var1"),
#        (agent_force_rethink, ":var1"),
#        (agent_set_slot, ":var1", 51, 0),
#      (try_end),
#    (try_end),
#  ]),
#
#  ("doghotel_special_actions",
#  [
#    (store_mission_timer_a_msec, ":var0"),
#    (options_get_combat_ai, ":var1"),
#    (try_begin),
#      (eq, ":var1", 2),
#      (assign, ":var2", "$g_doghotel_combat_ai_poor_block_reduction"),
#      (assign, ":var3", "$g_doghotel_combat_ai_poor_hold_reduction"),
#      (assign, ":var4", "$g_doghotel_combat_ai_poor_feint_reduction"),
#      (assign, ":var5", "$g_doghotel_combat_ai_poor_chamber_reduction"),
#    (else_try),
#      (eq, ":var1", 1),
#      (assign, ":var2", "$g_doghotel_combat_ai_average_block_reduction"),
#      (assign, ":var3", "$g_doghotel_combat_ai_average_hold_reduction"),
#      (assign, ":var4", "$g_doghotel_combat_ai_average_feint_reduction"),
#      (assign, ":var5", "$g_doghotel_combat_ai_average_chamber_reduction"),
#    (else_try),
#      (assign, ":var2", 0),
#      (assign, ":var3", 0),
#      (assign, ":var4", 0),
#      (assign, ":var5", 0),
#    (try_end),
#    (try_for_agents, ":var6"),
#      (agent_is_non_player, ":var6"),
#      (agent_is_human, ":var6"),
#      (agent_is_alive, ":var6"),
#      (agent_is_alarmed, ":var6"),
#      (agent_get_troop_id, ":var7", ":var6"),
#      (this_or_next|neq, "$g_doghotel_enable_only_for_heroes", 1),
#      (troop_is_hero, ":var7"),
#      (agent_get_simple_behavior, ":var8", ":var6"),
#      (neq, ":var8", 5),
#      (neq, ":var8", 6),
#      (neq, ":var8", 7),
#      (agent_get_slot, ":var9", ":var6", 40),
#      (gt, ":var9", 0),
#      (agent_get_animation, ":var10", ":var6", 0),
#      (neg|is_between, ":var10", 20, 26),
#      (agent_get_horse, ":var11", ":var6"),
#      (agent_get_wielded_item, ":var12", ":var6", 0),
#      (agent_get_wielded_item, ":var13", ":var6", 1),
#      (call_script, "script_doghotel_item_get_wpt", ":var12"),
#      (assign, ":var14", 0),
#      (assign, ":var15", 0),
#      (assign, ":var16", 0),
#      (assign, ":var17", 0),
#      (try_begin),
#        (troop_get_slot, ":var18", ":var7", 7),
#        (ge, ":var18", "$g_doghotel_renown_min"),
#        (val_add, ":var14", "$g_doghotel_renown_block_bonus"),
#        (val_add, ":var15", "$g_doghotel_renown_feint_bonus"),
#        (val_add, ":var16", "$g_doghotel_renown_hold_bonus"),
#        (val_add, ":var17", "$g_doghotel_renown_chamber_bonus"),
#      (try_end),
#      (try_begin),
#        (ge, ":var7", 0),
#        (store_proficiency_level, ":var19", ":var7", reg0),
#      (else_try),
#        (assign, ":var19", "$g_doghotel_min_weapon_prof"),
#      (try_end),
#      (val_clamp, ":var19", "$g_doghotel_min_weapon_prof", "$g_doghotel_max_weapon_prof"),
#      (store_sub, ":var20", ":var19", "$g_doghotel_min_weapon_prof"),
#      (try_begin),
#        (ge, ":var12", 0),
#        (item_has_property, ":var12", itp_crush_through),
#        (val_sub, ":var20", 30),
#      (try_end),
#      (val_min, ":var20", 1),
#      (try_begin),
#        (eq, ":var11", -1),
#        (neg|is_between, ":var10", 20, 26),
#        (agent_get_slot, ":var21", ":var6", 52),
#        (neq, ":var21", 1),
#        (store_sub, ":var22", "$g_doghotel_max_kick_chance", "$g_doghotel_min_kick_chance"),
#        (val_clamp, ":var22", 1, 100),
#        (store_div, ":var23", 100, ":var22"),
#        (store_div, ":var24", ":var20", ":var23"),
#        (val_add, ":var24", "$g_doghotel_min_kick_chance"),
#        (try_begin),
#          (eq, ":var12", -1),
#          (val_mul, ":var24", 2),
#        (else_try),
#          (ge, ":var13", 0),
#          (val_div, ":var24", 2),
#        (else_try),
#          (neg|item_has_capability, ":var12", itc_parry_polearm|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded),
#          (val_mul, ":var24", 2),
#        (try_end),
#        (store_random_in_range, ":var25", 0, 100),
#        (ge, ":var24", ":var25"),
#        (agent_set_slot, ":var6", 52, 1),
#      (try_end),
#      (try_begin),
#        (eq, ":var11", -1),
#        (ge, ":var12", 0),
#        (agent_get_slot, ":var26", ":var6", 35),
#        (le, ":var26", 0),
#        (item_has_capability, ":var12", itc_parry_polearm|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded),
#        (store_sub, ":var27", "$g_doghotel_max_chamber_chance", "$g_doghotel_min_chamber_chance"),
#        (val_clamp, ":var27", 1, 100),
#        (store_div, ":var23", 100, ":var27"),
#        (store_div, ":var24", ":var20", ":var23"),
#        (val_add, ":var24", "$g_doghotel_min_chamber_chance"),
#        (val_add, ":var24", ":var17"),
#        (val_sub, ":var24", ":var5"),
#        (store_random_in_range, ":var25", 0, 100),
#        (ge, ":var24", ":var25"),
#        (agent_set_slot, ":var6", 35, 1),
#      (try_end),
#      (try_begin),
#        (this_or_next|eq, ":var12", -1),
#        (this_or_next|item_has_capability, ":var12", itc_parry_polearm|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded),
#        (ge, ":var13", 0),
#        (store_sub, ":var27", "$g_doghotel_max_block_chance", "$g_doghotel_min_block_chance"),
#        (val_clamp, ":var27", 1, 100),
#        (store_div, ":var23", 100, ":var27"),
#        (store_div, ":var24", ":var20", ":var23"),
#        (val_add, ":var24", "$g_doghotel_min_block_chance"),
#        (val_add, ":var24", ":var14"),
#        (val_sub, ":var24", ":var2"),
#        (store_random_in_range, ":var25", 0, 100),
#        (ge, ":var24", ":var25"),
#        (agent_set_slot, ":var6", 38, 0),
#      (else_try),
#        (agent_set_slot, ":var6", 38, 1),
#      (try_end),
#      (try_begin),
#        (this_or_next|eq, ":var12", -1),
#        (this_or_next|item_has_capability, ":var12", itc_parry_polearm|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded),
#        (ge, ":var13", 0),
#        (eq, ":var11", -1),
#        (agent_get_slot, ":var28", ":var6", 36),
#        (store_sub, ":var29", ":var28", ":var0"),
#        (this_or_next|le, ":var28", ":var0"),
#        (neg|is_between, ":var29", 0, "$g_doghotel_max_hold_msec"),
#        (store_sub, ":var27", "$g_doghotel_max_hold_chance", "$g_doghotel_min_hold_chance"),
#        (val_clamp, ":var27", 1, 100),
#        (store_div, ":var23", 100, ":var27"),
#        (store_div, ":var24", ":var20", ":var23"),
#        (val_add, ":var24", "$g_doghotel_min_hold_chance"),
#        (val_add, ":var24", ":var16"),
#        (val_sub, ":var24", ":var3"),
#        (try_begin),
#          (eq, ":var12", -1),
#          (val_div, ":var24", 2),
#        (try_end),
#        (store_random_in_range, ":var25", 0, 100),
#        (try_begin),
#          (ge, ":var24", ":var25"),
#          (try_begin),
#            (ge, "$g_doghotel_min_hold_msec", "$g_doghotel_max_hold_msec"),
#            (assign, ":var30", "$g_doghotel_min_hold_msec"),
#          (else_try),
#            (store_random_in_range, ":var30", "$g_doghotel_min_hold_msec", "$g_doghotel_max_hold_msec"),
#          (try_end),
#          (store_add, ":var31", ":var0", ":var30"),
#          (agent_set_slot, ":var6", 36, ":var31"),
#        (else_try),
#          (agent_set_slot, ":var6", 36, 0),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":var11", -1),
#        (this_or_next|eq, ":var12", -1),
#        (item_has_capability, ":var12", itc_parry_polearm|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded),
#        (agent_get_slot, ":var32", ":var6", 37),
#        (le, ":var32", "$g_doghotel_max_consecutive_feints"),
#        (store_sub, ":var27", "$g_doghotel_max_feint_chance", "$g_doghotel_min_feint_chance"),
#        (val_clamp, ":var27", 1, 100),
#        (store_div, ":var23", 100, ":var27"),
#        (store_div, ":var24", ":var20", ":var23"),
#        (val_add, ":var24", "$g_doghotel_min_feint_chance"),
#        (val_add, ":var24", ":var15"),
#        (val_sub, ":var24", ":var4"),
#        (try_begin),
#          (eq, ":var12", -1),
#          (val_div, ":var24", 2),
#        (try_end),
#        (store_random_in_range, ":var25", 0, 100),
#        (ge, ":var24", ":var25"),
#        (val_add, ":var32", 1),
#        (agent_set_slot, ":var6", 37, ":var32"),
#      (try_end),
#    (try_end),
#  ]),
#
#  ("doghotel_distance_calculations",
#  [
#    (assign, ":var0", 0),
#    (assign, ":var1", 0),
#    (store_add, ":var2", "$g_doghotel_batch_offset", "$g_doghotel_batch_size"),
#    (try_for_agents, ":var3"),
#      (val_add, ":var0", 1),
#      (is_between, ":var0", "$g_doghotel_batch_offset", ":var2"),
#      (val_add, ":var1", 1),
#      (agent_is_active, ":var3"),
#      (agent_is_non_player, ":var3"),
#      (agent_is_human, ":var3"),
#      (agent_is_alive, ":var3"),
#      (agent_is_alarmed, ":var3"),
#      (agent_get_troop_id, ":var4", ":var3"),
#      (this_or_next|neq, "$g_doghotel_enable_only_for_heroes", 1),
#      (troop_is_hero, ":var4"),
#      (agent_get_position, pos1, ":var3"),
#      (assign, ":var5", 0),
#      (assign, ":var6", 0),
#      (assign, ":var7", -1),
#      (assign, ":var8", "$g_doghotel_nearby_enemy_radius"),
#      (assign, ":var9", -1),
#      (assign, ":var10", "$g_doghotel_nearby_enemy_radius"),
#      (assign, ":var11", -1),
#      (assign, ":var12", "$g_doghotel_nearby_enemy_radius"),
#      (assign, ":var13", -1),
#      (assign, ":var14", "$g_doghotel_nearby_neutral_radius"),
#      (assign, ":var15", -1),
#      (try_begin),
#        (agent_get_simple_behavior, ":var16", ":var3"),
#        (neq, ":var16", 5),
#        (neq, ":var16", 6),
#        (neq, ":var16", 7),
#        (try_begin),
#          (agent_ai_get_behavior_target, ":var17", ":var3"),
#          (ge, ":var17", 0),
#          (agent_is_active, ":var17"),
#          (agent_is_human, ":var17"),
#          (agent_is_alive, ":var17"),
#          (agent_get_position, pos2, ":var17"),
#          (get_distance_between_positions, ":var18", pos1, pos2),
#          (lt, ":var18", "$g_doghotel_nearby_enemy_radius"),
#          (assign, ":var15", ":var17"),
#        (else_try),
#          (agent_get_slot, ":var19", ":var3", 21),
#          (ge, ":var19", 0),
#          (agent_is_active, ":var19"),
#          (agent_is_human, ":var19"),
#          (agent_is_alive, ":var19"),
#          (assign, ":var15", ":var19"),
#        (try_end),
#      (try_end),
#      (agent_get_team, ":var20", ":var3"),
#      (try_for_agents, ":var21"),
#        (neq, ":var3", ":var21"),
#        (agent_is_human, ":var21"),
#        (agent_is_alive, ":var21"),
#        (assign, ":var22", 1),
#        (try_begin),
#          (multiplayer_is_server),
#          (eq, "$g_multiplayer_game_type", 0),
#          (assign, ":var22", 1),
#        (else_try),
#          (eq, ":var21", ":var15"),
#          (assign, ":var22", 1),
#        (else_try),
#          (agent_get_team, ":var23", ":var21"),
#          (teams_are_enemies, ":var20", ":var23"),
#          (assign, ":var22", 1),
#        (else_try),
#          (assign, ":var22", 0),
#        (try_end),
#        (try_begin),
#          (eq, ":var22", 1),
#          (try_begin),
#            (agent_get_position, pos2, ":var21"),
#            (get_distance_between_positions, ":var18", pos1, pos2),
#            (lt, ":var18", "$g_doghotel_nearby_enemy_radius"),
#            (val_add, ":var5", 1),
#            (lt, ":var18", ":var12"),
#            (position_transform_position_to_local, pos3, pos1, pos2),
#            (position_get_y, ":var24", pos3),
#            (ge, ":var24", 0),
#            (try_begin),
#              (lt, ":var18", ":var8"),
#              (assign, ":var11", ":var9"),
#              (assign, ":var9", ":var7"),
#              (assign, ":var7", ":var21"),
#              (assign, ":var12", ":var10"),
#              (assign, ":var10", ":var8"),
#              (assign, ":var8", ":var18"),
#            (else_try),
#              (lt, ":var18", ":var10"),
#              (assign, ":var11", ":var9"),
#              (assign, ":var9", ":var21"),
#              (assign, ":var12", ":var10"),
#              (assign, ":var10", ":var18"),
#            (else_try),
#              (lt, ":var18", ":var12"),
#              (assign, ":var11", ":var21"),
#              (assign, ":var12", ":var18"),
#            (try_end),
#          (try_end),
#        (try_end),
#        (try_begin),
#          (eq, ":var22", 0),
#          (multiplayer_is_server),
#          (eq, "$g_multiplayer_game_type", 7),
#          (agent_get_slot, ":var25", ":var3", 21),
#          (neq, ":var25", ":var21"),
#          (lt, ":var18", "$g_doghotel_nearby_neutral_radius"),
#          (val_add, ":var6", 1),
#          (lt, ":var18", ":var14"),
#          (try_begin),
#            (lt, ":var18", ":var14"),
#            (assign, ":var13", ":var21"),
#            (assign, ":var14", ":var18"),
#          (try_end),
#        (try_end),
#      (try_end),
#      (agent_set_slot, ":var3", 40, ":var5"),
#      (agent_set_slot, ":var3", 41, ":var6"),
#      (agent_set_slot, ":var3", 43, ":var7"),
#      (agent_set_slot, ":var3", 44, ":var9"),
#      (agent_set_slot, ":var3", 45, ":var11"),
#      (agent_set_slot, ":var3", 47, ":var13"),
#    (try_end),
#    (val_add, "$g_doghotel_batch_offset", ":var1"),
#    (try_begin),
#      (this_or_next|eq, ":var1", 0),
#      (ge, "$g_doghotel_batch_offset", ":var0"),
#      (assign, "$g_doghotel_batch_offset", 0),
#    (try_end),
#  ]),
#
#  ("doghotel_server_message",
#  [
#    (get_max_players, ":var0"),
#    (try_for_range, ":var1", 0, ":var0"),
#      (player_is_active, ":var1"),
#      (multiplayer_send_string_to_player, ":var1", 111, s1),
#    (try_end),
#    (server_add_message_to_log, s1),
#  ]),
#
#  ("doghotel_send_bot_config",
#  [
#    (store_trigger_param_1, ":var0"),
#    (try_begin),
#      (player_is_active, ":var0"),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 0, "$g_doghotel_enable_brainy_bots", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 1, "$g_doghotel_movement_actions_enabled", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 2, "$g_doghotel_batch_size", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 3, "$g_doghotel_nearby_enemy_radius", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 4, "$g_doghotel_nearby_neutral_radius", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 5, "$g_doghotel_nearby_ally_radius", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 6, "$g_doghotel_min_block_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 7, "$g_doghotel_max_block_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 8, "$g_doghotel_min_hold_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 9, "$g_doghotel_max_hold_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 10, "$g_doghotel_min_feint_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 11, "$g_doghotel_max_feint_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 12, "$g_doghotel_min_chamber_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 13, "$g_doghotel_max_chamber_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 14, "$g_doghotel_min_weapon_prof", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 15, "$g_doghotel_max_weapon_prof", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 16, "$g_doghotel_min_hold_msec", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 17, "$g_doghotel_max_hold_msec", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 18, "$g_doghotel_max_consecutive_feints", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 19, "$g_doghotel_combat_ai_poor_block_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 20, "$g_doghotel_combat_ai_poor_hold_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 21, "$g_doghotel_combat_ai_poor_feint_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 22, "$g_doghotel_combat_ai_poor_chamber_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 23, "$g_doghotel_combat_ai_average_block_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 24, "$g_doghotel_combat_ai_average_hold_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 25, "$g_doghotel_combat_ai_average_feint_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 26, "$g_doghotel_combat_ai_average_chamber_reduction", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 27, "$g_doghotel_renown_block_bonus", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 28, "$g_doghotel_renown_feint_bonus", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 29, "$g_doghotel_renown_hold_bonus", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 30, "$g_doghotel_renown_chamber_bonus", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 31, "$g_doghotel_renown_min", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 32, "$g_doghotel_combat_difficulty", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 34, "$g_doghotel_anti_autoblock", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 35, "$g_doghotel_enable_only_for_heroes", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 36, "$g_doghotel_version_id_netcode", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 37, "$g_doghotel_version_id", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 38, "$g_doghotel_min_kick_chance", 4097),
#      (multiplayer_send_3_int_to_player, ":var0", 120, 39, "$g_doghotel_max_kick_chance", 4097),
#    (try_end),
#  ]),
#
#  ("doghotel_configure_close",
#  [
#    (try_begin),
#      (is_presentation_active, "prsnt_doghotel_configure"),
#      (try_begin),
#        (is_between, "$g_doghotel_prsnt_configure_close", 1, 5),
#        (val_add, "$g_doghotel_prsnt_configure_close", 1),
#        (presentation_set_duration, 0),
#      (else_try),
#        (ge, "$g_doghotel_prsnt_configure_close", 5),
#        (call_script, "script_doghotel_error_message", "str_doghotel_unable_to_close_presentation"),
#        (assign, "$g_doghotel_prsnt_configure_close", 0),
#      (try_end),
#    (else_try),
#      (assign, "$g_doghotel_prsnt_configure_close", 0),
#    (try_end),
#  ]),
#  #Doghotel end
]