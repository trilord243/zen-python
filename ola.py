
#get random forest model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import mean_squared_error,r2

# load data from train.csv
train_df=pd.read_csv('train.csv')
train_df["target"]=train_df["target"].astype(int)

# split the data into training and testing

