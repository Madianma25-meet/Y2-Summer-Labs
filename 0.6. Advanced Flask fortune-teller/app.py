from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route('/home')
def home():
	return render_template("home.html")
my_fortunes = ["A fresh start will put you on your way." , "A golden opportunity is coming your way." , "Adventure awaits you this weekend." , "An exciting opportunity lies ahead of you." , "Believe in yourself and others will too." , "Change is coming; embrace it with open arms." , "Good news will be brought to you by mail." , "Happiness begins with facing life with a smile and a wink." ,"Now is the time to try something new." , "Your ability for accomplishment will follow with success."]
@app.route('/fortune')
def fortune():
	chosen = random.choice(my_fortunes)
	return render_template("fortune.html" , fortune=chosen)
if __name__ == '__main__':
    app.run(debug = True)