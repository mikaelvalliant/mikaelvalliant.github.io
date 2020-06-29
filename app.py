import flask
from flask import render_template, url_for

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def about():
    return render_template('index.md')


app.run()
