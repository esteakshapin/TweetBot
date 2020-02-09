from flask import Flask, render_template, session
import json
from make import m
app = Flask(__name__, static_folder='./static', template_folder='./templates')
startScreenBool = True
playScreenBool = False

app.secret_key= "6yTWFOE7j05WpVr8ic"
 

app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/', methods=['GET'])
def home():
  if 'startScreenBool' not in session:
    session['startScreenBool'] = True
    session['playScreenBool'] = False
    name = session.get('startScreenBool')
    print(name)


  return render_template(
    'index.html'
  )

@app.route('/game', methods=['GET'])
def game_page():
  return render_template(
    'game.html',
    startScreen = session.get('startScreenBool', True), 
    playScreen = session.get('playScreenBool', False) 
  )

@app.route('/startGame', methods=['POST'])
def startGame():
  global startScreenBool
  global playScreenBool
  session['startScreenBool'] = False
  session['playScreenBool'] = True
  return 'success'
  

@app.route('/learn', methods=['GET'])
def learn_page():
  return render_template(
    'learn.html'
  )

@app.route('/film', methods=['GET'])
def film_page():
  return render_template(
    'film.html'
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')


#useful modules
#picking -> method of database storage: can preserve classes
#www.MYURL/showcase.com#isFake?=True
