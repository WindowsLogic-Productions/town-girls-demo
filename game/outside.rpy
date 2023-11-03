# Load the map for revisiting locations.

label outside_map:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    if time == 3:
        show screen map_items_night
        scene map_night
        with pixellate
        
        play music "audio/town_night.flac" loop fadein 3.0
        
        call screen map_items_night
    else:
        show screen map_items_day
        scene map
        with pixellate
    
        play music "audio/town.flac" loop fadein 3.0
    
        call screen map_items_day
    
    screen map_items_day:
        
        if amber >= 3:
            imagebutton auto "park_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.904
                ypos 0.47
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Willow Gardens") ]
                action Jump("amber_2")
        else:
            image "debug":
                xanchor 0.5
                yanchor 0.5
                xpos 0.90
                ypos 0.47
            
        if amber >= 2:
            imagebutton auto "shop_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.84
                ypos 0.07
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Puddleshire General Store") ]
                action Jump("amber_1")
        else:
            image "debug":
                xanchor 0.5
                yanchor 0.5
                xpos 0.90
                ypos 0.47
            
        if sierra >= 2:
            imagebutton auto "museum_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.37
                ypos 0.28
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Puddleshire Art Museum") ]
                action Jump("sierra_1")
        else:
            image "debug":
                xanchor 0.5
                yanchor 0.5
                xpos 0.90
                ypos 0.47
            
        if violet == 2:
            imagebutton auto "house_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.57
                ypos 0.35
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Violet's House") ]
                action Jump("violet_1")
        elif violet >= 4:
            imagebutton auto "house_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.57
                ypos 0.35
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Violet's House") ]
                action Jump("violet_3")
        
        if violet >= 3:    
            imagebutton auto "cinema_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.12
                ypos 0.27
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Abandoned Cinema") ]
                action Jump("violet_2")
        else:
            image "debug":
                xanchor 0.5
                yanchor 0.5
                xpos 0.90
                ypos 0.47
                
        imagebutton auto "close_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.9
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
            action Jump("main_hub_screen")
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.11
            ypos 0.95
    
    return
    
    screen map_items_night:
    
        if amber >= 4:
            imagebutton auto "placeholder_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.84
                ypos 0.07
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Puddleshire General Store") ]
                action Jump("amber_3")
        else:
            image "debug":
                xanchor 0.5
                yanchor 0.5
                xpos 0.90
                ypos 0.47
                
        imagebutton auto "close_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.9
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
            action Jump("main_hub_screen")
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.11
            ypos 0.95
    
    return
return

