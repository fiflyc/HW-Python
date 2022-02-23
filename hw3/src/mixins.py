class WriteToFileMixin:
	def write(self, file: str):
		"""
		Prints value of the object in the file.
		:param file: path to the file as a string
		"""

		with open(file, 'w') as out:
			out.write(self.__str__())


class PrettyInfoMixin:
	def __str__(self) -> str:
		def to_str(object, newline='\n'):
			return str(object).replace('\n', newline)
		def space(n):
			return ''.join([' ' for _ in range(n)])


		return type(self).__name__ + ':\n' + \
		       ''.join(map(lambda p: f'\t{p[0]}: {p[1]}\n',
		       	           map(lambda k: (k, to_str(self.__dict__[k],
		       	                                    '\n\t' + space(len(k) + 2))),
		       	           	   self.__dict__)))


class GettersMixin:
	def __init__(self, *args):
		for field in self.__dict__:
			setattr(self.__class__, f'get_{field}', lambda s: s.__dict__[field])


class SettersMixin:
	def __init__(self, *args):
		def set(s, field, value):
			s.__dict__[field] = value

		for field in self.__dict__:
			setattr(self.__class__, f'set_{field}', lambda s, v: set(s, field, v))
