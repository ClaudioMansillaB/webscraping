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

    for lesson in lesson_list:
        titles.append(lesson.h2.get_text(strip = True))
        authors.append(lesson.h3.get_text(strip = True))
        summary.append(lesson.p.get_text(strip = True))
        link = lesson.a.get("href")
        links.append(f"http://programminghistorian.org{link}")
        dates.append(lesson.find("span", class_ = "date").get_text())
        topics.append(lesson.find("span", class_ = "topics").get_text().split())
        activites.append(lesson.find("span", class_ = "activity").get_text())
        difficulties.append(lesson.find("span", class_ = "difficulty").get_text())

    lessons = {"title": titles, "authors": authors, "summary": summary, "links": links, "dates": dates, "topics": topics, "activites": activites, "difficulties": difficulties}

    df_lessons = pd.DataFrame(lessons)

    df_lessons["difficulties"] = df_lessons["difficulties"].astype(int)



    df_lessons.to_csv("lessons-ph_es.csv", index = False)



if __name__ == "__main__":
    link = "http://programminghistorian.org/es/lecciones/"
    main(
        link = link
        )