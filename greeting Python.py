import time
t = time.localtime()
hour = t[3]
if hour < 8:
	print("Good morning")
elif hour >=8 and hour < 15:
	print("Hallo!")
elif hour >= 15 and hour < 18:
	print("Hallo World")
elif hour >= 18 and hour < 5:
	print("Good evnning!")
