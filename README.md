# iWiimote

### Python

This is written using python3.7

Run `pip install -r requirements.txt` to get the necessary python packages

### Starting the Controller

#### Openssl
Make sure you have the most up to date version of openssl (1.1.1c or higher)

### Runtime
Run `python start.py` to start the server. Scan the QR code and go to the website on your local network for instructions.

### Generate Certification for websockets
Please run the `generateCerts.sh IP` file in Git Bash on Windows or your normal Command Line on other OSs with the parameter being the IP address that appears in the runtime above. For example, run `generateCerts.sh 192.168.1.3`.


