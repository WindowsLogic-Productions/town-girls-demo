# Amber's opening scene.

label date_amber_opening:

    jump date_amber_timecheck
return

# Check time of game to determine if dates are possible.

label date_amber_timecheck:

    scene loading
    with irisout
    
    $ _game_menu_screen = None
    $ quick_menu = False

    if time == 1:
        if amber == 1:
            jump date_amber_1_pc
        elif amber == 2:
            jump date_amber_2_pc
        else:
            jump date_amber_timechecked_working
    elif time == 2:
        if amber == 1:
            jump date_amber_1_pc
        elif amber == 2:
            jump date_amber_2_pc
        else:
            jump date_amber_timechecked_working
    else:
        if amber == 1:
            jump date_amber_timechecked_asleep
        elif amber == 2:
            jump date_amber_timechecked_asleep
        else:
            jump date_amber_sex_letter
return

label date_amber_timechecked_working:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/time_advance_ph.flac" loop fadein 3.0
    
    pause 3.0
    
    scene black
    with dissolve
    
    n "Amber is currently working, do you want to advance time?"
        
    menu:
        "Go to sleep":
        
            n "You sleep until it's evening."
            
            $ time = 3
                
            jump main_hub_screen
                
        "Go to the shop Amber works at and stalk her":
                
            n "You go to the shop where Amber works to stalk her."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                scene a_working
                with pixellate
            elif nightstalk == 2:
                scene a_working
                with pixellate
            elif nightstalk == 3:
                scene a_working
                with pixellate
            else:
                scene a_working
                with pixellate
                
            $ time = 3
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

label date_amber_timechecked_asleep:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/time_advance_ph.flac" loop fadein 3.0
    
    pause 3.0
    
    scene black
    with dissolve

    n "Amber is currently sleeping, do you want to advance time?"
        
    menu:
        "Go to sleep":
            
            n "You sleep until it's morning."
                
            $ time = 1
                
            jump main_hub_screen
                
        "Go to Amber's house and watch her sleep until morning":
                
            n "You go to Amber's house with a ladder. Her bedroom window is open so you position the ladder and climb up to see her sleeping."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                scene a_sleeping
                with pixellate
            elif nightstalk == 2:
                scene a_sleeping
                with pixellate
            elif nightstalk == 3:
                scene a_sleeping
                with pixellate
            else:
                scene a_sleeping
                with pixellate
                
            $ time = 1
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

# Amber first date.

label date_amber_1_pc:

    $ achievement.grant("first")
    
    scene a_shop_outside
    with irisout
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/rain.flac" loop fadein 3.0
    
    pause 3.0
    
    n "After a month of stalking the tabby cat, you know exactly when her break hours are, so go to meet her. You want to make it seem like an accident."
    
    n "You arrive at the shop and notice the tabby cat is outside wearing the shop uniform and sucking on a Candy Stick like a cigarette. This feels like the perfect chance to talk to her. Do you approach?"
    
    label a1_jump_from_collect:
    
    if window_crack_a == 1:
        scene a_shop_outside_crack
        with dissolve
    else:
        scene a_shop_outside
        with dissolve
    
    call screen date_amber_1_objects with dissolve

    screen date_amber_1_objects:
            
        if window_crack_a == 0:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The shop where Amber works.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A small crack appeared in the glass."), SetVariable("window_crack_a", 1) ]
        elif window_crack_a == 1:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A small crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("Another small crack appeared in the glass."), SetVariable("window_crack_a", 2) ]
        elif window_crack_a == 2:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Another small crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A bigger crack appeared in the glass."), SetVariable("window_crack_a", 3) ]
        elif window_crack_a == 3:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A bigger crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_break.flac"), tooltip.Action("You broke the shop's windows."), SetVariable("window_crack_a", 4) ]
        else:
            imagebutton idle "a_shop_body_cracked":
                xanchor 0.5
                yanchor 0.5
                xpos 0.511
                ypos 0.432
                hovered [ tooltip.Action("You broke the shop's windows.") ]
                action Jump("a_collect_item_1")
        
        if window_crack_a == 4:
            
            $ window_cracked += 1
            
            imagebutton auto "amber_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Tabby Cat: I hope my boss doesn't think I did this.") ]
                action Jump("date_amber_1")
        else:
            imagebutton auto "amber_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Tabby Cat: I didn't expect it to be so wet today...") ]
                action Jump("date_amber_1")
                
        image "rain":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
    
    return
    return

    label a_collect_item_1:
    
    if a_item_glass == 1:
        
        scene a_shop_outside_crack
        with dissolve
        
        n "You search around the shop again and find nothing."
    else:
        
        scene a_shop_outside_crack_blur
        with dissolve
        
        show a_glass_shard at center with dissolve
        
        n "You search around the area of the shop and find a shard of glass."
        $ a_item_glass += 1
        $ a_items += 1
        
        hide a_glass_shard at center with dissolve
        
    jump a1_jump_from_collect
    
    return
