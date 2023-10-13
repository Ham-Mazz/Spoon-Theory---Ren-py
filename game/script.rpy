# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("[name]")

init python:
    def difficulty(num):
        spoons = 40 - num * 5
        social_points = 25 - num * 5
        return spoons, social_points

screen spoons_and_points:
    hbox:
        xalign 0.05
        yalign 0.05
        spacing 20

        text "Spoons: [spoons]" size 20
        text "Social Points: [social_points]" size 20
# The game starts here.

label start:
    $ name = renpy.input("What's your name?")
    $ name = name.strip()
    define e = Character("[name]")
    define b = Character("Boss Colton")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Choose the difficulty"
    menu:


        "Easy":
            $ spoons, social_points = difficulty(1) 
            
        "Normal":
            $ spoons, social_points = difficulty(2) 
            
        "Hard":
            $ spoons, social_points = difficulty(3) 

    show screen spoons_and_points

    


    "(Wake Up)"
    "You rise from your bed"

    e "It's a New day!."

    e "Hmm Should I take a Shower?"

    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a nice, warm, relaxing shower."
            e "ahh that was refershing!"
        "Skip shower":
            "You did not take a shower, you smell horrid."

    "you start to feel hungry, what do you want to do"
    e "hmm Should I make breakfast"

    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            "you made a scrumptious meal"
            e "That was tasty!"
        "Skip breakfast":
            "you skip breakfest, lets hope you don't get too hungry"

    "Time to get to Work!"

    e "I have to take the bus to work (-5 spoons)"
    $ spoons -= 5

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    b "Hey , [e], take your lunch, before you forget to, and remember to clock out for it as well."

    "You begrudgingly clock out. Grabbing your small lunch."
    e "Hmm, where should I eat lunch?"

    menu:
        "Eat with your co-worker (-5 spoons)":
            $ spoons -= 5
            "You sit down with (character), and having a amazing lunch break. You talk with (character) about (stuff)."
        "Eat in your cubicle (-2 Social Points)":
            $ social_points -= 2
            "You sit back down in your desk, open your small packed lunch and start eating, alone."
    

    menu:

        "Finish all your work for the day":
            $ spoons -= 10
            "After lunch, you focus and manage to get all your work finished somehow."
            
        "Take a break, resulting in you being unable to finish your work":
            $ spoons -= 5
            $ social_points -= 2
            "After lunch, you scroll through tiktoks and decide that the work on your desk can be done tommorow. Your coworkers are not impressed with the amount of work you left behind"
    
    e "Ok it's time to go home!"
    "You take the bus home (-5 spoons)"
    $ spoons -= 5
    e "hmm I wonder what should I have for dinner"

    menu:
        "Stop for groceries (-5 spoons)":
            $ spoons -= 5 
            jump groceries

        "Stop for takeout (-2 spoons)":
            $ spoons -= 2
            "That was a quick dinner!"
            
            

    menu groceries:
        "Invite friend over and cook dinner? (-2 spoons +2 social points)":
            $ spoons -= 2
            $ social_points += 2
            "You had a good time and and enjoyed a fufilling meal with your friend!"
        "Eat dinner alone":
            e "hmm that was a good meal!"
    
    e "it's almost bed time"

    e "should I do laundry?"

    menu:            
            "Do laundry (-3 spoons)":
                $ spoons -= 3
                e "at least I got that out of the way"
            "Watch TV":
                e "I will just chill tongiht and watch TV"
    
    e "Time To head to bed!"

    "You go to sleep"







        



    # This ends the game.

    return
