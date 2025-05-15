# This is where game :3

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, os

pygame.mixer.init()

musicFilePath = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.music.load(os.path.join(musicFilePath,'Hazed in a haste.mp3'))

pygame.mixer.music.play(loops=-1)

# rooms info
class RoomInfo:
    """klass som innehåller info inom alla rum"""

    def __init__(self, name = "Unnamed room", descriptions = "This is an undescribed room", choices = ""):
        self.name = name
        self.descriptions = descriptions
        self.choices = dict(choices)

# Where the game progress bools are stored

progressBooleans = {"Entered forest":[False],
                    "Entered deeper_forest":[False],
                    "Entered graveyard":[False],
                    "Entered misty_lake":[False],
                    "Entered misty_lake_island":[False],
                    "Entered misty_lake2":[False],
                    "Entered cave_entrance":[False],
                    "Entered cave":[False],
                    "Entered outside_cabin":[False],
                    "Entered behind_cabin":[False],
                    "Entered inside_cabin1":[False],
                    "Entered inside_cabin2":[False],
                    "Entered window":[False],
                    "Entered stairs":[False],
                    "Entered hallway":[False],

                    "Examined deeper_forest":[False, "Can examine deeper_forest"],
                    "Can examine deeper_forest":[True],
                    "Has wooden_key":[False, "Can collect wooden_key"],
                    "Can collect wooden_key":[True],

                    "Examined misty_lake_island":[False, "Can examine misty_lake_island"],
                    "Can examine misty_lake_island":[True],
                    "Has shovel":[False, "Can collect shovel"],
                    "Can collect shovel":[True],

                    "Examined graveyard":[False, "Can examine graveyard"],
                    "Can examine graveyard":[True],
                    "Dug johnsson_grave":[False, "Can dig johnsson_grave"],
                    "Can dig johnsson_grave":[True],
                    "Dug nameless_grave":[False, "Can dig nameless_grave"],
                    "Can dig nameless_grave":[True],
                    "Has dynamite":[False, "Can collect dynamite"],
                    "Can collect dynamite":[True],
                    "Has metal_key":[False, "Can collect metal_key"],
                    "Can collect metal_key":[True],
                    
                    "Has lighter":[False, "Can collect lighter"],
                    "Can collect lighter":[True],

                    "Opened_cave":[False, "Can open cave"],
                    "Can open cave":[True],
                    "Has lockpick":[False, "Can collect lockpick"],
                    "Can collect lockpick":[True],
                    
                    "door_unlocked":[False, "Can unlock door"],
                    "Can unlock door":[True]}

doingActions = {"isExaminating":False}


# This is where the descriptions for the rooms are made
# The first in the list is for first entry into the room, and the second is for every other entry

