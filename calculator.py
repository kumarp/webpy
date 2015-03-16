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
        # Displays number entered in URI
        # Can be used as a first step
        input = web.input()
        return input.number

class multi:
    def GET(self):
        # Gets a number from URI and displays that number multiplied by 2,5,10,25, and 100
        # Can be modified to whatever the students want
        input = web.input()
        num = int(input.number)
        return "x2: " + str(num*2) + "\nx5: " + str(num*5) + "\nx10: " + str(num*10) \
        + "\nx25: " + str(num*25) + "\nx100: " + str(num*100)

class range:
	def GET(self):
		# Gets a number from URI and displays which of the following ranges the number is in:
        #  < 10
        # 10 - 100
        # 100 - 1000
        # > 1000
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
        # Gets a number and then shows the binary value of that number
        # When converting to binary, the output is displayed with "0b" appended to the front
        # The second output shows the binary number without the "0b"
        input = web.input()
        num = int(input.number)
        return str(bin(num)) + "\n" + str(bin(num)[2:])

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()