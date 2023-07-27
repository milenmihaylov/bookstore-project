import os


def clean_up_files(path):
	try:
		os.remove(path)
	except FileNotFoundError:
		print('File not found!')
