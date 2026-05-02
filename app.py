from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["studentDB"]
students_collection = db["students"]

@app.route("/api/students", methods=["GET"])
def get_students():
    students = list(students_collection.find({}, {"_id": 0}))
    return jsonify(students)

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json
    students_collection.insert_one({
        "name": data["name"],
        "course": data["course"],
        "year": data["year"]
    })
    return jsonify({"message": "Student registered successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
