from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__ , template_folder= 'templates' , static_folder= 'static')
app.config['SECRET_KEY']="maDIzaBady"


firebaseConfig = {
  "apiKey": "AIzaSyAaONmOwTHqpgworT0gg7x1AvqYeKZilOI",
  "authDomain": "authentication-lab-3f8c6.firebaseapp.com",
  "projectId": "authentication-lab-3f8c6",
  "storageBucket": "authentication-lab-3f8c6.appspot.com",
  "messagingSenderId": "85167981563",
  "appId": "1:85167981563:web:fd4804e525bc93772f415e",
  "measurementId": "G-GL6E2HPHQK", 
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



@app.route('/' , methods= ['GET' , 'POST'])
def signup():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    login_session['qoutes']= []
    try:
      user = auth.create_user_with_email_and_password(email, password)
      login_session['user'] = user
      return redirect(url_for('home'))
    except:
      error = "oopsie"
      return render_template("signup.html", error=error)
  return render_template('signup.html')

@app.route('/signin', methods= ['GET' , 'POST'])
def signin():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    login_session['qoutes']= []
    user = auth.signin_user_with_email_and_password(email, password)
    login_session['user'] = user
    return redirect(url_for('home'))
  return render_template('signin.html')

@app.route('/home', methods= ['GET' , 'POST'])
def home():
  if request.method == "POST":
    quote = request.form['quote']
    if 'quotes' not in login_session: 
      login_session['quotes'] = []
    login_session['qoutes'].append(quote)
    return redirect(url_for('thanks'))
  return render_template('home.html')

  # if 'user' in login_session:
  #   return render_template('home.html', email=login_session['user']['email'])
  # return redirect(url_for('sig'))

@app.route('/signout', methods= ['GET' , 'POST'])
def signout():
  if request.method == "POST":
    login_session['user'] = None
    auth.current_user = None 
  return redirect(url_for('signin'))

@app.route('/thanks', methods= ['GET' , 'POST'])
def thanks():
  return render_template('thanks.html')

@app.route('/display', methods= ['GET' , 'POST'])
def display():
  if request.method == "POST":
    quotes = request.form['quotes']
    login_session['quotes'] = quotes
  return render_template('display.html')
  



if __name__ == '__main__':
    app.run(debug = True)