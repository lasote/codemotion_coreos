from bottle import route, run


@route('/')
def index():
    return '<h1>Hello! I AM YOUR WEBAPI</h1>'

run(host='0.0.0.0', port=8080)