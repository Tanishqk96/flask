from flask import Flask, request, render_template 

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return "<h1>Hello, Flask!<h1/>"

@app.route('/render')
def render():
    mylist=[1,2,3,4,5]
    return render_template('index.html', mylist=mylist)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == "GET":
        return  render_template('form.html')
    elif request.method == "POST":
        #username = request.form.get('username')
       # password = request.form.get('password')
   # return f"{username} {password}"
        form_data = request.form.to_dict()
        return f"Form Data: {form_data}"
    # any way is possible, second one gives whole body of the written code. 
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
