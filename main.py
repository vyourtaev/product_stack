#!/bin/python3 -w

import time
import json
import asyncio
from importlib import import_module, reload
import bTree


async def task(name, work_queue):
    '''
    Parsing log events and tasks creation
    '''

    module = import_module('operations')
    reload(module)

    while not work_queue.empty():
        event = json.loads(await work_queue.get())
        item = event.get('type')
        try:
            ops = getattr(module, item)(*list(event.values()))
            ops.run()
        except (ImportError, AttributeError, TypeError) as e:
            print(e)


async def main():
    '''
    Creation and Population async queue
    '''

    work_queue = asyncio.Queue()
    offset = 0

    while True:

        infile = open("input.json", "r")
        infile.seek(offset)

        for line in infile:
            await work_queue.put(line)

        offset = infile.tell()
        infile.close()
        time.sleep(1)

        # Run async consumers
        await asyncio.gather(
                asyncio.create_task(task("One", work_queue)),
                asyncio.create_task(task("Two", work_queue)),
            )


if __name__ == "__main__":
    asyncio.run(main())
    

