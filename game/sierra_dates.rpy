# Sierra's opening scene.

label date_sierra_opening:

    $ tooltip = Tooltip("")
    
    $ _game_menu_screen = None
    $ quick_menu = False
    hide screen bodystats
    hide screen dates
    hide screen dates_dark
    
    call loading from _call_loading_4
    
    stop music fadeout 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    play music "audio/opening.flac" loop fadein 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    
    if sierra == 1:
        scene sierra_start
        with dissolve
    
        n "When visiting the local art museum, you see a girl obsessing over the art, looking at the details and imperfections, you decide to search her up online."
        
        scene sierra_base_site
        with irisout
    else:
        scene sierra_base_site
        with irisout
    
    label posts_sp1:
    
        call screen date_sierra_opening_objects_ap1 with dissolve

        screen date_sierra_opening_objects_ap1:
        
            if sierra == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_sierra_timecheck")
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
            
            imagebutton auto "s_150416_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "s_100516_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s2")
                
            imagebutton auto "s_160716_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s1")
                
            imagebutton auto "s_090916_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s3")
                
            imagebutton auto "s_051116_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s4")
                
            imagebutton auto "up_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.87
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll up.") ]
                action Jump("posts_sp2")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label posts_sp2:
    
        call screen date_sierra_opening_objects_sp2 with dissolve

        screen date_sierra_opening_objects_sp2:
        
            if sierra == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_sierra_timecheck")
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
            
            imagebutton auto "s_151216_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s5")
                
            imagebutton auto "s_140117_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s6")
                
            imagebutton auto "s_240317_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s7")
                
            imagebutton auto "s_300517_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s8")
                
            imagebutton auto "s_050717_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s9")
                
            imagebutton auto "up_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.87
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll up.") ]
                action Jump("posts_sp3")
                
            imagebutton auto "down_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.95
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll down.") ]
                action Jump("posts_sp1")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label posts_sp3:
    
        call screen date_sierra_opening_objects_ap3 with dissolve

        screen date_sierra_opening_objects_ap3:
        
            if sierra == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_sierra_timecheck")
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
            
            imagebutton auto "s_140818_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s10")
                
            imagebutton auto "s_101218_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s11")
                
            imagebutton auto "s_311019_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s12")
                
            imagebutton auto "s_050120_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s13")
                
            imagebutton auto "s_100821_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_s11")
                
            imagebutton auto "down_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.95
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll down.") ]
                action Jump("posts_sp2")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label online_pic_s1:
    
        call screen online_pic_s1 with dissolve
        
        screen online_pic_s1:
        
            imagebutton idle "s_start_0":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_s2:
    
        call screen online_pic_s2 with dissolve
        
        screen online_pic_s2:
        
            imagebutton idle "s_start_1":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_s3:
    
        call screen online_pic_s3 with dissolve
        
        screen online_pic_s3:
        
            imagebutton idle "s_start_2":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp1")
            
        return
    return
    
    label online_pic_s4:
    
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
    
    label online_pic_s5:
    
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
    
    label online_pic_s6:
    
        call screen online_pic_s6 with dissolve
        
        screen online_pic_s6:
        
            imagebutton idle "s_start_5":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp2")
            
        return
    return
    
    label online_pic_s7:
    
        call screen online_pic_s7 with dissolve
        
        screen online_pic_s7:
        
            imagebutton idle "s_start_6":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp2")
            
        return
    return
    
    label online_pic_s8:
    
        call screen online_pic_s8 with dissolve
        
        screen online_pic_s8:
        
            imagebutton idle "s_start_7":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp2")
            
        return
    return
    
    label online_pic_s9:
    
        call screen online_pic_s9 with dissolve
        
        screen online_pic_s9:
        
            imagebutton idle "s_start_8":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp2")
            
        return
    return
    
    label online_pic_s10:
    
        call screen online_pic_s10 with dissolve
        
        screen online_pic_s10:
        
            imagebutton idle "s_start_9":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp3")
            
        return
    return
    
    label online_pic_s11:
    
        call screen online_pic_s11 with dissolve
        
        screen online_pic_s11:
        
            imagebutton idle "s_start_10":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp3")
            
        return
    return
    
    label online_pic_s12:
    
        call screen online_pic_s12 with dissolve
        
        screen online_pic_s12:
        
            imagebutton idle "s_start_11":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp3")
            
        return
    return
    
    label online_pic_s13:
    
        call screen online_pic_s13 with dissolve
        
        screen online_pic_s13:
        
            imagebutton idle "s_start_12":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_sp3")
            
        return
    return
