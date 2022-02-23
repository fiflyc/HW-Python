from src.matrix import Matrix


class MatrixHashMixin:
	def __hash__(self) -> int:
		"""
		Calculates hash of a matrix - sum of its coordinates.
		If the sum is -1, returns -2
		:returns: hash
		"""

		return hash(sum([sum(row) for row in self.value]))


class MatrixWithHash(Matrix, MatrixHashMixin):
	_cached = {}

	def __matmul__(self, other):
		"""
		Calculates product of matrices.
		:param other: a Matrix object to sum with
		:returns: a result of the operation as a new Matrix object
		:raises ValueError: if shapes of matrices are inconsistent
		"""

		if len(self.value[0]) != len(other.value):
			raise ValueError("matrices have incosistent shapes")

		if MatrixWithHash._cached.get((hash(self), hash(other))) is not None:
			return MatrixWithHash._cached.get((hash(self), hash(other)))

		k, n, m = len(self.value), len(self.value[0]), len(other.value[0])
		result = Matrix(((sum(self[i, c] * other[c, j] for c in range(n)) for j in range(m)) for i in range(k)))
		MatrixWithHash._cached[(hash(self), hash(other))] = result
		return result
