# Defined characters.

define l = Character("Literature", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pv = Character("[violet_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define pa = Character("[amber_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define ps = Character("[sierra_name]", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define n = Character("Narrator", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define v = Character("Violet", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define a = Character("Amber", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])
define s = Character("Sierra", color="#000000", who_outlines=[ (2, "#FFFFFF") ], what_outlines=[ (2, "#FFFFFF") ])

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
    default s_items = 0
    default tooltip = Tooltip("")

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

# Gallery

label gallery:
    
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
                action Jump("main_hub_screen")
                
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
        
            text "Items Collected: [v_items]/0" outlines [(2, "#fff")]:
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
                action Jump("main_hub_screen")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.017
                ypos 0.5
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("gallery_page_1")
 
            if sierra >= 2:
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
                
            if sierra >= 3:
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
                
            if sierra >= 4:
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
                
            if sierra >= 4:
            
                imagebutton auto "gallery/v_panties_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.6
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
        
            text "Items Collected: [s_items]/0" outlines [(2, "#fff")]:
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
                
                    jump gallery
        
                "Insert it":
        
                    n "You insert the glass shard into your vagina, it's extremely painful and causes a lot of bleeding."
                
                    jump gallery
            
                "Throw it away":
        
                    n "You throw the glass shard in the bin."
            
                    $ a_item_1_collected = 0
                    $ a_items -= 1
                
                    jump gallery
    
        else:
            menu:
                "Rub your dick on it":
                
                    n "You rub your dick on the glass shard, it causes cuts on your shaft with a bit of blood."
                
                    jump gallery
                
                "Insert it in up your arse":
                
                    n "You insert the glass shard up your arse, you feel extreme pain and start shitting blood."
                
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
                
                    jump gallery
        
                "Eat the sap":
        
                    n "You put the sap in your mouth and chew on it, it tastes disgusting."
                
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
                
                    jump gallery
                
                "Sound the sap":
                
                    n "You insert the sap into your dick hole, it hurts a bit, but it makes you cum everywhere."
                
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
                
                    jump gallery
                
                "Empty the contents into your arse":
        
                    n "You pour the used condom's contents into your arse, it feels cold, wet and sticky. You might have an STD now."
                
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
                
                    jump gallery
                
                "Put the condom in your arsehole inside-out":
                
                    n "You insert the condom into your arsehole inside-out and feel the cold contents fill you up. You might have an STD now."
                
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
                
                    jump gallery
                
                "Crack the egg inside your pussy":
        
                    n "You crack the egg into your pussy and feel the cold, slimy liquid fill you up. "
                
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
                
                    jump gallery
                
                "Crack the egg into your arse":
                
                    n "You crack the egg into your arse and feel the cold, slimy liquid fill you up."
                
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
                
                    jump gallery
                
                "Insert it":
        
                    n "You insert the tree bark into your vagina and feel extreme pain from splinters."
                
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
                
                    jump gallery
                
                "Insert it up your arse":
                
                    n "You insert the tree bark and feel extreme pain from splinters."
                
                    jump gallery
                
                "Throw it away":
            
                    n "You throw the tree bark in the bin"
                
                    $ a_item_bark = 0
                    $ a_items -= 1
                
                    jump gallery
    return
return 

# Stats

label stats:
    
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
                action Jump("main_hub_screen")
                
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
                action Jump("main_hub_screen")
                
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.29
                ypos 0.786
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to previous page.") ]
                action Jump("stats_page_1")
 
            if sierra == 2:
                image "stats/violet_stats_1.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 3:
                image "stats/violet_stats_2.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.407
                    ypos 0.682
            elif sierra == 4:
                image "stats/violet_stats_3.png":
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

# Python crap (annoying shit).

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        
        return True