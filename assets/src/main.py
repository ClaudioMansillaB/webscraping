import requests 
from bs4 import BeautifulSoup
import pandas as pd

def main(link: str):
    """
    This file is dedicated to web scraping the data from the website.
    """
    
    reply = requests.get(link)
    content = reply.text
    soup = BeautifulSoup(content, "html.parser")

    lesson_list = soup.find_all("div", class_ = "lesson-description")

    titles = []
    authors = []
    summary = []
    links = []
    dates = []
    topics = []
    activites = []
    difficulties = []

if __name__ == "__main__":
    link = "http://programminghistorian.org/es/lecciones/"
    main(
        link = link
        )