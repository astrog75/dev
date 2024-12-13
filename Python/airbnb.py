import pandas as pd
import pickle
import os
import seaborn as sns

csv_file = 'listings.csv'
pickle_file = 'listings.pkl'

# Check if pickle file exists
if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
else:
    data = pd.read_csv(csv_file)
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

# Total number of AirBnB housing
total = sum(data["id"].value_counts())
print("Total number of AirBnB housings :", total)
# 95461

# Nombre total de logements à Paris en 2020 : 1,39 million (source : Statista)
# Ratio de logements AirBnB :
r = round(total/1390000*100, 1)
print("Ratio de logements AirBnB :", r, "%")

# Number of AirBnB hosts
number_hosts = len(data["host_id"].value_counts())
print("Number of AirBnB hosts :", number_hosts)

# What factors may explain the "success" of a housing ?
# Let's define "success" by the number of reviews per month
# Caveat : a lot of housing have less than 1 review per month :
# print(sum(data["reviews_per_month"] < 1))
# data["reviews_per_month"].hist(bins = 100)

data_reviews_corr = data.corr(numeric_only = True)["reviews_per_month"]
print(data_reviews_corr)

# The correlation matrix doesn't seem to show anything relevant.

# How does localisation correlates with success of a housing ?
# Standardization latitudes
# We visually check that the latitude and the longitude distributions 
# are "roughly" normal
# 
# standardization of the longitude and latitude
data["latitude"] = (data["latitude"]-data["latitude"].mean())/data["latitude"].std()
data["longitude"] = (data["longitude"]-data["longitude"].mean())/data["longitude"].std()

# Another corre. matrix doesnt seen to show any correlation between
# localisation and reviews per month

# Is there a correlation between localisation and price ?
data["price"] = data["price"].str.replace('$', '')
data["price"] = data["price"].str.replace(',', '')
data["price"] = data["price"].astype(float)

subdata = data[["price", "longitude", "latitude"]]
print(subdata.corr())








