from flask import Flask, request, render_template , session, make_response
import pandas as pd
from flask_pymongo import PyMongo
app = Flask(__name__, template_folder="templates", static_folder='static', static_url_path='/')
app.secret_key = "sessionkey"
# ADDING MONGODB WITH FLASK
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db
@app.route('/')
def home():
    return "<h1>Hello, Flask!<h1/>"

@app.route('/mongo')
def mongo():
    db.inventory.insert_one({"b":2})
    return "inserted"
    
@app.route('/render')
def render():
    mylist=[1,2,3,4,5]
    return render_template('index.html', mylist=mylist)

# SETTING SESSIONS AND ALL THE RESPECTIVE OPERATIONS ON IT. 
#-------------------------------------------------------------
@app.route('/setsession')
def set_session():
    session['username'] = 'tanishq'  # Storing data in session
    return "Session set!"   

@app.route('/getsession')
def get_session():
    username = session.get('username', 'Not set')  # Retrieve session value
    return f"Stored username: {username}"

@app.route('/deletesession')
def delete_session():
    session.pop('username', None)  # Remove 'username' if it exists
    return "Session deleted!"

@app.route('/clearsession')
def clear_session():
    session.clear()  # Clears the entire session
    return "All session data cleared!"

#-------------------------------------------------------------
# SETTING COOKIES.
#-------------------------------------------------------------
@app.route('/setcookie')
def set_cookie():
    response = make_response("Cookie has been set!")
    response.set_cookie("username", "tanishq", max_age=60*60*24)  # Cookie expires in 1 day
    return response

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get("username", "No cookie found")  # Retrieve cookie
    return f"Stored username: {username}"

@app.route('/deletecookie')
def delete_cookie():
    response = make_response("Cookie deleted!")
    response.set_cookie("username", "", expires=0)  # Set expiry to delete cookie
    return response
#-------------------------------------------------------------


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
    
# uploading and reading files 
@app.route('/fileupload', methods=['GET','POST'])
def fileupload():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return "No file uploaded!", 400
        
        try:
            # Read file content as text
           # file_content = uploaded_file.read().decode('utf-8')
           file_content = pd.read_csv(uploaded_file)
           # either just read it normally or use pandas to read the csv 
        except Exception as e:
            return f"Error reading file: {e}", 500
        
        # Display the content (in a real app, you might want to render a template)
        return f"<h1>Uploaded File Content</h1><pre>{file_content}</pre>"

    
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
