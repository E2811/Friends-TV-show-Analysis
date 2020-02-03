from bs4 import BeautifulSoup
import functions as f

def QuoteAndImage():
    url ='https://www.channel24.co.za/ShowMax/10-unforgettable-lines-from-friends-20161109'
    soup = f.request(url)

    quotes = soup.select("strong")
    quotes = [q.text for q in quotes][0:-1]
    quotes.pop(8)
    quotes.pop(9)
    quotes.pop(7)
    quotes_characters = {}
    for q in quotes:
        n = q.split('.')[1]
        quotes_characters[n.split(':')[0]]=n.split(':')[1]

    for i in [' Joey',' Rachel',' Phoebe']:
        quotes_characters[i] = quotes_characters[i].replace('’',"'")

    images = soup.select("div[class='embed image'] img[src]")
    images.pop(2)
    images.pop(-1)
    images.pop(3)
    images.pop(-2)
    images = [images[i]['src'] for i in range(len(images))]
    character  =["Joey","Monica","Ross","Rachel","Phoebe","Chandler"]
    i = 0
    for image in images:
        f.save_image('OUTPUT/'+character[i]+'.jpg',image)
        i += 1

    url = 'https://es.wikipedia.org/wiki/Archivo:Friends_logo.svg'
    soup = f.request(url)
    logo = 'https:'+ soup.select('#file > a:nth-child(1) > img:nth-child(1)')[0]['src']
    f.save_image('OUTPUT/logo.svg.png',logo)
    return quotes_characters
