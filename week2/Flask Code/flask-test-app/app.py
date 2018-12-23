from flask import Flask, render_template, abort
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    return render_template('user_index.html', username=username)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)
