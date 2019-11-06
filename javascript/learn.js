// Alert, blocking anything
alert('NEVSTUPUJ POKUD SE BOJIS!');

// Best way for variables is keyword var
var total = 0;

// Array
var arr = [6,6,7];


// For loop i is key, not value
for (var i in arr) {
    total = total + i;
}

// Write to log, great for debug
console.log(total, typeof total);

// reference na DOM-objekt elementu <div id="odstavec"> ze stránky
var outputElement = document.getElementById('odstavec');

// Get root DOM object
var outputElement = document.documentElement;

var clicked = 0;

// function handling action, gets event, which called it
var onclickHandler = function(evt) {
    console.log('Click on <div id="odstavec">:', evt);
    switch(clicked%4) {
        case 0:
            evt.target.style.backgroundColor = 'yellow';
            clicked++;
          break;
        case 1:
            evt.target.style.backgroundColor = 'purple';
            clicked++;
            break;
        case 2:
            evt.target.style.backgroundColor = 'blue';
            clicked++;
            break;
        case 3:
            evt.target.style.backgroundColor = 'red';
            clicked++;
            break;
      }


};

// Connects the event with handler
outputElement.onclick = onclickHandler;

// vložení připraveného HTML-fragmentu do cílového místa
outputElement.innerHTML = txt;