import requests
from bs4 import BeautifulSoup, SoupStrainer
import random
import sys

iterator = 0
def scrapeWikiArticle(url):
    headerss = {
    "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headerss)
    #soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            results.append(link['href'])
    useless_list = []
    for link in list(results):
        if "https://en.wikipedia.org/wiki" in link:
            useless_list.append("l")
        else:
            results.remove(link)

    global iterator
    iterator = iterator + 1

    random_link = random.choice(results)
    print(random_link)
    substring_last = random_link[29:]
    

    if iterator == 10:
        sys.exit("After 10 jumps it ended at: " + substring_last)
    scrapeWikiArticle(random_link)

scrapeWikiArticle("https://en.wikipedia.org/wiki/Counter-Strike_2")

    # Man kan bruge soup.findall()links i form af href="https://www.w3schools.com"