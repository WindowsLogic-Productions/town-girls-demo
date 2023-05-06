# Violet first date.

label date_violet_1_pc:

    $ achievement.grant("first")
    
    scene black
    with dissolve
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene v_house_front
    with dissolve
    
    play music "audio/nature.tgm" loop fadein 3.0
    
    n "You don't know anything about this girl you found at a music shop. But she seems nice, so you asked to talk to her at her house and she agreed."
    
    n "You arrive at the Arctic Fox's house and see her outside with her garage open."
    
    scene v_house_front_pc
    with dissolve
    
    call screen date_violet_1_objects with dissolve

    screen date_violet_1_objects:
        
        imagebutton auto "v_electric_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.334
            ypos 0.35
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("The Arctic Fox's electric guitar is so cool.") ]
            clicked [ Play("sound", "audio/e_guitar_strum.tgm") ]
            
        imagebutton auto "v_acoustic_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.366
            ypos 0.356
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("It rattles.") ]
            clicked [ Play("sound", "audio/guitar_strum.tgm") ]
            
        imagebutton auto "v_amp_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.426
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Pretty rad amp with tons of dials.") ]
            clicked [ Play("sound", "audio/amp.tgm") ]
            
        imagebutton auto "v_wires_left_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.27
            ypos 0.401
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Just a bunch of audio cables.") ]
            clicked [ Play("sound", "audio/boing.tgm") ]
            
        imagebutton auto "v_wires_right_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.46
            ypos 0.380
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Just a bunch of audio cables.") ]
            clicked [ Play("sound", "audio/boing.tgm") ]
            
        imagebutton auto "v_mini_amp_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.47
            ypos 0.41
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A miniture tube amp.") ]
            clicked [ Play("sound", "audio/amp.tgm") ]
            
        imagebutton auto "tree_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.864
            ypos 0.337
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("I'd like to be a tree.") ]
            clicked [ Play("sound", "audio/tree.tgm") ]
            
        if window_crack_v == 0:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A window of the Arctic Fox's house.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("A small crack appeared."), SetVariable("window_crack_v", 1) ]
        elif window_crack_v == 1:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("Another small crack appeared."), SetVariable("window_crack_v", 2) ]
        elif window_crack_v == 2:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Another small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("A bigger crack appeared."), SetVariable("window_crack_v", 3) ]
        elif window_crack_v == 3:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A bigger crack appeared.") ]
                clicked [ Play("sound", "audio/glass_break.tgm"), tooltip.Action("You broke the window."), SetVariable("window_crack_v", 4) ]
                
        else:
        
            imagebutton idle "v_window_cracked":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ tooltip.Action("You broke the window.") ]
                action tooltip.Action("You broke the window.")
        
        if window_crack_v == 4:
            
            imagebutton auto "violet_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Arctic Fox: You know you're paying for\nthat window right?") ]
                action Jump("date_violet_1")
        else:
            imagebutton auto "violet_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Arctic Fox: Hey there cutie.") ]
                action Jump("date_violet_1")
            
        text tooltip.value:
            xpos 0.21
            ypos 0.75
    return
return

label date_violet_1:

    if window_cracked == 1:
        $ achievement.grant("window")
    elif window_cracked == 2:
        $ achievement.grant("windowfetish")

    if window_crack_v == 4:
        scene v_house_front_crack
        with dissolve
    else:
        scene v_house_front
        with dissolve

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/violet_theme.tgm" loop fadein 3.0
    
    show violet neutral at center with dissolve
    
    v "Oh hey, it's you from the other day. Did you have a safe trip here? The name's Violet, what's yours?"
    
    $ violet_name = renpy.input("Enter a name you want Violet to remember.")
    $ violet_name = violet_name.strip()
    if violet_name == "":
        $ violet_name = "Person"
        
    $ renpy.block_rollback()
    
    play audio "audio/remember.tgm"
    n "Violet will remember that."
    
    show violet giggle at center with dissolve
    
    v "[violet_name] is a pretty cool name."
    
    pv "How old are you? I'm [age]"
    
    v "I'm 22. My birthday is in July."
    
    v "Something else you should know about me [violet_name], is that I'm the guitarist in a band called Arctic Foxes, we've released three albums so far. Give them a listen if you wish."
    
    v "The thing I hate about being in the band is that all of my band mates are boys and there's no girls to chill with."
    
    menu:
        "Ever done anything lewd over the boys in your band?":
            pv "Ever done anything lewd over the boys in your band?"
            
            show violet embarrassed at center with dissolve
            
            $ renpy.block_rollback()
            
            v "I've been caught masturbating over my band mates several times. They're just so attractive, I can't contain myself."
        
        "Who needs girls when boys can give you sex?":
            pv "Who needs girls when boys can give you sex?"
            
            show violet giggle at center with dissolve
            
            $ renpy.block_rollback()
            
            v "Boys are great and all - especially for sex, but hanging out with girls is also neat too."
            
            show violet embarrassed at center with dissolve
            
            v "With girls, you can either finger them, eat them out or shove a dildo in them while they're doing their make-up, getting their hair done or while they're getting their nails painted."
    
    show violet neutral at center with dissolve
    
    v "I also have a ClopPad if you want to follow, the username is satansqt_vi0."
    
    menu:
        "What's ClopPad?":
            pv "What's ClopPad?"
            
            $ renpy.block_rollback()
            
            show violet confused at center with dissolve
            
            v "You don't know what ClopPad is, [violet_name]? You're missing out my dude. It's a social media that let's you make friends, create and post anything you want. It's ran by a company called Peta, which protects all animal data online!"
        
        "Oh cool, I'll follow you as soon as I can.":
            pv "Oh cool, I'll follow you as soon as I can."
            
            $ renpy.block_rollback()
            
            v "Thank you [violet_name], that means a lot to me!"
    
    show violet neutral at center with dissolve
    
    v "I also work for Peta, specifically the design of the ClopPad website."
    
    menu:
        "Do you have any secrets you would share?":
            pv "Do you have any secrets you would share?"
            
            show violet think at center with dissolve
            
            $ renpy.block_rollback()
            
            v "Hmm... Let me think..."
            
            show violet embarrassed at center with dissolve
    
            v "Uh... I'm very sexually outgoing and end up doing something stupidly lewd every Valentine's day. I normally end up posting something drunken on my ClopPad profile."
        
        "What's the kinkiest thing you've ever done?":
            pv "What's the kinkiest thing you've ever done?"
            
            show violet embarrassed at center with dissolve
            
            $ renpy.block_rollback()
            
            v "We've only just met [violet_name], so this is a bit of a forward question, but since we're learning about each other, I'll tell you."
            
            v "I once put a dildo so far up my vagina that it got stuck and I had cope with it being in there for two days until it finally got unstuck. Imagine peeing with an object inside you - so embarrassing."
            
        "Take off your clothes.":
        
            $ achievement.grant("takeoff")
            
            pv "Take off your clothes."
            
            show violet giggle at center with dissolve
            
            $ renpy.block_rollback()
            
            v "[violet_name], we've literally just met, wait until we know each other more you pervert."
    
    show violet neutral at center with dissolve
    
    v "Something else to know about me is that I started practising Satanism very recently."
    
    v "What about you, [violet_name]? Where are you from? What brings you to town?"
    
    $ violet_from = renpy.input("Enter where you're from.")
    $ violet_from = violet_from.strip()
    if violet_from == "":
        $ violet_from = "Nowhere"
        
    $ renpy.block_rollback()
    
    if gender == 0:
        pv "I'm from [violet_from], I moved here after my parents got divorced and I just needed a place to live away from all the drama of that."
    elif gender == 1:
        pv "I'm from [violet_from], I moved here to attend a university in the area."
    
    play audio "audio/remember.tgm"
    n "Violet will remember that."
    
    show violet happy at center with dissolve
    
    v "Cool. I hope we can see each other more, you're really nice to talk to, [violet_name]!"
    
    jump violet_succeed_date
    return
