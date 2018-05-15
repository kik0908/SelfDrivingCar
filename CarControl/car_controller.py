import pygame
from sys import exit
import socket
import cv2 as cv
import pickle
import numpy


screen = pygame.display.set_mode((600, 200))



pov_c = 6

speed_c = 5


speed = 1400
speed_d = speed
pov = 90

flags = []

clock = pygame.time.Clock()
flag = False

while True:
    s = socket.socket()
    s.connect(('172.24.1.1', 1080))



    screen.fill((155,255, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                s.connect(('172.24.1.1', 1080))
                s.send(b'11/1400/90')
                print(1)
                s.close()
            except:
                pass
            exit(3456)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if speed - speed_c == 1400:
                    s.send(b'00/1400/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    s.send(b'00/1300/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    s.send(b'00/1400/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    #s.send(b'00/1350/90')
                    #s.close()
                    #s = socket.socket()
                    #s.connect(('172.24.1.1', 1080))

                speed = max(speed - speed_c, 1100)

            elif event.key == pygame.K_s:
                if speed - speed_c == 1400:
                    s.send(b'00/1400/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    s.send(b'00/1500/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    s.send(b'00/1400/90')
                    s.close()
                    s = socket.socket()
                    s.connect(('172.24.1.1', 1080))
                    #s.send(b'00/1450/90')
                    #s.close()
                    #s = socket.socket()
                    #s.connect(('172.24.1.1', 1080))



                speed = min(speed + speed_c, 1600)

            if event.key == pygame.K_a:
                pov = min(120, pov + pov_c)
            elif event.key == pygame.K_d:
                pov = max(60, pov - pov_c)

    a = '00/{}/{}'.format(speed, pov).encode()
    print(a)
    s.send(a)
    print(a, 1)
    print('b')
    s.close()

    #s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_address = ('', 1085)
    #s1.bind(server_address)
    #s1.listen(1)
    #conn, addr = s1.accept()
    #data = []
    #for i in range(30):
    #    packet = conn.recv(1024)
    #    data.append(packet)
    #frame = b''.join(data)
    #print(frame)
    #with open('1.txt', 'rb') as file:
    #    frame = pickle.load(file)
#
    #print(type(frame))
    #cv.imshow('frame', pickle.loads(frame))
    #conn.close()



    pygame.display.flip()