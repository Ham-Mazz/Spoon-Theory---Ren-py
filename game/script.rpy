# The script of the game goes in this file.

define audio.dayMusic = "audio/day-placeholder.mp3"

define player = Character("[name]")

init python:
    #To-do list
    
    import random

    #initialize some counters
    showerCounter = 0
    laundryCounter = 0
    eatingCounter = 0
    dayCounter = 0
    difficultyLevel = 0
    
    #list containing all days

    dayList = [2,3,4,5,6,7]

    def difficultySet(num):
        difficultyLevel = num
        spoons = 40 - (difficultyLevel * 5)
        socialPoints = 25 - (difficultyLevel * 5)
        return spoons, socialPoints, difficultyLevel

    def addDailySpoons (currentSpoons, difficultyLevel):
        currentSpoons += 40 - (difficultyLevel * 5)
        return currentSpoons

    def getDifficultlyLevel():
        return difficultyLevel

    def getSpoons():
        return spoons

    def changeSpoons(amount):
        currentSpoons = getSpoons()
        newSpoons = (currentSpoons - amount)

        return newSpoons

    #def getSocialPoints():
    #    return socialPoints

    #def changeSocialPoints(amount):
    #    currentSocialPoints = getSpoons()
    #    newSocialPoints = (currentSocialPoints + amount)
    #
    #   return newSocialPoints


screen spoons_and_points:
    hbox:
        xalign 0.05
        yalign 0.05
        spacing 20

        text "Spoons: [spoons]" size 20
        text "Social Points: [socialPoints]" size 20

# The game starts here.

label start:

    screen characterSelect:
        pass
        #nothing here yet

    $ name = renpy.input("What's your name?")
    $ name = name.strip()
    $ difficultyLevel = 0
    define player = Character("[name]", image = "player")
    define boss = Character("Colton", image = "boss")
    define busDriver = Character("Martha", image = "busDrive")
    define coworker = Character("Alvaro", image = "coworker")
    define bestFriend = Character("Raneem", image = "bestFriend")

    image side player = "placeholder.jpeg"
    #image player state2 = "placeholder.jpeg"
    image side boss = "placeholder.jpeg"
    #image boss state2 = "placeholder.jpeg"

    image boss state1 = "placeholder.jpeg"
    image boss state2 = "placeholder.jpeg"

    image side busDriver = "placeholder.jpeg"

    image side coworker = "placeholder.jpeg"
    #image coworker state2 = "placeholder.jpeg"

    image side bestFriend = "placeholder.jpeg"
    #image bestFriend state2 = "placeholder.jpeg"
   
    "Choose the difficulty"
    menu:

        "Easy":
            $ maxSpoons, socialPoints, difficultyLevel = difficultySet(1)
            $ spoons = maxSpoons
            play music "sample1.mp3" loop
            
        "Normal":
            $ maxSpoons, socialPoints, difficultyLevel = difficultySet(2)
            $ spoons = maxSpoons
            play music "sample1.mp3" loop
 
        "Hard":
            $ maxSpoons, socialPoints, difficultyLevel = difficultySet(3)
            $ spoons = maxSpoons 
            play music "sample1.mp3" loop

    show screen spoons_and_points

    jump newDay
    #jump dayTwo
    #jump dayThree
    #jump dayFour
    #jump dayFive
    #jump daySix
    #jump daySeven
    #jump dayEight

    # This ends the game.

    return

