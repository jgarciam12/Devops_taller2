import funtions as f
from flask import Flask, jsonify

application = Flask(__name__)
data = f.load_file('./heroes.csv')

@application.route("/")
def index():
    return jsonify(data)

@application.route("/<string:id>")
def heroe(id):
    hero = data.get(id)
    if hero is None:
        return jsonify({"error": "No hero found"}), 404
    return jsonify(data[id])

if __name__ == "__main__":
    application.run(port = 5000, debug = True)