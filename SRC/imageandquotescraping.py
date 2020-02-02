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
    quotes_characters

    images = soup.select("div[class='embed image'] img[src]")
    images.pop(2)
    images.pop(-1)
    images.pop(3)
    images.pop(-2)
    images = [images[i]['src'] for i in range(len(images))]
    character  =["Joey","Monica","Ross","Rachel","Phoebe","Chandler"]
    i = 0
    for image in images:
        f.save_image(f'OUTPUT/{character[i]}.jpg',image)
        i += 1