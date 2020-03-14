# Science

Wierd name for great modules to work with data, namely:
NumPy, pandas, matplotlib, seaborn, jupyter and scikit

Jaroslav Langer, 2020/03/14

The knowlegde is taken partly from our seminars at FIT (CTU, Prague), partly form internet.

The code is heavily inspired by our seminars.

The only goal is to overcome my (or others) potential troubles in future with trying to invent the wheel.

[Statistics is fun](http://guessthecorrelation.com/)

## MENU
+ [NumPy](#numpy)
+ [matplotlib](#matplotlib)
+ [jupyter notebook](#jupyter-notebook)
+ [pandas](#pandas)
+ [seaborn](#seaborn)
+ [scikit-learn (sklearn)](#scikit-learn-(sklearn))

## NumPy

Basically mathematical library.

### Basics

```py
import numpy as np
```

## matplotlib

Module for ploting of all the graphs you can imagine.

### Basics

```py
import matplotlib
import matplotlib.pyplot as plt
# without following lines, matplotlib sometimes
# doesnt work correctly in jupyter notebooks
%matplotlib inline 
matplotlib.style.use('ggplot')
```

## jupyter notebook

Nice tool, enabling to work with code surounded by text smoothly.

### How to use it as a user

Ctrl+/ - for comment and uncomment

### Basics

```py
display()
# Quick documentation about any functionality '?'
data.plot?
```

### how the install the thing

[install jupyter](https://jupyter.org/install)

## pandas

The alpha and omega of data in python. 

### Basics

```py
import pandas as pd
import html5lib
import requests
```

### DataFrame from csv

and the other way around

```py
data1 = pd.read_csv('./path/data1.csv')
# Other separator? No problem.
data2 = pd.read_csv('./path/data2.csv',sep=';')
# Write dataframe to csv
df.to_csv('./path/data1_new.csv')
```

### First look at the Dataframe

```py
# First(/Last) 5 lines defaultly
df.head()
df.tail()

# Info about columns names, types, number of not null items..
df.info()

# Basic statistic info like mean, std, min, max...
df.describe()

# Sum all the data in every column
df.sum()
# Sum the null(/notnull) items
df.isnull().sum()
df.notnull().sum()
```

### Dataframe properties

```py
# Number of dataframe rows and columns
df.shape

# Array with names of columns
df.columns

# Accessing df column with its name
df.Age

# Array(/s) from Dataframe
df.values

# Range index of data
df.index
```

### Accessing the data
```py
# Column
data1['Age']
# Columns
data2['Name', 'Age']

# Slice - last 10 rows
data1['Age'][-10:]

# Create filter -> df of True/False
filter = data1['Age'] > 30
# Aplying filter, returns rows where the filter row is True 
data1[filter] 
# Aplying array filters only True will be returned
data1['Age'][-3:][[True, False, True]]
# Same as
data1['Age'][filter.values]

# Specify rows, and cols at the same time
# LOC takes 2:5 like [2,3,4,5]
data1.loc[2:5, ['Name', 'Age']]
# Same as (the 5 is there correctly, wierd)
data1.loc[[2,3,4,5], ['Name', 'Age']]

# Accessing through indices
# ILOC takes 2:5 like [2,3,4]
data1.iloc[2:5, [3,5]]
# Same as
data1.iloc[[2,3,4], [3,5]]
# i stands for integer (takes bool as well [bools].values)
# iloc with bools (take arrays)
data1.iloc[(data1['Age'] < 30).values, [3,5]]
```
[loc iloc source](https://www.pythonprogramming.in/what-is-difference-between-iloc-and-loc-in-pandas.html)

### Work with the dataframes

```py
# deep copy, very important
data1_tmp = data1.copy()

# Contencat two DataFrames
data = pd.concat([data1,data2_tmp])
# Or Contencat two DataFrames with ignored index
dataIgnored = pd.concat([data1,data2_tmp], ignore_index=True)

# Test whether equals
data.equals(dataIgnored) # True

# Correlation matrix
cor_matrix = df.corr()

# Groupby data like sql groupby
dataUJAK[dataUJAK['Rok'] > 2000].groupby(['Název práce']).size().sort_values(ascending=False)
```

### Work with dataframe columns

```py
# Drop columns
data2_tmp = data2_tmp.drop(['FootSize',data2.columns[0]], axis=1)

# Rename columns
data2_tmp = data2_tmp.rename(columns = {'BirthYear': 'Age'})

# DataFrame rename colums with numbers from range
data1_tmp.columns = range(12)

# Convert data type
# convert column "a" of a DataFrame to number type
df["a"] = pd.to_numeric(df["a"])
```

### Works with dataframe rows

```py
# Change all data of one column
data2_tmp['Age'] = 1912 - data2_tmp['Age']
# More complicated change
data['Sex'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)

# Unlike arrays, with df doesnt't work changing values of slices
data1['Age'][0:10] = 10
# Change value of slice
data1.loc[0:10, ['Age']] = 0

# Updating the index
data.index = range(data.shape[0])
```

### Plot the data

```py
# Basic plot
data.plot()

# Specified type of the graph
data.Age.plot(kind='bar')

# figsize=(10,10) size of figure in inches
data.plot(figsize=(10,10))

# Histogram (bins = number of piles)
data.Age.plot(kind='hist', bins=50)
# Same as
data.Age.hist(bins=50)

# Scatter
survived.plot.scatter(x='Age', y='Pclass', color='Green', label='Survived')

# Plot one graph (graph2) on another (graph1)
graph1 = not_survived.Age.hist()
data2.Age.plot.hist(ax = graph1)
```

### Configure the plot details, plot more graphs

```py
# Set size of figures in inches
plt.figure(figsize=(10,18))

# Examples of six ploted graphs
# Next graph will be plotted to pos 1 in grid 3 rows 2 columns
plt.subplot(321)
survived.Age.plot.hist(color='Green', bins=20)

plt.subplot(322)
not_survived.Age.hist(color='Black', bins=20)

plt.subplot(323)
survived['Pclass'].plot.hist(color='Green')

plt.subplot(324)
not_survived['Pclass'].plot.hist(color='Black')

plt.subplot(325)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green')

plt.subplot(326)
not_survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Black')
```

### DataFrame from XML

```py
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

### Srapping the HTML

```py
# Some url, example given
url = 'https://www.volby.cz/pls/kv2010/kv1111?xjazyk=CZ&xid=0&xdz=3&xnumnuts=2103&xobec=532053&xstat=0&xvyber=0'

# Straight swth url it works better (resolved encoding automaticaly)
dfs = pd.read_html(url,flavor='html5lib')

# display(len(dfs))
display(dfs[1])

# Method with requests (not recommended for simple tasks)
import requests
r = requests.get(url)
dfs = pd.read_html(r.text,flavor='html5lib')

# for desired html inputs write data
data = {
    'nameOfInput' : 'value',
    'prace' : 'BP', # DP = diplomka, DR = disertace, RI = rigorozní
    'nazev' : '%%%', # alespoň tři písmena z názvu hledané práce
    'pocet' : '0',
    'klic' : '', # alespoň tři písmena z klíčových slov
    'kl' : 'c', # c = částečně odpovídá, n = plně odpovídá
    'nameOfButton' : 'ActionValue'
}
data_all = pd.DataFrame()
r = requests.post(url, data)

# Important trifle
r.encoding='cp1250'

# header=0 means use row 0 to make the headers
ldf = pd.read_html(r.text,flavor='html5lib', header=0)
df = ldf[0]
```

## seaborn

When plotting with matplotlib may be exhausting, the seaborn is super nice.

```py
import seaborn as sns
```

### line plot
```
g = sns.relplot(x="time", y="value", kind="line", data=df)
```
[source](https://seaborn.pydata.org/generated/seaborn.relplot.html)

### heatmap
```py
# heatmap from correlation matrix
sns.heatmap(cor_matrix, annot=True)
```

### Scatter
```py
sns.stripplot(x="Pclass", y="Age", hue="Survived", data=data, palette= ['black','green']) #, jitter=False) 
```

### Plot pairwise relationships in dataset
```py
sns.pairplot(data, hue='Survived', palette=['red', 'green']) #, diag_kind='hist'
```

## scikit-learn (sklearn)

```py
import sklearn as skit
```
