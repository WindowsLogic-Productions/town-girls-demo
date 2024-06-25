# Crystal's opening scene.

label date_crystal_opening:

    $ tooltip = Tooltip("")
    
    $ _game_menu_screen = None
    $ quick_menu = False
    hide screen bodystats
    hide screen dates
    hide screen dates_dark
    
    call loading from _call_loading_6
    
    stop music fadeout 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    play music "audio/opening.flac" loop fadein 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    
    if crystal == 1:
        scene crystal_start
        with dissolve
    
        n "While walking around town, you notice an older sheep using a public telephone box, you decide to search her up online."
        
        scene crystal_base_site
        with irisout
    else:
        scene crystal_base_site
        with irisout
    
    label posts_crp1:
    
        call screen date_crystal_opening_objects_ap1 with dissolve

        screen date_crystal_opening_objects_ap1:
        
            if crystal == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_crystal_timecheck")
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
            
            imagebutton auto "cr_120915_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "cr_040816_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s2")
                
            imagebutton auto "cr_080518_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "cr_050620_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s3")
                
            imagebutton auto "cr_060521_%s":
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
    
    label online_pic_cr1:
    
        call screen online_pic_cr1 with dissolve
        
        screen online_pic_cr1:
        
            imagebutton idle "s_start_0":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_crp1")
            
        return
    return
    
    label online_pic_cr2:
    
        call screen online_pic_cr2 with dissolve
        
        screen online_pic_cr2:
        
            imagebutton idle "s_start_1":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_crp1")
            
        return
    return
    
    label online_pic_cr3:
    
        call screen online_pic_cr3 with dissolve
        
        screen online_pic_cr3:
        
            imagebutton idle "s_start_2":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_cr4:
    
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
    
    label online_pic_cr5:
    
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

label date_crystal_timecheck:

    hide screen bodystats
    hide screen dates
    hide screen dates_dark

    $ loading = renpy.random.randint(1, 3)
    
    call loading from _call_loading_7
    
    $ _game_menu_screen = None
    $ quick_menu = False
    
    $ renpy.pause(3.0, hard=True)

    if time == 1:
        if crystal == 1:
            jump date_crystal_timechecked_porn
        elif crystal == 2:
            jump date_crystal_timechecked_porn
        else:
            jump date_crystal_sex_letter
    elif time == 2:
        if crystal == 1:
            jump date_crystal_timechecked_porn
        elif crystal == 2:
            jump date_crystal_2_pc
        else:
            jump date_crystal_timechecked_working
    else:
        if crystal == 1:
            jump date_crystal_1_pc
        elif crystal == 2:
            jump date_crystal_timechecked_working
        else:
            jump date_crystal_timechecked_working
return

label date_crystal_timechecked_working:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/crystal_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_blur
    with dissolve
    
    n "Crystal is busy working at the strip club, do you want to advance time?"
        
    menu:
        "Go to sleep.":
        
            n "You sleep until morning."
            
            $ time = 1
            $ bladder = 2
                
            jump main_hub_screen
                
        "Go to Crystal's workplace.":
                
            n "You go to strip club to stalk her."
                
            $ nightstalk = renpy.random.randint(1, 5)
                
            if nightstalk == 1:
                
                n "You find Crystal pole dancing naked."
                
                scene blank
                with pixellate
            elif nightstalk == 2:
            
                n "You find Crystal pole dancing clothed, with money sticking out of her outfit."
                
                scene blank
                with pixellate
            elif nightstalk == 3:
            
                n "You find Crystal pole dancing naked, with money sticking out of her wet pussy."
            
                scene blank
                with pixellate
            elif nightstalk == 4:
            
                n "You find Crystal pole dancing naked, with cum dripping out of her pussy."
            
                scene blank
                with pixellate
            else:
                
                n "You find Crystal pole dancing naked, covered in cum."
                
                scene blank
                with pixellate
                
            pause 120.0
                
            $ time += 1
            $ bladder = 2
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

