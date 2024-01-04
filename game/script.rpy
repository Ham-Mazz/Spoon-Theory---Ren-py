# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define player = Character("[name]")

init python:
    #To-do list
    #create all the days on ion to randmoly choose a day
    #startDay andthe wireframes as labels
    #create a fuct endDay functions for stats. 

    #initialize some counters
    showerCounter = 0
    laundryCounter = 0
    eatingCounter = 0

    def difficultySet(num):
        spoons = 40 - (num * 5)
        socialPoints = 25 - (num * 5)
        return spoons, socialPoints
    def overspent():
        if spoons <= -5:
            pass #logic to end day and play overspent scene.

        


    def addDailySpoons (currentSpoons, difficultyLevel):
        currentSpoons += 40 - (difficultyLevel * 5)
        return currentSpoons

    

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
    $ difficultyLevel = 0
    define player = Character("[name]")
    define boss = Character("Boss Colton")
    define busDriver = Character("Martha")
    define coworker = Character("Alvaro")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Choose the difficulty"
    menu:

        "Easy":
            $ maxSpoons, socialPoints = difficulty(1)
            $ spoons = maxSpoons
            play music "sample1.mp3" loop
            
        "Normal":
            $ maxSpoons, socialPoints = difficulty(2)
            $ spoons = maxSpoons
            play music "sample1.mp3" loop
 
 
            
        "Hard":
            $ maxSpoons, socialPoints = difficulty(3)
            $ spoons = maxSpoons 
            play music "sample1.mp3" loop

    show screen spoons_and_points

    #jump dayOne
    #jump dayTwo
    #jump dayThree
    #jump dayFour
    #jump dayFive
    #jump daySix
    jump daySeven

    # This ends the game.

    return


label dayOne:
        
    # Day 1 timeline
    "Day 1"
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely. "
    scene large_bedroom
    "Let's see what the day has in store for you."

    scene main_bedroom
    #shower
    "A shower is a great way to start the day."
    "Remember, if you do not shower for 3 days, you will be deducted social points."
    "Would you like to take a shower today?"

    menu:
        "Take shower":
            $ spoons -= 2
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "Skip shower":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Remember, if you do not eat at least 2 times today, you will have less spoons tomorrow."
    "Would you like to make breakfast today?"

    menu:
        "Make and eat breakfast":
            $ spoons -= 3
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            player "That was tasty!"
            $ eatingCounter += 1
        "Skip breakfast":
            "You skip breakfast today. You need to save your spoons for other things today. Your stomach grumbles."

    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, it starts to rain. It makes your body ache."

    #bus
    busDriver "Hello [player]! Heading to work?"
    scene enter_bus

    player "Hi Martha! Sure am."
    "She has been the driver on your route for years and she knows you well"
    "She knows how much energy it takes for you to be here every day, and she always offers you a warm smile for your effort."
    scene sit_on_bus
    $ spoons -= 5
    " You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."
    
    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworkers greet you as you make your way through the building."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, before you forget to, and remember to clock out for it as well."

    "You begrudgingly clock out. Grabbing your small lunch."
    player "Hmm, where should I eat lunch?"
    
    $ eatingCounter += 1

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
    
    #packing up from work
    "You pack up all of your belongings, and begin the trek to the bus stop"
    "Your coworkers wave as you pass by them."
    coworker " Have a good night, [player]!"
    player "You too, [coworker]!"

    #at bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
    
    #bus home event
    player "Ok it's time to go home!"
    scene enter_bus
    $ spoons -= 5
    "(-5 spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
    scene sit_on_bus
    player "hmm I wonder what should I have for dinner"

    $ eatingCounter += 1

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
            $ laundryCounter = 0 
            player "at least I got that out of the way"
        "Watch TV":
            $ laundryCounter += 1
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"
    scene black
    "You go to sleep"
    #End of day 1 

