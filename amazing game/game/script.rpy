# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ryan")
define t = Character("Thomas")
define c = Character("Cole")
define n = Character("Nathan")
define a = Character("Artemis")
define s = Character("Stephen")
define adv = Character("Advisor")
define y = Character("You")
define mc = Character("[name]")

init:
    $ ryan_relationship = 0
    $ thomas_relationship = 0
    $ cole_relationship = 0
    $ nathan_relationship = 0
    $ artemis_relationship = 0
    $ stephen_relationship = 0

    $ business_points = 0
    $ english_points = 0
    $ math_points = 0
    $ compsci_points = 0
    $ art_points = 0
    $ biology_points = 0

# The game starts here.
label start:
    $ name = renpy.input("What's your name?")
    $ name = name.strip()

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "You are an incoming college freshman who applied to all of the top universities in your country… and one single safety school."
    "Although you managed to keep good grades in school, you didn’t bother thinking much about what you wanted to do in the future and went in undecided."
    "To your surprise, you got rejected from all of the top universities."
    "But congrats! You got into the safety school!"
    "Hopefully, during your time at Marigold University, you will meet many people who will help you choose your educational field!"
    "And maybe, your friendships will turn into something more…?"

    scene advisor room

    adv "Welcome to Marigold University, [name]."
    adv "It says here that your major is undecided. Well, we have a policy here at Marigold University that requires undecided freshmen to decide on a major by the end of the year."
    adv "In order to help you, I have enrolled you in a variety of classes, including Business, Computer Science, English, Art, Math, and Biology."
    adv "Be sure to keep up your grades, especially in the one you want to major in."
    adv "Good luck, [name]."

    scene black

    "Clutching your new schedule in hand, you walk to your first class, Biology 101."

    scene biology room
    
    "You walk into a packed lecture hall."
    "You find an empty seat towards the back of the hall."
    "Suddenly, a hand grasps the back of the seat next to you."
    "You look up to see."

    menu:
    
        s "Hi, is it okay if I sit here?"

        "I don’t mind.":

            $ stephen_relationship += 10
            jump dontmind

        "Stay silent.":

            $ stephen_relationship -= 10
            jump silent

    label dontmind:

    s "Thanks!"
    s "I’m Stephen. What’s your name?"

    y "I’m [name], it’s nice to meet you."

    jump bio1

    label silent:
    s "Sorry, but I think I’ll have to sit here. There aren’t any other open seats."
    s "I’m Stephen. What’s your name?"

    y "I’m [name]."
    
    jump bio1

    label bio1:

    s "So… are you also a biology major?"

    y "I’m actually undecided."

    s "Oh cool! Well, I think that biology is really interesting."
    s "I’m on the pre-med track. I really hope to be a doctor one day."
    s "I love working with patients. I like hearing about their stories and-"

    menu:

        s "Oh, sorry… I’m rambling again…"

        "Actually, I’d love to hear more.":

            $ stephen_relationship += 10
            jump hearmore
    
        "No worries, but I think class is about to start.":

            $ stephen_relationship -= 5
            jump classstart

    label hearmore:
        
    s "Wait really? I appreciate it."
    s "Healthcare has always been a big part of my life. That’s why I’m super passionate about it."
    s "Oh, it looks like class is about to start."
        
    "Stephen proceeds to take out his laptop and turns his attention to the front of the classroom."

    jump bio2

    label classstart:
    
    s "Oh, right!"
        
    "Stephen proceeds to take out his laptop and turns his attention to the front of the classroom."

    jump bio2

    label bio2:
    "The professor introduces himself and proceeds to talk about class expectations. He then gives an opportunity for introductions amongst students."
    "Stephen turns to look at you again."
    
    s "So you’re undecided…"

    menu:

        s "Not a big decision maker, huh?" #joke
    
        "Surprisingly, I didn’t get to make a decision on a college either…":

            $ stephen_relationship += 10
            jump collegedec
    
        "Excuse me?":

            $ stephen_relationship -= 10
            jump excuseme

    label collegedec:
    
    s "You also got rejected from other schools?" #Stephen asks with an empathetic look.

    "You nod."

    s "Don’t worry, I’m right there with you."

    jump bio3

    label excuseme:

    s "Sorry! I was just joking around."
    
    "The mood turns awkward."

    jump bio3

    label bio3:

    "The professor announces the end of class and thanks everyone for attending."

    s "It was nice meeting you, [name]."
    s "I’ll catch you around!"

    scene black

    scene business

    "You walk into a relatively empty classroom."
    "The students there before you filled up the back row, and you have no choice but to sit near the front."
    "As you settle down, you jolt in surprise when feeling a light tap on your shoulder."
    "You look back to see dudes desc"

    menu:
        
        r "Hey, this is Business Administration 120, right?"
    
        "Yeah, this is section 2.":

            $ ryan_relationship += 5
            jump section2

        "Stay silent.":

            $ ryan_relationship -= 5
            jump silence

    label section2:
    
    r "Awesome, I was worried this was the wrong classroom!"

    "Ryan sits next to you."

    jump bus1

    label silence:

    r "Oh, uhh shoot. Is this the wrong class?"

    "Ryan checks his schedule again and discovers that this is the correct classroom. He brushes off the player’s silent treatment and sits next to them."

    jump bus1


    label bus1:

    r "Let’s do icebreakers, where are you from and what’s your major?"
    
    "He points at himself and smiles."

    r "I’m Ryan from the Bay Area, and I’m going into Real Estate!"

    y "I’m [name], and I’m from (hometown). I’m actually undecided."

    menu:

        r "Oh cool! So you’re trying out all the classes! Personally, I think business is the way to go!"

        "Maybe you can convince me to commit to business.":

            $ ryan_relationship += 10
            jump convince

        "I’m just forced to take all the classes, I don’t think I’ll actually choose business.":

            $ ryan_relationship -= 10
            jump forced


    label convince:

    r "I guess that’ll be my goal for this semester!"
    "Ryan chuckles, looking happy for the rest of lecture."

    jump bus2

    label forced:
    
    r "Oh, well I guess you do have a bunch of other choices…"
    "Ryan’s mood is gloomy for the rest of lecture."

    jump bus2


    label bus2:

    "The lecture today was boring, mostly going over the syllabus and professor introductions."
    "At the end of class, as you pack up your things, Ryan approaches you."

    menu:
    
        r "You wanna exchange numbers? You seem pretty smart and I’m trying to assemble the best study group at Marigold University!" 

        "Sure, it’d be great to study for midterms together.":

            $ ryan_relationship += 15
            jump exchangenum

        "No thank you, I prefer to study alone.":

            $ ryan_relationship -= 10
            jump dontexchangenum

    label exchangenum:

    r "Thanks! I’ll text you."
    jump bus3


    label dontexchangenum:

    r "Oh, okay then. See you next class."
    jump bus3


    label bus3:

    scene black

    # This ends the game.

    return
