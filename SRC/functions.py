#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

'''web scraping using beautiful soup'''
def request(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')

''' fill NaN values '''
def fillNonValues(df):
    return df[col].fillna("0")

''' Only interest in the main characters''' 
def mainCharacters(df):
    return df in ["Chandler","Monica","Phoebe","Rachel","Ross",'Joey']

''' Only rows with number of episode and season '''

def nonNull(df):
    return df>0

''' Calculate number of lines per episode of each character '''
def nlines_episode(df,season, nepisodes=25):
    serie2 = []
    for i in range(1,nepisodes):
        serie = df[(df['episode_number']==i)&(df['season']==season)].groupby(['episode_number','character'])['character'].count()
        serie2.append(serie)
    return pd.concat(serie2)

''' Calculate the mean of words per line of each character '''
def mean_word_line():
    return df.groupby(['character']).agg({'nwords':'mean'}).reset_index()

''' Calculate total lines for season '''
def total_lines(df,new_col, list_col_sum):
    df[new_col] = df[list_col_sum].astype(int).sum(axis=1)
    return(df)