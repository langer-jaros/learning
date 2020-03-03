# Science

Wierd name for greate modules namely:
NumPy pandas matplotlib seaborn jupyter

## MENU
+ [NumPy](#numpy)
+ [jupyter notebook](#jupyter-notebook)
+ [pandas](#pandas)
+ [seaborn](#seaborn)
+ [matplotlib](#matplotlib)
+ [scikit-learn (sklearn)](#scikit-learn-(sklearn))

## NumPy

```py
import numpy as np
```

## jupyter notebook

Ctrl+/ - for comment and uncomment

```py
display()
```

### import of matplotlib
```py
import matplotlib.pyplot as plt
import matplotlib
# bez násl. řádku někdy nefunguje vykreslování grafů v Jupyter noteboocích
%matplotlib inline 
matplotlib.style.use('ggplot')
```

[install](https://jupyter.org/install)
http://guessthecorrelation.com/


## pandas

```py
import pandas as pd
import html5lib
import requests
```

### DataFrames

#### Read data from csv
```py
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv',sep=';')
```

#### DataFrame from xml
```
for node in xroot: 
    s_name = node.attrib.get("name")
    s_mail = node.find("email").text if node is not None else None
    s_grade = node.find("grade").text if node is not None else None
    s_age = node.find("age").text if node is not None else None
    
    rows.append({"name": s_name, "email": s_mail, 
                 "grade": s_grade, "age": s_age})

out_df = pd.DataFrame(rows, columns = df_cols)
```
[source](https://medium.com/@robertopreste/from-xml-to-pandas-dataframes-9292980b1c1c)

#### first look at the data
```py
df.head()
df.tail()
df.info()
df.describe()
df.isnull().sum()
df.notnull().sum()
```

#### Accessing the data
```py
# Column
data1['Age']
# same as
data1.Age
# Columns
data2['Name', 'Age']
# Slice - last 10 rows
data1['Age'][-10:]
# filters - only True will be returned
data1['Age'][-3:][[True, False, True]]
# array of True, False
filter = data1['Age'] > 30
data1[filter]
# accessing through indices
data1.iloc[2:10]
# only first row, columns Age and Sex
data1.loc[2:10, ['Name', 'Age']]
# i stands for integer (takes bool as well [bools].values)
data1.iloc[2:10, [3,5]] # indexy (viz .loc? a .iloc?)
# iloc with bools
data1.iloc[(data1['Age'] < 30).values, [3,5]]
```
[loc iloc source](https://www.pythonprogramming.in/what-is-difference-between-iloc-and-loc-in-pandas.html)

#### Work with the data
```py
# deep copy, very important
data1_tmp = data1.copy()
# DataFrame columns
data1_tmp.columns = range(12)
# Unlike arrays, with df doesnt't work changing values of slices
data1['Age'][0:10] = 10
# Change value of slice
data1.loc[0:10, ['Age']] = 0
# Drop columns
data2_tmp = data2_tmp.drop(['FootSize',data2.columns[0]], axis=1)
# Rename columns
data2_tmp = data2_tmp.rename(columns = {'BirthYear': 'Age'})
# Changing all data of one column
data2_tmp['Age'] = 1912 - data2_tmp['Age']
# Contencat two DataFrames
data = pd.concat([data1,data2_tmp])
# Updating the range
data.index = range(data.shape[0])
```

#### Convert data type

convert column "a" of a DataFrame to number type
```
df["a"] = pd.to_numeric(df["a"])
```


## seaborn

```py
import seaborn as sns
```

### line plot
```
g = sns.relplot(x="time", y="value", kind="line", data=df)
```
[source](https://seaborn.pydata.org/generated/seaborn.relplot.html)

## matplotlib

```py
import matplotlib.pyplot as plt
```

### Plot

```py
matplotlib.style.use('ggplot')
data.plot() # výchozí chování metody plot()
# specified
data.Age.plot(kind='bar')
```

## scikit-learn (sklearn)

```py
import sklearn as skit
```
