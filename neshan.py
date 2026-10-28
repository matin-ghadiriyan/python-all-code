
print ("square")
p = int(input("what is a side: "))
print (p  *  p)
print("rectangle")
g = int(input("what is a side: "))
p = int(input("what is a length: "))
if (g < p):
    print (g    *    p)
else:print("eror the sid")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
max = 0
if a > max:
    max = a
if b > max:
    max = b
if c > max:
    c = max
print(max)
try:

    class mashin_hesab:

        def __init__(self , add_1 , add_2):

            self . add_1 = add_1

            self .add_2 = add_2

    hh = int(input('add1:'))

    nf = int(input('add2:'))


    sel = mashin_hesab(hh , nf)

    i = int(input('1 = zarb   2 = taghsim   3 = gham   4 = menha: '))


    if i == 1:

        def a(a , b):

            return a * b

        a = a(sel.add_1 , sel.add_2)

        print(a)

    if i == 2:

        def b(k , l):

                return k / l

        b = b(sel.add_1 , sel.add_2)

        print(b)

    if i == 3:

        def g(s , d):

            return s + d

        g = g(sel.add_1 , sel.add_2)

        print(g)

    if i == 4:

        def k(bb , ll):

            return bb - ll

        k = k(sel.add_1 , sel.add_2)

        print(k)

except ValueError:
 
    print('shoma add vared nakardid bayad as aval shoro konid')
import random
g = random.randint(1,100)
while True:
    i = int(input('add shansit chiye?: '))
    if i == g:
        print('dorost gofti')
        break

    if g > i:
        print("bishtar")
    else:
        print("kamtar")
        from tkinter import *
from webbrowser import *
from tkinter import messagebox
app =Tk()
def com():
    if entry.get() == 0:
        messagebox.INFO('write the name site!!' , 'you must the write the name site')
    else:
        open(f"https://{entry.get()}.com" , new=0 , autoraise=True)
def ir():
    if entry.get() == 0:
        messagebox.INFO('write the name site!!' , 'you must the write the name site')
    else:
        open(f"https://{entry.get()}.ir" , new=0 , autoraise=True)
app.geometry('480x200')
label = Label(app , text='Enter the URL:' , font=("arial" , 20) , background='red' , foreground='blue')
label.grid(row=0 , column=0)
entry = Entry(app, font=("Arial" , 20))
entry.grid(row=0 , column=1)
btn = Button(
    text=".com",
    font=("Arail" , 20),
    background='red',
    foreground='blue',
    activebackground='blue',
    activeforeground='red',
    command=com
    )
btn2 = Button(
    text=".ir",
    font=("Arail" , 20),
    background='red',
    foreground='blue',
    activebackground='blue',
    activeforeground='red',
    command=ir
    )
btn3 = Button(
    text='Exite for the apliction',
    font=("Arail" , 20),
    background='red',
    foreground='blue',
    activebackground='blue',
    activeforeground='red',
    command=app.quit
)
app.title('site in the google')
app.iconbitmap('site in the google.ico')
btn.grid(row=1 , column=0 , sticky="ew" , columnspan=2 )
btn2.grid(row=2 , column=0 , sticky="ew" , columnspan=2)
btn3.grid(row=3 , column=0 , sticky="ew"  , columnspan=2)
app.mainloop()