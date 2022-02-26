import math
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
from time import time
from os import cpu_count


def integrate(f, a, b, *args, n_jobs=1, n_iter=1000, executor=None, callback=None):
	"""
	Numerically calculates integral.
	:param f: a funtion which integral will be found
	:param a: left borger of the integration
	:param b: right border of the integration
	:param n_iter: number of segments for calculating 
	:param executor: executor for parallel execution. If None then integral will be calculated sequentially
	:param n_jobs: number of jobs to send in the executor
	:param callback: a function that will be called before every job with (f, a, b) arguments
	:returns: result of the integration
	"""

	acc = 0
	step = (b - a) / n_iter

	if executor is None:
		if callback is not None:
			callback(f, a, b, *args)
		for i in range(n_iter):
			acc += f(a + i * step) * step
	else:
		futures = []
		batch = int(n_iter / n_jobs)

		for i in range(0, n_iter, batch):
			c = a + i * step
			d = min(b, c + batch * step)
			mini_iters = max(int((d - c) / step), 1)

			future = executor.submit(
				integrate,
				*((f, c, d) + args),
				**{'n_iter': mini_iters, 'callback': callback}
			)
			futures.append(future)
		
		for f in futures:
			acc += f.result()

	return acc


def test_int_threads(n_jobs, logs: str) -> float:
	"""
	Integrates numerically cos(x) in [0, PI / 2] using thread pool.
	:param n_jobs: number of jobs to send in a pool
	:param logs: path to a file where logs will be written
	:returns: intergal execution time
	"""

	out = open(logs, 'w')
	tic = time()

	def callback(f, a, b):
		out.write(f"A job calculating integral of {f.__name__} in [{a:.3f}, {b:.3f}] started in {time() - tic:.6f}s\n")

	integrate(
		math.cos, 0, math.pi / 2,
		n_jobs=n_jobs,
		executor=ThreadPoolExecutor(max_workers=cpu_count()),
		callback=callback
	)

	toc = time()
	out.close()

	return toc - tic


def proc_callback(f, a, b, queue):
	queue.put((f.__name__, a, b, time()))


def test_int_procs(n_jobs, logs: str) -> float:
	"""
	Integrates numerically cos(x) in [0, PI / 2] using process pool.
	:param n_jobs: number of jobs to send in a pool
	:param logs: path to a file where logs will be written
	:returns: intergal execution time
	"""

	queue = Manager().Queue()
	tic = time()

	integrate(
		math.cos, 0, math.pi / 2,
		queue,
		n_jobs=n_jobs,
		executor=ProcessPoolExecutor(max_workers=cpu_count()),
		callback=proc_callback
	)

	toc = time()

	with open(logs, 'w') as out:
		while True:
			try:
				f, a, b, t = queue.get(block=False)
				out.write(f"A job calculating integral of {f} in [{a:.3f}, {b:.3f}] started in {t - tic:.6f}s\n")
			except Exception:
				break

	return toc - tic
