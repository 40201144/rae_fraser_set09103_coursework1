from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return "Hello friends"

@app.route('/types/')
def types():
    return render_template("typehtml.html")

@app.route('/types/tank/')
def tanktest():
    return render_template("tanks.html")

@app.route('/types/support/')
def suptest():
    return ('Support here')

@app.route('/types/offensive/')
def offtest():
    return ('Offensive here')

@app.route('/types/defensive/')
def deftest():
    return ('Defensive here')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)