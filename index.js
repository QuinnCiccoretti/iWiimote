//this is javascript
//
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
document.body.onload=function(){
    console.log("it work");
    document.getElementById("green").addEventListener("click", green);
    document.getElementById("blue").addEventListener("click", blue);
    document.getElementById("red").addEventListener("click", red);
    document.getElementById("yellow").addEventListener("click", yellow);
    console.log("it work");
}
