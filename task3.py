[5:08 pm, 29/04/2022] Kshitee❤️: import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
from datetime import datetime
stock=pd.read_csv(r"C:\Users\hp\Downloads\Tesla.csv - Tesla.csv.csv")
stock.head(10)
stock.describe()
stock.info()
stock.columns
plt.figure(figsize=(15,6))
stock['Close'].plot()
plt.ylabel('Adj Close')
plt.xlabel(None)
plt.title(f"Closing price of stock")
plt.tight_layout()
stock['Daily Return']=stock['Close'].pct_change()
plt.figure(figsize=(12,7))
stock['Daily Return'].hist(bins=50)
plt.xlabel('Daily Return')
plt.title(f'company')
plt.tight_layout()
stock['Daily Return'].plot(legend=True,linestyle='--',marker='o')
closing_df=stock['Close']
closing_df.head()
tech_rets=closing_df.pct_change()
tech_rets.head()
tech_rets.to_frame()
plt.figure(figsize=(16,6))
plt.plot(stock['Close'])
plt.xlabel('date',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.title('Close Price History')
plt.show()
data=stock.filter(['Close'])
dataset=data.values
training_data_len=int(np.ceil(len(dataset) *.95))
training_data_len
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
scaled_data=scaler.fit_transform(dataset)
scaled_data
train_data=scaled_data[0:int(training_data_len), :]
x_train=[]
y_train=[]
for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])
    if i<=61:
        print(x_train)
        print(y_train)
        print()
x_train,y_train=np.array(x_train),np.array(y_train)
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
x_train.shape
