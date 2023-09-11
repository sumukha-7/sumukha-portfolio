from flask import Flask, jsonify, render_template

app = Flask(__name__)

PROJECTS=[
    {
        'id': 1,
        'title': "Oral cancer detection",
        'technology used': "Deep Learning",
        'team size': 3
    },
    {
        'id': 2,
        'title': "Food ordering app",
        'technology used': "flutter",
        'team size': 4
    },
    {
        'id': 3,
        'title': "Stock trend prediction",
        'technology used': "Machine learning, sentiment analysis",
        'team size': 2
    },
    {
        'id': 4,
        'title': "Japanese text OCR app",
        'technology used': "flutter",
        'team size': 1
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", projects=PROJECTS)

@app.route("/api/projects")
def list_projects():
    return jsonify(PROJECTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