label violet_1:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/nature.flac" loop fadein 3.0
    
    show screen violet_1_revisit_objects
    
    scene v_house_front_pc
    with dissolve
    
    label vr1_jump_from_collect:
    
        if window_crack_a == 1:
            scene v_house_front_crack
            with dissolve
        else:
            scene v_house_front_pc
            with dissolve
    
    call screen violet_1_revisit_objects with dissolve

    screen violet_1_revisit_objects:
    
        imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.05
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the map.") ]
                action Jump("outside_map")
        
        imagebutton auto "violet/date_1/v_electric_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.334
            ypos 0.35
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The Arctic Fox's electric guitar is so cool.") ]
            action Jump("vr_collect_item_3")
            
        imagebutton auto "violet/date_1/v_acoustic_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.366
            ypos 0.356
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("It rattles.") ]
            action Jump("vr_collect_item_3")
            
        imagebutton auto "violet/date_1/v_amp_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.426
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Pretty rad amp with tons of dials.") ]
            action Jump("vr_collect_item_4")
            
        imagebutton auto "violet/date_1/v_wires_left_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.27
            ypos 0.401
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Just a bunch of audio cables.") ]
            action Jump("vr_collect_item_5")
            
        imagebutton auto "violet/date_1/v_wires_right_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.46
            ypos 0.380
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Just a bunch of audio cables.") ]
            action Jump("vr_collect_item_5")
            
        imagebutton auto "violet/date_1/v_mini_amp_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.47
            ypos 0.41
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A miniture tube amp.") ]
            action Jump("vr_collect_item_4")
            
        imagebutton auto "violet/date_1/tree_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.864
            ypos 0.337
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("I'd like to be a tree.") ]
            action Jump("vr_collect_item_2")
            
        if window_crack_v == 0:
            imagebutton auto "violet/date_1/v_window_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A window of the Arctic Fox's house.") ]
                clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A small crack appeared."), SetVariable("window_crack_v", 1) ]
        elif window_crack_v == 1:
            imagebutton auto "violet/date_1/v_window_%s.png":
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
        
            imagebutton idle "v_window_cracked":
                xanchor 0.5
                yanchor 0.5
                xpos 0.053
                ypos 0.351
                hovered [ tooltip.Action("You broke Violet's window.") ]
                action Jump("vr_collect_item_1")
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
    return
    return
    
    label vr_collect_item_1:
    
        if v_item_glass == 1:
        
            show screen violet_1_revisit_objects
        
            scene v_house_front_crack
            with dissolve
        
            n "You search around Violet's house again and find nothing."
        else:
        
            scene v_house_front_crack_blur
            with dissolve
        
            show v_glass_shard at center with dissolve
        
            n "You search around the area of Violet's house and find a shard of glass."
            $ v_item_glass += 1
            $ v_items += 1
        
            hide v_glass_shard at center with dissolve
        
        jump vr1_jump_from_collect
    return
    
    label vr_collect_item_2:
        if v_item_bark == 1:
            show screen violet_1_revisit_objects
            
            n "You search around the tree again and find nothing."
        else:
            
            scene v_house_front_crack_blur
            with dissolve
            
            show v_bark at center with dissolve
            
            n "You search around the tree and find a piece of bark."
            
            $ v_item_bark += 1
            $ v_items += 1
            
            hide v_bark at center with dissolve
            
        jump vr1_jump_from_collect
    return
    
    label vr_collect_item_3:
    
        if v_item_pick == 1:
            show screen violet_1_revisit_objects
        
            n "You search around the guitar again and find nothing."
        else:
        
            scene v_house_front_crack_blur
            with dissolve
        
            show v_pick at center with dissolve
        
            n "You search around the around the guitar and find a pick."
            $ v_item_pick += 1
            $ v_items += 1
        
            hide v_pick at center with dissolve
        
        jump vr1_jump_from_collect 
    return
    
    label vr_collect_item_4:
    
        if v_item_tube == 1:
            show screen violet_1_revisit_objects
        
            n "You search around the amp again and find nothing."
        else:
        
            scene v_house_front_crack_blur
            with dissolve
        
            show v_tube at center with dissolve
        
            n "You search around the around the amp and find a tube."
            $ v_item_tube += 1
            $ v_items += 1
        
            hide v_tube at center with dissolve
        
        jump vr1_jump_from_collect 
    return
    
    label vr_collect_item_5:
    
        if v_item_cable == 1:
            show screen violet_1_revisit_objects
        
            n "You search around the audio cables again and find nothing."
        else:
        
            scene v_house_front_crack_blur
            with dissolve
        
            show v_cable at center with dissolve
        
            n "You search around the around the audio cables and find a gold-tipped cable."
            $ v_item_cable += 1
            $ v_items += 1
        
            hide v_cable at center with dissolve
        
        jump vr1_jump_from_collect 
    return
return