roomDescriptions = {"forest":["You wake up in the middle of a forest.\n\nit's quiet and dark.\n"
                              "You take a look around, and in the corner of your eye you spot something.\n"
                              "That, SOMETHING, seems to dissapear quicker than you even think about turning your head.\n"
                              "Maybe it was just an illusion cuased by your starteled mind.\n"
                              "That mind of yours can't even rememeber what your name is.\n"
                              "Given the time to breathe, you take a further look on the enviroment you find yourself in.\n"
                              "It's foggy a bit into the horizon...\n"
                              "It seems like a pillar of smoke comes from somewhere in the woods",

                              "You are back at the forest.\nit's quieter than before"],

                    "deeper_forest":["You walk through the forest, unaware of what might be lurking past the fog a few throws away\n"
                                     "It is as if a thick atmosphere surrounds you.\n"
                                     "Chills, even though it's not that cold.",

                                     "You go into the thick of the forest.\nYet again you get surrounded by the atmosphere",

                                     ["As you look around, a fallen log catches your eye.\n"
                                     "The top of a stick extruding from the log seems oddly shaped like a key",
                                     "isExaminating"]],

                    "graveyard":["The thick forest clears, showing what seems to be a graveyard.\n"
                                 "You enter the gate, as it creaks like any form of door in a horror movie for some reason.\n"
                                 "Suddenly it feels like something cold approaches you from behind.\n"
                                 "It's as if something placed their chilling, unnatrual hand on your shoulder.\n"
                                 "You turn around in a haste.\n"
                                 "Noone there.\n\n"
                                 "You once again look at the gate, shivering this time.\n",

                                 "At the graveyard again.\n"
                                 "You hear a crow in the distance. Or is it a raven?\n"
                                 "The gate creaks just like before.\nJust like the piercing regret of disturbing the dead.",
                                 
                                 ["Your mind feels fuzzy.\n"
                                  "You look around, an two graves catches your eye:\n"
                                  "Johnsson and... an unnamed grave.\n"
                                  "It looks like the graves have recently been dug up and reburied.\n"
                                  "You might need something like a shovel for that.\n\n"
                                  "There also seems to be an unlit candle on top of one of the gravestones.\nJohnssons.", "isExaminating"]],

                    "misty_lake":["Your vision starts to shorten as you head torwards the fog.\n"
                                  "As the fog surrounds you more and more. It starts to get rather humid.\n\n"
                                  "Your leg bumps into something. A boat!\n"
                                  "You are next to a lake.\n"
                                  "Eyeing the lake, you see an island in the middle of the lake, just bareley withing your viewing distance.",
                                  
                                  "The same atmosphere of thick, humid air surrounds you yet again."],
                                
                    "misty_lake_island":["The boat slowly floats over the silent surface of the water.\n"
                                         "It feels like the fog is getting more dense.\n\n"
                                         "Suddenly, it feels like something rocks the boat.\n"
                                         "*...aaaaaahhhhhh-*\n"
                                         "You quickly try to see what it is.\n"
                                         "nothing\n\n"
                                         "The boat hits the shore of the island and you step out of the boat",
                                         
                                         "Your boat slowly drags onto the shore of the island.\n"
                                         "The island feels disconnected from the rest of the foggy area.",
                                         
                                         ["You are surspised you can actually see further than 5 meters in front of you.\n"
                                          "Right by a shack, on the other side of the island, you see a shovel, just laying there.", 
                                          "isExaminating"]],

                    "misty_lake2" : ["The boat slowly heads back.\n"
                                     "It almost feels transcendent with how quiet and still it is.\n"
                                     "The smooth ripples on the surface of the water,\n"
                                     "the calm, bareley noticable swoosh of the water being moved by the boat...\n"
                                     "*Donk* \nThe boat hits the shore, you get up.",

                                     "The boat slowly heads back.\n"
                                     "It almost feels transcendent with how quiet and still it is.\n"
                                     "The smooth ripples on the surface of the water,\n"
                                     "the calm, bareley noticable swoosh of the water being moved by the boat...\n"
                                     "*Donk* \nThe boat hits the shore, you get up."],
                                     
                    "outside_cabin" : ["You head up to this house in the middle of the forest.\n"
                                       "Maybe you could finaly get some help by someone!\n"
                                       "You walk up to the door with hope.\n\n"
                                       "It's locked.\n"
                                       "There has to be a way in somehow!",
                                       
                                       "Yet again you find yourself at this woodland cabin.\n"
                                       "You know this must be the end of this weird nightmare you woke up in!"],
                                       
                    "behind_cabin" : ["You walk around the cabin and investigate.\n"
                                      "There seems to be a window here.\n"
                                      "Hmm, is there someone in there?\n"
                                      "Someone seems to be standing in the house far from the window.\n\n"
                                      "You lean in closer, for a better lo- AAAAAAHHH!-\n"
                                      "That p-person teleported from the opposite side to right in front of the window!\n"
                                      "Startled you look around in utter fear and confusion'.\n"
                                      "There seems to be a lighter on the ground!\n"
                                      "When you look up torwards the window you notice the persons abcense.",
                                      
                                      "Behind the cabin. What would you have to do here?"],
                                      
                    "cave_entrance" : ["It seems as a natrual wall of stone towers above you.\n"
                                       "There seems to be a crack in this giant wall of stone.\n"
                                       "But there is no way you're breaking through with just your arms.",

                                       "You're back at the supposedly mountainface\n"
                                       "You can't really see up that well because of the trees"],
                                       
                    "cave" : ["You take a step into the large cavern.\n"
                              "*STEP*- *step*- *s t e p*\n"
                              "Any sound gets echoed.\n"
                              '"Hello!", you say\n'
                              '"HELLO!"- "Hello"- "hello"- "h e l l o"-\n'
                              '"hi"-\n'
                              "You didn't say that.\n"
                              "...eeeheeheheh.-\n"
                              '"W-who is there?", you ask\n'
                              "...\n\n"
                              "Before you know it, you are at the end of the cave.\n"
                              "You take a look around.\n"
                              "There seems to be something on the ground, it looks like a lockpick.",
                              
                              "The cave is equally as echo-ey as before."],
                              
                    "inside_cabin1" : ["*Creeeeeeeaaaak*\n"
                                      "H-hello? Anyone there?\n"
                                      "You step inside.\n"
                                      "It's quiet.",
                                    
                                      "*Creeeeeeeaaaak*\n"
                                      "Maybe this is where you will get your answers."],
                                      
                    "inside_cabin2" : ["You step into the hall.\n"
                                       "There's a window to your left.\n"
                                       "It's where that person stood.\n"
                                       "There also seems to be a door that leads to a room.\n\n"
                                       "You try to open it.\n"
                                       "It's also locked.\n"
                                       "You try to use your lockpick.\n"
                                       "neither does that work.",
                                       
                                       "The door seems to almost speak to you.\n"
                                       "it's as if there is something that wants you to enter."],
                                       
                    "stairs" : ["You take a step down.\n"
                                "You stop, questioning if you wanna do this.\n"
                                "*step*\n\n"
                                "You take a look behind you.\n"
                                "It's them.\n"
                                "Right by the door which is ajar.\n"
                                "They start closing it.\n"
                                '"No no no NO NO N-"\n'
                                "It's locked.\n"
                                "You can not go back.",
                                
                                "You're not supposed to be here..."],
                                
                    "hallway" : ["Just when you thougt it couldn't get any darker, it just keeps getting.\n"
                                 "*step*\n"
                                 "step.\n"
                                 "step...\n\n"
                                 "you feel empty\n\n"
                                 "you feel like it doesn't matter\n\n"
                                 "you've given up\n\n"
                                 "*...whooooooOOOoOOoOOOOOOSH*-\n"
                                 "Suddenly, you get surrounded by a wind, just like before!\n"
                                 "It just gets louder and louder.\n"
                                 "You cover your ears.\n\n"
                                 "All of the sudden, it stops.\n"
                                 "You open your eyes.\n"
                                 "You are back in the middle of the forest.\n"
                                 "You see someone, unconcios, laying in the woods.\n"
                                 "They wake up, and look around them in confusion and fear.\n"
                                 "Their eyes quickly glance on you.\n"
                                 "You seems to get- ripped out of this world and dissapear.\n\n"
                                 "You just realised who that was\n\n"
                                 "That was you\n\n\n"]}


