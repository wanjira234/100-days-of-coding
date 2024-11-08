import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# Write your code below this line 👇
web_archive = response.text
soup = BeautifulSoup(web_archive, "html.parser")
articles_names = soup.find_all(name="div", class_="article-title-description__text")
article_text = []

for article_tag in articles_names:
    names = article_tag.find("h3").getText()
    if names:
        article_text.append(names)
article_text.reverse()

with open("greatest movies of all time.txt", "w", encoding="utf-8") as file:
    for index, name in enumerate(article_text, start=1):
        file.write(f"{name}\n")