return

# Violet second date.

label date_violet_2_pc:

    scene black
    with dissolve
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0

    scene v_abandoned_cinema
    with dissolve
    
    play music "audio/abandoned.tgm" loop fadein 3.0
    
    n "Violet visits you at your place and takes you to an abandoned cinema. The vacant venue reeks with the smell of fish."
    
    call screen date_violet_2_objects with dissolve

    screen date_violet_2_objects:
        
        imagebutton auto "violet/date_2/v_stage_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.322
            ypos 0.58
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A fancy-looking stage for theatre plays.\nThe curtains are damp with white-ish yellow\nstains and fishy smell.") ]
            clicked [ Play("sound", "audio/stage.tgm") ]
            
        imagebutton auto "violet/date_2/v_door_right_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.534
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A door leading to a fishy-smelling room.") ]
            clicked [ Play("sound", "audio/object_falling.tgm") ]
            
        imagebutton auto "violet/date_2/v_door_mright_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.628
            ypos 0.53
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A door leading to another room.") ]
            clicked [ Play("sound", "audio/objects_falling.tgm") ]
            
        imagebutton auto "violet/date_2/v_bench_back_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.926
            ypos 0.568
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Rows of seats with a suspicious yellow liquid\non them. Does Violet pee on them?!") ]
            clicked [ Play("sound", "audio/rotting_seats.tgm") ]
            
        
        imagebutton auto "violet/date_2/v_bench_front_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.681
            ypos 0.85
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Rows of seats with a suspucious yellow liquid\non them. Does Violet pee on them?!") ]
            clicked [ Play("sound", "audio/rotting_seats.tgm") ]
        
        
        imagebutton auto "violet/date_2/violet_click_cinema_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.8
            ypos 0.452
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Violet: Having fun exploring? Sorry about the\nsmell, I use this place for alone time. It's a very\nnice sense of freedom and risk.") ]
            action Jump("date_violet_2")
            
        text tooltip.value:
            xpos 0.16
            ypos 0.15
    return
return