label dayOne:
    play music dayMusic loop    
    # Day 1 timeline
    "Day 1"
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."

    scene large_bedroom
    with fade
    "Let's see what the day has in store for you."

    scene main_bedroom
    with dissolve
    #shower
    "A shower is a great way to start the day."
    "Remember, if you do not shower for 3 days, you will be deducted social points."

    menu:
        "Would you like to take a shower today?"

        "Yes, take a shower (-2 Spoons)":
            $ spoons = changeSpoons(2)
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No, skip shower  (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    if spoons < -5:
        jump overspentSpoons

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."
    "Remember, if you do not eat at least 2 times today, you will have less spoons tomorrow."
    #"Would you like to make breakfast today?"

    menu:
        "Would you like to make breakfast today?"

        "Yes, make and eat breakfast (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            $ eatingCounter += 1
        "No, Skip breakfast (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today. Your stomach grumbles."

    if spoons < -5:
        jump overspentSpoons

    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, it starts to rain. It makes your body ache."

    #bus
    busDriver "Hello [player]! Heading to work?"
    scene enter_bus
    with dissolve

    player "Hi [busDriver]! Sure am."
    "She has been the driver on your route for years and she knows you well"
    "She knows how much energy it takes for you to be here every day, and she always offers you a warm smile for your effort."
    scene sit_on_bus
    with dissolve
    $ spoons = changeSpoons(5)
    "You sit in your usual seat and watch the scenery go by. You are already feeling fatigued. (-5 Spoons)"

    if spoons < -5:
        jump overspentSpoons
    
    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworker, [coworker], greets you as you make your way through the building."

    #at your desk
    "You sit down and begin your work for the day"
    "You are finishing an important project with the rest of your team"

    #lunch
    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room."
 
    menu:
        "Would you like to eat lunch with your co-workers?"
        "Yes, eat with your co-workers (-5 Spoons)":
            $ eatingCounter += 1
            $ spoons = changeSpoons(5)
            "You join your co-workers in the break room. [coworker] tells you all about his daughter's dance recital."
            "You have fun, but being around this many people drains you of energy."
        "No, keep working (-2 Social Points, Hunger)":
            $ socialPoints -= 2
            "You tell them that you are going to skip lunch today to continue working on the project."
            "They look disappointed. [coworker] frowns at you. "
            "Your stomach grumbles."
        
    if socialPoints < 0:
        jump noSocialPoints
    
    if spoons < -5:
        jump overspentSpoons
    
    #working
    "You have a lot of work to do today, and the team is relying on you to finish it."
    "Whatever work you do not complete will have to be picked up by your co-workers."
    
    
    menu:
        "Would you like to finish all of your work today?"

        "Yes (-10 Spoons)":
            $ spoons = changeSpoons(10)
            "You finish all of your work for the day, and submit it to your boss, [boss]."
            boss "Great work today, [player]."
            player "Thanks [boss] I'll see you later."
            
        "No (-5 Spoons, -2 Social Points) ":
            $ spoons = changeSpoons(5)
            $ socialPoints -= 2
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
    
    if spoons < -5:
        jump overspentSpoons

    if socialPoints < 0:
        jump noSocialPoints

    #packing up from work
    "You pack up all of your belongings, and begin the trek to the bus stop"
    "Your coworkers wave as you pass by them."
    coworker " Have a good night, [player]!"
    player "You too, [coworker]!"

    #at bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
    "She greets you with a warm smile."
    busDriver "Are you ready to go home, hon?"
    player "Absolutely."
    
    #bus home event
    scene enter_bus
    with dissolve
    $ spoons = changeSpoons(5) 
    "(-5 Spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."   

    if spoons < -5:
        jump overspentSpoons

    scene sit_on_bus
    with dissolve
    #dinner

    "The grocery store near your house is having a sale on bread."
    menu:
        "Would you like to stop for groceries to make a hearty meal tonight?"

        "Yes, Stop for groceries (-5 Spoons)":
            $ spoons = changeSpoons(5) 
            scene large_grocery_store
            with dissolve
            "You buy fresh groceries. The effort leaves you feeling drained."
            if spoons < -5:
                jump overspentSpoons
            scene large_bedroom
            with dissolve
            "When you get home, you debate on whether or not you should invite your friend, [bestFriend], over for dinner."
            
            menu:
                "Do you invite [bestFriend] over and cook for her?"

                "Yes, Invite friend over. (-2 Spoons, +2 Social points)":
                    $ eatingCounter += 1
                    $ socialPoints += 2
                    $ spoons = changeSpoons(2) 
                    "You call [bestFriend], and she comes over while you cook."
                    "You share a delicious tater-tot hotdish, but the effort of cooking leaves you feeling exhausted."
                    if spoons < -5:
                        jump overspentSpoons
                    bestFriend "Thank you for the meal, [player]! I know how tiring cooking can be, and I appreciate you inviting me over."
                    player "Any time. I'm glad you liked it!"
                "No (- Hunger)":
                    "You decide that you do not have the energy to cook for yourself tonight, let alone someone else."
                    "You skip dinner"

        "Stop for takeout (-2 Spoons)":
            $ eatingCounter += 1
            $ spoons = changeSpoons(2)
            "Going to the store sounds exhausting, but you still need to eat."
            if spoons < -5:
                jump overspentSpoons
            scene large_diner
            with dissolve
            "You stop for takeout at the restaurant next to your house."

    #luandry
    "Despite it having been a long day, you notice that you need to do laundry."
    "Remember, if you do not do the laundry at least twice a week, you will be deducted social points."

    menu:     
        "Would you like to do your laundry?"

        "Yes, Do laundry (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ laundryCounter = 0 
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
            if spoons < -5:
                jump overspentSpoons
        "No, Watch TV":
            $ laundryCounter += 1
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
    
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    scene black
    with fade
    "You get into bed, close your eyes, and fall asleep."
    #End of day 1 
    #jump to next day
    stop music fadeout 1.0

    jump newDay

label dayTwo:
    play music dayMusic loop    

    #day 2 timeline
    "DAY 2"
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."
    $ spoons = addDailySpoons(spoons, difficultyLevel)
    scene large_bedroom
    with fade
    "Let's see what the day has in store for you."

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons
    
    #shower
    "A shower is a great way to start the day."

    menu:
        "Would you like to take a shower today?"

        "Yes, take a shower (-2 Spoons)":
            $ spoons = changeSpoons(2)
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No, skip shower  (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    if spoons < -5:
        jump overspentSpoons

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    menu:
        "Would you like to make breakfast today?"
        
        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You make and enjoy scrambled eggs. They're a little burnt, but you don't mind."
            "The effort of cooking leaves you feeling drained."
            $ eatingCounter += 1
            if spoons < -5:
                jump overspentSpoons
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    #bus stop
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, you watch the sun rise."
    
    #on the bus
    busDriver "Hello [player] How are you today?"
    scene enter_bus
    with dissolve
    player "I'm alright [busDriver]. How are you"
    busDriver "Same as always, my dear. Same as always."
    $ spoons = changeSpoons(5) 
    scene sit_on_bus
    "(-5 spoons) You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."
    if spoons < -5:
        jump overspentSpoons

    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworkers greet you as you make your way through the building."

    #at your desk
    "You sit down and begin your work for the day."
    "Your boss, [boss], approaches your desk."
    boss "Hey [player], are you ready for the investor presentation today?"
    player "Sure am, just finishing up that last couple things."
    boss "Thank you. I'm counting on you, [player]."

    #lunch
    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room"

    menu:
        "Would you like to eat lunch with your co-workers?"

        "Yes (-5 Spoons)":
            $ spoons = changeSpoons(5)
            $ eatingCounter += 1
            "You join your co-workers in the break room. You tell them about a new book you have been reading."
            "You have fun, but being around this many people drains you of energy."
            if spoons < -5:
                jump overspentSpoons
        "No (-1 Social Point, - Hunger)":
            $ socialPoints -= 1
            "You tell them that you are going to skip lunch today to continue working on the presentation."
            "They look disappointed, but understand."
            "Your stomach grumbles."
            if socialPoints < 0:
                jump noSocialPoints
    
    #work proposal event
    "It's almost time for you to give the presentation to the company's investors."
    "You know this will take a lot of your energy for the day, but your team is counting on you."
    "One of your co-workers, [coworker], could take over and present for you, but you know this project better than anyone else."

    menu:
        "Will you present to the investors?"

        "Yes (-6 Spoons, +3 Social Points)":
            $ spoons = changeSpoons(6)
            #$ socialPoints += 3
            "You present the project to the investors, and it goes smoothly."
            boss "Great job [player]!"
            "You are proud of yourself, but you feel exhausted after standing and talking for so long"
            $ socialPoints += 3
            if spoons < -5:
                jump overspentSpoons
        "No (-3 Social Points)":
            $ socialPoints -= 3
            player "[coworker], I'm so sorry to ask at the last minute, but can you take over the investor presentation?"
            coworker "I mean, I can. But why can't you do it?"
            player "I just... I don't really have the energy for it today."
            "Your whole team looks disappointed."
            "[boss] frowns as you return to your desk."
            "[bestFriend] delivers the presentation, but stumbles a few times."
            if socialPoints < 0:
                jump noSocialPoints

    #working
    "You have a lot of work to do today, and the team is relying on you to finish it."
    "Whatever work you do not complete will have to be picked up by your co-workers "    

    #finish work event
    menu:
        "Would you like to finish all of your work today?"

        "Yes (-10 Spoons)":
            $ spoons = changeSpoons(10)
            "You finish all of your work for the day, and submit it to your boss."
        "No (-5 Spoons, -2 Social Points) ":
            $ spoons = changeSpoons(5)
            $ socialPoints -= 2
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
            
    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    #pack up from work
    "You pack up all of your belongings, and begin the trek to the bus stop."
    "Your coworkers wave as you pass by them."
    coworker " Have a good night, [player]!"
    player "You too, [coworker]!"

    #at the bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."

    #on the bus
    scene enter_bus
    with dissolve
    "You exchange nods with her, and collapse into your usual seat."
    scene sit_on_bus
    $ spoons = changeSpoons(5)
    "(-5 Spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
    if spoons < -5:
        jump overspentSpoons
    "Watching the scenery helps clear your head after such a long day at work."

    #make dinner event
    "By the time you return home, your stomach is grumbling."
    "You should have enough food in your pantry to whip something up for dinner."
    
    menu:
        "Would you like to make dinner?"

        "Yes, make dinner (-3 Spoons)":
            $ spoons = changeSpoons(3) 
            "You make pasta with the homemade spaghetti sauce your mom brought over the last time she visited."
            "The spaghetti is almost as good as when she makes it for you."
            #why is this here?
            #$ spoons -= 5
            $ eatingCounter += 1
            if spoons < -5:
                jump overspentSpoons
        "No (- Hunger)":
            "You skip dinner today. You are too tired to make anything tonight anyways."
            "Your stomach grumbles."

    #laundry
    "Despite it having been a long day, you notice that you need to do laundry."
    
    menu:         
        "Would you like to do your laundry?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
            if spoons < -5:
                jump overspentSpoons
            $ laundryCounter = 0 
        "No, watch TV instead (-Laundry)":
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break. "
            "They are playing reruns of cartoons you used to watch as a child."
            "It brings a smile to your face."
            $ laundryCounter += 1

    #bedtime
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    scene black
    with fade
    "You get into bed, close your eyes, and fall asleep."
    
    #day 2 End
    stop music fadeout 1.0

    jump newDay

label dayThree:
    play music dayMusic loop    

    #day 3 timeline
    "DAY 3"

    scene large_bedroom
    with fade
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    "A shower is a great way to start the day."
    
    #shower event
    menu:
        "Would you like to take a shower today?"

        "Yes, Take a shower (-2 Spoons)":
            $ spoons -= changeSpoons(2)
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
            player "that was not enjoyable, but at least I smell somewhat adequate"
        "No (- Cleanliness)":
            $ showerCounter += 1
            "You skip a shower today and get dressed. You need to save your spoons for other things today."

    if spoons < -5:
        jump overspentSpoons

    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    #breakfast event
    menu:
        "Would you like to make breakfast today?"

        "Yes, Make breakfast (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ eatingCounter += 1
            "You make and enjoy some buttered toast. It's the simple things in life that make it worthwhile."
            "The effort of cooking leaves you feeling drained."
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    #bus stop dialouge
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, you watch the sun rise."

    #on the bus dialouge

    scene enter_bus
    with dissolve
    busDriver "Hi there [player]! Have a great day."
    player "Thank you [busDriver]. You too."
    $ spoons = changeSpoons(5)
    scene sit_on_bus
    "(-5 Spoons) You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    if spoons < -5:
        jump overspentSpoons

    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworkers greet you as you make your way through the building."

    #at your desk
    "You sit down and begin your work for the day."
    "Your co-worker, [coworker], approaches you."
    coworker "Hey [player], how are you?"
    player "I'm doing alright. How are you?"
    coworker "Well... about that. I'm a bit behind on the team project."
    coworker "Would you be able to help me catch up on the work?"

    menu:
        "You ponder over his offer. Would you like to help [coworker] catch up on his work?"

        "Yes (-8 Spoons)":
            $ spoons = changeSpoons(8)
            player "Sure, just forward me the files."
            coworker "Thank you [player], you're the best!"
            "[coworker] tells the rest of the team about how helpful you were."
            $ socialPoints += 4
            "You finish everything [coworker] sent you, but the extra work leaves you feeling exhausted."

        "No (-3 Social Points)":
            $ socialPoints -= 3
            player "I'm sorry [coworker], I've got a lot of my own work to finish today. Is there anyone else you can ask?"
            coworker "No, everyone else is busy. I'll figure it out."

    if socialPoints < 0:
        jump noSocialPoints
    
    if spoons < -5:
        jump overspentSpoons

    #lunch event 
    scene black
    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room."
    #lunch event

    menu:
        "Would you like to eat lunch with your co-workers?"

        "Yes (-5 Spoons)":
            $ spoons = changeSpoons(5)
            $ eatingCounter += 1
            "You join your co-workers in the break room. You tell them about a new movie you watched the other day."
            "You have fun, but being around this many people drains you of energy."
        "No (-2 Social Points)":
            $ socialPoints -= 2
            "You tell them that you are going to skip lunch today to get some more work done."
            "They look disappointed, but understand."
            "Your stomach grumbles."

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    #finish work event
    "You still have a lot of work to do today, and the team is relying on you to finish it."
    "Whatever work you do not complete will have to be picked up by your co-workers."

    menu:
        "Would you like to finish all of your work today?"

        "Yes (-10 Spoons)":
            $ spoons = changeSpoons(10)
            "You finish all of your work for the day, and submit it to your boss."   
        "No (-5 Spoons)":
            $ spoons = changeSpoons(5)
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
            $ socialPoints -= 2
    
    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    #pack up from work
    "You pack up all of your belongings, and begin the trek to the bus stop."
    "Your coworkers wave as you pass by them. "
    coworker "Have a good night, [player]! "
    player "You too, [coworker]! "

    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
    "You exchange nods with her, and collapse into your usual seat." 
    scene enter_bus
    with dissolve
    $ spoons = changeSpoons(5)
    "(-5 Spoons) Today has been long and exhausting. You can feel the fatigue wearing down on your body."
    "Watching the scenery helps clear your head after such a long day at work."

    if spoons < -5:
        jump overspentSpoons

    #make dinner event
    "By the time you return home, your stomach is grumbling."
    "You should have enough food in your pantry to whip something up for dinner."
    
    menu:
        "Would you like to make dinner?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3) 
            "You make a delicious grilled cheese sandwich."
            "The sage you add gives it an extra pop of flavor."
            $ eatingCounter += 1
        "No (- Hunger)":
            "You skip dinner today. You are too tired to make anything tonight anyways."
            "Your stomach grumbles."

    "Despite it having been a long day, you notice that you need to do laundry."

    # be productive event
    menu:
        "Would you like to do your laundry?"

        "Yes, Do your laundry (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ laundryCounter = 0 
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
        "No (- Laundry)":
            $ laundryCounter += 1
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
            "You watch a stand up comedian, who is telling jokes on a talk show."
            "Only half of them are actually funny, but you enjoy yourself nonetheless."
    
    scene large_bedroom
    with dissolve
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    "You get into bed, close your eyes, and fall asleep."
    #day 3 end

    scene black
    with fade

    stop music fadeout 1.0

    jump newDay

label dayFour: 
    play music dayMusic loop    

    #start day 4
    "DAY 4"
    "Good morning! It is the start of another day."
    scene large_bedroom
    with fade
    "Remember to conserve your spoons and use them wisely."
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    "A shower is a great way to start the day."
    
    #shower event
    menu:
        "Would you like to take a shower today?"

        "Yes (-2 Spoons)":
            $ showerCounter = 0
            $ spoons = changeSpoons(2)
            "You take a warm shower. It is nice to be clean, but the effort drains you."
            if spoons < -5:
                jump overspentSpoons
            player "that was not enjoyable, but at least I can stay in if i'd like, who cares."
        "No (- Cleanliness)":
            $ showerCounter += 1
            "You skip a shower today and get dressed. You need to save your spoons for other things today."

    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    #breakfast event
    menu:
        "Would you like to make breakfast today?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ eatingCounter += 1
            "You make and enjoy some fresh fruit and tea. It's refreshing and rejuvenating."
            "The effort of preparing food leaves you feeling drained."
            if spoons < -5:
                jump overspentSpoons
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    # No transition to branch dialouge?
    "It's your day off, and you plan on spending it at home. Your plan is disrupted when your friend [bestFriend] calls."
    "She asks you to go out with her for lunch."

    #go out or stay home (start of branching for day 4)
    menu:
        "Would you like to spend the day with [bestFriend]?"

        "Yes (-15 Spoons)":
            #go out pathway, start by taking the bus
            $ spoons = changeSpoons(15)
            "You tell [bestFriend] that you'll meet her at your favorite diner."
            "Your limbs ache as you pull on your shoes, but you are excited to spend time with [bestFriend]."
            if spoons < -5:
                jump overspentSpoons
            $ socialPoints += 3
            #bus stop
            "You leave the house, making sure to lock the door behind you." 
            "You walk a few blocks down the road to the bus stop."
            "As you wait for the bus, you listen to the birds."

            busDriver "Hi there [player]! Any fun plans today?"
            player "Hi [busDriver]! I'm going out with my friend."
            busDriver "Oh, have fun dear!"
            "You take a seat at the back of the bus."
            scene enter_bus
            with dissolve
            $ spoons = changeSpoons(5)

            #at the resturant
            "[bestFriend] is waiting for you by the time the bus arrives at the diner."
            if spoons < -5:
                jump overspentSpoons
            scene large_diner
            with dissolve
            "You both waste no time in getting inside and placing your orders."
            bestFriend "How have you been [player]? I feel like I haven't seen you in forever!"
            player "I've been okay. Busy with work. What about you?"
            "[bestFriend] tells you all about the research project she is working on. It's nice to talk with her like this."
            "After nearly two hours of sitting, the ache in your hips becomes nearly unbearable."
            $ spoons = changeSpoons(5)
            $ eatingCounter += 1
            "When you finish eating, [bestFriend] asks if you would like to go on a walk to continue hanging out."
            
            if spoons < -5:
                jump overspentSpoons

            #keep going out with friends, or go home
            menu:
                "Would you like to go on a walk?"

                "Yes (-7 Spoons)":
                    $ spoons = changeSpoons(7)
                    "You agree and pay for your meal."
                    if spoons < -5:
                        jump overspentSpoons
                    $ socialPoints += 2
                    "[bestFriend] points out her favorite shops as you walk down the street."
                    "You spend about an hour together laughing and talking before it starts to get dark."
                    bestFriend "I better head home. It was so good to see you again [player]!"
                    player "It was great to see you too. We should do this again soon. "
                    $ socialPoints += 2
                
                "No":
                    player "I'm sorry [bestFriend], I don't think I have the energy tonight."
                    bestFriend "Oh, okay. That's alright."
                    "You say good to her, pay for your meal, and leave the restaurant."
                    "You wave goodbye to [bestFriend] as you wait for the bus."

            #both pathways result in going home, so back to here

            "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
            "Today has been long and exhausting, even if it was fun."
            $ spoons = changeSpoons(5)
            "(-5 Spoons) You can feel the fatigue wearing down on your body."
            if spoons < -5:
                jump overspentSpoons
            
            #make dinner event
            "By the time you return home, your stomach is grumbling."
            scene large_bedroom
            with dissolve
            "You should have enough food in your pantry to whip something up for dinner."

            menu:   
                "Would you like to make dinner?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3) 
                    "You make a delicious grilled cheese sandwich."
                    "The sage you add gives it an extra pop of flavor."
                    $ eatingCounter += 1
                    if spoons < -5:
                        jump overspentSpoons
                "No (-Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."

            #chore or TV option
            "It has been a long and tiring day, but you notice that you need to do laundry."
            
            menu:
                "Would you like to do your laundry?"

                "Yes (-3 Spoons)":
                    #do chores
                    $ spoons = changeSpoons(3)
                    $ laundryCounter = 0 
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    if spoons < -5:
                        jump overspentSpoons
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
                    "A stand up comedian is telling jokes on a talk show."
                    "Only half of them are actually funny, but you enjoy yourself nonetheless."

            #sleep
            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."
            scene black 
            with fade
            
            stop music fadeout 1.0

            jump newDay

        "No (-6 Social Points)":
            $ socialPoints = changeSpoons(6)
            #stay at home path
            "You tell [bestFriend] that you're not really feeling up to hanging out today."
            "She is disappointed, but tells you that she understands."
            "You can't help but think about how long it's been since you last got to spend time with her."

            if socialPoints < 0:
                jump noSocialPoints
                
            #leftovers or dinner?
            "You spend most of the day resting, and by the time evening rolls around, your stomach is grumbling."
            "You should have enough food in your pantry to whip something up for dinner."

            menu:
                "Would you like to make dinner?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3)
                    "You make a delicious grilled cheese sandwich."
                    if spoons < -5:
                        jump overspentSpoons
                    "The sage you add gives it an extra pop of flavor."
                    $ eatingCounter += 1

                "No (- Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."

            #laundry
            "Despite wanting to rest today, you notice that you need to do laundry."
            
            menu:
                "Would you like to do your laundry?"
                
                "Yes (-3 Spoons)":
                    #do chores
                    $ spoons = changeSpoons(3)
                    $ laundryCounter = 0 
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    if spoons < -5:
                        jump overspentSpoons
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you get comfy on the couch and open a book that you have been meaning to start."
                    "The plot is light-hearted but engaging."
                    "You don't remember the last time you were able to indulge in the simple pleasure of a book."

            #sleep
            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."

            stop music fadeout 1.0

            jump newDay
            
label dayFive: 
    play music dayMusic loop    

    #start day 5
    "DAY 5"
    "Good morning! It is the start of another day."
    scene large_bedroom
    with fade
    "Remember to conserve your spoons and use them wisely."
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)
    
    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    "A shower is a great way to start the day."

    #shower event
    menu:
        "Would you like to take a shower today?"
        
        "Yes, Take a shower (-2 Spoons)":
            $ showerCounter = 0
            $ spoons = changeSpoons(2)
            "You take a warm shower. It is nice to be clean, but the effort drains you."

            if spoons < -5:
                jump overspentSpoons

        "No, Skip shower (- Cleanliness)":
            $ showerCounter += 1
            "You skip a shower today and get dressed. You need to save your spoons for other things today."

    #breakfast event
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    menu:
        "Would you like to make breakfast today?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ eatingCounter += 1
            "You make and enjoy some fresh fruit and tea. It's refreshing and rejuvenating."
            "The effort of preparing food leaves you feeling drained."

            if spoons < -5:
                jump overspentSpoons
            
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    #go out or stay home (start of branching for day 5)
    "It's your day off, and you plan on spending it at home. Your plan is disrupted when your friend [bestFriend] calls."
    "She asks you to go out with her for lunch."

    menu:
        "Would you like to spend the day with [bestFriend]?"

        "Yes (-15 Spoons)":
            $ spoons = changeSpoons(15)
            "You tell [bestFriend] that you'll meet her at your favorite diner."
            "Your limbs ache as you pull on your shoes, but you are excited to spend time with [bestFriend]."
            if spoons < -5:
                jump overspentSpoons
            $ socialPoints += 3
            #bus stop
            "You leave the house, making sure to lock the door behind you."
            "You walk a few blocks down the road to the bus stop."
            "As you wait for the bus, you listen to the birds."

            #on the bus
            busDriver "Hi there [player]! Any fun plans today?"
            player "Hi [busDriver]! I'm going out with my friend."
            busDriver "Oh, have fun dear!"
            "You take a seat at the back of the bus."
            scene sit_on_bus
            with fade
            $ spoons = changeSpoons(5)
            "(-5 Spoons) You are already feeling fatigued."
            if spoons < -5:
                jump overspentSpoons

            #at the resturant
            "[bestFriend] is waiting for you by the time the bus arrives at the diner."
            "You both waste no time in getting inside and placing your orders."
            scene large_diner
            with dissolve
            bestFriend "How have you been [player]? I feel like I haven't seen you in forever!"
            player "I've been okay. Busy with work. What about you?"
            "[bestFriend] tells you all about the book she is currently reading. It's nice to talk with her like this."
            $ spoons = changeSpoons(5)
            "(-5 Spoons) After nearly two hours of sitting, the ache in your hips becomes nearly unbearable."
            if spoons < -5:
                jump overspentSpoons
            "When you finish eating, [bestFriend] asks if you would like to watch a movie with her."

            menu:
                "Would you like to go to the movie theater?"

                "Yes (-7 Spoons)":
                    $ spoons = changeSpoons(7)
                    "You agree and pay for your meal."

                    if spoons < -5:
                        jump overspentSpoons

                    $ socialPoints += 2
                    "[bestFriend] leads you down the street to a movie theater and pays for your ticket to a romcom you had been looking forward to."
                    "By the time the movie ends, it is already getting late"
                    bestFriend "That was so much fun!"
                    player "Yeah! It was even better than I expected."
                    bestFriend "Well, I better head home. It was so good to see you again [player]!"
                    player "It was great to see you too. We should do this again soon. "

                "No":
                    player "I'm sorry [bestFriend], I don't think I have the energy tonight."
                    bestFriend "Oh, okay. That's alright."
                    "You say goodbye to her, pay for your meal, and leave the restaurant."
                    "You wave goodbye to [bestFriend] as you wait for the bus."
            #at the bus stop

            "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
            scene enter_bus
            with dissolve

            #on the bus
            "You exchange nods with her, and collapse into your usual seat."
            scene sit_on_bus
            "Today has been long and exhausting, even if it was fun."
            $ spoons = changeSpoons(5)
            "(-5 Spoons) You can feel the fatigue wearing down on your body."

            if spoons < -5:
                jump overspentSpoons

            scene main_bedroom
            with dissolve

            #dinner
            "By the time you return home, your stomach is grumbling."
            "You should have enough food in your pantry to whip something up for dinner."
            menu:
                "Would you like to make dinner?"

                "Yes (-3 spoons)":
                    $ spoons = changeSpoons(3) 
                    $ eatingCounter += 1
                    "You make a delicious grilled cheese sandwich."
                    "The sage you add gives it an extra pop of flavor."
                "No (- Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."
            
            #laundry

            "It has been a long and tiring day, but you notice that you need to do laundry."
            menu:
                "Would you like to do your laundry?"
                
                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3) 
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    $ laundryCounter = 0
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
                    "A stand up comedian is telling jokes on a talk show."
                    "Only half of them are actually funny, but you enjoy yourself nonetheless."
                    
            #sleep
            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."

            scene black
            with fade

            stop music fadeout 1.0

            jump newDay

        "No (-6 Social Points)":
            $ socialPoints -= 6
            "You tell [bestFriend] that you're not really feeling up to hanging out today."
            "She is disappointed, but tells you that she understands."
            "You can't help but think about how long it's been since you last got to spend time with her."
            
            if socialPoints < 0:
                jump noSocialPoints

            scene main_bedroom
            with dissolve

            #dinner
            "You spend most of the day resting, and by the time evening rolls around, your stomach is grumbling."
            "You should have enough food in your pantry to whip something up for dinner."
            
            menu:
                "Would you like to make dinner?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3)
                    $ eatingCounter += 1
                    "You make a delicious grilled cheese sandwich."
                    "The sage you add gives it an extra pop of flavor."
                "No (- Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."

            #laundry
            "Despite wanting to rest today, you notice that you need to do laundry."

            menu:
                "Would you like to do your laundry?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3)
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    $ laundryCounter = 0
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you get comfy on the couch and open a book that you have been meaning to start."
                    "The plot is light-hearted but engaging. "
                    "You don't remember the last time you were able to indulge in the simple pleasure of a book."

            #sleep
            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."

            scene black
            with fade

            stop music fadeout 1.0

            jump newDay