return

# Check time of game to determine if dates are possible.

label date_sierra_timecheck:

    hide screen bodystats
    hide screen dates
    hide screen dates_dark

    $ loading = renpy.random.randint(1, 3)
    
    call loading from _call_loading_5
    
    $ _game_menu_screen = None
    $ quick_menu = False
    
    $ renpy.pause(3.0, hard=True)

    if time == 1:
        if sierra == 1:
            jump date_sierra_1_pc
        elif sierra == 2:
            jump date_sierra_timechecked_masturbating
        else:
            jump date_sierra_sex_letter
    elif time == 2:
        if sierra == 1:
            jump date_sierra_1_pc
        elif sierra == 2:
            jump date_sierra_2_pc
        else:
            jump date_sierra_timechecked_masturbating
    else:
        if sierra == 1:
            jump date_sierra_timechecked_asleep
        elif sierra == 2:
            jump date_sierra_timechecked_asleep
        else:
            jump date_sierra_timechecked_asleep
return

label date_sierra_timechecked_masturbating:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/sierra_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_blur
    with dissolve
    
    n "Sierra doesn't want to see you right now, do you want to advance time?"
        
    menu:
        "Go to sleep.":
        
            n "You sleep for a few hours."
            
            $ time += 1
            $ bladder = 2
                
            jump main_hub_screen
                
        "Go to Sierra's flat.":
                
            n "You go to Sierra's flat to stalk her."
                
            $ nightstalk = renpy.random.randint(1, 5)
                
            if nightstalk == 1:
                
                n "You find Sierra sitting at her desk facing the window, squirting into a bottle."
                
                scene s_masturbate_bottle
                with pixellate
            elif nightstalk == 2:
            
                n "You find Sierra sitting at her desk facing the window, just finished with squirt on her desk."
                
                scene s_masturbate_desk
                with pixellate
            elif nightstalk == 3:
            
                n "You find Sierra sitting at her desk facing the window, just finished with her pussy dripping."
            
                scene s_masturbate_finished
                with pixellate
            elif nightstalk == 4:
            
                n "You find Sierra sitting at her desk facing the window, just finished squirt on her tablet."
            
                scene s_masturbate_tablet
                with pixellate
            else:
                
                n "You find Sierra sitting at her desk facing the window, just about to squirt."
                
                scene s_masturbate_starting
                with pixellate
                
            pause 120.0
                
            $ time += 1
            $ bladder = 2
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

label date_sierra_timechecked_asleep:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/sierra_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_night_blur
    with dissolve

    n "Sierra is currently sleeping, do you want to advance time?"
        
    menu:
        "Go to sleep.":
            
            n "You sleep until it's morning."
                
            $ time = 1
                
            jump main_hub_screen
                
        "Go to Sierra's flat and watch her sleep until morning.":
                
            n "You go to Sierra's flat with a ladder. Her bedroom window is open so you position the ladder and climb up."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                
                n "You find Sierra sleeping with a pen in her vagina."
                
                scene s_sleeping_pen
                with pixellate
            elif nightstalk == 2:
            
                n "You find Sierra sleeping in the middle of squirting on her bed."
            
                scene s_sleeping_squirt
                with pixellate
            elif nightstalk == 3:
            
                n "You find Sierra sleeping in the middle of squirting on her bed with a wet pen in her vagina."
            
                scene s_sleeping_squirt_pen
                with pixellate
            else:
                
                n "You find Sierra sleeping with a wet pen in her vagina."
                
                scene s_sleeping_wet_pen
                with pixellate
            
            pause 120.0
                
            $ time = 1
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