label dayTwo:

    #day 2 timeline
    "DAY 2"

    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    player "It's a New day... yay"

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    player "Hmm Should I take a Shower?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            $ showerCounter = 0
            "You took a cold shower."
            player "that was not enjoyable, but at least I smell adequate"
        "Skip shower":
            $ showerCounter += 1
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today"
    #breakfast event
    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            $ eatingCounter += 1
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
    $ eatingCounter += 1
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
            $ eatingCounter += 1
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
            $ laundryCounter = 0 
        "Watch TV":
            $ laundryCounter += 1
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"
    scene black
    "You go to sleep"
    #day 2 End

label dayThree:

    #day 3 timeline
    "DAY 3"

    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    player "It's a New day... yay"

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    player "Hmm Should I take a Shower?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ spoons -= 2
            $ showerCounter = 0
            "You took a cold shower."
            player "that was not enjoyable, but at least I smell somewhat adequate"
        "Skip shower":
            $ showerCounter += 1
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today, I think food is important for my body, but I am unsure why."
    #breakfast event
    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            $ eatingCounter += 1
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
    $ eatingCounter += 1

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
            $ eatingCounter += 1
        "starve":
            $ spoons -= 2
            "I dont need to eat anyways"

    
    player "it's almost time for me to go to sleep"

    player "should I do laundry?"
    # be productive event
    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            $ laundryCounter = 0 
            player "at least I got that out of the way"
        "Watch TV":
            $ laundryCounter += 1
            player "I will just chill tongiht and watch TV"
    scene large_bedroom
    player "Time To head to bed!"

    "You go to sleep"
    #day 3 end

label dayFour: 
    #start day 4
    "DAY 4"
    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    player "It's a New day, and I don't have work today, thank god."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    player "Hmm Should I take a Shower, or just stay in bed a little longer?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ showerCounter = 0
            $ spoons -= 2
            "You took a cold shower, that's one way to start a morning"
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
        "Skip shower":
            $ showerCounter += 1
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today, I think food is important for my body, but I am unsure why."
    #breakfast event
    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            $ eatingCounter += 1
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
            $ eatingCounter += 1
            #chore or book option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    $ laundryCounter = 0 
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Read a book for the night":
                    $ laundryCounter += 1
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
            $ eatingCounter += 1
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
                    $ eatingCounter += 1
                "starve":
                    "I dont need to eat anyways"

            #chore or TV option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    $ laundryCounter = 0 
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Watch TV":
                    $ laundryCounter += 1
                    "You watch 3 movies and pass out in the middle of the second, so much for a movie night"
    #end of day four
            
label dayFive: 
    #start day 5
    "DAY 5"
    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    player "It's a New day, and I don't have work today, thank god."

    player "Hmm Should I take a Shower, or just stay in bed a little longer?"
    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ showerCounter = 0
            $ spoons -= 2
            "You took a cold shower, that's one way to start a morning"
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
        "Skip shower":
            $ showerCounter += 1
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today, I think food is important for my body, but I am unsure why."
    #breakfast event
    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            $ eatingCounter += 1
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
            $ eatingCounter += 1
            #chore or book option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    $ laundryCounter = 0 
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Read a book for the night":
                    $ laundryCounter += 1
                    "You open and begin to read, the Night of our stars"
                    "the main character is attempting to jailbreak to his lover from the local jail"
                    "he succeeds and they live together happily in a beachouse, watching the stars soar over them during the night"
                    "after finishing the book, you head to bed"
            #hopefully jump to end day
        "go out with friends and do stuff":
            #go out pathway, start by taking the bus
            "you get ready, putting on a cute dress and doing your makeup"
            $ spoons -= 12
            $ socialPoints =+ 3;
            "you take the bus to the resturant, which is on the other side of the city"
            scene enter_bus
            $ spoons -= 5
            "you arrive at the cozy little diner, greeting your friends with a hug and laughter, you missed them"
            scene large_diner
            "you guys sit down, order food and begin to eat, laughter is heard from your table all night"
            $ spoons -= 3
            $ eatingCounter += 1
            "one of your friends covers the bill"

            #keep going out with friends to movies, or go home
            menu:
                "Go home for the day":
                    "afterwards you head back home"
                "go to the movies with friends":
                    $ spoons -= 5
                    $ socialPoints
                    "you watch barbie with friends, you are kenough"
                    "afterwards you head back home, tired and sick on sugar and salt"

            #both pathways result in going home, dinner event then chore event, so back to here
            
            #make dinner event
            menu:   
                "Make dinner":
                    $ spoons -= 3 
                    $ eatingCounter += 1
                    "Food is good"
                "starve":
                    "I dont need to eat anyways"

            #chore or TV option
            menu:
                "Do chores for the rest of the night":
                    #do chores
                    $ spoons -= 3
                    $ laundryCounter = 0 
                    "clean wax, idk do shit"
                    "after you finishing cleaning and doing stuff, you go to bed"
                "Watch TV":
                    $ laundryCounter += 1
                    "You watch 3 movies and pass out in the middle of the second, so much for a movie night"
    #end of day five

