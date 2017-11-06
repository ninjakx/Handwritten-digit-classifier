from tkinter import *
from tkinter import filedialog

import os

class PaintBox( Frame ):
   def __init__( self ):
    
      Frame.__init__( self )
      self.pack()
      self.master.title( "Drawing Tool" )
      self.master.geometry( "192x245" )
      
      self.sizex = 200
      self.sizey = 200
      # create Canvas component

      self.myCanvas = Frame(self, width=500, height=350, bd=1)
      self.myCanvas.pack()
      
      self.myCanvas1 = Frame(self.myCanvas, bd=2,relief=RAISED,background="gray")
      self.myCanvas1.pack(side = TOP ,expand=1, fill=X, ipady=20, ipadx=5)
      self.c = Canvas(self.myCanvas1, bg='white', width=340, height=200)
      self.c.pack()
  

      self.button=Button(self.myCanvas,text="Done!",width=10,bg='white',command=self.save)
      self.button.place(x=self.sizex/27,y=self.sizey+8)
      self.button1=Button(self.myCanvas,text="Clear!",width=10,bg='white',command=self.clear)
      self.button1.place(x=(self.sizex/27)+80,y=self.sizey+8)
     
      # bind mouse dragging event to Canvas
      self.c.bind( "<B1-Motion>", self.paint )
     
   def paint( self, event ):
      x1, y1 = ( event.x - 4 ), ( event.y - 4 )
      x2, y2 = ( event.x + 4 ), ( event.y + 4 )
      self.c.create_oval( x1, y1, x2, y2, fill = "black",outline='black')

   def save(self):
        
        filename = "sample_dig.ps"
        retval = self.c.postscript(file=filename, height=200, width=190, colormode="color")
        
        pngfile = 'sample_dig' + '.png'
        os.system('convert ' + filename + ' ' + pngfile)
        os.remove("sample_dig.ps")
        os.system("mogrify -alpha off sample_dig.png")

   def clear(self):
        self.c.delete("all")


def main():
   PaintBox().mainloop()

if __name__ == "__main__":
   main()



