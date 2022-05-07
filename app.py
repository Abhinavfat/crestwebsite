from flask import Flask, render_template, url_for, request

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
    return render_template("passcodes.html")

@app.route("/change_code")
def change_code():
    passcode = "12345"
    old_code = request.args.get("curr_code", "")
    new_code = request.args.get("new_code", "")
    message = ""

    if old_code == passcode:
        try:
            new_code = int(new_code)
            passcode = str(new_code)
            message = "Your passcode was successfully updated!"
        except:
            message = "Sorry, passcodes can only consist of numbers."
    else:
        message = "Sorry, incorrect passcode."

    return render_template("change_code_result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)