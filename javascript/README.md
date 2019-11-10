# JavaScript basics

## MENU

+ [Printing](#printing)
+ [Variables](#variables)
+ [Functions](#functions)
+ [Get HTML element](#get-html-element)
+ [Canvas](#canvas)
+ [Coordinates](#coordinates)
---
## Printing
Alert, blocks anything
```
alert('POP-UP MESSAGE!');
```
Write to log, great for debuging
```
console.log(total, typeof total);
```
---
## Variables
```
var name = 0;
```
global variable 
```
window.name = 0;
```
[source](https://www.javatpoint.com/javascript-global-variable)
[scope of variables](https://www.sitepoint.com/demystifying-javascript-variable-scope-hoisting/)

---
## Functions
```
var x = myFunction(4, 3);   // Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             // Function returns the product of a and b
}
```
[source](https://www.w3schools.com/js/js_functions.asp)

---
## Get HTML element
```
var canvas = document.getElementById('canvas01');
```
---
## Canvas
Nessesity to call, accessing through ctx.ANYTHING...
```
var ctx = canvas.getContext('2d');
```

### Get offset of the canvas
```
var rect = event.target.getBoundingClientRect();
var x = event.pageX - rect.left;
var y = event.pageY - rect.top;
```

### Handeling general touch 
+ [Pointer](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events)

### On touch screen
+ [touch](https://www.w3schools.com/jsref/obj_touchevent.asp)
+ [Touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events/Using_Touch_Events)

### Buttons 
```
if(event.buttons>0)
    ctx.fillRect(x, y, 5, 5);
```
[source](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)
### Drawing
Circle 
```
ctx.drawCircle = function(x, y, r){
        this.beginPath();
        this.arc(x, y, r, 0, 2*Math.PI);
        this.fill();
    }
```
Line
```
ctx.drawLine = function(x, y){
    this.beginPath();
    this.moveTo(window.prevX, window.prevY);
    this.lineTo(x, y);
    this.stroke();
    [window.prevX, window.prevY] = [ x, y ];
}
```
+ [draw a line](https://www.w3schools.com/tags/canvas_lineto.asp)
+ [line tutorial](https://www.html5canvastutorials.com/tutorials/html5-canvas-line-color/)

#### Properties
Line width
```
ctx.lineWidth = 50;
```
Line color
```
var changeColor = function(color){
    ctx.strokeStyle = color;
}
```
---
## Coordinates
```
var actionDown = function(evt){
    console.log('clientX/Y: ', evt.clientX, evt.clientY );
    console.log('layerX/Y: ', evt.layerX, evt.layerY );
    console.log('pageX/Y: ', evt.pageX, evt.pageY );
    console.log('x/y', evt.x, evt.y );
    console.log("---------------------");
}
```
---
```10/11/2019, Jaroslav Langer```
