from flask import Flask
from flask import render_template, redirect, url_for, request, session, flash
from flask import request
import savedData as saved

app = Flask(__name__)
app.secret_key = "smart_lock"

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/new', methods=['POST', 'GET'])
def new():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		saved.addUser(username, password)
		#users = saved.retrieveUsers()
		#return render_template('index.html', users=users)
	#else:
	return render_template('index.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Try again'
		else:
			session['logged_in'] = True
			flash('Logged in!')
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Logged out')
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080)
	