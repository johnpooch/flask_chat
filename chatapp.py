import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Stores messages between requests
messages = []



@app.route("/")
def get_index():
    return render_template("index.html")
    
    
@app.route("/login")
def do_login():
    username = request.args['username']
    return redirect(username)
    

@app.route("/<username>")
def get_userpage(username):
    return render_template("chat.html", logged_in_as=username, all_the_messages=messages)


@app.route("/new", methods=["POST"])
def add_message():
    username = request.form['username']
    text = request.form['message']
    
    words = text.split()
    naughtyWords = set(["dang", "crud", "willy", "fudge"])
    words = [ "*" * len(word) if word.lower() in naughtyWords else word for word in words]
    
    text = " ".join(map(str, words))
    
    message = {
        'sender': username,
        'body': text,
    }
    
    messages.append(message)
    return redirect(username)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))