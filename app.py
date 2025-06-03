from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Welcome</title>
            </head>
            <body>
                <h1>Hello from Flask!</h1>
                <p>This is the home page.</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
