from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
	("player", 0, "player", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("player_horseman", 0, "player_horseman", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("gray_knight", 0, "knight_a", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("vaegir_knight", 0, "knight_b", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("flagbearer_a", 0, "flagbearer_a", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("flagbearer_b", 0, "flagbearer_b", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("peasant", 0, "peasant_a", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("khergit", 0, "khergit_horseman", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("khergit_horseman_b", 0, "khergit_horseman_b", 0.05, snd_gallop, 0.15, 0.173, 0.0),

	("axeman", 0, "bandit_a", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("woman", 0, "woman_a", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("woman_b", 0, "woman_b", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),
#Icons for disasters begin
		  ("disaster_volcano", mcn_no_shadow, "disaster_volcano", 1.5, 0, 0, 0, 0),
  ("disaster_earthquake", mcn_no_shadow, "disaster_earthquake", 1.5, 0, 0, 0, 0),
  ("disaster_storm", mcn_no_shadow, "disaster_storm", 1.5, 0, 0, 0, 0),
  ("disaster_typhoon", mcn_no_shadow, "disaster_typhoon", 1.5, 0, 0, 0, 0),
  ("disaster_fire", mcn_no_shadow, "disaster_fire", 1.5, 0, 0, 0, 0),
  ("disaster_sand", mcn_no_shadow, "disaster_sand", 1.5, 0, 0, 0, 0),
  ("disaster_tides", mcn_no_shadow, "disaster_tides", 1.5, 0, 0, 0, 0),
  ("disaster_ice", mcn_no_shadow, "disaster_ice", 1.5, 0, 0, 0, 0),
  ("disaster_flood", mcn_no_shadow, "disaster_flood", 1.5, 0, 0, 0, 0),
  ("disaster_blackdeath", mcn_no_shadow, "disaster_blackdeath", 1.5, 0, 0, 0, 0),
  ("disaster_malaria", mcn_no_shadow, "disaster_malaria", 1.5, 0, 0, 0, 0),
  	#("ship_on_land", mcn_no_shadow, "boat_sail_off", 0.12, snd_click, 0.0, 0.0, 0.0),
  ("disaster_riot", mcn_no_shadow, "disaster_riot", 1.5, 0, 0, 0, 0),
	#Icons for disasters end
	("town", mcn_no_shadow, "Gulltown", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("town_steppe", mcn_no_shadow, "map_town_steppe_a", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("town_desert", mcn_no_shadow, "map_town_desert_a", avatar_scale, snd_click, 0.0, 0.0, 0.0),


	
	("village_a", mcn_no_shadow, "Stoney_Sept", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_b", mcn_no_shadow, "Saltpans", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_c", mcn_no_shadow, "map_village_c", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_a", mcn_no_shadow, "map_village_burnt_a", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_a", mcn_no_shadow, "map_village_deserted_a", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_b", mcn_no_shadow, "map_village_burnt_b", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_b", mcn_no_shadow, "map_village_deserted_b", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_c", mcn_no_shadow, "map_village_burnt_c", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_c", mcn_no_shadow, "map_village_deserted_c", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_snow_a", mcn_no_shadow, "eastern_village", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_snow_burnt_a", mcn_no_shadow, "map_village_snow_burnt_a", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_snow_deserted_a", mcn_no_shadow, "map_village_snow_deserted_a", 0.1, snd_click, 0.0, 0.0, 0.0),

	("camp", mcn_no_shadow, "camp_tent", 0.07, snd_click, 0.0, 0.0, 0.0),

	("ship", mcn_no_shadow, "boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0.0),

	("ship_on_land", mcn_no_shadow, "boat_sail_off", 0.12, snd_click, 0.0, 0.0, 0.0),

	("castle_a", mcn_no_shadow, "european_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("castle_b", mcn_no_shadow, "map_castle_b", 0.13, snd_click, 0.0, 0.0, 0.0),

	("castle_c", mcn_no_shadow, "map_castle_c", 0.13, snd_click, 0.0, 0.0, 0.0),

	("castle_d", mcn_no_shadow, "map_castle_d", 0.13, snd_click, 0.0, 0.0, 0.0),

	("town_snow", mcn_no_shadow, "map_town_snow_a", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("castle_snow_a", mcn_no_shadow, "map_castle_snow_a", 0.13, snd_click, 0.0, 0.0, 0.0),

	("castle_snow_b", mcn_no_shadow, "map_castle_snow_b", 0.13, snd_click, 0.0, 0.0, 0.0),

	("mule", 0, "icon_mule", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("cattle", 0, "icon_cow", 0.05, snd_footstep_grass, 0.15, 0.173, 0.0),

	("training_ground", mcn_no_shadow, "training", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("bridge_a", mcn_no_shadow, "map_river_bridge_a", 1.27, snd_click, 0.0, 0.0, 0.0),

	("bridge_b", mcn_no_shadow, "map_river_bridge_b", 0.7, snd_click, 0.0, 0.0, 0.0),

	("bridge_snow_a", mcn_no_shadow, "map_river_bridge_snow_a", 1.27, snd_click, 0.0, 0.0, 0.0),

	("longship", 0, "map_longship", avatar_scale, snd_sea_travel, 0.0, 0.05, 0.0),

	("longship_poland", 0, "map_longship_poland", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_denmark", 0, "map_longship_denmark", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_teu", 0, "map_longship_teu", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_lithuania", 0, "map_longship_lithuania", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_hre", 0, "map_longship_hre", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_hungary", 0, "map_longship_hungary", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_novgorod", 0, "map_longship_novgorod", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_england", 0, "map_longship_england", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_france", 0, "map_longship_france", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_norway", 0, "map_longship_norway", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_scotland", 0, "map_longship_scotland", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_ireland", 0, "map_longship_ireland", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_sweden", 0, "map_longship_sweden", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_mongol", 0, "map_longship_mongol", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_galicia", 0, "map_longship_galicia", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_portugal", 0, "map_longship_portugal", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_aragon", 0, "map_longship_aragon", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_castile", 0, "map_longship_castile", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_navarra", 0, "map_longship_navarra", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_granada", 0, "map_longship_granada", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_papal", 0, "map_longship_papal", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_byzantine", 0, "map_longship_byzantine", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_jerusalem", 0, "map_longship_jerusalem", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_sicily", 0, "map_longship_sicily", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_mamluke", 0, "map_longship_mamluke", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_latin", 0, "map_longship_latin", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_ilkhanate", 0, "map_longship_ilkhanate", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_hafsid", 0, "map_longship_hafsid", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_serbia", 0, "map_longship_serbia", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_bulgaria", 0, "map_longship_bulgaria", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_marinid", 0, "map_longship_marinid", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("longship_pirate", 0, "map_longship_pirate", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("constantinople", mcn_no_shadow, "map_constantinople", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("prague", mcn_no_shadow, "map_prague", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("andalusian", mcn_no_shadow, "map_icon_andalusian", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("italy", mcn_no_shadow, "map_icon_italy", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("russian", mcn_no_shadow, "map_icon_russian", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("eastern", mcn_no_shadow, "map_icon_eastern", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("eastern2", mcn_no_shadow, "map_icon_eastern2", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("wooden", mcn_no_shadow, "map_icon_wood", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("acre", mcn_no_shadow, "map_icon_acre", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("french_town", mcn_no_shadow, "french_town", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("dutch_town", mcn_no_shadow, "dutch_town", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("dutch_castle", mcn_no_shadow, "dutch_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("european_castle", mcn_no_shadow, "european_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("french_castle", mcn_no_shadow, "french_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("norman_castle", mcn_no_shadow, "norman_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("medi_castle", mcn_no_shadow, "medi_castle", 0.13, snd_click, 0.0, 0.0, 0.0),

	("castle_icon_a", mcn_no_shadow, "castle_icon_a", 0.1, snd_click, 0.0, 0.0, 0.0),

	("rus", mcn_no_shadow, "rus_town_icon", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("manor_icon", mcn_no_shadow, "map_village_a", 0.09, snd_click, 0.0, 0.0, 0.0),

	("merc_icon", mcn_no_shadow, "camp_tent", 0.04, snd_click, 0.0, 0.0, 0.0),

	("crusaders", 0, "crusaders", 0.07, snd_footstep_grass, 0.15, 0.173, 0.0),

	("italy_new_a", mcn_no_shadow, "Norvos", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("italy_new_b", mcn_no_shadow, "Lorath", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("teutonic_town", mcn_no_shadow, "teutonic_town", avatar_scale, snd_click, 0.0, 0.0, 0.0),

	("italy_castle", mcn_no_shadow, "Dorne_Town", 0.13, snd_click, 0.0, 0.0, 0.0),

	("village_eastern", mcn_no_shadow, "eastern_village", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_italy", mcn_no_shadow, "village_italy", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_middle_europe", mcn_no_shadow, "village_middle_europe", 0.1, snd_click, 0.0, 0.0, 0.0),

	("village_byzantium", mcn_no_shadow, "village_byzantium", 0.1, snd_click, 0.0, 0.0, 0.0),

	("castle_byzantium", mcn_no_shadow, "castle_byzantium", 0.12, snd_click, 0.0, 0.0, 0.0),

	("bandit_marker", mcn_no_shadow, "map_bandit_marker", 0.1, snd_click, 0.0, 0.0, 0.0),

	("bandit_lair", mcn_no_shadow, "map_bandit_lair", 0.45, snd_click, 0.0, 0.0, 0.0),

	("custom_banner_01", 0, "custom_map_banner_01", 0.25, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("custom_banner_02", 0, "custom_map_banner_02", 0.25, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("custom_banner_03", 0, "custom_map_banner_03", 0.25, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("banner_01", 0, "map_flag_01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_02", 0, "map_flag_02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_03", 0, "map_flag_03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_04", 0, "map_flag_04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_05", 0, "map_flag_05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_06", 0, "map_flag_06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_07", 0, "map_flag_07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_08", 0, "map_flag_08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_09", 0, "map_flag_09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_10", 0, "map_flag_10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_11", 0, "map_flag_11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_12", 0, "map_flag_12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_13", 0, "map_flag_13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_14", 0, "map_flag_14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_15", 0, "map_flag_15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_16", 0, "map_flag_16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_17", 0, "map_flag_17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_18", 0, "map_flag_18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_19", 0, "map_flag_19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_20", 0, "map_flag_20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_21", 0, "map_flag_21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_22", 0, "map_flag_22", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_23", 0, "map_flag_23", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_24", 0, "map_flag_24", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_25", 0, "map_flag_25", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_26", 0, "map_flag_26", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_27", 0, "map_flag_27", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_28", 0, "map_flag_28", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_29", 0, "map_flag_29", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_30", 0, "map_flag_30", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_31", 0, "map_flag_31", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_32", 0, "map_flag_32", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_33", 0, "map_flag_33", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_34", 0, "map_flag_34", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_35", 0, "map_flag_35", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_36", 0, "map_flag_36", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_37", 0, "map_flag_37", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_38", 0, "map_flag_38", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_39", 0, "map_flag_39", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_40", 0, "map_flag_40", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_41", 0, "map_flag_41", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_42", 0, "map_flag_42", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_43", 0, "map_flag_43", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_44", 0, "map_flag_44", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_45", 0, "map_flag_45", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_46", 0, "map_flag_46", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_47", 0, "map_flag_47", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_48", 0, "map_flag_48", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_49", 0, "map_flag_49", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_50", 0, "map_flag_50", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_51", 0, "map_flag_51", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_52", 0, "map_flag_52", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_53", 0, "map_flag_53", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_54", 0, "map_flag_54", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_55", 0, "map_flag_55", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_56", 0, "map_flag_56", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_57", 0, "map_flag_57", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_58", 0, "map_flag_58", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_59", 0, "map_flag_59", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_60", 0, "map_flag_60", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_61", 0, "map_flag_61", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_62", 0, "map_flag_62", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_63", 0, "map_flag_63", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_64", 0, "map_flag_d01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_65", 0, "map_flag_d02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_66", 0, "map_flag_d03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_67", 0, "map_flag_d04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_68", 0, "map_flag_d05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_69", 0, "map_flag_d06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_70", 0, "map_flag_d07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_71", 0, "map_flag_d08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_72", 0, "map_flag_d09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_73", 0, "map_flag_d10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_74", 0, "map_flag_d11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_75", 0, "map_flag_d12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_76", 0, "map_flag_d13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_77", 0, "map_flag_d14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_78", 0, "map_flag_d15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_79", 0, "map_flag_d16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_80", 0, "map_flag_d17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_81", 0, "map_flag_d18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_82", 0, "map_flag_d19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_83", 0, "map_flag_d20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_84", 0, "map_flag_d21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_85", 0, "map_flag_e01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_86", 0, "map_flag_e02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_87", 0, "map_flag_e03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_88", 0, "map_flag_e04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_89", 0, "map_flag_e05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_90", 0, "map_flag_e06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_91", 0, "map_flag_e07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_92", 0, "map_flag_e08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_93", 0, "map_flag_e09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_94", 0, "map_flag_e10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_95", 0, "map_flag_e11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_96", 0, "map_flag_e12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_97", 0, "map_flag_e13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_98", 0, "map_flag_e14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_99", 0, "map_flag_e15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_100", 0, "map_flag_e16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_101", 0, "map_flag_e17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_102", 0, "map_flag_e18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_103", 0, "map_flag_e19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_104", 0, "map_flag_e20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_105", 0, "map_flag_e21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_106", 0, "map_flag_f01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_107", 0, "map_flag_f02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_108", 0, "map_flag_f03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_109", 0, "map_flag_f04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_110", 0, "map_flag_f05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_111", 0, "map_flag_f06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_112", 0, "map_flag_f07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_113", 0, "map_flag_f08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_114", 0, "map_flag_f09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_115", 0, "map_flag_f10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_116", 0, "map_flag_f11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_117", 0, "map_flag_f12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_118", 0, "map_flag_f13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_119", 0, "map_flag_f14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_120", 0, "map_flag_f15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_121", 0, "map_flag_f16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_122", 0, "map_flag_f17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_123", 0, "map_flag_f18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_124", 0, "map_flag_f19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_125", 0, "map_flag_f20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_126", 0, "map_flag_f21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_127", 0, "map_flag_g01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_128", 0, "map_flag_g02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_129", 0, "map_flag_g03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_130", 0, "map_flag_g04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_131", 0, "map_flag_g05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_132", 0, "map_flag_g06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_133", 0, "map_flag_g07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_134", 0, "map_flag_g08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_135", 0, "map_flag_g09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_136", 0, "map_flag_g10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_137", 0, "map_flag_g11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_138", 0, "map_flag_g12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_139", 0, "map_flag_g13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_140", 0, "map_flag_g14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_141", 0, "map_flag_g15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_142", 0, "map_flag_g16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_143", 0, "map_flag_g17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_144", 0, "map_flag_g18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_145", 0, "map_flag_g19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_146", 0, "map_flag_g20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_147", 0, "map_flag_g21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_148", 0, "map_flag_h01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_149", 0, "map_flag_h02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_150", 0, "map_flag_h03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_151", 0, "map_flag_h04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_152", 0, "map_flag_h05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_153", 0, "map_flag_h06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_154", 0, "map_flag_h07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_155", 0, "map_flag_h08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_156", 0, "map_flag_h09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_157", 0, "map_flag_h10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_158", 0, "map_flag_h11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_159", 0, "map_flag_h12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_160", 0, "map_flag_h13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_161", 0, "map_flag_h14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_162", 0, "map_flag_h15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_163", 0, "map_flag_h16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_164", 0, "map_flag_h17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_165", 0, "map_flag_h18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_166", 0, "map_flag_h19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_167", 0, "map_flag_h20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_168", 0, "map_flag_h21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_169", 0, "map_flag_i01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_170", 0, "map_flag_i02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_171", 0, "map_flag_i03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_172", 0, "map_flag_i04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_173", 0, "map_flag_i05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_174", 0, "map_flag_i06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_175", 0, "map_flag_i07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_176", 0, "map_flag_i08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_177", 0, "map_flag_i09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_178", 0, "map_flag_i10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_179", 0, "map_flag_i11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_180", 0, "map_flag_i12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_181", 0, "map_flag_i13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_182", 0, "map_flag_i14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_183", 0, "map_flag_i15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_184", 0, "map_flag_i16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_185", 0, "map_flag_i17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_186", 0, "map_flag_i18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_187", 0, "map_flag_i19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_188", 0, "map_flag_i20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_189", 0, "map_flag_i21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_190", 0, "map_flag_j01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_191", 0, "map_flag_j02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_192", 0, "map_flag_j03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_193", 0, "map_flag_j04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_194", 0, "map_flag_j05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_195", 0, "map_flag_j06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_196", 0, "map_flag_j07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_197", 0, "map_flag_j08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_198", 0, "map_flag_j09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_199", 0, "map_flag_j10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_200", 0, "map_flag_j11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_201", 0, "map_flag_j12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_202", 0, "map_flag_j13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_203", 0, "map_flag_j14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_204", 0, "map_flag_j15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_205", 0, "map_flag_j16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_206", 0, "map_flag_j17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_207", 0, "map_flag_j18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_208", 0, "map_flag_j19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_209", 0, "map_flag_j20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_210", 0, "map_flag_j21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_211", 0, "map_flag_k01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_212", 0, "map_flag_k02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_213", 0, "map_flag_k03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_214", 0, "map_flag_k04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_215", 0, "map_flag_k05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_216", 0, "map_flag_k06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_217", 0, "map_flag_k07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_218", 0, "map_flag_k08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_219", 0, "map_flag_k09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_220", 0, "map_flag_k10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_221", 0, "map_flag_k11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_222", 0, "map_flag_k12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_223", 0, "map_flag_k13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_224", 0, "map_flag_k14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_225", 0, "map_flag_k15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_226", 0, "map_flag_k16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_227", 0, "map_flag_k17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_228", 0, "map_flag_k18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_229", 0, "map_flag_k19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_230", 0, "map_flag_k20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_231", 0, "map_flag_k21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_232", 0, "map_flag_l01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_233", 0, "map_flag_l02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_234", 0, "map_flag_l03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_235", 0, "map_flag_l04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_236", 0, "map_flag_l05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_237", 0, "map_flag_l06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_238", 0, "map_flag_l07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_239", 0, "map_flag_l08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_240", 0, "map_flag_l09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_241", 0, "map_flag_l10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_242", 0, "map_flag_l11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_243", 0, "map_flag_l12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_244", 0, "map_flag_l13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_245", 0, "map_flag_l14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_246", 0, "map_flag_l15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_247", 0, "map_flag_l16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_248", 0, "map_flag_l17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_249", 0, "map_flag_l18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_250", 0, "map_flag_l19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_251", 0, "map_flag_l20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_252", 0, "map_flag_l21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_253", 0, "map_flag_m01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_254", 0, "map_flag_m02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_255", 0, "map_flag_m03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_256", 0, "map_flag_m04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_257", 0, "map_flag_m05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_258", 0, "map_flag_m06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_259", 0, "map_flag_m07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_260", 0, "map_flag_m08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_261", 0, "map_flag_m09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_262", 0, "map_flag_m10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_263", 0, "map_flag_m11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_264", 0, "map_flag_m12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_265", 0, "map_flag_m13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_266", 0, "map_flag_m14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_267", 0, "map_flag_m15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_268", 0, "map_flag_m16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_269", 0, "map_flag_m17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_270", 0, "map_flag_m18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_271", 0, "map_flag_m19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_272", 0, "map_flag_m20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_273", 0, "map_flag_m21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_274", 0, "map_flag_n01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_275", 0, "map_flag_n02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_276", 0, "map_flag_n03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_277", 0, "map_flag_n04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_278", 0, "map_flag_n05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_279", 0, "map_flag_n06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_280", 0, "map_flag_n07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_281", 0, "map_flag_n08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_282", 0, "map_flag_n09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_283", 0, "map_flag_n10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_284", 0, "map_flag_n11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_285", 0, "map_flag_n12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_286", 0, "map_flag_n13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_287", 0, "map_flag_n14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_288", 0, "map_flag_n15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_289", 0, "map_flag_n16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_290", 0, "map_flag_n17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_291", 0, "map_flag_n18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_292", 0, "map_flag_n19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_293", 0, "map_flag_n20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_294", 0, "map_flag_n21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_295", 0, "map_flag_o01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_296", 0, "map_flag_o02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_297", 0, "map_flag_o03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_298", 0, "map_flag_o04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_299", 0, "map_flag_o05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_300", 0, "map_flag_o06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_301", 0, "map_flag_o07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_302", 0, "map_flag_o08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_303", 0, "map_flag_o09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_304", 0, "map_flag_o10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_305", 0, "map_flag_o11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_306", 0, "map_flag_o12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_307", 0, "map_flag_o13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_308", 0, "map_flag_o14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_309", 0, "map_flag_o15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_310", 0, "map_flag_o16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_311", 0, "map_flag_o17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_312", 0, "map_flag_o18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_313", 0, "map_flag_o19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_314", 0, "map_flag_o20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_315", 0, "map_flag_o21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_316", 0, "map_flag_p01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_317", 0, "map_flag_p02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_318", 0, "map_flag_p03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_319", 0, "map_flag_p04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_320", 0, "map_flag_p05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_321", 0, "map_flag_p06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_322", 0, "map_flag_p07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_323", 0, "map_flag_p08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_324", 0, "map_flag_p09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_325", 0, "map_flag_p10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_326", 0, "map_flag_p11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_327", 0, "map_flag_p12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_328", 0, "map_flag_p13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_329", 0, "map_flag_p14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_330", 0, "map_flag_p15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_331", 0, "map_flag_p16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_332", 0, "map_flag_p17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_333", 0, "map_flag_p18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_334", 0, "map_flag_p19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_335", 0, "map_flag_p20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_336", 0, "map_flag_p21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_337", 0, "map_flag_q01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_338", 0, "map_flag_q02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_339", 0, "map_flag_q03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_340", 0, "map_flag_q04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_341", 0, "map_flag_q05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_342", 0, "map_flag_q06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_343", 0, "map_flag_q07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_344", 0, "map_flag_q08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_345", 0, "map_flag_q09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_346", 0, "map_flag_q10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_347", 0, "map_flag_q11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_348", 0, "map_flag_q12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_349", 0, "map_flag_q13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_350", 0, "map_flag_q14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_351", 0, "map_flag_q15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_352", 0, "map_flag_q16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_353", 0, "map_flag_q17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_354", 0, "map_flag_q18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_355", 0, "map_flag_q19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_356", 0, "map_flag_q20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_357", 0, "map_flag_q21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_358", 0, "map_flag_r01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_359", 0, "map_flag_r02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_360", 0, "map_flag_r03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_361", 0, "map_flag_r04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_362", 0, "map_flag_r05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_363", 0, "map_flag_r06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_364", 0, "map_flag_r07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_365", 0, "map_flag_r08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_366", 0, "map_flag_r09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_367", 0, "map_flag_r10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_368", 0, "map_flag_r11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_369", 0, "map_flag_r12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_370", 0, "map_flag_r13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_371", 0, "map_flag_r14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_372", 0, "map_flag_r15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_373", 0, "map_flag_r16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_374", 0, "map_flag_r17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_375", 0, "map_flag_r18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_376", 0, "map_flag_r19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_377", 0, "map_flag_r20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_378", 0, "map_flag_r21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_379", 0, "map_flag_s01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_380", 0, "map_flag_s02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_381", 0, "map_flag_s03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_382", 0, "map_flag_s04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_383", 0, "map_flag_s05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_384", 0, "map_flag_s06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_385", 0, "map_flag_s07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_386", 0, "map_flag_s08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_387", 0, "map_flag_s09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_388", 0, "map_flag_s10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_389", 0, "map_flag_s11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_390", 0, "map_flag_s12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_391", 0, "map_flag_s13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_392", 0, "map_flag_s14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_393", 0, "map_flag_s15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_394", 0, "map_flag_s16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_395", 0, "map_flag_s17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_396", 0, "map_flag_s18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_397", 0, "map_flag_s19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_398", 0, "map_flag_s20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_399", 0, "map_flag_s21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_400", 0, "map_flag_t01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_401", 0, "map_flag_t02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_402", 0, "map_flag_t03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_403", 0, "map_flag_t04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_404", 0, "map_flag_t05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_405", 0, "map_flag_t06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_406", 0, "map_flag_t07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_407", 0, "map_flag_t08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_408", 0, "map_flag_t09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_409", 0, "map_flag_t10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_410", 0, "map_flag_t11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_411", 0, "map_flag_t12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_412", 0, "map_flag_t13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_413", 0, "map_flag_t14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_414", 0, "map_flag_t15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_415", 0, "map_flag_t16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_416", 0, "map_flag_t17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_417", 0, "map_flag_t18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_418", 0, "map_flag_t19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_419", 0, "map_flag_t20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_420", 0, "map_flag_t21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_421", 0, "map_flag_u01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_422", 0, "map_flag_u02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_423", 0, "map_flag_u03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_424", 0, "map_flag_u04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_425", 0, "map_flag_u05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_426", 0, "map_flag_u06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_427", 0, "map_flag_u07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_428", 0, "map_flag_u08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_429", 0, "map_flag_u09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_430", 0, "map_flag_u10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_431", 0, "map_flag_u11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_432", 0, "map_flag_u12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_433", 0, "map_flag_u13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_434", 0, "map_flag_u14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_435", 0, "map_flag_u15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_436", 0, "map_flag_u16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_437", 0, "map_flag_u17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_438", 0, "map_flag_u18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_439", 0, "map_flag_u19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_440", 0, "map_flag_u20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_441", 0, "map_flag_u21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_442", 0, "map_flag_v01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_443", 0, "map_flag_v02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_444", 0, "map_flag_v03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_445", 0, "map_flag_v04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_446", 0, "map_flag_v05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_447", 0, "map_flag_v06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_448", 0, "map_flag_v07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_449", 0, "map_flag_v08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_450", 0, "map_flag_v09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_451", 0, "map_flag_v10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_452", 0, "map_flag_v11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_453", 0, "map_flag_v12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_454", 0, "map_flag_v13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_455", 0, "map_flag_v14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_456", 0, "map_flag_v15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_457", 0, "map_flag_v16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_458", 0, "map_flag_v17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_459", 0, "map_flag_v18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_460", 0, "map_flag_v19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_461", 0, "map_flag_v20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_462", 0, "map_flag_v21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_463", 0, "map_flag_x01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_464", 0, "map_flag_x02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_465", 0, "map_flag_x03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_466", 0, "map_flag_x04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_467", 0, "map_flag_x05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_468", 0, "map_flag_x06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_469", 0, "map_flag_x07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_470", 0, "map_flag_x08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_471", 0, "map_flag_x09", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_472", 0, "map_flag_x10", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_473", 0, "map_flag_x11", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_474", 0, "map_flag_x12", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_475", 0, "map_flag_x13", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_476", 0, "map_flag_x14", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_477", 0, "map_flag_x15", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_478", 0, "map_flag_x16", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_479", 0, "map_flag_x17", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_480", 0, "map_flag_x18", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_481", 0, "map_flag_x19", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_482", 0, "map_flag_x20", 0.25, snd_click, 0.0, 0.0, 0.0),

	("banner_483", 0, "map_flag_x21", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_1", 0, "map_flag_f01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_2", 0, "map_flag_g01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_3", 0, "map_flag_h01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_4", 0, "map_flag_i01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_5", 0, "map_flag_j01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_6", 0, "map_flag_k01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_7", 0, "map_flag_l01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_8", 0, "map_flag_m01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_9", 0, "map_flag_n01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_10", 0, "map_flag_o01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_11", 0, "map_flag_p01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_12", 0, "map_flag_q01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_13", 0, "map_flag_r01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_14", 0, "map_flag_s01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_15", 0, "map_flag_v01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_16", 0, "map_flag_x01", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_17", 0, "map_flag_x02", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_18", 0, "map_flag_x03", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_19", 0, "map_flag_x04", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_20", 0, "map_flag_x05", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_21", 0, "map_flag_x06", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_22", 0, "map_flag_x07", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_23", 0, "map_flag_x08", 0.25, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_24", 0, "map_flag_x09", 0.25, snd_click, 0.0, 0.0, 0.0),

	# LAV MODIFICATIONS START (SIEGE CAMP ICON MINI-MOD)
  ("castle_besieged", mcn_no_shadow, "castle_a_spike_siege_combined", 0.65, 0),
# LAV MODIFICATIONS END (SIEGE CAMP ICON MINI-MOD)

### Insert anywhere in the list of map icons.

################################################################################
# LAV MODIFICATIONS START (EMOTICON MOD)
################################################################################

#    # Emoticons by Mandible start here
#    ("emo_cattle_normal", mcn_no_shadow, "icon_wheat",    1.0, 0),
#    ("emo_peasant_flee",  mcn_no_shadow, "icon_wolf",     1.0, 0),
#    ("emo_std_patrol",    mcn_no_shadow, "icon_patrol",   1.0, 0),
#    ("emo_std_flee",      mcn_no_shadow, "icon_flag",     1.0, 0),
#    ("emo_std_attack",    mcn_no_shadow, "icon_sword",    1.0, 0),
#    ("emo_bandit_patrol", mcn_no_shadow, "icon_mask",     1.0, 0),
#    ("emo_bandit_attack", mcn_no_shadow, "icon_axe",      1.0, 0),
#    ("emo_bandit_return", mcn_no_shadow, "icon_loot",     1.0, 0),
#    ("emo_bandit_flee",   mcn_no_shadow, "icon_rope",     1.0, 0),
#    ("emo_std_profit",    mcn_no_shadow, "icon_coins",    1.0, 0),
#    ("emo_std_return",    mcn_no_shadow, "icon_beer",     1.0, 0),
#    ("emo_lord_feast",    mcn_no_shadow, "icon_wine",     1.0, 0),
#    ("emo_lord_village",  mcn_no_shadow, "icon_house",    1.0, 0),
#    ("emo_lord_siege",    mcn_no_shadow, "icon_siege",    1.0, 0),
#    ("emo_lord_raid",     mcn_no_shadow, "icon_raid",     1.0, 0),
#    ("emo_lord_escort",   mcn_no_shadow, "icon_patrol",   1.0, 0),
#    ("emo_lord_marshall", mcn_no_shadow, "icon_crown",    1.0, 0),
#    ("emo_espionage",     mcn_no_shadow, "icon_spy",      1.0, 0),
#    ("emo_unhappy",       mcn_no_shadow, "icon_unhappy",  1.0, 0),
#    ("emo_std_thinking",  mcn_no_shadow, "icon_question", 1.0, 0),
#    ("emo_slaver_attack", mcn_no_shadow, "icon_chain",    1.0, 0),

################################################################################
# LAV MODIFICATIONS START (EMOTICON MOD)
################################################################################

]