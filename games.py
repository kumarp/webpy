import web
# Random is used for evens and odds game
import random

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
            return "You picked " + input.choice + "!\
            \nThe computer picks paper.\nThe computer wins!"
        elif input.choice == "scissors":
            return "You picked was " + input.choice + "!\
            \nThe computer picks rock.\nThe computer wins!"
        elif input.choice == "paper":
            return "You picked was " + input.choice + "!\
            \nThe computer picks scissors.\nThe computer wins!"
        else:
            return "Cheater"     


class guess:
    def GET(self):
        # Computer guesses what number is input in URI
        # Uses "random" import above
        input = web.input()
        # Generate a random number. If random is the same as input, computer wins
        random = random.randint(1,10)
        if int(input.number) > 10:
            return "Pick a number between 1 and 10"
        elif int(input.number) == random:
            return "Was your guess " + str(random) + "?\
            \nYes! I win!"
        else:
            return "Was your guess " + str(random) + "?\
            \nNo? I guess I lose..."


# More complicated game of evens and odds
# If evens URI is hit, play as evens
class evens:
    def GET(self):
        # Evens half of the evens and odds game.
        input = web.input()
        # Function below to play game
        return evenodds("evens", input.number)

# If odds URI is hit, play as odds
class odds:
    def GET(self):
        # Odds half of the evens and odds game.
        # Function below to play game
        input = web.input()
        return evenodds("odds", input.number)

# @param:
# choice: whether evens or odds is being played
# number: user's input of number chosen            
def evenodds(choice, number):
    # Generates a random number between 1 and 5
    # If playing evens and sum of random and player input is even, player wins
    # If playing odds and sum of random and player input is odd, player wins
    # Else, computer wins
    # Students might need a quick recap on %
    random = random.randint(1,5)
    total = random + int(number)
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
        return "Cheater"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()