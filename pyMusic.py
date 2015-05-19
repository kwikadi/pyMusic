from flask import (
	Flask,
	render_template,
	url_for,
	redirect
)
import auxil
import sys
import music

def nextSong(songname):
	pass

app = Flask(__name__)

@app.route('/')
def reroute():
	return redirect(url_for('hello', page_no=1))

@app.route('/page/<int:page_no>')
def hello(page_no):
	songslist = auxil.findsongs('C:\Users\\admin\Music\iTunes_ind')
	pages = len(songslist)/10 + 1
	back_available = page_no - 1
	front_available = pages - page_no
	if front_available >= 2 and back_available >= 2:
		paginator = [num for num in range(page_no - 2, page_no + 3)]
	elif back_available < 2 and front_available >2:
		paginator = [num for num in range(1,page_no + 5 - back_available)]
	elif back_available > 2 and front_available < 2:
		paginator = [num for num in range(page_no - 4 + front_available,pages+1)]
	else:
		paginator = [num for num in range(1, pages)]
	return render_template('index.html', filenames=songslist[10*(page_no - 1):10*(page_no - 1)+9], paginator=paginator, page=page_no)


if __name__ == '__main__':
	app.run(debug=True)

#nextSong()
