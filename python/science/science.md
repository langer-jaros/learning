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
+ [python](#python)

## NumPy

Basically mathematical library.

### Basics

```py
import numpy as np
```


```py
# Create NaN
NaN = np.nan

# Round number
np.round(theNumber, decimals=2)
```
[Round numpy](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.round_.html)

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

### Move legend from graph
```
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```
[link](https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot)

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

*The alpha and omega of data in python.*

First things first
+ [Import pandas](#import-pandas)

Get data into DataFrames
+ [Get dataframe from csv](#get-dataframe-from-csv)
+ [Write dataframe to csv](#write-dataframe-to-csv)
+ [DataFrame from XML](#dataframe-from-xml)
+ [Srapping the HTML](#srapping-the-html)

Accessing the dataframes
+ [First look at the Dataframe](#first-look-at-the-dataframe)
+ [Dataframe properties](#dataframe-properties)
+ [Accessing columns](#accessing-columns)
+ [Accessing rows](#accessing-rows)
+ [Rows and cols - loc, iloc](#rows-and-cols---loc,-iloc)

Modifing the dataframes
+ [Work with the dataframes](#work-with-the-dataframes)
+ [Work with dataframe columns](#work-with-dataframe-columns)
+ [Works with dataframe rows](#works-with-dataframe-rows)

Poltting the data
+ [Plot the data](#Plot-the-data)
+ [Configure the plot details, plot more graphs](#configure-the-plot-details,-plot-more-graphs)

Advanced features
+ [MultiIndex](#multiindex)
+ [pandas regex](#pandas-regex)

### TODO

```py
DF.set_index('columnName')
```
[Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)
[Join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)
[index](https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html)



### Import pandas

```py
import pandas as pd
import html5lib
import requests
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Get dataframe from csv

```py
data1 = pd.read_csv('./path/data1.csv')
# Other separator? No problem.
data2 = pd.read_csv('./path/data2.csv',sep=';')
# Specify rows for header of the table
data2 = pd.read_csv('./path/data2.csv',header=[0,1])
# Use different headers - names
candidates = pd.read_csv('./candidates.csv', names=columnsNamesList)
# Don't read index from csv
candidates = pd.read_csv('./candidates.csv', index=False)
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Write dataframe to csv

```py
# Write dataframe to csv
df.to_csv('./path/data1_new.csv')
# Write row names (index)
candidates.to_csv('./candidates.csv', index=False)
```
[Back to pandas](#pandas) | [Back to the top](#Science)

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

[Back to pandas](#pandas) | [Back to the top](#Science)

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

[Back to pandas](#pandas) | [Back to the top](#Science)

---

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

# List of unique values
df.name.unique()

# Number of uniqe values (default ignores NaN)
df.nunique()

# Check if NaN, not NaN
df.isnull()
df.notnull()

# Handy
df.isnull().sum()
df.notnull().sum()

# Bit statistics
df[COL].mean()
df[COL].median()
df[COL].var()
```

[Back to pandas](#pandas) | [Back to the top](#Science)

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

[Back to pandas](#pandas) | [Back to the top](#Science)

### Accessing columns

```py
# Access column or columns of an multi-column (multiindex)
data1['Age']
# Access Columns
data2['Name', 'Age']
# Resp. more correct is this, dunno why
df1 = df[['a','b']]
```

[correct columns access link](https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe)

[Back to pandas](#pandas) | [Back to the top](#Science)

### Accessing rows

```py
# Slice - last 10 rows
data1['Age'][-10:]
```
Filters
```py
# Create filter -> df of True/False
filter = data1['Age'] > 30
# Aplying filter, returns rows where the filter row is True 
data1[filter]
# Aplying array filters only True will be returned
data1['Age'][-3:][[True, False, True]]
# Same as
data1['Age'][filter.values]

# Filter negation
data1[~filter]
# Combining more filters
# Filter1 and filter2
data1[filter1 & filter2]
# Filter1 or filter2
data1[filter1 | filter2] 
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Rows and cols - loc, iloc

```py
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

[Back to pandas](#pandas) | [Back to the top](#Science)

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

```

Group by
```py
# Groupby data like sql groupby
dataUJAK[dataUJAK['Rok'] > 2000].groupby(['Název práce']).size().sort_values(ascending=False)
```
[groupby](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html)

[Back to pandas](#pandas) | [Back to the top](#Science)

### Work with dataframe columns

```py
# Drop columns
data2_tmp = data2_tmp.drop(['FootSize',data2.columns[0]], axis=1)

# Rename columns
data2_tmp = data2_tmp.rename(columns = {'BirthYear': 'Age'})

# Rename colums with numbers from range
data1_tmp.columns = range(12)

# Add column (colNumber, name(multiindex here), columnData, allowDuplicates)
df.insert(2, ("Age","Age"), [21, 23, 24, 21], True) 
# Better exemple
yearColumn = [year for x in range(candidates_tmp.shape[0])]
candidates_tmp.insert(0, ("Rok","Rok"), yearColumn, False)

# Reorder columns
general_tmp = general_tmp[[3, 4, 0, 1, 2, 5, 6, 7, 8, 9]]
# Or
df = df.reindex(columns=['mean',0,1,2,3,4])
# Sort order of columns
df = df.reindex(sorted(df.columns), axis=1)

# Convert data type
# convert column "a" of a DataFrame to number type
df["a"] = pd.to_numeric(df["a"])
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Works with dataframe rows

```py
# Change all data of one column
data2_tmp['Age'] = 1912 - data2_tmp['Age']
# More complicated change
data['Sex'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)

# Even more complicated change apply
candidates[DEGREE] = candidates[[DEGREE, DEGREE_TMP]].apply(lambda x:
    np.nan if (pd.isnull(x[0]) & pd.isnull(x[1])) else
        x[0] if pd.isnull(x[1]) else
            x[1] if pd.isnull(x[0]) else x[0]+x[1], axis=1)

# Apply lambda with function
df['col_3'] = df.apply(lambda x: f(x.col_1, x.col_2), axis=1)

# Strip all the words
candidates[nameSurname] = candidates[nameSurname].apply(lambda x: x.strip())
# Strip 
candidates[nameSurname] = candidates[nameSurname].str.strip()

# Unlike arrays, with df doesnt't work changing values of slices
data1['Age'][0:10] = 10
# Change value of slice
data1.loc[0:10, ['Age']] = 0

# Updating the index
data.index = range(data.shape[0])

# Replace values with
data = data.replace('?', np.nan)
```

[link to lambda with function](https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe)

[strip](https://www.geeksforgeeks.org/python-pandas-series-str-strip-lstrip-and-rstrip/)

[apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)

[Back to pandas](#pandas) | [Back to the top](#Science)

### Plot the data

```py
# Basic plot
data.plot()

# Specified type of the graph
data.Age.plot(kind='bar')
# Horizontal bar
graph = numberOfCandidatesByPartyDF.plot(kind='barh', stacked=True, colormap=myColors, figsize=(18, 15),width=0.9)

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

width
```py
df.plot(kind='bar', stacked=True, width=1)
```

TODO COLORMAP

[area link ](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.area.html)
[area plot](https://stackoverflow.com/questions/55214249/how-to-create-an-area-plot-in-seaborn)

[Back to pandas](#pandas) | [Back to the top](#Science)

### MultiIndex

Way how to better structure data in 2D

```py
# Create MultiIndex #
columns2 = pd.MultiIndex.from_tuples([
            (      'Kandidátní listina',                    'číslo'),
            (                  'Mandát',                   'Mandát')],
           )
# Compare two MultiIndices #
len(columns1.difference(columns2).values) > 0

# Rename MultiIndex columns
candidates_tmp = candidates_tmp.rename(columns = {'Kandidátnílistina': 'Kandidátní listina'}, level=1)

# Flatten the MultiIndex into Index of tuples
columns1.to_flat_index()
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### pandas regex

```py
# Match
Series.str.match(pattern, case=True, flags=0, na=nan)

# Extract

# Replace

```
[pandas replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)

[pandas extract](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html)

[pandas match](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.match.html)

[How to use Regex in Pandas](https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/)

[Back to pandas](#pandas) | [Back to the top](#Science)

---

## seaborn

When plotting with matplotlib may be exhausting, the seaborn is super nice.

### TODO

```py
hue=
```
[palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

```py
import seaborn as sns
```

### line plot
```
g = sns.relplot(x="time", y="value", kind="line", data=df)
```
[source](https://seaborn.pydata.org/generated/seaborn.relplot.html)

### barplot
```py
```
[link](https://seaborn.pydata.org/generated/seaborn.barplot.html)
[link2](https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars)

### heatmap
```py
# heatmap from correlation matrix
sns.heatmap(cor_matrix, annot=True)
```

### Scatter
```py
sns.stripplot(x="Pclass", y="Age", hue="Survived", data=data, palette= ['black','green']) #, jitter=False) 
sns.swarmplot(x='Rok', hue='Kandidátní listina - název', y='Věk', data=candidates)
```

### Plot pairwise relationships in dataset
```py
sns.pairplot(data, hue='Survived', palette=['red', 'green']) #, diag_kind='hist'
```

### distplot
```py
```
https://seaborn.pydata.org/tutorial/distributions.html

---

## scikit-learn (sklearn)

```py
import sklearn as skit
```

## Python

### Floats NaN
```py
NaN = float("NaN")
```