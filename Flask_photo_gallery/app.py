from flask import Flask

app = Flask(__name__)

#routes
@app.route('/')
def home():
    return("<html><head>Welcome to the amazing photo gallery</head><a href = '/food1'>  Shawarma</a><a href = '/cat'>  Cat</a><a href = '/food3'>  Steak</a><a href = '/earth'>  Earth</a></html>")
    #mystrings = "Welcome to the amazing gallery <a href = '/food1'> Shawarma</a>"
    #return mystrings

@app.route('/food1')
def food1():
    return ("<html><img src = 'https://cdn.britannica.com/49/236649-050-2F5C65AB/Shawarma-chef-using-a-knife-to-shave-chicken-shawarma-off-of-a-vertical-rotating-spit.jpg' width= '400px'><a href = '/'>  Go to Homepage</a><a href = '/food2'>    Cookies</a></html>")
@app.route('/food2')
def food2():
    return ("<html><img src = 'https://img.taste.com.au/puSNvmqQ/taste/2010/01/chocolate-chip-cookies-cropped-199866-1.jpg' width= '400px'><a href = '/food3'>  Steak</a></html>")
@app.route('/food3')
def food3():
    return ("<html><img src = 'https://iowagirleats.com/wp-content/uploads/2015/06/Perfect-Grilled-Steak-with-Herb-Butter-iowagirleats-03srgb.jpg' width= '400px'><a href = '/'>Homepage</a></html>")
@app.route('/cat')
def cat():
    return ("<html><img src = 'https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg' width= '400px'><a href = '/goat'>Goat</a><a href = '/cow'>Cow</a></html>")
@app.route('/goat')
def goat():
    return ("<html><img src = 'https://images2.minutemediacdn.com/image/upload/c_fill,w_1200,ar_1:1,f_auto,q_auto,g_auto/shape/cover/sport/iStock-177369626-1-0e8d40eaabe65d2cb2d745ef45f09229.jpg' width= '400px'><a href = '/cat'>Cat</a><a href = '/cow'>Cow</a></html>")
@app.route('/cow')
def cow():
    return ("<html><img src = 'https://www.treehugger.com/thmb/PVOiWku5eio3Tzu40yV6xV9vFlk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cow-playfully-cuddling-another-young-cow-lying-down-in-a-field-under-a-blue-sky--calves-love-each-other-1282528841-cb3871fc5b7a4d6082a4a8b35614e4df.jpg' width= '400px'><a href = '/cat'>Cat</a></html>")
@app.route('/earth')
def earth():
    return ("<html><img src = 'https://media.npr.org/assets/img/2013/03/06/bluemarble3k-smaller-nasa_custom-83176a970ec83a1b9e7fc285674472bb1b4e585e.jpg' width= '400px'><a href = '/mars'>  Mars</a><a href = '/solarsystem'>  Solar System</a><a href = '/home'>  Homepage</a></html>")
@app.route('/mars')
def mars():
    return ("<html><img src = 'https://www.airedalesprings.co.uk/wp-content/uploads/2016/08/mars-iStock_000026519382_Large-1024x766.jpg' width= '400px'><a href = '/earth'>  Earth</a><a href = '/solarsystem'>  Solar System</a></html>")
@app.route('/solarsystem')
def solar():
    return("<html><img src = 'https://science.nasa.gov/wp-content/uploads/2023/07/pia06890-our-solar-system-banner-1920x640-1.jpg?w=4096&format=jpeg' width= '400px'><a href = '/earth'>  Earth</a><a href = '/mars'>  Mars</a></html>")



if __name__ == '__main__':
    app.run(debug=True)