label date_violet_2:

    stop music fadeout 3.0
    
    pause 3.0
   
    play music "audio/violet_theme_c.tgm" loop fadein 3.0
    
    scene v_abandoned_cinema
    with dissolve
    
    show violet neutral at center with dissolve
    
    v "Whew, we're finally here, [violet_name]! This is where I usually hang out, pretty cool huh?"
    
    menu:
        "Yeah, it's cool.":
            pv "Yeah, it's cool."
            
        "Ew, this place is nasty.":
            pv "Ew, this place is nasty."
            jump violet_fail_date
    
    $ renpy.block_rollback()
    
    v "You weren't expecting anything fancy from me were you, [violet_name]? I'm not like other girls who take their dates to restaurants or cinemas. I take my dates to abandoned places and show them how cool they are."
    
    menu:
        "Yeah, I was expecting a bit more.":
            pv "Yeah, I was expecting a bit more."
            jump violet_fail_date
        "No, this is what I was expecting and it's really neat.":
            pv "No, this is what I was expecting and it's really neat."
            
    $ renpy.block_rollback()
    
    v "It's nice to finally meet someone who values abandoned places as much as I do."
    
    v "So what do you want to do while we've got all the time in the world, [violet_name]? You can ask me more things if you want?"
    
    menu:
        "How did you find this place?":
            pv "How did you find this place?"
            
            $ renpy.block_rollback()
            
            v "Oh, I found this place while I was hanging out with some old friends during my teens. I visit this place alone now since all of my friends moved away when they finished college."
            
            menu:
                "What did you used to do here?":
                    pv "What did you used to do here?"
                    
                    $ renpy.block_rollback()
                    
                    show violet giggle at center with dissolve
                
                    v "We used to put on silly plays for each other here every weekend which would always end up with us either hurting ourselves or ripping our clothes and having to go home naked."
                    
                    show violet embarrassed at center with dissolve
                    
                    v "I once ripped straight through my underwear and had to walk home completely naked with my friends laughing at me and making fun of how my pussy looked and how small my breasts were."
                    
                    v "I also managed to get my first kiss taken by my best friend while doing one of the plays, her lips were so soft and inviting. We both blushed after kissing each other."
                    
                    show violet giggle at center with dissolve
                    
                    v "After that play, my best friend whispered in my ear that she wanted more, so we went to a hidden room in the back. We kissed some more, but it devolved into sex, and that's how I lost my virginity."
                    
                    v "Have you lost your virginity yet?"
                     
                    menu:
                        "Yes":
                            pv "I have."
                            
                            $ renpy.block_rollback()
                            
                            show violet think at center with dissolve
                            
                            if gender == 0:
                                v "I bet the girl loved how big your cock was, [violet_name]!"
                            elif gender == 1:
                                v "I bet the boy loved how deep your pussy was, [violet_name]!"
                            
                        "No":
                            
                            $ achievement.grant("virgin")
                            
                            pv "I haven't."
                            
                            $ renpy.block_rollback()
                            
                            show violet giggle at center with dissolve
                            
                            v "Maybe I could change that at some point, cutie."
                
                "What do you do here now?":
                    pv "What do you do here now?"
                    
                    $ renpy.block_rollback()
                    
                    v "I come here to remember the good times with friends and remember how my first relationship started."
                    
                    v "It's very peaceful here since no one knows about this place."
                    
                    show violet giggle at center with dissolve
                    
                    v "So peaceful in fact that you can literally lie on the stage, masturbate and moan as loud as possible so it echoes and no one will hear you."
                    
                    v "Speaking of masturbation, there's a room in the back where I privately masturbate and squirt on the floor. Downside is that the room smells rather fishy now." 
                
        "What do you do here on your own?":
            pv "What do you do here on your own?"
            
            $ renpy.block_rollback()
            
            show violet giggle at center with dissolve
            
            v "Anything I want, dude."
            
            v "I get naked, play my guitar, do satanic rituals, masturbate. As far as I'm concerned this place is mine since no one else cares about it."
            
            show violet embarrassed at center with dissolve
            
            v "Sometimes I get naked and play my guitar, while doing satanic rituals and masturbating. In that order."
    
    show violet neutral at center with dissolve
    
    $ renpy.block_rollback()
    
    menu:
        "Can you strip down to your underwear?":
            pv "Can you strip down to your underwear?"
            
            $ renpy.block_rollback()
            
            v "Random, but okay!"
            
            show violet underwear at center with dissolve
            
            v "It's embarrassing because I wear really cute underwear, but everyone thinks I'm this tough girl."
            
            v "Sometimes I'm really soft, but people don't see that, except now you have."
            
            v "Is there anything else you want to do with me while we're here?"
            
            menu:
                "Can I take a peak at your breasts?":
                    pv "Can I take a peak at your breasts?"
                    
                    $ renpy.block_rollback()
            
                    v "Fine. But don't tell anyone."
                    
                    show violet underwear_boob at center with dissolve
                    
                    v "If you're wondering [violet_name], they're average."
                    
                "Is there anything you haven't told me yet?":
                    pv "Is there anything you haven't told me yet?"
                    
                    $ renpy.block_rollback()
                    
                    show violet underwear_think at center with dissolve
                    
                    v "Hmm... Let me think..."
                    
                    show violet underwear at center with dissolve
                    
                    v "Okay, this one is just me being a stupid bitch."
                    
                    v "One time after my yearly Valentine's day drinking party, I woke up and found a massive piss puddle on my floor."
                    
                    v "So now every time I want to get drunk, I prepare a massive bucket to just sit on while I drink so I don't spray on the floor."
            
                "I need the toilet, where do I go?":
                    pv "I need the toilet, where do I go?"
                    
                    $ renpy.block_rollback()
            
                    v "Since this place is abandoned, I guess you can go anywhere."
                    
                    v "But if you really want to be naughty [violet_name], you can do it on me."
                    
                    menu:
                        "I'll find somewhere to go.":
                            pv "I'll find somewhere to go."
                            
                            $ renpy.block_rollback()
                            
                            v "Okay, that's fine by me [violet_name]."
            
                        "I guess I'll just do it on you.":
                            pv "I guess I'll just do it on you."
                            
                            $ renpy.block_rollback()
            
                            v "Nice, let me get undressed first."
                            
                            scene black
                            with dissolve
                    
                            v "Okay, I'm ready [violet_name]!"
                    
                            n "You... uh... what the fuck? Violet is drenched now."
                            
                            $ achievement.grant("defecation")
                            
                            jump violet_fail_date
            
        "Take off your clothes.":
        
            $ achievement.grant("takeoff")
            
            pv "Take off your clothes."
            
            $ renpy.block_rollback()
            
            show violet giggle at center with dissolve
            
            v "The most I'll let you see for now is my underwear [violet_name]."
            
            show violet underwear at center with dissolve
            
            if gender == 0:
                v "You might get your wish when we see each other next, big boy."
                
                n "Violet clenches and squeezes your crotch. You feel extremely tight in your pants."
            elif gender == 1:
                v "You might get your wish when we see each other next, sexy."
            
                n "Violet shoves her hand down your underwear and fingers you thoroughly. You feel extremely wet."
    
    show violet underwear at center with dissolve
    
    $ renpy.block_rollback()
    
    v "Hey [violet_name], I'm gonna ask you some questions to see if you've been paying attention to me."
    
    v "How old am I?"
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    call screen first_question with dissolve
    
    screen first_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("35") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("22") ]
            action Jump("first_question_correct")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("16") ]
            action Jump("question_incorrect")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
            
    label first_question_correct:
        
        show violet underwear_happy at center with dissolve
        
        v "Well done!"
        
        jump second_question
        
    return
    
    label second_question:
    
    show violet underwear at center with dissolve
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    v "What's my ClopPad username?"
    
    call screen second_question with dissolve
    
    screen second_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("V10let_F0x") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("S3xqt_vio") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("satansqt_vi0") ]
            action Jump("second_question_correct")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
        
    label second_question_correct:
        
        show violet underwear_happy at center with dissolve
        
        v "That's right!"
        
        jump third_question
        
    return
    
    return
    
    label third_question:
    
    show violet underwear at center with dissolve
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    v "Which information about me is correct?"
    
    call screen third_question with dissolve
    
    screen third_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Satanist, guitarist, sexually outgoing") ]
            action Jump("third_question_correct")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Satanist, drummer, sexual deviant") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Christian, socialist, book worm") ]
            action Jump("question_incorrect")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
    
    label third_question_correct:
    
        show violet underwear_happy at center with dissolve
        
        v "Incredible!"
        
        jump fourth_question
    
    return
    
    return
    
    label fourth_question:
    
    show violet underwear at center with dissolve
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    v "I'm going to ask you some music-related questions now, be prepared."
    
    v "How many neutral notes are in an octave?"
    
    call screen fourth_question with dissolve
    
    screen fourth_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("5 notes") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("7 notes") ]
            action Jump("fourth_question_correct")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("8 notes") ]
            action Jump("question_incorrect")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
        
    label fourth_question_correct:
        
        show violet underwear_happy at center with dissolve
        
        v "That one was easy!"
        
        jump fifth_question
        
    return
    
    return
    
    label fifth_question:
    
    show violet underwear at center  with dissolve
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    v "How many beats are in the first bar of Vivaldi's 'Autumn' from 'The Four Seasons'?"
    
    call screen fifth_question with dissolve
    
    screen fifth_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("3 beats") ]
            action Jump("fifth_question_correct")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("4 beats") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("8 beats") ]
            action Jump("question_incorrect")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
        
    label fifth_question_correct:
    
        show violet underwear_happy at center with dissolve
        
        v "Did you really get that one first try?"
        
        jump sixth_question
        
    return
    
    return
    
    label sixth_question:
    
    show violet underwear at center with dissolve
    
    $ tooltip = Tooltip("")
    
    $ renpy.block_rollback()
    
    v "What key is My Darkest Days - Without You played in?"
    
    call screen sixth_question with dissolve
    
    screen sixth_question:
        
        image "guitar":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
        
        imagebutton auto "guitar_option_a_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.735
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("E") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_b_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.77
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("C") ]
            action Jump("question_incorrect")
            
        imagebutton auto "guitar_option_c_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.65
            ypos 0.795
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("D/F#") ]
            action Jump("sixth_question_correct")
        
        text tooltip.value:
            xpos 0.65
            ypos 0.64
        
    label sixth_question_correct:
        
        show violet underwear_happy at center with dissolve
        
        v "Wow, you got that one right! I'm impressed."
        
        jump violet_succeed_date
        
    return
    
    return
    
    label question_incorrect:
    
        $ renpy.block_rollback()
    
        show violet underwear_think at center with dissolve
        
        v "That's the wrong answer."
        
        jump violet_fail_date
        
    return
