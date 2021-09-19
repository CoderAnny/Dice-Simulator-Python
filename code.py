from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import random as rand

root = Tk()
root.title("----- DICE SIMULATOR -----")
root.geometry("500x700+0+0")
root.minsize(1300,800)
root.state("zoomed")


img1 = ImageTk.PhotoImage(Image.open(
    "Images/dice-1.jpg").resize((300, 300), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open(
    "Images/dice-2.jpg").resize((300, 300), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open(
    "Images/dice-3.jpg").resize((300, 300), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open(
    "Images/dice-4.jpg").resize((300, 300), Image.ANTIALIAS))
img5 = ImageTk.PhotoImage(Image.open(
    "Images/dice-5.jpg").resize((300, 300), Image.ANTIALIAS))
img6 = ImageTk.PhotoImage(Image.open(
    "Images/dice-6.jpg").resize((300, 300), Image.ANTIALIAS))

image_list = [img1, img2, img3, img4, img5, img6]


def checkwinner(i1, i2):

    l1_img = i1["image"][-1:]  # [-1:] provides us last digit
    l2_img = i2["image"][-1:]

    if(l1_img == l2_img):
        msg.showinfo("Game Result", "------ Match Is Tied ------")
    elif(l1_img < l2_img):
        msg.showinfo("Game Result", "Player 2 Wins This Match")
    else:
        msg.showinfo("Game Result", "Player 1 Wins This Match")


def rollingDice1():
    l1.config(image=rand.choice(image_list))
    b2.config(state=NORMAL)
    b1.config(state=DISABLED)


def rollingDice2():
    l2.config(image=rand.choice(image_list))
    checkwinner(l1, l2)
    b2.config(state=DISABLED)
    b1.config(state=NORMAL)


lbl1 = Label(root, text=" Player 1 ", font=(
    'Helevetica', 18, 'bold'), fg="#fff", bg="#000")
lbl1.place(x=200, y=70, width=300, height=70)
l1 = Label(root, image=rand.choice(image_list))
l1.place(x=200, y=150, width=300, height=300)
b1 = Button(root, text=f"{'Player 1 Turn'.upper()}", bg="blue", fg="#fff", font=(
    'Georgia', 15, 'bold'), cursor="hand2", command=lambda: rollingDice1())
b1.place(x=250, y=480, height=50)


lbl1 = Label(root, text=" Player 2 ", font=(
    'Helevetica', 18, 'bold'), fg="#fff", bg="#000")
lbl1.place(x=900, y=70, width=300, height=70)
l2 = Label(root, image=rand.choice(image_list))
l2.place(x=900, y=150, width=300, height=300)
b2 = Button(root, text=f"{'Player 2 Turn'.upper()}", bg="blue", fg="#fff", font=(
    'Georgia', 15, 'bold'), state=DISABLED, cursor="hand2", command=lambda: rollingDice2())
b2.place(x=950, y=480, height=50)


root.config(bg="#000")
root.mainloop()