label daySix:
    "DAY 6"
    #start of day 6

    "(Wake Up)"
    scene large_bedroom
    "You roll outta bed and hit the hard floor"

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    player "It's a New day, and I don't have work today, thank god."

    #shower event
    menu:
        "Take shower (-2 spoons)":
            $ showerCounter = 0
            $ spoons -= 2
            "You took a cold shower, that's one way to start a morning"
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
        "Skip shower":
            $ showerCounter += 1
            "You did not take a shower, you smell and look horrid."

    "you start to feel hungry, what do you want to do"
    player "hmm Should I starve today, I think food is important for my body, but I am unsure why."
    #breakfast event
    menu:
        "Make and eat breakfast (-3 spoons)":
            $ spoons -= 3
            $ eatingCounter += 1
            "you made (and ate) a scrumptious meal"
            player "That was tasty!"
        "Skip breakfast":
            "you skip breakfest, lets hope you don't get too hungry"

    #go out or stay home (start of branching for day 6)
    menu:
        "Stay home and have a relaxing day":
            #stay at home path
            "you choose to stay home and catch up on things that need to be done"
            "you clean the kitchen, and grab some leftovers to eat and finished those off. You should learn to cook better"
            "now that you ate, find something to do for the rest of the night"
            $ eatingCounter += 1
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
        "Go our with your friends for the night":
            #pathway that sends you to go with friends, upper two branches on figma wireframe
            $ spoons -= 12
            $ socialPoints += 3
            "go our with your friends, get ready and stuff"

            #take the bus to resturant

            $ spoons -= 5
            "you take the bus to the resturant, going with your freidns and chatting on the way there"

            #eat lunch at resturant
            $ eatingCounter += 1
            $ spoons -= 3
            "you eat lunch with your friends group, you have an amazing time doing so"

            #invite friend home or go home alone and single (I ship characters I don't actually know)
            menu:
                "Invite Friend back to your place":
                    $ spoons -=7
                    $ socialPoints += 2
                    "you invite your friend over for dinner as well, they agree so you go back to your place"
                    "now that your friend is here, do you choose to"
                    menu:
                        "be responisble and wash dishes, and do other chores":
                            $ laundryCounter = 0 
                            "you do chores after you get home, she hangs out for a while but heads home after a little bit"
                        "Hang out and do a movie marathon":
                            $ spoons -= 1
                            $ laundryCounter += 1 
                            $ socialPoints += 1
                            "you guys do a movie marathon, watching 5 movies before she passes out on the couch"
                "Go home alone":
                    $ spoons -=5
                    "you head home alone"
                    #make dinner event
                    menu:   
                        "Make dinner":
                            $ spoons -= 3 
                            $ eatingCounter += 1
                            "Food is good"
                        "starve":
                            "I dont need to eat anyways"

                    #chore or TV option
                    menu:
                        "Do chores for the rest of the night":
                            #do chores
                            $ spoons -= 3
                            $ laundryCounter = 0 
                            "clean wax, idk do shit"
                            "after you finishing cleaning and doing stuff, you go to bed"
                        "Watch TV":
                            $ socialPoints += 1
                            "You watch 3 movies and pass out in the middle of the second, so much for a movie night"
    #this should be the end of day 6

