import sys
from tkinter import Button, mainloop
x = Button(
		text = "Click Me",
		command = (lambda:sys.stdout.write("allen\n"))
	)

x.pack()
mainloop()