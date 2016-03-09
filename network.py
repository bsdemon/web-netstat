import os
import time
import psutil


"""
psutil.net_connections()
fd: the socket file descriptor
family: the address family, either AF_INET, AF_INET6 or AF_UNIX.
type: the address type, either SOCK_STREAM = tcp or SOCK_DGRAM = udp.
laddr: the local address as a (ip, port)
raddr: the remote address as a (ip, port)
status: represents the status of a TCP connection.  For UDP and UNIX is NONE.
pid: the PID of the process which opened the socket, if retrievable, else None. (root is needed).
"""


def netstat():
    conlist = psutil.net_connections()
    for con in conlist:
        if con[3][0] == '0.0.0.0' or len(con[3][0]) < 5 or con[3][0][:3] == '127':
            continue
        packet_type = "TCP"
        if con[2] == 2:
            packet_type = "UDP"
        process = psutil.Process(con[6])
        print('Type {0} : Local address {1!s:25s} : Remote address {2!s:25s} : Status {3!s:12s} : {4!s:20s}'.
              format(packet_type, con[3][0], con[4], con[5], process.name() ))


while True:
    netstat()
    time.sleep(1)
    os.system('clear')