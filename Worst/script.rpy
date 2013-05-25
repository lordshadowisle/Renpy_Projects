# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    $ menu = nvl_menu
    
# Declare characters used by this game.
    define e = Character('', kind=nvl, color="#c8ffc8")
    $ narrator = NVLCharacter(None, kind=nvl)

# The game starts here.
label start:
    
    # Interaction Elements
    $ flag_research = False
    $ flag_stats = False
    $ flag_interaction = False
    $ flag_plot = False
    $ int_research = 0
    $ int_stats = 0
    $ int_interaction = 0
    $ int_plot = 0
    # Result Elements
    $ int_time = 0
    $ int_personal = 0
    $ int_relationship = 0
    $ int_story = 0
    $ int_aboutHer = 0
    # Intermediate Elements
    $ flag_otf_personal = False 

label mainLoop:

    if int_time < 4:
        $ int_time += 1
        "What do I do next?"
        menu:
            "Research" if flag_research == False:
                nvl clear
                e "I will research." 
                $ flag_research = True
                jump storyEngine
            "Increase stats" if flag_stats == False:
                nvl clear
                e "I will increase my stats."
                $ flag_stats = True
                jump storyEngine
            "Increase interaction" if flag_interaction == False:
                nvl clear
                e "I will increase interaction."
                $ flag_interaction = True
                jump storyEngine
            "Advance plot" if flag_plot == False:
                nvl clear
                e "I will advance the plot."
                $ flag_plot = True
                jump storyEngine
        return        
    else:
        e "Testing is done."
    return
    
label storyEngine:
    # Update and display results directly stemming from interaction elements
    # highest in, to prevent race conditions.
    if flag_research == True:
        if int_research < 2:
                $ int_research += 1
                $ int_aboutHer += 1
                # Hate python lack of switch statement
                if int_research == 1:
                        "I spied on her today. She likes to tuck her hair behind her left ear using one hand."
                if int_research == 2:
                        "I spied on her again. She doesn't seem to like sports in general."
    
    if flag_interaction == True:
        if int_interaction < 3:
            $ int_interaction += 1
            $ int_relationship += 1
            if int_interaction == 1:
                "I tried talking to her today while walking to school. She seemed surprised, but managed a simple reply."
            if int_interaction == 2:
                "I created opportunities to pair with her during school. If it seemed all too obvious, it didn't reflect on her countenance." 
            if int_interaction == 3:
                "I had lunch with her today. She seemed pleased to have company for lunch."
        if int_research == 2:
                "Knowing her secret, I decided that perhaps it could be used to attract her attention. She played down her interest, but was quite obviously amused."
                $ int_relationship += 1
                $ int_research = 3
        # some text checks to display current relationship status.
        
    if flag_stats == True:
        $ int_personal += 1
        $ int_stats += 1
        if int_personal == 1:
            "I started to pay a bit more attention to the lectures. At home, I did some simple exercises to improve my fitness."
        if int_personal == 2:
            "I began a jogging routine, and stuck to it except for extreme weather. I started sleeping early regularly as well, which improved my concentration for class."
        if int_personal == 3:
            "I scored an A."
        if int_personal == 4:
            "I volunteered for success."
        if (int_relationship >= 3) and (flag_otf_personal == False):
            "She decided to help me with my paper, improving its quality."
            $ flag_otf_personal = True
    # Then update and display results from mutual interactions

    
    jump mainLoop
