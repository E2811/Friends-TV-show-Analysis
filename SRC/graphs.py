import pandas as pd
import matplotlib.pyplot as plt
import SRC.web-scraping as w

# Dataframe of the mean of words per line of each character
def mean_words_character_plot()
    word_line_df = f.mean_word_line()
    plt.pie(word_line_df['nwords'], labels=word_line_df['character'],explode=(0, 0, 0, 0.15, 0, 0))
    return plt.show(), word_line_df
plt.savefig('../output/'+name+'.png')
# Plot Total lines per character
lines_episode_df.groupby(['character']).agg({'Total':'sum'}).plot.bar()

#Number of lines per season 

def total_lines_season(df):
    main_characters = ["Chandler","Monica","Phoebe","Rachel","Ross",'Joey']
    dic = {}
    for i in main_characters:
        tup = []
        df2 = df[(df['character']==i)].reset_index()
        df2[seasons].plot()
        title(f'{i}')
        xlabel('episodes')
        ylabel('nº lines')
        show()
        #savefig(f'{i}nºlines/episode.png')
        df2.loc[df2.shape[0]+1] = df2.sum(axis=0)
        for s in ["season1","season2","season3","season4","season5","season6","season7","season8","season9","season10"]:
            value = df2[s][df2.shape[0]]
            tup.append((s,value))
        dic[i] = tup
    return dic

# Plot total lines per season includying in the same bar all characters
df_tlines = pd.DataFrame(tl)
for col in df_tlinescolumns:
    df_tlines[col] = df_tlines[col].apply(lambda x: x[1])
dftl.plot.bar(stacked=True)


# Plot rating per season 
rating_df = w.rating()
seasons_rating = {}  
e = 0
count = 1
for i in range(24,rating_df.shape[0]+18,24):
    seasons_rating[f'season{count}'] = rating_df[e:i]['rating'].astype(float).mean()
    e = i
    count += 1
plt.plot(seasons_rating.keys(),seasons_rating.values(), marker='o', linestyle='--', color='r')
ylabel('mean rating')
xlabel('seasons')
title('Rating per seasons')
show(rating_plot)