""" Made by Nicolas Mendes - Version 1.0.3 Aug 2021
CSS Basic Converter makes your life easier converting Px to Rem units or vice versa
Don't forget to contribute. You need Python 3.9 and Tkinter.
------------------------------------------------------------------------------
SUMMARY:
------------------------------------------------------------------------------
📚 Vars
💬 Entries
🧠 Entries Function and logic
📕 Static Informative Texts
🎲 Shapes
🎯 Buttons
🧩 Entry informative texts (units)
------------------------------------------------------------------------------ """

from pathlib import Path
from tkinter import *
from tkinter import messagebox
import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# 📚 Vars
tkRootWindow = Tk()
tkRootWindow.geometry("1152x700")
tkRootWindow.configure(bg="#283F52")
tkRootWindow.title("CSS Basic Converter - Nick")
tkRootWindow.resizable(False, False)

canvas = Canvas(tkRootWindow, bg="#283F52", height=700,
                width=1152, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# 💬 Entries
# Pixels 1
# Text var
entry_text_1 = StringVar()
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    361.0,
    316.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#94ADC3",
    highlightthickness=0,
    textvariable=entry_text_1,
    font="Quicksand 20"
)
entry_1.place(
    x=210.5,
    y=296.0,
    width=270.0,
    height=43.0
)
entry_text_1.set("16")
# REMs 2
# Text var
entry_text_2 = StringVar()
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    361.0,
    452.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#94ADC3",
    highlightthickness=0,
    textvariable=entry_text_2,
    font="Quicksand 20"
)
entry_2.place(
    x=210.5,
    y=432.0,
    width=250.0,
    height=43.0
)
entry_text_2.set("1")
# Default Font Size
entry_font_Size = StringVar()
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    361.0,
    613.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#94ADC3",
    highlightthickness=0,
    textvariable=entry_font_Size,
    font="Quicksand 20"
)
entry_3.place(
    x=210.5,
    y=593.0,
    width=270.0,
    height=43.0
)
entry_font_Size.set("16")
# Text var
entry_text_4 = StringVar()
# REM 1
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    791.0,
    316.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#94ADC3",
    highlightthickness=0,
    fg="#ffffff",
    disabledforeground="#ffffff",
    textvariable=entry_text_4,
    font="Quicksand 20 bold",
    state='disabled',
    disabledbackground="#94ADC3"
)
entry_4.place(
    x=640.5,
    y=296.0,
    width=250.0,
    height=43.0
)
entry_text_4.set("0")

# text var
entry_text_5 = StringVar()
# Pixels 2
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    791.0,
    452.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#94ADC3",
    disabledforeground="#ffffff",
    highlightthickness=0,
    textvariable=entry_text_5,
    font="Quicksand 20 bold",
    state='disabled',
    disabledbackground="#94ADC3"
)
entry_5.place(
    x=640.5,
    y=432.0,
    width=250.0,
    height=43.0
)
entry_text_5.set("0")

# 🧠 Entries Function and logic

# Regular Expression from module re;
# https://docs.python.org/3/library/re.html
# This def will make sure that the remTwo var can have a "." as float


def validate(string):
    result = re.match(r"(\+|\-)?\d+(\.\d+)?$", string)
    return result is not None


def resultPush():
    # Store the value from entry_* in variables
    pxOne = entry_1.get()
    remOne = entry_4.get()
    fontSize = entry_3.get()
    pxTwo = entry_5.get()
    remTwo = entry_2.get()
    fontSize = entry_3.get()

    # If entry_* has alphabetic then clear the all entries and add default values
    if not pxOne.isdigit() or not fontSize.isdigit():
        entry_1.delete(0, END)
        entry_text_1.set("16")
        entry_3.delete(0, END)
        entry_font_Size.set("16")
        messagebox.showinfo("Error! Impossible to proceed.",
                            "Please enter only digits!")

    if validate(remTwo):
        print("Ok! remTwo is good to go.")
    else:
        print("NO! remTwo is not good to go.")
        entry_2.delete(0, END)
        entry_text_2.set("1")
        messagebox.showinfo("Error! Impossible to proceed.",
                            "Please enter only digits!")

    # if pxOne or fontSize are zero or none, then show a messagebox.
    if pxOne is None or fontSize is None or pxOne == "0" or fontSize == "0":
        print("Error", "Please enter values")
        messagebox.showinfo("Error! Impossible to proceed.",
                            "Please enter valid values")
    else:
        remRes = float(float(pxOne) / float(fontSize))
        remResTwo = float(fontSize) * float(remTwo)
        print(remRes)
        print(remResTwo)

        entry_text_5.set(str(remResTwo))
        entry_text_4.set(str(remRes))


