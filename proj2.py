#proj2.py
from bs4 import BeautifulSoup
import requests
import re

# function to convert a given url into a bs4 obj
def soupify(my_url):
    # turns a given link to a soup obj
    r = requests.get(my_url, headers={'User-Agent': 'Mozilla/5.0'})
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
        print(headline.get_text().strip())

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

# function to actually get the faculty member's email
def parse_details_email(details_page):
    soup = soupify(details_page)
    return soup.find_all("a", href=re.compile("^mailto:"))[0].get_text()


# function to iterate through the people on the page get the link to their details page
def get_faculty_page(my_url):
    base_url = "https://www.si.umich.edu"

    nodes_list = list()

    soup = soupify(my_url)
    directory_section = soup.find("div", class_="view-directory")
    person_nodes = directory_section.find_all("a", href=re.compile("^/node/"))

    for rel_url in person_nodes:
        nodes_list.append(base_url + rel_url["href"])

    return nodes_list

#function to get all the pages of people
def dir_paging(my_url, url_list=None):
    base_url = "https://www.si.umich.edu"
    soup = soupify(my_url)

    if url_list == None:
        url_list = list()

    url_list.append(my_url)

    #checks to see if there is a anchor value on the pager class, if there is
    #create the full url and add it to the list
    check_children = soup.find("li", class_="pager-next").findChildren()
    if len(check_children) > 0:
        dir_paging(base_url + check_children[0]["href"], url_list)

    return url_list

def get_all_emails(starting_url):

    count = 1
    for page in dir_paging(starting_url):
        node_list = get_faculty_page(page)
        for node in node_list:
            print("{} {}".format(count, parse_details_email(node)))
            count += 1


get_all_emails("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4")
