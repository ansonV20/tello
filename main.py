import socket
import time, random

from djitellopy import TelloSwarm


#

tello1 = "192.168.1.3"

tello2 = "192.168.1.4"

tello3 = "192.168.1.5"

tello4 = "192.168.1.6"

tello5 = "192.168.1.7"

tello6 = "192.168.1.8"
#

UDP_IP = [tello1, tello2, tello3, tello4, tello5, tello6]
UDP_PORT = 8889
MESSAGE = ["EXT led 0 255 0", "EXT led 0 255 0", "EXT led 0 255 0"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# sock.sendto(MESSAGE[0].encode(), (UDP_IP[0], UDP_PORT))
# sock.sendto(MESSAGE[1].encode(), (UDP_IP[1], UDP_PORT))


swarm = TelloSwarm.fromIps([
    tello1,
    tello2,
    tello3,
    tello4,
    tello5,
    tello6
])

swarm2 = TelloSwarm.fromIps([
    tello1,
    tello2,
    tello3
])

allTello = [
    tello1,
    tello2,
    tello3,
    tello4,
    tello5,
    tello6
]

allTelloR = [
    tello6,
    tello5,
    tello4,
    tello3,
    tello2,
    tello1
]

#


tello1S = TelloSwarm.fromIps([
    tello1
])
tello2S = TelloSwarm.fromIps([
    tello2
])
tello3S = TelloSwarm.fromIps([
    tello3
])
tello4S = TelloSwarm.fromIps([
    tello4
])
tello5S = TelloSwarm.fromIps([
    tello5
])
tello6S = TelloSwarm.fromIps([
    tello6
])
#
drone = [tello1S, tello2S, tello3S, tello4S, tello5S, tello6S]
#

# drone2 = [tello1S, tello2S, tello3S]
#
# drone[0].connect()
# drone[1].connect()
# drone[2].connect()
#
# time.sleep(1)
#
# swarm2.takeoff()
#
# swarm.land()
# swarm.end()

# time.sleep(100)

for i in range(6):
    print(i+1)
    drone[i].connect()
    # drone[i].move_down(30)
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    # sock.send("EXT mled g b000000bbb00000bb0b0000bb00b000bb000b00bb0000b0bb00000bbb000000b".encode())
    sock.send("battery?".encode())
    data = sock.recv(1024)
    print(data)
    time.sleep(0.5)

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    sock.send("EXT led 0 0 0".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())


input("==========")

for i in range(5):
    print(5-i)
    time.sleep(1)



for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    sock.send("EXT led 255 255 255".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
    time.sleep(1)

time.sleep(2)

# #N
# sock.connect(((allTello[0]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g b000000bbb00000bb0b0000bb00b000bb000b00bb0000b0bb00000bbb000000b".encode())
# time.sleep(0.8)
# #I
# sock.connect(((allTello[1]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g bbbbbbbb000bb000000bb000000bb000000bb000000bb000000bb000bbbbbbbb".encode())
# time.sleep(0.8)
# #G
# sock.connect(((allTello[2]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g bbbbbbbbb0000000b0000000b0000000b0000000b000bbbbb0000b0bbbbbbb0b".encode())
# time.sleep(0.8)
# #G
# sock.connect(((allTello[3]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g bbbbbbbbb0000000b0000000b0000000b0000000b000bbbbb0000b0bbbbbbb0b".encode())
# time.sleep(0.8)
# #E
# sock.connect(((allTello[4]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g bbbbbbbbbbbbbbbbb0000000bbbbbbb0bbbbbbb0b0000000bbbbbbbbbbbbbbbb".encode())
# time.sleep(0.8)
# #R
# sock.connect(((allTello[5]), UDP_PORT))
# sock.send("EXT led 0 0 255".encode())
# sock.send("EXT mled g bbbbbbb0b000000bb000000bbbbbbbb0b000b000b0000b00b00000b0b000000b".encode())
# time.sleep(2)

# # # [
#     bbbbbbb0
#     b000000b
#     b000000b
#     bbbbbbb0
#     b000b000
#     b0000b00
#     b00000b0
#     b000000b
# # # ]
swarm.takeoff()


swarm.set_speed(100)
# swarm.move_up(80)
swarm.move_forward(90)
swarm.enable_mission_pads()
# swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 150, 40, i + 1))

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    sock.send("EXT led 0 255 0".encode())




#part1
# for b in range(2):
drone[0].move_up(50)
for a in range(5):
    move = TelloSwarm.fromIps([
        allTello[a+1],
        allTello[a]
    ])
    move.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, i % 2 * -100 + 50, 100))
