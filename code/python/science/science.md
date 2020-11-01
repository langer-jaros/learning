# Science

Wierd name for great modules to work with data, namely:
Matplotlib, seaborn, jupyter and scikit

`2020/10/26, Jaroslav Langer`

The knowlegde is taken partly from our seminars at FIT (CTU, Prague), partly form internet.

The code is heavily inspired by our seminars.

The only goal is to overcome my (or others) potential troubles in future with trying to invent the wheel.

[Statistics is fun](http://guessthecorrelation.com/)

## Content <!-- omit in toc -->

- [matplotlib](#matplotlib)
  - [Basics](#basics)
  - [Configure the plot details, plot more graphs](#configure-the-plot-details-plot-more-graphs)
  - [Move legend from graph](#move-legend-from-graph)
  - [Labels](#labels)
  - [TODO](#todo)
- [jupyter notebook](#jupyter-notebook)
  - [How to use it as a user](#how-to-use-it-as-a-user)
  - [Basics](#basics-1)
  - [how the install the thing](#how-the-install-the-thing)
- [scikit-learn (sklearn)](#scikit-learn-sklearn)

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

---

## scikit-learn (sklearn)

```py
import sklearn as skit
```
