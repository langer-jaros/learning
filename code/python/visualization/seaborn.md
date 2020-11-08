# seaborn

When plotting with matplotlib may be exhausting, the seaborn is super nice.

## Contents <!-- omit in toc -->
- [Import](#import)
- [lineplot](#lineplot)
- [barplot](#barplot)
- [heatmap](#heatmap)
- [Scatter](#scatter)
  - [Plot pairwise relationships in dataset](#plot-pairwise-relationships-in-dataset)
- [Histogram](#histogram)
- [Set title](#set-title)
- [Color palettes](#color-palettes)
- [Set style](#set-style)

## Import

```py
import seaborn as sns
```

## lineplot

```py
g = sns.relplot(x="time", y="value", kind="line", data=df)

g2 = sns.lineplot(    sort=False)
```

- [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html)

## barplot

```py
```

- [barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html)
- [multiple bars](https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars)

## heatmap

```py
# heatmap from correlation matrix
sns.heatmap(cor_matrix, annot=True)
```

## Scatter

```py
# Hue - group by Survived
sns.stripplot(x="Pclass", y="Age", hue="Survived", data=data, palette= ['black','green']) #, jitter=False) 
sns.swarmplot(x='Rok', hue='Kandidátní listina - název', y='Věk', data=candidates)

sns.scatterplot()
```

### Plot pairwise relationships in dataset

```py
sns.pairplot(data, hue='Survived', palette=['red', 'green']) #, diag_kind='hist'
```

## Histogram

- [distplot - DPERACATED](https://seaborn.pydata.org/generated/seaborn.distplot.html)

```py
sns.distplot(df["age"], kde=False)
```

- https://seaborn.pydata.org/tutorial/distributions.html


## Set title

```py
sns.distplot(df["age"], kde=False).set_title("Age distribution")
```

## Color palettes

```py
# Create the palette
pall = sns.color_palette("hls", 8)
# See the palette
sns.palplot(pall)
```

- [palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

## Set style

```py
sns.set_style("dark")
```

[Seaborn aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
