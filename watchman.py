import time
# from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
# from lxml.html.diff import htmldiff

url = "https://www.gran-turismo.com/us/gt7/news/"
site = BeautifulSoup(urlopen(url), "html.parser")
print(site.get_text())
exit()

# get url from user

# get time (x) from user

# run a while loop to check site every x minutes

    # if site has changed, tell user
    # can we use difflib.ndiff(a, b) to actually print the change?
    # update currentSite variable and keep running to look for changes in x minutes

# run another thread that waits for user input to stop program

# here is a test change to learn how to commit to git