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

if __name__ == "__main__":
  print("Server runnning in port %s"%(PORT))
  app.run(host=HOST, port=PORT)