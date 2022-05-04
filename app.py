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
    faces = ["Samarth", "Abhinav", "Pranav"]
    return render_template("faces.html", faces=faces)

@app.route("/passcode")
def passcode():
    passcode = 12345
    return render_template("passcodes.html", passcode=passcode)

if __name__ == '__main__':
    app.run(debug=True)