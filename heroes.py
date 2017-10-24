from flask import Flask, render_template, url_for
app = Flask(__name__)

#Unused route. Just tells user where content is
@app.route("/")
def root():
    return "Hello friends. localhost:5000/types is the site you are looking for"

#Defines route to the 'Main menu' for this project
@app.route('/types/')
def types():
    return render_template("typehtml.html")

#Defines the route for the page holding the 'tank heroes' content
@app.route('/types/tank/')
def tanktest():
    return render_template("tanks.html")

#Defines the route for the page holding the 'support heroes' content
@app.route('/types/support/')
def suptest():
    return render_template("supports.html")

#Defines the route for the page holding the 'offensive heroes' content
@app.route('/types/offensive/')
def offtest():
    return render_template("offensive.html")

#Defines the route for the page holding the 'offensive heroes' content
@app.route('/types/defensive/')
def deftest():
    return render_template("defensive.html")

#Puts the project online
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
