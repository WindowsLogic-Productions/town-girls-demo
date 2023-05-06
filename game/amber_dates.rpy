# Amber first date.

label date_amber_1_pc:

    $ achievement.grant("first")
    
    scene a_shop_outside
    with dissolve
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/rain.tgm" loop fadein 3.0
    
    pause 3.0
    
    n "You moved in not long ago and need food and drink to sustain yourself, so you decide to go to the local shop to pick up some groceries."
    
    n "You arrive at the shop and notice there’s a girl outside wearing the shop uniform and sucking on a Candy Stick like a cigarette. This feels like the perfect chance to talk to her. Do you approach?"
    
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
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("The shop where Amber works.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("A small crack appeared in the glass."), SetVariable("window_crack_a", 1) ]
        elif window_crack_a == 1:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A small crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("Another small crack appeared in the glass."), SetVariable("window_crack_a", 2) ]
        elif window_crack_a == 2:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Another small crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_knock.tgm"), tooltip.Action("A bigger crack appeared in the glass."), SetVariable("window_crack_a", 3) ]
        elif window_crack_a == 3:
            imagebutton auto "a_shop_body_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.51
                ypos 0.432
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("A bigger crack appeared in the glass.") ]
                clicked [ Play("sound", "audio/glass_break.tgm"), tooltip.Action("You broke the shop's windows."), SetVariable("window_crack_a", 4) ]
        else:
            imagebutton idle "a_shop_body_cracked":
                xanchor 0.5
                yanchor 0.5
                xpos 0.511
                ypos 0.432
                hovered [ tooltip.Action("You broke the shop's windows.") ]
                action Jump("a_collect_item_1")
        
        if window_crack_a == 4:
            
            $ window_cracked +=1
            
            imagebutton auto "amber_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Tabby Cat: I hope my boss doesn't think I did this.") ]
                action Jump("date_amber_1")
        else:
            imagebutton auto "amber_click_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.55
                ypos 0.55
                hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Tabby Cat: I didn't expect it to be so wet today...") ]
                action Jump("date_amber_1")
                
        image "rain":
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            
        text tooltip.value:
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
    elif window_cracked == 2:
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
    
    play music "audio/amber_theme.tgm" loop fadein 3.0
    
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
    
    play audio "audio/remember.tgm"
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
            
            $ achievement.grant("tabbynudes")
            
        "Nice, I'll follow you as soon as possible.":
            pa "Nice, I'll follow you as soon as possible."
            
            show amber giggle blushing at center with dissolve
            
            a "Thank you, that means a lot. I'm sure you'll like what you see on my profile."
            
            $ achievement.grant("tabbynudes")
            
    $ renpy.block_rollback()
    
    show amber neutral at center with dissolve
            
    a "Where are you from, [amber_name]?"
    
    $ amber_from = renpy.input("Enter where you're from.")
    $ amber_from = amber_from.strip()
    if amber_from == "":
        $ amber_from = "Nowhere"
        
    $ renpy.block_rollback()
        
    play audio "audio/remember.tgm" 
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

    n "Purchase the full game to access the saucy content here: https://store.steampowered.com/app/2212600/Town_Girls/"
    
    scene black
    with dissolve
    
    $ a_wet = 0
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0

    if window_crack_a == 4:
        scene a_shop_outside_crack
        with dissolve
    else:
        scene a_shop_outside
        with dissolve
    
    play music "audio/rain.tgm" loop fadein 3.0
    
    n "You meet Amber outside the shop she works but she’s not wearing anything on her lower half. Before you can say anything about it, she takes you to the local park."
    
    scene black
    with dissolve
    
    n "The park is empty as it’s raining, and you’re still wondering why Amber is not wearing anything on her lower half in the cold, wet rain."
    
    label a2_jump_from_collect:
    
    scene a_park
    with dissolve
    
    call screen date_amber_2_objects with dissolve

    screen date_amber_2_objects:
        
        imagebutton auto "a_park_tree_1_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.818
            ypos 0.372
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("I like being in parks.") ]
            action Jump("a_collect_item_2")
            
        imagebutton auto "a_park_tree_2_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.179
            ypos 0.297
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Parks are nice.") ]
            action Jump("a_collect_item_3")
            
        imagebutton auto "a_park_tree_3_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.681
            ypos 0.473
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("The rain makes me happy.") ]
            action Jump("a_collect_item_4")
            
        imagebutton auto "a_park_tree_4_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.171
            ypos 0.353
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Do you think the animals can hear us?") ]
            action Jump("a_collect_item_5")
        
        imagebutton auto "a_park_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.5
            hovered [ Play("audio", "audio/select.tgm"), tooltip.Action("Amber: I- I didn't think my pussy would be this c- cold...") ]
            action Jump("date_amber_2")
            
        text tooltip.value:
            xpos 0.5
            ypos 0.005
            
    return
    
    label a_collect_item_2:
    
    if a_item_sap == 1:
       n "You search the tree again and find nothing."
    else:
        
        scene a_park_blur
        with dissolve
        
        show a_sap at center with dissolve
        
        n "You search the tree and find a strange gooey liquid."
        $ a_item_sap += 1
        $ a_items += 1
        
    jump a2_jump_from_collect
    
    return
    
    label a_collect_item_3:
    
    if a_item_condom == 1:
       n "You search the tree again and find nothing."
    else:
        scene a_park_blur
        with dissolve
        
        show a_condom at center with dissolve
        
        n "You search the tree and find a used condom."
        $ a_item_condom += 1
        $ a_items += 1
        
    jump a2_jump_from_collect
    
    return
    
    label a_collect_item_4:
    
    if a_item_egg == 1:
       n "You search the tree again and find nothing."
    else:
        
        scene a_park_blur
        with dissolve
        
        show a_egg at center with dissolve
        
        n "You search the tree and find a bird egg."
        $ a_item_egg += 1
        $ a_items += 1
        
    jump a2_jump_from_collect
    
    return
    
    label a_collect_item_5:
    
    if a_item_bark == 1:
       n "You search the tree again and find nothing."
    else:
        scene a_park_blur
        with dissolve
        
        show a_bark at center with dissolve
        
        n "You search the tree and find a piece of bark."
        $ a_item_bark += 1
        $ a_items += 1
        
    jump a2_jump_from_collect
    
    return
return

# Amber fail date.

label amber_fail_date:

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
        
        play audio "audio/date_fail.tgm"
        n "Date failed..."
        
        jump main_hub_screen     
return

# Amber succeed dates.

label amber_succeed_date:

    if amber == 1:
    
        play audio "audio/date_success.tgm"
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
        play audio "audio/date_success.tgm"
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
        play music "audio/amber_theme.tgm" fadein 3.0

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
        
        play audio "audio/date_success.tgm"
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
    
        jump a_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label a_variable_update:
    
    $ dating += 1
    $ amber += 1
    jump main_hub_screen
    
    return

return