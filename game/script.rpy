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
    define bestFriend = Character("Raneem")

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
    #jump daySeven
    jump dayEight

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
        "Yes, take a shower (-2 Spoons)":
            $ spoons -= 2
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No, skip shower  (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Remember, if you do not eat at least 2 times today, you will have less spoons tomorrow."
    "Would you like to make breakfast today?"

    menu:
        "Yes, make and eat breakfast (-3 Spoons)":
            $ spoons -= 3
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            player "That was tasty!"
            $ eatingCounter += 1
        "No, Skip breakfast (- Hunger)":
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
    "You sit in your usual seat and watch the scenery go by. You are already feeling fatigued. (-5 spoons)"
    
    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworker, Alvaro, greets you as you make your way through the building."
    #should Alvaro say something?

    #at your desk
    "You sit down and begin your work for the day"
    "You are finishing an important project with the rest of your team"

    #lunch

    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room."

    "Would you like to eat lunch with your co-workers?"   
    menu:
        "Yes, eat with your co-workers (-5 spoons)":
            $ eatingCounter += 1
            $ spoons -= 5
            "You join your co-workers in the break room. Alvaro tells you all about his daughter's dance recital."
            #more Alvaro lore?
            "You have fun, but being around this many people drains you of energy."
        "No, keep working (-2 Social Points, Hunger)":
            "You tell them that you are going to skip lunch today to continue working on the project. "
            $ socialPoints -= 2
            "They look disappointed. Alvaro frowns at you. "
            "Your stomach grumbles."
    
    #working
    "You have a lot of work to do today, and the team is relying on you to finish it. "
    "Whatever work you do not complete will have to be picked up by your co-workers. "
    "Would you like to finish all of your work today?"
    
    menu:
        "Yes, Finish all your work for the day (-10 spoons)":
            $ spoons -= 10
            "You finish all of your work for the day, and submit it to your boss, Colton. "
            boss "Great work today, [player]."
            player "Thanks Colton, I'll see you later."
            
        "No, take a break which results in you being unable to finish your work (-5 spoons, -2 social points) ":
            $ spoons -= 5
            $ socialPoints -= 2
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
    
    #packing up from work
    "You pack up all of your belongings, and begin the trek to the bus stop"
    "Your coworkers wave as you pass by them."
    coworker " Have a good night, [player]!"
    player "You too, [coworker]!"

    #at bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
    "She greets you with a warm smile. "
    busDriver "Are you ready to go home, hon?"
    player "Absolutely."
    
    #bus home event
    scene enter_bus
    $ spoons -= 5
    "(-5 spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
    scene sit_on_bus
    player "hmm I wonder what should I have for dinner"

    #dinner

    "The grocery store near your house is having a sale on bread."
    "Would you like to stop for groceries to make a hearty meal tonight"
    menu:
        "Yes, Stop for groceries (-5 spoons)":
            $ spoons -= 5 
            scene large_grocery_store
            "You buy fresh groceries. The effort leaves you feeling drained."
            scene large_bedroom
            "When you get home, you debate on whether or not you should invite your friend, Raneem, over for dinner."\
            "Do you invite Raneem over and cook for her?"
            menu:
                "Yes, Invite friend over. (-2 spoons +2 social points)":
                    $ eatingCounter += 1
                    $ socialPoints += 2
                    "You call Raneem, and she comes over while you cook."
                    $ spoons -= 2
                    "You share a delicious tater tot hotdish, but the effort of cooking leaves you feeling exhausted."
                    bestFriend "Thank you for the meal, [player]! I know how tiring cooking can be, and I appreciate you inviting me over."
                    player "Any time. I'm glad you liked it!"
                "No (-hunger)":
                    "You decide that you do not have the energy to cook for yourself tonight, let alone someone else."
                    "You skip dinner"

        "Stop for takeout (-2 spoons)":
            $ eatingCounter += 1
            $ spoons -= 2
            "Going to the store sounds exhausting, but you still need to eat."
            scene large_diner
            "You stop for takeout at the restaurant next to your house."

    #luandry
    "Despite it having been a long day, you notice that you need to do laundry."
    "Remember, if you do not do the laundry at least twice a week, you will be deducted social points."
    "Would you like to do your laundry?"
    menu:            
        "Yes, Do laundry (-3 spoons)":
            $ spoons -= 3
            $ laundryCounter = 0 
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets. "
        "No, Watch TV":
            $ laundryCounter += 1
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
    
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    scene black
    "You get into bed, close your eyes, and fall asleep."
    #End of day 1 

label dayTwo:

    #day 2 timeline
    "DAY 2"
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."
    $ spoons = addDailySpoons(spoons, difficultyLevel)
    scene large_bedroom
    "Let's see what the day has in store for you."
    
    #shower
    "A shower is a great way to start the day."
    "Would you like to take a shower today?"

    menu:
        "Yes, take a shower (-2 Spoons)":
            $ spoons -= 2
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No, skip shower  (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Would you like to make breakfast today?"

    menu:
        "Yes (-3 Spoons)":
            $ spoons -= 3
            "You make and enjoy scrambled eggs. They're a little burnt, but you don't mind. "
            "The effort of cooking leaves you feeling drained."
            $ eatingCounter += 1
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    #bus stop
    "You leave the house, making sure to lock the door behind you. "
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, you watch the sun rise."
    
    #on the bus
    busDriver "Hello [player] How are you today?"
    scene enter_bus
    player "I'm alright [busDriver]. How are you"
    busDriver "Same as always, my dear. Same as always. "
    $ spoons -= 5
    scene sit_on_bus
    "(-5 spoons) You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk. "
    "Your coworkers greet you as you make your way through the building."

    #at your desk
    "You sit down and begin your work for the day."
    "Your boss, Colton, approaches your desk."
    boss "Hey [player], are you ready for the investor presentation today?"
    player "Sure am, just finishing up that last couple things."
    boss "Thank you. I'm counting on you, [player]."

    #lunch

    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room"
    
    "Would you like to eat lunch with your co-workers?"

    menu:
        "Yes (-5 spoons)":
            $ spoons -= 5
            $ eatingCounter += 1
            "You join your co-workers in the break room. You tell them about a new book you have been reading."
            "You have fun, but being around this many people drains you of energy."
        "No (-1 social point, - Hunger)":
            $ socialPoints -= 1
            "You tell them that you are going to skip lunch today to continue working on the presentation. "
            "They look disappointed, but understand."
            "Your stomach grumbles."
    
    #work proposal event
    "It's almost time for you to give the presentation to the company's investors."
    "You know this will take a lot of your energy for the day, but your team is counting on you."
    "One of your co-workers, Alvaro, could take over and present for you, but you know this project better than anyone else."
    "Will you present to the investors?"

    menu:
        "Yes (-6 spoons)":
            $ spoons -= 6
            "You finish all of your work for the day, and submit it to your boss."
            $ socialPoints += 3
        "No (-3 social points)":
            player "Alvaro, I'm so sorry to ask at the last minute, but can you take over the investor presentation?"
            coworker "I mean, I can. But why can't you do it"
            player "I just... I don't really have the energy for it today."
            $ socialPoints -= 3
            "Your whole team looks disappointed."
            "[boss] frowns as you return to your desk."
            "[bestFriend] delivers the presentation, but stumbles a few times."

    #working
    "You have a lot of work to do today, and the team is relying on you to finish it. "
    "Whatever work you do not complete will have to be picked up by your co-workers. "
    "Would you like to finish all of your work today?"

    #finish work event
    
    menu:
        "Yes, Finish all your work for the day (-10 spoons)":
            $ spoons -= 10
            "You finish all of your work for the day, and submit it to your boss, Colton. "
        "No, take a break which results in you being unable to finish your work (-5 spoons, -2 social points) ":
            $ spoons -= 5
            $ socialPoints -= 2
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
    
    #pack up from work

    "You pack up all of your belongings, and begin the trek to the bus stop"
    "Your coworkers wave as you pass by them."
    coworker " Have a good night, [player]!"
    player "You too, [coworker]!"

    #at the bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."

    #on the bus
    scene enter_bus
    "You exchange nods with her, and collapse into your usual seat."
    scene sit_on_bus
    "(-5 spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
    $ spoons -= 5
    "Watching the scenery helps clear your head after such a long day at work."

    #make dinner event
    "By the time you return home, your stomach is grumbling."
    "You should have enough food in your pantry to whip something up for dinner."
    "Would you like to make dinner?"
    menu:
        "Yes, make dinner (-3 spoons)":
            $ spoons -= 3 
            "You make pasta with the homemade spaghetti sauce your mom brought over the last time she visited."
            "The spaghetti is almost as good as when she makes it for you."
            $ eatingCounter += 1
        "No (- Hunger)":
            "You skip dinner today. You are too tired to make anything tonight anyways."
            "Your stomach grumbles."
    #laundry
    "Despite it having been a long day, you notice that you need to do laundry. "
    "Would you like to do your laundry?"
    menu:            
        "Yes, do laundry (-3 spoons)":
            $ spoons -= 3
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
            $ laundryCounter = 0 
        "No, watch TV instead (-laundry)":
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break. "
            "They are playing reruns of cartoons you used to watch as a child."
            "It brings a smile to your face."
            $ laundryCounter += 1

    #bedtime
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    scene black
    "You get into bed, close your eyes, and fall asleep."
    
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
        "Catch up on some work":
            "You catch up on some work"
            "you failed to kick ass, but you made a good impression"
            $ spoons -= 4
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

    #make dinner event
    menu:
        "Make dinner":
            $ spoons -= 3 
            "Food is good"
            $ eatingCounter += 1
        "starve":
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
    #day 8 End

label dayNine: 
    #starting day nine
    "DAY 9"

    #wake up
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

    #activity, start of branching

    "after your meal, you try to find something to do with your little free time, before you start your busy day. What do you wish to do today?"

    menu:

        "Read a book":
            #read a book path
            "plus 2 something?"
            $ spoons += 2

            #go out with friends

            "after you start reading your book, getting engrossed into many chapter of your long, fantasy novel. You get a call from one of your friends"
            #add friend on phone here
            player "Sure! I would love to come out and do that with you. Give me a little bit to get ready and i'll meet in you there in about an hour?"
            #responding friend dialouge

            "you then proceed get ready, putting on some nice clothes and doing your makeup"
            $ spoons -= 15
            $ socialPoints += 3

            #bus on upper branch
            "you take the bus to the resturant, which is on the other side of the city"
            scene enter_bus
            $ spoons -= 5

            #eat lunch with friends
            scene large_diner
            $ spoons -= 7
            "you arrive at the diner, and enjoy the chime as the door opens"
            "your friends greet you, you all order and have a barrel of laughs"
            $ eatingCounter += 1

            #say goodbye
            "after hours of talking, spilling tea and spending time with your friends, you all unfornatuately have to head home"
            "you head back to the bus stop"

            #bus home event
            player "Ok it's time to go home!"
            scene enter_bus
            $ spoons -= 5
            "(-5 spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
            scene sit_on_bus

            #dinner option
            player "hmm I wonder what should I have for dinner"
            menu:
                "Make dinner":
                    $ spoons -= 5 
                    "Food is good"
                    $ eatingCounter += 1
                "starve":
                    $ spoons -= 2
                    "I dont need to eat anyways"

        "do the laundry":
            #do the laundry path
            $ spoons -= 3

            #stay at home 
            "you choose to stay home and just take a day to lie down and relax"
            $ socialPoints -= 6
            "you clean the kitchen, and grab some leftovers to eat and finished those off. You should learn to cook better, maybe you wouldn't have to eat others leftovers all the time"
            "now that you ate, find something to do for the rest of the night"
            $ eatingCounter += 1

            #activity on lower branch

            menu:
                "THIS IS A DUPLICATION ACTION":
                    ""
                    $ spoons -= 3
                "Read a book":
                    "You decide to keep unwinding for tonight. SO you cuddle into your bed after grabbing Pride & Prejudice, and Sense & Sensiability from Janue Austen"
                    "You enjoy the warmth and soft lighting of your bedroom, eventually your eyes start to get heavy after finishing the first book you picked up"
                    "you pass out 4 chapters into Sense & Sensiability"
            #should jump to end of day

        