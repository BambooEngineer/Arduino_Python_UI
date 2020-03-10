import serial
import time
import tkinter as tk

i = input()

arduinoData = serial.Serial(i, 115200)
time.sleep(3)
S = str.encode('S')
A = str.encode('A')
T = str.encode('T')
U = str.encode('U')
R = str.encode('R')
N = str.encode('N')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.goodbye = tk.Button(self)
        self.T = tk.Button(self)
        self.U = tk.Button(self)
        self.R = tk.Button(self)
        self.N = tk.Button(self)
        
        self.hi_there["text"] = "S"
        self.goodbye["text"] = "A"
        self.T["text"] = "T"
        self.U["text"] = "U"
        self.R["text"] = "R"
        self.N["text"] = "N"
        
        self.hi_there["command"] = self.long
        self.goodbye["command"] = self.short
        self.T["command"] = self.Ta
        self.U["command"] = self.Ua
        self.R["command"] = self.Ra
        self.N["command"] = self.Na
        self.hi_there.pack(side="top")
        self.goodbye.pack(side="bottom")
        self.T.pack(side="bottom")
        self.U.pack(side="bottom")
        self.R.pack(side="bottom")
        self.N.pack(side="bottom")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def long(self):
        print("BLINKING")
        arduinoData.write(S)
    def short(self):
        print("BLINKING")
        arduinoData.write(A)

    def Ta(self):
        print("BLINKING")
        arduinoData.write(T)
    def Ua(self):
        print("BLINKING")
        arduinoData.write(U)
    def Ra(self):
        print("BLINKING")
        arduinoData.write(R)
    def Na(self):
        print("BLINKING")
        arduinoData.write(N)
    
    
   #data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   #c = data.decode('utf-8')
   


root = tk.Tk()
app = Application(master=root)
app.mainloop()

