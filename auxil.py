from collections import namedtuple
import glob
import id3reader
import json

Songs = namedtuple('Songs', 'name artist')

def findsongs(location):
	global songslist
	songslist = []
	filenames=glob.glob(location + '\*.mp3')
	for song in filenames:
		id3r = id3reader.Reader(song)
		# die, non tagged songs, die!
		if id3r.getValue('performer') is not None and id3r.getValue('title') is not None:
			songslist.append(Songs(id3r.getValue('title'),id3r.getValue('performer')))
	songslist.sort()
	print songslist[0]
	print songslist[1]
	createjson()
	return songslist

def createjson():
	data = {}
	for song in songslist:
		data[song[0]] = song[1]
	with open("songs.json", "w") as outfile:
		json.dump(data, outfile, sort_keys=True, indent=4)
