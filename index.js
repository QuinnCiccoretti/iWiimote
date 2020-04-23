//this is javascript
//
//
const KeyboardEnum = Object.freeze(
    {
        "Left":  1,
        "Right": 2,
        "Up":    3,
        "Down":  4,
        "Space": 5,
    }
);

const MouseEnum = Object.freeze(
    {
        "Right_Click": 0,
        "Left_Click":  1,
        "Move":        2,
    }
);

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
}
function blue(){
    console.log("I'm baby");
}
document.getElementById("green").addEventListener("click", green);
document.getElementById("blue").addEventListener("click", blue);
document.getElementById("red").addEventListener("click", red);
document.getElementById("yellow").addEventListener("click", yellow);

// D-pad
function up() {
    console.log("I'm up");
    ws.send(JSON.stringify({key: "Up"}));
}
function down() {
    console.log("I'm down");
    ws.send(JSON.stringify({key: "Down"}));
}
function left() {
    console.log("I'm left");
    ws.send(JSON.stringify({key: "Left"}));
}
function right() {
    console.log("I'm right");
    ws.send(JSON.stringify({key: "Right"}));
}
document.getElementById("up").addEventListener("click", up);
document.getElementById("down").addEventListener("click", down);
document.getElementById("left").addEventListener("click", left);
document.getElementById("right").addEventListener("click", right);
