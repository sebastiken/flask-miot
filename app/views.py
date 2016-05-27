from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Pappo'}
    return render_template('index.html',
                           title='Home',
                           user=user)

