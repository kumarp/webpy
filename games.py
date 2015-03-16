import web
import random # needed for the guess and the evens and odds game

urls = (
    '/', 'index',
    '/RPS', 'RPS',
    '/guess', 'guess',
    '/evens', 'evens',
    '/odds','odds')

class index:
    def GET(self):
        return "This website has three games\
        \nThe first game is rock, paper, scissors,\
        \npick your choice and the computer picks theirs.\
        \nIn the second game the computer tries to guess a number between 1 and 10.\
        \nIn the third game, pick evens or odds and your number."

class RPS:
    def GET(self):
        # A rock paper scissors game where the computer always wins.
        input = web.input()
        if input.choice == "rock":
            return "Your choice was " + input.choice + "!\
            \nThe computer picks paper.\nThe computer wins!"
        elif input.choice == "scissors":
            return "Your choice was " + input.choice + "!\
            \nThe computer picks rock.\nThe computer wins!"
        elif input.choice == "paper":
            return "Your choice was " + input.choice + "!\
            \nThe computer picks scissors.\nThe computer wins!"
        else:
            return "invalid input"     


class guess:
    def GET(self):
        # you need to import random for the code to work.
        # the computer tires to guess the number inputed.
        input = web.input()
        ran = random.randint(1,10)
        if int(input.number) > 10:
            return "Pick a number between 1 and 10"
        elif int(input.number) == ran:
            return "Was your guess " + str(ran) + "?\
            \nYes! I win!"
        else:
            return "Was your guess " + str(ran) + "?\
            \nNo? I guess I lose..."


# This game is probably too advanced for most of the students.
# However, it is a good introduction and use of functions.
class evens:
    def GET(self):
        # Evens half of the evens and odds game.
        input = web.input()
        return evenodds("evens", input.number)

class odds:
    def GET(self):
        # Odds half of the evens and odds game.
        input = web.input()
        return evenodds("odds", input.number)
            
def evenodds(choice, number):
    # You need to import random for code to work
    # the human picks evens or odds and a number
    # computer generates a random number between 1 and 5
    # then the winner of the game is determined based on the total
    # coders will need a reminder of what modulus is and an explaination of random
    ran = random.randint(1,5)
    total = ran + int(number)
    remainder = total%2
    
    if choice == "evens" and remainder == 0:
        return "The total was " + str(total) + ".\nYou win."
    elif choice == "evens" and remainder == 1:
        return "The total was " + str(total) + ".\nThe computer wins."
    elif choice == "odds" and remainder == 0:
        return "The total was " + str(total) + ".\nThe computer wins."
    elif choice == "odds" and remainder == 1:
        return "The total was " + str(total) + ".\nYou win."
    else:
        return "invalid input"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()