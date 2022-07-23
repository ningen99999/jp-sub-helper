# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '''補助記号<br>
                名詞<br>
                助詞<br>
                動詞<br>
                助動詞<br>
                接尾辞<br>
                形状詞<br>
                連体詞<br>
                接頭辞<br>
                代名詞<br>
                接続詞<br>
                副詞<br>
                形容詞<br>
                感動詞<br>
                記号<br>
                空白<br>'''


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()