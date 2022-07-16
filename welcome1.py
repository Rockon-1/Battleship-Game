from tkinter import *


class welcome1:
    global mwin
    global window_bg
    global canv
    global canvas_bg
        
    def start(self):
        self.mwin=Tk()
        self.window_bg="red"
        self.canvas_bg="white"

    def window_const(self):
        x=self.mwin.winfo_screenwidth()/2-500
        y=self.mwin.winfo_screenheight()/2-312
        self.mwin.title("Battle ship")
        self.mwin.geometry("%dx%d+%d+%d"%(1000,563,x,y))
        self.mwin.resizable(0,0)
        self.mwin.configure(bg=self.window_bg)

    def frame(self):
        self.fram=Frame(self.mwin,width=1000,height=625)
        self.fram.grid()

    def canvas(self):
        global canv
        global canvas_bg
        self.canv=Canvas(self.fram,width=1000,height=625,bg=self.canvas_bg)
        self.canv.grid()
        

    def image(self):
        self.img=PhotoImage(file="bt.png")
        self.canv.create_image(0,0, anchor=NW, image=self.img)

    def destroy_it(self):
        wel1.mwin.after(1000,self.fram.destroy)

    def main1(self):
        self.start()
        self.window_const()
        self.frame()
        self.canvas()
        self.image()
        self.destroy_it()
        return self
        
wel1=welcome1()       
if(__name__=="__main__"):
    wel1.main1()




