from requests import get
from bs4 import BeautifulSoup

# this scraps information from "weworkremotely"
def extract_wwr_jobs(keyword):
	base_url = "https://weworkremotely.com/remote-jobs/search?term="
	response = get(f"{base_url}{keyword}")
	if response.status_code != 200:
		print("Can't request website")
	else:
		results = []
		soup = BeautifulSoup(response.text, "html.parser")
		jobs = soup.find_all("section", class_="jobs") # save as list
		for job_section in jobs:
			job_posts = job_section.find_all("li") # save as list
			job_posts.pop(-1) # removing <li class="view-all"> 'cuz don't need it
			for post in job_posts:
				anchors = post.find_all("a")
				anchor = anchors[1]
				company, kind, region = anchor.find_all("span", class_="company") # not gonna use kind 
				link = f"{'https://weworkremotely.com'}{anchor['href']}"
				title = anchor.find("span", class_="title")
				job_data = {
					"company" : company.string,
					"link" : link,
					"location" : region.string,
					"position" : title.string
				}
				results.append(job_data)
		return results
	