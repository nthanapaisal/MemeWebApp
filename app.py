from flask import Flask

#create class
app = Flask(__name__) 

#specify route
@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)