import web

urls = (
    '/', 'index',
    # first string - regex of URI, second string - class name
    '/square', 'square',
    '/triangle', 'triangle',
    '/diamond', 'diamond',
    '/shape', 'shape'
)

class index:
    def GET(self):
        return "This webpage displays different shapes in ASCII art"

def asciiSquare():
    return "**\n**"

def asciiTriangle():
    return "  *  \n *** \n*****"

def asciiDiamond():
    return "  *  \n *** \n  *  "

class square:
    def GET(self):
        return asciiSquare()

class triangle:
    def GET(self):
        return asciiTriangle()

class diamond:
    def GET(self):
        return asciiDiamond()

class shape:
    def GET(self):
        input = web.input()
        if input.shape == "square":
            return asciiSquare()
        elif input.shape == "triangle":
            return asciiTriangle()
        elif input.shape == "diamond":
            return asciiDiamond()
        else:
            return "Not Defined"
  
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()