exceptionDescription = ""


# defining the choices you have

# First, like "forest", is the name of the room
# Second, like "Go deeper_forest", is the commands that are available
# Third, like ["Go deeper into the forest"], is the description of the action
# Fourth, Something like ["", ["Has wooden_key"]], is the boolean required to do the action
# And finally, something like ["", [""], "You take a hold of the key"], is the text that is written after the action
ChoicesList = {"forest" : {"Go deeper_forest":["Go deeper into the forest"],
                           "Go graveyard":["Head torwards the clearing of the forest"],
                           "Go misty_lake":["Go torwards the thicker fog"],
                           "Go outside_cabin":["Head torwards that pillar of smoke"],
                           "Go cave_entrance":["Go torwards the mountainous wall of stone"]},

               "deeper_forest" : {"Go forest":["Go back to the middle of the forest where you woke up"],
                                  "Examine deeper_forest":["Examine your surroundings", ["Can examine deeper_forest"]],
                                  "Collect wooden_key":["Grab the wooden key", ["Examined deeper_forest", "Can collect wooden_key"],
                                                        "You take a hold of the key.\n"
                                                        "It's like if it's growing out of the wood.\n"
                                                        "*Snap*\n"
                                                        "Got it!"]},

                "graveyard" : {"Go forest":["Go back torwards the forest"],
                               "Examine graveyard":["Examine the graveyard", ["Can examine graveyard"]],
                               "Dig johnsson_grave":["Dig up Johnssons grave", ["Has shovel", "Examined graveyard", "Can dig johnsson_grave"],
                                                      """You dig up the grave.\nAs you reach the coffin you slowly open it with fear.\n"""
                                                      """It's... empty...\n"""
                                                      """What could've happened to this ''Johnsson''?"""],

                               "Dig nameless_grave":["Dig up the nameless grave", ["Has shovel", "Examined graveyard", "Can dig nameless_grave"],
                                                     """The lack of name only fills your head with the most horrific thoughts of what lie underneath the soil.\n"""
                                                     """You pick up the- ''coffin'', and it seems a bit too small to fit a body...\n"""
                                                     """Seems like it's locked."""],
                                "Collect dynamite":["Open the ''coffin'' with the wooden key", ["Has wooden_key", "Dug nameless_grave", "Can collect dynamite"],
                                                    "You open the box.\n"
                                                    "To your relief there isn't a messed up body or something like that in the box.\n"
                                                    "It's a stick of dynamite."],
                                "Collect metal_key":["Light the candle", ["Examined graveyard", "Has lighter", "Can collect metal_key"],
                                                     "You take a look at the candle.\n"
                                                     "It hasn't been lit before.\n"
                                                     "You light it.\n\n"
                                                     "*Swoosh*\n"
                                                     "The candle goes out. The wind stops.\n\n"
                                                     "...\n\n"
                                                     "All of the sudden, A strong wind picks up and circles around you!\n"
                                                     "Voices start groaning faintly.\n"
                                                     "Something seems to materialize in front of you with such light.\n"
                                                     "A key, made of metal, pops into existance and falls right into your\nhands as quickly as the wind dissapears.\n"
                                                     "The candle is gone."]},

                "misty_lake" : {"Go misty_lake_island":["Take the boat to the island"],
                                "Go forest":["Go back to the forest"]},

                "misty_lake_island" : {"Go misty_lake2":["Take the boat back to the mainland"],
                                       "Examine misty_lake_island":["Examine your surroundings.", ["Can examine misty_lake_island"]],
                                       "Collect shovel":["Collect the shovel", ["Examined misty_lake_island", "Can collect shovel"],
                                       """You grab the shovel.\n"""
                                       """It feels a bit cold"""]},

                "misty_lake2" : {"Go forest":["Go back torwards the forest"],
                                 "Go misty_lake_island":["Take the boat back to the island"]},
                                 
                "outside_cabin" : {"Go forest":["Head back to the forest"],
                                   "Go behind_cabin":["Walk around the building"],

                                   "Say":["Try to open the door", ["Can collect lockpick"],
                                    """You try to open the door.\n"""
                                    """Locked!\n"""
                                    """You would need something for that lock"""],

                                    "Go inside_cabin1":["Use the lockpick to open the door", ["Has lockpick"]]},
                                    
                "behind_cabin" : {"Go outside_cabin":["Go back around the cabin"],
                                  "Collect lighter":["Grab the lighter", ["Can collect lighter"],
                                  """You grab the lighter."""]},
                                  
                "cave_entrance" : {"Go forest":["Return to the forest"],
                                   "Set Opened_cave":["Blow up the crack in the wall of the mountain", ["Can open cave", "Has dynamite", "Has lighter"],
                                                      "You light the dynamite, place it by the wall and run for cover.\n"
                                                      "You sit down behind a tree.\n"
                                                      "What was that?\n\n"
                                                      "You look up to see a mysterious figure.\n"
                                                      "A humaniod, seemingly glowing, stands about 5 meters in front of you.\n"
                                                      "*BOOOOOOOOM*\n"
                                                      "You get so startled by the explosion you lose track of whoever was standing there.\n"
                                                      "It turns out there was a cave behind that crack in the wall!"],
                                   "Go cave":["Enter the cave", ["Opened_cave"]]},
                                   
                "cave" : {"Go cave_entrance":["Go back"],
                          "Collect lockpick":["Grab the lockpick", ["Can collect lockpick"],
                                              "You grab the lockpick.\n"
                                              "Maybe you should get out now, this place is giving you the creeps."]},
                                              
                "inside_cabin1" : {"Go outside_cabin":["Go back outside"],
                                   "Go inside_cabin2":["Go further into the house"]},
                                   
                "inside_cabin2" : {"Go inside_cabin1":["Go back to the hall"],
                                   "Say":["Go torwards the window", ["Has lockpick"],
                                   "You take a step torwards the window.\n"
                                   "There seems to be a bit of wind outside.\n"
                                   "There...\n"
                                   "They're there...\n"
                                   "They're just standing there.\n"
                                   "Not moving, simply staring you dead in the eye.\n"
                                   "The illuminating humaniod.\n"
                                   "You get so uncomfortable seeing them you step back from the window, hoping it stops staring."],
                                   
                                   "Set door_unlocked":["Unlock the door with the metal key", ["Can unlock door"],
                                   "You unlock the door.\n"
                                   "It's dark.\n"
                                   "Do you really want to go?"],
                                   "Go stairs":["Enter the door", ["door_unlocked"]]},
                                   
                "stairs" : {"Go hallway":["Go down"]},
                
                "hallway" : {"No":["No"]}}


