from extractors.indeed_scraper import extract_indeed_jobs
from extractors.wwr_scraper import extract_wwr_jobs

# receive input, merge wwr and indeed datas.
# and export as a csv file.
keyword = input("What do you want to search for?")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")