return

label date_amber_1:

    if window_cracked == 1:
        $ achievement.grant("window")
    else:
        $ achievement.grant("windowfetish")

    $ amber_name = ""
    
    if window_crack_a == 4:
        scene a_shop_outside_crack
        with dissolve
    else:
        scene a_shop_outside
        with dissolve
    
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/amber_theme.flac" loop fadein 3.0
    
    pause 3.0
    
    show amber neutral at center with dissolve
    
    a "What’s up?"
    
    menu:
        "Nothing much, what about you?":
            pa "Nothing much, what about you?"
            
            a "I’m just on my break, and I decided to eat some Candy Sticks because I haven’t had them since childhood."
        
        "What's that in your hand?":
            pa "What’s that in your hand?"
            
            a "It’s a Candy Stick, I used to eat them mostly when I was a kid, but I thought I would get some today for nostalgia."
            
    $ renpy.block_rollback()
    
    a "My name is Amber, what’s yours?"
    
    $ amber_name = renpy.input("Enter a name you want Amber to remember.")
    $ amber_name = amber_name.strip()
    if amber_name == "":
        $ amber_name = "Person"
    
    $ renpy.block_rollback()
    
    play audio "audio/remember.flac"
    n "Amber will remember that."
    
    show amber giggle at center with dissolve
    
    a "[amber_name] is a cute name."
    
    show amber neutral at center with dissolve
    
    pa "I'm [age] years old, what about you?"
    
    a "I’m 18. My birthday is in April."
    
    a "I left school and got this part-time job when I was sixteen. It’s nice since the boss respects me and pays me fairly."
    
    a "Do you have a Xintendo 4DS? It’d be cool if we could add each other as friends!"
    
    menu:
        "I do. What's your friend code?":
            pa "I do. What's your friend code?"
            
            $ achievement.grant("3ds")
            
            a "My friend code is 4167 5812 4869."
            
            pa "Cool, I’ll add you as soon as possible."
            
        "I don’t, sorry.":
            pa "I don't, sorry."
            
            show amber giggle at center with dissolve
            
            a "That’s okay, it’s quite an old system anyway."
            
    $ renpy.block_rollback()
    
    show amber neutral at center with dissolve
    
    a "I read quite a lot. I’ve probably read over 100 books since I started."
    
    show amber giggle blushing at center with dissolve
    
    a "My favourite books have been the Harry Potter stories. His use of magic is so attractive."
    
    menu:
        "Have you read any other books?":
            pa "Have you read any other books?"
            
            show amber giggle at center with dissolve
            
            a "When I was younger, I used to read the “Mona” series of books, her imagination was so wild."
            
            $ achievement.grant("bookworm")
        
        "Have you read any smut?":
            pa "Have you read any smut?"
            
            show amber giggle blushing at center with dissolve
            
            a "Maybe I have, maybe I haven’t."
            
            show amber blush at center with dissolve
            
            a "I- I have written some smut about an animal wanting this other animal so badly that she m- masturbates in the school toilets for him."
            
            show amber embarrased blush at center with dissolve
            
            a "I- I might have posted some “smut” online recently as well."
            
            $ achievement.grant("lewd")
            
        "Take off your clothes.":
            pa "Take off your clothes."
            
            $ achievement.grant("takeoff2")
            
            show amber angry blush at center with dissolve
            
            a "What!? You… You… You PERVERT!!! Why would you ask something so direct when we’ve only just met!? I can’t believe this! I ought to file a restraining order for creeps like you!"
            
            jump amber_fail_date
            
    $ renpy.block_rollback()
    
    show amber neutral at center with dissolve
    
    menu:
        "Do you have any confessions or secrets?":
            pa "Do you have any confessions or secrets?"
            
            show amber embarrased blush at center with dissolve
            
            a "How forward of you… I- I think I can tell you some stuff."
            
            a "I- I might go outside without wearing anything except a hoodie to cover myself. I- I like it when people see my hole…"
            
            $ achievement.grant("hole")
            
        "What's the dirtiest thing you've done?":
            pa "What’s the dirtiest thing you’ve done?"
            
            show amber embarrased blush at center with dissolve
            
            a "T- That’s very forward… Um… I- I can tell you something."
            
            a "I- I have to travel home on the bus every day… I- I like r- rubbing my lower bits into the bus seats s- so they get wet with my f- fluids… D- Depending on i- if I need the t- toilet after work, I- I p- pee on the seat I’m sitting on."
            
            $ achievement.grant("bussy")
            
        "Do you have any kinks?":
            pa "Do you have any kinks?"
            
            show amber embarrased blush at center with dissolve
            
            a "F- Forward question!... I- I’ll only tell you one."
        
            a "T- The thought of doing something naughty with my hole in public makes me w- wet."
            
            $ achievement.grant("tabbykink")
            
    show amber neutral at center with dissolve
            
    a "I have a ClopPad profile if you want to follow it, my username is s3cr3tlyR3AD1N_."
    
    $ renpy.block_rollback()
    
    menu:
        "What's ClopPad?":
            pa "What's ClopPad?"
            
            show amber giggle at center with dissolve
            
            a "Have you not heard of it? It’s a cool social media that lets you post anything, even if it’s not safe for work."
            
            pa "Nice. I’ll make sure to follow you on there."
            
            show amber giggle blushing at center with dissolve
            
            a "Thank you, I’m sure you’ll like what you see."
            
            $ achievement.grant("lewd")
            
        "Nice, I'll follow you as soon as possible.":
            pa "Nice, I'll follow you as soon as possible."
            
            show amber giggle blushing at center with dissolve
            
            a "Thank you, that means a lot. I'm sure you'll like what you see on my profile."
            
            $ achievement.grant("lewd")
            
    $ renpy.block_rollback()
    
    show amber neutral at center with dissolve
            
    a "Where are you from, [amber_name]?"
    
    $ amber_from = renpy.input("Enter where you're from.")
    $ amber_from = amber_from.strip()
    if amber_from == "":
        $ amber_from = "Nowhere"
        
    $ renpy.block_rollback()
        
    play audio "audio/remember.flac" 
    n "Amber will remember that."
    
    show amber giggle at center with dissolve
    
    a "Oh, cool! I don’t think I’ve been to [amber_from] before."
    
    show amber angry at center with dissolve
    
    a "Ugh. I didn’t realise the time."
    
    a "I have to head back into work now. I’d love to see you again some time."
    
    a "Here’s a picture of me with the time I’m next free so you can see me."
    
    $ renpy.block_rollback()
    
    hide amber angry with dissolve
    
    jump amber_succeed_date
