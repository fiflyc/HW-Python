from multiprocessing import Process, Queue, Pipe
from threading import Thread
from time import sleep, time
from codecs import encode


def modify_and_send(queue, conn_b):
	try:
		while True:
			string = queue.get()
			sleep(5)
			conn_b.send(string.lower())
	except EOFError:
		return


def a_routine(main_conn, conn_b):
	queue = Queue()
	sender = Thread(target=modify_and_send, args=(queue, conn_b))
	sender.start()

	try:
		while True:
			string = main_conn.recv()
			queue.put(string)
	except KeyboardInterrupt:
		return
	except EOFError:
		return


def b_routine(a_conn, conn_main):
	try:
		while True:
			string = a_conn.recv()
			conn_main.send(encode(string, 'rot_13'))
	except KeyboardInterrupt:
		return
	except EOFError:
		return


def receive_and_print(b_conn, start, out):
	try:
		while True:
			string = b_conn.recv()
			print(string)
			out.write(f'({time() - start:.2f}s)\tApp output: {string}\n')
	except EOFError:
		return


def kill_all(*args):
	for p in args:
		if p is not None:
			p.kill()
			p.join()
			p.close()


def run(logs: str):
	A, B = None, None
	start = time()

	try:
		out_a, conn_a = Pipe()
		ab_conn, conn_ab = Pipe()
		b_conn, in_b = Pipe()

		A = Process(target=a_routine, args=(out_a, conn_ab))
		B = Process(target=b_routine, args=(ab_conn, in_b))
		A.start()
		B.start()

		with open(logs, 'w') as out:
			receiver = Thread(target=receive_and_print, args=(b_conn, start, out))
			receiver.start()

			while True:
				string = input()
				out.write(f'({time() - start:.2f}s)\tUser input: {string}\n')
				conn_a.send(string)
	except KeyboardInterrupt:
		print('')
		kill_all(A, B)
		return
	except EOFError:
		kill_all(A, B)
		return
