# Loads the main hub for boys.

label main_hub_screen:
    
    $ renpy.block_rollback()
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    show screen bodystats
    
    $ tooltip = Tooltip("")
    
    if gender == 0:
        
        play music "audio/boy_hub.flac" loop fadein 3.0
        
        if lamp == 1:
            scene hub_boy
            with pixellate
            if bladder == 3:
                n "You feel something warm trickle down your legs, leaving a puddle on the floor."
                $ bladder = 1
            else:
                $ bladder += 1
            call screen dates with dissolve
            
            
        else:
            scene hub_boy_dark
            with pixellate
            if bladder == 3:
                n "You feel something warm trickle down your legs, leaving a puddle on the floor." 
                $ bladder = 1
            else:
                $ bladder += 1
            call screen dates_dark with dissolve
        
    elif gender == 1:
    
        play music "audio/girl_hub.flac" loop fadein 3.0
    
        if lamp == 1:
            scene hub_girl
            with pixellate
            if bladder == 3:
                n "You feel something warm trickle down your legs, leaving a puddle on the floor."
                $ bladder = 1
            else:
                $ bladder += 1
            call screen dates with dissolve
        else:
            scene hub_girl_dark
            with pixellate
            if bladder == 3:
                n "You feel something warm trickle down your legs, leaving a puddle on the floor."
                $ bladder = 1
            else:
                $ bladder += 1
            call screen dates_dark with dissolve
return

# Return from pissing in the jar.

label from_piss_jar:

    $ renpy.block_rollback()
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    show screen bodystats
    
    $ tooltip = Tooltip("")
    
    if gender == 0:
        
        if lamp == 1:
            scene hub_boy
            with dissolve
            call screen dates with dissolve
            
        else:
            scene hub_boy_dark
            with dissolve
            call screen dates_dark with dissolve
        
    elif gender == 1:
    
        if lamp == 1:
            scene hub_girl
            with dissolve
            call screen dates with dissolve
        else:
            scene hub_girl_dark
            with dissolve
            call screen dates_dark with dissolve

return

#Dates and click-able hub objects.

