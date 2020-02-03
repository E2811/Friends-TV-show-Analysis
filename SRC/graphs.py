import pandas as pd
import matplotlib.pyplot as plt
import web_scraping as w
import functions as f
import cleaningdataset as C

# Dataframe of the mean of words per line of each character
def plots():
    df = C.clean_dataset()
    #mean words of each character per line
    word_line_df = f.mean_word_line(df)
    mean_words = plt.pie(word_line_df['nwords'], labels=word_line_df['character'],explode=(0, 0, 0, 0.15, 0, 0)) 
    f.save_graph('mean_words')
    plt.show()
    # Create dataframe with number of lines per episode in each season of each main character 
    lines_episode = {}
    for i in range(1,11):
        lines_episode["season"+str(i)] = f.nlines_episode(df,i) 
    lines_episode_df = pd.DataFrame(lines_episode)
    df3 = lines_episode_df.reset_index()

    # Total lines per character each episode / all seasons
    for i in list(lines_episode_df.columns):
        lines_episode_df[i]= lines_episode_df[i].fillna(0)
    f.total_lines(lines_episode_df,'Total',list(lines_episode_df.columns))
      
    # Plot Total lines per character
    lines_episode_df.groupby(['character']).agg({'Total':'mean'}).plot.bar()
    f.save_graph('lines_episode')
    plt.show()
    #Number of lines per season
    main_characters = ["Chandler","Monica","Phoebe","Rachel","Ross",'Joey']
    seasons =["season1","season2","season3","season4","season5","season6","season7","season8","season9","season10"]
    total_lines = f.total_lines_season(df3,main_characters,seasons)
     # Plot total lines per season includying in the same bar all characters
    df_tlines = pd.DataFrame(total_lines)
    for col in df_tlines.columns:
        df_tlines[col] = df_tlines[col].apply(lambda x: x[1])
    df_tlines.plot.bar(stacked=True)
    f.save_graph('mean_lines_season')
    plt.show()

    # Plot mean lines per character 
    df_tlines.loc[df_tlines.shape[0]+1] = df_tlines.mean(axis=0)
    mean_lines_character = df_tlines.loc[df_tlines.shape[0]]
    mean_lines_character_df =pd.DataFrame(mean_lines_character)
    mean_lines_character_df=mean_lines_character_df.reset_index().rename(columns={'index':'character',11:'mean/lines'})
    plt.pie(mean_lines_character_df['mean/lines'], labels=mean_lines_character_df['character'],explode=(0,0,0, 0.15, 0,0), autopct='%1d%%')
    plt.title('Mean of lines per character')
    f.save_graph('mean_lines')
    plt.show()
    # Plot rating per season 
    rating_df = w.rating()
    seasons_rating = {}  
    e = 0
    count = 1
    for i in range(24,rating_df.shape[0]+18,24):
        seasons_rating['season'+str(count)] = rating_df[e:i]['rating'].astype(float).mean()
        e = i
        count += 1
    plt.plot(seasons_rating.keys(),seasons_rating.values(), marker='o', linestyle='--', color='r')
    plt.ylabel('mean rating')
    plt.xlabel('seasons')
    plt.title('Rating per seasons')
    f.save_graph('Rating')
    plt.show()