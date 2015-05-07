from flask import (
	Flask,
	render_template
)
from collections import namedtuple
import sys
import glob
import music
import id3reader

'''def nextSong():
	filenames=glob.glob('*.mp3')
	for i in range(len(filenames)):
		if (votes[i]>temp):
			temp = i
	votes[i] = 0
	dumpWAV(filenames[i]);'''

app = Flask(__name__)

Songs = namedtuple('Songs', 'name artist')
songslist = []

filenames=glob.glob('*.mp3')

for song in filenames:
	id3r = id3reader.Reader(song)
	songslist.append(Songs(id3r.getValue('performer'),id3r.getValue('title')))

@app.route('/')
def hello():
	return render_template('index.html', filenames=songslist)
if __name__ == '__main__':
	app.run(debug=True)

#nextSong()
