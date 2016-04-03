import socket
import struct
import time
import os

tcp = "/proc/net/tcp"

state_status = ['ESTABLISHED', 'SYN_SENT', 'SYN_RECV', 'FIN_WAIT1', 'FIN_WAIT2', 'TIME_WAIT',
                'CLOSE', 'CLOSE_WAIT', 'LAST_ACK', 'LISTEN', 'CLOSING']


def _get_tcp():
    with open(tcp, 'r') as t:
        conn = t.readlines()
        conn.pop(0)
    return conn


def _ip(iphex):
    ipint = int(iphex, 16)
    ip = socket.inet_ntoa(struct.pack("<L", ipint))
    return ip


def _ip_port(connection):
    ip_port_hex = connection.split(':')
    iphex, porthex = ip_port_hex
    ip = _ip(iphex)
    port = int(porthex, 16)
    ip_port = str(ip) + ':' + str(port)
    return ip_port


def tcp_stat():
    result = []
    connections = _get_tcp()
    # print('{0:21}| {1:21} | {2:14}| {3}'.format('LOCAL_ADDR:PORT', 'REMOTE_ADDR:PORT', 'STATE', 'TX queue| RX queue'))
    for conn in connections:
        connection = conn.split(' ')
        connection = list(filter(None, connection))
        if '0100007F' in connection[1] or '00000000' in connection[1] or '0101007F' in connection[1]:
            continue
        local = _ip_port(connection[1])
        remote = _ip_port(connection[2])
        state = state_status[int(connection[3]) - 1]
        queue = connection[4].split(':')
        tx_queue = queue[0]
        rx_queue = queue[1]
        # print('{0:21}| {1:21} | {2:14}| {3}| {4}'.format(local, remote, state, tx_queue, rx_queue, connection[5]))
        formated_conn = local+' <=== '+remote+' |----| '+state+' | '+tx_queue+' | '+rx_queue
        result.append((formated_conn))
    return result


### print in console ###

# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     netstat = tcp_stat()
#     for stat in netstat:
#         print(stat)
#     time.sleep(10)