# Sierra first date.

label date_sierra_1_pc:

    $ achievement.grant("first")
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene s_museum_pc
    with irisout
    
    show screen bodystats
    
    play music "audio/town.flac" loop fadein 3.0
    
    n "After a month of stalking the Red Fox, you know where she hangs out, so go to meet her."
    
    n "You happen to see the Red Fox walking just outside the town museum. Do you approach?"
    
    label s1_jump_from_collect:
    
    scene s_museum_pc
    with dissolve
    
    call screen date_sierra_1_objects with dissolve

    screen date_sierra_1_objects:
        
        imagebutton auto "sierra_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.81
                ypos 0.42
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Red Fox: I wonder what I should draw when I get home.") ]
                action Jump("date_sierra_1")
                
        if s_item_leaflet == 0:
            imagebutton auto "s_museum_flyer_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.35
                    ypos 0.80
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Looks like a leaflet from the museum.") ]
                    action Jump("s_collect_item_1")
        else:
            imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
        
        if s_item_stand == 0:
            imagebutton auto "s_museum_board_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.60
                    ypos 0.56
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The museum board, looks like they have a nude figure painting session on today.") ]
                    action Jump("s_collect_item_2")
        else:
            imagebutton idle "debug.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.67
        
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
    
    return
    return
    
    label s_collect_item_1:
    
        if s_item_leaflet == 1:
        
            scene s_museum
            with dissolve
        
            n "You search around the front of the museum again and find nothing."
        else:
        
            scene s_museum_pc_blur
            with dissolve
        
            show s_leaflet at center with dissolve
        
            n "You pick up the leaflet off the floor."
            $ s_item_leaflet += 1
            $ s_items += 1
        
            hide s_leaflet at center with dissolve
        
        jump s1_jump_from_collect
    return
    
    label s_collect_item_2:
    
        if s_item_stand == 1:
        
            scene s_museum_pc
            with dissolve
        
            n "You search around the front of the museum again and find nothing."
        else:
        
            scene s_museum_pc_blur
            with dissolve
        
            show s_board at center with dissolve
        
            n "You steal the museum notice board."
            $ s_item_stand += 1
            $ s_items += 1
        
            hide s_board at center with dissolve
        
        jump s1_jump_from_collect
    return
return

