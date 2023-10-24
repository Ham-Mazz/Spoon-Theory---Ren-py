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
        socialPoints = 25 - (num * 5)
        return spoons, socialPoints

screen spoons_and_points:
    hbox:
        xalign 0.05
        yalign 0.05
        spacing 20

        text "Spoons: [spoons]" size 20
        text "Social Points: [socialPoints]" size 20

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
            $ spoons, socialPoints = difficulty(1) 
            
        "Normal":
            $ spoons, socialPoints = difficulty(2) 
            
        "Hard":
            $ spoons, socialPoints = difficulty(3) 

    show screen spoons_and_points

    jump dayOne
    jump dayTwo
    jump dayThree

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
            $ socialPoints -= 2
            "You sit back down in your desk, open your small packed lunch and start eating, alone."
    
    menu:

        "Finish all your work for the day":
            $ spoons -= 10
            "After lunch, you focus and manage to get all your work finished somehow."
            
        "Take a break, resulting in you being unable to finish your work":
            $ spoons -= 5
            $ socialPoints -= 2
            "After lunch, you scroll through tiktoks and decide that the work on your desk can be done tommorow. Your coworkers are not impressed with the amount of work you left behind"
    
    player "Ok it's time to go home!"
    "You take the bus home (-5 spoons)"
    $ spoons -= 5
    player "hmm I wonder what should I have for dinner"

    menu:
        "Stop for groceries (-5 spoons)":
            $ spoons -= 5 
            jump groceriesDayOne

        "Stop for takeout (-2 spoons)":
            $ spoons -= 2
            "That was a quick dinner!"

    menu groceriesDayOne:
        "Invite friend over and cook dinner? (-2 spoons +2 social points)":
            $ spoons -= 2
            $ socialPoints += 2
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

label dayTwo:

    #day 2 timeline

    "(Wake Up)"
    "You roll outta bed and hit the hard floor"

    player "It's a New day... yay"

    player "Hmm Should I take a Shower?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a cold shower."
            player "that was not enjoyable, but at least I smell adequate"
        "Skip shower":
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today"
    #breakfast event
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
    player "The bus is so overpriced now"

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, and remember that you have a proposal to present to the board afterwards"

    "You begrudgingly clock out for lunch. Grabbing your measly meal."
    player "Hmm, where should I eat lunch?"
    #lunch event
    menu:
        "Eat with your co-worker (-5 spoons)":
            $ spoons -= 5
            "You sit down with (character), and having a amazing lunch break. You talk with (character) about (stuff)."
        "Eat in your cubicle (-2 Social Points)":
            $ socialPoints -= 2
            "You sit back down in your desk, open your small packed lunch and start eating, alone."
    
    #work proposal event

    menu:
        "Present proposal to the board":
            "You show up the corner office, ready to KICK ASS"
            "you failed to kick ass, but you made a good impression"
            $ spoons -= 6
            $ socialPoints += 3
        "Ask co-worker to present proposal":
            "character says - you want me to present this blind? are you kidding, god damn it"
            $ socialPoints -= 3
            "your co-worker does the event, but she is furious about it"

    #finish work event
    menu:

        "Finish all your work for the day":
            $ spoons -= 10
            "After lunch, you focus and manage to get all your work finished somehow."
            
        "Take a break, resulting in you being unable to finish your work":
            $ spoons -= 5
            $ socialPoints -= 2
            "After lunch, you scroll through tiktoks and decide that the work on your desk can be done tommorow. Your coworkers are not impressed with the amount of work you left behind"
    
    player "Ok it's time to go home!"
    "You take the bus home (-5 spoons)"
    $ spoons -= 5
    player "hmm I wonder what should I have for dinner"

    #make dinner event
    menu:
        "Make dinner":
            $ spoons -= 5 
            "Food is good"
            

        "starve":
            $ spoons -= 2
            "I dont need to eat anyways"

    
    player "it's almost time for me to go to sleep"

    player "should I do laundry?"
    # be productive event
    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            player "at least I got that out of the way"
        "Watch TV":
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"

    "You go to sleep"
    #day 2 End



label dayThree:

    #day 3 timeline

    "(Wake Up)"
    "You roll outta bed and hit the hard floor"

    player "It's a New day... yay"

    player "Hmm Should I take a Shower?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a cold shower."
            player "that was not enjoyable, but at least I smell somewhat adequate"
        "Skip shower":
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today, I think food is important for my body, but I am unsure why."
    #breakfast event
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
    player "The bus is so overpriced now"

    #overflow work event

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, and remember that you have a proposal to present to the board afterwards"

    "You begrudgingly clock out for lunch. Grabbing your measly meal."
    player "Hmm, where should I eat lunch?"
    #lunch event
    menu:
        "Eat with your co-worker (-5 spoons)":
            $ spoons -= 5
            "You sit down with (character), and having a amazing lunch break. You talk with (character) about (stuff)."
        "Eat in your cubicle (-2 Social Points)":
            $ social_points -= 2
            "You sit back down in your desk, open your small packed lunch and start eating, alone."

    #finish work event
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

    #make dinner event
    menu:
        "Make dinner":
            $ spoons -= 5 
            "Food is good"
            

        "starve":
            $ spoons -= 2
            "I dont need to eat anyways"

    
    player "it's almost time for me to go to sleep"

    player "should I do laundry?"
    # be productive event
    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            player "at least I got that out of the way"
        "Watch TV":
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"

    "You go to sleep"
    #day 2 timeline