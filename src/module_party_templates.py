from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
	("none", "none", icon_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("rescued_prisoners", "Rescued Prisoners", icon_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("enemy", "Enemy", icon_gray_knight|pf_label_small, 0, fac_undeads, courage_7|merchant_personality, []),

	("hero_party", "Hero Party", icon_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("village_defenders", "Village Defenders", icon_peasant|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, [(trp_farmer, 10, 20), (trp_peasant_woman, 0, 4)]),

	("cattle_herd", "Cattle Herd", icon_cattle|carries_goods(10)|pf_label_small, 0, fac_neutral, courage_11|escorted_merchant_personality, [(trp_cattle, 80, 120)]),

	("looters", "Looters", icon_axeman|carries_goods(8)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_looter, 15, 50)]),

	("manhunters", "Manhunters", icon_gray_knight|pf_label_small, 0, fac_manhunters, soldier_personality, [(trp_manhunter, 9, 40)]),

	("curonians", "Curonians", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_kingdom_35, soldier_personality, [(trp_balt_skirmisher, 7, 10), (trp_balt_footman, 7, 10), (trp_balt_jav, 7, 10), (trp_balt_veteran_jav, 1, 4), (trp_balt_billman, 7, 10), (trp_balt_spearman, 7, 10)]),

	("prussians", "Prussians", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_kingdom_34, soldier_personality, [(trp_balt_skirmisher, 7, 10), (trp_balt_footman, 7, 10), (trp_balt_jav, 7, 10), (trp_balt_veteran_jav, 1, 4), (trp_balt_billman, 7, 10), (trp_balt_spearman, 7, 10)]),

	("samogitians", "Samogitians", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_kingdom_36, soldier_personality, [(trp_balt_skirmisher, 7, 10), (trp_balt_footman, 7, 10), (trp_balt_jav, 7, 10), (trp_balt_veteran_jav, 1, 4), (trp_balt_billman, 7, 10), (trp_balt_spearman, 7, 10)]),

	("yotvingians", "Yotvingians", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_kingdom_33, soldier_personality, [(trp_balt_skirmisher, 7, 10), (trp_balt_footman, 7, 10), (trp_balt_jav, 7, 10), (trp_balt_veteran_jav, 1, 4), (trp_balt_billman, 7, 10), (trp_balt_spearman, 7, 10)]),

	("welsh", "Welsh", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_kingdom_37, soldier_personality, [(trp_merc_welsh_bowman, 24, 31)]),

	("guelphs", "Guelphs", icon_gray_knight|pf_label_small, 0, fac_kingdom_40, soldier_personality, [(trp_iberian_knight, 1, 8), (trp_iberian_billman, 15, 30), (trp_iberian_veteran_crossbowman, 10, 15), (trp_iberian_veteran_spearman, 10, 15), (trp_iberian_light_cavalry, 10, 15)]),

	("ghibellines", "Ghibellines", icon_gray_knight|pf_label_small, 0, fac_kingdom_41, soldier_personality, [(trp_iberian_knight, 1, 4), (trp_merc_euro_guisarmer, 10, 15), (trp_merc_euro_range, 10, 15), (trp_merc_euro_spearman, 10, 15), (trp_iberian_light_cavalry, 10, 15)]),

	("crusaders", "Crusaders", icon_crusaders|pf_label_small, 0, fac_crusade, soldier_personality, [(trp_euro_horse_4, 10, 25), (trp_euro_spearman_2, 150, 200), (trp_merc_euro_range, 50, 100), (trp_merc_euro_guisarmer, 50, 100), (trp_merc_euro_spearman, 50, 100), (trp_merc_euro_horse, 25, 50)]),

	("merc_party", "Angry band of alchoholics", icon_gray_knight|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("crusader_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0, fac_kingdom_23, soldier_personality, [(trp_iberian_knight, 1, 4), (trp_iberian_light_cavalry, 5, 10), (trp_iberian_town_footman_1, 10, 15), (trp_iberian_veteran_spearman, 5, 8), (trp_iberian_veteran_crossbowman, 5, 15), (trp_iberian_billman, 1, 10)]),

	("jihadist_raiders", "Jihadists", icon_khergit|pf_show_faction, 0, fac_kingdom_25, soldier_personality, [(trp_bedouin_spearman, 8, 20), (trp_halqa_archer, 5, 8), (trp_bedouin_cav_2, 4, 10), (trp_halqa_cav_2, 1, 3), (trp_mamluke_turkoman_2, 10, 15)]),

	("teutonic_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0, fac_kingdom_1, soldier_personality, [(trp_teu_horse_3, 1, 3), (trp_teu_town_2_2, 2, 6), (trp_teu_ger_1, 3, 10), (trp_teu_ger_2_1, 5, 10), (trp_teu_town_2_1, 10, 16), (trp_teu_town_3_2, 5, 8)]),

	("manor", "Manor", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("farm", "Farm", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("linen", "Linen Workshop", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("salt", "Salt Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("furs", "Hunter", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("iron", "Iron Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("silk", "Silk Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("iron_mine", "Iron Mine", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("salt_mine", "Salt Mine", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("weapon", "Weapon Smithy", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("armor", "Armor Smithy", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("fletchery", "Fletchery", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),

	("breeder", "Horse Breeder", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, soldier_personality, []),

	("monastery", "Monastery", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, soldier_personality, []),

	("peasant_rebels_euro", "Peasant Rebels", icon_peasant|pf_label_small, 0, fac_peasant_rebels, soldier_personality, []),

	("steppe_bandits", "Steppe Bandits", icon_khergit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit, 15, 58)]),

	("taiga_bandits", "Taiga Bandits", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit, 15, 58)]),

	("desert_bandits", "Desert Bandits", icon_vaegir_knight|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_desert_bandit, 15, 58)]),

	("forest_bandits", "Forest Bandits", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_forest_bandit, 15, 52)]),

	("mountain_bandits", "Mountain Bandits", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_mountain_bandit, 15, 60)]),

	("sea_raiders", "Pirates", icon_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_sea_raider, 20, 50)]),

	("robber_knights", "Roving Robber Knight Band", icon_axeman|carries_goods(8)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_euro_horse_4, 1, 2), (trp_raider, 5, 12)]),

	("deserters", "Deserters", icon_vaegir_knight|carries_goods(3)|pf_label_small, 0, fac_deserters, bandit_personality, []),

	("merchant_caravan", "Merchant Caravan", icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_merc_euro_horse, 5, 15)]),

	("troublesome_bandits", "Troublesome Bandits", icon_axeman|carries_goods(9)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit, 14, 55)]),

	("bandits_awaiting_ransom", "Bandits Awaiting Ransom", icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit, 24, 58), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),

	("kidnapped_girl", "Kidnapped Girl", icon_woman|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_kidnapped_girl, 1, 1)]),

	("village_farmers", "Village Farmers", icon_peasant|pf_civilian, 0, fac_innocents, courage_7|merchant_personality, [(trp_farmer, 8, 18)]),

	("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy_partner, 1, 1), (trp_merc_euro_horse, 5, 11)]),

	("runaway_serfs", "Runaway Serfs", icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_farmer, 6, 7), (trp_peasant_woman, 3, 3)]),

	("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy, 1, 1)]),

	("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, []),

	("forager_party", "Foraging Party", icon_gray_knight|carries_goods(5)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("scout_party", "Scouts", icon_gray_knight|carries_goods(1)|pf_show_faction, 0, fac_commoners, bandit_personality, []),

	("patrol_party", "Patrol", icon_gray_knight|carries_goods(2)|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("messenger_party", "Messenger", icon_gray_knight|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("raider_party", "Raiders", icon_gray_knight|carries_goods(16)|pf_quest_party, 0, fac_commoners, bandit_personality, []),

	("raider_captives", "Raider Captives", icon_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_peasant_woman, 6, 30, pmf_is_prisoner)]),

	("kingdom_caravan_party", "Caravan", icon_mule|carries_goods(45)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1), (trp_merc_euro_horse, 1, 8)]),

	("prisoner_train_party", "Prisoner Train", icon_gray_knight|carries_goods(5)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("default_prisoners", "Default Prisoners", icon_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_bandit, 5, 10, pmf_is_prisoner)]),

	("routed_warriors", "Routed Enemies", icon_vaegir_knight|pf_label_small, 0, fac_commoners, soldier_personality, []),

	("center_reinforcements", "Reinforcements", icon_axeman|carries_goods(16)|pf_label_small, 0, fac_commoners, soldier_personality, [(trp_merc_euro_spearman, 9, 50)]),

	("kingdom_hero_party", "War Party", icon_flagbearer_a|pf_default_behavior|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("kingdom_teutonic_reinforcements_a", "{!}kingdom teutonic reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_1, soldier_personality, [(trp_teu_horse_1, 1, 3), (trp_teu_village_recruit, 4, 9), (trp_teu_town_1, 4, 9)]),

	("kingdom_teutonic_reinforcements_b", "{!}kingdom teutonic reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_1, soldier_personality, [(trp_teu_town_2_2, 2, 6), (trp_teu_ger_1, 1, 3), (trp_teu_balt_1, 1, 3), (trp_teu_town_2_1, 1, 3)]),

	("kingdom_teutonic_reinforcements_c", "{!}kingdom teutonic reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_1, soldier_personality, [(trp_teu_horse_4, 3, 6)]),

	("kingdom_baltic_reinforcements_a", "{!}kingdom baltic reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_2, soldier_personality, [(trp_balt_noble_recruit, 1, 3), (trp_balt_skirmisher, 4, 10), (trp_balt_footman, 4, 8)]),

	("kingdom_baltic_reinforcements_b", "{!}kingdom baltic reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_2, soldier_personality, [(trp_balt_archer, 1, 3), (trp_balt_jav, 1, 3), (trp_balt_veteran_jav, 1, 3), (trp_balt_billman, 1, 3), (trp_balt_spearman, 1, 3), (trp_balt_noble_1, 1, 3)]),

	("kingdom_baltic_reinforcements_c", "{!}kingdom baltic reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_2, soldier_personality, [(trp_balt_medium_cavalry, 1, 2), (trp_balt_noble_3, 1, 3)]),

	("kingdom_mongol_reinforcements_a", "{!}kingdom mongol reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_skirmisher, 5, 14), (trp_tatar_tribesman, 3, 7)]),

	("kingdom_mongol_reinforcements_b", "{!}kingdom mongol reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_horse_archer, 3, 8), (trp_tatar_horseman, 1, 5), (trp_tatar_lancer, 1, 2)]),

	("kingdom_mongol_reinforcements_c", "{!}kingdom mongol reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_veteran_horse_archer, 1, 2), (trp_tatar_heavy_lancer, 1, 1)]),

	("kingdom_nordic_reinforcements_a", "{!}kingdom nordic reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_village_recruit, 5, 12), (trp_nordic_town_recruit, 6, 9)]),

	("kingdom_nordic_reinforcements_b", "{!}kingdom nordic reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_veteran_archer, 1, 2), (trp_nordic_crossbowman, 1, 3), (trp_nordic_billman, 1, 3), (trp_nordic_veteran_spearman, 1, 3), (trp_nordic_spearman, 1, 3)]),

	("kingdom_nordic_reinforcements_c", "{!}kingdom nordic reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_knight, 1, 2), (trp_nordic_swords_sergeant, 2, 3)]),

	("kingdom_western_reinforcements_a", "{!}kingdom western reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_5, soldier_personality, [(trp_euro_horse_1, 3, 7), (trp_euro_village_recruit, 3, 7), (trp_euro_town_recruit, 3, 7)]),

	("kingdom_western_reinforcements_b", "{!}kingdom western reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_5, soldier_personality, [(trp_euro_archer_2, 1, 3), (trp_euro_xbow_2, 1, 3), (trp_euro_guisarm_2, 1, 3), (trp_euro_spearman_3, 1, 3), (trp_euro_spearman_2, 1, 3)]),

	("kingdom_western_reinforcements_c", "{!}kingdom western reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_5, soldier_personality, [(trp_euro_horse_2, 2, 5)]),

	("kingdom_rus_reinforcements_a", "{!}kingdom rus reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_8, soldier_personality, [(trp_rus_horse_1, 1, 3), (trp_rus_vil_1, 6, 13), (trp_rus_town_1, 2, 5)]),

	("kingdom_rus_reinforcements_b", "{!}kingdom rus reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_8, soldier_personality, [(trp_rus_vil_3_2, 2, 6), (trp_rus_vil_3_1, 1, 3), (trp_rus_town_4_2, 1, 3), (trp_rus_town_3_2, 1, 3)]),

	("kingdom_rus_reinforcements_c", "{!}kingdom rus reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_8, soldier_personality, [(trp_rus_horse_2, 1, 2), (trp_rus_horse_4, 1, 3)]),

	("kingdom_scot_reinforcements_a", "{!}kingdom scot reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_12, soldier_personality, [(trp_euro_horse_1, 1, 3), (trp_scottish_village_recruit, 4, 9), (trp_euro_town_recruit, 4, 9)]),

	("kingdom_scot_reinforcements_b", "{!}kingdom scot reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_12, soldier_personality, [(trp_euro_archer_2, 1, 3), (trp_euro_xbow_2, 1, 3), (trp_scottish_clansman, 1, 3), (trp_euro_spearman_2, 1, 3), (trp_scottish_forinsec_spearman, 1, 3)]),

	("kingdom_scot_reinforcements_c", "{!}kingdom scot reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_12, soldier_personality, [(trp_euro_horse_2, 2, 5)]),

	("kingdom_gaelic_reinforcements_a", "{!}kingdom gaelic reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_light_cavalry, 1, 3), (trp_gaelic_village_recruit, 4, 9), (trp_gaelic_village_recruit, 4, 9)]),

	("kingdom_gaelic_reinforcements_b", "{!}kingdom gaelic reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_archer_1, 1, 3), (trp_gaelic_archer_2, 1, 3), (trp_gaelic_infantry_2, 1, 3), (trp_gaelic_spearman_2, 1, 3), (trp_merc_gaelic_spearman, 1, 3)]),

	("kingdom_gaelic_reinforcements_c", "{!}kingdom gaelic reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_knight, 2, 5)]),

	("kingdom_iberain_reinforcements_a", "{!}kingdom iberain reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_light_cavalry, 1, 3), (trp_iberian_village_recruit, 4, 9), (trp_iberian_town_recruit, 4, 9)]),

	("kingdom_iberain_reinforcements_b", "{!}kingdom iberain reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_archer, 1, 3), (trp_iberian_veteran_crossbowman, 1, 3), (trp_iberian_billman, 1, 3), (trp_iberian_spears_sergeant, 1, 3), (trp_iberian_veteran_spearman, 1, 3)]),

	("kingdom_iberain_reinforcements_c", "{!}kingdom iberain reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_knight, 2, 5)]),

	("kingdom_italian_reinforcements_a", "{!}kingdom italian reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_40, soldier_personality, [(trp_italian_light_cavalry, 1, 3), (trp_italian_village_recruit, 4, 9), (trp_italian_town_recruit, 4, 9)]),

	("kingdom_italian_reinforcements_b", "{!}kingdom italian reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_40, soldier_personality, [(trp_italian_archer, 1, 3), (trp_italian_veteran_crossbowman, 1, 3), (trp_italian_billman, 1, 3), (trp_iberian_spears_sergeant, 1, 3), (trp_italian_veteran_spearman, 1, 3)]),

	("kingdom_italian_reinforcements_c", "{!}kingdom italian reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_40, soldier_personality, [(trp_italian_knight, 2, 5)]),

	("kingdom_andalus_reinforcements_a", "{!}kingdom andalus reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_village_recruit, 13, 32)]),

	("kingdom_andalus_reinforcements_b", "{!}kingdom andalus reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_spearman_1, 2, 5), (trp_andalus_spearman_2, 2, 5), (trp_andalus_town_xbow_1, 3, 12)]),

	("kingdom_andalus_reinforcements_c", "{!}kingdom andalus reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_horse_4, 2, 5)]),

	("kingdom_byzantium_reinforcements_a", "{!}kingdom byzantium reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_1, 1, 3), (trp_byz_village_1, 4, 9), (trp_byz_town_1, 4, 9)]),

	("kingdom_byzantium_reinforcements_b", "{!}kingdom byzantium reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_village_3_1, 1, 3), (trp_byz_village_3_2, 1, 3), (trp_byz_town_3_1, 2, 6), (trp_byz_town_3_2, 1, 3)]),

	("kingdom_byzantium_reinforcements_c", "{!}kingdom byzantium reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_4, 2, 5)]),

	("kingdom_mamluke_reinforcements_a", "{!}kingdom mamluke reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_25, soldier_personality, [(trp_halqa_recruit, 4, 9), (trp_mamluke_turkoman_1, 1, 3), (trp_bedouin_recruit, 4, 9), (trp_mamluke_turkoman_1, 0, 1)]),

	("kingdom_mamluke_reinforcements_b", "{!}kingdom mamluke reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_25, soldier_personality, [(trp_bedouin_spearman, 1, 3), (trp_halqa_archer, 1, 3), (trp_bedouin_cav_2, 1, 3), (trp_halqa_cav_2, 1, 3), (trp_mamluke_turkoman_2, 1, 3)]),

	("kingdom_mamluke_reinforcements_c", "{!}kingdom mamluke reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_25, soldier_personality, [(trp_mamluke_turkoman_3, 2, 5)]),

	("kingdom_marinid_reinforcements_a", "{!}kingdom marinid reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_village_rabble, 13, 32)]),

	("kingdom_marinid_reinforcements_b", "{!}kingdom marinid reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_light_spearmen, 2, 5), (trp_marinid_light_lancer, 2, 5), (trp_marinid_mounted_skirmisher_2, 3, 12)]),

	("kingdom_marinid_reinforcements_c", "{!}kingdom marinid reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_mounted_skirmisher_2, 3, 6), (trp_marinid_mounted_skirmisher_2, 3, 6)]),

	("kingdom_serbian_reinforcements_a", "{!}kingdom serbian reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_horse_1, 1, 6), (trp_serbian_vil_recruit, 6, 11), (trp_serbian_town_recruit, 2, 4)]),

	("kingdom_serbian_reinforcements_b", "{!}kingdom serbian reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_vil_spearman, 2, 6), (trp_serbian_vil_archer, 1, 3), (trp_serbian_vil_spearman_veteran, 1, 3), (trp_serbian_vil_axeman, 1, 3), (trp_serbian_vil_archer, 1, 3)]),

	("kingdom_serbian_reinforcements_c", "{!}kingdom serbian reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_horse_2, 1, 2), (trp_serbian_horse_4, 1, 3)]),

	("kingdom_balkan_reinforcements_a", "{!}kingdom balkan reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_horse_1, 1, 3), (trp_balkan_vil_1, 2, 7), (trp_balkan_town_1, 6, 11)]),

	("kingdom_balkan_reinforcements_b", "{!}kingdom balkan reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_vil_3_2_1, 2, 6), (trp_balkan_vil_3_1, 1, 3), (trp_balkan_town_3_1, 1, 3), (trp_balkan_town_3_2, 1, 3)]),

	("kingdom_balkan_reinforcements_c", "{!}kingdom balkan reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_horse_2, 1, 2), (trp_balkan_horse_4, 1, 3)]),

	("kingdom_welsh_reinforcements_a", "{!}kingdom welsh reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_horse_1, 1, 2), (trp_welsh_recruit, 5, 10), (trp_welsh_archer_1, 4, 9)]),

	("kingdom_welsh_reinforcements_b", "{!}kingdom welsh reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_archer_2, 3, 6), (trp_welsh_horse_2, 1, 1), (trp_welsh_spearman_1, 1, 2), (trp_welsh_spearman_2, 1, 2), (trp_welsh_archer_1, 1, 2)]),

	("kingdom_welsh_reinforcements_c", "{!}kingdom welsh reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_archer_2, 1, 2), (trp_welsh_horse_4, 1, 3)]),

	("steppe_bandit_lair", "Steppe Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_steppe_bandit, 15, 58)]),

	("taiga_bandit_lair", "Tundra Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_taiga_bandit, 15, 58)]),

	("desert_bandit_lair", "Desert Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_desert_bandit, 15, 58)]),

	("forest_bandit_lair", "Forest Bandit Camp", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_forest_bandit, 15, 58)]),

	("mountain_bandit_lair", "Highway Bandit Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mountain_bandit, 15, 58)]),

	("sea_raider_lair", "Sea Raider Landing", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_sea_raider, 15, 50)]),

	("robber_knight_lair", "Robber Knight's Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_euro_horse_4, 1, 1), (trp_raider, 15, 25)]),

	("looter_lair", "Kidnappers' Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_looter, 15, 25)]),

	("bandit_lair_templates_end", "{!}bandit lair templates end", icon_axeman|carries_goods(2)|pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_sea_raider, 15, 50)]),

	("leaded_looters", "Band of robbers", icon_axeman|carries_goods(8)|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_looter, 3, 3)]),

	("pagan_stronghold", "Pagan Stronghold", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_balt_skirmisher, 5, 7), (trp_balt_footman, 5, 7), (trp_balt_jav, 5, 7), (trp_balt_veteran_jav, 1, 3), (trp_balt_billman, 5, 7), (trp_balt_spearman, 5, 7)]),

	("dplmc_spouse", "Your spouse", icon_woman|pf_show_faction|pf_civilian, 0, fac_neutral, courage_7|merchant_personality, []),

	("dplmc_gift_caravan", "Your Caravan", icon_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_merc_euro_horse, 10, 35)]),

	("dplmc_recruiter", "Recruiter", icon_gray_knight|pf_show_faction, 0, fac_neutral, courage_7|merchant_personality, [(trp_dplmc_recruiter, 1, 1)]),

	("crusaders_teutonic", "{!}crusaders teutonic", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_3, 1, 6), (trp_teu_horse_4, 1, 3)]),

	("crusaders_templar", "{!}crusaders templar", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_templar_half_brother, 1, 6), (trp_templar_knight, 1, 3)]),

	("crusaders_hospitaller", "{!}crusaders hospitaller", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_hospitaller_half_brother, 1, 6), (trp_hospitaller_knight, 1, 3)]),

	("crusaders_lazarus", "{!}crusaders lazarus", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_saint_lazarus_half_brother, 1, 6), (trp_saint_lazarus_knight, 1, 3)]),

	("crusaders_santiago", "{!}crusaders santiago", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_santiago_half_brother, 1, 6), (trp_santiago_knight, 1, 3)]),

	("crusaders_calatrava", "{!}crusaders calatrava", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_calatrava_half_brother, 1, 6), (trp_calatrava_knight, 1, 3)]),

	("crusaders_saint_thomas", "{!}crusaders saint thomas", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_saint_thomas_half_brother, 1, 6), (trp_saint_thomas_knight, 1, 3)]),

	("teutonic_reinforcements_a", "{!}teutonic reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_1, 1, 3), (trp_teu_village_recruit, 4, 9), (trp_teu_town_1, 4, 9)]),

	("teutonic_reinforcements_b", "{!}teutonic reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_teu_town_2_2, 2, 6), (trp_teu_ger_1, 1, 3), (trp_teu_balt_1, 1, 3), (trp_teu_town_2_1, 1, 3)]),

	("teutonic_reinforcements_c", "{!}teutonic reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_4, 3, 6)]),

	("templar_reinforcements_a", "{!}templar reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_crusader_turkopole, 1, 3), (trp_iberian_village_recruit, 4, 9), (trp_iberian_town_recruit, 4, 9)]),

	("templar_reinforcements_b", "{!}templar reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_iberian_archer, 1, 3), (trp_iberian_veteran_crossbowman, 1, 3), (trp_iberian_billman, 1, 3), (trp_iberian_spears_sergeant, 1, 3), (trp_iberian_veteran_spearman, 1, 3)]),

	("templar_reinforcements_c", "{!}templar reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_templar_knight, 3, 6)]),

	("hospitaller_reinforcements_a", "{!}hospitaller reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_crusader_turkopole, 1, 3), (trp_iberian_village_recruit, 4, 9), (trp_iberian_town_recruit, 4, 9)]),

	("hospitaller_reinforcements_b", "{!}hospitaller reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_iberian_archer, 1, 3), (trp_iberian_veteran_crossbowman, 1, 3), (trp_iberian_billman, 1, 3), (trp_iberian_spears_sergeant, 1, 3), (trp_iberian_veteran_spearman, 1, 3)]),

	("hospitaller_reinforcements_c", "{!}hospitaller reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_hospitaller_knight, 3, 6)]),

	("kingdom_21_reinforcements_a", "{!}kingdom 21 reinforcements a", icon_player|pf_label_small, 0, fac_papacy, soldier_personality, [(trp_euro_horse_1, 1, 3), (trp_euro_village_recruit, 4, 9), (trp_euro_town_recruit, 4, 9)]),

	("kingdom_21_reinforcements_b", "{!}kingdom 21 reinforcements b", icon_player|pf_label_small, 0, fac_papacy, soldier_personality, [(trp_euro_archer_2, 1, 3), (trp_euro_xbow_2, 1, 3), (trp_euro_guisarm_2, 1, 3), (trp_euro_spearman_3, 1, 3), (trp_euro_spearman_2, 1, 3)]),

	("kingdom_21_reinforcements_c", "{!}kingdom 21 reinforcements c", icon_player|pf_label_small, 0, fac_papacy, soldier_personality, [(trp_euro_horse_2, 2, 5)]),

	("roman_reinforcements_a", "{!}roman reinforcements a", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_1, 1, 3), (trp_byz_village_1, 4, 9), (trp_byz_town_1, 4, 9)]),

	("roman_reinforcements_b", "{!}roman reinforcements b", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_village_3_1, 1, 3), (trp_byz_village_3_2, 1, 3), (trp_byz_town_3_1, 2, 6), (trp_byz_town_3_2, 1, 3)]),

	("roman_reinforcements_c", "{!}roman reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_2, 1, 2), (trp_byz_castle_4, 2, 3), (trp_varangian_guard, 1, 5)]),

	("armenian_reinforcements_c", "{!}armenian reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_23, soldier_personality, [(trp_anatolian_heavy_cavalry, 2, 5)]),

	("seljuk_reinforcements_c", "{!}seljuk reinforcements c", icon_player|pf_label_small, 0, fac_kingdom_27, soldier_personality, [(trp_anatolian_turkoman_3, 2, 5)]),

	("almogabar", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_almogabar, 20, 20)]),

	("welsh_merc", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_welsh_bowman, 20, 25), (trp_merc_welsh_bowman_commander, 1, 5)]),

	("sicilian_merc_1", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_infantry_2, 5, 5), (trp_merc_sicily_infantry_1, 15, 15)]),

	("sicilian_merc_2", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_foot_archer_2, 5, 5), (trp_merc_sicily_foot_archer_1, 15, 15)]),

	("sicilian_merc_3", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_horse_archer_2, 5, 5), (trp_merc_sicily_horse_archer_1, 15, 15)]),

	("zanata_merc", "{!}Lance", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_maghreb_horse, 10, 10), (trp_merc_maghreb_spearman, 10, 10), (trp_merc_maghreb_range, 10, 10)]),

	("generic_euro", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_euro_spearman, 12, 15), (trp_merc_euro_guisarmer, 5, 7), (trp_merc_euro_range, 6, 10), (trp_merc_euro_horse, 3, 7)]),

	("generic_balt", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_balt_spearman, 12, 15), (trp_merc_balt_guisarmer, 5, 7), (trp_merc_balt_range, 6, 10), (trp_merc_balt_horse, 3, 7)]),

	("generic_maghreb", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_maghreb_spearman, 14, 23), (trp_merc_maghreb_range, 6, 10), (trp_merc_maghreb_horse, 3, 7)]),

	("generic_rus", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_rus_spearman, 12, 15), (trp_merc_rus_guisarmer, 5, 7), (trp_merc_rus_range, 6, 10), (trp_merc_rus_horse, 3, 7)]),

	("generic_latin", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_latin_spearman, 10, 13), (trp_merc_latin_guisarmer, 4, 6), (trp_merc_latin_range, 5, 8), (trp_merc_latin_horse, 2, 5), (trp_merc_latin_light, 7, 12)]),

	("generic_balkan", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_balkan_spearman, 12, 15), (trp_merc_balkan_guisarmer, 5, 7), (trp_merc_balkan_range, 6, 10), (trp_merc_balkan_horse, 3, 7)]),

	("generic_scan", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_scan_spearman, 12, 15), (trp_merc_scan_guisarmer, 5, 7), (trp_merc_scan_range, 6, 10), (trp_merc_scan_horse, 3, 7)]),

	("generic_gaelic", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_gaelic_spearman, 12, 15), (trp_merc_gaelic_axeman_1, 5, 7), (trp_merc_gaelic_spearman_2, 6, 10), (trp_merc_gaelic_axeman_2, 3, 7)]),

	("generic_mamluk", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_mamluke_spearman, 12, 15), (trp_merc_mamluke_javalin, 7, 10), (trp_merc_mamluke_range, 5, 7), (trp_merc_mamluke_syrian, 3, 7)]),

	("company_genoese", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_genoese_crossbowman, 25, 32), (trp_genoese_crossbowman_commander, 1, 5)]),

	("company_brabantine", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_brabantine_spearman, 12, 15), (trp_merc_brabantine_guisarm, 4, 7), (trp_merc_brabantine_xbow, 6, 10)]),

	("company_welsh", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_welsh_bowman, 12, 15), (trp_merc_kern_infantry, 10, 15), (trp_merc_welsh_bowman_commander, 1, 3)]),

	("company_mamlukes", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_mamluke_medium_horse_archer, 5, 8), (trp_mamluke_heavy_horse_archer, 2, 3), (trp_mamluke_elite_horse_archer, 1, 3)]),

	("company_sicily", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_infantry_1, 12, 15), (trp_merc_sicily_infantry_2, 4, 7), (trp_merc_sicily_foot_archer_1, 6, 10), (trp_merc_sicily_foot_archer_2, 1, 5), (trp_merc_sicily_horse_archer_1, 1, 5), (trp_merc_sicily_horse_archer_2, 1, 5)]),

	("company_cuman", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_cuman_skirmisher, 12, 15), (trp_cuman_horseman, 4, 7), (trp_cuman_horse_archer, 6, 10), (trp_cuman_veteran_horse_archer, 3, 7), (trp_cuman_lancer, 1, 3), (trp_cuman_heavy_lancer, 1, 3)]),

	("company_georgian", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_georgian_lancer, 12, 18), (trp_goergian_horse_archer, 10, 18)]),

	("company_turkopoles", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_crusader_turkopole, 18, 32)]),

	("company_varangian", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_varangian_guard, 18, 32)]),

	("company_kwarezmian", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_kwarezmian_range, 12, 15), (trp_kwarezmian_light_horse, 10, 18), (trp_kwarezmian_medium_horse, 6, 8)]),

	("company_mordovian", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_mordovian_foot, 12, 18), (trp_mordovian_range, 4, 7), (trp_mordovian_horse, 6, 10)]),

	("company_kipchak", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_kipchak_range, 10, 15), (trp_kipchak_light_horse, 5, 9), (trp_kipchak_medium_horse, 5, 7)]),

	("company_teutons", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_teu_horse_3, 1, 6), (trp_teu_horse_4, 1, 2)]),

	("company_hospitalier", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_hospitaller_half_brother, 1, 6), (trp_hospitaller_knight, 1, 2)]),

	("company_templar", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_templar_half_brother, 1, 6), (trp_templar_knight, 1, 2)]),

	("company_lazarus", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_saint_lazarus_half_brother, 1, 6), (trp_saint_lazarus_knight, 1, 2)]),

	("company_santiago", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_santiago_half_brother, 1, 6), (trp_santiago_knight, 1, 2)]),

	("company_calatrava", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_calatrava_half_brother, 1, 6), (trp_calatrava_knight, 1, 2)]),

	("company_thomas", "{!}Company", icon_player|pf_label_small, 0, fac_neutral, soldier_personality, [(trp_saint_thomas_half_brother, 1, 6), (trp_saint_thomas_knight, 1, 2)]),

	("mongolian_camp", "Mongolian horde", icon_khergit|carries_goods(5)|pf_show_faction, 0, fac_commoners, soldier_personality, [(trp_tatar_veteran_horse_archer, 1, 2), (trp_tatar_heavy_lancer, 1, 1), (trp_tatar_skirmisher, 10, 14), (trp_tatar_tribesman, 8, 13)]),

	#recruiter kit begin troop recruiter
   #("recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_recruiter,1,1)]),
#recruiter kit end
]