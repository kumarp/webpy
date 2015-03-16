import web

urls = (
    '/', 'index',
    # first string - regex of URI, second string - class name
    # ex: localhost:8080/parameter will call the parameter class below
    '/parameter', 'parameter',
    '/ifStatement', 'ifStatement',
    '/function','function')

class index:
    def GET(self):
        return "Hello, world!"

# class that gets called when URI is hit
class parameter:
    def GET(self):
        # Creates tuple with input from URI
        # ex: URI localhost:8080/parameter?name=Fido will print "Bye, Fido!"
        # Pull value of tuple by key provided through URI
        input = web.input()
        return "Bye, " + input.name + "!"

class ifStatement:
    def GET(self):
        # Syntax for a simple if statement using numbers
        # Inputs are always read as a string, so the input is cast to an int
        input = web.input()
        if(int(input.number) < 10):
           return "The number is less than 10!"
        else:
            return "The number is greater than or equal to 10!"
            
def printAsciiArt():
    return " ><(((('>  "

# Sample that uses a function
class function:
    def GET(self):
        return printAsciiArt()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()