import requests
from bs4 import BeautifulSoup

def getPage(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('div', class_="more-infos-content")
    return " ".join(str(article.p)[33:-4].strip().split(" ")[1:-6])

if __name__ == "__main__":
    print(getPage("https://www.krosmoz.com/fr/almanax"))