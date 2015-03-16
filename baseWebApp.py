import web

urls = (
    '/', 'index',
    # first string - regex of URI, second string - class name
)

# class that is called when URI is hit
class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()