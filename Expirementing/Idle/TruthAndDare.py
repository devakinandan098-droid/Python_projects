import random as r
truths_and_dares = {
    "truth": [
        "What is the most embarrassing thing you've done at school or work?",
        "If you could switch lives with anyone in this room for a day, who would it be?",
        "What is a secret you've never told anyone in this room?",
        "What is your biggest fear or phobia?",
        "Have you ever lied to get out of a social obligation? What was the lie?",
        "What is the worst gift you have ever received from someone?",
        "What is the most childish thing you still do regularly?",
        "If you found a suitcase full of legal cash, would you keep it or turn it in?",
        "What is the biggest mistake you have ever made in your life?",
        "What is a bad habit you have that you find difficult to break?",
        "Have you ever broken something expensive and blamed it on someone else?",
        "What is the most useless talent or skill you possess?",
        "If you could change one decision you made in the past, what would it be?",
        "What is the longest you have ever gone without showering?",
        "Have you ever re-gifted something that was given to you?",
        "What is the weirdest food combination you secretly enjoy?",
        "What is the most expensive thing you've ever broken or ruined?",
        "If you could have any superpower for 24 hours, what would you choose?",
        "What is something you are incredibly self-conscious about?",
        "Have you ever taken credit for something you didn't actually do?",
        "What is the most ridiculous rule your parents or bosses ever enforced?",
        "If you could permanently erase one memory from your mind, what would it be?",
        "What is the most awkward misunderstanding you have ever experienced?",
        "Have you ever snooped through a family member or friend's personal belongings?",
        "What is the worst movie you have ever watched from start to finish?",
        "If you could live anywhere in the world for one year, where would it be?",
        "What is the funniest or weirdest dream you can vividly remember?",
        "Have you ever pretended to be sick to stay home from school or work?",
        "What is the most unusual thing you are afraid of?",
        "If you could master any musical instrument instantly, what would it be?",
        "What is the most money you have ever spent on a single item (excluding a car/house)?",
        "Have you ever accidentally sent a text message to the wrong person?",
        "What is the most adventurous thing you have ever done outdoors?",
        "If you had to eat only one meal for the rest of your life, what would it be?",
        "What is a popular trend or fashion style that you absolutely cannot stand?",
        "Have you ever skipped a long queue or line when you shouldn't have?",
        "What is the best piece of advice you have ever received?",
        "If you could meet any historical figure, who would it be?",
        "What is the longest you've gone without sleeping, and why?",
        "Have you ever accidentally ruined a surprise party or a secret event?",
        "What is the most common misconception people have about you?",
        "If you won the lottery tomorrow, what is the very first thing you would buy?",
        "What is a chore or task you absolutely hate doing the most?",
        "Have you ever eaten food that fell on the floor past the 5-second rule?",
        "What is the most embarrassing nickname you have ever had?",
        "If you could speak any foreign language fluently, what would it be?",
        "What is the most physically painful experience you have ever endured?",
        "Have you ever gotten lost in a public place as an adult?",
        "What is your absolute favorite way to waste time or procrastinate?",
        "If you could safely pet any wild animal, which animal would you choose?",
    ],
    "dare": [
        "Do your best impression of a famous celebrity until someone guesses who it is.",
        "Speak in a formal British accent for the next three rounds of the game.",
        "Let another player completely restyle your hair using only safe, available items.",
        "Call a local business and ask them if they sell something highly unusual or fictional.",
        "Do 20 jumping jacks while chanting a funny phrase of your choice.",
        "Balance a spoon on the tip of your nose for a full 30 seconds.",
        "Eat a spoonful of a condiment you don't particularly like (e.g., hot sauce, mustard).",
        "Try to juggle three random items chosen by the group for at least 10 seconds.",
        "Give a highly detailed, 2-minute passionate speech about a completely boring object.",
        "Sing the chorus of your favorite song out loud at the top of your lungs.",
        "Wear your socks on your hands for the next two rounds of the game.",
        "Text a random, context-free word like 'Pineapple' to a close family member.",
        "Do a dramatic, slow-motion walk around the entire room or yard.",
        "Draw a funny face on your stomach or hand using a washable marker.",
        "Attempt to do a headstand or a handstand safely against a nearby wall.",
        "Blindfold yourself and try to identify three random household objects by touch alone.",
        "Speak only in rhymes for the next two rounds of the game.",
        "Let the group choose a funny nickname that you must answer to for the rest of the day.",
        "Do your best imitation of a roaring lion or a howling wolf.",
        "Walk backward everywhere you need to go for the next 10 minutes.",
        "Hold a plank position for a full 60 seconds without dropping.",
        "Put on a blindfold and let someone feed you a small bite of an unknown safe food item.",
        "Talk to a household object or a houseplant like it is your best friend for two minutes.",
        "Try to touch your nose with your tongue, or do your best unique physical trick.",
        "Do a funny runway model walk across the room while detailing your outfit.",
        "Keep your eyes wide open without blinking for a full 45 seconds.",
        "Wrap yourself entirely in a blanket like a burrito and stay that way for one round.",
        "Read the last text message you received out loud in a dramatic Shakespearean voice.",
        "Balance a book on your head and walk in a straight line across the room.",
        "Do 15 push-ups right now, or as many as you can safely manage.",
        "Drink a glass of water without using your hands at all.",
        "Act like a robot whenever it is your turn to speak for the next two rounds.",
        "Pretend you are an opera singer and sing your next sentence to the group.",
        "Allow the group to draw a tiny, safe temporary design on your cheek.",
        "Put your shirt on backward and wear it that way for the rest of the game.",
        "Spell your full name backward out loud as quickly as you possibly can.",
        "Do a funny dance move continuously for one full minute without stopping.",
        "Try to whistle a complex song clearly until someone correctly identifies it.",
        "Imitate a flight attendant giving a pre-flight safety announcement using items around you.",
        "Make up a short, 4-line poem about a random item in the room and recite it.",
        "Keep a completely straight, expressionless face while the group tries to make you laugh.",
        "Mime your favorite hobby or sport until someone correctly guesses what it is.",
        "Wear an oven mitt or a thick glove on your dominant hand for the next two rounds.",
        "Give a compliments marathon: say something genuinely nice to every single player.",
        "Balance on one foot with your eyes completely closed for 30 seconds.",
        "Repeat everything the person to your left says for the next full minute.",
        "Try to balance an upright broom or stick on your flat palm for 15 seconds.",
        "Whisper every sentence you say for the next two rounds.",
        "Do your best impression of a dynamic game show host introducing the next player.",
        "Pretend you are walking through thick, sticky mud every time you move for five minutes.",
    ]
}
a="yes"
def play():
    global a
    print("Welcome to Truth and Dare!")
    answer = input("Would you like a Truth or a Dare: ").lower()
    number=r.randint(1,50)
    if answer=="truth":
        print("Your truth is:")
        input(truths_and_dares["truth"][number])
        print("Thank you for playing truth and dare")
        a=input("Do you want to play again('y'or'n'): ")
    elif answer=="dare":
        print("Your dare is:")
        print(truths_and_dares["dare"][number])
        print("Thank you for playing truth and dare")
        a=input("Do you want to play again('y'or'n'): ")
    else:
        print("Invalid input. Please Rerun")
        a=input("Do you want to play again('y'or'n'): ")
while a=="yes":
    play()