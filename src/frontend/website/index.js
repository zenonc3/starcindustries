function displayc() {
var refresh=1000; // Refresh rate in milli seconds
mytime=setTimeout('displayct()',refresh);
}

function displayct() {
var strcount;
var x = new Date();
document.getElementById('ct').innerHTML = x;
tt=displayc();
}
