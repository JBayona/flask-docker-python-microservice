import collections
from flask import Flask, json, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

INFO = {
  "languages": {
    "es": "Spanish",
    "en": "English",
    "fr": "French",
  },
  "colors":{
    "r": "red",
    "g": "green",
    "b": "blue",
  },
  "cloud": {
    "IBM": "IBM CLOUD",
    "AMAZON": "AWS",
    "MICROSOFT": "AZURE",
  }
}

# GET METHOD
@app.route("/")
def home():
  return "<h1 style='color: blue'>This is home!</h1>"

@app.route("/temp")
def template():
  return render_template("index.html")

@app.route("/qstr")
def query_string():
  if request.args:
    req = request.args
    res = {}
    for key, value in req.items():
      res[key] = value
    res = make_response(jsonify(res), 200)
    return res
  
  res = make_response(jsonify({"error": "No query string"}), 400)
  return res

@app.route("/json")
def get_json():
  res = make_response(jsonify(INFO), 200)
  return res

@app.route("/json/<collection>/<member>")
def get_data(collection, member):
  if collection in INFO:
    member = INFO[collection].get(member)
    if member:
      res = make_response(jsonify({"res": member}), 200)
      return res
    
    res = make_response(jsonify({"error": "Member not found"}), 400)
    return res
  
  res = make_response(jsonify({"error": "Collection not found"}), 400)
  return res

# POST METHOD
@app.route("/json/<collection>", methods=["POST"])
def create_collection(collection):
  req = request.get_json()
  if collection in INFO:
    res = make_response(jsonify({"error": "Collection already exist"}), 400)
    return res
  
  INFO.update({collection: req})
  res = make_response(jsonify({"message": "Collection created"}), 200)
  return res

# PUT METHOD
@app.route("/json/<collection>/<member>", methods=["PUT"])
def update_collection(collection, member):
  req = request.get_json()
  if collection in INFO:
    if member:
      INFO[collection][member] = req['new']
      res = make_response(jsonify({"message": INFO[collection]}), 200)
      return res
    
    res = make_response(jsonify({"error": "Member not found"}), 400)
    return res
  
  res = make_response(jsonify({"error": "Collection not found"}), 400)
  return res

if __name__ == "__main__":
  print("Server runnning in port %s"%(PORT))
  app.run(host=HOST, port=PORT)