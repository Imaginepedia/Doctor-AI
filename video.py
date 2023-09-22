import tkinter
from tkvideo import tkvideo

w=tkinter.Tk()
w.title("Docter AI")

lblvideo= tkinter.Label(w)
lblvideo.pack()

player= tkvideo("C:\\Users\\debaj\\OneDrive\\Documents\\WhatsApp Video 2023-09-21 at 17.04.31.mp4",lblvideo,loop=1,size=(700,500))

player.play()

w.mainloop()