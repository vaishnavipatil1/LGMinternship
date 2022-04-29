import pandas as pd
data=pd.read_csv(r'C:\Users\hp\Downloads\archive (1)\IRIS.csv')
data
data.head(5)
data.tail(5)
data.describe()
data.shape
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing  import LabelEncoder
from sklearn.metrics import accuracy_score
x = data.drop("species",axis=1)
x.head()
y =data.species
y.head()
code= LabelEncoder()
y = code.fit_transform(y)
y
data.info()
data.species.unique()
from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val=train_test_split(x,y,test_size=0.2,random_state=42)
x_train.info()
x_val.info()
model = LogisticRegression()
model.fit(x_train,y_train)
pred = model.predict(x_val)
acc = accuracy_score(y_val,pred)
print(acc)
import matplotlib.pyplot as plt
import seaborn as sns
print(model.score(x_train,y_train))
print(model.score(x_val,y_val))
c= x.corr()
print(c)
sns.heatmap(c,annot=True)
sns.pairplot(data)
