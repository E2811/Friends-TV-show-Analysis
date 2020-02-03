import pandas as pd
import matplotlib.pyplot as plt
import functions as f

########################### FRIENDS DATABASE ###############################
def clean_dataset():
    df = pd.read_csv("INPUT/friends.csv")
    df = df.drop(['Unnamed: 0',"quote_order"], axis=1)
    df['season']= df['season'].fillna("0")
    df['episode_number']= df['episode_number'].fillna("0")

    # Calculate number of words per quote 
    df['quote']= df['quote'].apply(lambda x: len(str(x).split(' ')))
    df = df.rename(columns={"author":"character","quote":"nwords"})

    # filter data, change type of values and remove secondary characters
    for col in ['season','episode_number']:
        df[col]= df[col].fillna("0")
        df[col]= df[col].apply(lambda x:int(x))
        df = df[(df[col].apply(f.nonNull))]

    df = df[(df['character'].apply(f.mainCharacters))]
    df.to_csv('OUTPUT/Friends.csv')

    return df 