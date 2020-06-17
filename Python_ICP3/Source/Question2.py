""" Program that parse a Wiki page mentioned :https://en.wikipedia.org/wiki/Deep_learning
Then do the following
Print out the title of the page
Find all the links in the page (‘a’ tag)
Iterate over each tag(above) then return the link using attribute "href" using get
Save all the links in the file """

# import libraries
import requests
from bs4 import BeautifulSoup

# declare list to append all href links in the wikipage
allLinks = []
# store the wiki page link in a variable
wikiPageUrl = "https://en.wikipedia.org/wiki/Deep_learning"

# Request to the web page
source = requests.get(wikiPageUrl)

# Extract content from the web page
text = source.text

# Using BeautifulSoup to parse the html
soup = BeautifulSoup(text, "html.parser")
# Display the title of the page
print("Title of the page:", soup.title.string)

# find all anchor tag elements and store them
b = (soup.find_all('a'))

# Using for loop to add all the links to the list and print them
for link in b:
    allLinks.append(link.get('href'))
print("Link in the page:", allLinks)

# Writing the links to a file
file = open("Q2Output.txt", "w")
for link in allLinks:
    file.write("%s \n" % link)
print("Output written to file Q2Output.txt")