return

# Violet "final" date for boy.

label date_violet_sex_letter:

    n "Purchase the full game to access the saucy content here: https://store.steampowered.com/app/2212600/Town_Girls/"
    
    jump main_hub_screen
    
    $ v_wet = 0

    scene black
    with dissolve
    
    play audio "audio/door_knock.flac"
    
    n "You hear a knock on the door, so you go downstairs and check."
    
    n "It's the mail, and there's a letter for you from Violet."
    
    play audio "audio/letter.flac"
    
    call screen violet_letter with dissolve
    
    screen violet_letter:
        
        imagebutton idle "violet_date_3_postcard":
            xanchor 0.5
            yanchor 0.5
            xpos 0.285
            ypos 0.5
            action Jump("date_violet_sex_pc")
        
        imagebutton idle "violet_date_3_pic":
            xanchor 0.5
            yanchor 0.5
            xpos 0.78
            ypos 0.5
            action Jump("date_violet_sex_pc")
    return
return

label date_violet_sex_pc:
    
    n "You get ready and make your way to Violet's house."
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene v_house_front_sex
    with dissolve
    
    play music "audio/nature.flac" loop fadein 3.0
    
    n "You arrive at Violet's house. There's no one outside and the garage is closed. Is anyone home?"
    
    scene v_house_front_sex
    with dissolve
    
    call screen date_violet_sex_objects with dissolve

    screen date_violet_sex_objects:
        
        imagebutton auto "v_door_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.637
            ypos 0.405
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's deep blue front door.") ]
            action Jump("date_violet_sex")
            
        imagebutton auto "v_gdoor_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.364
            ypos 0.364
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's garage - It's normally open, but\nnot today?") ]
            clicked [ Play("sound", "audio/garage.flac") ]
            
        imagebutton auto "tree_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.864
            ypos 0.337
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("I'd still like to be a tree.") ]
            clicked [ Play("sound", "audio/tree.flac") ]
            
        if window_crack_v == 0:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A window of Violet's house.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A small crack appeared."), SetVariable("window_crack_v", 1) ]
        elif window_crack_v == 1:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("Another small crack appeared."), SetVariable("window_crack_v", 2) ]
        elif window_crack_v == 2:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Another small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A bigger crack appeared."), SetVariable("window_crack_v", 3) ]
        elif window_crack_v == 3:
            imagebutton auto "v_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A bigger crack appeared.") ]
                clicked [ Play("sound", "audio/glass_break.flac"), tooltip.Action("You broke the window."), SetVariable("window_crack_v", 4) ]
                
        else:
        
            imagebutton idle "v_window_crack_ved":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ tooltip.Action("You broke the window.") ]
                action tooltip.Action("You broke the window.")
        
        if window_crack_v == 4:
            $ achievement.grant("window")
            $ achievement.grant("windowfetish")
            
        text tooltip.value:
            xpos 0.21
            ypos 0.75
    return
