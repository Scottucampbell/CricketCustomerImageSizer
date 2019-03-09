from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import math


i = 0
pointx = [0,0,0,0]
pointy = [0,0,0,0]
if __name__ == "__main__":
    root = Tk()
    root.title("Cricket Sizer")

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, relief=SUNKEN)
    canvas = Canvas(frame,  width=800, height=450, bd=0)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    frame.pack(fill=BOTH,expand=1)
    label = Label(root, text="Dime Size (in) :")
    label.place(relx = .7, rely = .25)
    label = Label(root, text="Cricket Size (in) :")
    label.place(relx=.7, rely=.40)

    dimeDiameter = StringVar()
    label = Label(root, textvariable=dimeDiameter)
    dimeDiameter.set("0.705")
    label.place(relx=.85, rely=.25)

    cricLengthvar = StringVar()
    label = Label(root, textvariable=cricLengthvar)
    cricLengthvar.set("0")
    label.place(relx=.85, rely=.40)



    #adding the image
    File = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(File)
    width, heigth = load.size
    wtohRatio = width/heigth
    print (width)
    print (heigth)
    load = load.resize((round(width/10), round(heigth/10)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(load)
    canvas.create_image(50,50,image=img,anchor="nw")


    #function to be called when mouse is clicked
    def printcoords(event):
        global i
        global myCircle
        #outputting x and y coords to console
        print (event.x,event.y)
        pointx[i] = event.x
        pointy[i] = event.y

        python_green = "#476042"
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        myCircle = canvas.create_oval(x1, y1, x2, y2, fill=python_green)
        if i == 1:
            canvas.create_line(pointx[0], pointy[0], pointx[1], pointy[1], fill="red")
        if i > 2:
            canvas.create_line(pointx[2], pointy[2], pointx[3], pointy[3], fill="red")
            #size Calcs
            xDifDime = abs(pointx[1]-pointx[0])
            yDifDime = abs(pointy[1] - pointy[0])
            pixeldimeLength = math.sqrt(xDifDime*xDifDime + yDifDime*yDifDime)

            xDifCric = abs(pointx[3] - pointx[2])
            yDifCric = abs(pointy[3] - pointy[2])
            pixelcricLength = math.sqrt(xDifCric * xDifCric + yDifCric * yDifCric)

            cricLength = (pixelcricLength / pixeldimeLength) * .705

            cricLengthvar.set(str(float('%.4g' % cricLength)))
            print (cricLength)


        i = i+1

    def clear():
        global i
        global myCircle
        i = 0
        canvas.delete(myCircle)



    #mouseclick event
    canvas.bind("<Button 1>",printcoords)
    Button(root, text='CLEAR', command=clear).pack()
    Button(root, text='CLOSE', command=root.destroy).pack()

    root.mainloop()