# drone[0].move_down(50)

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    sock.send("EXT led 0 255 0".encode())

for a in range(5):
    move = TelloSwarm.fromIps([
        allTelloR[a+1],
        allTelloR[a]
    ])
    move.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, i % 2 * -100 + 50, 100))
drone[0].move_down(50)


#part2
for i in range(28):
    if i < 13:
        ran = round((random.random() * 10) / 10 * 5)
        sock.connect((allTello[ran], UDP_PORT))
        sock.send("EXT led 0 255 0".encode())
        time.sleep(0.2)
        sock.send("EXT led 0 0 0".encode())
    elif i == 13:
        for a in range(6):
            sock.connect((allTello[a], UDP_PORT))
            sock.send("EXT led 0 0 0".encode())
            sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
    else:
        ran = round((random.random() * 10) / 10 * 5)
        sock.connect((allTello[ran], UDP_PORT))
        sock.send("EXT led 255 255 0".encode())
        time.sleep(0.2)
        sock.send("EXT led 0 0 0".encode())

for i in range(6):
    sock.connect((allTello[5-i], UDP_PORT))
    sock.send("EXT led 255 255 0".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
    time.sleep(0.1)


dout = TelloSwarm.fromIps([
    tello2,
    tello6
])

dmid = TelloSwarm.fromIps([
    tello3,
    tello4,
    tello5
])
df = TelloSwarm.fromIps([
    tello2,
    tello1
])


dout.parallel(lambda i, tello: tello.go_xyz_speed(i%2 * - 200 + 100, 0, 0, 100))
drone[0].move_forward(190)
dmid.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, 20, 100)) #t3,4,5 20
dout.parallel(lambda i, tello: tello.go_xyz_speed(0, i % 2 * - 360 + 180, 0, 100))
swarm.move_up(40) #t3,4,5 50, #t1,2,6 30
drone[0].go_xyz_speed(0, 270, 0, 100)
dmid.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, 20, 100)) #t3,4,5 70
drone[5].move_up(100) #t6 100
df.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, i * - 50 - 30, 100)) #t1 -50, t2 0
#t1 -50 t2 0 t3 70 t4 70 t5 70 t6 100

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    sock.send("EXT led 255 255 0".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
time.sleep(4)

for a in range(3):
    for i in range(6):
        sock.connect((allTello[i], UDP_PORT))
        sock.send("EXT led 255 255 0".encode())
        sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
    time.sleep(1)
    for i in range(6):
        sock.connect((allTello[i], UDP_PORT))
        sock.send("EXT led 0 0 0".encode())
        sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())
    time.sleep(0.5)

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    sock.send("EXT led 255 255 0".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())

#part3
db = TelloSwarm.fromIps([
    tello3,
    tello5
])

dbfull = TelloSwarm.fromIps([
    tello3,
    tello5,
    tello6
])
dmidfull = TelloSwarm.fromIps([
    tello2,
    tello4
])
db.move_back(100)
drone[3].go_xyz_speed(0, -100, 0, 100)
drone[5].move_down(60)
drone[1].go_xyz_speed(-100, 100, 0, 100)
drone[0].move_back(100)
db.parallel(lambda i, tello: tello.go_xyz_speed(0, i%2 * 200 - 100, 0, 100))
drone[1].move_up(60)
dmidfull.move_down(20)
dbfull.move_up(30)
drone[0].move_up(20)

lineup = [
    tello1,
    tello2,
    tello5,
    tello6,
    tello3,
    tello4
]

for a in range(3):
    for i in range(6):
        if i == 0:
            sock.connect((lineup[i], UDP_PORT))
            sock.send("EXT led 0 0 0".encode())
            sock.connect((lineup[5], UDP_PORT))
            sock.send("EXT led 255 225 0".encode())
            time.sleep(0.2)
        else:
            sock.connect((lineup[i], UDP_PORT))
            sock.send("EXT led 0 0 0".encode())
            sock.connect((lineup[i-1], UDP_PORT))
            sock.send("EXT led 255 225 0".encode())
            time.sleep(0.2)