label date_crystal_timechecked_porn:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/crystal_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_night_blur
    with dissolve

    n "Crystal is currently doing a porn shoot, do you want to advance time?"
        
    menu:
        "Go to sleep.":
            
            n "You sleep for a few hours."
                
            $ time += 1
                
            jump main_hub_screen
                
        "Go to Crystal's flat and watch her.":
                
            n "You go to Crystal's house with a ladder. You position the ladder and climb up and get a clear view of what's happening inside."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                
                n "You find Crystal with three random guys, pointing their hard dicks at her."
                
                scene blank
                with pixellate
            elif nightstalk == 2:
            
                n "You find Crystal with three random guys, cumming all over her."
            
                scene blank
                with pixellate
            elif nightstalk == 3:
            
                n "You find Crystal with three random guys, with cum inside her vagina."
            
                scene blank
                with pixellate
            else:
                
                n "You find Crystal with three random guys, and she's squirting on the bed."
                
                scene blank
                with pixellate
            
            pause 120.0
                
            $ time = 1
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

# crystal first date.

label date_crystal_1_pc:

    $ achievement.grant("first")
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene cr_stripclub_pc
    with irisout
    
    show screen bodystats
    
    play music "audio/strippin.flac" loop fadein 3.0
    
    n "It’s late and you’re extremely horny, so you head to the local strip club to get some much needed ''you'' time."
    
    n "Once you arrive you notice all the strippers are sheep, you think this is your opportunity to shag some sheep."
    
    label cr1_jump_from_collect:
    
    scene cr_stripclub_pc
    with dissolve
    
    call screen date_crystal_1_objects with dissolve

    screen date_crystal_1_objects:
        
        imagebutton auto "crystal_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.81
                ypos 0.58
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Sheep: Wanna fuck hun? I can give you a good time for a reasonable price.") ]
                action Jump("date_crystal_1")
                
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
    
    # label cr_collect_item_1:
    
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
    
    # label cr_collect_item_2:
    
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

