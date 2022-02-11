import sys
import csv
from avatargen.generation import generate as gen_img
from tabular import check_csv, gen_table


def gen_tex(csv_file: str, img: str, out_file: str):
	"""
	Generates a .tex file with a table and an image from an input.
	:param csv_file: a path to a csv file with the table
	:param img: a path to an image
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
			'\n\\begin{center}\n'
			f'\\includegraphics[scale=0.5]{{{img}}}\n',
			'\\end{center}\n'
			'\n\\end{document}\n'
		])
	
	with open(out_file, 'w') as output:
		output.write(result)


def settings() -> str:
	"""
	Returns a string with latex settings for the generating file.
	"""

	return ("\\documentclass[a4paper]{report}\n"
	        "\\usepackage[12pt]{extsizes}\n"
	        "\\usepackage[russian]{babel}\n"
	        "\\usepackage[utf8]{inputenc}\n"
	        "\\usepackage{graphicx}\n")


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 graphics.py [CSV FILE]")
	else:
		with gen_img(size=512,
		             block_size=512/8,
		             block_count=12) as avatar:
			avatar.save('in.png')

		gen_tex(sys.argv[1], 'in.png', 'artifacts/out_medium.tex')
