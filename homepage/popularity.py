import pandas as pd
import numpy as np 

Smartphones=pd.read_csv('input/updated_smartphone.csv')
Ratings=pd.read_csv('input/updated_rating.csv')

def popularity_recommendation():
    new_df=Ratings.merge(Smartphones,on='smartphone_id')
    new_df= new_df[['smartphone_id','name','user_id','ratings']]
    a=new_df.groupby(['smartphone_id'])['user_id'].count().reset_index()
    b=a.sort_values(by='user_id', ascending=False)
    b=b.head(6)
    popularity_list=b['smartphone_id'].values.tolist()
    return popularity_list



    