#parse and move files
#gotta add some more formats

import os
import shutil

formats = ['.png', '.jpeg', '.jpg', '.bmp', '.gif', '.webm', '.avi', '.mp4', '.mp3', '.pdf', '.epub', '.torrent', '.mkv', '.flv', '.mov', '.wmv', '.gz', '.txt', '.deb', '.svg']


directions = dict(
		#gif file formats
		webm = '/home/devonwc/Documents/gifs/',
		gif = '/home/devonwc/Documents/gifs/',
		#image file formats
		svg = '/home/devonwc/Documents/images/',
		png = '/home/devonwc/Documents/images/',
		jpg = '/home/devonwc/Documents/images/',
		bmp = '/home/devonwc/Documents/images/',
		jpeg = '/home/devonwc/Documents/images/',
		#video file formats
		mp4 = '/home/devonwc/Documents/videos/',
		mkv = '/home/devonwc/Documents/videos/',
		flv = '/home/devonwc/Documents/videos/',
		avi = '/home/devonwc/Documents/videos/',
		wmv = '/home/devonwc/Documents/videos/',
		mov = '/home/devonwc/Documents/videos/',
		#music file formats
		mp3 = '/home/devonwc/Documents/music/',
		#text, Documents and other file formats
		pdf = '/home/devonwc/Documents/pdf_files/',
		epub = '/home/devonwc/Documents/ebooks',
		txt = '/home/devonwc/Documents/text_files/',
		torrent = '/home/devownc/Documents/torrent_files/',
		gz = '/home/devonwc/Documents/tarballs/',
		deb = '/home/devonwc/Documents/deb_packages/',
		run = '/home/devonwc/Documents/run_packages/',						
)

hasm = 0

for file in os.listdir('/home/devonwc'):

	filename, file_extension = os.path.splitext(file)
	for fmt in formats:
		if file_extension == fmt:
			try:
				movedir = directions[fmt.split('.')[1]]
				shutil.move("/home/devonwc/%s" % file, movedir)
				hasm = hasm + 1
				print('File: /home/devonwc/%s' % file, '\nmoved to:', movedir, '\n')
			except Exception as e:
				print(e)

if hasm >= 1:
	print("%d files moved" % hasm)
else:
	print("Nothing to move")




