"""
2. Extract the following web URL text using BeautifulSoup
https://en.wikipedia.org/wiki/Google
3. Save it in input.txt
"""

from bs4 import BeautifulSoup
import urllib.request

# web scraping
def webScrap(url):
    f = open("input.txt", 'w+', encoding='utf-8')
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    f.write(soup.body.text.encode('utf-8', "rb").decode('utf-8'))
    print("Output witten to file input.txt")

webScrap("https://en.wikipedia.org/wiki/Google")