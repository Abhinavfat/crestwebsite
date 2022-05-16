from flask import Flask, render_template, url_for, request, redirect
import json
import os

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def login():
    with open("data.json") as f:
        data = json.load(f)
        
    passcode = data["data"][0].get("passcode")

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

app.config["IMAGE_UPLOADS"] = 'C:/Users\samar\OneDrive\Documents\CodingProjects\crestwebsite\static\photos'

@app.route("/faces", methods=["GET", "POST"])
def faces():
    with open("data.json") as f:
        data = json.load(f)

    faces = data["data"][1]["faces"]

    if request.method == "POST":
        for face, images in list(faces.items()):
            if request.form.get(face) == f"Delete {face}":
                faces.pop(face)
                data["data"][1]["faces"] = faces
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

        image = request.files["image"]
        direct = request.form["new_name"]

        os.mkdir(os.path.join(app.config["IMAGE_UPLOADS"], request.form["new_name"]))

        file = direct + "\\" + image.filename
        print(file)
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], file))

    return render_template("faces.html", faces=faces)

@app.route("/new_face", methods=["GET","POST"])
def new_face():
    
    return render_template("new_face.html")

@app.route("/passcode")
def passcode():
    return render_template("passcodes.html")

@app.route("/change_code", methods=["GET", "POST"])
def change_code():
    with open("data.json") as f:
        data = json.load(f)
        
    passcode = data["data"][0].get("passcode")

    message = ""

    if request.method == "POST":
        new_code = request.form["new_code"]
        try:
            new_code = int(new_code)
            data["data"][0]["passcode"] = str(new_code)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            message = "Your passcode was successfully updated!"
        except:
            message = "Passcodes can only contain numbers!"

        return render_template("change_code_result.html", message=message)
    else:
        return render_template("change_code_result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)