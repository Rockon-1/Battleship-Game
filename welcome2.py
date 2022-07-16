from tkinter import *
from welcome1 import *
from PIL import  ImageTk, Image
import check_location
from tkinter import messagebox
def res(move):  #Here is for printing Result to the User
    resss=""
    if move<=18:
        resss="GOLD"
        return resss
    elif move<25:
        resss="SILVER"
        return resss
    elif move<30:
        resss="BRONZE"
        return resss
    else :
        resss="FAILURE"
        return resss
class welcome2():
    global mwin_bg
    global framcol_bg
    global buttoncol_bg
    global moves
    def __init__(self):
        wel1.main1()
        self.mwin_bg="#000123466"
        self.framcol_bg="#120320455"
        self.buttoncol_bg="#435302128"
        self.moves=0
        
    def mwin_const(self):
        global mwin_bg
        wel1.mwin.geometry("1000x519")
        wel1.mwin.configure(bg=self.mwin_bg)

    def frame2(self):
        self.fram2=Frame(wel1.mwin,width=1000,height=667,bg=self.framcol_bg)
        self.fram2.grid()

    def canvas(self):
        self.canv2=Canvas(wel1.mwin,width=1000,height=519,bg="yellow")
        self.canv2.grid()

    def image2(self):
        self.img2=PhotoImage(file="bt2.png")
        self.canv2.create_image(0,0, anchor=NW, image=self.img2)

    def gridi(self):
        self.canv2.destroy()
        self.canvas()
        self.img3=PhotoImage(file="bt3.png")
        self.canv2.create_image(0,0,anchor=NW,image=self.img3)
        frame=Frame(self.canv2,bg="black")
        frame.place(x=200,y=100)
        Label(self.canv2,text="How to Play",font=("arial",18),bg="teal").place(x=700,y=200)
        Label(self.canv2,text="You have to find 3 ships of length 3 with minimum of clicks",font=("arial",10),bg="teal").place(x=600,y=260)
        Label(self.canv2,text="Ships can be Horizontal as well as Vertical",font=("arial",10),bg="teal").place(x=600,y=280)
        Label(self.canv2,text="If location turns Black then you miss it ,otherwise you find it.",font=("arial",10),bg="teal").place(x=600,y=300)

        btn00=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,0))
        btn00.grid(row=0,column=0)
        btn01=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,1))
        btn01.grid(row=0,column=1)
        btn02=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,2))
        btn02.grid(row=0,column=2)
        btn03=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,3))
        btn03.grid(row=0,column=3)
        btn04=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,4))
        btn04.grid(row=0,column=4)
        btn05=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,5))
        btn05.grid(row=0,column=5)
        btn06=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,0,6))
        btn06.grid(row=0,column=6)
        btn10=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,0))
        btn10.grid(row=1,column=0)
        btn11=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,1))
        btn11.grid(row=1,column=1)
        btn12=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,2))
        btn12.grid(row=1,column=2)
        btn13=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,3))
        btn13.grid(row=1,column=3)
        btn14=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,4))
        btn14.grid(row=1,column=4)
        btn15=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,5))
        btn15.grid(row=1,column=5)
        btn16=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,1,6))
        btn16.grid(row=1,column=6)
        btn20=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,0))
        btn20.grid(row=2,column=0)
        btn21=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,1))
        btn21.grid(row=2,column=1)
        btn22=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,2))
        btn22.grid(row=2,column=2)
        btn23=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,3))
        btn23.grid(row=2,column=3)
        btn24=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,4))
        btn24.grid(row=2,column=4)
        btn25=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,5))
        btn25.grid(row=2,column=5)
        btn26=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,2,6))
        btn26.grid(row=2,column=6)
        btn30=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,0))
        btn30.grid(row=3,column=0)
        btn31=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,1))
        btn31.grid(row=3,column=1)
        btn32=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,2))
        btn32.grid(row=3,column=2)
        btn33=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,3))
        btn33.grid(row=3,column=3)
        btn34=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,4))
        btn34.grid(row=3,column=4)
        btn35=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,5))
        btn35.grid(row=3,column=5)
        btn36=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,3,6))
        btn36.grid(row=3,column=6)
        btn40=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,0))
        btn40.grid(row=4,column=0)
        btn41=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,1))
        btn41.grid(row=4,column=1)
        btn42=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,2))
        btn42.grid(row=4,column=2)
        btn43=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,3))
        btn43.grid(row=4,column=3)
        btn44=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,4))
        btn44.grid(row=4,column=4)
        btn45=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,5))
        btn45.grid(row=4,column=5)
        btn46=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,4,6))
        btn46.grid(row=4,column=6)
        btn50=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,0))
        btn50.grid(row=5,column=0)
        btn51=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,1))
        btn51.grid(row=5,column=1)
        btn52=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,2))
        btn52.grid(row=5,column=2)
        btn53=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,3))
        btn53.grid(row=5,column=3)
        btn54=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,4))
        btn54.grid(row=5,column=4)
        btn55=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,5))
        btn55.grid(row=5,column=5)
        btn56=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,5,6))
        btn56.grid(row=5,column=6)
        btn60=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,0))
        btn60.grid(row=6,column=0)
        btn61=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,1))
        btn61.grid(row=6,column=1)
        btn62=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,2))
        btn62.grid(row=6,column=2)
        btn63=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,3))
        btn63.grid(row=6,column=3)
        btn64=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,4))
        btn64.grid(row=6,column=4)
        btn65=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,5))
        btn65.grid(row=6,column=5)
        btn66=Button(frame,width=3,text="",height=1,bg="cadet blue",command=lambda:self.ff(frame,6,6))
        btn66.grid(row=6,column=6)
        Button(self.canv2,text="PLAY NEW GAME ",width=15,height=3,bg="brown",borderwidth=10,relief="groove",font="Helvetica",command=self.newg).place(x=227,y=350)

    def newg(s):
        s.moves=0
        check_location.again()
        s.gridi()
    def ff(self,fr,a1,a2):
        self.moves=self.moves+1
        s1=str(a1);s2=str(a2)
        sf=s1+s2
        result=check_location.ch(sf)
        if result=="miss":
            new=Button(fr,width=3,height=1,bg="black")
            new.grid(row=a1,column=a2)
        if result=="hit" or result=="kill":
            new=Button(fr,width=3,height=1,bg="red")
            new.grid(row=a1,column=a2)
            if result=="kill":
                messagebox.showinfo("STATUS","You Killed it.")
        elif result=="killsall":
            new=Button(fr,width=3,height=1,bg="red")
            new.grid(row=a1,column=a2)
            lines="Your Total Moves is :- "+str(self.moves)+"\n"+" your Rank is :- "+res(self.moves)
            messagebox.showinfo("RESULT",lines)
            strff=messagebox.askquestion("Warning","Do you want to  play again ? ")
            if strff=="no":
                exit()
            if strff=="yes":
                self.newg()
                

    def button_win1(self):
        self.start=Button(self.canv2,text="Start game",width=10,height=3,bg="brown",borderwidth=10,relief="groove",font="Helvetica",command=self.gridi)
        self.canv2.create_window(150,440,window=self.start)
        self.exit=Button(self.canv2,text="exit",width=10,height=3,bg="brown",borderwidth=10,relief="groove",font="Helvetica",command=self.popup)
        self.canv2.create_window(799,440,window=self.exit)


    def popup(self):
        strf=messagebox.askquestion("Warning","Do you want to  exit ? ")
        if strf=="yes":
            exit()
       
    
    def main2(self):
        self.mwin_const()
        self.canvas()
        self.image2()
        self.button_win1()
      
wel2=welcome2()
wel2.main2()

