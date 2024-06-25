# Christine's opening scene.

label date_christine_opening:

    $ tooltip = Tooltip("")
    
    $ _game_menu_screen = None
    $ quick_menu = False
    hide screen bodystats
    hide screen dates
    hide screen dates_dark
    
    call loading from _call_loading_1000
    
    stop music fadeout 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    play music "audio/opening.flac" loop fadein 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    
    # Christine doesn't have a pre-opening.
    
    label posts_chp1:
    
        call screen date_christine_opening_objects_ap1 with dissolve

        screen date_christine_opening_objects_ap1:
        
            if christine == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_christine_timecheck")
            else:
                image "debug":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
            
            imagebutton auto "user_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.932
                ypos 0.018
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("main_hub_screen")
            
            imagebutton auto "ch_120915_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "ch_040816_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s2")
                
            imagebutton auto "ch_080518_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "ch_050620_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s3")
                
            imagebutton auto "ch_060521_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s4")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label online_pic_ch1:
    
        call screen online_pic_ch1 with dissolve
        
        screen online_pic_ch1:
        
            imagebutton idle "s_start_0":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_chp1")
            
        return
    return
    
    label online_pic_ch2:
    
        call screen online_pic_ch2 with dissolve
        
        screen online_pic_ch2:
        
            imagebutton idle "s_start_1":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_chp1")
            
        return
    return
    
    label online_pic_ch3:
    
        call screen online_pic_ch3 with dissolve
        
        screen online_pic_ch3:
        
            imagebutton idle "s_start_2":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_ch4:
    
        call screen online_pic_s4 with dissolve
        
        screen online_pic_s4:
        
            imagebutton idle "s_start_3":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_ch5:
    
        call screen online_pic_s5 with dissolve
        
        screen online_pic_s5:
        
            imagebutton idle "s_start_4":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp2")
            
        return
    return
return

# Check time of game to determine if dates are possible.

label date_christine_timecheck:

    hide screen bodystats
    hide screen dates
    hide screen dates_dark

    $ loading = renpy.random.randint(1, 3)
    
    call loading from _call_loading_1001
    
    $ _game_menu_screen = None
    $ quick_menu = False
    
    $ renpy.pause(3.0, hard=True)

    if time == 1:
        if christine == 1:
            jump date_christine_1_pc
        elif christine == 2:
            jump date_christine_timechecked_working
        else:
            jump date_christine_timechecked_working
    elif time == 2:
        if christine == 1:
            jump date_christine_1_pc
        elif christine == 2:
            jump date_christine_2_pc
        else:
            jump date_christine_timechecked_working
    else:
        if christine == 1:
            jump date_christine_1_pc
        elif christine == 2:
            jump date_christine_timechecked_sleeping
        else:
            jump date_christine_sex
return

label date_christine_timechecked_working:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/christine_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_blur
    with dissolve
    
    n "Christine is currently busy doing photo shoots, do you want to advance time?"
        
    menu:
        "Sleep for a few hours.":
        
            n "You sleep for a few hours."
            
            $ time += 1
            $ bladder += 1
                
            jump main_hub_screen
                
        "Go to Christine's house.":
                
            n "You go to Christine's house with a ladder. You position the ladder and climb up to stalk her."
                
            $ nightstalk = renpy.random.randint(1, 5)
                
            if nightstalk == 1:
                
                n "You find Christine in a sexy nun outfit, taking pictures of herself."
                
                scene s_masturbate_bottle
                with pixellate
            elif nightstalk == 2:
            
                n "You find Christine in a sexy nun outfit, taking pictures of herself with exposed breasts."
                
                scene s_masturbate_desk
                with pixellate
            elif nightstalk == 3:
            
                n "You find Christine in a sexy nun outfit, taking pictures of herself with no panties."
            
                scene s_masturbate_finished
                with pixellate
            elif nightstalk == 4:
            
                n "You find Christine in a sexy nun outfit, taking pictures of herself with fake cum everywhere."
            
                scene s_masturbate_tablet
                with pixellate
            else:
                
                n "You find Christine in a sexy nun outfit, taking pictures of herself with a dildo cumming inside her."
                
                scene s_masturbate_starting
                with pixellate
                
            pause 120.0
                
            $ time += 1
            $ bladder = 2
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

