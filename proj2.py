#proj2.py
from bs4 import BeautifulSoup
import requests


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
def get_nyt_10(my_url):
    r = requests.get(my_url)
    soup = BeautifulSoup(r.text, "html.parser")
    headline_list = soup.find_all("h2", class_="story-heading")
    for headline in headline_list[:10]:
        print(headline.get_text())

get_nyt_10("http://www.nytimes.com")

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
def get_most_read(my_url):
    r = requests.get(my_url)
    soup = BeautifulSoup(r.text, "html.parser")
    most_read_block = soup.find(class_="pane-mostread")
    article_list = most_read_block.find_all("li")
    for article in article_list:
        print(article.get_text())

get_most_read("http://michigandaily.com")
#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
