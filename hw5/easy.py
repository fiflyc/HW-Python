import sys
import asyncio
from src.pics import download


def main(n_pics, save_dir):
	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(download(
			n_pics,
			'https://picsum.photos/512',
			save_dir
		))
	finally:
		loop.close()


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("Usage: python3 easy.py [N_PICS] [FOLDER]\nwhere\n" + \
			  "\tN_PICS is a number of pictures to download\n" + \
			  "\tFOLDER is a path where pictures will be stored")
	else:
		try:
			main(int(sys.argv[1]), sys.argv[2])
		except ValueError:
			print("A number of pictures should be passed in the first argument")
