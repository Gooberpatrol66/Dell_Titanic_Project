import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
import csv
import datetime
#Code highly influenced by https://www.pluralsight.com/guides/machine-learning-for-time-series-data-in-python

#-5 years -> +2 years.

data = pd.read_csv("CCL.csv",parse_dates=True)
data=data.drop(['Open'],axis=1)
data=data.drop(['High'],axis=1)
data=data.drop(['Low'],axis=1)
data=data.drop(['Adj Close'],axis=1)
data=data.drop(['Volume'],axis=1)
print(data)
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].dt.strftime('%d/%m/%Y')
data['year'] = pd.DatetimeIndex(data['Date']).year
data['month'] = pd.DatetimeIndex(data['Date']).month
data['day'] = pd.DatetimeIndex(data['Date']).day

data = data.drop(['Date'],axis=1)

data = pd.get_dummies(data, columns=['year'], drop_first=True, prefix='year')
data = pd.get_dummies(data, columns=['month'], drop_first=True, prefix='month')

train = data[data['Class']=='Train']
test = data[data['Class']=='Test']

train = train.drop(['Class'],axis=1)
test = test.drop(['Class'],axis=1)

trait = ['Close']

train_traits = list(set(list(train.columns))-set(trait))

xtrain = train[train_traits].values
ytrain = train[trait].values

test_traits = list(set(list(test.columns))-set(trait))

xtest = test[test_traits].values

reg = tree.DecisionTreeRegressor(max_depth=8, min_samples_leaf=.13,random_state=3)
reg.fit(xtrain,ytrain)
prediction = reg.predict(xtest)

plt.plot(prediction, color="Red")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Projecting Carnival Cruise Stock Prices")
plt.show()

#with open('prediction.csv', 'w', newline='') as csvfile:
 #   writer = csv.writer(csvfile, delimiter=',',quotechar=' ')
  #  writer.writerow(['Date','Projected Revenue'])
   # for x in range(0,6):
    #    writer.writerow([data_test_year[x+10],prediction[x][0]])