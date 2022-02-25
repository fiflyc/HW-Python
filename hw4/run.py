from src.thread_proc_test import (
	test_seq,
	test_threads,
	test_proc
)


def easy():
	n = 600000
	c = 10

	with open('artifacts/time_easy.txt', 'w') as out:
		out.write(f'Sequential:      {test_seq(n, c):.4f}s\n')
		out.write(f'Multithreading:  {test_threads(n, c):.4f}s\n')
		out.write(f'Multiprocessing: {test_proc(n, c):.4f}s\n')


if __name__ == '__main__':
	easy()