screen dates_dark:

    # General hub button settings.
    
    if time == 1:
        image "hub/clock_10AM.png":
            xpos 0.8
            ypos 0.44
    elif time == 2:
        image "hub/clock_2PM.png":
            xpos 0.8
            ypos 0.44
    else:
        image "hub/clock_6PM.png":
            xpos 0.8
            ypos 0.44
            
    if pissjar == 1:
        imagebutton auto "hub/piss_jar_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder into the jar you keep under the desk.") ]
            action Jump("pissjarno")
    if pissjar == 2:
        imagebutton auto "hub/piss_jar_half_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder into the jar you keep under the desk.") ]
            action Jump("pissjarno")
    if pissjar == 3:
        imagebutton auto "hub/piss_jar_full_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder or empty the jar.") ]
            action Jump("pissjarno")
    
    imagebutton auto "hub/clipboard_dark_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.97
        ypos 0.5
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("View date progress and stats about yourself.") ]
        action Jump("stats")
    
    imagebutton auto "hub/lamp_dark_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.886
        ypos 0.65
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Turn the lamp on.") ]
        action Jump("lamp")
        
    imagebutton auto "hub/draws_dark_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.055
        ypos 0.94
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Visit the gallery to look back on pictures girls have given you and possessions you've stolen.") ]
        action Jump("gallery")
        
    imagebutton auto "hub/toilets_dark_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.89
        ypos 0.13
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Peak on girls in the local public toilets outside.") ]
        action Jump("toilets_opening")
        
    imagebutton auto "hub/outside_dark_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.89
        ypos 0.33
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go outside to revisit date locations and more.") ]
        action Jump("outside_map")

    # Violet hub button settings.
    
    if violet == 2:
        imagebutton auto "hub/violet_dated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Violet.") ]
            action Jump("date_violet_timecheck")
    elif violet == 3:
        imagebutton auto "hub/violet_dated2_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Violet.") ]
            action Jump("date_violet_timecheck")
    elif violet == 4:
        imagemap auto "hub/violet_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    elif violet == 5:
        imagemap auto "hub/violet_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    else:
        imagebutton auto "hub/violet_undated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Arctic Fox.") ]
            action Jump("date_violet_opening")
            
    if violet > 1:
        imagebutton auto "cloppad_dark_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.212
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Violet's ClopPad.") ]
            action Jump("date_violet_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            
    # Amber hub button settings.
    
    if amber == 2:
        imagebutton auto "hub/amber_dated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif amber == 3:
        imagebutton auto "hub/amber_dated2_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif amber == 4:
        imagemap auto "hub/amber_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    elif amber == 5:
        imagemap auto "hub/amber_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        imagebutton auto "hub/amber_undated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Tabby Cat.") ]
            action Jump("date_amber_opening")
            
    if amber > 1:
        imagebutton auto "cloppad_dark_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.402
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Amber's ClopPad.") ]
            action Jump("date_amber_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            
    # Sierra hub button settings.
    
    if sierra == 2:
        imagebutton auto "hub/sierra_dated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Sierra.") ]
            action Jump("date_sierra_timecheck")
    elif sierra == 3:
        imagebutton auto "hub/sierra_dated2_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Sierra.") ]
            action Jump("date_sierra_timecheck")
    elif sierra == 4:
        imagemap auto "hub/sierra_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
    elif sierra == 5:
        imagemap auto "hub/sierra_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
    else:
        imagebutton auto "hub/sierra_undated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Red Fox.") ]
            action Jump("date_sierra_opening")
            
    if sierra > 1:
        imagebutton auto "cloppad_dark_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.592
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Sierra's ClopPad.") ]
            action Jump("date_sierra_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            
    # Crystal hub button settings.
    
    if crystal == 2:
        imagebutton auto "hub/crystal_dated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Crystal.") ]
            action Jump("date_crystal_timecheck")
    elif crystal == 3:
        imagebutton auto "hub/crystal_dated2_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Violet.") ]
            action Jump("date_violet_timecheck")
    elif crystal == 4:
        imagemap auto "hub/crystal_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
    elif crystal == 5:
        imagemap auto "hub/crystal_dated3_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
    else:
        imagebutton auto "hub/crystal_undated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Sheep.") ]
            action Jump("date_crystal_timecheck")
            # ^^^ Temp. Change when opening is done!!!
            
    if crystal > 1:
        imagebutton auto "cloppad_dark_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.212
            ypos 0.646
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Crystal's ClopPad.") ]
            action Jump("date_crystal_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            
    text tooltip.value outlines [(2, "#fff")]:
        xpos 0.11
        ypos 0.9
        
    # Christine hub button settings.
    
    if christine == 2:
        imagebutton auto "hub/christine_dated_dark_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Christine.") ]
            action Jump("date_christine_timecheck")
            # ^^^ Temp! Change when opening is complete.
    elif christine == 3:
        imagebutton auto "hub/amber_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif christine == 4:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    elif christine == 5:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        image "hub/christine_undated_dark_idle.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.55
    
    if christine > 2:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.402
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Christine's ClopPad.") ]
            action Jump("date_christine_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    
    text tooltip.value outlines [(2, "#fff")]:
        xpos 0.11
        ypos 0.9
return
      
screen dates:

    # General hub button settings.
    
    if time == 1:
        image "hub/clock_10AM.png":
            xpos 0.8
            ypos 0.44
    elif time == 2:
        image "hub/clock_2PM.png":
            xpos 0.8
            ypos 0.44
    else:
        image "hub/clock_6PM.png":
            xpos 0.8
            ypos 0.44
            
    if pissjar == 1:
        imagebutton auto "hub/piss_jar_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder into the jar you keep under the desk.") ]
            action Jump("pissjarno")
    if pissjar == 2:
        imagebutton auto "hub/piss_jar_half_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder into the jar you keep under the desk.") ]
            action Jump("pissjarno")
    if pissjar == 3:
        imagebutton auto "hub/piss_jar_full_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.92
            ypos 0.95
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Empty your bladder or empty the jar.") ]
            action Jump("pissjarno")
    
    imagebutton auto "hub/clipboard_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.97
        ypos 0.5
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("View date progress and stats about yourself.") ]
        action Jump("stats")
    
    imagebutton auto "hub/lamp_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.886
        ypos 0.65
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Turn the lamp off.") ]
        action Jump("lamp")
        
    imagebutton auto "hub/draws_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.055
        ypos 0.94
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Visit the gallery to look back on pictures girls have given you and possessions you've stolen.") ]
        action Jump("gallery")
        
    imagebutton auto "hub/toilets_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.89
        ypos 0.13
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Peak on girls in the local public toilets outside.") ]
        action Jump("toilets_opening")
        
    imagebutton auto "hub/outside_%s.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.89
        ypos 0.33
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go outside to revisit date locations and more.") ]
        action Jump("outside_map")

    # Violet hub button settings.

    if violet == 2:
        imagebutton auto "hub/violet_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Violet.") ]
            action Jump("date_violet_timecheck")
    elif violet == 3:
        imagebutton auto "hub/violet_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Violet.") ]
            action Jump("date_violet_timecheck")
    elif violet == 4:
        imagemap auto "hub/violet_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    elif violet == 5:
        imagemap auto "hub/violet_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    else:
        imagebutton auto "hub/violet_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Arctic Fox.") ]
            action Jump("date_violet_opening")
    
    if violet > 1:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.212
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Violet's ClopPad.") ]
            action Jump("date_violet_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    
    # Amber hub button settings.
    
    if amber == 2:
        imagebutton auto "hub/amber_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif amber == 3:
        imagebutton auto "hub/amber_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif amber == 4:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    elif amber == 5:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        imagebutton auto "hub/amber_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Tabby Cat.") ]
            action Jump("date_amber_opening")
    
    if amber > 1:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.402
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Amber's ClopPad.") ]
            action Jump("date_amber_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    
    # Sierra hub button settings.
    
    if sierra == 2:
        imagebutton auto "hub/sierra_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Sierra.") ]
            action Jump("date_sierra_timecheck")
    elif sierra == 3:
        imagebutton auto "hub/sierra_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Sierra.") ]
            action Jump("date_sierra_timecheck")
    elif sierra == 4:
        imagemap auto "hub/sierra_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
    elif sierra == 5:
        imagemap auto "hub/sierra_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
    else:
        imagebutton auto "hub/sierra_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Red Fox.") ]
            action Jump("date_sierra_opening")
            
    if sierra > 1:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.592
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Sierra's ClopPad.") ]
            action Jump("date_sierra_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            
    # Crystal hub button settings.
    
    if crystal == 2:
        imagebutton auto "hub/crystal_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Crystal.") ]
            action Jump("date_crystal_timecheck")
    elif crystal == 3:
        imagebutton auto "hub/violet_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Violet.") ]
            action Jump("date_crystal_timecheck")
    elif crystal == 4:
        imagemap auto "hub/violet_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
    elif crystal == 5:
        imagemap auto "hub/violet_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
    else:
        imagebutton auto "hub/crystal_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Sheep.") ]
            action Jump("date_crystal_timecheck")
            # ^^^ Temp. Change when opening is done!!!
            
    if crystal > 1:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.212
            ypos 0.646
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Crystal's ClopPad.") ]
            action Jump("date_crystal_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    
    # Christine hub button settings.
    
    if christine == 2:
        imagebutton auto "hub/christine_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.55
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Christine.") ]
            action Jump("date_christine_timecheck")
            # ^^^ Temp. Change when opening is done!!!
    elif christine == 3:
        imagebutton auto "hub/amber_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_timecheck")
    elif christine == 4:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    elif christine == 5:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        image "hub/christine_undated_idle.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.55
    
    if christine > 2:
        imagebutton auto "cloppad_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.402
            ypos 0.346
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go to Christine's ClopPad.") ]
            action Jump("date_amber_opening")
    else:
        image "debug":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    
    text tooltip.value outlines [(2, "#fff")]:
        xpos 0.11
        ypos 0.9
return