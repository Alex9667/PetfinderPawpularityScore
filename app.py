import re
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from flask import Flask

from sklearn.linear_model import LinearRegression

app = Flask(__name__)

data_path = r'Data\train.csv'
temp_data = pd.read_csv(data_path, index_col=['Id'])

data = pd.DataFrame(temp_data)

X = data.drop(columns=['Pawpularity']).values
y = data['Pawpularity'].values

reg = LinearRegression()
reg.fit(X,y)

print(reg.score(X,y))

print(reg.predict([[0,0,0,0,0,0,0,0,0,0,0,0]]))


@app.route("/")
def home():
    return 'Godav!'
