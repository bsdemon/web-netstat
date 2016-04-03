import asyncio
import datetime
import random
import websockets
from tcp import tcp_stat

@asyncio.coroutine
def time(websocket, path):
    while True:
        netstat = tcp_stat()
        for stat in netstat:
            yield from websocket.send(stat)
        yield from asyncio.sleep(1)
        yield from websocket.send('end')

start_server = websockets.serve(time, '127.0.0.1', 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()