from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed_scraper import extract_indeed_jobs
from extractors.wwr_scraper import extract_wwr_jobs
from file import save_to_file

app = Flask(__name__) 

db = {} # Results from previous search.


@app.route("/") # decorator. Write the function directly below.
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/") 
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return (f"{keyword}.csv file has been downloaded.")

app.run("0.0.0.0")


