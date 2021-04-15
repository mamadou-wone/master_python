from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

# print(soup)
movies_list = soup.find_all(name="div", class_="jsx-2692754980")
# print(len(movies_list))
test = None

top_movie = [movie.find(name="img").get("alt") for movie in movies_list if movie.find(name="img") != None]


def reverse_list(input):
    input.reverse()
    return input

reversed_list = reverse_list(top_movie)



for i in range(len(reversed_list)):
    with open("myfovorite_movie.txt", "a") as file:
        file.write(f"{i+1}) {reversed_list[i]} \n")




# response = requests.get("https://syllart-shop.com/43-apple")
# content = response.text

# soup = BeautifulSoup(content, "html.parser")

# img_link = soup.find_all(name="img")
# for link in img_link:
#     print(link.get('src'))

# print(img_link)


#
# response = requests.get("https://news.ycombinator.com/")
#
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# articles = soup.find_all(name="a", class_="storylink")
# article_text = []
# article_link = []
# article_upvote = []
# for article_tag in articles:
#     article_text.append(article_tag.getText())
#     article_link.append(article_tag.get("href"))
#
# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
#
# print(article_text)
# print(article_link)
# print(article_upvote)
#
#
# min_value = min(article_upvote)
# print(article_text[min_value]+"\n"+article_link[min_value])


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tag = soup.find_all(name="a")
#
# for text in all_anchor_tag:
#     # print(text.getText())
#     print(text.get("href"))
