import asyncio
import aiohttp
import heapq
import os


async def download(n_pics: int, url: str, save_dir: str):
    """
    Downloads asyncronously images from an url.
    :param n_pics: number of different pictures to download
    :param url: get query to download picture
    :param save_dir: path to downloads
    """

    async with aiohttp.ClientSession() as session:
        pics = []

        while n_pics > 0:
            pics += await asyncio.gather(*(
                get_photo(session, url) for _ in range(n_pics)
            ))

            n_old = len(pics)
            pics = remove_duplicates(pics)
            if len(pics) == n_old:
                break
            else:
                n_pics = n_old - len(pics)

        save_photos(pics, save_dir)


async def get_photo(session: aiohttp.ClientSession, url: str) -> bytes:
    """
    Sends get query to download a picture.
    :param session: a client session from an aiohttp library
    :param path: get query to download picture
    :returns: picture as bytes
    """

    responce = await session.get(url)
    photo_bytes = await responce.read()

    return photo_bytes


def remove_duplicates(objects: list) -> list:
    """
    Removes duplicates from list by hash.
    :param objects: list contaning hashable objects
    :returns: list without duplicates
    """

    hashes = []
    result = []

    for obj in objects:
        h = hash(obj)
        if h in hashes:
            continue
        else:
            heapq.heappush(hashes, h)
            result.append(obj)

    return result


def save_photos(pics: list, dir: str):
    """
    Saves images in .jpg format.
    :param pics: list with bytes as images
    :param dir: path to save folder
    """

    if not os.path.exists(dir):
        os.mkdir(dir)

    for i, pic in enumerate(pics):
        with open(f'{dir}/{i}.jpg', 'wb') as file:
            file.write(pic)