label date_crystal_1:

    scene cr_stripclub_pc
    with dissolve
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/crystal_theme_date_1.flac" loop fadein 3.0
    
    pause 3.0
    
    $ balls == 1
    $ ovaries == 1
    
    if gender == 0:
        show crystal laugh at center with dissolve
    elif gender == 1:
        show crystal laugh g at center with dissolve
    
    cr "My my, you came quickly darling."
    
    if gender == 0:
        show crystal giggle at center with dissolve
    elif gender == 1:
        show crystal giggle g at center with dissolve
    
    cr "I was expecting you to last a little longer so mummy could have some more fun with you."
    
    if gender == 0:
        show crystal snarky at center with dissolve
        cr "I forgot to ask, what was your name? Is it as cute as your dick?"
    elif gender == 1:
        show crystal snarky g at center with dissolve
        cr "I forgot to ask, what was your name? Is it as cute as your pussy?"
        
    $ crystal_name = renpy.input("Enter a name you want crystal to remember.")
    $ crystal_name = crystal_name.strip()
    if crystal_name == "":
        $ crystal_name = "Person"
        
    $ renpy.block_rollback()
        
    play audio "audio/remember.flac"
    n "Crystal will remember that."
    
    pcy "I’m [age], what about you?"
    
    if gender == 0:
        show crystal giggle at center with dissolve
    elif gender == 1:
        show crystal giggle g at center with dissolve
    
    cr "I’m quite old at 40, but I still know how to give cuties like you a good time."
    
    if gender == 0:
        show crystal snarky at center with dissolve
    elif gender == 1:
        show crystal snarky g at center with dissolve
    
    cr "I’ve worked at this strip club since I was 18, and I also do porn shoots on the side if you ever want to join in on them."
    
    cr "I have a ClopPad account if you want to follow it, according to my daughter, it’s apparently all the rage at the moment."
    
    cr "Her friends also use it according to her as well."
    
    menu:
        "What's ClopPad?":
            pcy "What's ClopPad?"
            
            if gender == 0:
                show crystal laugh at center with dissolve
            elif gender == 1:
                show crystal laugh g at center with dissolve
            
            cr "I wish I could tell you exactly what it is, but I don’t know much about it."
        
        "Oh cool, I'll follow you.":
            pcy "Oh cool, I'll follow you."
            
            if gender == 0:
                show crystal snarky at center with dissolve
            elif gender == 1:
                show crystal snarky g at center with dissolve
            
            cr "I don’t really use it too much, just bear that in mind."
            
    if gender == 0:
        show crystal snarky at center with dissolve
    elif gender == 1:
        show crystal snarky g at center with dissolve
    
    cr "I’ve had too many sexual partners to count, being a stripper and all."
    
    if gender == 0:
        show crystal laugh at center with dissolve
    elif gender == 1:
        show crystal laugh g at center with dissolve
    
    cr "I kinda just want to find someone to settle down with now that I’m older, and continue with my profession of course."
    
    if gender == 0:
        show crystal giggle at center with dissolve
    elif gender == 1:
        show crystal giggle g at center with dissolve
    
    cr "Maybe I could arrange a place and time we can get saucy together in private, darling?"
    
    menu:
        "Yeah, sure.":
            pcy "Yeah, sure."
            
            if gender == 0:
                show crystal laugh at center with dissolve
            elif gender == 1:
                show crystal laugh g at center with dissolve
            
            cr "Okay, mummy will get that arranged for you."
            
            cr "We can use my special room back at my place."
        
        "No thanks, you’ve given me enough tonight.":
            ps "No thanks, you’ve given me enough tonight."
            
            if gender == 0:
                show crystal angry at center with dissolve
            elif gender == 1:
                show crystal angry g at center with dissolve
            
            cr "That’s a shame, mummy was going to give you rewards for being a good little bitch."
            
            jump crystal_fail_date
            
    if gender == 0:
        show crystal snarky at center with dissolve
    elif gender == 1:
        show crystal snarky g at center with dissolve
            
    cr "I let people into my house for casting for porn movies."
    
    cr "We do the porn shoots in either my bedroom or the spare ''porn room''."
    
    menu:
        "How messy do these shoots get?":
            pcy "How messy do these shoots get?"
            
            cr "It depends on the type of porn we’re doing, hun."
            
            cr "For example, if we’re doing a shoot for Wet Pussy Productions, then it gets very messy with fluids ranging from piss to period blood."
            
        "What's the best shoot you've done?":
            pcy "What's the best shoot you've done?"
            
            cr "Hmm, let me think."
            
            cr "That would have to be the shoot I did a few weeks ago."
            
            if gender == 0:
                show crystal ahegao at center with dissolve
            elif gender == 1:
                show crystal ahegao g at center with dissolve
                
            cr "His cock was so big and it went so deep inside me."
            
            if gender == 0:
                show crystal giggle at center with dissolve
            elif gender == 1:
                show crystal giggle g at center with dissolve
            
            cr "It was cute how he squirmed after being tied up and forced to breed me."
            
        "Take off your clothes.":
            pcy "Take off your clothes."
            
            cr "Feisty, are we my dear?"
            
            if gender == 0:
                show crystal laugh at center with dissolve
            elif gender == 1:
                show crystal laugh g at center with dissolve
            
            cr "You gotta earn that sort of attention, hun."
            
            if gender == 0:
                show crystal snarky at center with dissolve
            elif gender == 1:
                show crystal snarky g at center with dissolve
            
            cr "If you pay up, I could possibly do that and more."
            
    menu:
        "Why do I have to pay for you to do more?":
            pcy "Why do I have to pay for you to do more?"
            
            if gender == 0:
                show crystal angry at center with dissolve
            elif gender == 1:
                show crystal angry g at center with dissolve
            
            cr "Truthfully, it’s because the boss here doesn’t pay me enough for my time, darling."
            
            cr "I’ve worked here for so long; I should’ve gotten a raise several years ago."
            
        "What are your kinks?":
            pcy "What are your kinks?"
            
            if gender == 0:
                show crystal snarky at center with dissolve
            elif gender == 1:
                show crystal snarky g at center with dissolve
            
            cr "I have many kinks, but I would have to say the one I like most is MDLB."
            
            cr "I love when I can dominate someone younger than me the most."
            
        "What dirty stuff do you do here?":
            pcy "What dirty stuff do you do here?"
            
            if gender == 0:
                show crystal snarky at center with dissolve
            elif gender == 1:
                show crystal snarky g at center with dissolve
            
            cr "I can strip for you, rub my undercarriage in your face, fuck you silly or even piss and/or shit on you for reasonable prices."
            
            cr "Granted, some of those aren't what I like."
            
            if gender == 0:
                show crystal giggle at center with dissolve
            elif gender == 1:
                show crystal giggle g at center with dissolve
            
            cr "I have to please paying customers if they ask me to do something, hun."
            
    cr "So, what brings you here [crystal_name]? I haven’t seen you here before."
    
    $ crystal_from = renpy.input("Enter where you're from.")
    $ crystal_from = crystal_from.strip()
    if crystal_from == "":
        $ crystal_from = "Nowhere"
        
    $ renpy.block_rollback()
    
    pcy "I'm from [crystal_from], I moved here only recently."
        
    play audio "audio/remember.flac" 
    n "Crystal will remember that."
    
    if gender == 0:
        show crystal giggle at center with dissolve
    elif gender == 1:
        show crystal giggle g at center with dissolve
    
    cr "Huh, I don’t think I’ve been to [crystal_from] in my life, hun."
    
    cr "I'm sure if you like my company and you're willing to keep paying up."
    
    cr "We could go to your home town together."
    
    if gender == 0:
        show crystal laugh at center with dissolve
    elif gender == 1:
        show crystal laugh g at center with dissolve
    
    cr "Think of it as a paid girlfriend experience from yours truly."
    
    if gender == 0:
        show crystal snarky at center with dissolve
    elif gender == 1:
        show crystal snarky g at center with dissolve
    
    cr "Anyway, you better clean yourself up, I have to be ready in the back for another horny guy in ten minutes."
    
    cr "I hope to see you again, and don’t forget about our little agreement."
    
    if gender == 0:
        show crystal laugh at center with dissolve
    elif gender == 1:
        show crystal laugh g at center with dissolve
    
    cr "Thank you for letting me serve you, darling."
    
    n "Crystal slips a picture into your pocket."
    
    jump crystal_succeed_date
