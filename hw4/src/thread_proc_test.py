from threading import Thread
from multiprocessing import Process
from time import time


def fib(n: int) -> int:
	"""
	Returns n'th Fibonacci number.
	"""

	if n == 0:
		return 0 
	elif n in [1, -1]:
		return 1
	elif n > 1:
		a, b = 1, 1
		for i in range(2, n):
			a, b = b, a + b 
		return b
	else:
		a, b = -1, 1
		for i in range(2, -n):
			a, b = b - a, a
		return a


def test_seq(n: int, c: int) -> float:
	"""
	Sequentialy calculates Fibonacci numbers several times and returns execution time.
	:param n: Fibonacci number to calculate
	:param c: number of iterations
	:returns: execution time in seconds
	"""

	tic = time()
	for _ in range(c):
		fib(n)
	toc = time()

	return toc - tic


def test_threads(n: int, c: int) -> float:
	"""
	Calculates Fibonacci numbers several times using multithreading and returns execution time.
	:param n: Fibonacci number to calculate
	:param c: number of iterations
	:param n_threads: number of threads to use
	:returns: execution time in seconds
	"""

	tic = time()
	threads = []
	for _ in range(c):
		threads.append(Thread(target=fib, args=(n, )))
		threads[-1].start()
	for t in threads:
		t.join()
	toc = time()

	return toc - tic


def test_proc(n: int, c: int) -> float:
	"""
	Calculates Fibonacci numbers several times using multiprocessing and returns execution time.
	:param n: Fibonacci number to calculate
	:param c: number of iterations
	:param n_proc: number of processes to use
	:returns: execution time in seconds
	"""

	tic = time()
	procs = []
	for _ in range(c):
		procs.append(Process(target=fib, args=(n, )))
		procs[-1].start()
	for p in procs:
		p.join()
	toc = time()

	return toc - tic
