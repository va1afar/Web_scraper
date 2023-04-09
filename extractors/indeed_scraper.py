from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# this counts number of pages
def get_page_count(keyword):
	base_url = "https://kr.indeed.com/jobs?q="
	browser.get(f"{base_url}{keyword}")
	soup = BeautifulSoup(browser.page_source, "html.parser")
	pagination = soup.find("nav", class_="ecydgvn0")
	pages = pagination.find_all("div", class_="ecydgvn1")
	if not pages: 
		return 1
	if len(pages) >= 5:
		return 5
	else:
		return len(pages)
	
# this scraps information from "indeed.com(kr)"
def extract_indeed_jobs(keyword):
	pages = get_page_count(keyword)
	results = []
	for page in range(pages):
		base_url = "https://kr.indeed.com/jobs"
		final_url =f"{base_url}?q={keyword}&start={page*10}"
		print("Requesting", final_url)
		browser.get(final_url)
		soup = BeautifulSoup(browser.page_source,"html.parser")
		job_list = soup.find("ul", class_="jobsearch-ResultsList")
		jobs = job_list.find_all("li", recursive=False) # Search only first li's
		for job in jobs:
			zone = job.find("div", class_="mosaic-zone") 
			if zone == None:
				anchor = job.select_one("h2 a") # choose h2 and go inside bring a 
				title = anchor["aria-label"]
				link = anchor["href"]
				company = job.find("span", class_="companyName")
				location = job.find("div", class_="companyLocation")
				job_data = {
					"link" : f"https://kr.indeed.com{link}",
					"company" : company.string,
					"location" : location.string,
					"position" : title
				}
				results.append(job_data)
	return results