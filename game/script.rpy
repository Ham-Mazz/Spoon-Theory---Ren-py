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
    #jump dayTwo
    #jump dayThree
    jump dayFour

    # This ends the game.

    return


label dayOne:
        
    # Day 1 timeline

    "(Wake Up)"
    "You rise from your bed"
    scene large_bedroom

    player "It's a New day!."

    scene main_bedroom

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

    player "I have to take the bus to work (-5 spoons)"
    $ spoons -= 5
    scene enter_bus
    "You find an empty spot and take a sit, feeling the bus shake as it goes along"
    scene sit_on_bus

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
    scene enter_bus
    "You find an empty spot and take a seat, feeling the bus shake as it goes along"
    scene sit_on_bus
    player "hmm I wonder what should I have for dinner"

    menu:
        "Stop for groceries (-5 spoons)":
            $ spoons -= 5 
            "lets grab a this, and a that"
            scene large_grocery_store
            menu:
                "Invite friend over and cook dinner? (-2 spoons +2 social points)":
                    $ spoons -= 2
                    $ socialPoints += 2
                    "You had a good time and and enjoyed a fufilling meal with your friend!"
                "Eat dinner alone":
                    player "hmm that was a good meal!"

        "Stop for takeout (-2 spoons)":
            $ spoons -= 2
            scene large_diner
            "That was a quick dinner!"
    
    player "it's almost bed time"

    player "should I do laundry?"

    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            player "at least I got that out of the way"
        "Watch TV":
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"
    scene black
    "You go to sleep"
    #End of day 1 

label dayTwo:

    #day 2 timeline

    "(Wake Up)"
    scene large_bedroom
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
    scene enter_bus
    "You find an empty spot and take a sit, feeling the bus shake as it goes along"
    scene sit_on_bus
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
    scene enter_bus
    "You find an empty spot and take a sit, feeling the bus shake as it goes along"
    scene sit_on_bus
    "You hate this bus"
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
    scene black
    "You go to sleep"
    #day 2 End

label dayThree:

    #day 3 timeline

    "(Wake Up)"
    scene large_bedroom
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
    scene enter_bus
    $ spoons -= 5
    player "The bus is so overpriced now"
    "Someone is in your normal seat, you have to stand today"
    $ spoons -= 1

    #overflow work event
    "someone in your group at work has been slacking off, and now there is a bunch of wor that the rest of the group needs to pick up"
    menu:
        "help them out":
            $ spoons -= 8
            $ socialPoints += 4
            "yeah we can finish this, no problem"
        "say you have other responseibilites":
            "sorry guys I got a document that needs to be finished today"
            $ socialPoints -= 4

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    scene black

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
    scene enter_bus
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
    scene large_bedroom
    player "Time To head to bed!"

    "You go to sleep"
    #day 3 end

label dayFour: 
    #start day 4

    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    player "It's a New day, and I don't have work today, thank god."

    player "Hmm Should I take a Shower, or just stay in bed a little longer?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a cold shower, that's one way to start a morning"
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
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

    #go out or stay home (start of branching for day 4)
    menu:
        "Stay home and have a relaxing day":
            #stay at home path
            "you choose to stay home and catch up on things that need to be done"
            "you clean the kitchen, and grab some leftovers to eat and finished those off. You should learn to cook better"
            "now that you ate, find something to do for the rest of the night"
            #chore or book option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Read a book for the night":
                    "You open and begin to read, the Night of our stars"
                    "the main character is attempting to jailbreak to his lover from the local jail"
                    "he succeeds and they live together happily in a beachouse, watching the stars soar over them during the night"
                    "after finishing the book, you head to bed"
            #hopefully jump to end day
        "go out with friends and do stuff":
            #go out pathway, start by taking the bus
            "you get ready, putting on a cute dress and doing your makeup"
            $ spoons -= 15
            "you take the bus to the resturant, which is on the other side of the city"
            scene enter_bus
            $ spoons -= 5
            "you arrive at the cozy little diner, greeting your friends with a hug and laughter, you missed them"
            scene large_diner
            "you guys sit down, order food and begin to eat, laughter is heard from your table all night"
            $ spoons -= 5
            "one of your friends covers the bill"

            #keep going out with friends, or go home
            menu:
                "Go home for the day":
                    "afterwards you head back home"
                "go to the park with friends":
                    $ spoons -= 7
                    $ socialPoints
                    "you head to the park with your friends"
                    "afterwards you head back home"

            #both pathways result in going home, dinner event then chore event, so back to here
            
            #make dinner event
            menu:   
                "Make dinner":
                    $ spoons -= 3 
                    "Food is good"
                "starve":
                    "I dont need to eat anyways"

            #chore or TV option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Watch TV":
                    "You watch 3 movies and pass out in the middle of the second, so much for a movie night"
    #end of day four
            
label dayFive: 
    #start day 5

    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    player "It's a New day, and I don't have work today, thank god."

    player "Hmm Should I take a Shower, or just stay in bed a little longer?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            "You took a cold shower, that's one way to start a morning"
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
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

    #go out or stay home (start of branching for day 5)
    menu:
        "Stay home and have a relaxing day":
            #stay at home path
            "you choose to stay home and catch up on things that need to be done"
            "you clean the kitchen, and grab some leftovers to eat and finished those off. You should learn to cook better"
            "now that you ate, find something to do for the rest of the night"
            #chore or book option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Read a book for the night":
                    "You open and begin to read, the Night of our stars"
                    "the main character is attempting to jailbreak to his lover from the local jail"
                    "he succeeds and they live together happily in a beachouse, watching the stars soar over them during the night"
                    "after finishing the book, you head to bed"
            #hopefully jump to end day
        "go out with friends and do stuff":
            #go out pathway, start by taking the bus
            "you get ready, putting on a cute dress and doing your makeup"
            $ spoons -= 15
            "you take the bus to the resturant, which is on the other side of the city"
            scene enter_bus
            $ spoons -= 5
            "you arrive at the cozy little diner, greeting your friends with a hug and laughter, you missed them"
            scene large_diner
            "you guys sit down, order food and begin to eat, laughter is heard from your table all night"
            $ spoons -= 5
            "one of your friends covers the bill"

            #keep going out with friends to movies, or go home
            menu:
                "Go home for the day":
                    "afterwards you head back home"
                "go to the park with friends":
                    $ spoons -= 5
                    $ socialPoints
                    "you watch barbie with friends, you are kenough"
                    "afterwards you head back home, tired and sick on sugar and salt"

            #both pathways result in going home, dinner event then chore event, so back to here
            
            #make dinner event
            menu:   
                "Make dinner":
                    $ spoons -= 3 
                    "Food is good"
                "starve":
                    "I dont need to eat anyways"

            #chore or TV option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Watch TV":
                    "You watch 3 movies and pass out in the middle of the second, so much for a movie night"
    #end of day five