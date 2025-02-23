from flask import Flask, request, render_template 

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "<h1>Hello, Flask!<h1/>"

@app.route('/render')
def render():
    return render_template('index.html')

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == "GET":
        return "get request"
    elif request.method == "POST":
        return "post request"
    
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
