# Matplotlib

Module for ploting of all the graphs you can imagine.

`2020/11/08, Jaroslav Langer`

## Content <!-- omit in toc -->

- [Basics](#basics)
- [Set figure size](#set-figure-size)
- [Plot more graphs](#plot-more-graphs)
  - [subplot](#subplot)
  - [subplots](#subplots)
- [Move legend from graph](#move-legend-from-graph)
- [Labels](#labels)
- [Save figure as png](#save-figure-as-png)
- [TODO](#todo)

## Basics

```py
import matplotlib
import matplotlib.pyplot as plt
# without following lines, matplotlib sometimes
# doesnt work correctly in jupyter notebooks
%matplotlib inline 
matplotlib.style.use('ggplot')
```

## Set figure size

```py
# Set size of figures in inches
plt.figure(figsize=(10,18))
# Or
fig.set_size_inches(11.7, 8.27)
```

## Plot more graphs

### subplot

```py
# Examples of six ploted graphs
# Next graph will be plotted to pos 1 in grid 3 rows 2 columns
plt.subplot(121)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green')
plt.subplot(122)
not_survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Black')
```

### subplots

```py
fig, (ax1, ax2) = plt.subplots(1, 2)
# fig, axes = plt.subplots(nrows=1, ncols=2)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green', ax=ax1)
not_survived['Sex'].plot.hist(color='Black', ax=ax2)
```

## Move legend from graph

```py
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```

- [link](https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot)


## Labels

```py
# Rotate x ticks, hadny if too long
plt.xticks(rotation=‌​45)

# Only xticks present in the dataset
ax.set(xticks=df["x_column"].nunique(), xticklabels=df["x_column"].nunique())
```

## Save figure as png

```py
fig.savefig("output.png")
```

## TODO

plt.show()
fig.show()
