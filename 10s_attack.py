import time
import tkinter as tk

class mush10s:
	def __init__(self, root):
		root.title("Mash Button")
		root.geometry("600x400")
		self.canvas = tk.Canvas(root, width =600, height =400, bg="white")
		self.canvas.place(x = 0, y = 0)
		self.label = tk.Label(text="")
		self.label.pack()
		start_btn = tk.Button(root, text="start", command=self.start)
		start_btn.place(x=170, y=350)
		btn = tk.Button(root, text="push", command=self.counter)
		btn.place(x=270, y=350)
		root.mainloop()

	def start(self):
		self.ready_t = 3
		self.t = 10	
		self.cnt = 0
		self.timer()

	def counter(self):
		if self.t > 0:
			self.cnt += 1

	def result(self):
		rst = tk.Label(root, text=self.cnt)
		rst.pack()
		rst.place(x=100, y=100)

	def timer(self):
		if self.ready_t > 0:
			self.label.configure(text=self.ready_t, font=('Helvetica', '50'), bg="white")
			self.ready_t -= 1
			root.after(1000, self.timer)
		elif self.t > 0:
			self.label.configure(text=self.t, font=('Helvetica', '50'), bg="white")
			self.t -= 1
			root.after(1000, self.timer)
		else:
			btn2 = tk.Button(root, text="result", command=self.result)
			btn2.place(x=400, y=350)
		#print(self.cnt)

if __name__ == "__main__":
	root = tk.Tk()
	f = mush10s(root)