label date_sierra_1:

    scene s_museum_pc
    with dissolve
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/sierra_theme_date_1.flac" loop fadein 3.0
    
    pause 3.0
    
    show sierra neutral at center with dissolve
    
    s "Sup?"
    
    menu:
        "Not much, just hanging around.":
            ps "Not much, just hanging around."
            
            s "Ah, I was just heading to meet some friends to hang out."
        
        "It looks like you're wearing nothing under that hoodie.":
            ps "It looks like you're wearing nothing under that hoodie."
            
            show sierra embarrassed at center with dissolve
            
            s "Shush dude, I'm wearing something under it. Like I would go around with nothing on like that."
            
    $ renpy.block_rollback()
    
    s "My name's Sierra, what’s yours?"
    
    $ sierra_name = renpy.input("Enter a name you want sierra to remember.")
    $ sierra_name = sierra_name.strip()
    if sierra_name == "":
        $ sierra_name = "Person"
    
    $ renpy.block_rollback()
    
    play audio "audio/remember.flac"
    n "Sierra will remember that."
    
    show sierra giggle at center with dissolve
    
    s "[sierra_name] is a pretty awesome name."
    
    show sierra neutral at center with dissolve
    
    ps "I'm [age], what about you?"
    
    show sierra giggle at center with dissolve
    
    s "I’m only 25 so still pretty young."
    
    s "I’ve been to into art since I was 13, I started drawing at that age too, got banned several times from ClopPad since I was drawing porn when I was underage."
    
    show sierra smug at center with dissolve
    
    s "You can follow me on my new account, gla55drawz_BK if you want to see my art."
    
    menu:
        "What's ClopPad?":
            ps "What's ClopPad?"
            
            show sierra neutral at center with dissolve
            
            s "Oh, it's just the social media all animals in this town use. They banned me three times already for posting pornographic art when I was younger."
            
            ps "Cool, I’ll add you as soon as possible."
            
        "Oh cool, I'll follow you.":
            ps "Oh cool, I'll follow you."
            
            show sierra smug at center with dissolve
            
            s "Thanks, I'm sure you'll like the art I've posted."
            
    $ renpy.block_rollback()
    
    show sierra neutral at center with dissolve
    
    s "I like all forms of art, but I mostly like drawing animals in the nude."
    
    show sierra giggle at center with dissolve
    
    s "What type of art do you like [sierra_name]?"
    
    menu:
        "I like art of humans.":
            ps "I like art of humans."
            
            show sierra giggle at center with dissolve
            
            s "How taboo of you, that’s quite risky as well given the law."
            
            s "I’m actually surprised you haven’t got caught yet."
            
            #$ achievement.grant("bookworm")
        
        "I like art of other animals.":
            ps "I like art of other animals."
            
            show sierra smug at center with dissolve
            
            s "You would like what I draw then considering I mostly draw animals."
            
            #$ achievement.grant("lewd")
            
        "I quite like scenery art.":
            ps "I quite like scenery art."
            
            show sierra neutral at center with dissolve
            
            s "Is that it? I don’t think you’d like what I draw."
            
        "I only like human porn.":
            ps "I only like human porn."
            
            show sierra laugh at center with dissolve
            
            s "How haven’t you got caught yet considering that’s a capital offense which can land you life in prison."
            
            s "You being a bad boy is kinda hot."
            
        "I only like animal porn.":
            ps "I only like animal porn."
            
            show sierra smug at center with dissolve
            
            s "That’s pretty normal, most people your age love jerking off to it."
            
    $ renpy.block_rollback()
    
    show sierra smug at center with dissolve
    
    s "I’ve drawn so much since I started, I probably have a decent chunk of my hard drive dedicated to just my pornographic art."
    
    s "I also do commissions if you’re interested, they’re reasonably priced."
    
    menu:
        "Ever masturbated over the things you draw?":
            ps "Ever masturbated over the things you draw?"
            
            show sierra embarrassed at center with dissolve
            
            s "Sometimes I do, but that’s only if I’m really horny at the time."
            
            #$ achievement.grant("hole")
            
        "What’s the kinkiest thing you’ve drawn?":
            ps "What’s the kinkiest thing you’ve drawn?"
            
            show sierra laugh at center with dissolve
            
            s "Oh, that would have to be paw fetish art."
            
            s "People online can’t get enough of the stuff."
            
            s "Hence why it’s one of the only things that makes me money."
            
            #$ achievement.grant("bussy")
            
        "Take off your clothes.":
            ps "Take off your clothes."
            
            show sierra embarrassed at center with dissolve
            
            s "Yeah right, you wish. I could probably draw it for you though."
            
            #$ achievement.grant("tabbykink")
            
    show sierra neutral at center with dissolve
    
    $ renpy.block_rollback()
    
    menu:
        "Do you have any secrets you would share with me?":
            ps "Do you have any secrets you would share with me?"
            
            show sierra giggle at center with dissolve
            
            s "Unlikely, unless they were small ones which I wouldn’t really care about sharing."
            
            s "I can tell you one though."
            
            s "My breasts embarrass me, so it’s unlikely you’ll ever see me without a bra on."
            
            #$ achievement.grant("lewd")
            
        "Got any kinks you wanna share?":
            ps "Got any kinks you wanna share?"
            
            show sierra angry at center with dissolve
            
            s "Dude, this is way too early to be sharing kinks with you."
            
            s "Wait until we know each other more."
            
            jump sierra_fail_date
            
            #$ achievement.grant("lewd")
        "What dirty stuff do you like doing?":
            ps "What dirty stuff do you like doing?"
            
            show sierra embarrassed at center with dissolve
        
            s "I just draw porn and masturbate to it or stuff online."
            
            s "That’s really it."
            
            s "I wish I could tell you more, but we barely know each other."
            
    $ renpy.block_rollback()
    
    show sierra neutral at center with dissolve
            
    s "Where are you from, [sierra_name]? I haven’t seen you around before."
    
    $ sierra_from = renpy.input("Enter where you're from.")
    $ sierra_from = sierra_from.strip()
    if sierra_from == "":
        $ sierra_from = "Nowhere"
        
    $ renpy.block_rollback()
        
    play audio "audio/remember.flac" 
    n "Sierra will remember that."
    
    show sierra giggle at center with dissolve
    
    s "Interesting, I’ve never heard of [sierra_from] before."
    
    s "If we become close, maybe you could take me there."
    
    show sierra happy at center with dissolve
    
    s "I hope we can see each other more, you’re an okay person to talk to."
    
    s "Here’s a pic so you can remember me."
    
    s "Don’t jerk off to it, pervert."
    
    $ renpy.block_rollback()
    
    jump sierra_succeed_date
