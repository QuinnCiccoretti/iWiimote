# iWiimote

### Python

This is written using python3.7

Run `pip install -r requirements.txt` to get the necessary python packages

### Starting the Controller

#### 0. Openssl
Make sure you have the most up to date version of openssl (1.1.1c or higher). You can check this by running `openssl version` in your command line.

### 1. Startup
```
cd server
python start.py
```
Run the above to start the server. Scan the QR code and go to the website on your local network for instructions. 

### 2. Generate Certification for websockets
There are two versions of generateCerts.sh. If any error messages pop up in your console, try the other file. Please run `generateCerts.sh IP` in the root directory in Git Bash on Windows or your normal Command Line on other OSs with the parameter being the IP address that appears in the runtime above. For example, run `generateCerts.sh 192.168.1.3`.

### 3. Runtime
You can now run the server whenever you want. You may need to close the terminal every time you need to restart the server. To start the server after this setup, run the below command.
```
cd server
python controller.py
```

### Controller Website
https://iwiimote.herokuapp.com/?ipAddr=IP:12000
![Image description]()


