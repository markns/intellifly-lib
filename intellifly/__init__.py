from flask import Flask

from test import function

app = Flask(__name__)

if __name__ == '__main__':
    app.add_url_rule('/', 'index', function.index)
    app.run()
