import pandas as pd
import numpy as np 
# numpy..numerical python deals with multidimensional array...matrices
import math
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


Smartphones=pd.read_csv('input/updated_smartphone.csv')
Ratings=pd.read_csv('input/updated_rating.csv')

Mean= Ratings.groupby(['user_id'], as_index = False, sort = False).mean().rename(columns = {'ratings': 'rating_mean'})[['user_id','rating_mean']]


Ratings= pd.merge(Ratings, Mean, on ='user_id')
Ratings['rating_adjusted']=Ratings['ratings']-Ratings['rating_mean']

train_data, test_data = train_test_split(Ratings, test_size=0.20)

train_matrix=pd.pivot_table(train_data,index='user_id',columns='smartphone_id',values='ratings') 

#pivot table
final=pd.pivot_table(train_data,index='user_id',columns='smartphone_id',values='rating_adjusted') #value with actual ratings

# Replacing NaN by user Average
final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)


#cosine similarity
def cosine(user):
    b = cosine_similarity(user)
    np.fill_diagonal(b, 0)
    similarity_with_u = pd.DataFrame(b,index=user.index)
    similarity_with_u.columns=user.index
    return (similarity_with_u)

similarity_with_user = cosine(final_user)

#k nearest neighbours

def find_n_neighbours(df,n):
    #order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
           .iloc[:n].index, 
          index=['top{}'.format(i) for i in range(1, n+1)]), axis=1) #axis 0 for index 1 for columns
    return df

#top 3 neighbours for each user
sim_user_3_u = find_n_neighbours(similarity_with_user,3)


#list of items rated by every users
train_data = train_data.astype({"smartphone_id": str})
gadget_user = train_data.groupby(by = 'user_id')['smartphone_id'].apply(lambda x:','.join(x))


#USER ITEM SCORE USING SCORE FUNCTION

def User_item_score2(user):
    gadget_seen_by_user=train_matrix.columns[train_matrix[train_matrix.index==user].notna().any()].tolist()
    a=sim_user_3_u[sim_user_3_u.index==user].values #similar users to a particular user
    b=a.squeeze().tolist()
    c=gadget_user[gadget_user.index.isin(b)]
    l=','.join(c.values)
    gadget_seen_by_similar_users=l.split(',')
    gadget_under_considiration=list(set(gadget_seen_by_similar_users)-set(list(map(str,gadget_seen_by_user))))
    gadget_under_considiration=list(map(int, gadget_under_considiration))
    score=[]
    for item in gadget_under_considiration:
        d=final_user.loc[:,item] #sabai uer le tyo item lai deko ratings
        e=d[d.index.isin(b)] #similar users le deko ratings extract gariyo
        f=e[e.notnull()]
        avg_user=train_data.loc[train_data['user_id']==user,'rating_mean'].values[0]
        index = f.index.values.squeeze().tolist() #neighbour users
        corr=similarity_with_user.loc[user,index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score','correlation']
        fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
        nume = fin['score'].sum()
        deno = fin['correlation'].sum()
        final_score = avg_user + (nume/deno)
        score.append(final_score)
    data = pd.DataFrame({'smartphone_id':gadget_under_considiration,'score':score})
    top_recommendation=data.sort_values(by='score',ascending=False).head(4)
    gadget_name=top_recommendation.merge(Smartphones, how='inner', on='smartphone_id')
    gadget_id=gadget_name.smartphone_id.values.tolist()
    return(gadget_id)


    
    
