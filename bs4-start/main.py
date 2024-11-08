from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    #  finding a nested a tag that doesn't have a clas you first access the class
    #  then get the inside class using the find()
    text_tag = article_tag.find("a")
    if text_tag:
        # Append the text of the <a> tag
        article_texts.append(text_tag.text)
        # Append the href attribute of the <a> tag
        article_links.append(text_tag.get("href"))
# upvote
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_texts)
# print(article_links)
# print(article_upvotes)

# links = soup.find_all("a", href=True)
# for link in links:
#     print(link["href"])


# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
#
# anchor_tags = soup.find_all(name="a")
# # print(anchor_tags)
# # for tag in anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
# heading = soup.find(name="h1", id="name")
# # print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.get("class"))
# company_url = soup.select_one(selector="p a")
# print(company_url)
