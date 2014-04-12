from tkinter import *
tk = Tk()
import time
t = time.localtime()
hour = t[3]
if hour < 8:
	print("Good morning No Click")
elif hour >=8 and hour < 15:
	btn = Button(tk, text="Hallo! Click me!")
	btn.pack()
elif hour >= 15 and hour < 18:
	print("Hallo World")
elif hour >= 18 and hour < 5:
        btn = Button(tk, text="Good evnning Click now!")
        btn.pack()
   
