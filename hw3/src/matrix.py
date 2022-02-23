from typing import Union


class Matrix:
	"""
	A math object that represents rectangular array of numbers.
	"""

	def __init__(self, array):
		"""
		:param array: a 2D iterable object
		:raises ValueError: if lenght of rows is different or object is not 2D iterable
		"""

		self.value = []
		try:
			for row in array:
				self.value.append([])
				for num in row:
					self.value[-1].append(num)
		except TypeError:
			raise ValueError("Matrix can be created only from a 2D iterable object with numbers. " \
			                 "Got non 2D object.")

		self.__n_rows = len(self.value)
		self.__n_cols = len(self.value[0])
		for row in self.value:
			if len(row) != self.__n_cols:
				raise ValueError("Matrix can be created only from a 2D iterable object with numbers. " \
				                 "Got object with diferent lenght of rows.")

	def __getitem__(self, index):
		"""
		Get the matrix coordinate value.
		:param index: a position of a coordinate
		:returns: a coordinate of the matrix
		:raises IndexError: if the index out of range
		:raices TypeError: if type of the index is incorrect
		"""

		try:
			if type(index) == tuple:
				if len(index) == 2:
					return self.value[index[0]][index[1]]
			else:
				return self.value[index]
		except TypeError:
			raise TypeError("matrix indices must be integers or slices, not " + type(index))
		except IndexError:
			raise IndexError("matrix index is out of range")
		raise IndexError("too many indices for a 2D matrix")

	def __add__(self, other: 'Matrix') -> 'Matrix':
		"""
		Calculates sum of matrices.
		:param other: a Matrix object to sum with
		:returns: a result of the operation as a new Matrix object
		:raises ValueError: if shapes of matrices are different
		"""

		if self.__n_rows != other.__n_rows or \
		   self.__n_cols != other.__n_cols:
			raise ValueError("matrices have different shapes.")

		k, n = self.__n_rows, self.__n_cols
		return Matrix(((self[i, j] + other[i, j] for j in range(n)) for i in range(k)))

	def __mul__(self, other: 'Matrix') -> 'Matrix':
		"""
		Calculates Hadamard product of matrices.
		:param other: a Matrix object to sum with
		:returns: a result of the operation as a new Matrix object
		:raises ValueError: if shapes of matrices are different
		"""

		if self.__n_rows != other.__n_rows or \
		   self.__n_cols != other.__n_cols:
			raise ValueError("matrices have different shapes.")

		k, n = self.__n_rows, self.__n_cols
		return Matrix(((self[i, j] * other[i, j] for j in range(n)) for i in range(k)))

	def __matmul__(self, other: 'Matrix') -> 'Matrix':
		"""
		Calculates product of matrices.
		:param other: a Matrix object to sum with
		:returns: a result of the operation as a new Matrix object
		:raises ValueError: if shapes of matrices are inconsistent
		"""

		if self.__n_cols != other.__n_rows:
			raise ValueError("matrices have incosistent shapes")

		k, n, m = self.__n_rows, self.__n_cols, other.__n_cols
		return Matrix(((sum(self[i, c] * other[c, j] for c in range(n)) for j in range(m)) for i in range(k)))

	def __str__(self) -> str:
		return '\n'.join(['\t'.join(map(str, row)) for row in self.value])
