from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")

        results = []

        jobsboard = soup.find('table', id="jobsboard")
        jobs = jobsboard.find_all('tr', class_="job")

        for job in jobs:
            link = job.find('a', class_="preventLink").get('href')
            link = f"https://remoteok.com/{link}"

            company = job.find('h3').string.strip()
            position = job.find('h2').string.strip()

            location = job.find_all('div', class_="location")
            pay = location[-1].string.strip()
            location = [loc.string.strip() for loc in location[:-1]]

            tags = job.find('td', class_="tags").find_all('div', class_="tag")
            tags = [tag.find('h3').string.strip() for tag in tags]

            job_data = {
                'link': link,
                'company': company,
                'position': position,
                'location': location,
                'pay': pay,
                'tags': tags
            }

            results.append(job_data)

        for result in results:
            print(result)
    else:
        print("Can't get jobs.")


extract_jobs("rust")
