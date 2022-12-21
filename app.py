from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    return jsonify({"users": "foo,bar,baz"})


if __name__ == "__main__":
  app.run(debug=True)