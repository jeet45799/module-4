def LastNlines(fname, N):
	with open(fname) as file:

		for line in (file.readlines() [-N:]):
			print(line, end ='')



if __name__ == '__main__':
	fname = 'reading.txt'
	N = 3
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
