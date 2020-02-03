#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os 

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
def nlines_episode(df,season):
    serie2 = []
    for i in range(1,25):
        serie = df[(df['episode_number']==i)&(df['season']==season)].groupby(['episode_number','character'])['character'].count()
        serie2.append(serie)
    return pd.concat(serie2)

''' Calculate the mean of words per line of each character '''
def mean_word_line(df):
    return df.groupby(['character']).agg({'nwords':'mean'}).reset_index()

''' Calculate mean total lines for season '''
def total_lines(df,new_col, list_col_sum):
    df[new_col] = df[list_col_sum].astype(int).mean(axis=1)
    return(df)

''' Calculate number of lines per season '''
def total_lines_season(df, main_characters, seasons):
    main_characters = ["Chandler","Monica","Phoebe","Rachel","Ross",'Joey']
    dic = {}
    for i in main_characters:
        tup = []
        df2 = df[(df['character']==i)].reset_index()
        df2[seasons].plot()
        plt.title('Number of lines per season '+str(i))
        plt.xlabel('episodes')
        plt.ylabel('n lines')
        save_graph('n lines_episode' +str(i))
        plt.show()
        df2.loc[df2.shape[0]+1] = df2.sum(axis=0)
        for s in ["season1","season2","season3","season4","season5","season6","season7","season8","season9","season10"]:
            value = df2[s][df2.shape[0]]
            tup.append((s,value))
        dic[i] = tup
    return dic

''' Save Image of each character by scraping '''
def save_image(file_name, item_link):
        response = requests.get(item_link)
        with open(os.path.join(file_name), 'wb') as image_file:
            image_file.write(response.content)
            image_file.close()

''' Save Graphs '''
def save_graph(name):
    plt.savefig('OUTPUT/'+str(name)+'.png')


''' Create PDF '''
def createPdf(pdf):
    pdf.add_page()
    pdf.set_font('Arial','B',16)
    pdf.image('OUTPUT/logo.svg.png', x = 50 , y = 30 , w = 100, )

''' Add images to PDF ''' 
def addImagesPdf(pdf,image_path,quote,name):
    #Insert images
    pdf.image(image_path, x=50, y=50, w=100)
    pdf.cell(180, 200, txt=quote, align ="C")
    pdf.image('OUTPUT/n lines_episode'+name+'.png', x = 30 , y = 120 , w = 150, )

''' Save pdf '''
def save(pdf):
    #Save pdf
    pdf.output("OUTPUT/FriendsTV.pdf")