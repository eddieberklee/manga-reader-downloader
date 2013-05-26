from bs4 import BeautifulSoup
import urllib,urllib2
import os

ROOT = 'http://www.mangareader.net'

def parseUrl(url):
    parts = url.split('/')
    if parts[4] and not parts[5]:
        return [parts[3], parts[4], '1']
    return [parts[3], parts[4], parts[5]]

def findAndDownloadImage(opener, url):
    manga, chapter, page = parseUrl(url)

    f = opener.open(url)
    html = f.read()
    soup = BeautifulSoup(html)

    image_src = soup.find('img',id='img')
    if image_src:
        image_src = image_src['src']
        image_type = image_src.split('.')[-1]

        directory = manga + '/' + chapter
        if not os.path.exists(directory):
                os.makedirs(directory)
        print directory + '/' + page + '.' + image_type
        image = open(directory + '/' + page + '.' + image_type, 'wb')
        image.write(opener.open(image_src).read())
        image.close()

def findNextPage(opener, url):
    html = opener.open(url).read()
    soup = BeautifulSoup(html)
    image = soup.find('img',id='img')
    if image:
        next_page = image.parent['href']
        return next_page
    else:
        return False

if __name__=='__main__':
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    # query = 'shingeki'

    # manga = findSimilar(query, database)[0]

    manga = "shingeki-no-kyojin"
    chapter = '1'
    page = '1'

    url = "http://www.mangareader.net/" + manga + "/" + chapter + "/" + page

    findAndDownloadImage(opener, url)

    # find next page
    next_page = findNextPage(opener, url)
    while next_page:
        # set next_page to False if there is no next page aka when there is no <img id='img'
        next_page = findNextPage(opener, url)
        url = ROOT + next_page
        manga, chapter, page = parseUrl(url)
        findAndDownloadImage(opener, url)
        # print manga, chapter, page, "was saved!"
        pass
    
    print "Reached the end of the manga series at chapter %s page %s" % (chapter, page)