return

# Amber second date.

label date_amber_2_pc:

    n "Hold up! You need to purchase the full game to see Amber's tight pussy: https://windowslogic.itch.io/town-girls"
    
    jump main_hub_screen
return

# Amber fail date.

label amber_fail_date:

    stop music
        
    $ renpy.block_rollback()
        
    if amber == 2:
        show amber angry hn at center with dissolve
            
        $ a_item_condom = 0
        $ a_item_egg = 0
        $ a_item_bark = 0
        $ a_item_sap = 0
        if a_item_glass == 0:
            $ a_items = 0
        else:
            $ a_items = 1
    elif amber == 3:
        show amber angry n at center with dissolve
        
    elif amber == 1:
        show amber angry at center with dissolve
            
        $ a_item_glass = 0
        $ a_items = 0
        
    $ achievement.grant("fail")
        
    a "I thought we really had something [amber_name]. I can't believe this."
        
    play audio "audio/date_fail.flac"
    n "Date failed..."
        
    if time == 3:
        $ time -= 2
    else:
        $ time += 1
        
    jump main_hub_screen
return

# Amber succeed dates.

label amber_succeed_date:

    if amber == 1:
    
        play audio "audio/date_success.flac"
        n "Date Success!"
    
        scene blank
        with irisin
    
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
        with irisin
    
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
        with irisin
    
        if gender == 0:
            n "You might have made Amber pregnant and took her panties."
        elif gender == 1:
            n "You took Amber's panties."
        
        $ achievement.grant("amber_3_success")
    
        jump a_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label a_variable_update:
    
    $ dating += 1
    $ amber += 1
    if time == 3:
        $ time -= 2
    else:
        $ time += 1
    jump main_hub_screen
    
    return

return