label daySix:
    play music dayMusic loop    

    "DAY 6"
    #start of day 6

    "Good morning! It is the start of another day."
    scene large_bedroom
    with fade
    "Remember to conserve your spoons and use them wisely."
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    #shower event
    "A shower is a great way to start the day."

    menu:
        "Would you like to take a shower today?"

        "Yes, Take a shower (-2 Spoons)":
            $ showerCounter = 0
            $ spoons = changeSpoons(2)
            "You take a warm shower. It is nice to be clean, but the effort drains you."

            if spoons < -5:
                jump overspentSpoons

        "No, Skip shower (- Cleanliness)":
            $ showerCounter += 1
            "You skip a shower today and get dressed. You need to save your spoons for other things today."

    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    #breakfast event
    menu:
        "Would you like to make breakfast today?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ eatingCounter += 1
            "You make and enjoy some fresh fruit and tea. It's refreshing and rejuvenating."
            "The effort of preparing food leaves you feeling drained."

            if spoons < -5:
                jump overspentSpoons
            
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    "It's your day off, and you plan on spending it at home. Your plan is disrupted when your friend [bestFriend] calls."
    "She asks you to go out with her for lunch."

    menu:
        "Would you like to spend the day with [bestFriend]?"

        "Yes (-15 Spoons)":
            $ spoons = changeSpoons(15)
            "You tell [bestFriend] that you'll meet her at your favorite diner."
            "Your limbs ache as you pull on your shoes, but you are excited to spend time with [bestFriend]."
            if spoons < -5:
                jump overspentSpoons
            $ socialPoints += 3

            #bus stop
            "You leave the house, making sure to lock the door behind you."
            "You walk a few blocks down the road to the bus stop."
            "As you wait for the bus, you listen to the birds."

            #on the bus
            busDriver "Hi there [player]! Any fun plans today?"
            player "Hi [busDriver]! I'm going out with my friend."
            busDriver "Oh, have fun dear!"
            "You take a seat at the back of the bus."
            scene sit_on_bus
            with dissolve
            $ spoons = changeSpoons(5)
            "(-5 Spoons) You are already feeling fatigued."
            if spoons < -5:
                jump overspentSpoons

            "[bestFriend] is waiting for you by the time the bus arrives at the diner."
            "You both waste no time in getting inside and placing your orders."
            scene large_diner
            with dissolve
            bestFriend "How have you been [player]? I feel like I haven't seen you in forever!"
            player "I've been okay. Busy with work. What about you?"
            "[bestFriend] tells you all about the book she is currently reading. It's nice to talk with her like this."
            $ spoons = changeSpoons(5)
            "(-5 Spoons) After nearly two hours of sitting, the ache in your hips becomes nearly unbearable."
            if spoons < -5:
                jump overspentSpoons

            "When you finish eating, you realize that you want to keep talking with [bestFriend]."

            menu:
                "Would you like to invite her to come home with you?"

                "Yes (-7 Spoons)":
                    $ spoons = changeSpoons(7)
                    "[bestFriend] is thrilled and agrees to come home with you to continue hanging out."
                    if spoons < -5:
                        jump overspentSpoons
                    $ socialPoints += 2
                    "You pay for your meal, and she drives both of you to your house."
                    scene large_bedroom
                    with dissolve
                    "You spend the next few hours laughing and sharing stories."
                    bestFriend "Thank you for having me over! I had so much fun."
                    player "Of course! It was great talking with you."
                    bestFriend "Well, I better head home before it gets too dark. Have a great rest of your evening!"
                    player "Drive safe!"
                    "You wave to [bestFriend] as she drives away, a content smile settling across your face."
                "No (-5 Spoons)":
                    $ spoons = changeSpoons(5)
                    "As much as you'd like to continue hanging out, you don't have the energy to keep socializing."
                    "You ask [bestFriend] to give you a ride home, and in exchange, you pay for both of your meals."
                    if spoons < -5:
                        jump overspentSpoons
                    bestFriend "It was good to see you again, have a good night."
                    player "Thank you for the ride, we should hang out again soon."

            scene main_bedroom
            with dissolve

            #dinner
            "By the time you return home, your stomach is grumbling."
            "You should have enough food in your pantry to whip something up for dinner."

            menu:
                "Would you like to make dinner?"

                "Yes (-3 spoons)":
                    $ spoons = changeSpoons(3) 
                    $ eatingCounter += 1
                    "You make a delicious grilled cheese sandwich."
                    "The sage you add gives it an extra pop of flavor."
                "No (- Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."

            #laundry
            "Despite wanting to rest today, you notice that you need to do laundry."
    
            menu:
                "Would you like to do your laundry?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3)
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    $ laundryCounter = 0
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
                    "A stand up comedian is telling jokes on a talk show."
                    "Only half of them are actually funny, but you enjoy yourself nonetheless."
            
            #bed time

            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."
            stop music fadeout 1.0

            scene black 
            with dissolve

            jump newDay

        "No (-6 Social Points)":
            
            $ socialPoints -= 6

            "You tell [bestFriend] that you're not really feeling up to hanging out today."
            "She is disappointed, but tells you that she understands."
            "You can't help but think about how long it's been since you last got to spend time with her."
            
            if socialPoints < 0:
                jump noSocialPoints

            scene main_bedroom
            with dissolve

            #dinner
            "You spend most of the day resting, and by the time evening rolls around, your stomach is grumbling."
            "You should have enough food in your pantry to whip something up for dinner."

            menu:
                "Would you like to make dinner?"

                "Yes (-3 spoons)":
                    $ spoons -= 3 
                    $ eatingCounter += 1
                    "You make a delicious grilled cheese sandwich."
                    "The sage you add gives it an extra pop of flavor."
                "No (- Hunger)":
                    "You skip dinner today. You are too tired to make anything tonight anyways."
                    "Your stomach grumbles."

            #laundry         
            "Despite wanting to rest today, you notice that you need to do laundry."

            menu:
                "Would you like to do your laundry?"

                "Yes (-3 Spoons)":
                    $ spoons = changeSpoons(3)
                    "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
                    $ laundryCounter = 0
                "No (- Laundry)":
                    $ laundryCounter += 1
                    "Instead of doing laundry, you get comfy on the couch and open a book that you have been meaning to start."
                    "The plot is light-hearted but engaging."
                    "You don't remember the last time you were able to indulge in the simple pleasure of a book."
            
            #bedtime

            "After a long and tiring day, you decide it's time for bed."
            "You make your way to your bedroom."
            "You get into bed, close your eyes, and fall asleep."
            
            scene black 
            with fade
            
            stop music fadeout 1.0

            jump newDay

