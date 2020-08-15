# JavaScript basics

## MENU

+ [Printing](#printing)
+ [Variables](#variables)
+ [Data types](#data-types)
+ [Conditions](#conditions)
+ [Loops](#loops)
+ [Functions](#functions)
+ [HTML elements](#html-elements)
+ [Handlers](#Handlers)
+ [Coordinates](#coordinates)
+ [Math](#math)
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
Best way for variables is keyword var
```
var name = 0;
```
global variable 
```
[window.prevX, window.prevY] = [ x, y ];
```
[source](https://www.javatpoint.com/javascript-global-variable)
[scope of variables](https://www.sitepoint.com/demystifying-javascript-variable-scope-hoisting/)

## Data types
### String
lenght 
```
myString.length
```
#### Concatenate strings
```
var hello = 'hell' + 'o';
// be careful
var fivety = '5' + 0; // will be '50'
```
#### Accessing chars of string
(like myString[i] in other languages)
```
myString.charAt(i);
```
---

### Arrays
```
var arr = [6,6,7];
```
#### Number of items
```
myArray.length
```
### Adding item to array
```
myArray.push("something");
```
[source](https://www.w3schools.com/js/js_arrays.asp)
### Pop last item
```
item = myArray.pop();
```
---
## Conditions
Switch
```
switch (clicked%4) {
case 0:
    break;
case 1:
    clicked++;
    break;
default:
    clicked = 0;
}
```
[source](https://www.w3schools.com/js/js_switch.asp)

## Loops
```
var i;
for (i = 0; i < cars.length; i++) { 
  text += cars[i] + "<br>";
}
```
[source](https://www.w3schools.com/js/js_loop_for.asp)
For loop i is key, not value
```
for (var i in arr) {
    total = total + i;
}
```
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
## HTML elements
reference to DOM-object of element '<div id="odstavec">' from page
```
var canvas = document.getElementById('canvas01');
```
https://www.w3schools.com/jsref/dom_obj_body.asp


Get root DOM object
```
var outputElement = document.documentElement;
```

vložení připraveného HTML-fragmentu do cílového místa
```
outputElement.innerHTML = txt;
```

### Append child

https://www.w3schools.com/jsref/met_node_appendchild.asp

## Create element specify class

https://www.htmldog.com/guides/javascript/advanced/creatingelements/


### Insert html string to element not replace

```js
element.insertAdjacentHTML(position, text);
```

[source](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)

---
## Handlers
### function handling action, gets event, which called it
```
var onclickHandler = function(evt) {
    console.log('Click on <div id="odstavec">:', evt);
};
```
### Connects event with handler
```
outputElement.onclick = onclickHandler;
```
### Access target from event
```
evt.target.style.backgroundColor = 'yellow';
```
### Handeling general touch 
+ [Pointer](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events)

### On touch screen
+ [touch](https://www.w3schools.com/jsref/obj_touchevent.asp)
+ [Touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events/Using_Touch_Events)

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
## Math
### Radians from degrees
```
rad = Math.PI * deg/180;
```
### Trigonometric functions
```
newX = this.X + length * Math.cos(this.heading);
newY = this.Y - length * Math.sin(this.heading);
```
---
```2019/12/04, Jaroslav Langer```
