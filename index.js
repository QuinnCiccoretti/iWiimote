//this is javascript
//
var output = document.getElementById('statusbar');

function handleOrientation(event) {
    var x = event.beta;  // In degree in the range [-180,180]
    var y = event.gamma; // In degree in the range [-90,90]

    output.innerHTML = "beta : " + x + "\n";
    output.innerHTML += "gamma: " + y + "\n";

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
console.log("it work");
document.getElementById("green").addEventListener("click", green);
document.getElementById("blue").addEventListener("click", blue);
document.getElementById("red").addEventListener("click", red);
document.getElementById("yellow").addEventListener("click", yellow);
console.log("it work");
