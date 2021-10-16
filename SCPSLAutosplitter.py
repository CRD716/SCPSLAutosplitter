from pynput.keyboard import Key, Controller
from PIL import ImageGrab#, ImageDraw
from time import sleep

while True:
	screen = ImageGrab.grab()
	#screen.show()
	# 255, 142, 0 is the d class rgb values
	width, height = screen.size

	#uncomment these and the import imagedraw so you can sorta see where it's targeting
	#img1 = ImageDraw.Draw(screen)
	#img1.point([width/2, height/2.5], (0,255,0))
	#screen.show()
	

	r, g, b = screen.getpixel((width/2, height/2.5)) #modify x and y if it isn't working for you

	print(r, g, b)

	keyboard = Controller()

	if (r in range(230,256)) & (g in range(135, 150)) & (b in range(0,5)): #play around with these ranges.
		# print("ORANG DETECTED!")
		keyboard.press(Key.f7)
		sleep(20)
	else:
		# print("nope")
		sleep(0.5)