# Where the actual rooms are defined

roomsDict = {"forest" :            RoomInfo("forest",            roomDescriptions["forest"], ChoicesList["forest"]),
             "deeper_forest" :     RoomInfo("deeper_forest",     roomDescriptions["deeper_forest"], ChoicesList["deeper_forest"]),
             "graveyard" :         RoomInfo("graveyard",         roomDescriptions["graveyard"], ChoicesList["graveyard"]),
             "misty_lake" :        RoomInfo("misty_lake",        roomDescriptions["misty_lake"], ChoicesList["misty_lake"]),
             "misty_lake_island" : RoomInfo("misty_lake_island", roomDescriptions["misty_lake_island"], ChoicesList["misty_lake_island"]),
             "misty_lake2" :       RoomInfo("misty_lake2",       roomDescriptions["misty_lake2"], ChoicesList["misty_lake2"]),
             "outside_cabin" :     RoomInfo("outside_cabin",     roomDescriptions["outside_cabin"], ChoicesList["outside_cabin"]),
             "behind_cabin" :      RoomInfo("behind_cabin",      roomDescriptions["behind_cabin"], ChoicesList["behind_cabin"]),
             "cave_entrance" :     RoomInfo("cave_entrance",     roomDescriptions["cave_entrance"], ChoicesList["cave_entrance"]),
             "cave" :              RoomInfo("cave",              roomDescriptions["cave"], ChoicesList["cave"]),
             "inside_cabin1" :     RoomInfo("inside_cabin1",     roomDescriptions["inside_cabin1"], ChoicesList["inside_cabin1"]),
             "inside_cabin2" :     RoomInfo("inside_cabin2",     roomDescriptions["inside_cabin2"], ChoicesList["inside_cabin2"]),
             "stairs" :            RoomInfo("stairs",            roomDescriptions["stairs"], ChoicesList["stairs"]),
             "hallway" :           RoomInfo("hallway",           roomDescriptions["hallway"], ChoicesList["hallway"])}


