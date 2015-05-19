from flask import (
	Flask,
	render_template,
	url_for,
	redirect,
	jsonify
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
	return render_template('index.html')

@app.route('/api/songs')
def returnvalues():
	jsonval = auxil.findsongs('C:\Users\\admin\Music\iTunes_ind')
	return jsonify({'songs' : jsonval})

if __name__ == '__main__':
	app.run(debug=True)

