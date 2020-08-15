# Learn HTML5 and CSS3

Extracted information from youtube video course
[Link to the video. (freeCodeCamp.org)](https://youtu.be/mU6anWqZJcc)

## MENU

+ [Images colors background linear-gradient](#images-colors-background-linear-gradient)
+ [Types of values](#types-of-values)
+ [Fonts and Icons](#fonts-and-icons)
+ [Text-Align And Text-Indent](#text-align-and-text-indent)
+ [Border, Margin](#border,-margin)
+ [Navigate inside webpage](#navigate-inside-webpage)
+ [Display, Opaciti, Visibility](#display,-opaciti,-visibility)
+ [Positions static, relative, fixed, absolute](#positions-static,-relative,-fixed,-absolute)
+ [CSS selectors Before, After, child, Frist-line](#CSS-selectors-before,-after,-child,-frist-line)
+ [Hover](#hover)
+ [Root selector](#root-selector)
+ [Transform, transition](#transform,-transition)
+ [Animation](#animation)
+ [Css Variables](#css-variables)
+ [Text-Shadow Box-Shadow](#text-shadow-box-shadow)
+ [Browser Prefixes](#browser-prefixes)
+ [Semantic Tags](#semantic-tags)
+ [Events handling](#events-handling)

## Not from the video
+ [](#)

## USE LIVE SERVER

perhaps from visual studio code

## Minimal html site

https://www.sitepoint.com/a-minimal-html-document-html5-edition/

## Link css in html

https://www.w3schools.com/tags/tag_link.asp

## Images colors background linear-gradient
### Images knowledge 
[ 16) Images - 51:17 ]

### Sites with free images    
[pixabay](https://pixabay.com)
[pexels](https://www.pexels.com/)
[gratisography](https://gratisography.com/)

## Color pallete

74) External Resources - 04:52:57
[Color pallete](https://coolors.co/)

## 111) Background Image Shortcuts Combined - 07:56:49
```
.header{
    backround: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
    url("./big.jpeg")center/cover no-repeat fixed;
}
```
## 112) Linear-Gradient Colorzilla - 08:06:56
[css gradient generator](https://www.colorzilla.com/gradient-editor/)

## Types of values

[ 77) Percent Values - 05:02:13 | 78) Em Values - 05:05:44 | 79) Rem Values - 05:11:42 ]
```
percents depend on parant</p>
ems depend on parant</p>
rems depend on root of document</p>
*{
    margin 0;
    padding 0;
    box-sizing: border-box;
}
```
## Fonts and Icons

### Google Fonts

[ 86) - 05:39:23 ]

[Fonts google](https://fonts.google.com/)

### Font-Awesome Icons 

143) Font-Awesome Icons - 10:56:19    

fontawesome.com


## Text-Align And Text-Indent

88) Text-Align And Text-Indent - 05:53:30
```text-indent: 50px```

## Border, Margin

94) Border-Radius, Negative Margin - 06:23:57
```
p {
    border-radius: 50%;
}
```

## Navigate inside webpage

99) Mobile Navbar Example - 06:48:11
```<a href="#">#</a>```

## Display, Opaciti, Visibility

102) Display:none, Opacity, Visibility - 07:09:29
```
opacity | opacity-5 | opacity-0
backround-repeat: round
```

## Positions static, relative, fixed, absolute

116) Position Static - 08:25:59 | 117) Position Relative - 08:30:44  118) Position Absolute - 08:33:18 | 119) Position Fixed - 08:38:4

oo

## CSS selectors Before, After, child, Frist-line

### ::Before And ::After

122) ::Before And ::After Pseudo Elements - 09:06:04
```css
p::before{ content: "hello "; display: block;}
```

### Descendent child selectors >

125) Descendant Child Selectors - 09:31:07
```css
div h1 {} | div > h1 {}
```

### First-line, first-letter

126) First Line And First Letter - 09:35:50
```css
p::first-line {} | p::first-letter
```

## Hover
127) :Hover Pseudo-Class Selector - 09:36:56
```css
p:hover
```

## Root selector

129) :Root Preudo-Class Selectors - 09:44:36

```css
p:root - good for responsive size of text
```

## Transform, transition

### Transform:transition()

131) Transform:transition() - 09:52:17

```css
display: inline-block;
transform: translate(px, px)
transform: scale( $num, $num)
transform: rotateX|Y|Z($(num)deg) 
transform: skew(40deg, 60deg)
```

### Transition Property

135) Transition Property - 10:06:31

```css
div:hover {
    backround: coral;
}
.three{
    transition-property: backround;
    transition-duration: 4s;
}
transition-delay: 4s;
transition: {property} {lenght} {delay  
transition: all 4s function 5s;
}
```

### Transition-Timing Function

138) Transition-Timing Function - 10:16:36

```css
ease = default
.sth{
    transition-timig-function: ease;
}
ease | linear | ease-in | ease-out | ease-in-out
```

## Animation

139) Animation - 10:25:51

```css
@keyframes  move {
    0%{
        transform: translateX
    } 
    50%{
        transform: translateX
    }
}
.div {
    animation-name: move;
    animation-duration: 10s;
    animation-iteration-count: 2;
    animation: move duration count;
    animation: move 5s infinite;
}
```

### Animation-Fill-Mode

140) Animation-Fill-Mode - 10:35:51

```css
animation-fill-mode: forwards;
```

## Css Variables

142) Css Variables - 10:41:32

```css
:root{
    --primaryColor: #f15025;
}
.div{
    color:var(--primaryColor)
}
```

## Text-Shadow Box-Shadow

144) Text-Shadow Box-Shadow - 11:07:55

box-shadow generator

can i use css

## Browser Prefixes

145) Browser Prefixes - 11:14:44

autoprefixer css online

## Semantic Tags

146) Semantic Tags - 11:19:23
semantic HTML

## Events handling

### Click
```
onclick="changeColor('black')
```
### Touch
```
ontouchmove="funMove(event)" 
ontouchstart="funStart(event)" 
ontouchend="funEnd(event)"
```
### Mouse
```
onmousedown="mouseDown(event)" 
onmousemove="mouseMove(event)" 
onmouseup="mouseUp(event)" 
```
### Pointer
```
onpointermove="funMove(event)"
onpointerdown="funDown(event)"
onpointerup="funUp(event)"
```

## Grid

https://css-tricks.com/snippets/css/complete-guide-grid/
https://www.w3schools.com/css/css_grid.asp

```css
display: grid;
    grid-template-columns: 3fr 1fr 6fr 1fr;
```

## Background image

https://www.w3schools.com/html/html_images_background.asp

```css
background-image: url("../pictures/industry-839254_1920.jpg");
```

## Scripts

The script can be placed either in the head, or in the body [link](https://www.w3schools.com/js/js_whereto.asp)

Prefered way is to put it at the end of body, or in the head, if it si executed once the body is load. [link](https://faqs.skillcrush.com/article/176-where-should-js-script-tags-be-linked-in-html-documents)

```html
<script src='./path/script.js'></script>
```

## history

The browser remembers the history and it is possible to travel forward and backward through it.
[link](https://stackoverflow.com/questions/824349/how-do-i-modify-the-url-without-reloading-the-page)