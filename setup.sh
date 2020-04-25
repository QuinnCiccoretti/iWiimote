# !/bin/bash
$1 = IP

cd ./server/certificates
./generateCerts.sh 192.168.1.3
cd ../
