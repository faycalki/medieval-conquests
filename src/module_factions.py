# -*- coding: utf8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

factions = [
	("no_faction", "No Faction", 0, 0.9, []),

	("commoners", "Commoners", 0, 0.1, [("forest_bandits",-0.20),("player_faction",0.10),("mountain_bandits",-0.20),("undeads",-0.70),("outlaws",-0.60)]),

	("outlaws", "Outlaws", 0, 0.5, [("kingdom_9",-0.05),("kingdom_15",-0.05),("kingdom_23",-0.05),("kingdom_3",-0.05),("kingdom_24",-0.05),("kingdom_10",-0.05),("kingdom_1",-0.05),("kingdom_20",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("kingdom_36",-0.05),("kingdom_11",-0.05),("player_supporters_faction",-0.05),("kingdom_34",-0.05),("kingdom_37",-0.05),("kingdom_25",-0.05),("kingdom_8",-0.05),("kingdom_5",-0.05),("kingdom_42",-0.05),("kingdom_2",-0.05),("kingdom_31",-0.05),("merchants",-0.50),("kingdom_22",-0.05),("kingdom_32",-0.05),("innocents",-0.05),("kingdom_35",-0.05),("player_faction",-0.15),("kingdom_18",-0.05),("kingdom_26",-0.05),("papacy",-0.05),("kingdom_38",-0.05),("kingdom_28",-0.05),("crusade",-0.05),("kingdom_39",-0.05),("kingdom_30",-0.05),("manhunters",-0.60),("kingdom_7",-0.05),("kingdom_16",-0.05),("kingdom_6",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_40",-0.05),("kingdom_4",-0.05),("kingdom_29",-0.05),("commoners",-0.60),("kingdom_41",-0.05),("kingdom_14",-0.05),("kingdom_17",-0.05),("kingdom_27",-0.05)], [], 0x00888888),

	("neutral", "Neutral", 0, 0.1, [], [], 0x00ffffff),

	("innocents", "Innocents", ff_always_hide_label, 0.5, [("outlaws",-0.05),("dark_knights",-0.90)]),

	("merchants", "Merchants", ff_always_hide_label, 0.5, [("forest_bandits",-0.50),("deserters",-0.50),("mountain_bandits",-0.50),("outlaws",-0.50)]),

	("dark_knights", "{!}Dark Knights", 0, 0.5, [("innocents",-0.90),("player_faction",-0.40)]),

	("culture_finnish", "{!}culture finnish", 0, 0.9, []),

	("culture_mazovian", "{!}culture mazovian", 0, 0.9, []),

	("culture_serbian", "{!}culture serbian", 0, 0.9, []),

	("culture_welsh", "{!}culture welsh", 0, 0.9, []),

	("culture_teutonic", "{!}culture teutonic", 0, 0.9, []),

	("culture_balkan", "{!}culture balkan", 0, 0.9, []),

	("culture_rus", "{!}culture rus", 0, 0.9, []),

	("culture_nordic", "{!}culture nordic", 0, 0.9, []),

	("culture_baltic", "{!}culture baltic", 0, 0.9, []),

	("culture_marinid", "{!}culture marinid", 0, 0.9, []),

	("culture_mamluke", "{!}culture mamluke", 0, 0.9, []),

	("culture_byzantium", "{!}culture byzantium", 0, 0.9, []),

	("culture_iberian", "{!}culture iberian", 0, 0.9, []),

	("culture_italian", "{!}culture italian", 0, 0.9, []),

	("culture_andalus", "{!}culture andalus", 0, 0.9, []),

	("culture_gaelic", "{!}culture gaelic", 0, 0.9, []),

	("culture_anatolian_christian", "{!}culture anatolian", 0, 0.9, []),

	("culture_anatolian", "{!}culture anatolian", 0, 0.9, []),

	("culture_scotish", "{!}culture scotish", 0, 0.9, []),

	("culture_western", "{!}culture western", 0, 0.9, []),

	("culture_mongol", "{!}culture mongol", 0, 0.9, []),

	("player_faction", "Player Faction", 0, 0.9, [("black_khergits",-0.30),("player_supporters_faction",1.00),("peasant_rebels",-0.40),("forest_bandits",-0.15),("manhunters",0.10),("deserters",-0.10),("mountain_bandits",-0.15),("undeads",-0.50),("outlaws",-0.15),("dark_knights",-0.40),("commoners",0.10)], [], 0x00cccccc),

	("player_supporters_faction", "Player's Supporters", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("player_faction",1.00),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00468493),

	("kingdom_1", "Teutonic Order", 0, 0.9, [("black_khergits",-0.02),("kingdom_8",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_6",0.50),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_75",-0.50),("kingdom_76",-0.50),("kingdom_77",-0.50),("kingdom_78",-0.50),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_43",-40.00)], [], 0x00e9e9e9),

	("kingdom_2", "Kingdom of Lithuania", 0, 0.9, [("black_khergits",-0.02),("kingdom_3",0.10),("kingdom_36",0.50),("kingdom_34",0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_35",0.50),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_33",0.50)], [], 0x00badeb2),

	("kingdom_3", "Golden Horde", 0, 0.9, [("kingdom_8",0.10),("kingdom_5",-1.00),("kingdom_2",0.10),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("kingdom_7",-1.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00a33e32),

	("kingdom_4", "Kingdom of Denmark", 0, 0.9, [("kingdom_1",0.10),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x009b1a1a),

	("kingdom_5", "Polish Principalities", 0, 0.9, [("kingdom_3",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_7",0.10),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ff0000),

	("kingdom_6", "Holy Roman Empire", 0, 0.9, [("kingdom_1",0.50),("kingdom_42",1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_38",0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_41",1.00)], [], 0x00ffcc00),

	("kingdom_7", "Kingdom of Hungary", 0, 0.9, [("kingdom_3",-1.00),("kingdom_5",0.10),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00289327),

	("kingdom_8", "Novgorod Republic", 0, 0.9, [("kingdom_3",0.10),("kingdom_1",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_14",-0.20)], [], 0x009e0b6f),

	("kingdom_9", "Kingdom of England", 0, 0.9, [("kingdom_37",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("kingdom_79",-0.50),("outlaws",-0.05)], [], 0x00931124),

	("kingdom_10", "Kingdom of France", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00002395),

	("kingdom_11", "Kingdom of Norway", 0, 0.9, [("kingdom_13",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_12",-0.20)], [], 0x006669d6),

	("kingdom_12", "Kingdom of Scotland", 0, 0.9, [("kingdom_11",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0022d8a7),

	("kingdom_13", "Gaelic Kingdoms", 0, 0.9, [("kingdom_11",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0077b322),

	("kingdom_14", "Kingdom of Sweden", 0, 0.9, [("kingdom_1",0.10),("kingdom_8",-0.20),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003254b5),

	("kingdom_15", "Kingdom of Halych-Volhynia", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00ece874),

	("kingdom_16", "Kingdom of Portugal", 0, 0.9, [("kingdom_20",-40.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00003399),

	("kingdom_17", "Crown of Aragon", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0007b233),

	("kingdom_18", "Crown of Castile", 0, 0.9, [("kingdom_20",-40.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00d85ac4),

	("kingdom_19", "Kingdom of Navarre", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00f7f497),

	("kingdom_20", "Emirate of Granada", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_18",-40.00),("crusade",-0.50),("deserters",-0.02),("kingdom_16",-40.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00abc904),

	("papacy", "Papal States", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00fff17a),

	("kingdom_22", "Byzantine Empire", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_26",-1.00),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00760d0d),

	("kingdom_23", "Crusader States", 0, 0.9, [("kingdom_25",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_27",0.10)], [], 0x00f3efb8),

	("kingdom_24", "Kingdom of Sicily", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00799cb5),

	("kingdom_25", "Mamluk Sultanate", 0, 0.9, [("kingdom_23",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_27",-1.00)], [], 0x00ebe800),

	("kingdom_26", "Latin Empire", 0, 0.9, [("peasant_rebels",-0.10),("kingdom_22",-1.00),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00b26248),

	("kingdom_27", "Ilkhanate", 0, 0.9, [("kingdom_23",0.10),("kingdom_25",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e19004),

	("kingdom_28", "Hafsid Dynasty", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00a48460),

	("kingdom_29", "Kingdom of Serbia", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00b38263),

	("kingdom_30", "Bulgarian Empire", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0076a296),

	("kingdom_31", "Marinid Dynasty", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00c1272d),

	("kingdom_32", "Republic of Venice", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00c1172d),

	("kingdom_33", "Yotvingians", 0, 0.9, [("kingdom_2",0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003e7583),

	("kingdom_34", "Prussians", 0, 0.9, [("kingdom_2",0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0065c0d7),

	("kingdom_35", "Curonians", 0, 0.9, [("kingdom_2",0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x003e7583),

	("kingdom_36", "Samogitians", 0, 0.9, [("kingdom_2",0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00529cae),

	("kingdom_37", "Principality of Wales", 0, 0.9, [("kingdom_9",-1.00),("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0000dc00),

	("kingdom_38", "Republic of Genoa", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("crusade",-0.50),("kingdom_39",-0.50),("deserters",-0.02),("kingdom_6",0.50),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e1900a),

	("kingdom_39", "Republic of Pisa", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_38",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x0007e233),

	("kingdom_40", "Guelphs", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_41",-0.80)], [], 0x003254e5),

	("kingdom_41", "Ghibellines", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_6",1.00),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_40",-0.80)], [], 0x009e026a),

	("kingdom_42", "Kingdom of Bohemia", 0, 0.9, [("peasant_rebels",-0.10),("forest_bandits",-0.05),("deserters",-0.02),("kingdom_6",1.00),("mountain_bandits",-0.05),("outlaws",-0.05)], [], 0x00e8e8e8),
#####Kaos Safe Begin

	#MAUAL EDITS REQUIRED
#####Kaos begin add factions correct major faction, also fix the colors for the factions, especially for the start as king/prince, as well as for the rebels/civ.
 #Module factions Search for this line ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []), and place these lines above it
#KAOS (POLITICAL)

#Begin rebels (They are only named this until they win the war, if they win the war) must be double amount of regular factions to test for simple_trigger errors, empire too. *42-84
  ("kingdom_43",  "Teutonics-Prussians", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -40.00)], [], 0x00888888),  #0x00c9c9c9 #Change colors here, as well as relations 0XCC9900 is color, ("forest_bandits", -0.05) means -5 relations against forest bandits, must apply to both factions.
  ("kingdom_44",  "Wendish Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00698064),
  ("kingdom_45",  "Pecheng Clan", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00813229),
  ("kingdom_46",  "Kingdom of Scandinavia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x008a372d),
  ("kingdom_47",  "Pomeralia Principalities",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00872f2f),
  ("kingdom_48",  "Empire of Germania",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x008c7001),
    ("kingdom_49",  "Empire of Carpathia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00278c25),
  ("kingdom_50",  "Kievan Rus",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006555d6), #0x00E714A3
  ("kingdom_51",  "Kingdom of Brittania", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006a1c12),
  ("kingdom_52",  "New Francia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00243777),
  ("kingdom_53",  "Kingdom of Norge",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x000f1d67),
  ("kingdom_54",  "Chiefdom of Kemi",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00105a46),
    ("kingdom_55",  "Kingdom of Ireland", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0048720e),
  ("kingdom_56",  "Chiefdom of Sapmi",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00314375),
  ("kingdom_57",  "Kingdom of Galicia-Volhynia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00737013),
  ("kingdom_58",  "Hispania",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00002b80),
  ("kingdom_59",  "Principality of Catalonia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00035218),
  ("kingdom_60",  "Crown of Leon",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00572850),
    ("kingdom_61",  "Kingdom of Vasconia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006d6b44),
  ("kingdom_62",  "Ahlidid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00485500),
  ("kingdom_63",  "Union of Papacy", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00817408),
  ("kingdom_64",  "Eastern Roman Empire",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00440000),
  ("kingdom_65",  "Kingdom of Armenia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00858369),
  ("kingdom_66",  "Kingdom of Apulia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x002c4557),
    ("kingdom_67",  "Hashimid Emirate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006f6d00),
  ("kingdom_68",  "Empire of Aegean", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x008c5341),
  ("kingdom_69",  "Kingdom of Georgia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00ed370b), #Red
  ("kingdom_70",  "Maghrawavid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006F6457),
  ("kingdom_71",  "Kingdom of Epirius",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00338681),
  ("kingdom_72",  "Kingdom of Karvuna-Moesia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00394f49),
    ("kingdom_73",  "Zayanid Dynasty", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00803739),
  ("kingdom_74",  "Kingdom of Croatia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00881184),
  ("kingdom_75",  "Middle Rurikid Dynasty", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_78", 0.85),("kingdom_76", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x00566f75),
  ("kingdom_76",  "West Rurikid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_78", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x0048DAFF),
  ("kingdom_77",  "East Rurikid Dynasty",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_76", 0.85),("kingdom_78", 0.85),("forest_bandits", -0.05)], [], 0x00B1EFFF),
  ("kingdom_78",  "North Rurikid Dynasty",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_76", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x0028464f),
    ("kingdom_79",  "Kingdom of Gwynedd", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_9", -0.80),("forest_bandits", -0.05)], [], 0x00526652),
  ("kingdom_80",  "Most Serene House Doria",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FFAD26),
  ("kingdom_81",  "Most Serene House D'Appiano", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00F19E0E),
  ("kingdom_82",  "Kingdom of Italy",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00a19c7d),
  ("kingdom_83",  "Kingdom of Florence",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x005d1144),
  ("kingdom_84",  "Kingdom of House Premyslid",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0075728a),
#End rebels

##Begin rebels old colors
#  ("kingdom_43",  "Teutonics-Prussians", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -40.00)], [], 0x00888888),  #0x00c9c9c9 #Change colors here, as well as relations 0XCC9900 is color, ("forest_bandits", -0.05) means -5 relations against forest bandits, must apply to both factions.
#  ("kingdom_44",  "Wendish Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x009DC196),
#  ("kingdom_45",  "Pecheng Clan", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00a33e32),
#  ("kingdom_46",  "Kingdom of Scandinavia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00EC5D4C),
#  ("kingdom_47",  "Pomeralia Principalities",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FF5A5A),
#  ("kingdom_48",  "Empire of Germania",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00BD9700),
#    ("kingdom_49",  "Empire of Carpathia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x003DD93B),
#  ("kingdom_50",  "Kievan Rus",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00700c50), #0x00E714A3
#  ("kingdom_51",  "Kingdom of Brittania", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00DE3622),
#  ("kingdom_52",  "New Francia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x003D69FA),
#  ("kingdom_53",  "Kingdom of Norge",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FF3737),
#  ("kingdom_54",  "Chiefdom of Kemi",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00157B5F),
#    ("kingdom_55",  "Kingdom of Ireland", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0090E715),
#  ("kingdom_56",  "Chiefdom of Sapmi",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00668EFF),
#  ("kingdom_57",  "Kingdom of Galicia-Volhynia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FFF826),
#  ("kingdom_58",  "Hispania",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x000055FF),
#  ("kingdom_59",  "Principality of Catalonia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0004681E),
#  ("kingdom_60",  "Crown of Leon",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0078366E),
#    ("kingdom_61",  "Kingdom of Vasconia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00ADAA6A),
#  ("kingdom_62",  "Ahlidid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00586800),
#  ("kingdom_63",  "Union of Papacy", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00F0D80B),
#  ("kingdom_64",  "Eastern Roman Empire",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x004E0000),
#  ("kingdom_65",  "Kingdom of Armenia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FFFFFF),
#  ("kingdom_66",  "Kingdom of Apulia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x003B5D75),
#    ("kingdom_67",  "Hashimid Emirate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x007A7800),
#  ("kingdom_68",  "Empire of Aegean", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FF8C66),
#  ("kingdom_69",  "Kingdom of Georgia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00855400),
#  ("kingdom_70",  "Maghrawavid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006F6457),
#  ("kingdom_71",  "Kingdom of Epirius",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00B86938),
#  ("kingdom_72",  "Kingdom of Karvuna-Moesia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x004C6961),
#    ("kingdom_73",  "Zayanid Dynasty", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00BB4C50),
#  ("kingdom_74",  "Kingdom of Croatia",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00B916B4),
#  ("kingdom_75",  "Middle Rurikid Dynasty", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_78", 0.85),("kingdom_76", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x006C8B93),
#  ("kingdom_76",  "West Rurikid Dynasty",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_78", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x0048DAFF),
#  ("kingdom_77",  "East Rurikid Dynasty",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_76", 0.85),("kingdom_78", 0.85),("forest_bandits", -0.05)], [], 0x00B1EFFF),
#  ("kingdom_78",  "North Rurikid Dynasty",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_1", -0.50),("kingdom_75", 0.85),("kingdom_76", 0.85),("kingdom_77", 0.85),("forest_bandits", -0.05)], [], 0x00376571),
#    ("kingdom_79",  "Kingdom of Gwynedd", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("kingdom_9", -0.80),("forest_bandits", -0.05)], [], 0x00A0D1A0),
#  ("kingdom_80",  "Most Serene House Doria",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FFAD26),
#  ("kingdom_81",  "Most Serene House D'Appiano", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00F19E0E),
#  ("kingdom_82",  "Kingdom of Italy",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00A1ADE1),
#  ("kingdom_83",  "Kingdom of Florence",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00D8239C),
#  ("kingdom_84",  "Kingdom of House Premyslid",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00aca6ce),
#  #End old colors


#Begin Civil (If rebels win the war, they change to a civil faction below). #84-126 for testing
#  ("kingdom_85",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_86",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_87",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_88",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_89",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_90",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_91",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_92",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_93",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_94",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_95",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_96",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_97",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_98",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_99",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_100",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_101",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_102",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_103",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_104",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_105",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_106",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_107",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_108",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_109",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_110",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_111",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_112",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_113",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_114",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_115",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_116",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_117",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_118",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_119",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_120",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),
#    ("kingdom_121",  "Empire Of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC9900),
#  ("kingdom_122",  "Empire Of Vaegir",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X669999),
#  ("kingdom_123",  "Khergit Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCC66FF),
#  ("kingdom_124",  "Empire Of Nord",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X3333FF),
#  ("kingdom_125",  "Empire Of Rhodok",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0X99FF66),
#  ("kingdom_126",  "Sarranid Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0XCCFF66),

#End civil
#KAOS (POLITICAL)
#####Kaos Safe End
#####Kaos end add faction
	("kingdoms_end", "{!}kingdoms end", 0, 0.0, []),

	("robber_knights", "{!}robber knights", 0, 0.1, []),

	("khergits", "{!}Khergits", 0, 0.5, []),

	("black_khergits", "{!}Black Khergits", 0, 0.5, [("kingdom_1",-0.02),("kingdom_2",-0.02),("player_faction",-0.30)]),

	("manhunters", "Manhunters", 0, 0.5, [("forest_bandits",-0.60),("player_faction",0.10),("deserters",-0.60),("mountain_bandits",-0.60),("outlaws",-0.60)]),

	("deserters", "Deserters", 0, 0.5, [("kingdom_9",-0.02),("kingdom_15",-0.02),("kingdom_23",-0.02),("kingdom_3",-0.02),("kingdom_24",-0.02),("kingdom_10",-0.02),("kingdom_1",-0.02),("kingdom_20",-0.02),("kingdom_13",-0.02),("kingdom_19",-0.02),("kingdom_36",-0.02),("kingdom_11",-0.02),("player_supporters_faction",-0.02),("kingdom_34",-0.02),("kingdom_37",-0.02),("kingdom_25",-0.02),("kingdom_8",-0.02),("kingdom_5",-0.02),("kingdom_42",-0.02),("kingdom_2",-0.02),("kingdom_31",-0.02),("merchants",-0.50),("kingdom_22",-0.02),("kingdom_32",-0.02),("kingdom_35",-0.02),("player_faction",-0.10),("kingdom_18",-0.02),("kingdom_26",-0.02),("papacy",-0.02),("kingdom_38",-0.02),("kingdom_28",-0.02),("crusade",-0.02),("kingdom_39",-0.02),("kingdom_30",-0.02),("manhunters",-0.60),("kingdom_7",-0.02),("kingdom_16",-0.02),("kingdom_6",-0.02),("kingdom_12",-0.02),("kingdom_33",-0.02),("kingdom_40",-0.02),("kingdom_4",-0.02),("kingdom_29",-0.02),("kingdom_41",-0.02),("kingdom_14",-0.02),("kingdom_17",-0.02),("kingdom_27",-0.02)], [], 0x00888888),

	("mountain_bandits", "Mountain Bandits", 0, 0.5, [("kingdom_9",-0.05),("kingdom_15",-0.05),("kingdom_23",-0.05),("kingdom_3",-0.05),("kingdom_24",-0.05),("kingdom_10",-0.05),("kingdom_1",-0.05),("kingdom_20",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("kingdom_36",-0.05),("kingdom_11",-0.05),("player_supporters_faction",-0.05),("kingdom_34",-0.05),("kingdom_37",-0.05),("kingdom_25",-0.05),("kingdom_8",-0.05),("kingdom_5",-0.05),("kingdom_42",-0.05),("kingdom_2",-0.05),("kingdom_31",-0.05),("merchants",-0.50),("kingdom_22",-0.05),("kingdom_32",-0.05),("kingdom_35",-0.05),("player_faction",-0.15),("kingdom_18",-0.05),("kingdom_26",-0.05),("papacy",-0.05),("kingdom_38",-0.05),("kingdom_28",-0.05),("crusade",-0.05),("kingdom_39",-0.05),("kingdom_30",-0.05),("manhunters",-0.60),("kingdom_7",-0.05),("kingdom_16",-0.05),("kingdom_6",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_40",-0.05),("kingdom_4",-0.05),("kingdom_29",-0.05),("commoners",-0.20),("kingdom_41",-0.05),("kingdom_14",-0.05),("kingdom_17",-0.05),("kingdom_27",-0.05)], [], 0x00888888),

	("forest_bandits", "Forest Bandits", 0, 0.5, [("kingdom_9",-0.05),("kingdom_15",-0.05),("kingdom_23",-0.05),("kingdom_3",-0.05),("kingdom_24",-0.05),("kingdom_10",-0.05),("kingdom_1",-0.05),("kingdom_20",-0.05),("kingdom_13",-0.05),("kingdom_19",-0.05),("kingdom_36",-0.05),("kingdom_11",-0.05),("player_supporters_faction",-0.05),("kingdom_34",-0.05),("kingdom_37",-0.05),("kingdom_25",-0.05),("kingdom_8",-0.05),("kingdom_5",-0.05),("kingdom_42",-0.05),("kingdom_2",-0.05),("kingdom_31",-0.05),("merchants",-0.50),("kingdom_22",-0.05),("kingdom_32",-0.05),("kingdom_35",-0.05),("player_faction",-0.15),("kingdom_18",-0.05),("kingdom_26",-0.05),("papacy",-0.05),("kingdom_38",-0.05),("kingdom_28",-0.05),("crusade",-0.05),("kingdom_39",-0.05),("kingdom_30",-0.05),("manhunters",-0.60),("kingdom_7",-0.05),("kingdom_16",-0.05),("kingdom_6",-0.05),("kingdom_12",-0.05),("kingdom_33",-0.05),("kingdom_40",-0.05),("kingdom_4",-0.05),("kingdom_29",-0.05),("commoners",-0.20),("kingdom_41",-0.05),("kingdom_14",-0.05),("kingdom_17",-0.05),("kingdom_27",-0.05)], [], 0x00888888),

	("undeads", "{!}Undeads", 0, 0.5, [("player_faction",-0.50),("commoners",-0.70)]),

	("slavers", "{!}Slavers", 0, 0.1, []),

	("peasant_rebels", "{!}Peasant Rebels", 0, 1.0, [("kingdom_9",-0.10),("kingdom_15",-0.10),("kingdom_23",-0.10),("kingdom_3",-0.10),("kingdom_24",-0.10),("kingdom_10",-0.10),("noble_refugees",-1.00),("kingdom_1",-0.10),("kingdom_20",-0.10),("kingdom_13",-0.10),("kingdom_19",-0.10),("kingdom_36",-0.10),("kingdom_11",-0.10),("player_supporters_faction",-0.10),("kingdom_34",-0.10),("kingdom_37",-0.10),("kingdom_25",-0.10),("kingdom_8",-0.10),("kingdom_5",-0.10),("kingdom_42",-0.10),("kingdom_2",-0.10),("kingdom_31",-0.10),("kingdom_22",-0.10),("kingdom_32",-0.10),("kingdom_35",-0.10),("player_faction",-0.40),("kingdom_18",-0.10),("kingdom_26",-0.10),("papacy",-0.10),("kingdom_38",-0.10),("kingdom_28",-0.10),("crusade",-0.10),("kingdom_39",-0.10),("kingdom_30",-0.10),("kingdom_7",-0.10),("kingdom_16",-0.10),("kingdom_6",-0.10),("kingdom_12",-0.10),("kingdom_33",-0.10),("kingdom_40",-0.10),("kingdom_4",-0.10),("kingdom_29",-0.10),("kingdom_41",-0.10),("kingdom_14",-0.10),("kingdom_17",-0.10),("kingdom_27",-0.10)]),

	("noble_refugees", "{!}Noble Refugees", 0, 0.5, [("peasant_rebels",-1.00)]),

	("crusade", "Crusaders", 0, 0.9, [("kingdom_3",-0.50),("kingdom_20",-0.50),("kingdom_36",-0.50),("kingdom_34",-0.50),("kingdom_25",-0.50),("kingdom_2",-0.50),("kingdom_31",-0.50),("peasant_rebels",-0.10),("forest_bandits",-0.05),("kingdom_35",-0.50),("papacy",-0.50),("kingdom_38",-0.50),("kingdom_28",-0.50),("deserters",-0.02),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_33",-0.50),("kingdom_27",-0.50)], [], 0x00fff17a),

	("end_minor_faction", "Village Idiots", 0, 0.9, [], [], 0x00fff17a),

]