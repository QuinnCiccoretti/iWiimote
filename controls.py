import keyboard
import mouse

class Controls():
    def __init__(self, update):
        self.update = update

"""Function call to translate sensor readings to controls for minecraft
Rotate left/right to look around
Tilt foward to move 
Tile backward to jump
"""
def minecraftUpdate(acc=(0,0,0), gyro=(0,0,0), mag=(0,0,0)):
    accX, accY, accZ = acc
    # Oritentation left-right
    if (abs(accY)>0.5): # dead zone within (-0.5, 0.5)
        mouse.move(accY*10, 0, absolute=False)
    
    # Foward
    if(accZ < -1):
        keyboard.press('up')
    else:
        keyboard.release('up')
    # Jump
    if(accZ < -1):
        keyboard.press('up')
    else:
        keyboard.release('up')

Minecraft = Controls(minecraftUpdate)


##################################
## Change the current Game to the selected game
##################################
Game = Minecraft
