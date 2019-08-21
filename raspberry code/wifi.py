import RPi.GPIO as GPIO
from time import ctime
from socket import *
import robot


robot.init()
host = ''
port = 21567
size = 1024
addr = (host,port)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(addr)
tcpSerSock.listen(5)
print("started");

while True:
        
        tcpCliSock,ad = tcpSerSock.accept()
        try:
                while True:
                        data=(tcpCliSock.recv(size)).decode("utf-8")
                        print(data=="null")
                        print(data)
                        if not data:
                                break
                        else:
                                if data == "null":
                                        robot.null()
                                else:
                                        try:
                                                data = int(data)
                                        except:
                                                break
                                        
                                        if data>0 and data <90:
                                                procent = int((data/90)*100)
                                                robot.rightUp(procent)
                                        elif data > 90 and data <180:
                                                procent = int(((data-90)/90)*100)
                                                robot.leftUp(procent)
                                        elif data > 180 and data <270:
                                                procent = int(((data-180)/90)*100)
                                                robot.leftDown(procent)
                                        elif data > 270 and data <360:
                                                procent = int(((data-270)/90)*100)
                                                robot.rightDown(procent)
                                        elif data == 0:
                                                robot.rightUp(0)
                                        elif data == 90:
                                                robot.rightUp(100)
                                        elif data == 180:
                                                robot.leftDown(0)
                                        elif data == 270:
                                                robot.rightDown(100)
                        
                                        
                                        


                                        
                                        

        except KeyboardInterrupt:
                robot.close()
                
tcpSerSock.close()
