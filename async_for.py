import asyncio
import time


async def func(arg_1_1):
    for i in range(arg_1_1):
        yield i
        await asyncio.sleep(1)


async def run(arg_1_2):
    async for i in func(arg_1_2 + 1):
        print(i)
        print('asyncio.sleep(1)')


async def main():
    star_time = time.time()
    await asyncio.gather(run(4), run(2))
    finish_time = time.time()
    release_time = finish_time - star_time
    print(release_time)


if __name__ == '__main__':
    asyncio.run(main())




