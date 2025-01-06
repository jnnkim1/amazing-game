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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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

    adv "Welcome to Marigold University, ____."
    adv "It says here that your major is undecided. Well, we have a policy here at Marigold University that requires undecided freshmen to decide on a major by the end of the year."
    adv "In order to help you, I have enrolled you in a variety of classes, including Business, Computer Science, English, Art, Math, and Biology."
    adv "Be sure to keep up your grades, especially in the one you want to major in."
    adv "Good luck, _____."

    scene black screen

    "Clutching your new schedule in hand, you walk to your first class, Biology 101."

    scene biology room
    
    "You walk into a packed lecture hall."
    "You find an empty seat towards the back of the hall."
    "Suddenly, a hand grasps the back of the seat next to you."
    "You look up to see [dudes desc]."

    menu:
    
        s "Hi, is it okay if I sit here?"

        "I don’t mind.":

            call dontmind

        "Stay silent.":

            call silent

    label dontmind:

    s "Thanks!"
    s "I’m Stephen. What’s your name?"

    y "I’m _____, it’s nice to meet you."

    return

    label silent:
    s "Sorry, but I think I’ll have to sit here. There aren’t any other open seats."
    s "I’m Stephen. What’s your name?"

    y "I’m _____."
    
    return

    s "So… are you also a biology major?"

    y "I’m actually undecided."

    s "Oh cool! Well, I think that biology is really interesting."
    s "I’m on the pre-med track. I really hope to be a doctor one day."
    s "I love working with patients. I like hearing about their stories and-"
    s "Oh, sorry… I’m rambling again…"

    # This ends the game.

    return
