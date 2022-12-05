"""
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't reqeust website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all('section', class_="jobs"))
"""


def say_hello(name, age):
    print(f"Hello {name}. You are {age} years old.")


say_hello("Nicolas", 29)
say_hello(age=12, name="Nicolas")
