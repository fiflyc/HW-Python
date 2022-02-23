import numpy as np
from src.matrix import Matrix


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


if __name__ == '__main__':
	easy()
