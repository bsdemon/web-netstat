import socket
import struct

TCP = "/proc/net/tcp"
STATE = {
        '01': 'ESTABLISHED',
        '02': 'SYN_SENT',
        '03': 'SYN_RECV',
        '04': 'FIN_WAIT1',
        '05': 'FIN_WAIT2',
        '06': 'TIME_WAIT',
        '07': 'CLOSE',
        '08': 'CLOSE_WAIT',
        '09': 'LAST_ACK',
        '0A': 'LISTEN',
        '0B': 'CLOSING'
        }


def _get_tcp():
    with open(TCP,'r') as t:
        conn = t.readlines()
        conn.pop(0)
    return conn


def _ip(iphex):
    ipint = int(iphex,16)
    ip = socket.inet_ntoa(struct.pack("<L", ipint))
    return ip


def tcp_stat():
    result = []
    connections = _get_tcp()
    for conn in connections:
        connection = conn.split(' ')
        connection = list(filter(None, connection))
        ip_port_hex = connection[1].split(':')
        iphex, porthex = ip_port_hex
        ip = _ip(iphex)
        port = int(porthex, 16)
        print(str(ip) + ':' + str(port))

tcp_stat()
