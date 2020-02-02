import pandas as pd
import matplotlib.pyplot as plt
import requests 
from bs4 import BeautifulSoup

url ='https://www.channel24.co.za/ShowMax/10-unforgettable-lines-from-friends-20161109'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
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
images = [images[i]['src'] for i in range(len(images))]
import os
for image in images:
    os.system("wget " + image)