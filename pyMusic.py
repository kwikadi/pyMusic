import cherrypy
import sys
import glob
from threading import Thread

votes=[0,0,0,1]
filenames=glob.glob('*.mp3')

class Pageypage(object):
	@cherrypy.expose
	def index(self):
		return """ <head>
			<title>Booooring</title>
			</head>
			<body>
			<h1>Hello world!</h1>
			<form action="http://localhost:8080/upvote?id=0">
				<input type="submit" value="Song 1">
			</form>
			<form action="http://localhost:8080/upvote?id=1">
				<input type="submit" value="Song 2">
			</form>
			<form action="http://localhost:8080/upvote?id=2">
				<input type="submit" value="Song 3">
			</form>
			<form action="http://localhost:8080/upvote?id=3">
				<input type="submit" value="Song 4">
			</form>
			</body>"""

	@cherrypy.expose
	def upvote(self, id=0):
		global votes
		votes[id] += 1
		"""return what?"""
		
def playering( fname ):
	import pymedia.audio.sound as sound
	import time, wave
	f= wave.open( fname, 'rb' )
	sampleRate= f.getframerate()
	channels= f.getnchannels()
	format= sound.AFMT_S16_LE
	snd1= sound.Output( sampleRate, channels, format )
	s= ' '
	while len( s ):
		s= f.readframes( 1000 )
		snd1.play( s )
  
	while snd1.isPlaying(): 
		time.sleep( 0.05 )
		
	nextSong()


def dumpWAV( name ):
	import pymedia.audio.acodec as acodec
	import pymedia.muxer as muxer
	import time, wave, string, os
	name1= str.split( name, '.' )
	name2= string.join( name1[ : len( name1 )- 1 ] )
	dm= muxer.Demuxer( name1[ -1 ].lower() )
	dec= None
	f= open( name, 'rb' )
	snd= None
	s= " "
	while len( s ):
		s= f.read( 20000 )
		if len( s ):
			frames= dm.parse( s )
			for fr in frames:
				if dec== None:
					dec= acodec.Decoder( dm.streams[ 0 ] )
				r= dec.decode( fr[ 1 ] )
				if r and r.data:
					if snd== None:
						snd= wave.open( name2+ '.wav', 'wb' )
						snd.setparams( (r.channels, 2, r.sample_rate, 0, 'NONE','') )
					
					snd.writeframes( r.data )
	print("Now playing " +name2)
	playering(name2+ '.wav')
					


def nextSong():
	global votes
	filenames=glob.glob('*.mp3')
	temp = 0
	i=0
	for i in range(len(filenames)):
		if (votes[i]>temp):
			temp = i
	votes[i] = 0
	dumpWAV(filenames[i]);

	
t1=Thread(target = nextSong())
t1.setDaemon=True
t1.start()
cherrypy.quickstart(Pageypage())
while True:
	pass