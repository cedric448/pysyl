from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

#如果是POST操作，则设置cookie，并返回一个readcookie.html的页面
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
    return resp

#获取cookie，并打印本cookie (userID)的页面
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome, '+name+'</h1>'
