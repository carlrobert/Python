import tkinter as tk

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, prompt):
        tk.Toplevel.__init__(self, parent)
        self.var = tk.StringVar()

        self.label = tk.Label(self, text=prompt)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)
		
        self.label.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x")
        self.ok_button.pack(side="right")
		
        self.entry.bind("<Return>", self.on_ok)

    def on_ok(self, event=None):
        self.destroy()
		
    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()
		

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        info = 'britt'
        self.svar = CustomDialog(self, "Svar").show()

if __name__ == "__main__":
    test246 = ''
    e = Example(test246)
    print(e.svar)
