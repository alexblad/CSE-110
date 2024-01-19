
start_adventure=input('Hello there, would you like to go on an adventure? YES/NO ')
if start_adventure.lower()== 'yes':
    print('Good luck, let\'s hope you make it out alive...')
else:
    print('That\'s too bad, your fate has already been decided...')


print('You begin to fade away into a deep, deep sleep.')
print('As you cling to the last moments of consciousness, you hear these words')
print('\"Choices, choices, so many choices....\"')
print()
print('As you wake up, you can see that you are on a street you have nver seen before.')

answer=input('Will you go UP or DOWN the street? (UP/DOWN) ')

if answer.lower()== 'up':
    print('You see a bookshop witha a sign that catches your eye, \'Adventurer\'s wanted! Inquire within.')
    answer=input('Will you enter the bookshop? (YES/NO)')
    if answer.lower()=='yes':
        print('You enter the bookshop and are met by a cheery old man. \"Looking for an adventure?\" he says.')
        answer=input('Will you go on an ADVENTURE, or did you just want to look at BOOKS? (ADVENTURE/BOOKS) ')
        if answer.lower()=='adventure':
            print('''You decide to go on an adventure! You are soon introduced to you party of fellow adventurers and whisked away on many adventures,
             becoming a living legend! You grow old, and have made many memories. As you close your eyes for you last time you have no regrets.
             Then, you wake up! You are back at home in bed. Was it all just a dream? YOU WIN ''')
        else:
            print('''You tell the shop keeper that you were just hoping to browse his selection of books. He says, "Oh no worry, take all the time you need.”
             You find a book that seems rather interesting and as you begin to read you eyes grow heavy. You wake up back in your bed at home! Did you just 
             dream the whole thing? YOU ARE CONFUSED)''')
    elif answer.lower()=='no':
        print('You continue walking up the street, and see a man selling ice cream.')
        answer=input('Do you BUY some ice cream, STEAL some ice cream, or watch your weight and SKIP the ice cream? (BUY/STEAL/SKIP) ')
        if answer.lower()=='buy':
            print('You buy some ice cream, and start to eat it. As you are eating you start to feel weak… POISON! You are dead. YOU LOSE')
        elif answer.lower()=='skip':
            print('You skip the ice cream, it\'s almost summer! This desicion leads to you leading a life as a body builder...until you realize that this entire thing is a dream and you\'re stuck in it! YOU LOSE')
        else:
            print('The ice cream man was actually a monster in disguise! Enraged that you would dare steal from him he attacks you. You are dead. YOU LOSE')
else:
    print('You walk down the street and see a strange door')
    answer=input('You feel drawn to it. Will you enter the door? (YES/NO) ')
    if answer.lower()=='yes':
        print('You walk towards the door an enter it, you find yourself in a great hall. There seems to be no one around.')
        answer=input('Will you SEARCH for people, or WAIT for someone to show up? (SEARCH/WAIT)')
        if answer.lower()=='search':
            print('''You decide to search for anyone to find an explanation for all of this. Fortunately, eventually you find a group of guards.
             Unfortunately they were guarding the king, and think you are an assassin! They imprison you and you spend the rest of your few short
              days wasting away in a dungeon. YOU LOSE.''')
        else:
            print('''You wait in the hall. Eventually a group of men show up. They ask you where you came from, and as you tell them they actually believe you!
             They think you must be a wizard from another plane and offer you a place in the king\'s court as his personal wizard! You accept the job, and as you start
              your new life you feel a strange tingling in your fingers… YOU WIN!''')
    else:
        print('You continue to walk down the street and see some kids playing a game you\'ve never seen.')
        answer=input('Do you JOIN their game, or try to RETURN home? (JOIN/RETURN) ')
        if answer.lower()=='join':
            print('''You join the kids in their game, but as you try to learn the rules you can\'t seem to grasp them. Then you notice something strange, you feel smaller.
             You should be at least 2 feet taller than all these kids but you\'re the same height. A voice creeps into your mind, “Welcome my child, won\'t you play a game with us?”
              It was a trap! YOU LOSE''')
        else:
            print('''You start to make your way home. You ask around to figure out where you are and you\'re in your home town! Great, you may not recognize anything but surely
             you can make your way home eventually! However the more you try the less you trust that you are actually home. You spend the rest of you life wandering this labyrinth of a city.  
             YOU ARE LOST''')

print('THE END')