"""
generate_pi code based off Classic Computer Science Problems in Python's Section 1.4
* https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/calculating_pi.py

async generator docs: 
* https://www.python.org/dev/peps/pep-0525/
* Check out the example near the end of the page

async Websocket in Python:
* https://websockets.readthedocs.io/en/stable/intro.html#browser-based-example
"""

import asyncio
import websockets
import json

# Leibniz formula for pi with an async generator
async def generate_pi():
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    i: int = 0 # index corresponds to number of items in the series
    while True: 
        pi += operation * (numerator / denominator)
        yield i, pi 
        await asyncio.sleep(0) # blocks to free event loop
        denominator += 2.0
        operation *= -1.0
        i += 1

async def pi_websocket(websocket, path):
    # generates 'better' pi calulation on the fly
    async for (i, pi) in generate_pi():
        # for every new calculation, send a websocket messsage
        await websocket.send(json.dumps({'i': i, 'pi': pi}))
        print(i, pi) 
        await asyncio.sleep(0.2) # acts as the brakes


if __name__ == "__main__":
    ws_server = websockets.serve(pi_websocket, "127.0.0.1", 5678)

    asyncio.get_event_loop().run_until_complete(ws_server)
    asyncio.get_event_loop().run_forever()