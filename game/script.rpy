# Python crap (annoying shit).

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        
        return True
        
    def nv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/narr_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def lv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/lit_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
    
    def prov(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/protag_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def vv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/vio_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def av(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/amb_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def sv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sie_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def cyv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/cry_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)
            
    def chrv(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/chr_voice.flac", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

# Define narrator type "characters".

define l = Character("Literature", callback=lv, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define n = Character("Narrator", callback=nv, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])

# Define protagonist fake names.

define pv = Character("[violet_name]", callback=prov, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pa = Character("[amber_name]", callback=prov, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define ps = Character("[sierra_name]", callback=prov, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pcy = Character("[crystal_name]", callback=prov, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pc = Character("[christine_name]", callback=prov, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])

# Define characters.

define v = Character("Violet", callback=vv,  color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define a = Character("Amber", callback=av, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define s = Character("Sierra", callback=sv, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define cr = Character("Crystal", callback=cyv, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define ch = Character("Christine", callback=chrv, color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define ap = Character("April", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])

# Splash screen.

label splashscreen:

    scene black
    with dissolve
    
    pause 1.0
    
    play music "audio/splash.flac" 
    
    scene splash1
    with dissolve
    
    pause 2.5
    
    stop music fadeout 1.0
    
    scene black
    with dissolve
    
    scene splash2
    with dissolve
    
    pause 2.0
    
    scene black
    with dissolve
    
return

# Start of a new game.

label start:
    
    $ achievement.grant("welcome")
    
    # Variable settings.
    
    $ flash = Fade(.25, 0.0, .75, color="#fff")
    default gender = 0
    default real_name = "REDACTED"
    default other_info = "Manipulative sexual predator"
    default virgin = 0
    default dating = 1
    default violet = 1
    default amber = 1
    default sierra = 1
    default crystal = 1
    default christine = 1
    default april = 1
    default time = 3
    default bladder = 2
    default balls = 1
    default ovaries = 1
    default pissjar = 1
    default nightstalk = 1
    default v_toilet_fuck = 0
    default a_toilet_fuck = 0
    default s_toilet_fuck = 0
    $ age = 18
    $ violet_name = ""
    $ violet_from = ""
    $ amber_name = ""
    $ amber_from = ""
    $ sierra_name = ""
    $ sierra_from = ""
    $ load_from = ""
    default window_crack_v = 0
    default window_crack_a = 0
    default window_cracked = 0
    default vase = 0
    default v_items = 0
    default v_item_glass = 0
    default v_item_bark = 0
    default v_item_tube = 0
    default v_item_cable = 0
    default v_item_pick = 0
    default a_items = 0
    default a_item_glass = 0
    default a_item_sap = 0
    default a_item_condom = 0
    default a_item_egg = 0
    default a_item_bark = 0
    default a_item_boxedcondoms = 0
    default v_wet = 0
    default a_wet = 0
    default a_cum = 0
    default s_naked = 0
    default ch_naked = 0
    default s_fingered = 0
    default s_clothes = 0
    default s_wherefucked = 0
    default s_items = 0
    default s_item_leaflet = 0
    default s_item_stand = 0
    default cr_items = 0
    default chr_items = 0
    default ap_items = 0
    default tooltip = Tooltip("")
    default lamp = 0
    default loading = 0

    # Show attention warning regarding age of characters.
    
    stop music fadeout 3.0
    
    scene attention
    with dissolve
    
    pause 120.0
    
    play music "audio/game_setup.flac" loop fadein 3.0
    
    scene map_blur
    with dissolve
    
    # Ask question to user if they are a boy or girl and what age they are.
    
    n "Before we start, you must setup the game."
    
    n "Are you a boy or a girl? How old are you? What's your real name? What other information can you say about yourself? Have you lost your virginity yet?"
    
    n "What you choose will affect how the story is presented and how it finishes."
    menu:
        "Boy":
            $ achievement.grant("boy")
            $ gender = 0
            python:
                try:
                    age = int(renpy.input("Enter your age."))
                except Exception:
                    age = 18
            if age <= 18:
                $ achievement.grant("underage")
                $ age = 18
            
            $ real_name = renpy.input("Enter your real name.", length=24)
            $ real_name = real_name.strip()
            if real_name == "":
                $ real_name = "REDACTED"
            
            $ other_info = renpy.input("Enter information about yourself.", length=4226)
            $ other_info = other_info.strip()
            if other_info == "":
                $ other_info = "Manipulative sexual predator."
                
            n "Are you a virgin?"
            
            menu:
                "Yes":
                    n "You haven't lost your virginity yet."
                    $ virgin = 1
                "No":
                    n "You have lost your virginity."
                    $ virgin = 0
            
            jump starting_path
        "Girl":
            $ achievement.grant("girl")
            $ gender = 1
            python:
                try:
                    age = int(renpy.input("Enter your age."))
                except Exception:
                    age = 18
            if age <= 18:
                $ achievement.grant("underage")
                $ age = 18
            
            $ real_name = renpy.input("Enter your real name.", length=24)
            $ real_name = real_name.strip()
            if real_name == "":
                $ real_name = "REDACTED"
            
            $ other_info = renpy.input("Enter information about yourself.", length=42)
            $ other_info = other_info.strip()
            if other_info == "":
                $ other_info = "Manipulative sexual predator"
                
            n "Are you a virgin?"
            
            menu:
                "Yes":
                    n "You haven't lost your virginity yet."
                    $ virgin = 1
                "No":
                    n "You have lost your virginity."
                    $ virgin = 0
            
            jump starting_path
return

label starting_path:
    
    stop music fadeout 3.0

    $ renpy.block_rollback()
    
    show screen bodystats
    
    scene car
    with dissolve
    
    play music "audio/car_music.flac" loop fadein 3.0
    
    play voice "audio/rain.flac" loop fadein 3.0
    
    pause 3.0
    
    if gender == 0:
        
        n "The rain splashes heavily in the puddles outside as if the heavens are crying, as you make your way to your destination..."
    
        n "The car radio drones on a discordant rock tune as you try to make any semblance of reality..."
    
        n "You're moving to a new, smaller town as you were banished from the town you grew up in..."
    
        n "You want to forget what happened in the past, but the thoughts of the crimes you committed keep bothering you, knocking on your door, waiting for an answer..."

        n "'The best way to get pussy and not get caught...', you think and mumble to yourself as you near your new living arrangements..."
        
        n "You ponder on this question... It intrigues you... What if you could get all the girls in this small town to like you...?"
        
        n "You wonder if they would notice you stealing their possessions, or lying to them..."
        
        n "The thoughts of tricking girls to like you gets your cock erect and wet..."
        
    elif gender == 1:
        
        n "The rain splashes heavily in the puddles outside as if the heavens are crying, as you make your way to your destination..."
    
        n "The car radio drones on a discordant rock tune as you try to make any semblance of reality..."
    
        n "You're moving to a new, smaller town as you were banished from the town you grew up in..."
    
        n "You want to forget what happened in the past, but the thoughts of the crimes you committed keep bothering you, knocking on your door, waiting for an answer..."

        n "'The best way to get pussy and not get caught...', you think and mumble to yourself as you near your new living arrangements..."
        
        n "You ponder on this question... It intrigues you... What if you could get all the girls in this small town to like you...?"
        
        n "You wonder if they would notice you stealing their possessions, or lying to them..."
        
        n "The thoughts of tricking girls to like you gets your pussy wet and throbbing..."
    
    scene house
    with dissolve
    
    n "The car screeches to a halt. You have arrived at your new home..."
    
    play audio "audio/thunder.flac"
    
    n "You grab your bags and head inside. You look around and find a study with a desk and a pin board..."
    
    n "You notice that there's already some pins on the board, so you take a closer look..."
    
    n "It appears to be a list of girls in this small town, or at least what species they are..."
    
    n "From this, you decide to use this as your ''base of operations.''"
    
    stop voice fadeout 3.0
    
    stop music fadeout 3.0
    
    jump main_hub_screen
return

# Body physics

label body_stats:

    screen bodystats:
    
        if bladder == 1:
            image "Bladder1.png":
                xpos 0.94
                ypos 0.8
        elif bladder == 2:
            image "Bladder2.png":
                xpos 0.94
                ypos 0.8
        else:
            image "Bladder3.png":
                xpos 0.94
                ypos 0.8
                
            image "BMeterWarn.png":
                xpos 0.78
                ypos 0.005 
        
        if gender == 0:    
            if balls == 1:
                image "Balls1.png":
                    xpos 0.94
                    ypos 0.9
            elif balls == 2:
                image "Balls2.png":
                    xpos 0.94
                    ypos 0.9
            else:
                image "Balls3.png":
                    xpos 0.94
                    ypos 0.9
        else:
            if ovaries == 1:
                image "Ovar1.png":
                    xpos 0.94
                    ypos 0.9
            elif ovaries == 2:
                image "Ovar2.png":
                    xpos 0.94
                    ypos 0.9
            else:
                image "Ovar3.png":
                    xpos 0.94
                    ypos 0.9
    
    return
return

label pissjarno:

    if lamp == 1:
        show screen dates
    else:
        show screen dates_dark

    if pissjar == 1:
        if bladder == 2:
            
            $ pissjar += 1
            $ bladder = 1
            
            jump from_piss_jar
        elif bladder == 3:
            
            $ pissjar += 2
            $ bladder = 1
            
            jump from_piss_jar
        else:
            n "You try emptying your bladder, but nothing comes out."
            
            jump from_piss_jar
    elif pissjar == 2:
        if bladder == 2:
        
            $ pissjar += 1
            $ bladder = 1
            
            jump from_piss_jar
        elif bladder == 3:
                n "Emptying a full bladder into a half filled jar will overflow."
                menu:
                    "Empty bladder":
                        n "You empty your bladder into the half filled jar and it overflows, gushing to the floor."
                    
                        $ pissjar += 1
                        $ bladder = 1
                        
                        jump from_piss_jar
                    "Empty jar out the window and use it":
                        n "You carefully take the jar to the window and dump it out."  

                        $ pissjar = 1
                        $ pissjar += 2
                        $ bladder = 1
                        
                        jump from_piss_jar
        else:
            n "You try emptying your bladder, but nothing comes out."
            
            jump from_piss_jar
    else:
        if bladder == 2:
        
            n "Emptying your bladder into a filled jar will overflow."
            menu:
                "Empty bladder":
                    n "You empty your bladder into the filled jar and it overflows, gushing to the floor."
                    
                    $ pissjar += 1
                    $ bladder = 1
                        
                    jump from_piss_jar
                "Empty jar out the window and use it":
                    n "You carefully take the jar to the window and dump it out."  

                    $ pissjar = 1
                    $ pissjar += 1
                    $ bladder = 1
                        
                    jump from_piss_jar
        elif bladder == 3:
                n "Emptying your bladder into a filled jar will overflow."
                menu:
                    "Empty bladder":
                        n "You empty your bladder into the filled jar and it overflows, gushing to the floor."
                        
                        $ bladder = 1
                        
                        jump from_piss_jar
                    "Empty jar out the window and use it":
                        n "You carefully take the jar to the window and dump it out."  

                        $ pissjar = 1
                        $ pissjar += 2
                        $ bladder = 1
                        
                        jump from_piss_jar
        else:
            n "You try emptying your bladder, but nothing comes out."
            
            jump from_piss_jar
return

# Gallery

label gallery:

    hide screen bodystats
    scene gallery
    with pixellate
    
    $ achievement.grant("gallery")

    label gallery_page_1:
    
        $ tooltip = Tooltip("")
    
        call screen gallery_items_1 with dissolve
    
        screen gallery_items_1:
    
            image "gallery/violet_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.08
            
            image "gallery/amber_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.52
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "right_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.984
                ypos 0.5
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to next page.") ]
                action Jump("gallery_page_2")
 
            if violet >= 2:
                imagebutton auto "gallery/gallery_violet_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Violet gave you on your first date.") ]
                    action Jump("violet_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if violet >= 3:
                imagebutton auto "gallery/gallery_violet_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Violet gave you on your second date.") ]
                    action Jump("violet_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if violet >= 4:
                imagebutton auto "gallery/gallery_violet_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Violet gave you in a letter before your third date.") ]
                    action Jump("violet_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if violet >= 4:
            
                imagebutton auto "gallery/v_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Violet on the third date.") ]
                    action Jump("gallery")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.2
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
                    
            if v_item_glass == 1:
                
                imagebutton auto "gallery/a_glass_shardg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.22
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A glass shard you collected from breaking Violet's window during her first date.") ]
                    action Jump("violet_item_1_interact")
            else:
                
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                    
            if v_item_bark == 1:
                imagebutton auto "gallery/a_barkg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.22
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A piece of bark you collected from Violet's first date.") ]
                    action Jump("violet_item_2_interact")
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                    
            if v_item_pick == 1:
                imagebutton auto "gallery/v_pickg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.65
                    ypos 0.22
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A guitar pick you collected during Violet's first date.") ]
                    action Jump("violet_item_3_interact")
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.67
                    
            if v_item_tube == 1:
                imagebutton auto "gallery/v_tubeg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.35
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A amp tube you collected during Violet's first date.") ]
                    action Jump("violet_item_4_interact")
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                    
            if v_item_cable == 1:
                imagebutton auto "gallery/v_cableg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.35
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("An audio cable you collected during Violet's first date.") ]
                    action Jump("violet_item_5_interact")
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
        
            if amber >= 2:
                imagebutton auto "gallery/gallery_amber_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you on your first date.") ]
                    action Jump("amber_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if amber >= 3:
                imagebutton auto "gallery/gallery_amber_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you on your second date.") ]
                    action Jump("amber_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if amber >= 4:
                imagebutton auto "gallery/gallery_amber_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you in a letter before your third date.") ]
                    action Jump("amber_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if amber >= 4:
            
                imagebutton auto "gallery/a_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Amber on the third date.") ]
                    action Jump("gallery")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
        
            if a_item_glass == 1:
            
                imagebutton auto "gallery/a_glass_shardg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A glass shard you collected from breaking the shop windows during Amber's first date.") ]
                    action Jump("amber_item_1_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                
            if a_item_sap == 1:
            
                imagebutton auto "gallery/a_sapg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.8
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A lump of tree sap you collected during Amber's second date.") ]
                    action Jump("amber_item_2_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                
            if a_item_condom == 1:
            
                imagebutton auto "gallery/a_condomg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.67
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A used condom you collected during Amber's second date.") ]
                    action Jump("amber_item_3_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                
            if a_item_egg == 1:
                imagebutton auto "gallery/a_eggg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.8
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A bird egg you collected during Amber's second date.") ]
                    action Jump("amber_item_4_interact")
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.57
                    ypos 0.67
                
            if a_item_bark == 1:
                imagebutton auto "gallery/a_barkg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.65
                    ypos 0.67
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A piece of tree bark you collected during Amber's second date.") ]
                    action Jump("amber_item_5_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
        
            text "Items Collected: [v_items]/5" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.13
            
            text "Items Collected: [a_items]/5" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.58
        
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        return
    return
    
    label gallery_page_2:
        $ tooltip = Tooltip("")
    
        call screen gallery_items_2 with dissolve
    
        screen gallery_items_2:
    
            image "gallery/sierra_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.08
                
            image "gallery/crystal_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.135
                ypos 0.52
            
            image "debug.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.52
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "right_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.984
                ypos 0.5
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to next page.") ]
                action Jump("gallery_page_3")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.017
                ypos 0.5
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("gallery_page_1")
 
            if sierra >= 2:
                imagebutton auto "gallery/gallery_sierra_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Sierra gave you on your first date.") ]
                    action Jump("sierra_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if sierra >= 3:
                imagebutton auto "gallery/gallery_sierra_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Sierra gave you on your second date.") ]
                    action Jump("sierra_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if sierra >= 4:
                imagebutton auto "gallery/gallery_sierra_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Sierra gave you in a letter before your third date.") ]
                    action Jump("sierra_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if sierra >= 4:
            
                imagebutton auto "gallery/s_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Sierra on the third date.") ]
                    action Jump("gallery_page_2")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.2
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
                    
            if s_item_leaflet == 1:
            
                imagebutton auto "gallery/s_leafletg_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.22
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("A leaflet you collected from outside the museum on Sierra's first date.") ]
                    action Jump("sierra_item_1_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.35
                
            if s_item_stand == 1:
            
                imagebutton auto "s_boardg_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.35
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The museum notice board which you stole during Sierra's first date.") ]
                    action Jump("sierra_item_2_interact")
                
            else:
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
                    
            if crystal >= 2:
                imagebutton auto "gallery/gallery_crystal_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Crystal gave you on your first date.") ]
                    action Jump("crystal_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if crystal >= 3:
                imagebutton auto "gallery/gallery_amber_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you on your second date.") ]
                    action Jump("amber_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if crystal >= 4:
                imagebutton auto "gallery/gallery_amber_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you in a letter before your third date.") ]
                    action Jump("amber_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if crystal >= 4:
            
                imagebutton auto "gallery/a_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Amber on the third date.") ]
                    action Jump("gallery")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
        
            text "Items Collected: [s_items]/2" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.13
            
            text "Items Collected: [cr_items]/0" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.58
        
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        
        return
    return
    
    label gallery_page_3:
        $ tooltip = Tooltip("")
    
        call screen gallery_items_3 with dissolve
    
        screen gallery_items_3:
    
            image "gallery/christine_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.08
                
            image "gallery/april_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.52
            
            image "debug.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.52
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.017
                ypos 0.5
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("gallery_page_2")
 
            if christine >= 2:
                imagebutton auto "gallery/gallery_christine_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Christine gave you on your first date.") ]
                    action Jump("christine_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if christine >= 3:
                imagebutton auto "gallery/gallery_sierra_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Sierra gave you on your second date.") ]
                    action Jump("sierra_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if christine >= 4:
                imagebutton auto "gallery/gallery_sierra_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Sierra gave you in a letter before your third date.") ]
                    action Jump("sierra_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if christine >= 4:
            
                imagebutton auto "gallery/chr_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.3
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Sierra on the third date.") ]
                    action Jump("gallery_page_2")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.2
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
                    
            if april >= 2:
                imagebutton auto "gallery/gallery_amber_1_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you on your first date.") ]
                    action Jump("amber_p1")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.1
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if april >= 3:
                imagebutton auto "gallery/gallery_amber_2_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you on your second date.") ]
                    action Jump("amber_p2")
            else:
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.25
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if crystal >= 4:
                imagebutton auto "gallery/gallery_amber_3_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The picture Amber gave you in a letter before your third date.") ]
                    action Jump("amber_p3")
                
            else:
            
                imagebutton auto "gallery/gallery_unknown_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.4
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this picture by completing the corresponding date.") ]
                
            if april >= 4:
            
                imagebutton auto "gallery/a_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.8
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("The panties you stole from Amber on the third date.") ]
                    action Jump("gallery")
            else:
            
                imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
                    ypos 0.75
                    hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Unlock this item by completing the corresponding date.") ]
        
            text "Items Collected: [chr_items]/2" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.13
            
            text "Items Collected: [ap_items]/0" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.58
        
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        
        return
    return
    
    # Violet pictures.
    
    label violet_p1:
        
        scene blank
    
        call screen violet_p1 with pixellate
    
        screen violet_p1:
        
            imagebutton idle "violet_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    label violet_p2:
        scene blank
    
        call screen violet_p2 with pixellate
    
        screen violet_p2:
        
            imagebutton idle "violet_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    label violet_p3:
        scene blank
    
        call screen violet_p3 with pixellate
    
        screen violet_p3:
        
            imagebutton idle "violet_date_3_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    # Amber pictures.
    
    label amber_p1:
        scene blank
    
        call screen amber_p1 with pixellate
    
        screen amber_p1:
        
            imagebutton idle "amber_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    return
    
    label amber_p2:
        
        scene blank
    
        call screen amber_p2 with pixellate
    
        screen amber_p2:
        
            imagebutton idle "amber_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
        
        return
    return
    
    label amber_p3:
        
        scene blank
    
        call screen amber_p3 with pixellate
    
        screen amber_p3:
        
            imagebutton idle "amber_date_3_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
            
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
        
        return
    return
    
    # Sierra pictures.
    
    label sierra_p1:
        
        scene blank
    
        call screen sierra_p1 with pixellate
    
        screen sierra_p1:
        
            imagebutton idle "sierra_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    label sierra_p2:
        
        scene blank
    
        call screen sierra_p2 with pixellate
    
        screen sierra_p2:
        
            imagebutton idle "sierra_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
                
        return
    return
    
    label sierra_p3:
        scene blank
    
        call screen sierra_p3 with pixellate
    
        screen sierra_p3:
        
            imagebutton idle "sierra_date_3_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")      
        return
    return
    
    # Crystal pictures.
    
    label christine_p1:
        
        scene blank
    
        call screen christine_p1 with pixellate
    
        screen christine_p1:
        
            imagebutton idle "christine_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    # Christine pictures.
    
    label crystal_p1:
        
        scene blank
    
        call screen crystal_p1 with pixellate
    
        screen crystal_p1:
        
            imagebutton idle "crystal_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("gallery")
                
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("gallery")
    
        return
    return
    
    # Violet item interaction.
    
    label violet_item_1_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the glass shard."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub yourself with it.":
            
                    n "You rub yourself with the glass shard, it's extremely painful and causes some bleeding."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it":
        
                    n "You insert the glass shard into your vagina, it's extremely painful and causes a lot of bleeding."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away":
        
                    n "You throw the glass shard in the bin."
            
                    $ a_item_glass = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your dick on it":
                
                    n "You rub your dick on the glass shard, it causes cuts on your shaft with a bit of blood."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it in up your arse":
                
                    n "You insert the glass shard up your arse, you feel extreme pain and start shitting blood."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the glass shard in the bin."
                
                    $ a_item_glass = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    label violet_item_2_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the tree bark."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub yourself with it.":
            
                    n "You rub yourself with the bark, it's extremely painful and causes some external and internal bleeding."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it.":
        
                    n "You insert the bark into your vagina, you feel extreme pain from splinters."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away.":
        
                    n "You throw the piece of bark in the bin."
            
                    $ v_item_bark = 0
                    $ v_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Try inserting it in your pee hole.":
                
                    n "You try to insert it in your pee hole and cause external and internal bleeding."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it in up your arse.":
                
                    n "You insert the bark up your arse, you feel extreme pain from splinters."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the piece of bark in the bin."
                
                    $ v_item_bark = 0
                    $ v_items -= 1
                
                    jump gallery
    return
    
    label violet_item_3_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the guitar pick."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Strum your clit with it.":
            
                    n "You strum your clit like a guitar and squirt all over your bed."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it.":
        
                    n "You insert the guitar pick into your vagina. It feels nice but then you realise you can't get it out, even with pushing. You've lost the guitar pick inside yourself."
                    
                    $ v_item_pick = 0
                    $ v_items -= 1
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away.":
        
                    n "You throw the guitar pick in the bin."
            
                    $ v_item_pick = 0
                    $ v_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Strum your prostate with it.":
                
                    n "You position the guitar pick behind your balls and start strumming your prostate. You end up cumming all over your bed."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it up your arse.":
                
                    n "You insert the guitar pick up your arse. It feels good but then you realise you can't get it out, even with pushing. You've lost the guitar pick inside yourself."
                    
                    $ v_item_pick = 0
                    $ v_items -= 1
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the guitar pick in the bin."
                
                    $ v_item_pick = 0
                    $ v_items -= 1
                
                    jump gallery
    return
    
    label violet_item_4_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the amp tube."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub it on your pee hole.":
            
                    n "You rub the amp tube on your pee hole and get a little shock from it. It causes you to pee on your bed."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it.":
        
                    n "You insert the amp tube into your vagina. It gives you a little shock and causes you to squirt on your bed."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away.":
        
                    n "You throw the amp tube in the bin."
            
                    $ v_item_tube = 0
                    $ v_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub it on your tip.":
                
                    n "You rub the amp tube on your tip, it gives you a little shock and causes you to cum on your bed."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it up your arse.":
                
                    n "You insert the amp tube up your arse. It shatters in your arse and you start shitting blood."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the amp tube in the bin."
                
                    $ v_item_tube = 0
                    $ v_items -= 1
                
                    jump gallery
    return
    
    label violet_item_5_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the audio cable."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Force it up your pee hole.":
            
                    n "You force the audio cable up your pee hole until you feel it in your bladder, along with immense pain. You slowly pull it out, but after it's out you start pissing blood onto your bed."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it.":
        
                    n "You insert the audio cable into your vagina. It gives you a tingly sensation and you end up squirting on the bed."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away.":
        
                    n "You throw the audio cable in the bin."
            
                    $ v_item_cable = 0
                    $ v_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Force it up your dick.":
                
                    n "You force the audio cable up your dick until it it reaches your bladder. You feel immense pain and as soon as you pull it out, you start pissing blood onto your bed."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Vore it.":
                
                    n "You insert the audio cable into your mouth and swallow it whole. After a few hours you feel immense pain in your stomach and you die a slow, painful death from metal poisoning."
                    
                    $ balls == 1
                
                    jump game_over
                
                "Throw it away.":
            
                    n "You throw the audio cable in the bin."
                
                    $ v_item_cable = 0
                    $ v_items -= 1
                
                    jump gallery
    return
    
    # Amber item interaction.
    
    label amber_item_1_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the glass shard."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub yourself with it.":
            
                    n "You rub yourself with the glass shard, it's extremely painful and causes some bleeding."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Insert it":
        
                    n "You insert the glass shard into your vagina, it's extremely painful and causes a lot of bleeding."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away":
        
                    n "You throw the glass shard in the bin."
            
                    $ a_item_glass = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your dick on it":
                
                    n "You rub your dick on the glass shard, it causes cuts on your shaft with a bit of blood."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it in up your arse":
                
                    n "You insert the glass shard up your arse, you feel extreme pain and start shitting blood."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the glass shard in the bin."
                
                    $ a_item_glass = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    label amber_item_2_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the sap."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Finger yourself with it":
            
                    n "You pour the sap over your fingers and start fucking yourself, it feels extremely sticky."
                    
                    $ ovaries == 1
                
                    jump gallery
        
                "Eat the sap":
        
                    n "You put the sap in your mouth and chew on it, it tastes disgusting."
                    
                    $ ovaries == 1
                
                    jump gallery
            
                "Throw it away":
        
                    n "You throw the sap in the bin."
            
                    $ a_item_sap = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your dick with it":
                
                    n "You put your hand on your dick with your hand covered in sap and start rubbing, it's extremely sticky."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Sound the sap":
                
                    n "You insert the sap into your dick hole, it hurts a bit, but it makes you cum everywhere."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the sap in the bin."
                
                    $ a_item_sap = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    label amber_item_3_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the used condom."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Empty the contents into your vagina":
            
                    n "You pour the used condom's contents into your vagina, it feels cold, wet and sticky. You might have an STD or be pregnant now."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Empty the contents into your arse":
        
                    n "You pour the used condom's contents into your arse, it feels cold, wet and sticky. You might have an STD now."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Throw it away":
        
                    n "You throw the used condom in the bin"
            
                    $ a_item_condom = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Put it on":
                
                    n "You put the used condom on and feel a cold sensation slowly trickle into your foreskin. You might have an STD now."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Put the condom in your arsehole inside-out":
                
                    n "You insert the condom into your arsehole inside-out and feel the cold contents fill you up. You might have an STD now."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the used condom in the bin"
                
                    $ a_item_condom = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    label amber_item_4_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the bird egg."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Shove the egg in your vagina":
            
                    n "You shove the bird egg into your vagina. You accidentally clench and it cracks inside you."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Crack the egg inside your pussy":
        
                    n "You crack the egg into your pussy and feel the cold, slimy liquid fill you up. "
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Throw it away":
        
                    n "You throw the egg in the bin"
            
                    $ a_item_egg = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Shove the egg in your arse":
                
                    n "You shove the egg in your arse and it cracks inside you."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Crack the egg into your arse":
                
                    n "You crack the egg into your arse and feel the cold, slimy liquid fill you up."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the egg in the bin"
                
                    $ a_item_egg = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    label amber_item_5_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the tree bark."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub yourself with it":
            
                    n "You rub yourself with the tree bark and feel extreme pain from splinters."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Insert it":
        
                    n "You insert the tree bark into your vagina and feel extreme pain from splinters."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Throw it away":
        
                    n "You throw the tree bark in the bin"
            
                    $ a_item_bark = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your tip with it":
                
                    n "You rub your tip with the tree bark and get a rash inside your pee hole."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it up your arse":
                
                    n "You insert the tree bark and feel extreme pain from splinters."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the tree bark in the bin"
                
                    $ a_item_bark = 0
                    $ a_items -= 1
                
                    jump gallery
    return
    
    # Sierra item interaction.
    
    label sierra_item_1_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the leaflet."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Pee on it.":
            
                    n "You place the leaflet flat on your bed and pee on it, it's all soggy now."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Insert it.":
        
                    n "You insert the leaflet into your vagina and feel it getting soggy inside you."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Throw it away":
        
                    n "You throw the leaflet in the bin"
            
                    $ s_item_leaflet = 0
                    $ s_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Pee on it.":
                
                    n "You place the leaflet flat on your bed and pee on it, it's all soggy now."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it up your arse":
                
                    n "You insert the leaflet up your arse, when you pull it out it's covered in shit."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the leaflet in the bin"
                
                    $ s_item_leaflet = 0
                    $ s_items -= 1
                
                    jump gallery
    return
    
    label sierra_item_2_interact:
        
        scene blank
        with dissolve
    
        n "You head to your bedroom with the museum notice board."
    
        n "What would you like to do with it?"
    
        if gender == 1:
            menu:
                "Rub yourself on it.":
            
                    n "You rub yourself on the pole of the notice board and end up squirting."
                    
                    $ ovaries == 1
                
                    jump gallery
                
                "Insert it.":
        
                    n "You unscrew the notice board's foot and start inserting the pole inside yourself. You keep going pushing it in until the pain becomes unbearable, then you hear something rip. You die a slow, painful death from rupturing your intestines."
                    
                    $ ovaries == 1
                
                    jump game_over
                
                "Throw it away.":
        
                    n "You throw the notice board out the window."
            
                    $ s_item_stand = 0
                    $ s_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your dick on it.":
                
                    n "You rub your dick on it and get an STD."
                    
                    $ balls == 1
                
                    jump gallery
                
                "Insert it up your dick.":
                
                    n "You unscrew the notice board's foot and start inserting the pole into your penis. You only get so far until you split your penis in half and bleed out."
                    
                    $ balls == 1
                
                    jump game_over
                
                "Throw it away.":
            
                    n "You throw the notice board out the window."
                
                    $ s_item_stand = 0
                    $ s_items -= 1
                
                    jump gallery
    return
