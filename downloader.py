from bs4 import BeautifulSoup
import urllib

f = open('/Users/elee/Desktop/shingeki-no-kyojin.html', 'r')
html = f.read()
soup = BeautifulSoup(html)

image_src = soup.find('',id='img')['src']

# find next page

# what does the last page of a series look like?

manga = "shingeki-no-kyojin"
chapter = '34'
page = '37'

url = "www.mangareader.net/" + manga + "/" + chapter + "/" + page

print url

