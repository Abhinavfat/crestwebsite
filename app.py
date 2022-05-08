from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def login():
    with open("passcode_data.txt", "r") as f:
        passcode = f.read()

    if request.method == "POST":
        check_code = request.form["passcode"]
        if passcode == check_code:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", incorrect=True)
    else:
        return render_template("login.html", incorrect=False)

@app.route("/home")
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

@app.route("/change_code", methods=["GET", "POST"])
def change_code():
    with open("passcode_data.txt", "r") as f:
        passcode = f.read()
    message = ""

    if request.method == "POST":
        new_code = request.form["new_code"]
        try:
            new_code = int(new_code)
            with open("passcode_data.txt", "w") as f:
                f.write(str(new_code))
            message = "Your passcode was successfully updated!"
        except:
            message = "Sorry, passcodes can only consist of numbers."

        return render_template("change_code_result.html", message=message)
    else:
        return render_template("change_code_result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)