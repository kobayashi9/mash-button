import time
import tkinter as tk
class mush10s:
	def __init__(self, root):
		#root frame
		root.title("Mush Button")
		#root.geometry("600x400")
		self.label = tk.Label(text="")
		#self.label.pack()
		self.f_page = tk.Frame(root, height=400, width=600)
		self.m_page = tk.Frame(root, height=400, width=600)
		self.r_page = tk.Frame(root, height=400, width=600)
		
		for frame in (self.f_page, self.m_page, self.r_page):
			frame.grid(row=0, column=0)
			#frame.pack()
		#tk.Button(f_page, text='Go to frame 2', command=lambda:self.changePage(m_page)).pack()
		#First page
		tk.Label(self.f_page, text="Mush Button within 10 seconds.", font=40).pack()
		start_btn = tk.Button(self.f_page, text='Start', command=self.start).pack()
		
		#Play page
		push_btn = tk.Button(self.m_page, text='Push', command=self.counter).pack()
		#push_btn.grid()
		
		#Result page
		self.changePage(self.f_page)
		#start_btn = tk.Button(root, text="start", command=self.start)
		#start_btn.place(x=170, y=350)
		#push_btn = tk.Button(root, text="push", command=self.counter)
		#push_btn.place(x=270, y=350)
		root.mainloop()
	
	def end(self):
		root.destroy()

	def start(self):
		self.ready_t = 3
		self.t = 10	
		self.cnt = 0
		self.changePage(self.m_page)
		self.timer()
	
	def changePage(self, page):
		page.tkraise()


	def firstPage(self):
		pass

	def playPage(self):
		pass
	
	def resultPage(self):
		pass

	def counter(self):
		if self.t > 0 and self.ready_t == 0:
			self.cnt += 1

	def result(self):
		rst = tk.Label(root, text=self.cnt)
		#rst.pack()
		#rst.place(x=100, y=100)

	def timer(self):
		if self.ready_t > 0:
			#self.label.configure(text=self.ready_t, font=('Helvetica', '50'))
			#tk.Label(self.m_page, text=self.ready_t, font=('Helvetica', '50')).pack()
			self.ready_t -= 1
			root.after(1000, self.timer)
		elif self.t >= 0:
			#tk.Label(self.m_page, text=self.t, font=('Helvetica', '50')).pack()
			self.t -= 1
			root.after(1000, self.timer)
		else:
			result_btn = tk.Button(root, text="Result", command=self.result)
		print(self.cnt)

if __name__ == "__main__":
	root = tk.Tk()
	f = mush10s(root)


