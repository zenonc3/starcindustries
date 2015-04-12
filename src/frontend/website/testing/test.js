

function setup(){
  
  var host = "ws://192.168.1.4:9090/ws";
  var socket = new WebSocket(host);

  // event handlers for websocket
  if(socket){

    socket.onopen = function(){
      console.log("connection opened....");
    }

    socket.onmessage = function(msg){
      console.log(msg.data);
      sortActions(msg.data)
      
    }

    socket.onclose = function(){
      //alert("connection closed....");
      console.log("The connection has been closed.");
    }

  }else{
    console.log("invalid socket");
  }

  function sortActions(action){
    if (action === "right" || action == "twistright"){
      prevSlide();
    }else if (action === "left" || action == "twistleft"){
      nextSlide()
    }
  }
  function fadein() {
      $("#outer").hide();
      setTimeout(show(),1000);
      //$("#outer").fadeIn(3000);
  }

  function show() {
      $("#outer").show();
  }

  function nextSlide() {
    $('#carousel-example-generic').carousel('next');
  }

  function prevSlide() {
    $('#carousel-example-generic').carousel('prev');
  }

  document.getElementById("testButton").addEventListener("click", function(){
    console.log("pressed!");
    prevSlide()
  });
  
}

window.onload = setup;