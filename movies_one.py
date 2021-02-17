# Title: Merging csv files from movie lens dataset

import pandas as pd

movie_df=pd.read_csv("movies.dat",delimiter="::")
user_df=pd.read_csv("users.dat",delimiter="::")
rating_df=pd.read_csv("ratings.dat",delimiter="::")
print(movie_df.columns.values)
print(user_df.columns.values)
print(rating_df.columns.values)

movies_integrated=pd.merge(pd.merge(movie_df,rating_df,on="MovieID"),user_df,on="UserID")
movies_integrated.to_csv("movies_integrated.csv")
print(movies_integrated)



#print(movie_df.head)


#print(user_df.head)
#print(rating_df.head)
