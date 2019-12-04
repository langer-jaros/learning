# Canvas

## MENU
+ [Accessing trough context](#accessing-trough-context)
+ [Canvas offset](#canvas-offset)
+ [Buttons](#buttons)
+ [Drawing](#drawing)
+ [Canvas properties](#canvas-properties)

## Accessing trough context
```
var canvas = document.getElementById('cnvs01');
var ctx = canvas.getContext('2d');

ctx.ANYTHING(...)
```

## Canvas offset
```
var rect = event.target.getBoundingClientRect();
var x = event.pageX - rect.left;
var y = event.pageY - rect.top;
```

## Buttons
```
if(event.buttons>0)
    ctx.fillRect(x, y, 5, 5);
```
[source](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)

## Drawing
### Circle 
```
ctx.drawCircle = function(x, y, r){
        this.beginPath();
        this.arc(x, y, r, 0, 2*Math.PI);
        this.fill();
    }
```
### Line
```
ctx.drawLine = function(x, y){
    this.beginPath();
    this.moveTo(window.prevX, window.prevY);
    this.lineTo(x, y);
    this.stroke();
}
```
+ [draw a line](https://www.w3schools.com/tags/canvas_lineto.asp)
+ [line tutorial](https://www.html5canvastutorials.com/tutorials/html5-canvas-line-color/)

## Canvas properties
### Widht and height
```
[canvas.width, canvas.height] = [window.innerWidth, window.innerHeight];
```
### Baground colour
```
canvas.style.backgroundColor = 'lightblue';
```

### Line width
```
ctx.lineWidth = 50;
```
### Line color
```
var changeColor = function(color){
    ctx.strokeStyle = color;
}
```
---
`2019/12/04, Jaroslav Langer`
