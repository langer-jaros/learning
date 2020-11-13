# How to code

without falling into deep depresion

`2020/10/26, Jaroslav Langer`

## Content <!-- omit in toc -->

- [Recommendations](#recommendations)
  - [Use keyboard as much as possible](#use-keyboard-as-much-as-possible)
  - [Do not invent the wheel](#do-not-invent-the-wheel)
  - [Adding funtionality from elsewhere](#adding-funtionality-from-elsewhere)
  - [How to work on an assingment](#how-to-work-on-an-assingment)
- [Tools that saves time (and scripts)](#tools-that-saves-time-and-scripts)
- [Naming](#naming)
  - [Date and time formats](#date-and-time-formats)
- [Folders hierarchy](#folders-hierarchy)
- [My code routine](#my-code-routine)
- [Test driven development](#test-driven-development)
- [Debugging](#debugging)

## Recommendations

### Use keyboard as much as possible

### Do not invent the wheel

It is so much more fun, to explore the worl by try and fail approach.
Also it is so less efficient. Don't do it often! Just google it, read it, then try it.
Try in small piecies, not big features.
Any time you want to try something big, elsewhere test every tiny piece.
Testing on simple funcionality, is annoing, useless and quick.
On the other hand writing a piece, debugging it at once is hard, challanging, and slow.
Don't conquer the code, write it.

### Adding funtionality from elsewhere

Always try it before adding to your code!
It will probably work if you don't but it will likely to work in other way than you've expected.

### How to work on an assingment

- Do not spend too much time with details right from the beginning.
  - i.e. do the most of the fluent work from the start,
  - the problems will be visible afterwards, and also it will be clear how much time is left.

## Tools that saves time (and scripts)

## Naming

### Date and time formats

```
2020/04/25

2020-04-25

20200425

Apr. 25, 2020
```

As the names of months are in many languages derived form
[latin](https://blogs.transparent.com/latin/months-of-the-year/)
it is not wrong to use their abbreviations.

| Abbreviation | Month |
| --- | --- |
| Jan.| January |
| Feb.| February |
| Mar.| March |
| Apr.| April |
| May | May |
| Jun.| June |
| Jul.| July |
| Aug.| August |
| Sep. or Sept. | September |
| Oct.| October |
| Nov.| November |
| Dec.| December |

[Months abbreviations source](https://abbreviations.yourdictionary.com/articles/standard-month-and-days-of-the-week-abbreviations.html)

## Folders hierarchy

## My code routine

1) Go to projects folder
```sh
cd projects
```

2) Make myself new enviroment (new journey, new terminal)
```sh
bash
```

3) Go to git repository
```sh
cd git_project_name
```

4) Swich to the branch (or create) of the feature or goal
```sh
git checkout example_testing
```

## Test driven development

## Debugging

Do not debug code with debugging prints. It is simle, it is straight forward and it is so bad.
I was doing ti for much longer than i should have. Now I perform debugging inside of MS code.

[link](https://code.visualstudio.com/docs/cpp/config-linux)
