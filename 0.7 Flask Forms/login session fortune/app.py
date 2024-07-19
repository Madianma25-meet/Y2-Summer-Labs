from flask import Flask, render_template , request, redirect, url_for
from flask import session as login_session
import random
app = Flask(__name__ , template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY']= "PASSY"
my_fortunes = ["A fresh start will put you on your way." , "A golden opportunity is coming your way." , "Adventure awaits you this weekend." , "An exciting opportunity lies ahead of you." , "Believe in yourself and others will too." , "Change is coming; embrace it with open arms." , "Good news will be brought to you by mail." , "Happiness begins with facing life with a smile and a wink." ,"Now is the time to try something new." , "Your ability for accomplishment will follow with success."]



@app.route('/', methods=['GET' , 'POST'])
def login():
	if request.method == "POST":
		username = request.form['username']
		birth_month = request.form['birth_month']
		if birth_month:
			index = len(birth_month)
			if index < 10:
				chosen = my_fortunes[index]
				return redirect(url_for('home'))
		else:
			chosen = random.choice(my_fortunes)
			login_session['username'] = username
			login_session['birth_month'] = birth_month
			login_session['fortune'] = chosen
		
	return render_template('login.html')
	
@app.route('/home')
def home():
	if 'username' not in login_session or 'birth_month' not in login_session:
		return redirect(url_for('login'))
	username = login_session['username']
	birth_month = login_session['birth_month']
	return render_template('home.html', username=username, birth_month=birth_month)


@app.route('/fortune/<birth_month>')
def fortune(birth_month):
	if 'fortune' not in login_session or login_session['birth_month'] != birth_month:
		return redirect(url_for('login'))
	fortune = login_session['fortune']
	return render_template('fortune.html', fortune=fortune)
@app.route('/too_long')
def too_long():
	return render_template('too_long.html')

if __name__ == '__main__':
    app.run(debug = True)