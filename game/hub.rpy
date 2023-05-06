# Loads the main hub for boys.

label main_hub_screen:
    
    $ renpy.block_rollback()
    
    $ tooltip = Tooltip("")
    
    if gender == 0:
        
        play music "audio/boy_hub.tgm" loop fadein 3.0
        scene hub_boy
        with dissolve
        
    elif gender == 1:
        
        play music "audio/girl_hub.tgm" loop fadein 3.0
        scene hub_girl
        with dissolve

    
    call screen dates with dissolve
return

#Dates and clickable hub objects.
      
screen dates:

    # General hub button settings.
    
    imagebutton auto "hub/clipboard_%s.tgp":
        xanchor 0.5
        yanchor 0.5
        xpos 0.97
        ypos 0.5
        hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("View date progress and stats about yourself.") ]
        action Jump("stats")
    
    imagebutton auto "hub/lamp_%s.tgp":
        xanchor 0.5
        yanchor 0.5
        xpos 0.886
        ypos 0.65
        hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("This is a desk lamp. It lights up areas in a space.") ]
        clicked [ Play("audio", "audio/boing.tgm") ]
        
    imagebutton auto "hub/draws_%s.tgp":
        xanchor 0.5
        yanchor 0.5
        xpos 0.055
        ypos 0.94
        hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Visit the gallery to look back on pictures girls have given you.") ]
        action Jump("gallery")
        
    imagebutton auto "hub/toilets_%s.tgp":
        xanchor 0.5
        yanchor 0.5
        xpos 0.89
        ypos 0.23
        hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Peak on girls in the local public toilets outside.") ]
        action Jump("toilets_boy")

    # Violet hub button settings.

    if violet == 2:
        imagebutton auto "hub/violet_dated_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a second date with Violet.") ]
            action Jump("date_violet_2_pc")
    elif violet == 3:
        imagebutton auto "hub/violet_dated2_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a third date with Violet.") ]
            action Jump("date_violet_sex_letter")
    elif violet == 4:
        imagemap auto "hub/violet_dated3_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
    else:
        imagebutton auto "hub/violet_undated_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.16
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a first date with the Arctic Fox.") ]
            action Jump("date_violet_1_pc")
            
    # Amber hub button settings.
    
    if amber == 2:
        imagebutton auto "hub/amber_dated_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a second date with Amber.") ]
            action Jump("date_amber_2_pc")
    elif amber == 3:
        imagebutton auto "hub/amber_dated2_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a third date with Amber.") ]
            action Jump("date_amber_sex")
    elif amber == 4:
        imagemap auto "hub/amber_dated3_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
    else:
        imagebutton auto "hub/amber_undated_%s.tgp":
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.24
            hovered [ Play("sound", "audio/select.tgm"), tooltip.Action("Go on a first date with the Tabby Cat.") ]
            action Jump("date_amber_1_pc")
            
    text tooltip.value:
        xpos 0.11
        ypos 0.9
return