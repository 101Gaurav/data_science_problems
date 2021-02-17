import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
df=pd.read_csv("movies_integrated.csv")
print(df.columns.values)
#female_rating=df.Rating[df.Gender=="F"]
#print(female_rating[:20])
#male_rating=df.Rating[df.Gender=="M"]
#print(male_rating[:20])

#barWidth = 0.25
#x=df["Title"]
df_2=df[['Title','Gender','Rating']]
print(df_2.columns.values)
#w=0.3
fig, ax = plt.subplots()

#ax.bar(x, height=male_rating, width=w, color='b', align='center')
#ax.bar(x+w, height=female_rating, width=w, color='g', align='center')
df_2.plot.bar(x='Title', ax=ax)
plt.show()
#plt.xticks()
#plt.plot(df[])
