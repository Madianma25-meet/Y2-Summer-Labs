from flask import Flask, render_template , request, redirect, url_for
import random
app = Flask(__name__)
my_fortunes = ["A fresh start will put you on your way." , "A golden opportunity is coming your way." , "Adventure awaits you this weekend." , "An exciting opportunity lies ahead of you." , "Believe in yourself and others will too." , "Change is coming; embrace it with open arms." , "Good news will be brought to you by mail." , "Happiness begins with facing life with a smile and a wink." ,"Now is the time to try something new." , "Your ability for accomplishment will follow with success."]


@app.route('/home', methods=['GET' , 'POST'])
def home():
	if request.method == "POST":
		birth_month = request.form['birth_month']
		chosen = random.choice(my_fortunes)
		return redirect(url_for('fortune', birth_month=birth_month))
		# return render_template('fortune.html', fortune=chosen, birth_month=birth_month)
	return render_template('home.html')
@app.route('/fortune/<birth_month>')
def fortune(birth_month): 

	if birth_month:
		index = len(birth_month) 
		
	else:
		chosen = random.choice(my_fortunes)
	if index < 10:
		chosen = my_fortunes[index]
		return render_template("fortune.html" , fortune=chosen, birth_month=birth_month)
	else:
		return render_template("too_long.html")


if __name__ == '__main__':
    app.run(debug = True)