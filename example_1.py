import time
import asyncio


async def async_func():
    print(1)
    await asyncio.sleep(1)
    print(2)


async def main():
    star_time = time.time()
    await asyncio.gather(async_func(), async_func(), async_func(), async_func(), async_func(),
                         async_func(), async_func(), async_func(), async_func(), async_func(),)
    finish_time = time.time()
    release_time = finish_time - star_time
    print(release_time)


if __name__ == '__main__':
    asyncio.run(main())












