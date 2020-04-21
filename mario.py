import keyboard
import mouse
from iWiimote import iWiimote

#phyphox configuration
MOVE_DIR = "left"
PP_CHANNELS = ["accX", "accY", "accZ"]
def update(iw):
    data = iw.getData()
    accX = data["accX"]
    accY = data["accY"]
    accZ = data["accZ"]
    
    threshold = 3
    
    if(accX and accY and accZ):
        left = accY < -threshold
        right = accY > threshold
        up = accX > threshold*2
        down = accX < -threshold*2
        
        if(left):
            keyboard.press("left")
        else:
            keyboard.release("left")
        
        if(right):
            keyboard.press("right")
        else:
            keyboard.release("right")
        
        if(up):
            keyboard.press("s")
        else:
            keyboard.release("s")
        
        if(down):
            keyboard.press("down")
        else:
            keyboard.release("down")

			
def main():
    iw = iWiimote(PP_CHANNELS)
    while True:
        update(iw)

if __name__ == '__main__':
    main()
