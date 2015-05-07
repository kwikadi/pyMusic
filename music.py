		
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
