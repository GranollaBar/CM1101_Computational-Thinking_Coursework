room_bedroom = {
    "id" : "bedroom",
	
    "story":"""Welcome to quest for breakfast!

In your sleep you feel an intense pain in your stomach, feeling as if your hunger might spell the end of you.
You need breakfast, NOW!

To find your way to the kitchen, use the actions:
"inspect" , "use", and "go" 
to navigate the world around you.

There are various breakfast pieces scattered around this world where not everything is as it seems.
Find your breakfast, get to the kitchen, or die trying. 
GOOD LUCK!

The pain waking you, you rouse from your slumber and with a demanding grumble from your stomach, you roll out of bed.
Type "inspect kitchen door" to start your adventure, and remember to type "help" if you forget the commands.""",

    "visited" : False,
    "description" : "Your bedroom",
    "exits" : {
                "kitchen" : {"name" : "kitchen door", "description" : "It is locked", "unlocked" : False, "prompt" : "", "checkpoint" : 0},
                "bathroom" : {"name" : "bathroom door", "description" : "It is locked", "unlocked" : False, "prompt" : "", "checkpoint" : 0}
              },
    "interactions" : {
                        "bed" : {"name" : "bed", "description" : "It's a mess", "prompt" : "", "checkpoint" : 0},
                        "mess" : {"name" : "mess", "description" : "There are clothes everywhere", "prompt" : "", "checkpoint" : 0}
                    }
}

room_bathroom = {
    "id" : "bathroom",

    "story": """
You open the door...
It's your bathroom, just as expected.

You scan the room, everything looks in place.
Now, time to brush your teeth""",

    "visited" : False,
    "description" : "Your bathroom",
     "exits" : {
                "bedroom" : {"name" : "bedroom door", "description" : "It leads to your bedroom", "unlocked" : True, "prompt" : "", "checkpoint" : 0}
              },
    "interactions" : {
                        "mirror" : {"name" : "mirror", "description" : "you see yourself in the reflection", "prompt" : "", "checkpoint" : 0},
                        "sink" : {"name" : "sink", "description" : "Your regular old sink", "prompt" : "", "checkpoint" : 0},
                    }
}

room_mirror = {
    "id" : "mirror",

    "story":"""
The mirror swallows you whole, sending you through a vortex of the unknown 
before you realize it, you're thrown to the cold, black concrete.

As you rise, you turn to reveal a gray face staring back at you from the mirror,
its just like the evil queen's mirror from snow white.
You try to say the iconic phrase 'mirror mirror on the wall, who is the fairest of them all'
the mirror responds 'the grumpy dwarf obviously'
'huh...'
you look around the room.""",

	"visited" : False,
    "description" : "The open room is dominated by the ominous staring of the face in the mirror",
    "exits" : { 
    		},
    "interactions" : { 
						"mirror" : {"name" : "magic mirror", "description" : "It leads back to your bathroom", "prompt" : "", "checkpoint" : 0},
						"maze" : {"name" : "maze entrance", "description" : "It is the entrance to a hedge maze", "prompt" : "", "checkpoint" : 0}
					}
}

room_courtroom = {
    "id" : "courtroom",

    "story": "",

    "visited" : False,
    "description" : "A courtroom full of monsters instead of humans? Also who let Miles Edgeworth in?",
    "exits" : {
    		    },
	  "interactions" : {
				        }
}

room_alcatraz_cell  = {
    "id" : "cell",

    "story": """
You wake up to cold water dripping on your face.

You slowly begin to remember what happened, the monster, the court room, and realise you're in prison!

You look around to see a dirty cell with metal bars stopping your exit,
light shines through some cracks in the wall and a narrow window.

Through the jail-bars you see many penguins waddling around
'the penguins from club penguin?'
Each of them are fully geared out in grade-A military outifts and equipped with many weapons
these guys look serious, you should probably find a way out of here.""",

	  "visited" : False,
    "description" : "A cold and empty prison cell.",
    "exits" : {
    },
    "interactions" : {
                        "bed" : {"name" : "bed", "description" : "A tiny bunk barely large enough for you to fit on.", "prompt" : "", "checkpoint" : 0},
						"door" : {"name" : "cell door", "description" : "It's locked tight and those bars are made from solid steel.", "prompt" : "", "checkpoint" : 0},
                        "drain" : {"name" : "drain cover", "description" : "A fairly small drainage cover", "prompt" : "", "checkpoint" : 0},
                        "food" : {"name" : "prison food", "description" : "A plate of grey sludge", "prompt" : "", "checkpoint" : 0}
                    }
}

room_alcatraz_drain  = {
    "id" : "drain",

    "story": "",

	"visited" : False,
    "description" : "",
    "exits" : {},
    "interactions" : {}
}

room_sea = {
    "id" : "sea",

    "story": """
After the nuclear detonation at alcatraz, the smoke finally disappears, 
only to reveal the fence is still standing.

The sign beside you is also unaffected and reads:
'The outdoor fence is made of ant-nuclear fencing so good luck getting through that' signed Sensei Wu
you are frightened by this realisation.

However you notice various items scattered across the ground,
'maybe I can use these' you think""",

		"visited" : False,
        "description" : "The ominous sea waves crashed against the island with brutality.",
		"exits" : {},
        "interactions": {
                          	"fence" : {"name" : "fence", "description" : "A massive, unclimbable barrier.", "prompt" : "", "checkpoint" : 0},
                          	"workbench" : {"name" : "workbench", "description" : "The metalshop fabricator has landed outside in perfect condition.", "prompt" : "", "checkpoint" : 0},
							"1" : {"name" : "rubble 1", "description" : "A pile of rubble.\nThere is nothing of value", "prompt" : "", "checkpoint" : 0},
							"2" : {"name" : "rubble 2", "description" : "A pile of rubble.", "prompt" : "", "checkpoint" : 0}, 
							"3" : {"name" : "rubble 3", "description" : "A pile of rubble.\nThere is nothing of value", "prompt" : "", "checkpoint" : 0}, 
							"4" : {"name" : "rubble 4", "description" : "A pile of rubble.", "prompt" : "", "checkpoint" : 0}, 
							"5" : {"name" : "rubble 5", "description" : "A pile of rubble.\nThere is nothing of value", "prompt" : "", "checkpoint" : 0},
							"6" : {"name" : "rubble 6", "description" : "A pile of rubble.", "prompt" : "", "checkpoint" : 0}
                        }
}

room_pirateship = {
    "id" : "pirate ship",

    "story": "",

	"visited" : False,
    "description" : "",
    "exits" : { },
    "interactions" : { }
}

room_kitchen = {
    "id" : "kitchen",
    
    "story" : """
You have finally made it back home and can start to make your breakfast with the items you have 
collected along your journey.""",

	"visited" : False,
    "description" : "You have made it back home and to your kitchen, now it is time to make breakfast!",
	"exits" : {},
    "interactions" : {
						"cooker" : {"name" : "cooker", "description" : "For all of your cooking needs.", "prompt" : "", "checkpoint" : 0}
					}
}

rooms_list = {
    "bedroom" : room_bedroom,
    "bathroom" : room_bathroom,
    "mirror" : room_mirror,
    "courtroom" : room_mirror,
    "cell" : room_alcatraz_cell,
    "sea" : room_sea,
    "pirate ship" : room_pirateship,
    "kitchen" : room_kitchen
}
