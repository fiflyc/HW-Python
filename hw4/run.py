import sys
from os import cpu_count
from src.thread_proc_test import (
	test_seq,
	test_threads,
	test_proc
)
from src.integrate import test_int_threads, test_int_procs


def easy():
	n = 200000
	c = 10

	with open('artifacts/time_easy.txt', 'w') as out:
		out.write(f'Sequential:      {test_seq(n, c):.4f}s\n')
		out.write(f'Multithreading:  {test_threads(n, c):.4f}s\n')
		out.write(f'Multiprocessing: {test_proc(n, c):.4f}s\n')


def medium():
	with open('artifacts/time_medium.txt', 'w') as out:
		for n_jobs in range(1, cpu_count() * 2):
			time_t = test_int_threads(n_jobs, 'artifacts/logs_threads_medium.txt')
			time_p = test_int_procs(n_jobs, 'artifacts/logs_procs_medium.txt')
			out.write(f'ThreadPoolExecutor  (jobs={n_jobs}):\t{time_t:.6f}s\n')
			out.write(f'ProcessPoolExecutor (jobs={n_jobs}):\t{time_p:.6f}s\n')


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 run.py [PART]\nwhere PART = easy | medium | hard")
	elif sys.argv[1] == 'easy':
		easy()
	elif sys.argv[1] == 'medium':
		medium()
	elif sys.argv[1] == 'hard':
		pass
	else:
		print("Usage: python3 run.py [PART]\nwhere PART = easy | medium | hard")