for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    sock.send("EXT led 255 255 0".encode())

time.sleep(1)
for i in range(6):
    sock.connect((allTello[i], UDP_PORT))
    sock.send("EXT led 0 0 0".encode())
time.sleep(3)


for i in range(6):
    print(i)
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    sock.send("EXT led 255 0 0".encode())
    sock.send("EXT mled g rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr".encode())

time.sleep(3)
for a in range(3):
    for i in range(6):
        print(i)
        sock.connect((allTello[i], UDP_PORT))
        sock.send("EXT led 0 0 0".encode())
    time.sleep(1)
    for i in range(6):
        print(i)
        sock.connect((allTello[i], UDP_PORT))
        sock.send("EXT led 255 0 0".encode())
    time.sleep(1)

time.sleep(5)

for i in range(6):
    print(i)
    sock.connect((allTello[i], UDP_PORT))
    # sock.send("battery?".encode())
    sock.send("EXT led 0 0 0".encode())
    sock.send("EXT mled g 0000000000000000000000000000000000000000000000000000000000000000".encode())


swarm.land()
swarm.end()


#
#
# # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
# # time.sleep(1)
# # drone[0].move_up(60)
# # time.sleep(0.5)
# # drone[1].move_up(60)
# # time.sleep(1)
# # drone[2].move_up(60)
# # time.sleep(1)
# #
# # time.sleep(2)
# # swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 120, 40, i+1))
# # swarm.move_up(30)
# # swarm.move_forward(155)
# #
# # tello = [tello1,tello2, tello3]
# # b=0
# # h = -1
# # for a in range(3):
# #     sock.connect((tello[b], UDP_PORT))
# #     sock.send("tof?".encode())
# #     data = int(sock.recv(1024)[:-4])/10
# #     print(data)
# #     if data <= 100:
# #         h = b
# #     b = b + 1
# #     time.sleep(1)
# # if h == -1:
# #     pass
# # else:
# #     sock.connect((tello[h], UDP_PORT))
# #     sock.send("EXT led 255 0 0".encode())
# #
# # swarm.move_back(145)
# # time.sleep(1)
# #
# # swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
# # # part 2
# # time.sleep(1)
# # drone[2].move_down(40)
# # drone[0].move_up(80)
# # drone[1].move_up(140)
# #
# # time.sleep(4)
# # swarm.parallel(lambda i, tello: tello.go_xyz_speed(20, i * 195 - 195, 0, 100))
# # drone[2].move_up(100)
# # drone[1].move_down(90)
# # swarm.move_down(40)
# # time.sleep(2)
# #
# # swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
# # swarm.move_forward(100)
# #
# # if h == 0:
# #     swarm2 = TelloSwarm.fromIps([
# #         tello2,
# #         tello3
# #     ])
# # elif h == 1:
# #     swarm2 = TelloSwarm.fromIps([
# #         tello1,
# #         tello3
# #     ])
# # elif h == 2:
# #     swarm2 = TelloSwarm.fromIps([
# #         tello1,
# #         tello2
# #     ])
# # time.sleep(1)
# # if h == -1:
# #     swarm.flip_forward()
# # else:
# #     drone[h].flip_forward()
# #     swarm2.flip_forward()
# #
# #
# # time.sleep(1)
# # swarm.move_back(110)
# # swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
# # swarm.move_down(30)
# # swarm.move_forward(110)
# #
# # b=0
# # h = -1
# # for a in range(3):
# #     sock.connect((tello[b], UDP_PORT))
# #     sock.send("tof?".encode())
# #     data = int(sock.recv(1024)[:-4])/10
# #     print(data)
# #     if data <= 100:
# #         h = b
# #     b = b + 1
# #     time.sleep(1)
# # if h == -1:
# #     pass
# # else:
# #     sock.connect((tello[h], UDP_PORT))
# #     sock.send("EXT led 255 0 0".encode())
# #
# # if h == 0:
# #     swarm3 = TelloSwarm.fromIps([
# #         tello2,
# #         tello3
# #     ])
# # elif h == 1:
# #     swarm3 = TelloSwarm.fromIps([
# #         tello1,
# #         tello3
# #     ])
# # elif h == 2:
# #     swarm3 = TelloSwarm.fromIps([
# #         tello1,
# #         tello2
# #     ])
# #
# # swarm3.move_back(110)
#

