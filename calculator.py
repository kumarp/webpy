import web

urls = (
    '/', 'index',
    '/number', 'number',
    '/multi', 'multi',
    '/range', 'range',
    '/binary', 'binary'
)

class index:
    def GET(self):
    	# Homepage and information about what each page does
        return "Homepage:\n\nThis is a website calculator.\
        	\nGo to /number to see the number you entered\
        	\nGo to /multi to see the number multiplied by 1,2,5,10,25, and 100\
        	\nGo to /range to see what range of numbers your number is between\
        	\nGo to /binary to convert your number to binary"

class number:
    def GET(self):
        # gets a number and then displays it
        # good first step for students
        input = web.input()
        return input.number

class multi:
    def GET(self):
        # gets a number and then shows that number multiplied by 2,5,10,25, and 100
        # students may be interested in finding how large of a number they can enter
        input = web.input()
        num = int(input.number)
        return str(num*2) + "\n" + str(num*5) + "\n" + str(num*10) \
        + "\n" + str(num*25) + "\n" + str(num*100)

class range:
	def GET(self):
		# gets a number and then displays the range the number is in
		input = web.input()
		num = int(input.number)
		if num < 10:
			return "The number is less than 10"
		elif num >= 10 and num < 100:
			return "The number is between 10 and 100"
		elif num >= 100 and num <= 1000:
			return "The number is between 100 and 1000"
		else:
			return "The number is greater than 1000"

class binary:
    def GET(self):
        # gets a number and then shows the binary value of that number
        # coders know what binary is, so this may be of interest to them
        # normally "0b" is given in front of the number (as in the first output)
        # the second output gives the binary number without the "0b"
        input = web.input()
        num = int(input.number)
        return str(bin(num)) + "\n" + str(bin(num)[2:])

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()