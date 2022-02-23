import numpy as np
from src.matrix import Matrix
from src.matrix_mixined import MatrixMixined
from src.matrix_hash import MatrixWithHash


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


def hard():
	np.random.seed(0)
	A = MatrixWithHash(np.identity(10))
	C = MatrixWithHash(np.identity(10)[::-1])
	B = MatrixWithHash(np.random.randint(0, 10, (10, 10)))
	D = B

	AB = A @ B
	CD = C @ D

	with open('artifacts/hard/A.txt', 'w') as out:
		out.write(str(A))
	with open('artifacts/hard/B.txt', 'w') as out:
		out.write(str(B))
	with open('artifacts/hard/C.txt', 'w') as out:
		out.write(str(C))
	with open('artifacts/hard/D.txt', 'w') as out:
		out.write(str(D))
	with open('artifacts/hard/AB.txt', 'w') as out:
		out.write(str(AB))
	with open('artifacts/hard/CD.txt', 'w') as out:
		out.write(str(CD))
	with open('artifacts/hard/hash.txt', 'w') as out:
		h = hash(AB)
		out.write(str(h))
		assert h == hash(CD)


if __name__ == '__main__':
	easy()
	medium()
	hard()
