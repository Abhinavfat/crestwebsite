from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/captures")
def captures():
    return render_template("videos.html")

@app.route("/faces")
def faces():
    return "Faces"

if __name__ == '__main__':
    app.run()