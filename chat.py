import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

messages =[]

@app.route("/")
def get_index():
    return render_template('index.html')
    
@app.route('/login')
def login():
    username = request.args.get('username')
    return redirect(username)
    
@app.route('/<username>')
def get_username(username):
    return str(messages)

@app.route('/<username>/<message>')
def add_message(username, message):
    message = "<strong>{0}:</strong> {1}".format(username, message)
    messages.append(message)
    return str(messages)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

