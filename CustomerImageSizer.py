from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

i = 0
pointx = [0,0,0,0]
pointy = [0,0,0,0]
if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(File)
    width, heigth = load.size
    wtohRatio = width/heigth
    load = load.resize((400, int(400/wtohRatio)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(load)
    canvas.create_image(50,50,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
        global i
        #outputting x and y coords to console
        print (event.x,event.y)
        pointx[i] = event.x
        pointy[i] = event.y

        print (pointx)
        print (pointy)
        python_green = "#476042"
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        canvas.create_oval(x1, y1, x2, y2, fill=python_green)
        if i == 1:
            canvas.create_line(pointx[0], pointy[0], pointx[1], pointy[1], fill="red")
        if i > 2:
            canvas.create_line(pointx[2], pointy[2], pointx[3], pointy[3], fill="red")



        i = i+1
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)



    Button(root, text='OK', command=root.destroy).pack()

    root.mainloop()