return

label date_violet_sex:
    
    $ tooltip = Tooltip("")
    
    play audio "audio/door_open.flac"
    
    scene v_house_front_sex_od
    with dissolve
    
    v "Hey [violet_name], I'm glad you made it! Please, come inside."
    
    scene v_inside_1
    with dissolve
    
    stop music fadeout 3.0
    
    show violet underwear_happy at center with dissolve
    
    v "I'm gonna head upstairs to get ready for our night of fun. Just come in my room when you're ready cutie."
    
    hide violet underwear_happy with dissolve
    
    jump date_violet_sex_hall
return

label date_violet_sex_hall:

    scene v_inside_1
    with dissolve
    
    call screen date_violet_boy_inside_objects with dissolve

    screen date_violet_boy_inside_objects:
        
        imagebutton auto "v_inside_door_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.438
            ypos 0.31
            hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Go into the storage room.") ]
            action Jump("date_violet_sex_storage")
            
        imagebutton auto "v_inside_stairs_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.859
            ypos 0.395
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go upstairs.") ]
            action Jump("date_violet_sex_landing")
            
        imagebutton auto "v_inside_pictures_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.6575
            ypos 0.238
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A picture of what appears to be Violet's parent's wedding\nand a generic picture of a flower.") ]
            clicked [ Play("sound", "audio/wedding.flac") ]
            
        imagebutton auto "v_inside_cupboard_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.46
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("An understair cupboard - I wonder what's inside?") ]
            clicked [ Play("sound", "audio/boing.flac") ]
            
        text tooltip.value:
            xpos 0.21
            ypos 0.75
    return
return

label date_violet_sex_storage:

    scene v_inside_2
    with dissolve

    call screen date_violet_boy_inside_storage with dissolve

    screen date_violet_boy_inside_storage:
        
        imagebutton auto "v_inside_boxes_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.5775
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Massive boxes full of various sex toys.") ]
            clicked [ Play("sound", "audio/boxes.flac") ]
            
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the hall.") ]
            action Jump("date_violet_sex_hall")
            
        imagebutton auto "left_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.0179
            ypos 0.4
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go into the kitchen.") ]
            action Jump("date_violet_sex_kitchen")
            
        text tooltip.value:
            xpos 0.1
            ypos 0.8
    return
return

label date_violet_sex_kitchen:
    
    scene v_inside_3
    with dissolve

    call screen date_violet_boy_inside_kitchen with dissolve

    screen date_violet_boy_inside_kitchen:
        
        imagebutton auto "v_inside_sink_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.955
            ypos 0.6
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A typical kitchen sink.") ]
            action Jump("sink_dialogue")
            
        imagebutton auto "v_inside_kettle_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.719
            ypos 0.491
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Your pretty average electric kettle.") ]
            clicked [ Play("audio", "audio/kettle.flac") ]
            
        imagebutton auto "v_inside_tea_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.483
            ypos 0.528
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A pot for storing tea bags.") ]
            clicked [ Play("audio", "audio/ding.flac") ]
            
        imagebutton auto "v_inside_sugar_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.539
            ypos 0.528
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A pot for storing sugar.") ]
            clicked [ Play("audio", "audio/ding_c.flac") ]
            
        imagebutton auto "v_inside_cupboards_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.662
            ypos 0.712
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Kitchen cupboards for storing kitchen stuff.") ]
            clicked [ Play("audio", "audio/boing.flac") ]
            
        imagebutton auto "v_inside_coffee_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.595
            ypos 0.528
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A pot for storing coffee.") ]
            clicked [ Play("audio", "audio/ding_a.flac") ]
            
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to storage.") ]
            action Jump("date_violet_sex_storage")
            
        imagebutton auto "v_inside_kdoor_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.181
            ypos 0.419
            hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Go into the dining room.") ]
            action Jump("date_violet_sex_dining")
            
        text tooltip.value:
            xpos 0.1
            ypos 0.86
    return
    
    label sink_dialogue:
    
    "The sink is too clean. Pee in it?"
    
    menu:
        "Sure, I needed to go anyway.":
            play audio "audio/peeing.flac"
            
            $ achievement.grant("sinkpee")
            
            if gender == 0:
                "You stand over the sink and fill it up with yellow liquid."
            elif gender == 1:
                "You sit over the sink and fill it up with yellow liquid."
            jump date_violet_sex_kitchen
            
            pause 15.0
            
        "Ew, no that's disgusting.":
            
            $ achievement.grant("nosinkpee")
            
            jump date_violet_sex_kitchen
    return
return

