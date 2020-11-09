import flask
from flask import jsonify
from flask import request
import hashlib

app = flask.Flask(__name__)

@app.route("/admin/execute/<route_param>", methods=["POST"])
@admin_login_required
def execute(route_param):
  return exec(route_param)
    
@app.route("/account/create", methods=["PUT"])
def create_account():
  data = request.get_json().strip()
  hashed_pass = hashlib.md5(data.get("password"))
  db_add_user_info(data.get("username"), hashed_pass)
  return jsonify(status="success"), 201