label violet_2:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    show screen violet_2_revisit_objects

    scene v_abandoned_cinema
    with irisout
    
    play music "audio/abandoned.flac" loop fadein 3.0
    
    call screen violet_2_revisit_objects with dissolve

    screen violet_2_revisit_objects:
    
        imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.05
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the map.") ]
                action Jump("outside_map")
        
        imagebutton auto "violet/date_2/v_stage_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.322
            ypos 0.58
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A fancy-looking stage for theatre plays.\nThe curtains are damp with white-ish yellow\nstains and fishy smell.") ]
            clicked [ Play("sound", "audio/stage.flac") ]
            
        imagebutton auto "violet/date_2/v_door_right_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.54
            ypos 0.534
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A door leading to a fishy-smelling room.") ]
            clicked [ Play("sound", "audio/object_falling.flac") ]
            
        imagebutton auto "violet/date_2/v_door_mright_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.628
            ypos 0.53
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A door leading to another room.") ]
            clicked [ Play("sound", "audio/objects_falling.flac") ]
            
        imagebutton auto "violet/date_2/v_bench_back_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.926
            ypos 0.568
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Rows of seats with a suspicious yellow liquid\non them. Does Violet pee on them?!") ]
            clicked [ Play("sound", "audio/rotting_seats.flac") ]
            
        
        imagebutton auto "violet/date_2/v_bench_front_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.681
            ypos 0.85
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Rows of seats with a suspucious yellow liquid\non them. Does Violet pee on them?!") ]
            clicked [ Play("sound", "audio/rotting_seats.flac") ]
        
        
        imagebutton auto "left_arrow_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.8
            ypos 0.452
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet: Having fun exploring? Sorry about the\nsmell, I use this place for alone time. It's a very\nnice sense of freedom and risk.") ]
            action Jump("date_violet_2")
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
    return
return