label daySeven:
    "DAY 7"
    # Day 7 timeline
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely. "
    scene large_bedroom
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    scene main_bedroom
    #shower
    "A shower is a great way to start the day."
    "Remember, if you do not shower for 3 days, you will be deducted social points."
    "Would you like to take a shower today?"

    player "Hmm Should I take a Shower?"

    menu:
        "Take shower":
            $ spoons -= 2
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "Skip shower":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1
    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Remember, if you do not eat at least 2 times today, you will have less spoons tomorrow."
    "Would you like to make breakfast today?"

    menu:
        "Make and eat breakfast":
            $ spoons -= 3
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            player "That was tasty!"
            $ eatingCounter += 1
        "Skip breakfast":
            "You skip breakfast today. You need to save your spoons for other things today. Your stomach grumbles."

    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, it starts to rain. It makes your body ache."
    #bus
    $ spoons -= 5
    "The bus driver, Martha, greets you as you board. She has been the driver on your route for years and she knows you well."
    scene enter_bus
    "She knows how much energy it takes for you to be here every day, and she always offers you a warm smile for your effort."
    scene sit_on_bus
    "You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    "You arrive at work and sit down in your small, cramped, dusty cubicle. You already wish the work day was over."
    "..."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, and remember that you have a proposal to present to the board afterwards"

    "You begrudgingly clock out for lunch. Grabbing your measly meal."
    player "Hmm, where should I eat lunch?"
    #lunch event
    $ eatingCounter += 1
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

    #bus home event
    player "Ok it's time to go home!"
    "You take the bus home (-5 spoons)"
    $ spoons -= 5
    scene enter_bus
    "You find an empty spot and take a seat, feeling the bus shake as it goes along"
    scene sit_on_bus
    player "hmm I wonder what should I have for dinner"
    
    $ eatingCounter += 1

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
            menu:
                "Invite friend over and eat together? (-2 spoons +2 social points)":
                    $ spoons -= 2
                    $ socialPoints += 2
                    "You had a good time and and enjoyed a fufilling meal with your friend!"
                "Eat takeout alone":
                    player "hmm that was a fast, greasy meal"
    #lunadry event      
    menu:            
        "Do laundry (-3 spoons)":
            $ spoons -= 3
            $ laundryCounter = 0 
            player "at least I got that out of the way"
        "Watch TV":
            $ laundryCounter += 1
            player "I will just chill tongiht and watch TV"
    
    player "Time To head to bed!"
    scene black
    "You go to sleep"
    #End of day 7

label dayEight:
    "DAY 8"
    #Day 8 timeline
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely. "
    scene large_bedroom
    "Let's see what the day has in store for you."

    
    scene main_bedroom
    #shower
    "A shower is a great way to start the day."
    "Remember, if you do not shower for 3 days, you will be deducted social points."
    "Would you like to take a shower today?"

    menu:
        "Take shower":
            $ spoons -= 2
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "Skip shower":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Remember, if you do not eat at least 2 times today, you will have less spoons tomorrow."
    "Would you like to make breakfast today?"

    menu:
        "Make and eat breakfast":
            $ spoons -= 3
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            player "That was tasty!"
            $ eatingCounter += 1
        "Skip breakfast":
            "You skip breakfast today. You need to save your spoons for other things today. Your stomach grumbles."
    
    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, it starts to rain. It makes your body ache."

    #bus
    busDriver "Hello [player]! Heading to work?"
    scene enter_bus

    player "Hi Martha! Sure am."
    "She has been the driver on your route for years and she knows you well"
    "She knows how much energy it takes for you to be here every day, and she always offers you a warm smile for your effort."
    scene sit_on_bus
    $ spoons -= 5
    " You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    
    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworkers greet you as you make your way through the building."

    "Eventually, you hear a knock on the wall of your cubicle. It's your boss Colton."

    boss "Hey , [player], take your lunch, before you forget to, and remember to clock out for it as well."

    "You begrudgingly clock out. Grabbing your small lunch."
    player "Hmm, where should I eat lunch?"
    
    #lunch option
    $ eatingCounter += 1

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
    

