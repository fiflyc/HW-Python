import numpy as np
from src.matrix import Matrix
from src.matrix_mixined import MatrixMixined


def easy():
	np.random.seed(0)
	A = Matrix(np.random.randint(0, 10, (10, 10)))
	B = Matrix(np.random.randint(0, 10, (10, 10)))

	with open('artifacts/easy/matrix+.txt', 'w') as out:
		out.write(str(A + B))
	with open('artifacts/easy/matrix*.txt', 'w') as out:
		out.write(str(A * B))
	with open('artifacts/easy/matrix@.txt', 'w') as out:
		out.write(str(A @ B))


def medium():
	np.random.seed(0)
	A = MatrixMixined(np.random.randint(0, 10, (10, 10)))
	B = MatrixMixined(np.random.randint(0, 10, (10, 10)))

	(A + B).write('artifacts/medium/matrix+.txt')
	(A * B).write('artifacts/medium/matrix*.txt')
	(A @ B).write('artifacts/medium/matrix@.txt')


if __name__ == '__main__':
	easy()
	medium()
