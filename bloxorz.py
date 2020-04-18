import requests
import keyboard
import mouse


#phyphox configuration
PP_ADDRESS = "http://192.168.1.232"
PP_CHANNELS = ["accX", "accY", "accZ"]
LOCK_INPUT = False
RELEASE = True
def update(url):
	data = requests.get(url=url).json()
	accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
	accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
	accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
	global LOCK_INPUT
	# mouse.move(-accX*20, -accY*20, absolute=False)
	threshold = 3
	if(accX and accY and accZ):
		#print(accX, sep=" ")
		left = accY < -threshold
		right = accY > threshold
		up = accX < -threshold
		down = accX > threshold
		any_input = up or down or left or right
		if(not LOCK_INPUT):
			move_dir = None
			if(left):
				move_dir = "left"
			if(right):
				move_dir = "right"
			if(up):
				move_dir = "up"			
			if(down):
				move_dir = "down"
			
			if(any_input):
				LOCK_INPUT = True
		elif(not any_input):
			LOCK_INPUT=False

			
def main():
	url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))
	while True:
		update(url)
		

if __name__ == '__main__':
	main()
