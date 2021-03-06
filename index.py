# Import libraries
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'
nepal_url = 'https://www.worldometers.info/coronavirus/country/nepal/'

print "Live Corona updates:"
print ' '


def corona_updater(given_url, name):
    global x
    response = requests.get(given_url)
    soup = BeautifulSoup(response.text, "html.parser")
    total = soup.find("div", {"class": "maincounter-number"})
    b = total.span
    c = b.text
    print name, ':', c
    print 'Time:', now
    intervals = [300, .635]
    if x == 0:
        x = x + 1
        time.sleep(intervals[x])
    else:
        x = x - 1
        time.sleep(intervals[x])


while True:
    now = datetime.now()
    x = 0
    corona_updater(url, "Total")
    corona_updater(nepal_url, "Nepal")
    print ' '

