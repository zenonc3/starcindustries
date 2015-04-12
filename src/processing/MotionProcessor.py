import socket, traceback
import time

#class DataStream(threading.Thread):
#	def run(self):

class MotionProc:
	
	def __init__(self):
		self.action = 'nomovement'
		self.callback = self.placeholder_callback
    		
	def set_callback(self, callbackref):
		self.callback = callbackref
        
	def placeholder_callback(self, action):
		print '[Not connected] action: ' + str(action)
	
	def gesture_loop(self):
		host = '192.168.1.4'
		port = 5555
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		s.bind((host, port))
		counter=0
		counting=False
		action="starting"
		while 1:
			try:
			#print counter, counting

				if counter==20:
					counting=False
					counter=0
				#Get full string
				message, address = s.recvfrom(8192)
				#print counter
				#print message
				if counting==True:	
					counter=counter+1

				else:

					#strip space
					message.strip(" ")

					#message.replace(" ,",",")
					#delimit string
					delimitedVariables=message.split(",");

					#Extract gyroscope information and convert to integer
					if delimitedVariables[5]!=4:

						gx= float(delimitedVariables[6])
						gy= float(delimitedVariables[7])
						gz= float(delimitedVariables[8])
						#print gx,gy, gz
						threshold=5;

						maxValue = max(gx, gy, gz)
						minValue = min(gx,gy,gz)
						#print maxValue, minValue

						if(abs(maxValue)>abs(minValue)):
							largest = maxValue

						else:
							largest = minValue 
						#Get action
						if largest < -threshold and largest==gx:
							self.action = "left"
							counting=True
							self.callback(self.action)
						elif largest > threshold-1 and largest==gx:
							self.action = "right"
							counting=True
							self.callback(self.action)
						elif largest > threshold-2 and largest==gz: 
							self.action= "up"
							counting=True
							self.callback(self.action)
						elif largest < -threshold and largest==gz:
							self.action="down"
							counting=True
							self.callback(self.action)
						elif largest < -threshold and largest==gy:
							self.action="twistleft"
							counting=True
							self.callback(self.action)
						elif largest > threshold and largest==gy:
							self.action="twistright"
							counting=True
							self.callback(self.action)

						else:
							action="nomovement"
							counting=False

				#time.sleep(0.1)
				#print gx,gy,gz
					#print message
			except (KeyboardInterrupt, SystemExit):
				raise
			except:
				traceback.print_exc()
				
				

			
if __name__ == "__main__":
	mp = MotionProc()
	mp.gesture_loop()
	
	

