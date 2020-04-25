# !/bin/sh
IP=$1

mkdir ./server/certificates
cd ./server/certificates
# Generate Certificate Authority
openssl genrsa -out myCA.key 2048
openssl req -x509 -sha256 -new -key myCA.key -out myCA.cer -days 730 -subj "//CN=""iWiimote CA"
# Generate Server Certificate
openssl genrsa -out iwiimote_server.key 2048
openssl req -new -out iwiimote_server.req -key iwiimote_server.key -subj "//CN=$IP"
# Example hostextfile
# extendedKeyUsage=1.3.6.1.5.5.7.3.1
# subjectAltName=IP:192.168.1.3
echo extendedKeyUsage=1.3.6.1.5.5.7.3.1 > hostextfile
echo subjectAltName=IP:$IP >> hostextfile
openssl x509 -req -sha256 -in iwiimote_server.req -out iwiimote_server.cer -CAkey myCA.key -CA myCA.cer -days 365 -CAcreateserial -CAserial serial -extfile hostextfile
cd ../../