label daySeven:
    play music dayMusic loop    

    "DAY 7"
    # Day 7 timeline
    #wake up
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."
    scene large_bedroom
    with fade
    "Let's see what the day has in store for you."

    $ spoons = addDailySpoons(spoons, difficultyLevel)

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    scene main_bedroom
    with dissolve
    #shower
    "A shower is a great way to start the day."

    menu:
        "Would you like to take a shower today?"

        "Yes(-2 Spoons)":
            $ spoons = changeSpoons(2)
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    if spoons < -5:
        jump overspentSpoons
    
    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    menu:
        "Would you like to make breakfast today?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You make and enjoy scrambled eggs. You might have added a little too much salt, but they're still tasty."
            "The effort of cooking leaves you feeling drained."
            $ eatingCounter += 1
            if spoons < -5:
                jump overspentSpoons
        "No (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today."
            "Your stomach grumbles."

    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, it starts to rain. It makes your body ache."

    #bus
    busDriver "Hello [player]! Off to work?."
    player "I sure am."
    scene sit_on_bus
    with dissolve
    $ spoons = changeSpoons(5)
    "You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    if spoons < -5:
        jump overspentSpoons

    #at work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworker, [coworker], greets you as you make your way through the building."
    "You sit down and begin your work for the day."
    "You are starting an important project with the rest of your team."

    #lunch event
    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room."

    menu:
        "Would you like to eat lunch with your co-workers?"
        
        "Yes (-5 Spoons)":
            $ eatingCounter += 1
            $ spoons = changeSpoons(5)
            "You join your co-workers in the break room. [coworker] tells you about a new book he has been reading."
            "You have fun, but being around this many people drains you of energy."
            if spoons < -5:
                jump overspentSpoons
        "No (-2 Social Points) (- Hunger)":
            $ socialPoints -= 2
            "You tell them that you are going to skip lunch today to continue working on the project."
            "They look disappointed. [coworker] frowns at you."
            "Your stomach grumbles."

            if socialPoints < 0:
                jump noSocialPoints

    #finish work event
    "You have a lot of work to do today, and the team is relying on you to finish it."
    "Whatever work you do not complete will have to be picked up by your co-workers."

    menu:
        "Would you like to finish all of your work today?"

        "Yes (-10 Spoons)":
            $ spoons = changeSpoons(10)
            "You finish all of your work for the day, and submit it to your boss."
            boss "Great work today, [player]."
            player "Thanks [boss], I'll see you later."
            
        "No (-5 Spoons)":
            $ spoons = changeSpoons(5)
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."
            $ socialPoints -= 2
            if socialPoints < 0:
                jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons

    #pack up
    "You pack up all of your belongings, and begin the trek to the bus stop."
    "Your coworkers wave as you pass by them. "
    coworker "Have a good night, [player]!"
    player "You too, [coworker]! "

    #bus home event

    scene enter_bus
    with dissolve
    
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home."
    "She greets you with a warm smile."
    busDriver "Are you ready to go home, hon?"
    player "Absolutely."

    $ spoons = changeSpoons(5)
    "Today has been long and exhausting. You can feel the fatigue wearing down on your body."

    if spoons < -5:
        jump overspentSpoons

    #dinner pathing
    "The grocery store near your house is having a sale on vegetables."

    menu:
        "Would you like to stop for groceries to make a hearty meal tonight, or would you rather save your energy and get takeout?"

        "Get groceries (-5 Spoons)":
            $ spoons = changeSpoons(5) 
            scene large_grocery_store
            with dissolve
            "You buy fresh groceries. The effort leaves you feeling drained."
            
            if spoons < -5:
                jump overspentSpoons

            scene large_bedroom
            with dissolve
                
            "When you get home, you debate on whether or not you should invite your friend, [bestFriend], over for dinner."
            "Do you invite [bestFriend] over and cook for her?"
            
            menu:
                "Yes (-2 Spoons)":
                    $ spoons = changeSpoons(2)
                    $ eatingCounter += 1
                    "You call [bestFriend], and she comes over while you cook."
                    "You share a delicious leek and potato soup, but the effort of cooking leaves you feeling exhausted."
                    if spoons < -5:
                        jump overspentSpoons
                    bestFriend "Thank you for the meal, [player]! I know how tiring cooking can be, and I appreciate you inviting me over."
                    player "Any time. I'm glad you liked it!"
                    $ socialPoints += 2
                "No (- Hunger)":
                    "You decide that you do not have the energy to cook for yourself tonight, let alone someone else."
                    "You skip dinner."

        "Get takeout (-2 Spoons)":
            $ spoons = changeSpoons(2)
            scene large_diner
            with dissolve
            "Grocery shopping sounds exhausting, so you elect to get takeout instead."
            "When you get home, you realize that you ordered far too much food for one person."
            scene main_bedroom
            with dissolve
            "Would you like to invite your friend [bestFriend] over to share the food?"

            menu:
                "Yes (-2 spoons)":
                    $ spoons = changeSpoons(2)
                    "You call [bestFriend], and she comes over before the food goes cold."
                    bestFriend "Thank you for thinking of me, [player]! This was delicious"
                    player "Of course!"
                    if spoons < -5:
                        jump overspentSpoons
                    $ socialPoints += 2

                "No":
                    "As much as you would like to see [bestFriend], you don't have the energy to spend time around others tonight"
                    $ eatingCounter += 1
                    "You eat your takeout alone and put the leftovers in the fridge."            
            
    #lunadry event      
    "Despite it having been a long day, you notice that you need to do laundry."

    menu:
        "Would you like to do your laundry?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            $ laundryCounter = 0 
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but at least you get to go to bed with clean sheets."
        "No":
            $ laundryCounter += 1
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
    
    "After a long and tiring day, you decide it's time for bed. "
    "You make your way to your bedroom."
    "You get into bed, close your eyes, and fall asleep."
    scene black
    with fade
    stop music fadeout 1.0

    jump newDay
    #End of day 7

