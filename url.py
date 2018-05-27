import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'files')


with open('url.txt','a') as w:
	for subdir, dirs, files in os.walk(path):
			for file in files:
				file_path = subdir + os.path.sep + file
				f = open(file_path, 'r')
				first_line = f.readline()
				f.close()
				output = file + "," + first_line 
				w.write(output)

			