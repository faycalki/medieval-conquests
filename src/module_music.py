from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory
#If you want songs to exist while you are in battle: mtf_sit_fight flag.
tracks = [
	("cant_find_this", "cant_find_this.ogg", 0, 0),

	("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),

	("capture", "capture.ogg", mtf_module_track, 0),

	("empty_village", "empty_village.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("escape", "escape.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("euro_1", "euro_1.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_2", "euro_2.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_3", "euro_3.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_4", "euro_4.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_5", "euro_5.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_6", "euro_6.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_7", "euro_7.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_8", "euro_8.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_9", "euro_9.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_10", "euro_10.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_11", "euro_11.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_12", "euro_12.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1),

	("euro_13", "euro_13.ogg", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
	
#New tracks begin now.
("euro_14", "teurol2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_15", "teuro1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 

("euro_16", "euros3.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_17", "euros2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_18", "eurols1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_19", "eurob1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 


#Less than 30 seconds length("euro_20", "euro16.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_21", "euro17.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_22", "euro18.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_23", "euro19.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_24", "euro20.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_25", "eurostrat.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_26", "eurostrat_2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_27", "eurostrat_5.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_28", "eurostrat_6.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_29", "eurostrat_7.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_30", "eurostrat_8.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_31", "eurostrat3.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_32", "eurostrat9.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_33", "eurostrat10.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#New tracks end now.

#New tracks V2
("euro_34", "euron1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_35", "euron2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_36", "euron3.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_37", "euron4.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_38", "euron5.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_39", "euron6.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_40", "euron7.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_41", "euron8.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_42", "euron9.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_43", "euron10.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_44", "euron12.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_45", "euron13.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
("euro_46", "euron14.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_47", "euron15.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_48", "euron16.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_49", "euron17.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_50", "euron18.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_51", "euron19.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_52", "euron20.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_53", "euron22.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_54", "euron26.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Teutons
#Less than 30 seconds length("euro_55", "teuro1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_56", "teuro2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_57", "teuro3.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_58", "teuro4.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_59", "teuro5.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_60", "teuro6.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_61", "teuro7.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#("euro_62", "teuro8.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#Less than 30 seconds length("euro_63", "teuro9.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_1), 
#New Tracks V2

	("baltic_1", "baltic_1.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),

	("baltic_2", "baltic_2.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),

	("baltic_3", "baltic_3.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),

	("baltic_4", "baltic_4.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),

	("baltic_5", "baltic_5.ogg", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	
	#New
	("baltic_6", "baltnc1.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_7", "mediter2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_8", "medite3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_9", "mediter4.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_10", "mediter5.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_11", "mediter6.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#New
	
	#New Tracks V2
	#("baltic_12", "balntn9.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_13", "baltnc2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
("baltic_14", "medicalm1.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_15", "baltn3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
("baltic_16", "medicalm2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
("baltic_17", "medicalm3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_18", "baltn6.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_19", "baltn7.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_20", "baltn8.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_21", "baltn10.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_22", "baltn12.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_23", "baltn13.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_24", "baltnn1.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_25", "baltnn2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_26", "baltnn3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_27", "baltnn4.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_28", "baltnn5.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_29", "baltnn6.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_30", "baltnn7.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#Less than 30 seconds length	("baltic_31", "baltnn9.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#New tracks V2
	#Mediterr version for balts
#	("baltic_32", "medin1.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_33", "medin2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_34", "medin3.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_35", "medin4.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_36", "medin5.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
#	("baltic_37", "medin6.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_38", "medin7.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_39", "medin8.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_40", "medin9.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_41", "medin10.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_42", "medin12.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_43", "medin13.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	("baltic_44", "medin14.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#("baltic_45", "mediter.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_2),
	#Mediterr Version for balts
	
	
	("rus_1", "rus_1.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),

	("rus_2", "rus_2.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),

	("rus_3", "rus_3.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),

	("rus_4", "rus_4.ogg", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	
	#New
	#("rus_5", "mediterr.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#("rus_6", "mediter2.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	("rus_7", "rusnnn1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#("rus_8", "mediter4.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#("rus_9", "mediter5.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#("rus_10", "mediter6.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#New
	
	#Mediterr Version for rus
		#("rus_11", "medin1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
			("rus_12", "medin2.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
			#	("rus_13", "medin3.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
					#("rus_14", "medin4.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
						("rus_15", "medin5.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
							#("rus_16", "medin6.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
								("rus_17", "medin7.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
									("rus_18", "medin8.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
										("rus_19", "medin9.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
											("rus_20", "medin10.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
												("rus_21", "medin12.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
													("rus_22", "medin13.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
														("rus_23", "medin14.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
															("rus_24", "rusl1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#Mediterr Version for rus
("rus_25", "rusn1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
("rus_26", "medicalm3.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
("rus_27", "medicalm2.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
("rus_28", "medicalm1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
#("rus_29", "rusnn5.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
#Less than 30 seconds length("rus_30", "rusnn6.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
#Less than 30 seconds length("rus_31", "rusnn7.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
#("rus_32", "rusnn8.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
#("rus_33", "rusnn9.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_5),
	#Tracks V2 for Rus Begin
	
	#Tracks V2 for Rus End
	
	("saracen_1", "saracen_1.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_2", "saracen_2.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_3", "saracen_3.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_4", "saracen_4.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_5", "saracen_5.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_6", "saracen_6.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),

	("saracen_7", "saracen_7.ogg", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	
	#New
	("saracen_8", "arablc1.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	("saracen_9", "arablc2.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	("saracen_10", "arabnc1.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	("saracen_11", "arabstart4.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	("saracen_12", "arabstart5.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#	("saracen_13", "arabstart6.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	#New
	
	#Tracks V2 for Arabs Begin
	("saracen_14", "arabn1.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	("saracen_15", "arabn2.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#Less than 30 seconds length	("saracen_16", "arabn3.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#	("saracen_17", "arabn4.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#Less than 30 seconds length	("saracen_18", "arabn5.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#Less than 30 seconds length	("saracen_19", "arabn6.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#Less than 30 seconds length	("saracen_20", "arabn7.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#Less than 30 seconds length	("saracen_21", "arabn8.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
#	("saracen_22", "arabn9.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_4),
	#Tracks V2 for Arabs end

	("mong_1", "mong_1.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_2", "mong_2.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_3", "mong_3.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_4", "mong_4.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_5", "mong_5.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_6", "mong_6.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_7", "mong_7.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),

	("mong_8", "mong_8.ogg", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	
	#New
	("mong_9", "mongolc1.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	("mong_10", "medicalm1.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	#("mong_11", "medite3.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	("mong_12", "medicalm2.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	("mong_13", "medicalm3.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#	("mong_14", "mediter6.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	#New

	#Mongol Tracks V2 Begin
#Less than 30 seconds length	("mong_15", "mongoln1.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#	("mong_16", "mongoln2.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#	("mong_17", "mongoln3.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	("mong_18", "mongoln4.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#Less than 30 seconds length	("mong_19", "mongoln5.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#Less than 30 seconds length	("mong_20", "mongoln6.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
#Less than 30 seconds length	("mong_21", "mongoln7.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_3),
	#Mongol Tracks V2 End
	("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

	("coronation", "coronation.ogg", mtf_persist_until_finished, 0),

	("ambient_1", "ambient_1.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_2", "ambient_2.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_3", "ambient_3.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_4", "ambient_4.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_5", "ambient_5.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_6", "ambient_6.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_7", "ambient_7.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_8", "ambient_8.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_9", "ambient_9.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_sit_fight|mtf_module_track, mtf_culture_all),

	("ambient_10", "ambient_10.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	
#	("ambient_1", "ambient_1.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_2", "ambient_2.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_3", "ambient_3.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_4", "ambient_4.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_5", "ambient_5.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_6", "ambient_6.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_7", "ambient_7.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_8", "ambient_8.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_9", "ambient_9.ogg", mtf_culture_all|mtf_persist_until_finished|mtf_module_track, mtf_culture_all),
#
#	("ambient_10", "ambient_10.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	#("silence", "silence.ogg", mtf_persist_until_finished|mtf_module_track, 0), #Legacy
	("silence", "silence_enh.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	#("reset_silence", "silence_enh.wma", mtf_module_track, 0),
	("reset_silence", "silence_enh.ogg", mtf_module_track, 6969), #0
	#("silence_enh", "silence_enh.wma", mtf_persist_until_finished|mtf_module_track, 0),
	##New tracks for battles Begin, note that use module_sounds tracks for Single Player, and module_tracks from here for Multiplayer.
	#Tension music requires sit_travel thus must be moved to module_sounds and controlled there due to lack of track operations.
	#("battle_arab", "(Arabic_Tension_1)_Kebabka.mp3", mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 0),
	
	#Tension
	
	#Mediterr
	("medm1", "(Brittania_Tension)_Ghosts_Of_Loch.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("medm2", "(Britannia_Camp_Battle)_Tally-ho.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("medm3", "(Euro_Tension_2)_Call_Of_The_Sheep.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("medm4", "(Euro_Tension_9)_Grave_Blow.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("medm5", "(Euro_Tension_6)_Chase.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	#Arabs
	("arabt1", "(Arabic_Tension_4).mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("arabt2", "(Arabic_Tension_3).mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("arabt3", "(Crusades_Tension)_Parched.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("arabt4", "(Crusades_Loading)_Against_The_Rock.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("arabt5", "(Arabic_Camp_Battle_1)_Honour_Of_Sultan.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("arabt6", "(Crusades_Campaign_Battle)_Sun_Eyes.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),

	#Euro_Tension
	("eurottt1", "(Euro_Tension_1)_BladeGrass.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt2", "(Euro_Tension_3)_Fear_Frozen.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt3", "(Euro_Tension_4).mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt4", "(Euro_Tension_5).mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt5", "(Euro_Tension_7)_The_Reveal.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt6", "(Euro_Tension_8)_Ignosi.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt7", "(Teutonic_Tension)_Forest_Haze.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt8", "(Teutonic_Campaign_Loading)_Brothers_Together.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt9", "(Euro_Loading_3)_Epic_Unease.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt10", "(Teutonic_Campaign_Battle)_Hungry_Sword.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),
	("eurottt11", "(Euro_Camp_Battle_1)_Destiny.mp3", mtf_sit_encounter_hostile|mtf_module_track, 6969),

	####
   ("arabb1", "(Arabic_Battle_1)_Crack_your_head_with_a_Tabla.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("arabb2", "(Arabic_Battle_2)_Wind_Cuts.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("arabb4", "(Arabic_Battle_3).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("arabb5", "(Arabic_Battle_4).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("arabb6", "(Crusades_Battle)_Valley_Of_Death.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabb8", "(Arabic_Tension_1)_Kebabka.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabb9", "(Arabic_Tension_5).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Starsand
  #NOTE Mediterrain battle and mobilize (sieges) are shared songs.
  #Mobilize
  ("medib1", "(Mediterranean_Battle_1)_Lifted_To_The_Hotplate.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("medib3", "(Mediterranean_Mobilize_1)_Mare_Nostrum.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("medib4", "(Mediterranean_Mobilize_2)_Death_Lullaby.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("medib5", "(Mediterranean_Mobilize_2)_Song_For_Toomba.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
   ("medib6", "(Mediterranean_Tension_1)_By_The_Marmara.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("medib7", "(Mediterranean_Tension_2)_Secret_Sandals.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("medib8", "(Arabic_Tension_2)_Starsand.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Starsand
  #Field Continuation
  ##
   ("eurob1", "(Euro_Battle_1)_Duke_of_Death.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob2", "(Euro_Battle_2)_Nothing_Left.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob3", "(Euro_Battle_3)_Crusaders.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob4", "(Euro_Battle_4)_War_of_Kings.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob5", "(Euro_Battle_5).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob6", "(Euro_Battle_6).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob7", "(Euro_Battle_7).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob8", "(Euro_Battle_8)_Vortex.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob9", "(Euro_Battle_9)_Dangerous.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("eurob11", "(Teutonic_Battle)_Darker_Skies_Ahead.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
  ##Sieges
   ("arabs1", "(Arabic_Mobilize_1)_High_Winds.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabs2", "(Arabic_Mobilize_2).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabs3", "(Arabic_Mobilize_3).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabs4", "(Arabic_Mobilize_4).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ("arabs5", "(Crusades_Mobilize)_Honour_Moment.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
    #Mediterr & Arabs
	("medis1", "(Euro_Mobilize_5)_Action.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("medis2", "(Euro_Mobilize_9)_Feral_Chase.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
   ##Euro
	#("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_sit_encounter_hostile|mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	#("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_sit_encounter_hostile|mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	#Mtf_sit_travel is necessary.
	("euros2", "(Euro_Mobilize_2)_Solenka.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros3", "(Euro_Mobilize_3)_This_is_it.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros4", "(Euro_Mobilize_4)_New_Arc_Ascending.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros5", "(Euro_Mobilize_6).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros6", "(Euro_Mobilize_7).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros7", "(Euro_Mobilize_8).mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros8", "(Euro_Mobilize_10)_Tectonic.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros9", "(Teutonic_Mobilize)_Hymn_Of_War.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	("euros10", "(Euro_Mobilize_11)_We_Got_Trouble.mp3", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),

	
	#####Battle-end sounds
	("lost_arab", "(Arabic_Lose_1)_Fly_Away.mp3", mtf_start_immediately|mtf_sit_feast|mtf_module_track, 6969),
	("lost_crusade", "(Crusades_Lose)_Blood_Blisters.mp3", mtf_start_immediately|mtf_sit_feast|mtf_module_track, 6969),
	("lost_brittania", "(Brittania_Lose)_Black_Garden.mp3", mtf_start_immediately|mtf_sit_town|mtf_module_track, 6969),
	("lost_aztec", "(Aztec_Lose_1)_Muahyan.mp3", mtf_start_immediately|mtf_sit_feast|mtf_module_track, 6969),
	("lost_mediterr", "(Mediterranean_Lose_1)_Cordone.mp3", mtf_start_immediately|mtf_sit_arena|mtf_module_track, 6969),
	("lost_euro1", "(Euro_Lose_1)_Duty.mp3", mtf_start_immediately|mtf_sit_town|mtf_module_track, 6969),
	("lost_euro2", "(Euro_Lose_2)_Spirit_Fingers.mp3", mtf_start_immediately|mtf_sit_town|mtf_module_track, 6969),
	("lost_euro3", "(Euro_Lose_3)_Did_they_have_to_die_today.mp3", mtf_start_immediately|mtf_sit_town|mtf_module_track, 6969),
	("lost_teuton", "(Teutonic_Lose)_Warrior's_Tomb.mp3", mtf_start_immediately|mtf_sit_town|mtf_module_track, 6969),
	##Losses end

	#Wins begin
	("won_arab", "(Arabic_Win_1)_Balalip.mp3", mtf_start_immediately|mtf_sit_night|mtf_module_track, 6969),
	("won_crusade", "(Crusades_Win)_Hands_High.mp3",mtf_start_immediately|mtf_sit_night|mtf_module_track, 6969),
	("won_brittania", "(Brittania_Win)_Harvest.mp3", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 6969),
	("won_aztec", "(Aztec_Win_1)_Mextli_Mambo.mp3", mtf_start_immediately|mtf_sit_night|mtf_module_track, 6969),
	("won_euro", "(Euro_Win_1)_Going_Home.mp3", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 6969),
	("won_mediterr", "(Mediterranean_Win_1)_Grab_Your_Castanets.mp3", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 6969),
	("won_teuton", "(Teutonic_Win)_Chaos_Victorious.mp3", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 6969),
	##### Backup below
	
	#mtf_sit_ambushed
	#mtf_sit_town
	
	#mtf_sit_town_infiltrate
	#mtf_sit_arena
	
	#mtf_sit_night
	#mtf_sit_feast
	
	#####Battle-end sounds
	("lost_generic", "players_army_destroyed.mp3", mtf_sit_day|mtf_module_track, 6969),
	("won_generic", "rebels_victorious.mp3", mtf_sit_victorious|mtf_module_track, 6969),
	("won_generic2", "infantry_group_celebrate_small_01.mp3", mtf_sit_victorious|mtf_module_track, 6969),
	("won_generic3", "infantry_group_celebrate_large_01.mp3", mtf_sit_victorious|mtf_module_track, 6969),
	##### Backup below
	

	
#		#####Battle-end sounds
#	("lost_arab", "(Arabic_Lose_1)_Fly_Away.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_crusade", "(Crusades_Lose)_Blood_Blisters.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_brittania", "(Brittania_Lose)_Black_Garden.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_aztec", "(Aztec_Lose_1)_Muahyan.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_mediterr", "(Mediterranean_Lose_1)_Cordone.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_euro1", "(Euro_Lose_1)_Duty.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_euro2", "(Euro_Lose_2)_Spirit_Fingers.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_euro3", "(Euro_Lose_3)_Did_they_have_to_die_today.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	("lost_teuton", "(Teutonic_Lose)_Warrior's_Tomb.mp3", mtf_start_immediately|mtf_sit_day|mtf_module_track, 6969),
#	##Losses end
#
#	#Wins begin
#	("won_arab", "(Arabic_Win_1)_Balalip.mp3", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_crusade", "(Crusades_Win)_Hands_High.mp3",mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_brittania", "(Brittania_Win)_Harvest.mp3", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_aztec", "(Aztec_Win_1)_Mextli_Mambo.mp3", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_euro", "(Euro_Win_1)_Going_Home.mp3",mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_mediterr", "(Mediterranean_Win_1)_Grab_Your_Castanets.mp3", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	("won_teuton", "(Teutonic_Win)_Chaos_Victorious.mp3", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 6969),
#	##### Backup below
#	
#	#mtf_sit_ambushed
#	#mtf_sit_town
#	#mtf_sit_town_infiltrate
#	#mtf_sit_arena
#	#mtf_sit_night
#	#mtf_sit_feast
#	
#	#####Battle-end sounds
#	("lost_generic", "players_army_destroyed.mp3", mtf_sit_day|mtf_module_track, 6969),
#	("won_generic", "rebels_victorious.mp3", mtf_sit_victorious|mtf_module_track, 6969),
#	("won_generic2", "infantry_group_celebrate_small_01.mp3", mtf_sit_victorious|mtf_module_track, 6969),
#	("won_generic3", "infantry_group_celebrate_large_01.mp3", mtf_sit_victorious|mtf_module_track, 6969),
#	##### Backup below
	
	
#	#Mediterr
#	("medm1", "(Brittania_Tension)_Ghosts_Of_Loch.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("medm2", "(Britannia_Camp_Battle)_Tally-ho.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("medm3", "(Euro_Tension_2)_Call_Of_The_Sheep.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("medm4", "(Euro_Tension_9)_Grave_Blow.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("medm5", "(Euro_Tension_6)_Chase.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	#Arabs
#	("arabt1", "(Arabic_Tension_4).mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("arabt2", "(Arabic_Tension_3).mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("arabt3", "(Crusades_Tension)_Parched.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("arabt4", "(Crusades_Loading)_Against_The_Rock.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("arabt5", "(Arabic_Camp_Battle_1)_Honour_Of_Sultan.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("arabt6", "(Crusades_Campaign_Battle)_Sun_Eyes.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#
#	#Euro_Tension
#	("eurottt1", "(Euro_Tension_1)_BladeGrass.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt2", "(Euro_Tension_3)_Fear_Frozen.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt3", "(Euro_Tension_4).mp3",mtf_sit_travel| mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt4", "(Euro_Tension_5).mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt5", "(Euro_Tension_7)_The_Reveal.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt6", "(Euro_Tension_8)_Ignosi.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt7", "(Teutonic_Tension)_Forest_Haze.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt8", "(Teutonic_Campaign_Loading)_Brothers_Together.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt9", "(Euro_Loading_3)_Epic_Unease.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt10", "(Teutonic_Campaign_Battle)_Hungry_Sword.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("eurottt11", "(Euro_Camp_Battle_1)_Destiny.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#
#	####
#   ("arabb1", "(Arabic_Battle_1)_Crack_your_head_with_a_Tabla.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("arabb2", "(Arabic_Battle_2)_Wind_Cuts.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("arabb4", "(Arabic_Battle_3).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("arabb5", "(Arabic_Battle_4).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("arabb6", "(Crusades_Battle)_Valley_Of_Death.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabb8", "(Arabic_Tension_1)_Kebabka.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabb9", "(Arabic_Tension_5).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Starsand
#  #NOTE Mediterrain battle and mobilize (sieges) are shared songs.
#  #Mobilize
#  ("medib1", "(Mediterranean_Battle_1)_Lifted_To_The_Hotplate.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("medib3", "(Mediterranean_Mobilize_1)_Mare_Nostrum.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("medib4", "(Mediterranean_Mobilize_2)_Death_Lullaby.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("medib5", "(Mediterranean_Mobilize_2)_Song_For_Toomba.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Sieges too
#   ("medib6", "(Mediterranean_Tension_1)_By_The_Marmara.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("medib7", "(Mediterranean_Tension_2)_Secret_Sandals.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("medib8", "(Arabic_Tension_2)_Starsand.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969), #Starsand
#  #Field Continuation
#  ##
#   ("eurob1", "(Euro_Battle_1)_Duke_of_Death.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob2", "(Euro_Battle_2)_Nothing_Left.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob3", "(Euro_Battle_3)_Crusaders.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob4", "(Euro_Battle_4)_War_of_Kings.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob5", "(Euro_Battle_5).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob6", "(Euro_Battle_6).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob7", "(Euro_Battle_7).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob8", "(Euro_Battle_8)_Vortex.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob9", "(Euro_Battle_9)_Dangerous.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("eurob11", "(Teutonic_Battle)_Darker_Skies_Ahead.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#  ##Sieges
#   ("arabs1", "(Arabic_Mobilize_1)_High_Winds.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabs2", "(Arabic_Mobilize_2).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabs3", "(Arabic_Mobilize_3).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabs4", "(Arabic_Mobilize_4).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ("arabs5", "(Crusades_Mobilize)_Honour_Moment.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#    #Mediterr & Arabs
#	("medis1", "(Euro_Mobilize_5)_Action.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("medis2", "(Euro_Mobilize_9)_Feral_Chase.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#   ##Euro
#	#("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	#("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_start_immediately|mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros1", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_sit_travel|mtf_sit_travel|mtf_sit_encounter_hostile|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	#Mtf_sit_travel is necessary.
#	("euros2", "(Euro_Mobilize_2)_Solenka.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros3", "(Euro_Mobilize_3)_This_is_it.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros4", "(Euro_Mobilize_4)_New_Arc_Ascending.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros5", "(Euro_Mobilize_6).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros6", "(Euro_Mobilize_7).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros7", "(Euro_Mobilize_8).mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros8", "(Euro_Mobilize_10)_Tectonic.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros9", "(Teutonic_Mobilize)_Hymn_Of_War.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
#	("euros10", "(Euro_Mobilize_11)_We_Got_Trouble.mp3", mtf_sit_travel|mtf_sit_main_title|mtf_sit_multiplayer_fight|mtf_sit_fight|mtf_sit_siege|mtf_module_track, 6969),
	#mtf_sit_encounter_hostile, mtf_sit_victorious
	#("euros1", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_1)_Sister_Davul.mp3"]),
	##End tracks for battles end
	#mtf_sit_multiplayer_fight #For MP.
	
	
	#More main title songs begin
	##
	#("won_arab", "(Arabic_Win_1)_Balalip.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6969),
	#("won_crusade", "(Crusades_Win)_Hands_High.mp3",mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6969),
	##
	("(Teutonic_Campaign)_Hearty_Horn", "(Teutonic_Campaign)_Hearty_Horn.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	("dama4", "dama4.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	("whoarewetosay", "whoarewetosay.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	("whoarewetosayvocal", "whoarewetosayvocal.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	("damn4", "damn4.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	("kaw", "kaw.ogg", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	#unused
	#("aminotworthy", "aminotworthy.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	#("aloneinthis", "aloneinthis.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	#("relatives", "relatives.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 6968),
	#unused
	#End
	
]