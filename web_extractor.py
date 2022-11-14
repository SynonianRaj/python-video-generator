import requests as req
import re
from bs4 import BeautifulSoup

url = "https://www.uschamber.com/co/start/strategy/steve-jobs-quotes-for-business-owners"
# pat = r'<strong*?>\s*[0-9]\.(.*)\s*<\/strong>'
# pat = r'<strong*?>\s*(.*)\s*<\/strong>'
# pat = r'<li>\s*(.*)\s*<\/li>'

pat = r'<h2>\s*(.*)\s*<\/h2>'


def quotesList(url=url, pattern=pat):
    web = req.get(url)
    soup = BeautifulSoup(web.content, 'html.parser')
    a = soup.prettify()
    # print(a)
    quotes = re.findall(pattern, a, re.IGNORECASE)
    print(quotes[0:14])
    return quotes[0:14]


quotesList(url, pat)
