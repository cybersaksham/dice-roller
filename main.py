from tkinter import *


class GUI(Tk):
    def __init__(self, title="Window", width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


def dice_label(i):
    msg = Label(root, text=Dice[i], font=("Times", 100), width=2)
    msg.grid(row=0, column=0, padx=25, pady=5)


def roll():
    from random import randint
    i = randint(1, 6)
    dice_label(i)


if __name__ == '__main__':
    Dice = {
        0: '🎲',
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
    }

    # Making Window
    root = GUI(title="Dice Roller", width=270)

    dice_label(0)
    rollBtn = Button(root, text="Roll", command=roll)
    rollBtn.grid(row=0, column=1)

    # Starting Window
    root.start()
