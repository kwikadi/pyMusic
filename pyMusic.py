from flask import (
	Flask,
	render_template,
	url_for,
	redirect
)
from collections import namedtuple
import sys
import glob
import music
import id3reader

def nextSong(songname):
	pass

app = Flask(__name__)

Songs = namedtuple('Songs', 'name artist')

@app.route('/')
def reroute():
	return redirect(url_for('hello', page_no=1))

@app.route('/page/<int:page_no>')
def hello(page_no):
	songslist = []
	filenames=glob.glob('*.mp3')
	pages = len(filenames)/10 + 1
	for song in filenames:
		id3r = id3reader.Reader(song)
		songslist.append(Songs(id3r.getValue('performer'),id3r.getValue('title')))
	back_available = page_no - 1
	front_available = pages - page_no
	if front_available >= 2 and back_available >= 2:
		print "first"
		paginator = [num for num in range(page_no - 2, page_no + 3)]
	elif back_available < 2 and front_available >2:
		print "Second"
		paginator = [num for num in range(1,page_no + 5 - back_available)]
	elif back_available > 2 and front_available < 2:
		print "Third"
		paginator = [num for num in range(page_no - 4 + front_available,pages+1)]
	else:
		print "Final"
		paginator = [num for num in range(1, pages)]
	return render_template('index.html', filenames=songslist[10*(page_no - 1):10*(page_no - 1)+9], paginator=paginator, page=page_no)


if __name__ == '__main__':
	app.run(debug=True)

#nextSong()
