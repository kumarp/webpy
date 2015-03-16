import web

urls = (
    '/', 'index',
    # first string - regex of URI, second string - class name
    '/number', 'number',
    '/generation', 'generation',
    '/strengths', 'strengths'
)

class index:
    def GET(self):
        return "This website displays basic information on Pokemon"

#Prints the name of the pokemon when number is input
class number:
    def GET(self):
        input = web.input()
        if( int(input.number) == 1 ):
            return "Bulbasaur"
        elif ( int(input.number) == 4):
            return "Charmander"
        elif ( int(input.number) == 7):
            return "Squirtle"

#Prints the generation of the pokemon when number is input
class generation:
    def GET(self):
        input = web.input()
        number = int(input.number)
        if number > 1 and number <= 151:
            return "Generation 1"
        elif number >= 152 and number <= 251:
            return "Generation 2"
        elif number >= 252 and number <= 386:
            return "Generation 3"
        elif number >= 387 and number <= 493:
            return "Generation 4"
        elif number >= 494 and number <= 649:
            return "Generation 5"
        elif number >= 650 and number <= 721:
            return "Generation 6"
        else:
            return "Not a valid number"

def fire():
    strengths = "Strong Against: Bug, Grass, Ice"
    weaknesses = "Weak Against: Rock, Fire, Water, Dragon"
    return strengths + "\n" + weaknesses

def water():
    strengths = "Strong Against: Ground, Rock, Fire"
    weaknesses = "Weak Against: Water, Grass, Dragon"
    return strengths + "\n" + weaknesses

def grass():
    strengths = "Strong Against: Ground, Rock, Water"
    weaknesses = "Weak Against: Flying, Poison, Bug, Fire, Grass, Dragon"
    return strengths + "\n" + weaknesses

class strengths:
    def GET(self):
        input = web.input()
        type = input.type
        if type == "fire":
            return fire()
        elif type == "water":
            return water()
        elif type == "grass":
            return grass()
        else:
            return "No information available"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()