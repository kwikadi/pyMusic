import pyglet
import glob

from pyglet.window import key

i = 0
filenames = glob.glob('*.mp3')
window = pyglet.window.Window()
player = pyglet.media.Player()
label = pyglet.text.Label("MusicX", font_name='Times New Roman', font_size=36,x=window.width//2, y=window.height-20, anchor_x='center', anchor_y='center')

play = 0
start = 0


@window.event
def on_draw():
	window.clear()
	label.draw()

@window.event
def on_key_press(symbol,modifiers):
	global i
	global play
	global start
	if symbol == key.ENTER and start == 0:
		source = pyglet.media.load(filenames[i])
		player.queue(source)
		player.play()
		play = 1
		start = 1

	elif symbol == key.SPACE:
		if play == 1:
			player.pause()
			play = 0
		else:
			player.play()
			play = 1
	
	elif symbol == key.RIGHT:
		if i != len(filenames)-1:
			i += 1
			source = pyglet.media.load(filenames[i])
			player.queue(source)
			player.next()
	
	elif symbol == key.LEFT:
		if i > 0:
			i -=1
			source = pyglet.media.load(filenames[i])
			player.queue(source)
			player.next()

@player.event
def on_eos():
	global i
	i += 1
	if i != len(filenames)-1:
		source = pyglet.media.load(filenames[i])
		player.queue(source)
		player.play()
pyglet.app.run()
