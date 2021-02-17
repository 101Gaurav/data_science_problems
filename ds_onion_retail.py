import pandas as pd

data=pd.read_csv("daily_retail_price_Onion-upto_apr_2015.csv")
#print(data.shape)
print(data.columns.values)
#print(data.head)
maxPrice=max(data.Price)
minPrice=min(data.Price)
print(data[data.Price==maxPrice].Centre_Name.unique())
#print(data[data.Price<=maxPrice].Centre_Name.value_counts())

################################################################################
#method="pearson"
#print(data.corr(date[:,]))
#c1=data.sort_values(by ='Centre_Name').Centre_Name.unique().tolist()

'''
for i in c1:
    print(i)
    print(data[data.Centre_Name==i].Price.tolist())
    print(len(data[data.Centre_Name==i & df.date==data.date].Price.tolist()))

    if data[data.date == df.date]:
        df[i] = data[data.Centre_Name == i].Price
    #df.set_index(data.sort_values(by ='Date').Date.unique())
#print(df)
'''

new_data=data.pivot(index='Date',columns='Centre_Name',values='Price')
print(new_data)
print(new_data.corr(method='pearson'))

