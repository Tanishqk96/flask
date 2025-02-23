from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!<h1/>"

@app.route('/xy')
def xy():
    return "hello"

@app.route('/xyz/<name>')
def xyz(name):
    return f" Hellow {name} !"

# url will be something like this 
# http://127.0.0.1:5555/handleurl?name=tanishq&greeting=hey
@app.route('/handleurl')
def handleurl():
    if 'greeting' in request.args.keys() and 'name' in  request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f" {greeting} , {name}"
    
if __name__ == '__main__':
    app.run(debug=True, port=5555,)
