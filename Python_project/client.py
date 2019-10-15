#클라이언트연결
import socket
import time
import struct
#소켓 셋팅(TCP통신)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#소켓 연결(주소,포트)
sock.connect(('10.1.0.26', 5000))
#message = 1,3,0,101,0,5,149,214
#message = 0x01,0x03,0x00,0x65,0x00,0x05,0x95,0xd6
#send message 작성 
message = bytearray(8)
message[0] = 0x01
message[1] = 0x03
message[2] = 0x00
message[3] = 0x65
message[4] = 0x00
message[5] = 0x05
message[6] = 0x95
message[7] = 0xd6
#메세지전송, 서버 호출
sock.send(message)
#수신대기 10초
time.sleep(20)
#메세지 수신 및 설정 1024byte
sock.settimeout(10)
data = sock.recv(1024)
co2 = round(((data[3]<<8) + data[4]),1)
temp = round((((data[5]<<8) + data[6])/10.1),1)
humi = round((((data[7]<<8) + data[8])/10.1),1)
print("co2:", co2,"PPM")
print("temp:", temp,"C")
print("humi:", humi,"%")

        