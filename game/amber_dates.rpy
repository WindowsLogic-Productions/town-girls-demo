# Amber's opening scene.

label date_amber_opening:

    $ tooltip = Tooltip("")
    
    $ _game_menu_screen = None
    $ quick_menu = False
    hide screen bodystats
    hide screen dates
    hide screen dates_dark
    
    call loading from _call_loading_2
    
    stop music fadeout 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    play music "audio/opening.flac" loop fadein 3.0
    
    $ renpy.pause(3.0, hard=True)
    
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    
    if amber == 1:
        scene amber_pre-opening
        with dissolve
    
        n "When going shopping at the local supermarket, you see a tabby cat and decide to search her up online."
        
        scene amber_base_site
        with irisout
    else:
        scene amber_base_site
        with irisout
    
    label posts_ap1:
    
        call screen date_violet_opening_objects_ap1 with dissolve

        screen date_violet_opening_objects_ap1:
        
            if amber == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_amber_timecheck")
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
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("main_hub_screen")
            
            imagebutton auto "251016_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_lit_a1")
                
            imagebutton auto "010117_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_lit_a2")
                
            imagebutton auto "270717_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a1")
                
            imagebutton auto "170818_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_lit_a3")
                
            imagebutton auto "300419_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a2")
                
            imagebutton auto "up_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.87
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll up.") ]
                action Jump("posts_ap2")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label posts_ap2:
    
        call screen date_amber_opening_objects_ap2 with dissolve

        screen date_amber_opening_objects_ap2:
        
            if amber == 1:
                imagebutton auto "logout_%s":
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.979
                    ypos 0.018
                    hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Log out and proceed to date.") ]
                    action Jump("date_amber_timecheck")
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
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("main_hub_screen")
            
            imagebutton auto "250820_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.92
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a3")
                
            imagebutton auto "080920_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.81
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a4")
                
            imagebutton auto "171021_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.7
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a6")
                
            imagebutton auto "100222_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.59
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a7")
                
            imagebutton auto "060422_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.631
                ypos 0.48
                hovered [ Play("audio", "audio/select.flac") ]
                action Jump("online_pic_a8")
                
            imagebutton auto "down_arrow_%s":
                xanchor 0.5
                yanchor 0.5
                xpos 0.23
                ypos 0.95
                hovered [ Play("audio", "audio/select.flac"), tooltip.Action("Scroll down.") ]
                action Jump("posts_ap1")
                
            text tooltip.value outlines [(2, "#fff")]:
                xpos 0.05
                ypos 0.9
            
        return
    return
    
    label online_lit_a1:
    
        scene a_start_0
        with dissolve
        
        n "A Sudden Shock - Published: 25th October 2016 - Last Edited: 22nd May 2022"
    
        l "Chapter 1 - Wet Dreaming"
    
        l "It was morning and Amy was just waking up after a wet dream about a boy she liked. She could feel the soggy sheets up against her like a raging bull wanting to widdle her noodle. She couldn’t stay in bed all day though, so she got up and got ready for a long day of school."
    
        l "She hated school for the most part, especially the teachers, but there was one redeeming quality of school, that was Phillipe the rabbit. Amy was throbbing so much wetness for this rabbit that every time she saw him, she couldn’t contain herself."
    
        l "Amy didn’t like to admit it, but she would secretly go into the girl’s toilets at lunch and masturbate over Phillipe because she knew that she could imagine caressing his massive rabbit peen."
    
        l "After Amy was done masturbating, she would leave a note of how many times she came in a constant battle with the other girls who used the toilets for masturbation."
    
        l "At least that was when girls didn’t shove tons of dirty period stuff down the toilets to clog them, and the smell of period blood didn’t fill the air like toxic waste."
        
        scene amber_base_site
        with dissolve
        
        jump posts_ap1
    return
    
    label online_lit_a2:
    
        scene a_start_0
        with dissolve
        
        n "My Little Ka-hony: Fucking is Magic - Published: 1st January 2017 - Last Edited: 17th April 2022"
    
        l "Chapter 1 - The New Pony In Town"
    
        l "The sun rises in Ponkyville as TwinkleSpry wakes up to find that last night's 'Cyder Party' went off without a hitch; AppSack in the corner with Footershit sleeping with her nose in her coochie, Raindash with a strap-on still attached,"
    
        l "and Rarer with a letter to Molester asking her to come over and fuck her silly shoved in Pinkledick's tight arsehole."
    
        l "TwinkleSpry got out of bed and shouted, 'GET UP AND OUT OF MY HOUSE! FRIENDSHIP ISN'T MAGICAL IF I DON'T GET MY MORNING MASTURBATION SESSION!' as her pussy was dripping wet from the dream, she had last night."
    
        l "AppSack immediately woke up and found a horse in her cunt, 'What in the hay is Footershit doing up my hole!?'"
    
        l "Footershit woke up just after and breathed in AppSack's fresh vagina, 'Oh my goodness...' Raindash woke up before AppSack and couldn't stop talking about how big her dick was."
    
        l "Pinkledick woke up to wonder why her rear hole was so scrunchy. Rarer woke up as soon as Raindash flew into her with her strap on attached and tried fucking Rarer while she was still asleep, 'How dare you try that while I'm asleep Raindash!'"
    
        l "TwinkleSpry's 'friends' all walked out of her castle to get on with their daily activities, while TwinkleSpry touched her tight horse pussy and thought about Shiner's fat cock inside her tight hole, slowly moving up and down, enough to make her cum."
    
        l "After TwinkleSpry had squirted all over Spine while he was still asleep, she went outside to smoke a fat blunt and for good measure, touched herself some more in public and ended up squirting on Lie and Bon who were just walking by at the time, they were not impressed by this."
    
        l "TwinkleSpry realised that she didn't have her morning piss yet, so she just let it out all over the floor on which she was sitting, it felt good to get all that 'Cyder' out of her little hole, even though it did make her cheeks wet."
    
        l "A new pony that had just arrived in Ponyville walked up to TwinkleSpry and asked, 'Aren't you the princess of friendship? Why are you smoking weed and sat in a puddle?'"
    
        l "TwinkleSpry said, high as fuck, 'I used to be the princess of friendship until Molester said I wasn't being fair to my friends when I locked them in my sex dungeon and got them all pregnant from a stallion called Biggie.'"
    
        l "The new pony said, 'Where I'm from, we learn about how sex is magical and how we can use it to get what we want, do you want me to teach you about it?'"
    
        l "TwinkleSpry moaned, 'But I've read every book about sex, how can I learn more?'"
    
        l "The new pony kissed TwinkleSpry on the cheek and showed TwinkleSpry her parts, her vagina was the right tightness with the perfect amount of wetness dripping out, no bacon sag and very clean, her arsehole was the perfect shade of pink, looked untouched and also equally as clean as her pussy."
    
        l "TwinkleSpry's jaw dropped and she let the new pony in her castle for some 'deep learning' exercises."
    
        l "Chapter 2 - A Whole New Sexy World"

        l "TwinkleSpry took the new pony down to her sex dungeon so she could see the equipment TwinkleSpry used to practice the act of sexual encounters."
    
        l "The new pony exclaimed, 'This is good, but what you really need is a sex machine' as she whips one out in front of TwinkleSpry and begins to show her how to use it."
    
        l "The sex machine had a golden horse cock on the end of it and was a shiny black colour which gleamed in the dim purple lighting of TwinkleSpry's sex dungeon."
    
        l "'I'll go first to show you how it's done', the new pony said excitedly."
    
        l "She bent over on the machine and let it fuck her, before realising she really needed to go, so asked TwinkleSpry, 'Can I use your bathroom afterwards?'"
    
        l "But it was too late, the new pony tried not to let her waste out all over TwinkleSpry's sex dungeon floor but soaked the carpet with liquid every time the machine fucked her until she soaked the carpet in a sea of piss and cum."
    
        l "TwinkleSpry was very annoyed and this and shouted, 'Get the fuck out of my castle and go ruin someone else's sex dungeon, or I'll fill you up with my unspeakable liquids you dirty whore.'"
    
        l "The new pony ran out of the castle to find Biggie standing there with a massive boner, he asked, 'Are you okay there? Something happen? I can make it all better.'"
    
        l "The new pony accepted Biggie's offer and got fucked silly until her perfect pussy was filled to the brim with sticky, white sauce."
    
        l "TwinkleSpry thought about it and wondered if she was a bit too harsh on the new pony, she was only trying to help TwinkleSpry get laid with Molester, which was her ultimate goal as taking Molester's virginity would stop her from ever raising the sun again, leaving Equestia in a black darkness."
    
        l "After getting her vagina beaten with a Biggie sack, the new pony walked towards Rarer's clothes shop, her pussy still dripping with Biggie's cum."
    
        l "She walked into the shop, still dripping with jizz, as Rarer noticed herm ran up to her and started licking the cum out of her pussy, knowing it was possibly Biggie's."
    
        l "The new pony was shocked by this encounter but accepted it, 'I guess you're a white pony because you like the sauce', the new pony moaned deeply while getting licked."
    
        l "After Rarer was done licking, she stuck her horn inside and started slowly moving up and down, making sure to touch the new pony's womb with her tip."
    
        l "'Ahh~ You're so horny miss', moaned the new pony. Rarer softly said, 'I'm only being generous darling, and making you not drip Biggie's syrup all over my shop floor is the least I can do.'"
    
        l "'Giving you a reverse horn job was an extra I was feeling like giving you since I've never seen you before darling~.'"
    
        l "'Ahh~ I'm going to cum~', panted the new pony as Rarer exclaimed, 'Do it, bitch! Do it all over my shop floor you dirty whore!' The new pony came all over Rarer's face and on her floor, leaving a puddle of sticky, yet sweet liquid."
    
        l "'Now let's take you back to TwinkleSpry so she can get some help with her evil plan!', excitedly said Rarer."
    
        l "Chapter 3 - Me(a)ting The Main Siz"
    
        l "The new pony and Rarer returned to TwinkleSpry's castle, and to Rarer's surprise, all of her friends were there waiting outside along with TwinkleSpry."
    
        l "Rarer asked, 'Why are you all here?' Everypony excitedly proclaimed, 'We wanted to learn about the new pony's ways of sexual conquest!'"
    
        l "Rarer noticed that her friend's pussies were dripping, making a big puddle of horse wetness on the floor, except for TwinkleSpry, who was dripping wetness on Spine's head."
    
        l "Everypony walked into the castle, down into TwinkleSpry's sex dungeon, leaving a trail of pussy juice on the floor."
    
        l "The dungeon was still drenched in a sea of piss and cum, so TwinkleSpry and all her 'friends' grabbed some straws and drank every last drop until the floor wasn't a river of sweet, sticky horse juices."
    
        l "The new pony watched this... getting more and more horny by the minute... until... she started gushing with wetness."
    
        l "Once the Main Six were done drinking, TwinkleSpry asked, 'Is everything okay? Do you want me to help with your urges?' The new pony looked at TwinkleSpry longingly until she said, 'I think we should empty ourselves before we learn, TwinkleSpry!'"
    
        l "TwinkleSpry seductively looked at the new pony, then proceeded to walk to nearest corner of the dungeon where Spine was sitting, and emptied herself all over him."
    
        l "Spine was used to being used as a dungeon toilet for TwinkleSpry and all of her friends, though he didn't like how he would have to wash himself afterwards every time."
    
        l "TwinkleSpry's 'friends' proceeded to follow TwinkleSpry and all pissed hard on Spines body, making sure to cover every last inch until he was soaked in clit juice."
    
        l "The new pony approached Spine after the others were done, but instead of urinating on him, the new pony proceeded to give him a taste of her pussy by fucking him hard."
    
        l "The shape of Spine's dragon cock was making the new pony feel euphoric, but she tried to contain herself so she could feel Spine's cum fill her pussy up."
    
        l "The Main Six watched as the new pony rode Spine and moments later, the new pony moaned loudly, 'Ahh~ He's cumming inside me!'"
    
        l "Spine had lost his virginity to a pony he had never met in his life and the Main Six wanted a slice of that pie, especially TwinkleSpry, who had been holding in her feelings since day one."
    
        l "Spine was turned into a sex attraction with the Main Six fucking him back-to-back until he died from too much sex."
    
        l "TwinkleSpry was happy that she had sex with her slave, but also sad because he wouldn't be able to do her bidding anymore."
    
        l "Rarer decided to give Spine a proper send-off, by proceeding to masturbate and cum on Spine's corpse, moaning, 'I always loved you!'"
    
        l "After Rarer was done, AppSack stood over Spine's corpse and said, 'I never really liked Spine, most of us here thought he was annoying, it is my great honour to show what I thought about him after all these years.'"
    
        l "The new pony exclaimed, 'The only thing I knew about him, was he was nice to fuck.' AppSack took a stance and shat all over Spine's corpse, washing it with her piss afterwards. Rarer cried while the rest of the Main Six cheered, 'No more annoyance!'"
    
        l "After that intense experience, they all fell asleep together in the sex dungeon."
    
        l "Chapter 4 - Learning Begins"
    
        l "The next morning, the new pony woke up to the sound of moaning, TwinkleSpry was touching herself in her sleep and mumbling about a pony called Shiner;"
    
        l "TwinkleSpry's 'friends' had gone home after last night's debauchery, so the new pony decided to rub her pussy on TwinkleSpry's face to wake her up, but it didn't work."
    
        l "She kept fucking TwinkleSpry's face until she ended up squirting all over her."
    
        l "TwinkleSpry woke up from this intense wetness and noticed a cute, pretty pink vagina in front of her, she licked the wet pussy dry."
    
        l "The new pony asked, 'Shall we get started with learning how to fuck?' TwinkleSpry politely nodded as she took her big, hard morning piss on the carpet."
    
        l "The dungeon was now smelling rancid, with death, cum, shit and piss all over the walls and floor, this odour turned TwinkleSpry on even more and she was ready to learn how to fuck hard."
    
        l "The new pony first showed TwinkleSpry how to put on a strap-on so she could fuck the new pony and get used to being dominant towards Molester."
    
        l "The new pony explained, 'This is a special type of strap-on that's filled with real stallion sperm, when you fuck me hard enough, it will explode inside me, using your mare cum to wash the sperm inside me!'"
    
        l "TwinkleSpry smiled at this and slid the rubber dong into the new pony as she moaned with joy, 'Ahhh~ That's perfect, now move in and out like you mean it!'"
    
        l "TwinkleSpry started moving in and out slowly, then got faster and faster as she became more confident, her wetness running down her legs as she humped the new pony."
    
        l "The new pony screamed, 'Yeah~ That's it Twinkle babe, fuck me until I cum!'"
    
        l "TwinkleSpry went deeper and deeper until she was hitting the new pony's womb, after a while of deeply fucking her, TwinkleSpry let out a massive moan and came into the new pony's tight pussy, filling it to the brim with stallion sperm."
    
        l "The new pony got off the strap-on, turned around and looked at TwinkleSpry, kissing her on the lips, 'You did great. I'll teach you more tomorrow!' The new pony left TwinkleSpry's castle and went to do something else."
    
        l "TwinkleSpry couldn't stop thinking about what exciting things she would get up to with the new pony the next day, she began touching herself, thinking about the new pony and how sexy she was with her pretty pink clit and perfect body."
    
        l "TwinkleSpry began feeling super horny over the new pony and ended up squirting her female cum all over her bedroom walls, leaving a sticky residue behind, 'I'll clean that up later...', said TwinkleSpry reluctantly, as the dungeon hadn't been cleaned since a few days ago when she met the new pony."
    
        l "TwinkleSpry decided to smoke a fat blunt and piss the bed to forget about her troubles, before falling asleep in her puddle of yellow."
    
        l "After a few hours, TwinkleSpry woke up to find that she was soggy with her own juices, she didn't care that she smelt like a toilet or that there were her own juices dripping from her fur."
    
        l "She went to make herself something to eat because fucking the new pony made her hungry."
    
        l "She walked into the castle's parlour to find Pinkledick making a cake which smelt very odd. TwinkleSpry asked, 'Why are you here making a cake?'"
    
        l "Pinkledick explained, 'Oh, I fucked up Sugarcube Corner's kitchen so badly that I got kicked out, so I came here so I could make something sweet for myself.' TwinkleSpry had a look at the cake mixture, it was oddly red with a yellow tint, 'What's in this cake?', TwinkleSpry asked."
    
        l "Pinkledick proceeded to grab TwinkleSpry's head and pulled her down so her mouth was on Pinkledick's pussy."
    
        l "TwinkleSpry gave Pinkle's pussy a good wiff before slowly starting to lick it because she could and she was still horny from earlier, while she was licking, her nose got covered in something red, it was period blood."
    
        l "Slowly TwinkleSpry started to realise what the cake mixture had in it and TwinkleSpry was disgusted at Pinkledick, for even TwinkleSpry would not go this far."
    
        l "'GET THE FUCK OUT OF MY CASTLE OR I'LL SHIT IN YOUR PUSSY!', screamed TwinkleSpry as she was very angry about what Pinkledick had done."
    
        l "After that ordeal, TwinkleSpry flopped on her soaking wet bed and fell asleep once more until morning."
        
        scene amber_base_site
        with dissolve
        
        jump posts_ap1
    return
    
    label online_pic_a1:
    
        call screen online_pic_a1 with dissolve
        
        screen online_pic_a1:
        
            imagebutton idle "a_start_3":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap1")
            
        return
    return
    
    label online_lit_a3:
    
        scene a_start_0
        with pixellate
    
        n "Confessions - Published: 17th August 2018"
    
        l "Chapter 1"
    
        l "This is a list of confessions that I'll try and keep up to date so you can learn more about what I'm into and what I like."
    
        scene a_start_4
        with pixellate
    
        l "Confession #1"
    
        l "I go outside without wearing anything except a long hoodie to cover my bits. If I need to bend over, I let people in public to see my noodle. This also allows me to pee while I'm walking!!! x3"
    
        scene a_start_2
        with pixellate
    
        l "Confession #2"
    
        l "I rub my taint on bus seats so the next person who sits there, sits in my discharge/wetness..."
    
        scene a_start_2p
        with pixellate
    
        l "(maybe pee if I'm feeling extra naughty)! ;)"
    
        scene a_start_5
        with pixellate
    
        l "Confession #3"
    
        l "The thought of being caught doing something naughty makes me super wet just thinking about it! OwO"
    
        scene a_start_6
        with pixellate
    
        l "Confession #4"
    
        l "I think my boss likes me considering he doesn't care if I walk into work completely naked. He's kinda cute too!!! :D"
        
        scene amber_base_site
        with dissolve
        
        jump posts_ap1
    return
    
    label online_pic_a2:
    
        call screen online_pic_a2 with dissolve
        
        screen online_pic_a2:
        
            imagebutton idle "a_start_1":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap1")
            
        return
    return
    
    label online_pic_a3:
    
        call screen online_pic_a3 with dissolve
        
        screen online_pic_a3:
        
            imagebutton idle "a_start_6":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
    
    label online_pic_a4:
    
        call screen online_pic_a4 with dissolve
        
        screen online_pic_a4:
        
            imagebutton idle "a1-c":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
    
    label online_pic_a5:
    
        call screen online_pic_a5 with dissolve
        
        screen online_pic_a5:
        
            imagebutton idle "a_start_2e":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
    
    label online_pic_a6:
    
        call screen online_pic_a6 with dissolve
        
        screen online_pic_a6:
        
            imagebutton idle "a2-c":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
    
    label online_pic_a7:
    
        call screen online_pic_a7 with dissolve
        
        screen online_pic_a7:
        
            imagebutton idle "a_start_1":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
    
    label online_pic_a8:
    
        call screen online_pic_a8 with dissolve
        
        screen online_pic_a8:
        
            imagebutton idle "a_start_7":
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.5
                action Jump("posts_ap2")
            
        return
    return