label date_christine_timechecked_sleeping:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/christine_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_night_blur
    with dissolve

    n "Christine is currently sleeping, do you want to advance time?"
        
    menu:
        "Go to sleep.":
            
            n "You sleep until morning."
                
            $ time = 1
            $ bladder = 2
                
            jump main_hub_screen
                
        "Go to Christine's flat and watch her sleep until morning.":
                
            n "You go to christine's flat with a ladder. Her bedroom window is open so you position the ladder and climb up."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                
                n "You find Christine sleeping naked on her computer chair."
                
                scene s_sleeping_pen
                with pixellate
            elif nightstalk == 2:
            
                n "You find christine sleeping in the middle of squirting on her bed."
            
                scene s_sleeping_squirt
                with pixellate
            elif nightstalk == 3:
            
                n "You find christine sleeping in the middle of squirting on her bed with a wet pen in her vagina."
            
                scene s_sleeping_squirt_pen
                with pixellate
            else:
                
                n "You find christine sleeping with a wet pen in her vagina."
                
                scene s_sleeping_wet_pen
                with pixellate
            
            pause 120.0
                
            $ time = 1
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

# christine first date.

label date_christine_1_pc:

    $ achievement.grant("first")
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene chr_outsidesc_pc
    with irisout
    
    show screen bodystats
    
    play music "audio/strippin_outside.flac" loop fadein 3.0
    play voice "audio/town_night.flac" loop fadein 3.0
    
    n "After getting served at the local strip club, you notice a younger sheep outside trying to ask passersby for sexual favours. Do you approach?"
    
    label ch1_jump_from_collect:
    
    scene chr_outsidesc_pc
    with dissolve
    
    call screen date_christine_1_objects with dissolve

    screen date_christine_1_objects:
        
        imagebutton auto "christine_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.58
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Lamb: I wish someone would take my virginity...") ]
                action Jump("date_christine_1")
                
        # if s_item_leaflet == 0:
            # imagebutton auto "s_museum_flyer_%s":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.35
                    # ypos 0.80
                    # hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Looks like a leaflet from the museum.") ]
                    # action Jump("s_collect_item_1")
        # else:
            # imagebutton idle "debug.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.5
                    # ypos 0.67
        
        # if s_item_stand == 0:
            # imagebutton auto "s_museum_board_%s":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.60
                    # ypos 0.56
                    # hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The museum board, looks like they have a nude figure painting session on today.") ]
                    # action Jump("s_collect_item_2")
        # else:
            # imagebutton idle "debug.png":
                    # xanchor 0.5
                    # yanchor 0.5
                    # xpos 0.5
                    # ypos 0.67
        
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
    
    return
    return
    
    # label ch_collect_item_1:
    
        # if s_item_leaflet == 1:
        
            # scene s_museum
            # with dissolve
        
            # n "You search around the front of the museum again and find nothing."
        # else:
        
            # scene s_museum_pc_blur
            # with dissolve
        
            # show s_leaflet at center with dissolve
        
            # n "You pick up the leaflet off the floor."
            # $ s_item_leaflet += 1
            # $ s_items += 1
        
            # hide s_leaflet at center with dissolve
        
        # jump s1_jump_from_collect
    # return
    
    # label ch_collect_item_2:
    
        # if s_item_stand == 1:
        
            # scene s_museum_pc
            # with dissolve
        
            # n "You search around the front of the museum again and find nothing."
        # else:
        
            # scene s_museum_pc_blur
            # with dissolve
        
            # show s_board at center with dissolve
        
            # n "You steal the museum notice board."
            # $ s_item_stand += 1
            # $ s_items += 1
        
            # hide s_board at center with dissolve
        
        # jump s1_jump_from_collect
    # return
return

