from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app) # Libera o acesso do JavaScript
clicks = 0
@app.route("/clicks", method=['GET'])
def get_clicks():
    return jsonify({"clicks": clicks})
def increment_clicks():
    global clicks
    clicks += 1
    return jsonify({"clicks": clicks})
def home():
    return render_template("site002.html")
if __name__ == "__main__":
    app.run(debug=True)