![Logo of the project](https://media.moddb.com/images/mods/1/30/29657/auto/CKOgYyl.png)

![Picture](https://media.moddb.com/images/mods/1/30/29657/20160816104143_1.jpg)

![Picture](https://media.moddb.com/images/mods/1/30/29657/20160710093713_1.jpg)

![Picture](https://media.moddb.com/cache/images/mods/1/30/29657/thumb_620x2000/20160817014210_1.jpg)


# Medieval Conquests
Medieval Conquests is a Medieval Ages complete overhaul for the Mount & Blade: Warband, this modification takes you back to the 13th century with a fresh new campaign and an improved networking code re-structure for viable co-operative gaming.

From this point on the player and the computer lords shape the land and fight for supremacy and control of the continent in a political landscape full of intrigue and supremacy.

## Installing / Getting started

A quick introduction of the minimal setup you need to get Medieval Conquests up and running
1. Make sure you have a copy of Mount & Blade: Warband video game
2. Download the latest build from Moddb at: https://www.moddb.com/mods/medieval-conquests or at the github's release page.
3. Insert the module into the Modules folder in your game folder, launch the game and switch the module from the launcher into the name of the overhaul.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

unfortunately Python 3 is not supported by the warband module system, so you'll have to install Python 2.7 in order to further develop this project, here are some steps to install Python 2.7 easily, but any other method would work as long as the version between 2 to 2.8 of Python.

First, git clone the repository for the latest source code.
```shell
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src
sudo tar xzf Python-2.7.16.tgz
sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
cd Python-2.7.16
sudo ./configure --enable-optimizations
sudo make altinstall
```

1. After installing Python, obtain the latest build files from ModDb hosting website or at the github release page.
2. Adjust the export directory within module_info.py to the game's full module folder.
3. Run build_module.bat and wait for the compilation to finish.
4. Once the compilation finishes successfully, attempt to launch the project within the game Mount & Blade: Warband's by switching the Module from "Native" to the project's name.
5. Play and enjoy your new changes.


## Features
The features of the overhaul are listed in descending order from latest additions to oldest.

- Faction forming system with potentional coup's, independence, rebellions, civil wars and more!
- Simplified upgrade all troops menu allowing player to upgrade troops to their choice with just one click.
- Dynamic UI (3) depending on which faction you are part of.
- Hundreds of new events depending on your character status (King-vassal-neither).
- World-map events such as storms, floods, fires, epidemics and more.
- Ability to join any encounter regardless of relations.
- Ability to adjust minimum size of all garrisons & parties.
- Particle effects for hitting shields & weapon breaking.
- Hardcore mode, as well as player permadeath, hardcore mode makes several changes to the game making every battle important towards your characters wellbeing, with persistant injuries, and other things to discover.
- Extended camera mode, allowing the player to adjust the camera to their preference, you can now view in your character in a top down view, and any angle you want.
- Troops use torches during night-time.
- Enhanced skybox and time of day.
- Several new games to discover in taverns!
- New improved looting and inventory system, as well as browse attributes of lords etc with LAV's companion overseer.
- Multiple starting choices ranging from a Monarchy to a lowly bandit! (Monarch, Prince/Princess, Vassal, Adventurer, Bandit).
- AI lords can die within the game.

-Succession system for lords
- Troop ratio bar showing the current balance of forces and who is winning.
- Terrain-aware music system for tense situations, and combat situations, as well as sieges, in both SP & Co-Op/MP.
- Factional sounds depending on which faction you are part of, and depending on your status (king-vassal-none).
- Some dynamic heraldic armors
- Marriage and family titles
- English names and Titles for the nobility.
- Lords execution system with dynamic changes in the game depending on the actions.
- Offers a lot of customization, from UI Elements to in-game elements.
- Ability to reform the Roman Empire as the Byzantine Empire Monarch start.
- Dynamic weapons & Dynamic banners
- Armies can now crouch on command
- Low walking
- Full support for dedicated and listens servers MP/Co-Op.
- More visual effects depending on the situations.
- Random Events while travelling some with benefits/consequences depending on the choice you choose!
- Realistic Ballistics.
- Realistic sounds from hitting a wooden shield to grunting and death sounds.
- Improved AI drastically, you can press F5 to adjust the AI settings.
- Better female textures.
- Better Blood Splatters & Blood Textures.
- Includes Battle_Time re-coded to work properly under the latest version of warband, and now you don't even need WSE to join multiplayer games, only to host them, Linux & Mac players can rejoice about this, now its possible to experience some co-op easily!
- Play your campaign in singleplayer and your battles in multiplayer.
- When you fight a battle, siege, or attack a village, host a multiplayer game so your friends can help you win the fight.
- Use a dedicated server so that players do not need to reconnect for each battle.
- Anyone that joins the MP battle can choose to be the player, a companion in the player's SP party, any lord from either team, or a random regular soldier.
- Take command of a troop division or all the troops from your chosen party.
- The main party inventory is available during the MP battle by choosing "Access Inventory" from the Esc menu before spawning or using the box at your spawn point.
- The multiplayer battle will have the correct scene, troops (weapons and skills), banners, and weather.
- After the battle, load your saved game and apply the results from the multiplayer battle.
- Great for LAN play or online with voice chat and screen sharing software.
- Battle Time uses the Warband Script Enhancer (Only required for hosts, not players joining), adding more features and support for dedicated servers.
Mission types that can use co-op:
- Normal encounter
- Join a battle
- Join a siege assault
- Siege attack
- Defend castle you are in
- Village attacked by bandits
- Village raid attacked by lord
- Village raid defended by lord
- Village attack when looting them
- Village train peasants
- Bandit lairs
- Improved animations
- New textures to fonts and interfaces such as the inventory, notes, and other sections
- All of Europe, featuring 42 factions, with another 42 possible to form.
- Hundred of new historical, region based troops.
- More then a thousand new items, armors, weapons, all historically accurate for XIII century.
- Buildable castles.
- Manor system, with the ability to build custom settlements (build buildings appear in the scene!)
- Realistic combat system, with taunts, formations, improved horse archer skirmishing scripts and other features.
- Custom battle scenes, realistically depicting each region of Europe.
- Weather system, including desert storms, blizzards, rain storms
- Play as one of your soldiers after your death, with our made auxiliary player feature (can be turned off in the mod options).
- Cruading system: Join a crusade or start one yourself!
- Join a crusader order as sergeant or a knight!
- New lance recruitment system, aiming to emulate medieval feudal recruitment system.
- Companion system improved and remade
- Sea battles and sea travel
- Many new scenes for castles, towns and villages. A good number of them - are historically based reconstructions of real places!
- All lords have proper titles according to their faction.
- Many other minor and major features!

## Contributing

This project is licensed under MIT, so feel free to contribute and re-release the overhaul as long as you provide credits.

This module had been built on top of 1257AD's source code, with several contributors listed in the taleworlds page.

## Links
- Project homepage: https://www.moddb.com/mods/medieval-conquests
- Mirror 1: https://www.nexusmods.com/mbwarband/mods/6128
- Mirror 2: https://forums.taleworlds.com/index.php?topic=349371.0
- Repositories and my other projects: https://github.com/faycalki/
  - In case of sensitive bugs like security vulnerabilities, please feel free to contact me whenever, I value all efforts to improve the security of the project.
