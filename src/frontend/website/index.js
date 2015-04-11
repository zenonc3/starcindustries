function displayc() {
	var refresh=1000; // Refresh rate in milli seconds
	mytime=setTimeout('displayct()',refresh);
}

function displayct() {
	var strcount;
	var x = new Date();
	//document.getElementById('ct').innerHTML = x;
	tt=displayc();
}

function displayLog() {
	var logMessageExists;
	if (logMessageExists === true) {
		var x = new Date();
		var logMessageType = "Log";
		var logMessage = "";
	}	
}

function displayt() {
	var y = new Date();
	//var z = y.getTime()
	document.getElementById('t').innerHTML = y;
	yy = displayt();
}