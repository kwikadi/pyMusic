from flask import (
	Flask,
	render_template
)
from collections import namedtuple
import sys
import glob
import music
import eyed3

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
tag = eyed3.Tag()

for song in filenames:
	tag.link(song)
	songslist.append(Songs(tag.getArtist,tag.getTitle))


@app.route('/')
def hello():
	return render_template('index.html', filenames=songslist)
if __name__ == '__main__':
	app.run(debug=True)

#nextSong()
