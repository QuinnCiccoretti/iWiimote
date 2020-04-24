#Import libraries
import socket 
import http.server
import socketserver 
import cv2  
import pyqrcode
from pyqrcode import QRCode
from PIL import Image

import os
import sys
import fileinput

def startInstructionServer(IP):     
    print("Your Computer IP Address is:" + IP)

    url1 = "http://"+IP + ":" + "8000"

    #Generate QR Code
    url = pyqrcode.create(url1)
    url.png("Insmyqr.png",scale=8)
    img = cv2.imread("myqr.png")
    # print(type(img))
    cv2.imwrite('myqr.png',img)
    im = Image.open('myqr.png')
    im.show()

    with open("InstructionsServer/index_source.html") as f:
        with open("index.html", "w") as f1:
            for line in f:
                f1.write(line)

    # Inserts the IP address into the correct positions in the index.html file
    text_to_search = "(IP)" 
    replacement_text = IP+":12000"
    with fileinput.FileInput("index.html", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

    #Start http server
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        print("Running your port")
        httpd.serve_forever()


if __name__ == '__main__':
    startInstructionServer()