return

# crystal second date.

label date_crystal_2_pc:

    n "Hold up! You need to purchase the full game to see Crystal's heavily used pussy: https://windowslogic.itch.io/town-girls"
    
    jump main_hub_screen
return

# crystal fail date.

label crystal_fail_date:

    stop music
        
    $ renpy.block_rollback()
        
    if crystal == 2:
        show crystal angry hn at center with dissolve
        
        $ s_fingered = 0
            
        #$ a_item_condom = 0
        #$ a_item_egg = 0
        #$ a_item_bark = 0
        #$ a_item_sap = 0
        #if a_item_glass == 0:
        #    $ a_items = 0
        #else:
        #    $ a_items = 1
    elif crystal == 3:
        show crystal angry cw uw at center with dissolve
        
    elif crystal == 1:
    
        if gender == 0:
            show crystal angry at center with dissolve
        elif gender == 1:
            show crystal angry g at center with dissolve
            
        #$ s_item_leaflet = 0
        #$ s_item_stand = 0
        #$ s_items = 0
        
    $ achievement.grant("fail")
        
    cr "Hmm, it looks like your time with me has run out [crystal_name]. Pay up or get out."
        
    play audio "audio/date_fail.flac"
    n "Date failed..."
        
    if time == 3:
        $ time -= 2
    else:
        $ time += 1
        
    jump main_hub_screen
return

# crystal succeed dates.

label crystal_succeed_date:

    if crystal == 1:
    
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Crystal. You can now look at this picture in the Gallery."
    
        $ achievement.grant("crystal_1_success")
    
        call screen crystal_pic_1 with dissolve
    
        screen crystal_pic_1:
        
            imagebutton idle "crystal_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("cr_variable_update")
        return
    elif crystal == 2:
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of crystal. You can now look at this picture in the Gallery."
    
        $ achievement.grant("crystal_2_success")
    
        call screen crystal_pic_2 with dissolve
    
        screen crystal_pic_2:
        
            imagebutton idle "crystal_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("cr_variable_update")
    elif crystal == 3:
        play music "audio/crystal_theme_date_3.flac" fadein 3.0

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
                
                scene crystal_ending_cum
                with dissolve
                
                n "crystal passes out after cumming inside her."
                
            else:
                s "You came so much..."
                
                scene crystal_ending_cum
                with dissolve
                
                n "After crystal passes out, you fuck her until you cum in her pussy for good measure."
                
        elif gender == 1:
            s "You're one wet and wild girl..."
            
            scene crystal_ending_wet
            with dissolve
            
            n "crystal passes out after you squirt all over her."
        
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.flac"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
            
        scene blank
        with irisout
            
        $ renpy.movie_cutscene("video/ya_got_crystal.webm")
        
        $ achievement.grant("crystal_3_success")
    
        jump cr_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label cr_variable_update:
    
        $ dating += 1
        $ crystal += 1
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
        
        if crystal == 2:
            jump date_christine_timecheck
        else:
            jump main_hub_screen
    return

return