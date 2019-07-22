import requests
from bs4 import BeautifulSoup
import urllib.request
import re

PAGE = "http://galaxyheavyblow.web.fc2.com"


def main():
    response = requests.get(PAGE)
    soup = BeautifulSoup(response.content, "html.parser")
    link_list = soup.find_all(
        "a",
        attrs={"href": re.compile(r"/fc2-imageviewer/\?aid=\d&iid=\d")}
    )
    
    for link in link_list:
        print(link)

if __name__ == "__main__":
    main()