from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/captures")
def captures():
    return render_template("videos.html")

@app.route("/faces")
def faces():
    return render_template("faces.html")

@app.route("/passcode")
def passcode():
    return render_template("passcodes.html")

if __name__ == '__main__':
    app.run(debug=True)