return 

# Stats

label stats:

    hide screen bodystats
    scene hub_blurred
    with pixellate

    label stats_page_1:
        $ tooltip = Tooltip("")
    
        call screen stats_items_1 with dissolve
    
        screen stats_items_1:
    
            image "stats/stats.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
            
            text "{font=windowslogic-regular.ttf}{size=50}Your Information":
                xpos 0.32
                ypos 0.125
                
            text "{font=windowslogic-regular.ttf}{size=40}You are a Squirrel.":
                xpos 0.32
                ypos 0.182
                
            text "{font=windowslogic-regular.ttf}{size=40}Your real name is [real_name].":
                xpos 0.32
                ypos 0.232
                
            text "{font=windowslogic-regular.ttf}{size=40}Your age is [age].":
                xpos 0.32
                ypos 0.282
                
            text "{font=windowslogic-regular.ttf}{size=40}[other_info].":
                xpos 0.32
                ypos 0.332
                
            if virgin == 1:
                text "{font=windowslogic-regular.ttf}{size=40}You are a virgin.":
                    xpos 0.32
                    ypos 0.382
            elif virgin == 0:
                text "{font=windowslogic-regular.ttf}{size=40}You are not a virgin.":
                    xpos 0.32
                    ypos 0.382
            
            text "{font=windowslogic-regular.ttf}{size=50}Date Progress":
                xpos 0.32
                ypos 0.529
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "right_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.711
                ypos 0.786
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to next page.") ]
                action Jump("stats_page_2")
 
            if violet == 2:
                image "stats/violet_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif violet == 3:
                image "stats/violet_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif violet == 4:
                image "stats/violet_stats_3.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif violet == 5:
                image "stats/violet_stats_4.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            else:
                image "stats/violet_stats_0.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
                
            if amber == 2:
                image "stats/amber_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif amber == 3:
                image "stats/amber_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif amber == 4:
                image "stats/amber_stats_3.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif amber == 5:
                image "stats/amber_stats_4.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            else:
                $ amber_name = ""
                image "stats/amber_stats_0.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            
            text "{font=windowslogic-regular.ttf}{size=40}[violet_name]":
                xpos 0.5
                ypos 0.67
            
            text "{font=windowslogic-regular.ttf}{size=40}[amber_name]":
                xpos 0.5
                ypos 0.87
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        return
    return
    
    label stats_page_2:
        $ tooltip = Tooltip("")
    
        call screen stats_items_2 with dissolve
    
        screen stats_items_2:
    
            image "stats/stats.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
            
            text "{font=windowslogic-regular.ttf}{size=50}Your Information":
                xpos 0.32
                ypos 0.125
                
            text "{font=windowslogic-regular.ttf}{size=40}You are a Squirrel.":
                xpos 0.32
                ypos 0.182
                
            text "{font=windowslogic-regular.ttf}{size=40}Your real name is [real_name].":
                xpos 0.32
                ypos 0.232
                
            text "{font=windowslogic-regular.ttf}{size=40}Your age is [age].":
                xpos 0.32
                ypos 0.282
                
            text "{font=windowslogic-regular.ttf}{size=40}[other_info].":
                xpos 0.32
                ypos 0.332
                
            if virgin == 1:
                text "{font=windowslogic-regular.ttf}{size=40}You are a virgin.":
                    xpos 0.32
                    ypos 0.382
            elif virgin == 0:
                text "{font=windowslogic-regular.ttf}{size=40}You are not a virgin.":
                    xpos 0.32
                    ypos 0.382
            
            text "{font=windowslogic-regular.ttf}{size=50}Date Progress":
                xpos 0.32
                ypos 0.529
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.29
                ypos 0.786
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("stats_page_1")
                
            imagebutton auto "right_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.711
                ypos 0.786
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to next page.") ]
                action Jump("stats_page_3")
 
            if sierra == 2:
                image "stats/sierra_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 3:
                image "stats/sierra_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 4:
                image "stats/sierra_stats_3.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 5:
                image "stats/sierra_stats_4.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            else:
                $ sierra_name = ""
                image "stats/sierra_stats_0.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
                    
            if crystal == 2:
                image "stats/crystal_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif crystal == 3:
                image "stats/crystal_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif crystal == 4:
                image "stats/crystal_stats_3.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            elif sierra == 5:
                image "stats/crystal_stats_4.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            else:
                $ crystal_name = ""
                image "stats/crystal_stats_0.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.883
            
            text "{font=windowslogic-regular.ttf}{size=40}[sierra_name]":
                xpos 0.5
                ypos 0.67
            
            text "{font=windowslogic-regular.ttf}{size=40}[crystal_name]":
                xpos 0.5
                ypos 0.87
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        return
    return
    
    label stats_page_3:
        $ tooltip = Tooltip("")
    
        call screen stats_items_3 with dissolve
    
        screen stats_items_3:
    
            image "stats/stats.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
            
            text "{font=windowslogic-regular.ttf}{size=50}Your Information":
                xpos 0.32
                ypos 0.125
                
            text "{font=windowslogic-regular.ttf}{size=40}You are a Squirrel.":
                xpos 0.32
                ypos 0.182
                
            text "{font=windowslogic-regular.ttf}{size=40}Your real name is [real_name].":
                xpos 0.32
                ypos 0.232
                
            text "{font=windowslogic-regular.ttf}{size=40}Your age is [age].":
                xpos 0.32
                ypos 0.282
                
            text "{font=windowslogic-regular.ttf}{size=40}[other_info].":
                xpos 0.32
                ypos 0.332
            
            if virgin == 1:
                text "{font=windowslogic-regular.ttf}{size=40}You are a virgin.":
                    xpos 0.32
                    ypos 0.382
            elif virgin == 0:
                text "{font=windowslogic-regular.ttf}{size=40}You are not a virgin.":
                    xpos 0.32
                    ypos 0.382
            
            text "{font=windowslogic-regular.ttf}{size=50}Date Progress":
                xpos 0.32
                ypos 0.529
    
            imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.95
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("from_piss_jar")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.29
                ypos 0.786
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("stats_page_1")
 
            if christine == 2:
                image "stats/christine_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 3:
                image "stats/sierra_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 4:
                image "stats/sierra_stats_3.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 5:
                image "stats/sierra_stats_4.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            else:
                $ christine_name = ""
                image "stats/christine_stats_0.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
                    
            # if crystal == 2:
                # image "stats/crystal_stats_1.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.407
                    # ypos 0.883
            # elif crystal == 3:
                # image "stats/crystal_stats_2.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.407
                    # ypos 0.883
            # elif crystal == 4:
                # image "stats/christine_stats_3.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.407
                    # ypos 0.883
            # elif sierra == 5:
                # image "stats/christine_stats_4.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.407
                    # ypos 0.883
            # else:
                # $ crystal_name = ""
                # image "stats/crystal_stats_0.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.407
                    # ypos 0.883
            
            text "{font=windowslogic-regular.ttf}{size=40}[christine_name]":
                xpos 0.5
                ypos 0.67
            
            # text "{font=windowslogic-regular.ttf}{size=40}[crystal_name]":
                # xpos 0.5
                # ypos 0.87
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
        return
    return
return

label lamp:
    
    if gender == 0:
        
        if lamp == 1:
            scene hub_boy_dark
            $ lamp = 0
            call screen dates_dark
        else:
            scene hub_boy
            $ lamp = 1
            call screen dates
        
    elif gender == 1:
        
        if lamp == 1:
            scene hub_girl_dark
            $ lamp = 0
            call screen dates_dark
        else:
            scene hub_girl
            $ lamp = 1
            call screen dates
        
        play music "audio/girl_hub.flac" loop fadein 3.0
        scene hub_girl    
return

# Loading Screen

label loading:
    $ loading = renpy.random.randint(1, 6)
    
    if loading == 1:
        scene loading_violet
        with irisout
    elif loading == 2:
        scene loading_amber
        with irisout
    elif loading == 3:
        scene loading_sierra
        with irisout
    elif loading == 4:
        scene loading_crystal
        with irisout
    elif loading == 5:
        scene loading_christine
        with irisout
    else:
        scene loading_emma
        with irisout
return

# Game Over Screen

label game_over:
    scene game_over
    with dissolve
    
    pause 3.0
return