label dayEight:
    play music dayMusic loop    

    "DAY 8"
    #Day 8 timeline
    #wake up
    
    "Good morning! It is the start of another day."
    "Remember to conserve your spoons and use them wisely."
    $ spoons = addDailySpoons(spoons, difficultyLevel)
    scene large_bedroom
    with fade
    "Let's see what the day has in store for you."

    #daily checks
    if eatingCounter < 2:
        #player did not eat enough during the day prior, deduct spoons
        "You did not eat at least 2 meals yesterday. You have 5 less spoons today."
        $ spoons = changeSpoons(5)

    if showerCounter >= 3:
        #player has not showered in the past few days, deduct spoons
        "You have not showered in the last 3 days. You start to smell, and lose 2 social points."
        $ socialPoints -= 3

    if laundryCounter >= 3:
        #player has not done laundry in the past few days, deduct spoons
        "You have not done your laundry in 3 days. You have no clean clothes, and lose 2 social points."
        $ socialPoints -= 3

    if socialPoints < 0:
        jump noSocialPoints

    if spoons < -5:
        jump overspentSpoons
    
    #shower
    "A shower is a great way to start the day."

    menu:
        "Would you like to take a shower today?"

        " Yes, take a shower (-2 Spoons)":
            $ spoons = changeSpoons(2)
            $ showerCounter = 0
            "You take a warm shower. It is nice to be clean, but the effort drains you."
        "No, skip shower (- Cleanliness)":
            "You skip a shower today and get dressed. You need to save your spoons for other things today."
            $ showerCounter += 1

    if spoons < -5:
        jump overspentSpoons

    #breakfast
    "Now that you are ready for the day, it's time for breakfast. It is important to nourish your body."

    menu:
        "Would you like to make breakfast today?"

        "Yes, make and eat breakfast (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You make and enjoy pancakes. They're a little lumpy, but still delicious. The effort of cooking leaves you feeling drained."
            player "That was tasty!"
            $ eatingCounter += 1
        "No, skip breakfast (- Hunger)":
            "You skip breakfast today. You need to save your spoons for other things today. Your stomach grumbles."

    if spoons < -5:
        jump overspentSpoons
    
    #transition
    "You leave the house, making sure to lock the door behind you."
    "You walk a few blocks down the road to the bus stop."
    "As you wait for the bus, you watch the sun rise. The sky is beautiful this morning."

    #bus
    busDriver "Hello [player]! How are you today?"
    scene enter_bus
    with dissolve

    player "I'm alright [busDriver]. How are you?"
    "Same as always, my dear. Same as always."
    scene sit_on_bus
    $ spoons = changeSpoons(5)
    "You sit in your usual seat and watch the scenery go by. You are already feeling fatigued."

    if spoons < -5:
        jump overspentSpoons
    
    #arrival to work
    "After the bus drops you off at work, you waste no time getting to your desk."
    "Your coworkers greet you as you make your way through the building."

    #at your desk
    "You sit down and begin your work for the day."
    "Your boss, [boss], approaches your desk."
    boss "Hey [player], how is the project coming along?"
    player "It's going well, I just have a few more things to finish."
    boss "Good. The other team is waiting on you. I'm counting on you, [player]."

    #lunch option
    "Partway through the day, your stomach begins to rumble. It's time for lunch."
    "Your co-workers approach you. They invite you to join them for lunch in the break room."

    menu:
        "Would you like to eat lunch with your co-workers?"

        "Yes (-5 Spoons)":
            $ eatingCounter += 1
            $ spoons = changeSpoons(5)
            "You join your co-workers in the break room. You tell them about a new show you have been watching."
            "You have fun, but being around this many people drains you of energy."
            if spoons < -5:
                jump overspentSpoons
        "No (-2 Social Points) (- Hunger)":
            $ socialPoints -= 2
            "You tell them that you are going to skip lunch today to continue working on the project"
            "They look disappointed, but understand."
            "Your stomach grumbles."
            if socialPoints < 0:
                jump noSocialPoints

    #Catch up on work
    "Some of your coworkers have been falling behind on their work and your boss asked you to help pick up the slack."
    "You know this will take a lot of your energy for the day, but your team is counting on you."
    "Your team will fall behind on their deadlines if someone doesn't take charge."  
    
    menu:
        "Will you finish your coworkers unfinished work?"  

        "Yes (-6 Spoons)":
            $ spoons = changeSpoons(6)
            "You finish all of the extra work and submit it to your boss."
            $ socialPoints += 3
            "He smiles gratefully."
            if spoons < -5:
                jump overspentSpoons

        "No (-3 Social Points)":
            player "I'm sorry [boss], but I have my own work to worry about."
            boss "I understand, but we really need someone to catch the team up."
            player "I'm sorry. I just can't today."
            "[boss] looks disappointed."


    #finish work event
    "You still have a lot of work to do today, and the team is relying on you to finish it."
    "Whatever work you do not complete will have to be picked up by your co-workers."

    menu:
        "Would you like to finish all of your work today?"

        "Yes (-10 Spoons)":
            $ spoons = changeSpoons(10)
            "You finish all of your work for the day, and submit it to your boss."
        "No (-5 spoons)":
            $ spoons = changeSpoons(5)
            $ socialPoints -= 2
            "You complete some of your work, but there are still some things left unfinished. Your co-workers do not appreciate having to pick up the slack."

    if spoons < -5:
        jump overspentSpoons

    if socialPoints < 0:
        jump noSocialPoints

    #packing up from work
    "You pack up all of your belongings, and begin the trek to the bus stop"
    "Your coworkers wave as you pass by them."
    coworker "Have a good night, [player]!"
    player "You too, [coworker]!"

    #at bus stop
    "You are not at the bus stop for long before [busDriver] pulls up, ready to take you home. She smiles at you through the window."
    
    #bus home event
    player "You exchange nods with her, and collapse into your usual seat."
    scene enter_bus
    with dissolve
    $ spoons = changeSpoons(5)
    "(-5 spoons) Today has been long and exhausting. You can feel the fatigue wearing down on you."

    if spoons < -5:
        jump overspentSpoons
    
    scene sit_on_bus
    "Watching the scenery helps clear your head after such a long day at work."

    #make dinner event
    scene main_bedroom
    with dissolve
    "By the time you return home, your stomach is grumbling."
    "You should have enough food to make something for dinner."

    menu:
        "Would you like to make dinner?"

        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3) 
            "You make stew with some things that you bought the last time you went grocery shopping, happy you got to use some of the vegetables you never know what to do with."
            $ eatingCounter += 1
            "It was perfect, and exactly what you were craving."
        "No":
            "You skip dinner today. You are too tired to make anything tonight anyways."
            "Your stomach grumbles."

    if spoons < -5:
        jump overspentSpoons
    
    "Despite it having been a long day, you notice that you need to do laundry."
    #be productive event
    
    menu:            
        "Would you like to do your laundry?"
        
        "Yes (-3 Spoons)":
            $ spoons = changeSpoons(3)
            "You wash, dry, fold, and put away all of your laundry. You are exhausted, but going to bed with clean sheets was worth it."
            $ laundryCounter = 0 
        "No (- Laundry)":
            $ laundryCounter += 1
            "Instead of doing laundry, you sit on the couch and watch TV for a while. You deserve a break."
            "You watch a new series that's been talked about a lot."
            "It was good, and kept you entertained."
    
    "After a long and tiring day, you decide it's time for bed."
    "You make your way to your bedroom."
    "You get into bed, close your eyes, and fall asleep."

    stop music fadeout 1.0
    scene black
    with fade
    #day 8 End
    jump newDay

