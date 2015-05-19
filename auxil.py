import glob
import id3reader
import json

def findsongs(location):
	songslist = []
	filenames=glob.glob(location + '\*.mp3')
	for song in filenames:
		id3r = id3reader.Reader(song)
		# die, non tagged songs, die!
		dictio = {}
		if id3r.getValue('performer') is not None and id3r.getValue('title') is not None:
			dictio['title'] = id3r.getValue('title')
			dictio['performer'] = id3r.getValue('performer')
			dictio['album'] = id3r.getValue('album')
			dictio['year'] = id3r.getValue('year')
			dictio['genre'] = id3r.getValue('genre')
			songslist.append(dictio)
	songslist.sort()
	return songslist
