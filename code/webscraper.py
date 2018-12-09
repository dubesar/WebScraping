import urllib.request
from bs4 import BeautifulSoup
print('Enter the Name of the Website')
wiki = input()
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page)
print(soup.prettify())
