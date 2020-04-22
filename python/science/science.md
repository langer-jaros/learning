# Science

Wierd name for great modules to work with data, namely:
NumPy, matplotlib, seaborn, jupyter and scikit

Jaroslav Langer, 2020/03/14

The knowlegde is taken partly from our seminars at FIT (CTU, Prague), partly form internet.

The code is heavily inspired by our seminars.

The only goal is to overcome my (or others) potential troubles in future with trying to invent the wheel.

[Statistics is fun](http://guessthecorrelation.com/)

## MENU
+ [NumPy](#numpy)
+ [matplotlib](#matplotlib)
+ [jupyter notebook](#jupyter-notebook)
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
# Or
fig.set_size_inches(11.7, 8.27)

# Examples of six ploted graphs
# Next graph will be plotted to pos 1 in grid 3 rows 2 columns
plt.subplot(121)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green')
plt.subplot(122)
not_survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Black')

# Or
fig, (ax1, ax2) = plt.subplots(1, 2)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green', ax=ax1)
not_survived['Sex'].plot.hist(color='Black', ax=ax2)
```

### Move legend from graph
```
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```
[link](https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot)


### Labels

```py
plt.xticks(rotation=‌​45)
```

### TODO

plt.show()
fig.show()

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

### lineplot

```py
g = sns.relplot(x="time", y="value", kind="line", data=df)

g2 = sns.lineplot(    sort=False)
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

sns.scatterplot()
```

### Plot pairwise relationships in dataset
```py
sns.pairplot(data, hue='Survived', palette=['red', 'green']) #, diag_kind='hist'
```

### distplot
```py
```
https://seaborn.pydata.org/tutorial/distributions.html

### Color palettes

```py
# Create the palette
pall = sns.color_palette("hls", 8)
# See the palette
sns.palplot(pall)
```

### Set style

```py
sns.set_style("dark")
```

[Seaborn aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)

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