label date_christine_1:

    scene chr_outsidesc_pc
    with dissolve
    
    stop music fadeout 3.0
    stop voice fadeout 3.0
    
    pause 3.0
    
    play music "audio/christine_theme_date_1.flac" loop fadein 3.0
    
    pause 3.0
    
    show christine think at center with dissolve
    
    ch "Hey there, do you wanna go around back and take my virginity?"
    
    show christine neutral at center with dissolve
    
    ch "I can set you up for a reasonable price, it’s an offer you can’t refuse. "
    
    show christine giggle at center with dissolve
    
    ch "Oh, silly me, I haven’t even introduced myself or asked your name."
    
    ch "My name is Christine, what's yours?"
    
    show christine think at center with dissolve
        
    $ christine_name = renpy.input("Enter a name you want Christine to remember.")
    $ christine_name = christine_name.strip()
    if christine_name == "":
        $ christine_name = "Person"
        
    $ renpy.block_rollback()
    
    play audio "audio/remember.flac"
    n "Christine will remember that."
    
    ch "Huh, [christine_name] is a sexy name."
    
    pc "I’m [age], what about you? You look very young and subtle..."
    
    show christine angry at center with dissolve
    
    ch "I’m 19, my mother says I’m still a baby."
    
    show christine think at center with dissolve
    
    ch "I saw you come out of the strip club; did you meet my mum there at all?"
    
    show christine neutral at center with dissolve
    
    ch "She knows what I do online on a site called ClopPad, but she says she accepts whatever makes me happy."
    
    show christine laugh at center with dissolve
    
    ch "If you followed, I’m sure you’d like what you see."
    
    menu:
        "What's ClopPad?":
            pc "What's ClopPad?"
            
            show christine laugh at center with dissolve
            
            ch "Oh, it’s a site where you can post anything you want, including nudes for horny men like I do."
        
        "Oh wow, I'll follow you.":
            pc "Oh wow, I'll follow you."
            
            show christine giggle at center with dissolve
            
            ch "Thank you, I hope that gets me closer to my sex working career."
            
    show christine neutral at center with dissolve
    
    ch "I wish people would see me for my sexual ability."
    
    show christine lust at center with dissolve
    
    ch "You seem nice. Would you like to be the one to take my virginity? No payment necessary."
    
    menu:
        "Oh, yeah, sure.":
            pc "Oh, yeah, sure."
            
            show christine shock at center with dissolve
            
            ch "Wait, really?"
            
            show christine lust at center with dissolve
            
            if gender == 0:
                ch "Yes! I can’t wait to feel cock for the first time."
            elif gender == 1:
                ch "Yes! I can’t wait to feel pussy for the first time."
        
        "No thanks, I’m not into virgins.":
            pc "No thanks, I’m not into virgins."
            
            show christine angry at center with dissolve
            
            ch "Oh, I see what type you’re into. You don’t see my sexual ability."
            
            jump christine_fail_date
            
    if gender == 0:
            menu:
                "Do you want me to cum inside too?":
                    pc "Do you want me to cum inside too?"
            
                    show christine euphoric at center with dissolve
            
                    ch "Yes! Make me your teenage cumslut and brim me!"
        
                "No cumming, I can't afford extra baggage.":
                    pc "No cumming, I can't afford extra baggage."
            
                    show christine giggle at center with dissolve
            
                    ch "Awww, why not? I'd love to feel you brim my pussy, even if I'm not on any contraception."
    elif gender == 1:
            menu:
                "Do you want me to cum too?":
                    pc "Do you want me to cum too?"
            
                    show christine euphoric at center with dissolve
            
                    ch "Yes! Make me your teenage slut and squirt all over me!"
        
                "No cumming, that's too messy.":
                    pc "No cumming, that's too messy."
            
                    show christine giggle at center with dissolve
            
                    ch "Awww, why not? I'd love for you to soak me in girl cum."
    
    show christine neutral at center with dissolve
            
    ch "If you want to know what else I’m into, I like getting drunk at parties and doing crazy shit."
    
    show christine lust at center with dissolve
    
    ch "I’m surprised no one has tried knocking me up while I’m piss drunk, I would’ve enjoyed it."
    
    menu:
        "What’s your favourite alcoholic drink?":
            pc "What’s your favourite alcoholic drink?"
            
            show christine neutral at center with dissolve
            
            ch "It depends on how I’m feeling, but most of the time, I drink wine."
            
            show christine giggle at center with dissolve
            
            ch "Sometimes if I’m feeling extra silly, I drink shots and vodka to get wild."
            
            show christine euphoric at center with dissolve
            
            ch "This one time, I stripped completely naked and passed out."
            
            show christine lust at center with dissolve
            
            ch "The people at the party took pictures of my naked body and one even took a video of fingering me until I came on the floor."
            
            ch "They sent these to me on ClopPad afterwards and I felt so happy that they thought I was that hot."
            
        "What do you do in your spare time?":
            pc "What do you do in your spare time?"
            
            show christine neutral at center with dissolve
            
            ch "I’m a student at the local Puddleshire University."
            
            ch "I’m studying biology as I have a fascination with sex and reproduction."
            
        "Take off your clothes.":
            pcy "Take off your clothes."
            
            show christine shock at center with dissolve
            
            ch "Right now? In public?"
            
            show christine lust at center with dissolve
            
            ch "Oh my God, yeah!"
            
            show christine giggle n at center with dissolve
            
            $ ch_naked = 1
            
            ch "I've never gotten naked in front of anyone before."
            
            ch "Let alone, in public."
            
            show christine laugh n at center with dissolve
            
            ch "So thrilling."
            
    menu:
        "Do you have any confessions or secrets?":
            pc "Do you have any confessions or secrets?"
            
            if ch_naked == 0:
                show christine euphoric at center with dissolve
            elif ch_naked == 1:
                show christine euphoric n at center with dissolve
            
            ch "Truthfully, when my mum and her clients are fucking in the room next door to mine, I masturbate over the noises."
            
            if ch_naked == 0:
                show christine giggle at center with dissolve
            elif ch_naked == 1:
                show christine giggle n at center with dissolve
            
            ch "The reason I do that is because I wish it was me getting fucked."
            
        "Do you have any kinks?":
            pc "Do you have any kinks?"
            
            if ch_naked == 0:
                show christine lust at center with dissolve
            elif ch_naked == 1:
                show christine lust n at center with dissolve 
            
            ch "I want to let the person I have sex with decide what kinks we do."
            
            if ch_naked == 0:
                show christine neutral at center with dissolve
            elif ch_naked == 1:
                show christine neutral n at center with dissolve
            
            ch "I personally don’t really have any kinks other than selling my body."
            
        "Do you do anything dirty at home?":
            pc "Do you do anything dirty at home?"
            
            if ch_naked == 0:
                show christine think at center with dissolve
            elif ch_naked == 1:
                show christine think n at center with dissolve
            
            ch "Sometimes, I have to finger my mum when she’s in heat."
            
            if ch_naked == 0:
                show christine neutral at center with dissolve
            elif ch_naked == 1:
                show christine neutral n at center with dissolve
            
            ch "She usually ends up squirting as I get to her g-spot."
            
            ch "I’m very close with my mum as she brought me up on her own."
            
    if ch_naked == 0:
        show christine think at center with dissolve
    elif ch_naked == 1:
        show christine think n at center with dissolve
    
    ch "What brought you to this strip club [christine_name]? I haven’t seen you here before."
    
    $ christine_from = renpy.input("Enter where you're from.")
    $ christine_from = christine_from.strip()
    if christine_from == "":
        $ christine_from = "Nowhere"
        
    $ renpy.block_rollback()
    
    pcy "I'm from [christine_from], I moved here only recently."
        
    play audio "audio/remember.flac" 
    n "Christine will remember that."
    
    if ch_naked == 0:
        show christine think at center with dissolve
    elif ch_naked == 1:
        show christine think n at center with dissolve
    
    ch "Hmm, I’ve never heard of [christine_from] before."
    
    if ch_naked == 0:
        show christine giggle at center with dissolve
    elif ch_naked == 1:
        show christine giggle n at center with dissolve
    
    ch "Maybe you could take me there and fuck me one day."
    
    if ch_naked == 0:
        show christine angry at center with dissolve
    elif ch_naked == 1:
        show christine angry n at center with dissolve
    
    ch "Hmph. I think my mum has finished working."
    
    ch "I have to head home now."
    
    if ch_naked == 0:
        show christine lust at center with dissolve
    elif ch_naked == 1:
        show christine lust n at center with dissolve
    
    ch "Here’s a picture of me so you don’t forget how sexy I am."
    
    jump christine_succeed_date
