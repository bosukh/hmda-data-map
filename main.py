import logging
from flask import flash, redirect, url_for
from flask import render_template

from app import app

@app.errorhandler(401)
def page_not_found(e):
    flash("Requested page(%s) requires login OR you are not authorized. Redirected to main page. Thanks."%request.url)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    flash("Requested page(%s) does not exist. Redirected to main page. Thanks."%request.url)
    return redirect(url_for('index'))

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("map.html")