label overspentSpoons:
    "You exerted too much energy and ran out of spoons. You will have 5 less spoons tomorrow."
    #call a new day, randomly, somehow
    stop music fadeout 1.0

    jump newDay

label noSocialPoints:
    "You have lost all of your social points. You lose."
    #ending the game
    $ dayCounter = 100

label newDay:
    if dayCounter == 0:
        $ dayCounter += 1
        jump dayOne
    elif dayCounter == 6:
        $ dayCounter += 1
        jump daySeven
    elif dayCounter == 100:
        #game Over, Ran out of spoons ending 
        screen black
        "The Game is over, you have lost all of your social points. (somrthing about spoon theory.) Life is exhausting."
    elif dayCounter > 6:
        #end everything
        
        screen black
        "7 days have passed, the game should end"
    else:
        #random day
        $ dayCounter += 1
        jump newRandomDay

label newRandomDay:
    #get a new index using the arr len
    $ newDayIndex = random.randint(0, len(dayList))

    #pop off value using index

    $ newDay = dayList.pop(newDayIndex)

    #using new day value, get the new day and jump to it.

    if newDay == 2:
        jump dayTwo
    elif newDay == 3:
        jump dayThree
    elif newDay == 4:
        jump dayFour
    elif newDay == 5:
        jump dayFive
    elif newDay == 6:
        jump daySix
    elif newDay == 7:
        jump dayEight
    
