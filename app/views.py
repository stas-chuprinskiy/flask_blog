from flask import render_template

from app import app


@app.route('/')
def index():
    name = 'Stanislav'
    return render_template('index.html', name=name)