return

# Check time of game to determine if dates are possible.

label date_amber_timecheck:

    hide screen bodystats
    hide screen dates
    hide screen dates_dark

    call loading from _call_loading_3
    
    $ _game_menu_screen = None
    $ quick_menu = False
    
    $ renpy.pause(3.0, hard=True)

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
    
    play music "audio/amber_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_blur
    with dissolve
    
    n "Amber is currently working, do you want to advance time?"
        
    menu:
        "Go to sleep":
        
            n "You sleep until it's evening."
            
            $ time = 3
            $ bladder = 2
                
            jump main_hub_screen
                
        "Go to the shop Amber works at and stalk her":
                
            n "You go to the shop where Amber works to stalk her."
                
            $ nightstalk = renpy.random.randint(1, 4)
                
            if nightstalk == 1:
                
                n "You find Amber bent over half naked in front of the shop tills with her arse pressed against the shop window."
                
                scene a_working
                with pixellate
            elif nightstalk == 2:
            
                n "You find Amber bent over half naked in front of the shop tills with her arse pressed against the shop window. As soon as you see her, she starts squirting on the glass."
                
                scene a_working_squirt
                with pixellate
            elif nightstalk == 3:
            
                n "You find Amber bent over half naked in front of the shop tills with her arse pressed against the shop window. She's been there a while as there's pussy juice all over the window."
            
                scene a_working_wetpuddle
                with pixellate
            else:
                
                n "You find Amber bent over half naked in front of the shop tills with her arse pressed against the shop window. As soon as you see her, she starts spraying on the glass."
                
                scene a_working_spray
                with pixellate
                
            pause 120.0
                
            $ time = 3
            $ bladder = 2
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

