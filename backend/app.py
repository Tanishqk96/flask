from flask import Flask, request, render_template 
import pandas as pd
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
