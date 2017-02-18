#proj2.py
from bs4 import BeautifulSoup
import requests

def soupify(my_url):
    # turns a given link to a soup obj
    r = requests.get(my_url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
def get_nyt_10(my_url):
    soup = soupify(my_url)
    headline_list = soup.find_all("h2", class_="story-heading")
    for headline in headline_list[:10]:
        print(headline.find("a").get_text().strip())

get_nyt_10("http://www.nytimes.com")

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
def get_most_read(my_url):
    soup = soupify(my_url)
    most_read_block = soup.find(class_="pane-mostread")
    article_list = most_read_block.find_all("li")
    for article in article_list:
        print(article.get_text())

get_most_read("http://michigandaily.com")

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
def find_alt_tags(my_url):
    soup = soupify(my_url)
    img_list = soup("img")
    for tag in img_list:
        if tag.has_attr("alt"):
            print(tag["alt"])
        else:
            print("No alternative text provided!")

find_alt_tags("http://newmantaylor.com/gallery.html")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
def get_faculty_mail(my_url):
    soup = soupify(my_url)
    base_url = "https://www.si.umich.edu"
    full_url_list = list()
    # if soup.find_all
    pager_link = soup.find(attrs={"title":"Go to next page"})
    full_url_list.append(base_url + pager_link["href"])
    print(full_url_list)

# get_faculty_mail("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4")
