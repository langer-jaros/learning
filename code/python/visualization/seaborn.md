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
  - [Dash styles](#dash-styles)
- [Set style](#set-style)

## Import

```py
import seaborn as sns
```

## lineplot

```py
g = sns.relplot(x="time", y="value", kind="line", data=df)
# Legend full to see present values in legend, not approximative
g2 = sns.lineplot(hue="something", legend="full" sort=False)
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

### Dash styles

It is not possible to plot more than 6 values with different style.

In case it needed, the styles can be defined.

```py
dash_styles = ["",
               (4, 1.5),
               (1, 1),
               (3, 1, 1.5, 1),
               (5, 1, 1, 1),
               (5, 1, 2, 1, 2, 1),
               (2, 2, 3, 1.5),
               (1, 2.5, 3, 1.2)]
sns.relplot(...,  dashes=dash_styles,...)
```

- [dash_styles](https://github.com/mwaskom/seaborn/issues/1513)

## Set style

```py
sns.set_style("dark")
```

[Seaborn aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
