from tkinter import *

# Initialize the main window
window = Tk()
window.title("Calculator")
window.geometry("400x500")

# String variable to hold the calculator input/output
fn1 = StringVar()
 
# Function to clear the input
def delete():
    fn1.set("")

# Function to append character to the input
def append(character):
    current_text = fn1.get()
    fn1.set(current_text + character)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(fn1.get())
        fn1.set(result)
    except:
        fn1.set("Error")

# Labels and entry fields
l1 = Label(window, text="CALCULATOR", fg="black", bg="white", font=("arial", 19, "bold"))
l1.place(x=120, y=10)
en = Entry(window, textvariable=fn1, width=30, font=("arial", 14), bd=4)
en.place(x=30, y=50)

# Buttons for the calculator
b1 = Button(window, text='C', command=delete, bg="black", fg="white", border=4, width=5)
b2 = Button(window, text='+', command=lambda: append('+'), bg="black", fg="white", border=4, width=5)
b3 = Button(window, text='-', command=lambda: append('-'), bg="black", fg="white", border=4, width=5)
b4 = Button(window, text='*', command=lambda: append('*'), bg="black", fg="white", border=4, width=5)
b5 = Button(window, text='/', command=lambda: append('/'), bg="black", fg="white", border=4, width=5)
b6 = Button(window, text='%', command=lambda: append('%'), bg="black", fg="white", border=4, width=5)
b7 = Button(window, text='1', command=lambda: append('1'), bg="black", fg="white", border=4, width=5)
b8 = Button(window, text='2', command=lambda: append('2'), bg="black", fg="white", border=4, width=5)
b9 = Button(window, text='3', command=lambda: append('3'), bg="black", fg="white", border=4, width=5)
b10 = Button(window, text='4', command=lambda: append('4'), bg="black", fg="white", border=4, width=5)
b11 = Button(window, text='5', command=lambda: append('5'), bg="black", fg="white", border=4, width=5)
b12 = Button(window, text='6', command=lambda: append('6'), bg="black", fg="white", border=4, width=5)
b13 = Button(window, text='7', command=lambda: append('7'), bg="black", fg="white", border=4, width=5)
b14 = Button(window, text='8', command=lambda: append('8'), bg="black", fg="white", border=4, width=5)
b15 = Button(window, text='9', command=lambda: append('9'), bg="black", fg="white", border=4, width=5)
b16 = Button(window, text='0', command=lambda: append('0'), bg="black", fg="white", border=4, width=5)
b17 = Button(window, text='.', command=lambda: append('.'), bg="black", fg="white", border=4, width=5)
b18 = Button(window, text='=', command=evaluate, bg="black", fg="white", border=4, width=5)

# Placing buttons using grid
b1.place(x=40, y=100)
b2.place(x=120, y=100)
b3.place(x=200, y=100)
b4.place(x=280, y=100)

b7.place(x=40, y=170)
b8.place(x=120, y=170)
b9.place(x=200, y=170)
b10.place(x=280, y=170)

b11.place(x=40, y=240)
b12.place(x=120, y=240)
b13.place(x=200, y=240)
b14.place(x=280, y=240)

b15.place(x=40, y=310)
b16.place(x=120, y=310)
b17.place(x=200, y=310)
b18.place(x=280, y=310)

b5.place(x=40, y=380)
b6.place(x=280, y=380)

window.mainloop()