return

# Christine second date.

label date_christine_2_pc:

    n "Hold up! You need to purchase the full game to see Christine's tiny teen pussy: https://windowslogic.itch.io/town-girls"
    
    jump main_hub_screen
return

# christine fail date.

label christine_fail_date:

    stop music
        
    $ renpy.block_rollback()
        
    if christine == 2:
        show christine angry hn at center with dissolve
        
        $ s_fingered = 0
            
        #$ a_item_condom = 0
        #$ a_item_egg = 0
        #$ a_item_bark = 0
        #$ a_item_sap = 0
        #if a_item_glass == 0:
        #    $ a_items = 0
        #else:
        #    $ a_items = 1
    elif christine == 3:
        show christine angry cw uw at center with dissolve
        
    elif christine == 1:
            
        show christine angry at center with dissolve
        
        $ dating -= 1
        $ crystal -= 1
            
        #$ s_item_leaflet = 0
        #$ s_item_stand = 0
        #$ s_items = 0
        
    $ achievement.grant("fail")
        
    ch "Hmph. I don't want sex with you anymore, you've annoyed me."
        
    play audio "audio/date_fail.flac"
    n "Date failed..."
        
    if time == 3:
        $ time -= 2
    else:
        $ time += 1
        
    jump main_hub_screen
