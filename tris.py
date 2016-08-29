import pyglet
from pyglet.window import mouse
import pyglet.gl

window = pyglet.window.Window(width = 940, height = 940)

icon1 = pyglet.image.load('16x16.png')
icon2 = pyglet.image.load('32x32.png')
window.set_icon(icon1, icon2)

background = pyglet.resource.image('background.png')

cross_image = pyglet.resource.image('cross.png')
cross_texture = cross_image.get_texture()
cross_texture.width = 300
cross_texture.height = 300

circle_image = pyglet.resource.image('circle.png')
circle_texture = circle_image.get_texture()
circle_texture.width = 300
circle_texture.height = 300

class tris:
	def __init__(self):
		self.a = [[0]*3,[0]*3,[0]*3]
		self.turn = True
		self.start = True
		self.restart = False
		self.victory = 0

	def click(self,x,y):
		if self.turn == True:
			self.a[x][y] = 1
		else:
			self.a[x][y] = 2
		self.turn = not self.turn

mytris = tris()

def screenwrite(a):
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (20,530,920,530,920,410,20,410) ), ('c3f', (0, 0, 0)*4 ) )
	label = pyglet.text.Label(a,
                          font_name='Times New Roman',
                          font_size=60,
                          color=(255,255,255,255),
                          #color=(40,150,240,200),
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
	label.draw()

def victory(i):
	mytris.victory = i
	mytris.restart = True

def check():
	for x in range(3):
		for y in range(3):
			if mytris.a[x][y] == 1:
				cross_texture.blit(x*310+10, y*310+10)
			elif mytris.a[x][y] == 2:
				circle_texture.blit(x*310+10, y*310+10)
	# Victory condition
	for x in range(3):
		# Horizontal
		if mytris.a[x][0] == mytris.a[x][1] and mytris.a[x][0] == mytris.a[x][2] and mytris.a[x][0] != 0:
			victory(mytris.a[x][0])
			return 0
		# Vertical
		if mytris.a[0][x] == mytris.a[1][x] and mytris.a[0][x] == mytris.a[2][x] and mytris.a[0][x] != 0:
			victory(mytris.a[0][x])
			return 0
	# Diagonal
	if mytris.a[0][0] == mytris.a[1][1] and mytris.a[0][0] == mytris.a[2][2] and mytris.a[0][0] != 0:
		victory(mytris.a[0][0])
		return 0
	if mytris.a[2][0] == mytris.a[1][1] and mytris.a[1][1] == mytris.a[0][2] and mytris.a[1][1] != 0:
		victory(mytris.a[1][1])
		return 0
	# Draw condition
	for x in range(3):
		for y in range(3):
			if mytris.a[x][y] == 0:
				return 0
	victory(0)

@window.event
def on_draw():
	window.clear()
	background.blit(0, 0)
	check()
	if mytris.start == True:
		window.clear()
		screenwrite('Click to start')
		return 0
	elif mytris.restart == True:
		mytris.a = [[0]*3,[0]*3,[0]*3]
		if mytris.victory == 0:
			screenwrite('Draw! Click to restart')
		elif mytris.victory == 1:
			screenwrite('Cross win! Click to restart')
		elif mytris.victory == 2:
			screenwrite('Circle win! Click to restart')
		return 0

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		if mytris.start == True:
			mytris.start = False
			return 0
		elif mytris.restart == True:
			mytris.restart = False
			return 0
		else:
			x = int(x//300)
			y = int(y//300)
			print "%d , %d" % (x, y)
			if mytris.a[x][y] == 0:
				mytris.click(x,y)
			print mytris.a

pyglet.app.run()
