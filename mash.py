#from tkinter import * 
import tkinter as tk
class Mush10s:
	def __init__(self, root):
		root.title("Mush Button")
		self.f1 = tk.Frame(root, height=400, width=600) 
		self.f2 = tk.Frame(root, height=400, width=600) 
		self.f3 = tk.Frame(root, height=400, width=600) 
		self.f4 = tk.Frame(root, height=400, width=600) 
		for frame in (self.f1, self.f2, self.f3, self.f4): 
		    frame.grid(row=0, column=1, sticky='news')
		self.firstPage()
		self.playPage()
		self.changePage(self.f1) 
		root.mainloop() 

	def start(self):
		self.ready_t = 3
		self.t = 10
		self.cnt = 0
		self.changePage(self.f2)
		self.timer()

	def firstPage(self):
		tk.Label(self.f1, text='Mush Button', font=('Helvetica', '60')).pack()
		#Button(self.f1, text='Go to frame 2', command=lambda:self.changePage(self.f2)).pack() 
		tk.Button(self.f1, text='Start', command=self.start).place(x=260, y=300)
	
	def playPage(self):
		tk.Label(self.f3, text='Push!!', font=('Helvetica', '60')).pack() 
		#tk.Button(self.f2, text='Go to frame 3', command=lambda:self.changePage(self.f1)).pack() 
		push_btn = tk.Button(self.f3, text='Push', command=self.counter).place(x=260, y=300)
		back_btn = tk.Button(self.f3, text='Back', command=lambda:self.changePage(self.f1)).place(x=100, y=300)
	
	def resultPage(self):
		res_label = tk.Label(self.f4, text="{} times".format(self.cnt), font=('Helvetica', '60')).place(x=150, y=50)
		tk.Button(self.f4, text="Back", command=lambda:self.changePage(self.f1)).place(x=260, y=300)
		self.changePage(self.f4)
	
	def changePage(self, frame): 
		frame.tkraise()

	def counter(self):
		if self.t >= 0 and self.ready_t == -1:
			self.cnt += 1
	
	def timer(self):
		if self.ready_t >= 0:
			#self.label.configure(text=self.ready_t, font=('Helvetica', '50'))
			r_label = tk.Label(self.f2, text=self.ready_t, font=('Helvetica', '50'))
			r_label.place(x=270, y=100)
			self.ready_t -= 1
			root.after(1000, self.timer)
		elif self.t >= 0:
			#m_label = tk.Label(self.f3, text=self.t, font=('Helvetica', '20')).place(x=260, y=100)
			root.after(1000, self.timer)
			self.t -= 1
			print(self.cnt)
		else:
			self.resultPage()
		
		if self.ready_t < 0 and self.t > 0:
			self.changePage(self.f3)

if __name__ == "__main__":
	root = tk.Tk()
	Mush10s(root)