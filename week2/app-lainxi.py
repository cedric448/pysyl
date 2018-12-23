from flask import Flask
from flask import url_for
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def courses(name):
    return 'Courses:{}'.format(name)

#打印绝对路径，并重定向
@app.route('/test')
def test():
    print(url_for('courses', name='Java', _external=True))
    return redirect(url_for('index'))

#methods是规定格式。GET时获取参数是request.args.get()   POST时获取参数是request.form.get()
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
