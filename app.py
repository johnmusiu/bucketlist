"""Bucketlist Application"""
import os
#import logging

from flask import Flask, url_for, redirect, render_template, request, session, flash#, abort

app = Flask(__name__)

#empty dictionary to hold data initialization
database = {}
db_bucketlists = {}

#database['admin'] = "password"


@app.route('/', methods=['GET'])
def home():
    '''Defines the home route'''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('view_bucketlists.html')


@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    '''Login method'''
    errors = None
    if request.method == 'POST':
        post_data = request.form.to_dict()

        # username = post_data.get('username')
        # password = post_data.get('password')
        #logging.warning(username)
       # errors = "Username not found"
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                errors = "Invalid credentials, please try again!"
            else:
                session['logged_in'] = True
                flash("Login success!")
                return redirect(url_for('add_bucketlist'))
            return render_template('login.html', error=errors)
        # if username not in database:
        #     return render_template('login.html', error=errors)

        # for key, value in database.items():
        #     if key == username:
        #         if value == password:
        #             session['logged_in'] = True
        #             session['user'] = username
        #             return redirect(url_for('add_bucketlist'))
        #         elif value != password:
        #             return render_template(
        #                 'login.html', error="wrong username password combination")
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
        return render_template('add_bucketlist.html')

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


@app.route("/add_bucketlist", methods=['GET', 'POST'])
def add_bucketlist():
    '''function that handles user input for adding bucketlist'''
    alerts = ""
    if not session.get('logged_in'):
        return render_template('login.html', error="Your session expired, login again!")
    else:
        if request.method == 'POST':
            post_data = request.form.to_dict()

            title = post_data.get('bucketlist')
            desc = post_data.get('description')

            db_bucketlists[title] = desc
            alerts = "inserted successfully"
            return render_template('add_bucketlist.html', alert=alerts)

        else:
            return render_template('add_bucketlist.html')


@app.route("/view_bucketlists", methods=['GET', 'POST'])
def view_bucketlists():
    ''' lists bucketlists in a table format'''
    if not session.get('logged_in'):
        return render_template('login.html', error="Your session expired, login again!")
    else:
        bucketlist_view = {}
        if request.method == 'GET':
            bucketlist_view = db_bucketlists
    return render_template('view_bucketlists.html', blist=bucketlist_view)


@app.route("/delete_bucketlist", methods=['GET', 'POST'])
def delete_bucketlist():
    ''' deletes a bucketlist item then reloads the bucketlists page '''
    if not session.get('logged_in'):
        return render_template('login.html', error="Your session expired, login again!")
    else:
        alerts = ""
        if request.method == 'POST':
            post_data = request.form.to_dict()
            key = post_data.get('key')
            print(key)
            # if key in db_bucketlists.items():
            del db_bucketlists[key]
            alerts = "Deleted successfully"
            # else:
                # alerts = "item you are trying to delete was not found"
        return render_template('view_bucketlists.html', blist=db_bucketlists)

@app.route("/edit_bucketlist", methods=['GET', 'POST'])
def edit_bucketlist():
    ''' edits a bucketlist '''
    if not session.get('logged_in'):
        return render_template('login.html', error="Your session expired, login again!")
    else:
        if request.method == 'POST':
            post_data = request.form.to_dict()

            new_title = post_data.get('key')
            new_desc = post_data.get('value')
            org_key = post_data.get('org_key')
            db_bucketlists[new_title] = ""
            db_bucketlists[new_title] = db_bucketlists.pop(org_key)
            db_bucketlists[new_title] = new_desc
            alerts = "inserted successfully"
            return render_template('view_bucketlists.html', blist=db_bucketlists)
        else:
            return render_template('view_bucketlist.html', blist=db_bucketlists)
        
        

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