label date_violet_sex_dining:

    scene v_inside_4
    with dissolve

    call screen date_violet_boy_inside_dining with dissolve

    screen date_violet_boy_inside_dining:
        
        imagebutton auto "v_inside_dpic_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.709
            ypos 0.198
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A generic picture of a mountain field.") ]
            clicked [ Play("audio", "audio/nature.flac") ]
        
        if vase == 0:
            imagebutton auto "v_inside_vase_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.52
                ypos 0.491
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A glass vase with a fake potted plant inside.") ]
                clicked [ Play("audio", "audio/glass_break.flac"), SetVariable("vase", 1), tooltip.Action("You pushed the vase off the table.") ]
        else:
            imagebutton idle "debug"
        
        imagebutton auto "left_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.0179
            ypos 0.4
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go into the lounge.") ]
            action Jump("date_violet_sex_lounge")
        
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the kitchen.") ]
            action Jump("date_violet_sex_kitchen")
            
        text tooltip.value:
            xpos 0.1
            ypos 0.1
    return
return

label date_violet_sex_lounge:

    scene v_inside_5
    with dissolve

    call screen date_violet_boy_inside_lounge with dissolve

    screen date_violet_boy_inside_lounge:
        
        imagebutton auto "v_inside_tv_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.645
            ypos 0.445
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Quite an old flat screen television.") ]
            clicked [ Play("audio", "audio/tv.flac") ]
        
        if window_crack_v == 0:
            imagebutton auto "v_inside_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.316
                ypos 0.333
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The lounge window.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A small crack appeared."), SetVariable("window_crack_v", 1) ]
        elif window_crack_v == 1:
            imagebutton auto "v_inside_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.316
                ypos 0.333
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("Another small crack appeared."), SetVariable("window_crack_v", 2) ]
        elif window_crack_v == 2:
            imagebutton auto "v_inside_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.316
                ypos 0.333
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Another small crack appeared.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A bigger crack appeared."), SetVariable("window_crack_v", 3) ]
        elif window_crack_v == 3:
            imagebutton auto "v_inside_window_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.316
                ypos 0.333
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A bigger crack appeared.") ]
                clicked [ Play("sound", "audio/glass_break.flac"), tooltip.Action("You broke the window."), SetVariable("window_crack_v", 4) ]
        else:
            imagebutton idle "v_inside_bwindow":
                xanchor 0.5
                yanchor 0.5
                xpos 0.316
                ypos 0.333
                hovered [ tooltip.Action("You broke the window.") ]
                action tooltip.Action("You broke the window.")
        
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the dining room.") ]
            action Jump("date_violet_sex_dining")
            
        text tooltip.value:
            xpos 0.1
            ypos 0.7
    return
return

label date_violet_sex_landing:

    play audio "audio/stairs.flac"
    
    scene v_inside_6
    with dissolve

    call screen date_violet_boy_inside_landing with dissolve

    screen date_violet_boy_inside_landing:
        
        imagebutton auto "v_inside_vdoor_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.829
            ypos 0.48
            hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Violet's bedroom; it smells like her scent.") ]
            action Jump("date_violet_sex_room")
            
        imagebutton auto "v_inside_ldoor_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.315
            ypos 0.255
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Looks to be another bedroom, but the door is locked.") ]
            clicked [ Play("audio", "audio/parents_sex.flac") ]
        
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back downstairs.") ]
            action Jump("date_violet_sex_hall")
            
        text tooltip.value:
            xpos 0.1
            ypos 0.7
    return
    
return

label date_violet_sex_room:
    
    scene v_inside_7
    with dissolve

    call screen date_violet_boy_inside_room with dissolve

    screen date_violet_boy_inside_room:
    
        imagebutton auto "v_inside_bed_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.735
            ypos 0.64
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's bed. There's boxes underneath full of various sex toys, such as, dildos, fuzzy cuffs and vibrators.") ]
            clicked [ Play("audio", "audio/boing.flac") ]
    
        imagebutton auto "v_inside_chair_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.33
            ypos 0.6
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's desk chair. It looks like its seen her cum more than a few times.") ]
            clicked [ Play("audio", "audio/boing.flac") ]
    
        imagebutton auto "v_inside_pc_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.13
            ypos 0.34
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's computer. There's a lot of porn on the desktop.") ]
            clicked [ Play("audio", "audio/computer.flac") ]
            
        imagebutton auto "v_inside_desk_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.11
            ypos 0.624
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's desk. In the draw, there's a rainbow dildo, lube and some tampons.") ]
            clicked [ Play("audio", "audio/boing.flac") ]
        
        imagebutton auto "v_inside_mirror_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.052
            ypos 0.64
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's mirror. So that's how she gets those decent pics.") ]
            clicked [ Play("audio", "audio/boing.flac") ]
        
        imagebutton auto "down_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.9681
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the landing.") ]
            action Jump("date_violet_sex_landing")
            
        imagebutton auto "v_click_uw_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.6
            ypos 0.55
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Hey cutie, when you wanna get dirty?") ]
            action Jump("date_violet_sex_start")
            
        text tooltip.value:
            xpos 0.05
            ypos 0.02
    return
return

label date_violet_sex_start:

    scene v_inside_sex
    with dissolve

    play music "audio/violet_theme.flac" loop fadein 3.0
    
    show violet underwear at center with dissolve
    
    v "Do you like my room? I decorated it myself a few years ago."
    
    menu:
        "It's really cool!":
            pv "It's really cool!"
            
            show violet underwear_happy at center with dissolve
            
            v "Thank you, you're so kind."
            
        "Black and red? Seriously? Are you 12?":
            pv "Black and red? Seriously? Are you 12?"
            
            jump violet_fail_date
    
    v "I want to reward you with something special because you've been a great partner these last few months."
    
    menu:
        "What did you want to give to me?":
            pv "What did you want to give to me?"
            
            show violet underwear_happy at center with dissolve
            
            v "As a thank you, I wanted to give you full access to my body so you can do whatever you want to me."
            
        "Thanks, it's the least I could do.":
            pv "Thanks, it's the least I could do."
            
            show violet underwear_happy at center with dissolve
            
            v "No, thank you for not being a creep and actually listening to me for once. Other people don't give a shit about me."
    
    v "I think you should take my panties off first, cutie. I really want to show my pussy."
    
    hide violet underwear_happy at center with dissolve
    
    jump take_off_1
