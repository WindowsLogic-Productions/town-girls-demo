# Defined characters.

define l = Character("Literature", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pv = Character("[violet_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pa = Character("[amber_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define ps = Character("[sierra_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define n = Character("Narrator", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define v = Character("Violet", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define a = Character("Amber", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define s = Character("Sierra", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])

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
    
    default gender = 0
    default dating = 1
    default violet = 1
    default amber = 1
    default sierra = 1
    default time = 3
    default bladder = 2
    default balls = 1
    default ovaries = 1
    default pissjar = 1
    default nightstalk = 1
    $ age = 18
    $ violet_name = ""
    $ violet_from = ""
    $ amber_name = ""
    $ amber_from = ""
    $ sierra_name = ""
    $ sierra_from = ""
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
    default s_fingered = 0
    default s_clothes = 0
    default s_wherefucked = 0
    default s_items = 0
    default s_item_leaflet = 0
    default s_item_stand = 0
    default tooltip = Tooltip("")
    default lamp = 0
    default loading = 0

    # Show a blank background for the game setup.
    
    scene blank
    with dissolve
    
    stop music
    
    # Ask question to user if they are a boy or girl and what age they are.
    
    n "Before we start, are you a boy or a girl? How old are you?"
    menu:
        n "What you choose will affect the story path."
        "Boy":
            $ achievement.grant("boy")
            $ gender = 0
            python:
                try:
                    age = int(renpy.input("Enter the age you want your character to be."))
                except Exception:
                    age = 18
            if age <= 18:
                $ achievement.grant("underage")
                $ age = 18
            $ violet = 1
            $ amber = 1
            jump starting_path
        "Girl":
            $ achievement.grant("girl")
            $ gender = 1
            python:
                try:
                    age = int(renpy.input("Enter the age you want your character to be."))
                except Exception:
                    age = 18
            if age <= 18:
                $ achievement.grant("underage")
                $ age = 18
            $ violet = 1
            $ amber = 1
            jump starting_path
return

label starting_path:

    $ renpy.block_rollback()
    
    show screen bodystats
    
    scene car
    with dissolve
    
    play music "audio/car_music.flac" loop fadein 3.0
    
    play sound "audio/rain.flac" loop fadein 3.0
    
    pause 3.0
    
    if gender == 0:
        
        n "The rain splashes heavily in the puddles outside as if the heavens are crying, as you make your way to your destination."
    
        n "The car radio drones on a discordant rock tune."
    
        n "You feel a pit in your stomach as you've never been this far away from home before."
    
        n "You're moving to a small town because your parents are divorcing."

        n "You want to start making friends with the local girls, and maybe even get into their panties."
        
    elif gender == 1:
        
        n "The rain splashes heavily in the puddles outside as if the heavens are crying, as you make your way to your destination."
    
        n "The car radio drones on a discordant rock tune."
    
        n "You feel a pit in your stomach as you've never been this far away from home before."

        n "You're moving to a small town because your attending a university there."
    
        n "Recently, you came out as lesbian to your old friends, but you're afraid of what the animals in this new town will think."
    
    
    scene house
    with dissolve
    
    n "The car screeches to a halt. You have arrived at your new home..."
    
    play audio "audio/thunder.flac"
    
    n "You grab your bags and head inside. You look around and find a study with a desk and a pinboard. You decide to use this as your ''base of operations.''"
    
    stop music fadeout 3.0
    
    stop sound fadeout 3.0
    
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

    show screen dates

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
        
            text "Items Collected: [s_items]/2" outlines [(2, "#fff")]:
                xpos 0.46
                ypos 0.13
            
            text "":
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
            
            image "stats/your_information.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.29
            
            image "hub/date_progress_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.405
                ypos 0.545
    
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
                
            text "[age]":
                xpos 0.36
                ypos 0.33
            
            text "[violet_name]":
                xpos 0.5
                ypos 0.67
            
            text "[amber_name]":
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
            
            image "stats/your_information.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.29
            
            image "hub/date_progress_title.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.405
                ypos 0.545
    
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
                image "stats/violet_stats_4.png":
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
                
            text "[age]":
                xpos 0.36
                ypos 0.33
            
            text "[sierra_name]":
                xpos 0.5
                ypos 0.67
            
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

label game_over:
    scene game_over
    with dissolve
    
    pause 3.0
return

# Python crap (annoying shit).

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        
        return True