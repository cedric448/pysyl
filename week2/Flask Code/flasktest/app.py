from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html', coursename=name)

@app.route('/test')
def test():
    print(url_for('courses', name='Java', _external=True))
    return redirect(url_for('index')) 

@app.route('/httptest', methods=['GET', 'POST'])
def httptest():
    #print('method:', request.method)
    if str(request.method) == 'GET':
        print('t:', request.args.get('t'))
        print('q:', request.args.get('q'))
        return('It is a get request!')
    elif str(request.method) == 'POST':
        print('Q:',request.form.getlist('Q'))
        return('It is a post request!')


if __name__ == '__main__':
    app.run()
