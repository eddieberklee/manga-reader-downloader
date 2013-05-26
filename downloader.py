from bs4 import BeautifulSoup
import urllib
import os

def parseUrl(url):
    parts = url.split('/')
    return [parts[3], parts[4], parts[5]]

if __name__=='__main__':

    # query = 'shingeki'

    # manga = findSimilar(query, database)[0]

    manga = "shingeki-no-kyojin"
    chapter = '1'
    page = '1'

    url = "http://www.mangareader.net/" + manga + "/" + chapter + "/" + page

    f = urllib.urlopen(url)
    html = f.read()
    soup = BeautifulSoup(html)

    print soup

    image_src = soup.find('',id='img')['src']

    directory = manga
    if not os.path.exists(directory):
            os.makedirs(directory)
    image = open('', 'wb')
    urllib.urlopen(image_src)

    # find next page

    # what does the last page of a series look like?

    manga, chapter, page = parseUrl(url)

    print manga, chapter, page




