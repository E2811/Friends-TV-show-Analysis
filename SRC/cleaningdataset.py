import pandas as pd
import matplotlib.pyplot as plt
import SRC.function as f

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
    df.to_csv('Output/Friends.csv')

    # Create dataframe with number of lines per episode in each season of each main character 
    lines_episode = {}
    for i in range(1,11):
        lines_episode[f'season{i}'] = f.nlines_episode(df,i)
    lines_episode_df = pd.DataFrame(lines_episode)

    # Total lines per character each episode / all seasons
    df[col]= df[col].fillna("0")
    f.total_lines(lines_episode_df,'Total',list(lines_episode_df.columns))

    # Total lines per character
    lines_episode_df.groupby(['character']).agg({'Total':'sum'}).plot.bar()
    
