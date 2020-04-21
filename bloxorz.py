import keyboard
import mouse
from iWiimote import iWiimote

#phyphox configuration
LOCK_INPUT = False
PP_CHANNELS = ["accX", "accY", "accZ"]
def update(iw):
    data = iw.getData()
    accX = data["accX"]
    accY = data["accY"]
    accZ = data["accZ"]
    
    global LOCK_INPUT
    threshold = 3
    
    if(accX and accY and accZ):
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
                keyboard.press_and_release(move_dir)
                LOCK_INPUT = True
        elif(not any_input):
                LOCK_INPUT=False

			
def main():
    iw = iWiimote(PP_CHANNELS)
    while True:
        update(iw)

if __name__ == '__main__':
    main()