label date_amber_timechecked_asleep:

    stop music fadeout 3.0
    
    pause 3.0
    
    play music "audio/amber_stalking.flac" loop fadein 3.0
    
    pause 3.0
    
    scene map_night_blur
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
                
                n "You find Amber sleeping and cuddling a massive pony plushie upside down whilst rubbing her vagina on it's chin."
                
                scene a_sleeping
                with pixellate
            elif nightstalk == 2:
            
                n "You find Amber sleeping and cuddling a massive pony plushie upside down whilst rubbing her vagina on it's chin. As soon as you see her, she gives a long pining meow and starts spraying on it."
            
                scene a_sleeping_spray
                with pixellate
            elif nightstalk == 3:
            
                n "You find Amber sleeping and cuddling a massive pony plushie upside down whilst rubbing her vagina on it's chin. As soon as you see her, she lets out a big moan and starts squirting all over it."
            
                scene a_sleeping_squirting
                with pixellate
            else:
                
                n "You find Amber sleeping and cuddling a massive pony plushie upside down whilst rubbing her vagina on it's chin. The plushie's chin looks like it's completely soaked with cat piss."
                
                scene a_sleeping_soaked
                with pixellate
            
            pause 120.0
                
            $ time = 1
            
            stop music fadeout 3.0
    
            pause 3.0
        
            jump main_hub_screen
