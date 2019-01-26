from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Paul'}
    return '''

<html>
    <head>
        <title>Home page</title>
    </head>
    <body>
        <h1>Greetings, ''' + user['username'] + '''!</h1>
    </body>
</html>'''