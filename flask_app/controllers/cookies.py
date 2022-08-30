from flask import render_template
from flask_app import app


@app.route('/cookies')
def r_cookies():
    return render_template('cookies.html')