label violet_3:
    label violet_3_revisit_sex_pc:
    
        $ tooltip = Tooltip("")
    
        stop music fadeout 3.0
    
        pause 3.0
        
        show screen violet_3_revisit_objects
    
        scene v_house_front_sex
        with irisout
    
        play music "audio/nature.flac" loop fadein 3.0
    
        scene v_house_front_sex
        with dissolve
    
        call screen violet_3_revisit_objects with dissolve

        screen violet_3_revisit_objects:
        
            imagebutton auto "close_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.05
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("outside_map")
        
            imagebutton auto "v_door_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.637
                ypos 0.405
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's deep blue front door.") ]
                action Jump("violet_3_revisit_hall")
            
            imagebutton auto "v_gdoor_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.364
                ypos 0.364
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Violet's garage - It's normally open, but\nnot today?") ]
                clicked [ Play("sound", "audio/garage.flac") ]
            
            imagebutton auto "violet/date_1/tree_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.864
                ypos 0.337
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("I'd still like to be a tree.") ]
                clicked [ Play("sound", "audio/tree.flac") ]
            
            if window_crack_v == 0:
                imagebutton auto "violet/date_1/v_window_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.053
                    ypos 0.351
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A window of Violet's house.") ]
                    clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A small crack appeared."), SetVariable("window_crack_v", 1) ]
            elif window_crack_v == 1:
                imagebutton auto "violet/date_1/v_window_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.053
                    ypos 0.351
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A small crack appeared.") ]
                    clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("Another small crack appeared."), SetVariable("window_crack_v", 2) ]
            elif window_crack_v == 2:
                imagebutton auto "violet/date_1/v_window_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.053
                    ypos 0.351
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Another small crack appeared.") ]
                    clicked [ Play("sound", "audio/glass_knock.flac"), tooltip.Action("A bigger crack appeared."), SetVariable("window_crack_v", 3) ]
            elif window_crack_v == 3:
                imagebutton auto "violet/date_1/v_window_%s.png":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.053
                    ypos 0.351
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("A bigger crack appeared.") ]
                    clicked [ Play("sound", "audio/glass_break.flac"), tooltip.Action("You broke the window."), SetVariable("window_crack_v", 4) ]
                
            else:
        
                imagebutton idle "v_window_cracked":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.053
                    ypos 0.351
                    hovered [ tooltip.Action("You broke the window.") ]
                    action tooltip.Action("You broke the window.")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.21
                ypos 0.75
        return
    return
    
    label violet_3_revisit_hall:
    
        show screen violet_3_revisit_inside_objects

        scene v_inside_1
        with dissolve
    
        call screen violet_3_revisit_inside_objects with dissolve

        screen violet_3_revisit_inside_objects:
            imagebutton auto "close_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.05
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the hub.") ]
                action Jump("outside_map")
        
            imagebutton auto "v_inside_door_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.438
                ypos 0.31
                hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Go into the storage room.") ]
                action Jump("violet_3_revisit_storage")
            
            imagebutton auto "v_inside_stairs_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.859
                ypos 0.395
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go upstairs.") ]
                action Jump("violet_3_revisit_landing")
            
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
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.21
                ypos 0.75
        return
    return
    
    label violet_3_revisit_storage:
    
        show screen violet_3_revisit_inside_storage

        scene v_inside_2
        with pixellate

        call screen violet_3_revisit_inside_storage with dissolve

        screen violet_3_revisit_inside_storage:
        
            imagebutton auto "v_inside_boxes_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.54
                ypos 0.5775
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Massive boxes full of various sex toys.") ]
                clicked [ Play("sound", "audio/boxes.flac") ]
            
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.3
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the hall.") ]
                action Jump("violet_3_revisit_hall")
            
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.0179
                ypos 0.4
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go into the kitchen.") ]
                action Jump("violet_3_revisit_kitchen")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.1
                ypos 0.8
        return
    return
    
    label violet_3_revisit_kitchen:
    
        show screen violet_3_revisit_inside_kitchen
    
        scene v_inside_3
        with pixellate

        call screen violet_3_revisit_inside_kitchen with dissolve

        screen violet_3_revisit_inside_kitchen:
        
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
            
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.3
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to storage.") ]
                action Jump("violet_3_revisit_storage")
            
            imagebutton auto "v_inside_kdoor_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.181
                ypos 0.419
                hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Go into the dining room.") ]
                action Jump("violet_3_revisit_dining")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.1
                ypos 0.86
        return
    
        label violet_3_revisit_sink_dialogue:
    
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
    
    label violet_3_revisit_dining:
    
        show screen violet_3_revisit_inside_dining

        scene v_inside_4
        with pixellate

        call screen violet_3_revisit_inside_dining with dissolve

        screen violet_3_revisit_inside_dining:
        
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
        
            imagebutton auto "left_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.0179
                ypos 0.4
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go into the lounge.") ]
                action Jump("date_violet_sex_lounge")
        
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the kitchen.") ]
                action Jump("violet_3_revisit_kitchen")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.1
                ypos 0.1
        return
    return
    
    label violet_3_revisit_lounge:
    
        show screen date_violet_boy_inside_lounge

        scene v_inside_5
        with pixellate

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
        
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the dining room.") ]
                action Jump("violet_3_revisit_dining")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.1
                ypos 0.7
        return
    return
    
    label violet_3_revisit_landing:

        play audio "audio/stairs.flac"
        
        show screen violet_3_revisit_inside_landing
    
        scene v_inside_6
        with pixellate

        call screen violet_3_revisit_inside_landing with dissolve

        screen violet_3_revisit_inside_landing:
        
            imagebutton auto "v_inside_vdoor_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.829
                ypos 0.48
                hovered [ Play("audio", "audio/door_open.flac"), tooltip.Action("Violet's bedroom; it smells like her scent.") ]
                action Jump("violet_3_revisit_room")
            
            imagebutton auto "v_inside_ldoor_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.315
                ypos 0.255
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Looks to be another bedroom, but the door is locked.") ]
                clicked [ Play("audio", "audio/parents_sex.flac") ]
        
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back downstairs.") ]
                action Jump("violet_3_revisit_hall")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.1
                ypos 0.7
        return    
    return
    
    label violet_3_revisit_room:
    
        show screen violet_3_revisit_inside_room
    
        scene v_inside_7
        with pixellate

        call screen violet_3_revisit_inside_room with dissolve

        screen violet_3_revisit_inside_room:
    
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
        
            imagebutton auto "down_arrow_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.9681
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Go back to the landing.") ]
                action Jump("violet_3_revisit_landing")
            
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.02
        return
    return
return

label amber_1:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene a_shop_outside
    with irisout
    
    play music "audio/rain.flac" loop fadein 3.0
    
    label ar1_jump_from_collect:
    
    if window_crack_a == 1:
        scene a_shop_outside_crack
        with dissolve
    else:
        scene a_shop_outside
        with dissolve
    
    call screen amber_1_revisit_objects with dissolve

    screen amber_1_revisit_objects:
    
        imagebutton auto "close_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.9
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the map.") ]
            action Jump("outside_map")
            
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
                action Jump("ar_collect_item_1")
        
        if window_crack_a == 4:
            
            $ window_cracked += 1
                
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

    label ar_collect_item_1:
    
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
        
        jump ar1_jump_from_collect
    return
