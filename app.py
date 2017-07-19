"""Bucketlist Application"""
import os

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

#empty dictionary to hold data initialization
database = dict()


@app.route('/', methods=['GET'])
def home():
    '''Defines the home route'''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        #return "hello world!"
        return render_template('view_bucketlists.html')

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    '''Login method'''
    if request.method == 'POST':
        post_data = request.form.to_dict()

        username = post_data.get('username')
        password = post_data.get('password')

        if username not in database:
            return "username not associated with any accounts"

        for key, value in database:
            if key == username:
                if value == password:
                    session['logged_in'] = True
                else:
                    flash('wrong username password combination')
    return home()

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''method that handles user registration'''
    if not session.get('logged_in'):
        if request.method == 'GET':
            return render_template('register.html')
        else:
            post_data = request.form.to_dict()

            username = post_data.get('email')
            password = post_data.get('password')
            confirm_password = post_data.get('confirm_password')

            if not username:
                return "Username cant be empty"
            if not password == confirm_password:
                return "Password missmatch"
    else:
        return render_template('view_bucketlists.html')

    database[username] = password
    session['logged_in'] = True
    session['user'] = username
    return register()

@app.route("/logout")
def logout():
    '''This method logs out a user, deleting their username from the session'''
    session['logged_in'] = False
    session.pop('user', None)

    return home()


@app.route("/add_bucketlist")
def add_bucketlist():
    '''function that handles user input for adding bucketlist'''
    check_login('add_bucketlist.html')


def check_login(option: ""):
    '''reusable function for checking whether a user is logged in
        takes in template name requested and returns login if user not logged in
        or loads desired view if user logged in'''
        
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template(option)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
