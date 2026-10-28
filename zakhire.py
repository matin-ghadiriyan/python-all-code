num = 0
while num < 20:
    print((num),"_matin") 
    num= num +1
print("end matin and number")
for i in range(10):
    print(i)
print("end the number 1 for 10")
for i in range(10):
    if i == 6:
        break
    print(i)
for i in range(10):
    if i == 8:
        continue
    print (i)
for i in range(20):
    if i == (1 and 5 and 10 and 6 and 19):
        continue
    print(i)
for i in range(20):
    if i == 9:
        break
    print(i)
for i in range(10):
    print(i)
    pass
for i in range(19):
    for l in range(10):
        print(l , i)
if i == 1234:
    print("matin")
if i == 5555:
    print("ali")
if i == 9999:
    print("mahdi")
else:
    print("its not user name")
students = ["matin" , "qoodosi" , "jafari"]
print(type (students))
print(students[0:1])
if 'main' in students:
    print("yes")
else:
    print("no")
print('qoodoi' in students)
print('qoodos' in students)
students[0] = 'mohamad matin'
print(students)
students [0:2] = ['matin' , 'reza']
print(students)
students.append('ghadiriyan') and ('hosin') and ('amir mohamad')
print(students)
students.remove('matin')
students.pop(1)
print(students)
students.sort()
print(students)
students.sort(reverse = True)
students2 = students.copy()
students2.append('matin')
print(students)
print(students2)
students2 = ['ali' , 'hasan']
print(students  + students2)
s = [123 , 125 ,222 ,255]
for len in s:
    print(len)
h = [2 , 5484 , 47 , 55 , 65]
nors = []
for hel in h:
    if hel > 20:
        nors.append
        if  []:
            continue
        print(nors , hel)
s = [123 , 125 ,222 ,255]
xx = [ hh for hh in s if hh > 200]
print(xx)
h = [123 , 125 ,222 ,255]
gg = [ dd for dd in h if dd > 200]
print(gg)
l = [1 , 2 ,3 , 4]
f = {1 , 2 ,3 , 4}
h = (1 , 2 ,3 , 4)
n = {'name':'matin' , 'age':11 , 'city':'tehran'}
print(l)
print(f)
print(h)
print(n)
print(n['name'])
n['name'] = 'matin ghadiriyan'
print(n['name'])
print(n)


try:
    num = input('num: ')
    num = int(num)

    print(num*2)
except TypeError:
    print('error')
    print('shoma bayad add ra vared konid na kalame')
except ValueError:
    pass
except:
    print()

else:
    print('else')

finally:
    print('end')
num = input('num: ')
num = int(num)

if num > 10:
    raise Exception('eror add shoma balatar az 10e')
          #to mitoni beghayte in eror ham benevisi
print(num)
def welcom():
    for i in range(10):
        print('welcom')
welcom()
welcom()
welcom()
def welcom(name):
    print('welcom' , name)
    if name == 'hooshang':
       print('welcom')

welcom('nima')
welcom('mahsa')
welcom('amir')
welcom('hooshang')
def welcom(age , name , city):

    print('welcom' , name)
    

    print('shahr' , city)


welcom('nima' , 20 , 'mashha')
def sum(a , b):
    return a + b

res = sum(sum(2 , 5) , 6)
print(res)
def sum(*a):
    print(a)

res = sum(2 , 5) 
print(res)
def sum(*a):
    s = 0
    for i in a:
        s += i
        return s

    res = sum(1,3,5,7)
    print(res) 

def print_user(**a):
    for i in a:
        print(i , a[i])

print_user(fname= 'amir' , lastname= 'neasj' , age = 12)
ll = input('')

class UserAcont:

    def __init__(self , user_name , pass_word , full_name):

       self.user_name = user_name 

       self.pass_word =pass_word 

       self.full_name=full_name

h1 = UserAcont('hooshang' , '12345' , 'hooshang@gmail.com')

h2 = UserAcont('mohamad' , '57572' , 'mohamad@gmail.com')

h3 = UserAcont('ali' , '56465' , 'ali@gmail.com')
class UserAcont:

    def __init__(self , user_name , pass_word , full_name):

       self.user_name = user_name 

       self.pass_word =pass_word 

       self.full_name=full_name

    def p(self):
        print(self.full_name , self.pass_word , self.user_name)
h1 = UserAcont('hooshang' , '12345' , 'hooshang@gmail.com')

h2 = UserAcont('mohamad' , '57572' , 'mohamad@gmail.com')

h3 = UserAcont('ali' , '56465' , 'ali@gmail.com')
h3.p()


i = (input('user_name: '))

d = (input('name: '))

h = (input('full_name: '))

k = (input('password: '))

class user_name:
    def __init__(self , user_name , name , full_name , password):
            self .user_name = i
            self.name = d
            self.full_name = h
            self.password = k

print('in baraye in ast ke sabet shavad shoma robat nistid')

n = (input('user_name: '))

l = (input('name: '))

b = (input('full_name: '))

g = (input('password: '))

