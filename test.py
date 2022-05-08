import json

with open("data.json") as f:
        data = json.load(f)
faces = data["data"][1]["faces"]
print(faces)
faces.pop("Abhinav")
data["data"][1]["faces"] = faces
with open("data.json", "w") as f:
        json.dump(data, f, indent=4)