# 📕 Static Informative Texts
canvas.create_text(
    404.0,
    64.0,
    anchor="nw",
    text="CSS Basic Converter",
    fill="#FFFFFF",
    font=("Quicksand Medium", 36 * -1)
)

canvas.create_text(
    403.0,
    129.0,
    anchor="nw",
    text="Pixels     REM",
    fill="#FFBF5A",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    687.0,
    129.0,
    anchor="nw",
    text="REM     Pixels",
    fill="#FFBF5A",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    311.0,
    129.0,
    anchor="nw",
    text="Convert           to",
    fill="#FF704D",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    595.0,
    129.0,
    anchor="nw",
    text="Convert         to",
    fill="#FF704D",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    545.0,
    129.0,
    anchor="nw",
    text=">",
    fill="#94ADC3",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    831.0,
    129.0,
    anchor="nw",
    text=">",
    fill="#94ADC3",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    298.0,
    129.0,
    anchor="nw",
    text="<",
    fill="#94ADC3",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    569.0,
    129.0,
    anchor="nw",
    text="</",
    fill="#94ADC3",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    331.0,
    241.0,
    anchor="nw",
    text="Pixels",
    fill="#FFFFFF",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    754.0,
    384.0,
    anchor="nw",
    text="Pixels",
    fill="#FFFFFF",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    765.0,
    241.0,
    anchor="nw",
    text="REM",
    fill="#FFFFFF",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    331.0,
    384.0,
    anchor="nw",
    text="REM",
    fill="#FFFFFF",
    font=("Quicksand Regular", 24 * -1)
)

canvas.create_text(
    196.0,
    545.0,
    anchor="nw",
    text="Default Font Size",
    fill="#FFFFFF",
    font=("Quicksand Regular", 24 * -1)
)

# 🎲 Shapes
canvas.create_rectangle(
    549.0,
    316.0,
    603.0,
    316.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    549.0,
    452.0,
    603.0,
    452.0,
    fill="#FFFFFF",
    outline="")

# 🎯 Buttons
# Button Convert
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: resultPush(),
    relief="flat"
)
button_1.place(
    x=756.0,
    y=572.0,
    width=200.0,
    height=64.0
)

# 🧩 Entry informative texts (units)
# Texts for entries
pxFontSizeTxt = canvas.create_text(
    480.0,
    601.0,
    anchor="nw",
    text="px",
    fill="#FFFFFF",
    font=("Quicksand Regular", 20 * -1)
)
canvas.tag_raise(pxFontSizeTxt)

remTwoTxt = canvas.create_text(
    470.0,
    440.0,
    anchor="nw",
    text="rem",
    fill="#FFFFFF",
    font=("Quicksand Regular", 20 * -1)
)
canvas.tag_raise(remTwoTxt)

pxTwoTxt = canvas.create_text(
    910.0,
    440.0,
    anchor="nw",
    text="px",
    fill="#FFFFFF",
    font=("Quicksand Regular", 20 * -1)
)
canvas.tag_raise(pxTwoTxt)

remOneTxt = canvas.create_text(
    895.0,
    304.0,
    anchor="nw",
    text="rem",
    fill="#FFFFFF",
    font=("Quicksand Regular", 20 * -1)
)
canvas.tag_raise(remOneTxt)

pxOneTxt = canvas.create_text(
    480.0,
    304.0,
    anchor="nw",
    text="px",
    fill="#FFFFFF",
    font=("Quicksand Regular", 20 * -1)
)
canvas.tag_raise(pxOneTxt)