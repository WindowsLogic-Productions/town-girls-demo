# Loads the main hub for boys.

label main_hub_screen:
    
    $ renpy.block_rollback()
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    
    $ tooltip = Tooltip("")
    
    if gender == 0:
        
        play music "audio/boy_hub.flac" loop fadein 3.0
        scene hub_boy
        with pixellate
        
    elif gender == 1:
        
        play music "audio/girl_hub.flac" loop fadein 3.0
        scene hub_girl
        with pixellate

    
    call screen dates with dissolve
return

#Dates and clickable hub objects.
      
screen dates:

    # General hub button settings.
    
    if time == 1:
        text "Time: 10 AM":
            xpos 0.8
            ypos 0.44
    elif time == 2:
        text "Time: 2 PM":
            xpos 0.8
            ypos 0.44
    else:
        text "Time: 6 PM":
            xpos 0.8
            ypos 0.44
    
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
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("This is a desk lamp. It lights up areas in a space.") ]
        clicked [ Play("audio", "audio/boing.flac") ]
        
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
        ypos 0.23
        hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Peak on girls in the local public toilets outside.") ]
        action Jump("toilets_opening")

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
    else:
        imagebutton auto "hub/violet_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Arctic Fox.") ]
            action Jump("date_violet_opening")
            
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
    else:
        imagebutton auto "hub/amber_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Tabby Cat.") ]
            action Jump("date_amber_opening")
            
    # Sierra hub button settings.
    
    if sierra == 2:
        imagebutton auto "hub/amber_dated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a second date with Amber.") ]
            action Jump("date_amber_2_pc")
    elif sierra == 3:
        imagebutton auto "hub/amber_dated2_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_sex")
    elif sierra == 4:
        imagemap auto "hub/amber_dated3_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        imagebutton auto "hub/sierra_undated_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.24
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Go on a first date with the Red Fox.") ]
            action Jump("date_sierra_opening")
            
    text tooltip.value outlines [(2, "#fff")]:
        xpos 0.11
        ypos 0.9
return