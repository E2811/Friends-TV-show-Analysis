#!/usr/local/bin/python3

##### web scraping to obtain the rating of each episode ########

import requests
import pandas as pd
from bs4 import BeautifulSoup

links = ['https://www.imdb.com/search/title/?series=tt0108778&sort=release_date,asc&view=simple', 'https://www.imdb.com/search/title/?series=tt0108778&view=simple&sort=release_date,asc&start=51&ref_=adv_nxt','https://www.imdb.com/search/title/?series=tt0108778&view=simple&sort=release_date,asc&start=101&ref_=adv_nxt','https://www.imdb.com/search/title/?series=tt0108778&view=simple&sort=release_date,asc&start=151&ref_=adv_nxt','https://www.imdb.com/search/title/?series=tt0108778&view=simple&sort=release_date,asc&start=201&ref_=adv_nxt']
ratingtotal = []
episodestotal = []

def rating():
    for i in links:
        res = requests.get(i)
        soup = BeautifulSoup(res.text, 'html.parser')
        rating = soup.select("strong")
        episodes = soup.select('a[href^="/title"]')
        rating = [r.text for r in rating][2:]
        episodes = [e.text for e in episodes][2::3]
        ratingtotal.append(rating)
        episodestotal.append(episodes)
    episodestotal.append(episodes)
    rate = [e.replace('\n','') for sublist in ratingtotal for e in sublist]
    data = {"episodes":[e for sublist in episodestotal for e in sublist],
        "rating":[rate.replace('  ','') for rate in rate]}

    df_rating = pd.DataFrame(data)
    return df_rating