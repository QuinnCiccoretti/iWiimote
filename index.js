//this is javascript
//
//


var urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('ipAddr')) {
    var ipAddr = urlParams.get('ipAddr');
    console.log(ipAddr);
}

var testws = document.getElementById("testws");
testws.addEventListener("click", WebSocketTest);
var statusbar = document.getElementById('statusbar');
var ws;
function WebSocketTest() {
    if ("WebSocket" in window) {
        statusbar.innerHTML = "WebSocket is supported by your Browser!";
        if (!ipAddr) {
            statusbar.innerHTML = "You buffoon, you didn't enter the ip in the address";   
        }
        ws = new WebSocket("wss://" + ipAddr);

        ws.onopen = function () {
            statusbar.innerHTML = "Connected to WebSocket at: " + ipAddr;
        };

        ws.onmessage = function (evt) {
            var received_msg = evt.data;
        };

        ws.onclose = function () {
            statusbar.innerHTML = "Connection is closed...";
        };
    } else {
        statusbar.innerHTML ="WebSocket NOT supported by your Browser!";
    }
}

function handleMotion(event) {
    var gyroOut = document.getElementById('gyrobar');
    let gyroscope = event.rotationRate;

    gyroOut.innerHTML = "X-Axis : " + gyroscope.alpha + "<br />";
    gyroOut.innerHTML += "Y-Axis: " + gyroscope.beta + "<br />";
    gyroOut.innerHTML += "Z-Axis : " + gyroscope.gamma + "<br />";
    ws.send(JSON.stringify({
        gyrZ: gyroscope.alpha,
        gyrX: gyroscope.beta
    }));
}

// Get permission to access device sensors
function getPermission() {
    // feature detect for iOS 13+
    if (typeof DeviceMotionEvent.requestPermission === 'function') {
        DeviceMotionEvent.requestPermission()
            .then(permissionState => {
                if (permissionState === 'granted') {
                    window.addEventListener('devicemotion', handleMotion);
                }
            })
            .catch(console.error);
    } else {
        // handle regular non iOS 13+ devices
        window.addEventListener('devicemotion', handleMotion);
    }
}

// Right side buttons
function press_green(){
    console.log("press green");
    ws.send(JSON.stringify({ key: "press shift" }));
}
function release_green() {
    console.log("release green");
    ws.send(JSON.stringify({ key: "release shift" }));
}

function press_blue() {
    console.log("press blue");
}
function release_blue() {
    console.log("release blue");
}

function press_red() {
    console.log("press red");
}
function release_red() {
    console.log("release red");
}

function press_yellow() {
    console.log("press yellow");
    ws.send(JSON.stringify({ key: "press up" }));
}
function release_yellow() {
    console.log("release yellow");
    ws.send(JSON.stringify({ key: "release up" }));
}

addMultipleEventListener("green", ['mousedown', 'touchstart'], press_green);
addMultipleEventListener("green", ['mouseup', 'touchend'], release_green);
addMultipleEventListener("blue", ['mousedown', 'touchstart'], press_blue);
addMultipleEventListener("blue", ['mouseup', 'touchend'], release_blue);
addMultipleEventListener("red", ['mousedown', 'touchstart'], press_red);
addMultipleEventListener("red", ['mouseup', 'touchend'], release_red);
addMultipleEventListener("yellow", ['mousedown', 'touchstart'], press_yellow);
addMultipleEventListener("yellow", ['mouseup', 'touchend'], release_yellow);

// D-pad
function press_up() {
    console.log("I'm up down");
    ws.send(JSON.stringify({ key: "press up" }));
}
function release_up() {
    console.log("I'm up up");
    ws.send(JSON.stringify({ key: "release up" }));
}

function press_down() {
    console.log("I'm down down");
    ws.send(JSON.stringify({ key: "press down" }));
}
function release_down() {
    console.log("I'm down up");
    ws.send(JSON.stringify({ key: "release down" }));
}

function press_left() {
    console.log("I'm left down");
    ws.send(JSON.stringify({ key: "press left" }));
}
function release_left() {
    console.log("I'm left up");
    ws.send(JSON.stringify({ key: "release left" }));
}

function press_right() {
    console.log("I'm right down");
    ws.send(JSON.stringify({ key: "press right" }));
}
function release_right() {
    console.log("I'm right up");
    ws.send(JSON.stringify({ key: "release right" }));
}

addMultipleEventListener("up", ['mousedown', 'touchstart'], press_up);
addMultipleEventListener("up", ['mouseup', 'touchend'], release_up);
addMultipleEventListener("down", ['mousedown', 'touchstart'], press_down);
addMultipleEventListener("down", ['mouseup', 'touchend'], release_down);
addMultipleEventListener("left", ['mousedown', 'touchstart'], press_left);
addMultipleEventListener("left", ['mouseup', 'touchend'], release_left);
addMultipleEventListener("right", ['mousedown', 'touchstart'], press_right);
addMultipleEventListener("right", ['mouseup', 'touchend'], release_right);

function addMultipleEventListener(element, events, handler) {
    events.forEach(e => document.getElementById(element).addEventListener(e, handler, false));
}