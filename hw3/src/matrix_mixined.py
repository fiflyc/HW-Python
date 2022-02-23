import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
import src.mixins as ms
from src.matrix import Matrix


class MatrixMixined(NDArrayOperatorsMixin,
                    ms.PrettyInfoMixin,
                    ms.WriteToFileMixin,
                    ms.GettersMixin,
                    ms.SettersMixin):
	"""
	A math objects that represents rectangular array of numbers.
	"""

	def __init__(self, array):
		"""
		:param array: a 2D iterable object
		:raises ValueError: if lenght of rows is different or object is not 2D iterable
		"""

		self.value = np.array(array)
		super().__init__()

	def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
		out = kwargs.get('out', ())
		for x in inputs + out:
			if not isinstance(x, MatrixMixined):
				return NotImplemented

		inputs = tuple(x.value if isinstance(x, MatrixMixined) else x for x in inputs)
		if out:
			kwargs['out'] = tuple(
				x.value if isinstance(x, MatrixMixined) else x for x in out)
		result = getattr(ufunc, method)(*inputs, **kwargs)

		if type(result) is tuple:
			return tuple(type(self)(x) for x in result)
		elif method == 'at':
			return None
		else:
			return type(self)(result)
