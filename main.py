# from extractors.indeed_scraper import extract_indeed_jobs
# from extractors.wwr_scraper import extract_wwr_jobs
# from file import save_to_file

# # receive input, merge wwr and indeed datas.
# # and export as a csv file.
# keyword = input("What do you want to search for?")
# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)


# ---------------------------------------------------
# gonna make UI for more convinient use
# with Flask. 
# ---------------------------------------------------

from flask import Flask

app = Flask("WebScrapper")

@app.route("/") # decorator
def home():
    return "hey there!"

app.run("0.0.0.0")


