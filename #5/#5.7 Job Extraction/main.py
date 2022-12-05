from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't reqeust website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for job_post in job_posts:
            anchors = job_post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']

            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find("span", class_="title")

            print(title, company, kind, region)
            print("/" * 10)


# list_of_numbers = [1, 2, 3]
# first, second, third = list_of_numbers