return

# Amber first date.

label date_amber_1_pc:

    $ achievement.grant("first")
    
    $ tooltip = Tooltip("")
    
    stop music fadeout 3.0
    
    pause 3.0
    
    scene a_shop_outside
    with irisout
    
    show screen bodystats
    
    play music "audio/rain.flac" loop fadein 3.0
    
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
    
    play music "audio/amber_theme_date_1.flac" loop fadein 3.0
    
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
            
            a "I- I have to travel home on the bus every day… I- I like r- rubbing my lower bits into the bus seats s- so they get wet with my f- fluids… D- Depending on i- if I need the t- toilet after work, I- I s- spray on the seat I’m sitting on."
            
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
        
        n "You can now revisit this location via the map."
    
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
        
        n "You can now revisit this location via the map."
    
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
        play music "audio/amber_theme_date_3.flac" fadein 3.0

        if gender == 0:
            scene a_sex_scene_cum
            with flash
        if gender == 1:
            scene a_sex_scene_squirt
            with flash
            
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
            
            scene amber_ending_cum
            with dissolve
        
            n "Amber gets up, pushes you out of the way and runs out of the shop naked and crying with cum dripping down her legs."
        elif gender == 1:
            scene a_sex_scene_squirt_neutral
            with dissolve
            
            a "I- I didn't think I liked girls until I met you."
            
            a "B- But now that I've had sex with you, I'm happy it was a girl who I did it with first time."
            
            scene amber_ending_wet
            with dissolve
        
            n "Amber gets up and runs home naked, happy about the encounter she just had."
        
        $ renpy.block_rollback()
    
        stop music fadeout 3.0
        
        play audio "audio/date_success.flac"
        if gender == 0:
            n "Date Success?"
        elif gender == 1:
            n "Date Success!"
    
        if gender == 0:
            n "You can now revisit this location via the map."
        elif gender == 1:
            n "You can now revisit this location via the map."
           
        scene blank
        with irisout
            
        $ renpy.movie_cutscene("video/ya_got_amber.webm")
        
        $ achievement.grant("amber_3_success")
    
        jump a_variable_update
    else:
        n "If you see this, you have found a bug. Please report asap."
        
    label a_variable_update:
    
        $ dating += 1
        $ amber += 1
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