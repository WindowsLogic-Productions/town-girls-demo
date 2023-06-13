# Sierra's opening scene.

label date_sierra_opening:

    show screen dates

    n "Coming soon..."
    
    jump main_hub_screen
    
    scene a_start_0
    with dissolve
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/opening.flac" loop fadein 3.0
    
    pause 3.0
    
    
return

# Amber first date.

label date_sierra_1_pc:

    $ achievement.grant("first")
    
    scene a_shop_outside
    with dissolve
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/rain.flac" loop fadein 3.0
    
    pause 3.0
    
    
return

label date_sierra_1:

    
return

# Sierra fail date.

label sierra_fail_date:

        stop music
        
        $ renpy.block_rollback()
        
        if amber == 2:
            show amber angry hn at center with dissolve
            
            $ a_item_2_collected = 0
            $ a_item_3_collected = 0
            $ a_item_4_collected = 0
            $ a_item_5_collected = 0
            if a_item_5_collected == 1:
                $ a_items -= 4
            else:
                $ a_items = 1
        else:
            show amber angry at center with dissolve
            
            $ a_item_1_collected = 0
            $ a_items = 0
        
        a "I thought we really had something [amber_name]. I can't believe this."
        
        play audio "audio/date_fail.flac"
        n "Date failed..."
        
        jump main_hub_screen     
return

# Sierra succeed dates.

label sierra_succeed_date:

    if amber == 1:
    
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with dissolve
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Amber. You can now look at this picture in the Gallery."
    
        $ achievement.grant("amber_1_success")
    
        call screen amber_pic_1 with dissolve
    
        screen amber_pic_1:
        
            imagebutton idle "amber_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("a_variable_update")
        return
    elif amber == 2:
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with dissolve
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Amber. You can now look at this picture in the Gallery."
    
        $ achievement.grant("amber_2_success")
    
        call screen amber_pic_2 with dissolve
    
        screen amber_pic_2:
        
            imagebutton idle "amber_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("a_variable_update")
                
    elif amber == 3:
        play music "audio/amber_theme.flac" fadein 3.0

        if gender == 0:
            scene a_sex_scene_cum
            with dissolve
        if gender == 1:
            scene a_sex_scene_squirt
            with dissolve
            
        a "A- Are we done already? T- That felt really good…"
        
        if gender == 0:
            if a_item_boxedcondoms == 0:
            
                scene a_sex_scene_cum_realise
                with dissolve
            
                a "W- Wait… I- If your spout is out… W- What’s inside me…?"
                
                scene a_sex_scene_cum_shock
                with dissolve
                
                a "Y- You c- came i- in m- me…"
                
                
            else:
                
                scene a_sex_scene_cum_realise
                with dissolve
                
                a "T- Thank you for wearing protection, I was worried I was going to end up preg-"
                
                scene a_sex_scene_cum_shock
                with dissolve
                
                a "Y- You w- weren’t w- wearing t- the c- condom…"
                
        elif gender == 1:
            a "I- I t- think y- you m- made m- me c- cum..."
    
        if gender == 0:
            scene a_sex_scene_cum_shock_cry
            with dissolve
            
            a "I- I’m g- going t- to b- be p- pregnant…"
                
            # TODO: End scene needed.
            scene blank
            with dissolve
        
            n "Amber gets up, pushes you out of the way and runs out of the shop naked and crying leaving a trail of cum."
        elif gender == 1:
            scene a_sex_scene_squirt_neutral
            with dissolve
            
            a "I- I didn't think I liked girls until I met you."
            
            a "B- But now that I've had sex with you, I'm happy it was girl who I did it with first time."
        
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.flac"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
    
        scene blank
        with dissolve
    
        if gender == 0:
            n "You might have made Amber pregnant and took her panties."
        elif gender == 1:
            n "You took Amber's panties."
        
        $ achievement.grant("amber_3_success")
    
        jump s_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label s_variable_update:
    
    $ dating += 1
    $ amber += 1
    jump main_hub_screen
    
    return

return