from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import time

playlistLink = input("Enter playlist link: ")

my_url = Request(playlistLink, headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
data = page_soup.find_all('a', {"class":"playlist-video"})
links = []
for link in data:
    links.append("https://youtube.com"+link.get('href'))
