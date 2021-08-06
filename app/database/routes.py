from flask import Flask, request
from app.database import (
    scan, insert,
    deactivate_user, select
)

app = Flask(__name__)


@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = scan()
    return out 

@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "ok": True,
        "message": "Success"
    }
    user_data = request.json
    out["new_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return out, 201

@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    deactivate_user(uid)
    return out, 200

@app.route("/users/<int:uid>", methods=["GET"])
def get_single_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = select(uid)
    return out

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your user agent is: %s </p>" % user_agent