return

# christine succeed dates.

label christine_succeed_date:

    if christine == 1:
    
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Christine. You can now look at this picture in the Gallery."
    
        $ achievement.grant("christine_1_success")
    
        call screen christine_pic_1 with dissolve
    
        screen christine_pic_1:
        
            imagebutton idle "christine_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("ch_variable_update")
        return
    elif christine == 2:
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Christine. You can now look at this picture in the Gallery."
    
        $ achievement.grant("christine_2_success")
    
        call screen christine_pic_2 with dissolve
    
        screen christine_pic_2:
        
            imagebutton idle "christine_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("ch_variable_update")
    elif christine == 3:
        play music "audio/christine_theme_date_3.flac" fadein 3.0

        if gender == 0:
            if s_wherefucked == 0:
                scene s_sex_scene_finished0
                with flash
            elif s_wherefucked == 1:
                scene s_sex_scene_finished1
                with flash
            else:
                scene s_sex_scene_finished2
                with flash
        if gender == 1:
            scene s_sex_scene_finishedg
            with flash
            
        s "So... Warm... So... Lovely..."
        
        if gender == 0:
            
            if s_wherefucked == 0:
                s "Hey! Did you cum in me!?"
                
                s "I hope I'm not preg-"
                
                scene christine_ending_cum
                with dissolve
                
                n "christine passes out after cumming inside her."
                
            else:
                s "You came so much..."
                
                scene christine_ending_cum
                with dissolve
                
                n "After christine passes out, you fuck her until you cum in her pussy for good measure."
                
        elif gender == 1:
            s "You're one wet and wild girl..."
            
            scene christine_ending_wet
            with dissolve
            
            n "christine passes out after you squirt all over her."
        
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.flac"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
            
        scene blank
        with irisout
            
        $ renpy.movie_cutscene("video/ya_got_christine.webm")
        
        $ achievement.grant("christine_3_success")
    
        jump ch_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label ch_variable_update:
    
        $ dating += 1
        $ christine += 1
        if balls == 3:
            $ balls += 0
        else:
            $ balls += 1
            
        if ovaries == 3:
            $ ovaries += 0
        else:
            $ ovaries += 1
        if time == 3:
            $ time -= 2
        else:
            $ time += 1
        jump main_hub_screen
    return

return