return

label amber_2:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0

    label ar2_jump_from_collect:
    
    scene a_park
    with dissolve
    
    call screen amber_2_revisit_objects with dissolve

    screen amber_2_revisit_objects:
    
        imagebutton auto "close_%s.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.05
            ypos 0.9
            hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the map.") ]
            action Jump("outside_map")
        
        imagebutton auto "a_park_tree_1_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.818
            ypos 0.372
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("I like being in parks.") ]
            action Jump("ar_collect_item_2")
            
        imagebutton auto "a_park_tree_2_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.179
            ypos 0.297
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Parks are nice.") ]
            action Jump("ar_collect_item_3")
            
        imagebutton auto "a_park_tree_3_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.681
            ypos 0.473
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("The rain makes me happy.") ]
            action Jump("ar_collect_item_4")
            
        imagebutton auto "a_park_tree_4_%s":
            xanchor 0.5
            yanchor 0.5
            xpos 0.171
            ypos 0.353
            hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Do you think the animals can hear us?") ]
            action Jump("ar_collect_item_5")
            
        text tooltip.value outlines [(2, "#fff")]:
            xpos 0.1
            ypos 0.1
            
    return
    
    label ar_collect_item_2:
    
    if a_item_sap == 1:
       n "You search the tree again and find nothing."
    else:
        
        scene a_park_blur
        with dissolve
        
        show a_sap at center with dissolve
        
        n "You search the tree and find a strange gooey liquid."
        $ a_item_sap += 1
        $ a_items += 1
        
    jump ar2_jump_from_collect
    
    return
    
    label ar_collect_item_3:
    
    if a_item_condom == 1:
       n "You search the tree again and find nothing."
    else:
        scene a_park_blur
        with dissolve
        
        show a_condom at center with dissolve
        
        n "You search the tree and find a used condom."
        $ a_item_condom += 1
        $ a_items += 1
        
    jump ar2_jump_from_collect
    
    return
    
    label ar_collect_item_4:
    
    if a_item_egg == 1:
       n "You search the tree again and find nothing."
    else:
        
        scene a_park_blur
        with dissolve
        
        show a_egg at center with dissolve
        
        n "You search the tree and find a bird egg."
        $ a_item_egg += 1
        $ a_items += 1
        
    jump ar2_jump_from_collect
    
    return
    
    label ar_collect_item_5:
    
    if a_item_bark == 1:
       n "You search the tree again and find nothing."
    else:
        scene a_park_blur
        with dissolve
        
        show a_bark at center with dissolve
        
        n "You search the tree and find a piece of bark."
        $ a_item_bark += 1
        $ a_items += 1
        
    jump ar2_jump_from_collect
    
    return   
return

label amber_3:

    jump outside_map

return

label sierra_1:

    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene s_museum_pc
    with irisout
    
    play music "audio/town.flac" loop fadein 3.0
    
    label sr1_jump_from_collect:
    
    scene s_museum_pc
    with dissolve
    
    call screen sierra_1_revisit_objects with dissolve

    screen sierra_1_revisit_objects:
    
        imagebutton auto "close_%s.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.05
                ypos 0.9
                hovered [ Play("sound", "audio/select.flac"), tooltip.Action("Return to the map.") ]
                action Jump("outside_map")
                
        if s_item_leaflet == 0:
            imagebutton auto "s_museum_flyer_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.35
                    ypos 0.80
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Looks like a leaflet from the museum.") ]
                    action Jump("sr_collect_item_1")
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
                    action Jump("sr_collect_item_2")
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
    
    label sr_collect_item_1:
    
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
        
        jump sr1_jump_from_collect
    return
    
    label sr_collect_item_2:
    
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
        
        jump sr1_jump_from_collect
    return

return

