from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_jobs(skills):
    skills = skills.lower()
    jobs = []

    if "python" in skills:
        jobs.append("Data Analyst")
        jobs.append("Backend Developer")

    if "html" in skills or "css" in skills:
        jobs.append("Web Developer")

    if "java" in skills:
        jobs.append("Software Developer")

    if "sql" in skills:
        jobs.append("Database Administrator")

    if "c++" in skills:
        jobs.append("System Programmer")

    if "javascript" in skills:
        jobs.append("Frontend Developer")

    if not jobs:
        jobs.append("No matching jobs found. Try skills like Python, HTML, Java.")

    return jobs


@app.route("/", methods=["GET", "POST"])
def home():
    jobs = []
    if request.method == "POST":
        skills = request.form["skills"]
        jobs = recommend_jobs(skills)

    return render_template("index.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)