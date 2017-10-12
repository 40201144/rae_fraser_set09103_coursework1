from flask import Flask, url_for, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello friends"

@app.route('/heroes')
def heroes():
    return "Heroes goes here"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