# Sets the starting room to forest

currentRoom = roomsDict["forest"]

# Functions handling the commands!

def go(targetRoom):
    try:
        str(targetRoom)
    except:
        print("Hey, you did something wrong there, you silly ;3\nYou baka UwU")
    finally:
        global currentRoom
        currentRoom = roomsDict[targetRoom]

def collect(itemName):
    global progressBooleans
    progressBooleans["Has " + itemName][0] = True
    if len(progressBooleans["Has " + itemName]) > 1:
        progressBooleans[progressBooleans["Has " + itemName][1]][0] = False

def examine(roomName):
    global progressBooleans
    progressBooleans["Examined " + roomName][0] = True

    global doingActions
    doingActions["isExaminating"] = True

    if len(progressBooleans["Examined " + roomName]) > 1:
        progressBooleans[progressBooleans["Examined " + roomName][1]][0] = False

def Dig(objectName):
    global progressBooleans
    progressBooleans["Dug " + objectName][0] = True

    if len(progressBooleans["Dug " + objectName]) > 1:
        progressBooleans[progressBooleans["Dug " + objectName][1]][0] = False

def Say(whatToSay):
    global exceptionDescription
    exceptionDescription = whatToSay

def Set(booleanName):
    progressBooleans[booleanName][0] = True

    if len(progressBooleans[booleanName]) > 1:
        progressBooleans[progressBooleans[booleanName][1]][0] = False


