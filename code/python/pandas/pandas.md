# pandas

*The alpha and omega of data in python.*

First things first
+ [Import pandas](#import-pandas)

Get data into DataFrames
+ [Dataframe form dictionary](#dataframe-form-dictionary)
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
+ [More dataframes](#More-dataframes)

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

[Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)
[Join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)

data['embarked'] = data[['embarked']].astype('category').apply(lambda x: x.cat.codes)

### Import pandas

```py
import pandas as pd
import html5lib
import requests
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Dataframe form dictionary

```py
lists = [[1,2,3,4], [2,3,4], [5,2,4,7,8]]
lengths = [len(sublist) for sublist in lists]

df_dict = {"lengths": lengths, "lists": lists}
df = pd.DataFrame(df_dict)
```

[df from dicts and lists](https://pbpython.com/pandas-list-dict.html)

### Get dataframe from csv

```py
data1 = pd.read_csv('./path/data1.csv')
# Other separator? No problem.
data2 = pd.read_csv('./path/data2.csv', sep=';', decimal=',')
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

### Dataframe from json

```py
pd.read_json("./time_spent.json", orient="index")
```

[types of json structure](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)

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
# 
filter = data1['Age'].isin([30,31,32])
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

# iterate rows
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### loc - Specify rows, and cols at the same time

Usage: dataFrame.loc[<ROWS RANGE> , <COLUMNS RANGE>]

```py
# LOC takes 2:5 like [2,3,4,5]
data1.loc[2:5, ['Name', 'Age']]
# Same as (the 5 is there correctly, wierd)
data1.loc[[2,3,4,5], ['Name', 'Age']]
```

### iloc - Accessing through indices

Usage: dataFrame.iloc[<ROWS INDEX RANGE> , <COLUMNS INDEX RANGE>]

```py
# ILOC takes 2:5 like [2,3,4]
data1.iloc[2:5, [3,5]]
# Same as
data1.iloc[[2,3,4], [3,5]]
# i stands for integer (takes bool as well [bools].values)
# iloc with bools (take arrays)
data1.iloc[(data1['Age'] < 30).values, [3,5]]
```
[usages from here](https://thispointer.com/select-rows-columns-by-name-or-index-in-dataframe-using-loc-iloc-python-pandas/)
[loc iloc source](https://www.pythonprogramming.in/what-is-difference-between-iloc-and-loc-in-pandas.html)

[Back to pandas](#pandas) | [Back to the top](#Science)

### More dataframes

```py
df1.equals(df2)
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Work with the dataframes

```py
# First to deep copy the data (important)
data1_tmp = data1.copy()

# Create dataframe from dictionary
df = pd.DataFrame({'A': [a], 'B': [b]})
# or
df = pd.DataFrame({'A': a, 'B': b}, index=[0])

# Contencat two DataFrames
data = pd.concat([data1,data2_tmp])
# Or Contencat two DataFrames with ignored index
dataIgnored = pd.concat([data1,data2_tmp], ignore_index=True)

# Test whether indexes equal
data.equals(dataIgnored) # True

# Correlation matrix
cor_matrix = df.corr()

# Sort rows or columns # only kind='mergesort' is stable
DataFrame.sort_values(by, axis=0, ascending=True, inplace=True, kind='quicksort')

# Sort index
df = df.sort_index(ascending=False, ignore_index=True)
```

#### Group by

```py
# Groupby data like sql groupby
dataUJAK[dataUJAK['Rok'] > 2000].groupby(['Název práce']).size().sort_values(ascending=False)
```
[groupby](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html)

[Back to pandas](#pandas) | [Back to the top](#Science)

### Work with dataframe columns

```py
# Set index from column
DF.set_index('columnName')

# Updating the index
data.index = range(data.shape[0])

# Drop columns
data2_tmp = data2_tmp.drop(['FootSize',data2.columns[0]], axis=1)

# Rename columns
df.columns = [COLNAME1, COLNAME1, COLNAME1]
# Rename specific columns
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

# Change columns type to datetime
df[df.columns[0]] = pd.to_datetime(df.columns[0], format='%d.%m.%Y')
```
[python date time formats](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
```
# Days from datetime
rfm[RECENCY] = rfm[RECENCY].astype('timedelta64[D]')
```

[Back to pandas](#pandas) | [Back to the top](#Science)

### Works with dataframe rows

```py
# Change all data of one column
data2_tmp['Age'] = 1912 - data2_tmp['Age']
# More complicated change - apply
data['Sex'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)

# Even more complicated change apply
# Default axis for DataFrame.apply is axis=0, goes through lines
# to acess columns use axis=1
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

# Remove duplicated indices
df3 = df3[~df3.index.duplicated(keep='first')]

# Replace values with
data = data.replace('?', np.nan)
```

[link to lambda with function](https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe)

[strip](https://www.geeksforgeeks.org/python-pandas-series-str-strip-lstrip-and-rstrip/)

[apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)

[index](https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html)

[remove duplicated indices](https://stackoverflow.com/questions/13035764/remove-rows-with-duplicate-indices-pandas-dataframe-and-timeseries)

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
data.Age.hist(color='green', bins=50)

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
numeral_filter = df['ticket'].str.match(r'(\A[0-9]+\Z)', case=False)==True
df['ticket'] = df['ticket'].apply(lambda x: np.nan if x == '' else x) 
display(df[numeral_filter].shape[0])
display(df[~numeral_filter])


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
