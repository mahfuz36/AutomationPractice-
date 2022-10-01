import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', method=['GET'])
def home():
    return "<h1>Hello World</h1> <p> This is API Test"

app.run()