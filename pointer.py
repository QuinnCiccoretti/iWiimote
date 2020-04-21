import keyboard
import mouse
import fire
from iWiimote import iWiimote

PP_CHANNELS = ["gyrX", "gyrY", "gyrZ"]
def update(iw):
    data = iw.getData()
    # Gyroscope
    gyrX = data["gyrX"]
    gyrY = data["gyrY"]
    gyrZ = data["gyrZ"]
    if(gyrX and gyrY and gyrZ):
            mouse.move(-gyrZ*20, -gyrX*20, absolute=False)
			
def main():
    iw = iWiimote(PP_CHANNELS)
    while True:
        update(iw)

if __name__ == '__main__':
	main()
