from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        #return "hello world!"
        return render_template('view_bucketlists.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    result = False
    if True:
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/add_bucketlist")
def add_bucketlist():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        #return "hello world!"
        return render_template('add_bucketlist.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