return

label take_off_1:

    show violetmg at center
    
    call screen take_off_1
    
    $ renpy.block_rollback()
    
    if droppable == "Drag Space":
        $ xpos_var = 150
    else:
        $ xpos_var = 640
    if draggable == "wrong_answer_1":
    
        hide violetmg at center
        show violetboobsangry at center with dissolve
        v "Gah! You weren't supposed to take that off yet, pervert! Wait until I tell you to!"
        jump violet_fail_date
        
    elif draggable == "right_answer":
    
        hide violetmg at center
        show violet vagina_happy at center with dissolve
        v "Hehe! Like the look of my pussy between my legs?"
        jump take_off_2
    
    screen take_off_1:
        
        draggroup:
            drag:
                drag_name "wrong_answer_1"
                xpos 0.458
                ypos 0.295
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                image "violetbra"
                    
            drag:
                drag_name "right_answer"
                xpos 0.429
                ypos 0.625
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                image "violetpanties"
            drag:
                drag_name "Drag Space"
                xpos 0.7
                ypos 0.33
                child "tub"
                draggable False
                droppable True
                
        image "violetmgarm":
            xpos 0.4
            ypos 0.365
    return
return

label take_off_2:

    hide violet vagina_happy
    
    show violetmg at center
    
    call screen take_off_2
    
    $ renpy.block_rollback()
    
    if droppable == "Drag Space":
        $ xpos_var = 150
    else:
        $ xpos_var = 640
    if draggable == "right_answer":
        
        hide violetmg at center
        show violet naked at center with dissolve
        v "Thank you for undressing me. I'll get comfortable on the bed now."
        jump violet_date_sex_play
    elif draggable == "wrong_answer_1":
        ""
        
    screen take_off_2:
        
        draggroup:
            drag:
                drag_name "right_answer"
                xpos 0.458
                ypos 0.295
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                image "violetbra"
                    
            drag:
                drag_name "wrong_answer_1"
                xpos 0.429
                ypos 0.625
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                image "debug"
            drag:
                drag_name "Drag Space"
                xpos 0.7
                ypos 0.33
                child "tub"
                draggable False
                droppable True
                
        image "violetmgarm":
            xpos 0.4
            ypos 0.365
    return
return

label violet_date_sex_play:

    if v_wet == 0:
        scene v_inside_play_1
        with dissolve
    elif v_wet == 1:
        scene v_inside_play_1a
        with dissolve
    
    v "You can either play with me first or go straight into making love. It's your choice, hun."
    
    if gender == 0:
        call screen date_violet_boy_inside_sex_play with dissolve

        screen date_violet_boy_inside_sex_play:
    
            imagebutton auto "pp_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.9
                ypos 0.85
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Use Violet's rainbow dildo on her.") ]
                action Jump("violet_date_sex_dildo")
    
            imagebutton auto "finger_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.9
                ypos 0.6
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Finger Violet until she's wet.") ]
                action Jump("violet_date_sex_finger")
    
            imagebutton auto "sex_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.9
                ypos 0.4
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Commit sexual intercourse with Violet.") ]
                action Jump("violet_date_sex_intercourse")
            
            text tooltip.value:
                xpos 0.05
                ypos 0.1
        return
    
    elif gender == 1:
        call screen date_violet_girl_inside_sex_play with dissolve

        screen date_violet_girl_inside_sex_play:
    
            imagebutton auto "pp_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.9
                ypos 0.85
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Use Violet's rainbow dildo on her.") ]
                action Jump("violet_date_sex_dildo")
    
            imagebutton auto "finger_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.9
                ypos 0.4
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Commit sexual intercourse with Violet.") ]
                action Jump("violet_date_sex_intercourse")
            
            text tooltip.value:
                xpos 0.05
                ypos 0.1
        return
return

label violet_date_sex_finger:

    scene v_inside_play_2
    with dissolve
    
    $ v_wet = 1
    
    v "Yes... I can feel your fingers touching my g-spot..."
    
    jump violet_date_sex_play
return

label violet_date_sex_dildo:

    scene v_inside_play_3
    with dissolve
    
    $ v_wet = 1
    
    v "Ahhh... It feels so good..."
    
    jump violet_date_sex_play
return

label violet_date_sex_intercourse:

    scene blank
    with dissolve
    
    stop music fadeout 3.0
    
    if gender == 0:
        n "You slowly insert your penis into Violet's tight fox pussy..."
    
        n "She moans with happiness as you move up and down inside her..."
    elif gender == 1:
        n "You slowly insert your fingers into Violet's tight fox pussy..."
    
        n "She moans with happiness as you move up and down inside her..."
    
    play music "audio/violet_sex.flac"
    
    pause 39.0
    
    stop music fadeout 3.0
    
    pause 3.0
    
    jump violet_date_sex_success
return

