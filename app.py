from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title":"Software engineer",
        "location":"hyderbad",
        "salary":"RS 15,00,000"
    },
     {
        "id":2,
        "title":"Data engineer",
        "location":"Remote",
        "salary":"RS 12,000$"
    },
     {
        "id":3,
        "title":"Backend engineer",
        "location":"San francisco",
        "salary":"RS 11,000$"
    }
]
@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS,company_name="Hopeso")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS) 


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)