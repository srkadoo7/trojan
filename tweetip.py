from BeautifulSoup import BeautifulSoup as soupy
import urllib
import re


def gettip():
    try:
        html = urllib.urlopen('https://twitter.com/AkshayBiradar19').read()
        soup = soupy(html)
        x = soup.find("meta", {"name":"description"})['content']
        filter = re.findall(r'"(.*?)"',x)
        tweet =  filter[0]                   
        return tweet
    except:
        return 
print gettip()

