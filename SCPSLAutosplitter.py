from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener
from PIL import ImageGrab#, ImageDraw
from time import sleep

keyboard = Controller()

def on_press(key):
	if key == Key.f5:
		#Stop livesplit
		keyboard.press(Key.f6)
		sleep(0.05)
		keyboard.release(Key.f6)
		#open console
		keyboard.press('`')
		sleep(0.05)
		keyboard.release('`')
		#seed
		keyboard.type("seed")
		keyboard.press(Key.enter)
		sleep(0.05)
		keyboard.release(Key.enter)
		#restart
		sleep(1)
		keyboard.type("restart")
		keyboard.press(Key.enter)
		sleep(0.05)
		keyboard.release(Key.enter)
		#seed again
		sleep(5)
		keyboard.type("seed")
		keyboard.press(Key.enter)
		sleep(0.05)
		keyboard.release(Key.enter)
		sleep(0.5)
		keyboard.press('`')
		sleep(0.05)
		keyboard.release('`')
	return 0

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

	

	

	if (r in range(230,256)) & (g in range(135, 150)) & (b in range(0,5)): #play around with these ranges.
		# print("ORANG DETECTED!")
		keyboard.press(Key.f7)
		sleep(0.05)
		keyboard.release(Key.f7)
		sleep(20)
		
		with Listener(on_press=on_press) as listener:
			listener.join()

	else:
		# print("nope")
		sleep(0.5)