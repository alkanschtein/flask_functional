from flask import Blueprint, jsonify, request, render_template

home_bp = Blueprint('/home', __name__, url_prefix='/home') #url_prefix mandatory else it wont work except / 


@home_bp.route('/')
@home_bp.route('/index')
def index():
    return render_template("Home/index.html")