if n == i and l == d and b == h and k == g:
    print('shoma varede barname shodid')

if (n == i) == False\
or (l == d) == False\
or (b == h) == False \
or (k == g) == False:
    raise Exception('user shoma ghalat ast')

vb = int(input('1 = didan ketab   2 = neveshtan ketab 3 = kharegh shodan as user   4 = didan user:  '))

class book:
    def __init__(book_def , didan_ketab , nevashtan_ketab , khareg_shodan_as_user , didan_user):
            
        book_def . didan_ketab = vb
            
        book_def . neveshtan_ketab  = vb
            
        book_def . khareg_shodan_as_user = vb
        
        book_def . didan_user = vb

if vb == 3:
    raise Exception('user shoma baste shod')

if vb == 2:
    print('ketabat ra bene vis')

    gg = input('')

vb = int(input('1 = didan ketab       2 = didan user:  '))



if vb == 1 :
    print(gg)

vb = int(input(' 2 = didan user:  '))

if vb == 2:
    print('  user_name =' + i , '  name =' + d , 'full_name =' + h , '  password =' + k)
class person:
    def __init__(self , name , code_meli , ):
        self . name = name
        self . code_meli = code_meli

    def chek_code_meli(self):
            return self.code_meli.isdigit()
        
class student(person):
     def __init__(self, name, code_meli , code_daneshamozi):
          super().__init__(name , code_meli)
          self . code_daneshgoii = code_daneshamozi

st = student('amir' , '0020000' ,'980000')
print(st.chek_code_meli())
print(st.name)
print(st.code_meli)
print(st.code_daneshgoii)
class person:
    def __init__(self , name , code_meli , ):
        self . name = name
        self . code_meli = code_meli

    def chek_code_meli(self):
            return self.code_meli.isdigit()
    def info(self):
         return f'name:{self.name} code_meli:{self.code_meli}'
class student(person):
     def __init__(self, name, code_meli , code_daneshamozi):
          super().__init__(name , code_meli)
          self . code_daneshgoii = code_daneshamozi

          self.name

          super().chek_code_meli()
     def info(self):
            return f'{super().info()} code_daneshamozi{self.code_daneshgoii}'

#         return f'name:{self.name} code_meli:{self.code_meli} code_daneshamozi:{self.code_daneshgoii}' ghalate chon code nabayad tekrar shavad   dry   dont ripit your code

st = student('amir' , '0020000' ,'980000')
print(st.chek_code_meli())
print(st.name)
print(st.code_meli)
print(st.code_daneshgoii)
print(st.info())
from time import sleep
i = (1763213183 / 60)
a = (i / 60)
g = (a / 24)
h = (g / 365)
print(h)
sleep(2)
print('end')
import time 
print(time.time())
import time 
print(time.ctime(1763381253.8838797))
import time 
print('start')
time.sleep(1)
print('end')
from time import sleep
print('matin')
sleep(1)
print('ali')
from time import *
print('matin')
sleep(1)
print('ali')
print(ctime(time()))
import random
print(random.randint(1,100))

import time 
import threading
def t1():
    time.sleep(1)
    print('t1')
def t2():
    time.sleep(4)
    print('t2')

thread1 = threading.Thread(target=t1)
thread2 = threading.Thread(target=t2)
print('start')
thread1.start()
thread2.start()
print('end')

import time 
import threading
def t1(name):
    time.sleep(1)
    print('t1')
def t2(name):
    time.sleep(4)
    print('t2')

thread1 = threading.Thread(target=t1 , args=('matin' ,))
thread2 = threading.Thread(target=t2 , args=('mohamad' ,))
print('start')
thread1.start()
thread2.start()
print('end')

import tkinter
from tkinter import messagebox
def ali():
    messagebox.showinfo('404' , 'dost daram eror betham')
Window = tkinter.Tk()
Window.geometry('700x600')

greeting = tkinter.Label(text='matin')

botton = tkinter.Button(
    text = 'click me!',
    width=12,
    height=20,
    bg='black',
    fg='red',
    command=ali
)
botton.pack()

greeting.pack()

Window.mainloop()
try:

    import time
    import random
    g = random.randint(1,100)
    while True:
        i = int(input('add shansit chiye?: '))
        if i == g:
            print('add ', g ,' bod')
            print('dorost gofti')
            time.sleep(9)
            print(g)
            break
            
        if g > i:
            print("bishtar")
        else:
            print("kamtar")
except ValueError:
    print('bayad add var mi kardi')
    import tkinter as tk
import random
randomnumber = random.randint(1,100)
app = tk.Tk()
app.title('play')
app.geometry('500x400')
label = tk.Label(app, text='play', font=('Arial', 24))
label.pack()
entry = tk.Entry(font=('Arial' , 24))
entry.pack()
entry = int()
i = ""
if entry == randomnumber:
    i = 'win'
if entry < randomnumber:
    i = 'up'
if entry > randomnumber:
    i = 'down'
btn = tk.Button(app,text='click to number',font=('Arial' , 24),command=lambda: label.config(text=i))
btn.pack()
app.mainloop()