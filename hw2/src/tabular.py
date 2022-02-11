import sys
import csv
from typing import Optional
from operator import add
from itertools import repeat
from collections.abc import Iterator


def gen_tex(csv_file: str, out_file: str):
	"""
	Generates a .tex file with a table from an input.
	:param csv_file: a path to a csv file with the table
	:param out_file: a path to the output file
	"""
	n_cols = check_csv(csv_file)
	if n_cols is None:
		print("Invalid CSV file: number of columns in each row should be the same")
		return

	with open(csv_file, newline='') as input_file:
		table = csv.reader(input_file)
		result = ''.join([
			settings(),
			'\n\\begin{document}\n\n',
			gen_table(table, n_cols),
			'\n\\end{document}\n'
		])
	
	with open(out_file, 'w') as output:
		output.write(result)


def check_csv(csv_file: str) -> Optional[int] :
	"""
	Checks a csv file for the fact that number of columns is the same for each row.
	:param csv_file: a path to a csv file with the table
	:returns: number of columns if this value is the same for each row, None otherwise 
	"""

	with open(csv_file, newline='') as input_file:
		table = csv.reader(input_file)
		n_cols = map(lambda row: len(row), table)
		
		result = next(n_cols)
		unmatched = filter(lambda n: n != result, n_cols)
		try:
			next(unmatched)
		except StopIteration:
			return result
		return None


def settings() -> str:
	"""
	Returns a string with latex settings for the generating file.
	"""

	return ("\\documentclass[a4paper]{report}\n"
	        "\\usepackage[12pt]{extsizes}\n"
	        "\\usepackage[russian]{babel}\n"
	        "\\usepackage[utf8]{inputenc}\n")


def gen_table(table: Iterator, n_cols: int) -> str:
	"""
	Builds a string with a latex code that imports a table.
	:param table: an iterator iterating over lists of strings
	:param n_cols: number of columns in the table. If you pass a wrong number, the result will be an invalid latex code
	:returns: a string with the latex code
	"""

	begin = ("\\begin{center}\n"
	         "\\begin{tabular}{|" + '|'.join(repeat('c', n_cols)) + "|}\n"
	         "\\hline\n")
	end = ("\\end{tabular}\n"
	       "\\end{center}\n")

	body = map(lambda row: ' & '.join(row) + ' \\\\\n\\hline\n', table)

	return begin + ''.join(body) + end


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 tabular.py [CSV FILE]")
	else:
		gen_tex(sys.argv[1], 'artifacts/out_easy.tex')
