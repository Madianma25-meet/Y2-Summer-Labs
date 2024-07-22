from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__ , template_folder= 'templates' , static_folder= 'static')
app.config['SECRET_KEY']="maDIzaBady"


firebaseConfig = {
  "apiKey": "AIzaSyAaONmOwTHqpgworT0gg7x1AvqYeKZilOI",
  "authDomain": "authentication-lab-3f8c6.firebaseapp.com",
  "projectId": "authentication-lab-3f8c6",
  "storageBucket": "authentication-lhttps://github.com/meet-projects/Y2-Summer-Labs/tree/master/0.9%20Firebase%20Realtime%20Databaseab-3f8c6.appspot.com",
  "messagingSenderId": "85167981563",
  "appId": "1:85167981563:web:fd4804e525bc93772f415e",
  "measurementId": "G-GL6E2HPHQK", 
  "databaseURL": "https://authentication-lab-3f8c6-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



@app.route('/' , methods= ['GET' , 'POST'])
def signup():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    full_name = request.form['full_name']
    username = request.form['username']

    user_data = {"full_name": full_name,
    "email": email,
    "username": username
    }

    user = auth.create_user_with_email_and_password(email, password)
    login_session['user'] = user
    login_session['quotes']= []
    login_session.modified = True

    db.child("users").child(user['localId']).set(user_data)


    return redirect(url_for('home'))
  return render_template('signup.html')

@app.route('/signin', methods= ['GET' , 'POST'])
def signin():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    login_session['quotes']= []
    user = auth.signin_user_with_email_and_password(email, password)
    login_session['user'] = user
    login_session.modified = True
    return redirect(url_for('home'))
  return render_template('signin.html')

@app.route('/home', methods= ['GET' , 'POST'])
def home():
  if request.method == "POST":
    text = request.form['text']
    said_by = request.form['said_by']

    quote = {"text": text,
     "said_by": said_by,
     "uid": login_session['user']['localId']}

    login_session['quotes'].append(quote)
    login_session.modified = True

    db.child("Quotes").push(quote)

    return redirect(url_for('thanks'))
  return render_template('home.html')

@app.route('/signout', methods= ['GET' , 'POST'])
def signout():
  login_session.clear()
  return redirect(url_for('signin'))

@app.route('/thanks', methods= ['GET' , 'POST'])
def thanks():
  return render_template('thanks.html')

@app.route('/display', methods= ['GET' , 'POST'])
def display():
  
  return render_template('display.html', quotes=db.child("Quotes").get().val())
  



if __name__ == '__main__':
    app.run(debug = True)