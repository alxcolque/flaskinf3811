from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return ("Hola mundo!")
@app.route("/saludo")
def saludo():
    return ("Hola !")

@app.route("/usuario/<string:usuario>")
def usuario():
    return "Hola: "+usuario

if __name__ == "__main__":
    app.run(debug=True, port=5001)