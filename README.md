# Midas by Starc Industries
Created as part of the SpaceApps NZ 2015 challenge.

This product is a piece of wearable technology that allows a user to program gestures and associate them with actions on a computer or another piece of wearable technology, such as an HUD. It is designed to allow computer control and data transmission while performing other tasks such as conducting on-board experiments. Uses of the technology include navigating between different views on a head-mounted display, performing basic tasks on a main computer and logging external sensor data. 

##Getting set up

###What you're going to need:

 - An Android phone with a Gyroscope and [SensorStream](https://play.google.com/store/apps/details?id=de.lorenz_fenster.sensorstreamgps&hl=en) installed.
 - Python 2.7
 - Tornado Server installed on your machine - Its easiest to do this with the [pip](https://pip.pypa.io/en/stable/#) command  `pip install tornado`


### Lets get this show rollin'

 1. Clone our git repository somewhere nice  (preferably on a machine running Windows or OSX since we've tested on these)
 2. Whip open terminal/command prompt like you're Tony Stark and `cd` into `src/processing/` as fast as you can. `python ProcessServer.py` is what you want to type once you're there.
 3. Open up `test.js` - you can find it in `src/frontend/website/testing/`. 
 ( 3a. Pretend to like our naming scheme.)
 4. Change the host IP address to that of your own machine. Theres a good chance `localhost` will work as well if you can't be bothered finding this out.
 5. Open up `test.html` in your web browser (we've' tested Chrome and Safari). 
 6. Grab your phone (with SensorStream running) and swipe around like you know what you're doing. We've got support for up,down,left,right,and twists!

 - For voice, we've set up a wit instance with a couple of trained commands [here](https://wit.ai/zncolaco/spaceglove) that you can try out, although its not really wired up with the rest of the system.