return

# Sierra second date.

label date_sierra_2_pc:
    n "Hold up! You need to purchase the full game to see Sierra's massive vulva: https://windowslogic.itch.io/town-girls"
    
    jump main_hub_screen
return

# sierra fail date.

label sierra_fail_date:

    stop music
        
    $ renpy.block_rollback()
        
    if sierra == 2:
        show sierra angry hn at center with dissolve
        
        $ s_fingered = 0
            
        #$ a_item_condom = 0
        #$ a_item_egg = 0
        #$ a_item_bark = 0
        #$ a_item_sap = 0
        #if a_item_glass == 0:
        #    $ a_items = 0
        #else:
        #    $ a_items = 1
    elif sierra == 3:
        show sierra angry cw uw at center with dissolve
        
    elif sierra == 1:
        show sierra angry at center with dissolve
            
        $ s_item_leaflet = 0
        $ s_item_stand = 0
        $ s_items = 0
        
    $ achievement.grant("fail")
        
    s "Bruh. What even was that [sierra_name]? That was your idea of a date?"
        
    play audio "audio/date_fail.flac"
    n "Date failed..."
        
    if time == 3:
        $ time -= 2
    else:
        $ time += 1
        
    jump main_hub_screen
return

# sierra succeed dates.

label sierra_succeed_date:

    if sierra == 1:
    
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Sierra. You can now look at this picture in the Gallery."
    
        $ achievement.grant("sierra_1_success")
    
        call screen sierra_pic_1 with dissolve
    
        screen sierra_pic_1:
        
            imagebutton idle "sierra_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("s_variable_update")
        return
    elif sierra == 2:
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
        stop music fadeout 3.0
    
        pause 3.0
        
        n "You got a picture of Sierra. You can now look at this picture in the Gallery."
    
        $ achievement.grant("sierra_2_success")
    
        call screen sierra_pic_2 with dissolve
    
        screen sierra_pic_2:
        
            imagebutton idle "sierra_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("s_variable_update")
    elif sierra == 3:
        play music "audio/sierra_theme_date_3.flac" fadein 3.0

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
                
                scene sierra_ending_cum
                with dissolve
                
                n "Sierra passes out after cumming inside her."
                
            else:
                s "You came so much..."
                
                scene sierra_ending_cum
                with dissolve
                
                n "After Sierra passes out, you fuck her until you cum in her pussy for good measure."
                
        elif gender == 1:
            s "You're one wet and wild girl..."
            
            scene sierra_ending_wet
            with dissolve
            
            n "Sierra passes out after you squirt all over her."
        
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.flac"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
            
        scene blank
        with irisout
            
        $ renpy.movie_cutscene("video/ya_got_sierra.webm")
        
        $ achievement.grant("sierra_3_success")
    
        jump s_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label s_variable_update:
    
        $ dating += 1
        $ sierra += 1
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