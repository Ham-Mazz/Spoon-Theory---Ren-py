# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define player = Character("[name]")

init python:
    #To-do list
    #create all the days on the wireframes as labels
    #create a fuction to randmoly choose a day
    #startDay and endDay functions for stats.  
    def difficulty(num):
        spoons = 40 - (num * 5)
        social_points = 25 - (num * 5)
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
    define player = Character("[name]")
    define boss = Character("Boss Colton")

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

    jump dayOne
    


    # This ends the game.

    return


label dayOne:
        
    # Day 1 timeline

    "(Wake Up)"
    "You rise from your bed"

    player "It's a New day!."

    player "Hmm Should I take a Shower?"

    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a nice, warm, relaxing shower."
            player "ahh that was refershing!"
        "Skip shower":
            "You did not take a shower, you smell horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I make breakfast"

    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            "you made a scrumptious meal"
            player "That was tasty!"
        "Skip breakfast":
            "you skip breakfest, lets hope you don't get too hungry"

    "Time to get to Work!"

    player "I have to take the bus to work (-5 spoons)"
    $ spoons -= 5

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, before you forget to, and remember to clock out for it as well."

    "You begrudgingly clock out. Grabbing your small lunch."
    player "Hmm, where should I eat lunch?"

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
    
    player "Ok it's time to go home!"
    "You take the bus home (-5 spoons)"
    $ spoons -= 5
    player "hmm I wonder what should I have for dinner"

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
            player "hmm that was a good meal!"
    
    player "it's almost bed time"

    player "should I do laundry?"

    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            player "at least I got that out of the way"
        "Watch TV":
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"

    "You go to sleep"
    #End of day 1 

