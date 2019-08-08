from header_quests import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

quests = [
	("deliver_message", "Deliver Message to {s13}", qf_random_quest,
	"{!}{s9}_asked_you_to_take_a_message_to_{s13}._{s13}_was_at_{s4}_when_you_were_given_this_quest."
	),

	("deliver_message_to_enemy_lord", "Deliver Message to {s13}", qf_random_quest,
	"{!}{s9}_asked_you_to_take_a_message_to_{s13}_of_{s15}._{s13}_was_at_{s4}_when_you_were_given_this_quest."
	),

	("raise_troops", "Raise {reg1} {s14}", qf_random_quest,
	"{!}{s9}_asked_you_to_raise_{reg1}_{s14}_and_bring_them_to_him."
	),

	("escort_lady", "Escort {s13} to {s14}", qf_random_quest,
	"{!}None"
	),

	("deal_with_bandits_at_lords_village", "Save the Village of {s15} from Marauding Bandits", qf_random_quest,
	"{!}{s13}_asked_you_to_deal_with_the_bandits_who_took_refuge_in_his_village_of_{s15}_and_then_report_back_to_him."
	),

	("collect_taxes", "Collect Taxes from {s3}", qf_random_quest,
	"{!}{s9}_asked_you_to_collect_taxes_from_{s3}._He_offered_to_leave_you_one-fifth_of_all_the_money_you_collect_there."
	),

	("hunt_down_fugitive", "Hunt Down {s4}", qf_random_quest,
	"{!}{s9}_asked_you_to_hunt_down_the_fugitive_named_{s4}._He_is_currently_believed_to_be_at_{s3}."
	),

	("kill_local_merchant", "Assassinate Local Merchant at {s3}", qf_random_quest,
	"{!}{s9}_asked_you_to_assassinate_a_local_merchant_at_{s3}."
	),

	("bring_back_runaway_serfs", "Bring Back Runaway Serfs", qf_random_quest,
	"{!}{s9}_asked_you_to_bring_back_the_three_groups_of_runaway_serfs_back_to_{s2}._He_said_all_three_groups_must_be_running_away_in_the_direction_of_{s3}."
	),

	("follow_spy", "Follow the Spy to Meeting", qf_random_quest,
	"{!}{s11}_asked_you_to_follow_the_spy_that_will_leave_{s12}._You_must_be_careful_not_to_be_seen_by_the_spy_during_his_travel,_or_else_he_may_get_suspicious_and_turn_back._Once_the_spy_meets_with_his_accomplice,_you_are_to_ambush_and_capture_them_and_bring_them_both_back_to_{s11}."
	),

	("capture_enemy_hero", "Capture a Lord from {s13}", qf_random_quest,
	"{!}TODO:_{s11}_asked_you_to_capture_a_lord_from_{s13}."
	),

	("lend_companion", "Lend Your Companion {s3} to {s9}", qf_random_quest,
	"{!}{s9}_asked_you_to_lend_your_companion_{s3}_to_him_for_a_week."
	),

	("collect_debt", "Collect the Debt {s3} Owes to {s9}", qf_random_quest,
	"{!}{s9}_asked_you_to_collect_the_debt_of_{reg4}_denars_{s3}_owes_to_him."
	),

	("incriminate_loyal_commander", "Incriminate the Loyal Commander of {s13}, {s16}", qf_random_quest,
	"{!}None"
	),

	("meet_spy_in_enemy_town", "Meet Spy in {s13}", qf_random_quest,
	"{!}None"
	),

	("capture_prisoners", "Bring {reg1} {s3} Prisoners", qf_random_quest,
	"{!}{s9}_wanted_you_to_bring_him_{reg1}_{s3}_as_prisoners."
	),

	("lend_surgeon", "Lend Your Surgeon {s3} to {s1}", qf_random_quest,
	"{!}Lend_your_experienced_surgeon_{s3}_to_{s1}."
	),

	("follow_army", "Follow {s9}'s Army", qf_random_quest,
	"{!}None"
	),

	("report_to_army", "Report to {s13}, the Marshall", qf_random_quest,
	"{!}None"
	),

	("deliver_cattle_to_army", "Deliver {reg3} Heads of Cattle to {s13}", qf_random_quest,
	"{!}None"
	),

	("join_siege_with_army", "Join the Siege of {s14}", qf_random_quest,
	"{!}None"
	),

	("screen_army", "Screen the Advance of {s13}'s Army", qf_random_quest,
	"{!}None"
	),

	("scout_waypoints", "Scout {s13}, {s14} and {s15}", qf_random_quest,
	"{!}None"
	),

	("rescue_lord_by_replace", "Rescue {s13} from {s14}", qf_random_quest,
	"{!}None"
	),

	("deliver_message_to_prisoner_lord", "Deliver Message to {s13} at {s14}", qf_random_quest,
	"{!}None"
	),

	("duel_for_lady", "Challenge {s13} to a Trial of Arms", qf_random_quest,
	"{!}None"
	),

	("duel_courtship_rival", "Challenge {s13} to a Trial of Arms (optional)", qf_random_quest,
	"{!}None"
	),

	("duel_avenge_insult", "Challenge {s13} to a Trial of Arms", qf_random_quest,
	"{!}None"
	),

	("move_cattle_herd", "Move Cattle Herd to {s13}", qf_random_quest,
	"{!}Guildmaster_of_{s10}_asked_you_to_move_a_cattle_herd_to_{s13}."
	),

	("escort_merchant_caravan", "Escort Merchant Caravan to {s8}", qf_random_quest,
	"{!}Escort_the_merchant_caravan_to_the_town_of_{s8}."
	),

	("deliver_wine", "Deliver {reg5} Units of {s6} to {s4}", qf_random_quest,
	"{!}{s9}_of_{s3}_asked_you_to_deliver_{reg5}_units_of_{s6}_to_the_tavern_in_{s4}_in_7_days."
	),

	("troublesome_bandits", "Hunt Down Troublesome Bandits", qf_random_quest,
	"{!}{s9}_of_{s4}_asked_you_to_hunt_down_the_troublesome_bandits_in_the_vicinity_of_the_town."
	),

	("kidnapped_girl", "Ransom Girl from Bandits", qf_random_quest,
	"{!}Guildmaster_of_{s4}_gave_you_{reg12}_denars_to_pay_the_ransom_of_a_girl_kidnapped_by_bandits._You_are_to_meet_the_bandits_near_{s3}_and_pay_them_the_ransom_fee._After_that_you_are_to_bring_the_girl_back_to_{s4}."
	),

	("persuade_lords_to_make_peace", "Make Sure Two Lords Do Not Object to Peace", qf_random_quest,
	"{!}Guildmaster_of_{s4}_promised_you_{reg12}_denars_if_you_can_make_sure_that_{s12}_and_{s13}_no_longer_pose_a_threat_to_a_peace_settlement_between_{s15}_and_{s14}._In_order_to_do_that,_you_must_either_convince_them_or_make_sure_they_fall_captive_and_remain_so_until_a_peace_agreement_is_made."
	),

	("deal_with_looters", "Deal with Looters", qf_random_quest,
	"{!}The_Guildmaster_of_{s4}_has_asked_you_to_deal_with_several_bands_of_looters_around_{s4},_and_bring_back_any_goods_you_recover."
	),

	("deal_with_night_bandits", "Deal with Night Bandits", qf_random_quest,
	"{!}TODO:_The_Guildmaster_of_{s14}_has_asked_you_to_deal_with_night_bandits_at_{s14}."
	),

	("deliver_grain", "Bring wheat to {s3}", qf_random_quest,
	"{!}The_elder_of_the_village_of_{s3}_asked_you_to_bring_them_{reg5}_packs_of_wheat.."
	),

	("deliver_cattle", "Deliver {reg5} Heads of Cattle to {s3}", qf_random_quest,
	"{!}The_elder_of_the_village_of_{s3}_asked_you_to_bring_{reg5}_heads_of_cattle."
	),

	("train_peasants_against_bandits", "Train the Peasants of {s13} Against Bandits.", qf_random_quest,
	"{!}None"
	),

	("eliminate_bandits_infesting_village", "Save the Village of {s7} from Marauding Bandits", qf_random_quest,
	"{!}A_villager_from_{s7}_begged_you_to_save_their_village_from_the_bandits_that_took_refuge_there."
	),

	("visit_lady", "Visit Lady", qf_random_quest,
	"{!}None"
	),

	("formal_marriage_proposal", "Formal Marriage Proposal", qf_random_quest,
	"{!}None"
	),

	("obtain_liege_blessing", "Formal Marriage Proposal", qf_random_quest,
	"{!}None"
	),

	("wed_betrothed", "Wed Your Betrothed", qf_random_quest,
	"{!}None"
	),

	("wed_betrothed_female", "Wed Your Betrothed", qf_random_quest,
	"{!}None"
	),

	("join_faction", "Give Oath of Homage to {s1}", qf_random_quest,
	"{!}Find_{s1}_and_give_him_your_oath_of_homage."
	),

	("rebel_against_kingdom", "Help {s13} Claim the Throne of {s14}", qf_random_quest,
	"{!}None"
	),

	("consult_with_minister", "Consult With Minister", qf_random_quest,
	"{!}Consult_your_minister,_{s11},_currently_at_{s12}"
	),

	("organize_feast", "Organize Feast", qf_random_quest,
	"{!}Bring_goods_for_a_feast_to_your_spouse_{s11},_currently_at_{s12}"
	),

	("resolve_dispute", "Resolve Dispute", qf_random_quest,
	"{!}Resolve_the_dispute_between_{s11}_and_{s12}"
	),

	("offer_gift", "Procure Gift", qf_random_quest,
	"{!}Give_{s10}_a_gift_to_provide_to_{reg4?her:his}_{s11},_{s12}"
	),

	("denounce_lord", "Denounce Lord", qf_random_quest,
	"{!}Denounce_{s11}_in_Public"
	),

	("intrigue_against_lord", "Intrigue against Lord", qf_random_quest,
	"{!}Criticize_{s11}_in_Private"
	),

	("track_down_bandits", "Track Down Bandits", qf_random_quest,
	"{!}{s9}_of_{s4}_asked_you_to_track_down_{s6},_who_attacked_travellers_on_the_roads_near_town."
	),

	("track_down_provocateurs", "Track Down Provocateurs", qf_random_quest,
	"{!}{s9}_of_{s4}_asked_you_to_track_down_a_group_of_thugs,_hired_to_create_a_border_incident_between_{s5}_and_{s6}."
	),

	("retaliate_for_border_incident", "Retaliate for a Border Incident", qf_random_quest,
	"{!}{s9}_of_{s4}_asked_you_to_defeat_{s5}_of_the_{s7}_in_battle,_defusing_tension_in_the_{s8}_to_go_to_war."
	),

	("raid_caravan_to_start_war", "Attack a Neutral Caravan to Provoke War", qf_random_quest,
	"{!}placeholder"
	),

	("cause_provocation", "Give a Kingdom Provocation to Attack Another", qf_random_quest,
	"{!}placeholder"
	),

	("rescue_prisoner", "Rescue or Ransom a Prisoner", qf_random_quest,
	"{!}placeholder"
	),

	("destroy_bandit_lair", "Destroy Bandit Lair", qf_random_quest,
	"{!}{s9}_of_{s4}_asked_you_to_discover_a_{s6}_and_destroy_it."
	),

	("blank_quest_2", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_3", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_4", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_5", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_6", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_7", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_8", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_9", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_10", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_11", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_12", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_13", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_14", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_15", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_16", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_17", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_18", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_19", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_20", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_21", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_22", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_23", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_24", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_25", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_26", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("blank_quest_27", "{!}blank quest", qf_random_quest,
	"{!}placeholder"
	),

	("collect_men", "Collect Five Men", 0,
	"{!}{s9}_asked_you_to_collect_at_least_5_men_before_you_move_against_the_bandits_threatening_the_townsmen._You_can_recruit_soldiers_from_villages_as_well_as_town_taverns._You_can_find_{s9}_at_the_tavern_in_{s4}_when_you_have_think_you_have_enough_men."
	),

	("learn_where_merchant_brother_is", "Learn Where the Hostages are Held.", 0,
	"{!}placeholder."
	),

	("save_relative_of_merchant", "Attack the Bandit Lair", 0,
	"{!}placeholder."
	),

	("save_town_from_bandits", "Save Town from Bandits", 0,
	"{!}placeholder."
	),

	("freelancer_enlisted", "Enlisted in the Party of {s13}", 0,
	"{!}You_are_currently_enlisted_in_the_party_of_{s13}_of_{s14}."
	),

	("freelancer_vacation", "Enlisted: On Leave", 0,
	"{!}You_have_been_granted_leave_from_the_party_of_{s13}_of_{s14}."
	),

	("freelancer_captured", "Enlisted: Captured", 0,
	"{!}Your_commander's_party_has_been_defeated_and_you_have_been_captured._Return_to_the_service_of_{s13}_of_{s14}."
	),

	("quests_end", "Quests End", 0,
	"{!}."
	),

]