# The "update" loop
running = True
while running:
    print("\n\n\n")

    if exceptionDescription == "":
        if progressBooleans["Entered " + currentRoom.name.lower()][0] == False:
            # The room is new
            if len(currentRoom.descriptions) < 3:
                print(currentRoom.descriptions[0])
            elif doingActions[currentRoom.descriptions[2][1]] == True:
                print(currentRoom.descriptions[2][0])

                doingActions[currentRoom.descriptions[2][1]] = False
            else:
                print(currentRoom.descriptions[0])
        else:
            # The room HAS been entered before
            if len(currentRoom.descriptions) < 3:
                print(currentRoom.descriptions[1])
            elif doingActions[currentRoom.descriptions[2][1]] == True:
                print(currentRoom.descriptions[2][0])

                doingActions[currentRoom.descriptions[2][1]] = False
            else:
                print(currentRoom.descriptions[1])
    else:
        print(exceptionDescription)
        exceptionDescription = ""

    
    
    if progressBooleans["Entered " + currentRoom.name][0] == False:
        progressBooleans["Entered " + currentRoom.name][0] = True


    if currentRoom.name != "hallway":
        # What you can do:
        print("\nYou can do the following:")

        choicePos = 0
        choiceLetters = ["A", "B", "C", "D", "E", "F"]

        for choice, choiceName in currentRoom.choices.items():
            if len(choiceName) < 2:
                print(choiceLetters[choicePos] + ": " + currentRoom.choices[choice][0])
                choicePos += 1
            else: 
                # Checking if ALL the booleans required are true in order to allow doing action
                canDoAction = True
                for i in range(0, len(choiceName[1])):
                    if progressBooleans[choiceName[1][i]][0] == False:
                        canDoAction = False

                if canDoAction:
                    print(choiceLetters[choicePos] + ": " + currentRoom.choices[choice][0])
                    choicePos += 1

        # Where the command is handled
        command = input("\n")


        command = command.strip()
        command = command.upper()

        i = 0
        while i < len(choiceLetters):
            
            availableChoices = list(currentRoom.choices.keys())
            for choice, choiceValue in currentRoom.choices.items():
                if len(choiceValue) > 1:
                    for j in range(0, len(choiceValue[1])):
                        if len(choiceValue) > 1:
                            if progressBooleans[choiceValue[1][j]][0] == False and availableChoices.__contains__(choice):
                                availableChoices.remove(choice)

            if command == choiceLetters[i] and i < len(availableChoices):


                shouldDo = availableChoices[i]

                if len(currentRoom.choices[shouldDo]) >= 3:
                    exceptionDescription = currentRoom.choices[shouldDo][2]

                shouldDo = shouldDo.split()


                if shouldDo[0] == "Go":
                    go(shouldDo[1])
                elif shouldDo[0] == "Collect":
                    collect(shouldDo[1])
                elif shouldDo[0] == "Examine":
                    examine(shouldDo[1])
                elif shouldDo[0] == "Dig":
                    Dig(shouldDo[1])
                elif shouldDo[0] == "Say":
                    Say(currentRoom.choices[availableChoices[i]][2])
                elif shouldDo[0] == "Set":
                    Set(shouldDo[1])

                i = len(choiceLetters)
            i += 1
    else:
        running = False