label violet_date_sex_success:
    
    play music "audio/violet_theme.flac" fadein 3.0

    if gender == 0:
        scene v_inside_cum
        with dissolve
    if gender == 1:
        $ v_wet = 1
        scene v_inside_play_2
        with dissolve
    
    v "Oh my God... That felt so good... I needed that so badly... Thank you..."
    
    menu:
        "How about another round?":
            
            pv "How about another round?"
            
            v "Only this once, cutie."
            
            scene blank
            with dissolve
    
            stop music fadeout 3.0
            
            if gender == 0:
                
                $ achievement.grant("balls")
                
                n "You insert your penis back into Violet's opened hole..."
    
                n "She again, moans with happiness as you move up and down inside her..."
            elif gender == 1:
            
                $ achievement.grant("ironfingers")
                
                n "You insert your fingers back into Violet's opened hole..."
    
                n "She again, moans with happiness as you move them up and down inside her..."
    
            play music "audio/violet_sex.flac"
    
            pause 39.0
    
            stop music fadeout 3.0
    
            pause 3.0
            
            play music "audio/violet_theme.flac" fadein 3.0
           
        "Doing you felt amazing.":
            pv "Doing you felt amazing."
            
    if gender == 0:
        scene v_inside_cum
        with dissolve
    if gender == 1:
        $ v_wet = 1
        scene v_inside_play_2
        with dissolve
            
    if gender == 0:
        v "Wait... Did you cum in me?"
    
        v "Were you even wearing protection...?"
    
        v "I'm not on contraception..."
    
        v "..."
    elif gender == 1:
        v "I think I came."
        
        v "Your fingers felt so amazing inside me."
    
    $ renpy.block_rollback()
    
    stop music fadeout 3.0
        
    play audio "audio/date_success.flac"
    n "Date Success!"
    
    scene blank
    with dissolve
    
    if gender == 0:
        n "You might have made Violet pregnant and took her panties."
    elif gender == 1:
        n "You took Violet's panties."
        
    $ achievement.grant("violet_3_success")
    
    $ dating += 1
    $ violet += 1
    jump main_hub_screen
return

# Violet fail date.

label violet_fail_date:

    hide violetboobsangry
    hide violetvaginaangry

    stop music

    $ renpy.block_rollback()
    
    show violet angry at center with dissolve
    
    $ achievement.grant("fail")
        
    v "It seems we're not a great match for each other [violet_name]. I think we should see other people. I'm sorry."
        
    play audio "audio/date_fail.tgm"
    n "Date failed..."
        
    jump main_hub_screen     
return

# Violet succeed date.

label violet_succeed_date:
    if violet == 1:
        if gender == 0:
            v "Here's a picture of me so you can jerk off to it or something."
        elif gender == 1:
            v "Here's a picture of me so you can finger yourself to it or something."
    
        play audio "audio/date_success.tgm"
        n "Date Success!"
    
        hide violet happy with dissolve
    
        scene blank
        with dissolve
    
        stop music fadeout 3.0
    
        pause 3.0
    
        n "You got a picture of Violet. You can now look at this picture in the Gallery."
    
        $ achievement.grant("violet_1_success")
    
        call screen violet_pic_1 with dissolve
    
        screen violet_pic_1:
        
            imagebutton idle "violet_date_1_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("v_variable_update")
    elif violet == 2:
        
        $ renpy.block_rollback()
        
        v "I would love to take our relationship to the next level [violet_name]."
        
        show violet underwear_happy at center with dissolve
        
        if gender == 0:
            v "Here's a picture of me so you can jerk off to me more."
        elif gender == 1:
            v "Here's a picture of me so you can finger yourself to me more."
        
        play audio "audio/date_success.tgm"
        n "Date Success!"
        
        hide violet underwear_happy with dissolve
        
        scene blank
        with dissolve
    
        stop music fadeout 3.0
        
        pause 3.0
        
        n "You got a picture of Violet in her underwear. You can now look at this picture in the Gallery."
        
        $ achievement.grant("violet_2_success")
        
        call screen violet_pic_2 with dissolve
    
        screen violet_pic_2:
        
            imagebutton idle "violet_date_2_pic":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("v_variable_update")
        return
    elif violet == 3:    
        play music "audio/violet_theme.tgm" fadein 3.0

        if gender == 0:
            scene v_inside_cum
            with dissolve
        if gender == 1:
            $ v_wet = 1
            scene v_inside_play_2
            with dissolve
    
        v "Oh my God... That felt so good... I needed that so badly... Thank you..."
    
        menu:
            "How about another round?":
            
                pv "How about another round?"
            
                v "Only this once, cutie."
            
                scene blank
                with dissolve
    
                stop music fadeout 3.0
            
                if gender == 0:
                
                    $ achievement.grant("balls")
                
                    n "You insert your penis back into Violet's opened hole..."
    
                    n "She again, moans with happiness as you move up and down inside her..."
                elif gender == 1:
            
                    $ achievement.grant("ironfingers")
                
                    n "You insert your fingers back into Violet's opened hole..."
    
                    n "She again, moans with happiness as you move them up and down inside her..."
    
                play music "audio/violet_sex.tgm"
    
                pause 39.0
    
                stop music fadeout 3.0
    
                pause 3.0
            
                play music "audio/violet_theme.tgm" fadein 3.0
           
            "Doing you felt amazing.":
                pv "Doing you felt amazing."
            
        if gender == 0:
            scene v_inside_cum
            with dissolve
        if gender == 1:
            $ v_wet = 1
            scene v_inside_play_2
            with dissolve
            
        if gender == 0:
            v "Wait... Did you cum in me?"
    
            v "Were you even wearing protection...?"
    
            v "I'm not on contraception..."
    
            v "..."
        elif gender == 1:
            v "I think I came."
        
            v "Your fingers felt so amazing inside me."
    
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.tgm"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
    
        scene blank
        with dissolve
    
        if gender == 0:
            n "You might have made Violet pregnant and took her panties."
        elif gender == 1:
            n "You took Violet's panties."
        
        $ achievement.grant("violet_3_success")
        
        jump v_variable_update
        
        
    label v_variable_update:
        $ dating += 1
        $ violet += 1
        jump main_hub_screen
    return    
return