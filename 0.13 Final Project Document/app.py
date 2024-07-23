from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__ , template_folder= 'templates' , static_folder= 'static')
app.config['SECRET_KEY']="maDIzaBady"


firebaseConfig = {
  "apiKey": "AIzaSyDDSfRPSEcmAo5J0CUpLpL3RY5J540S0dI",
  "authDomain": "restaurant-reviews-ad184.firebaseapp.com",
  "projectId": "restaurant-reviews-ad184",
  "storageBucket": "restaurant-reviews-ad184.appspot.com",
  "messagingSenderId": "863455497320",
  "appId": "1:863455497320:web:f94501caa7554c1e3a3fdd",
  "measurementId": "G-6MNPCNPN1F",
  "databaseURL": "https://restaurant-reviews-ad184-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



@app.route('/' , methods= ["POST" , "GET"])
def signup():
  if request.method == "POST":
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    user_data = {"email": email,
    "username": username,
    "password": password
    }
    try:
      user = auth.create_user_with_email_and_password(email, password)
      login_session['user'] = user
      db.child("users").child(user['localId']).set(user_data)
      return redirect(url_for('home'))
    except:
      return 'Oopsie! something went wrong, please try again'
  else:
    return render_template('signup.html')

@app.route('/signin', methods = ["GET" , "POST"])
def signin():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    try:
      user = auth.signin_user_with_email_and_password(email, password)
      login_session['user'] = user
      login_session.modified = True
      return redirect(url_for('home'))
    except:
      return 'Oopsie! something went wrong, please try again'
  return render_template('signin.html')

@app.route('/home' , methods = ["GET" , "POST"])
def home():
  if request.method == "GET":
    return render_template('home.html')
  else:
    rest_name = request.form['rest_name']
    link = request.form['link']
    review = request.form['review']



    added = {"rest_name": rest_name,
    "link": link,
    "review": review
    }
    login_session['reviews'] = []
    login_session['reviews'].append(added)
    # login_session['reviews']=login_session['reviews'].append(added)
    login_session.modified = True

    db.child("reviews").push(added)
    return redirect(url_for('home'))


@app.route('/profile', methods = ["GET" , "POST"])
def profile():
  return render_template('profile.html')

@app.route('/signout', methods = ["GET" , "POST"])
def signout():
  login_session.clear()
  return render_template('signin.html')



  
if __name__ == '__main__':
    app.run(debug = True)