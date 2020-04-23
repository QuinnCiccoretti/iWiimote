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

var gyroOut = document.getElementById('gyrobar');
function handleOrientation(event) {
    var x = event.beta;  // In degree in the range [-180,180]
    var y = event.gamma; // In degree in the range [-90,90]

    // gyroOut.innerHTML = "beta : " + x + "\n";
    // gyroOut.innerHTML += "gamma: " + y + "\n";

    // Because we don't want to have the device upside down
    // We constrain the x value to the range [-90,90]
    if (x > 90) { x = 90 };
    if (x < -90) { x = -90 };

    // To make computation easier we shift the range of 
    // x and y to [0,180]
    x += 90;
    y += 90;

    // 10 is half the size of the ball
    // It center the positioning point to the center of the ball
}

// Get permission to access device sensors
function getPermission() {
    // feature detect
    if (typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission()
            .then(permissionState => {
                if (permissionState === 'granted') {
                    window.addEventListener('deviceorientation', handleOrientation);
                }
            })
            .catch(console.error);
    } else {
        // handle regular non iOS 13+ devices
        window.addEventListener('deviceorientation', handleOrientation);
    }
}
getPermission();

let gyroscope = new Gyroscope({ frequency: 60 });
gyroscope.addEventListener('reading', e => {
    gyroOut.innerHTML = "X-Axis : " + gyroscope.x + "<br />";
    gyroOut.innerHTML += "Y-Axis: " + gyroscope.y + "<br />";
    gyroOut.innerHTML += "Z-Axis : " + gyroscope.x + "<br />";
    ws.send(JSON.stringify({
        gyrZ: gyroscope.z,
        gyrX: gyroscope.x
    }));
});
gyroscope.start();

// Right side buttons
function green(){
    console.log("I'm green");
}
function red(){
    console.log("I'm red");
}
function yellow(){
    console.log("I'm yel");
    ws.send(JSON.stringify({mouse: "Left Click"}));
}
function blue(){
    console.log("I'm baby");
}
document.getElementById("green").addEventListener("click", green);
document.getElementById("blue").addEventListener("click", blue);
document.getElementById("red").addEventListener("click", red);
document.getElementById("yellow").addEventListener("click", yellow);

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