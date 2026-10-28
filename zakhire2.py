import time
'''
import pyscreeze
image1 = pyscreeze.screenshot("image1.png")
'''
# #in baraye screenshot ast
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
#dar ghesmat baad az ghesmat avalin tamrin mitoni tac tac amozesh haye in code ha ra bebini
time.sleep(2)
from tkinter import *
from tkinter import messagebox
def mass():
    messagebox.showinfo('iran eror' , 'in the iran')
app = Tk()
one_menu = Menu(app)
app.config(menu=one_menu)
filemenu = Menu(one_menu)
one_menu.add_cascade(label='in the iran code' , menu=filemenu)
filemenu.add_command(label='massagebox' , command = mass)
filemenu.add_cascade(label='Exite' , command=app.quit)
app.mainloop()
#baraye sakht ye lst dar tkinter
from time import *
from tkinter import *
from tkinter import messagebox
def mass():
    messagebox.showinfo('iran eror' , 'in the iran')
    sleep(1)
    messagebox.showwarning('iran eror2' , 'in the iran')
    sleep(1)
    messagebox.askquestion('iran eror2' , 'in the iran')
    sleep(1)
    messagebox.askokcancel('iran eror2' , 'in the iran')
    sleep(1)
    i = messagebox.askokcancel('iran eror2' , 'in the iran')
    print(i)
    sleep(5)
app = Tk()
one_menu = Menu(app)
app.config(menu=one_menu)
filemenu = Menu(one_menu)
one_menu.add_cascade(label='in the iran code' , menu=filemenu)
filemenu.add_command(label='massagebox' , command = mass)
filemenu.add_cascade(label='Exite' , command=app.quit)
app.mainloop()
#anvoee messagebox ha
sleep(2)
from tkinter import *
app = Tk()
app.title('matin ghadiriyan')
'esm barname'
app.geometry('200x600')
'andazeye barname'
app.iconbitmap('logo.ico')
'logoye barname'
app.resizable(True,False)
'mitoni begi mishe az arz bishtar ya kamtar kard vali az tool nemishavad'
app.mainloop()
#tanzimat ha va kar haii ke mitavan baraye sakhat in ha angham dad
sleep(2)
from tkinter import *
app = Tk()
app.geometry('500x500')
app.title('matin ghadiriyan app')
app.iconbitmap('nesh.ico')
label = Label(app, text='matin' , font=('Arial' , 20), background='red' ,foreground='black')
label.pack()
app.mainloop()
#kar ba ((label))
from tkinter import *
import time
def btn():
    print('Chack the button')
app = Tk()
btns = Button(app , text='Exite' , width=20 ,height=20 , command=btn , background='blue',foreground='red')
btns.pack()
app.mainloop()
#sakhte dokme ba tanzimat
""""
from tkinter import *
def get_name():
    label.config(app, text='hello' + entry.get())
app = Tk()
label = Label(app, text='Enter your name: ' , font=('Arial' , 20))
label.pack()
entry = Entry(app, width=50)
entry.pack()
btns = Button(app , text='ok' , width=10 ,height=2 , command=get_name)
btns.pack()
app.mainloop()
"""
from tkinter import *
app = Tk()
label = Label(app, text='Enter the name' , font=('Arial' , 20))
label.pack()
entry = Entry(app, font=('Arial' , 10))
entry.pack()
def name():
    label = Label(app, text=f'hello {entry.get()}' , font=('Arial' , 20))    
    label.pack()
btn = Button(
    text='Enter',
    background='red',
    foreground='blue',
    width=15,
    height=10,
    command=name
)
btn.pack()
app.mainloop()
#Entry
from tkinter import *
app = Tk()
app.geometry('800x800')
def chek():
    label = Label(app, text=f'{bolvar.get()}' , font=('Arial' , 20))        
    label.pack()
bolvar = BooleanVar()
checkbutto = Checkbutton(app , text='hello' , variable=bolvar)
checkbutto.pack()
btn = Button(
    text='Enter',
    width=15,
    height=10,
    background='black',
    foreground= 'red',
    command=chek
)
def defin():
    label1 = Label(app, text=bolva.get() , font=('Arial' , 20))
    label1.pack()
bolva = BooleanVar()
checkbutt = Checkbutton(app , text='hello', variable=bolva,command=defin)
checkbutt.pack()
btn.pack()
app.mainloop()
#((checkbox)) ha
from tkinter import *
app = Tk()
app.geometry('800x800')
var2 = IntVar()
radi = Radiobutton(app, text='Entaer the famili' , variable=var2 , value=1 , command=lambda: print(var2.get()))
radi.pack()
radi1 = Radiobutton(app, text='Entaer the famili' , variable=var2 , value=2 , command=lambda: print(var2.get()))
radi1.pack()
app.mainloop()
#((radiobutton))    dar Radiobutton faghat mitavan yek gozinaro faaol kard va beghaye booleaVar ma intVar ra mizarim
from tkinter import *
app = Tk()
app.geometry('600x600')

list = Listbox(app , selectmode= MULTIPLE)
list.insert(1, 'python')
list.insert(2, 'java')
list.insert(3, 'java script')
list.insert(4, 'css')
list.insert(5, 'datapast')
list.insert(6, 'android')
list.insert(7, 'viual studio code')
list.insert(8, 'vscode')
list.insert(9, 'site')
list.insert(10, 'datapast back end')
list.insert(11, 'window')
list.insert(12, 'c**')
list.insert(13, 'php')
list.insert(14, 'wordpres')
list.insert(15, 'luncher')
list.pack()
btn1 = Button(
    text='in the 1',
    background='red',
    foreground='white',
    command=lambda:print(list.curselection())
)
'''
on addady ke ava neveshte shode ra mitavan taratib ha ra mishakhas kard
'''
btn1.pack()
lis = Listbox(app , selectmode= MULTIPLE)
lis.insert(1, 'python')
lis.insert(2, 'java')
lis.insert(3, 'java script')
lis.insert(4, 'css')
lis.insert(5, 'datapast')
lis.pack()
def name_python():
    for i in lis.curselection():
        print(lis.get(i))
btn2 = Button(
    text='in the 2',
    background='red',
    foreground='white',
    command= name_python)
'''
baraye in ke beghaye tupel khodesh biyad
'''
btn2.pack()
app.mainloop()
#((listbox)) ha
from tkinter import *
app = Tk()
app.geometry('800x800')
btn1 = Button(app, text='click',background='red')
btn2 = Button(app, text='click1', background='blue')
btn3= Button(app, text='click2', background='black' , foreground='white')
btn4= Button(app, text='click3', background='green' , foreground='red')
btn1.pack(side=LEFT)
'''chap'''
btn2.pack(side=RIGHT)
'''rast'''
btn3.pack(side=TOP)
'''bala'''
btn4.pack(side=BOTTOM)
'''paiin'''
btn5= Button(app, text='click4', background='red' , foreground='green')
btn6= Button(app, text='click5', background='green' , foreground='blue')
btn7= Button(app, text='click6', background='yellow' , foreground='red')
btn8= Button(app, text='click7', background='green' , foreground='yellow')
btn9= Button(app, text='click8', background='green' , foreground='red')

btn5.pack(side=BOTTOM , fill=X)
btn6.pack(side=RIGHT , fill=Y)
btn7.pack(side=BOTTOM , fill=Y , expand=YES)
btn8.pack(side=BOTTOM , fill=X , expand=YES)
btn9.pack(side=BOTTOM )
'''agar ((fill)) ra behesh ((BOTH)) ra midahim kol safhe ra migirad'''
'''dar ((padx=i)) mitoni beghaye (i) ye addad beyari ke baees mishavad ke az chap va rast beteddad add fasele biofte'''
'''dar ((pady=i)) bra aks ((pad)) ast yaani az bala va paiin fasale miandazasd'''
'''nokte: y = soton va x = radif'''
app.mainloop()
#kar ba [pack()]
from tkinter import * 
from tkinter import ttk
app = Tk()
def comboboxss():
    print(combo.get())
app.geometry('800x800')
combo = ttk.Combobox(app, values=['python' , 'java' , "c++" , 'c#'])
combo.pack()
combo.bind("<<ComboboxSelected>>")
btn = Button(
    text='Enter',
    command=comboboxss
)
btn.pack()
app.mainloop()
#((combobox)) ha
from tkinter import * 
app = Tk()
app.geometry("800x800")
scale = Scale(app, from_=0 , to=100 , orient=HORIZONTAL)
scale.pack()
'''from_= yaani shoraa az on addadi ke behesh midim va to= ta addi ke hast va
orient= ham maalom mikonad ofoghi bashad ya aamodi va HORIZONTAL ofoghi ast va VERTICAL amodi'''
scale = Scale(app, from_=0 , to=100 , orient=VERTICAL)
scale.pack()
scale = Scale(app, from_=6, to=200 , orient=HORIZONTAL , command= lambda x: print(x))
'''
dar lambda har chizi beyne : va lambda benevisim be soran yek motoghayer dar tabbe ast
va andazash misavi ast be chis haye poshtash
'''
scale.pack()
def rang():
    print(scale1.get())
scale1 = Scale(app, from_=50 , to=10000 , orient=HORIZONTAL)
scale1.pack()
btn = Button(
    text='Enter range',
    command=rang
)
btn.pack()
app.mainloop()
#range ya scale ha
from tkinter import * 
app = Tk()
app.geometry("800x800")
label = Label(app, text='hello' , font=("Arial" , 20) , background='red' , foreground='black')
label.pack()
messag = Message(app, text='hello' , font=("Arial" , 20) , background='red' , foreground='black')
messag.pack()
'''dar message hamon label ast vali label matn hara to ye yek khat minevise
vali message shekastegi dare va baraye harf haye tolani mofide wa mitavan be on tol va aarz ham dad'''
app.mainloop()
#messag ha
from tkinter import *
from time import *
from tkinter import ttk
app = Tk()
app.geometry("800x800")
label = Label(app,text='hello' , font=('Arial' , 20) , background='red', foreground='black')
label.pack()
porgressbar = ttk.Progressbar(app , orient=VERTICAL)
'''((VERTICAL)) baraye amodi kardan ast'''
porgressbar.pack()
def nameha():
    for i in range(100):
        sleep(0.1)
        porgressbar["value"] = i
        app.update_idletasks()
btn = Button(
    text='click for start',
    background='red',
    foreground='black',
    command=nameha
)
btn.pack()
app.mainloop()
'''
progressbar ha nokte dar progressbar ha vaghti vared ttk mishavi nemitoni az backgroun va ... estefade
koni baya inghori tarif koni ((from tkinter import ttk)) va aval har metodi ke dar ttk bod yek ((.ttk)) bazari
'''
#porgressbar ha
from tkinter import *
app = Tk()
app.geometry("800x800")
spinbox = Spinbox(app, from_=0 , to=100 )
spinbox.pack()
'''from_=0 as va to=200 ta ra bayan mikonad ke masalan as 0 ta 200'''
text = Text(app, width=30 , height=30)
text.pack()
def Enter():
    print(spinbox.get() , text.get("5.0" , END))
    '''
    baraye text bayad maalom koni ke chi ro mikhaym bekhonim va
    bayad dakhel get() bayad dakhe "" begim 1.5 yaani line 1 va harf pangom
    va bayad badesh ham benevisi ((, END)) baraye in ke ta akhar print kone
    va baraye END ta a khar hameye horof mire
    '''
btn = Button(
    text='Enter',
    command=Enter
)
btn.pack()
app.mainloop()
#spinbox va text
from tkinter import *
from PIL import Image, ImageTk
app = Tk()
app.geometry("800x800")
img = Image.open('nesh.png')
img = img.resize((500,500))#baraye andaze bayad img ro be in sorat nevesht va bayad do ta () gozashr
imagtk = ImageTk.PhotoImage(img)
label = Label(app , image=imagtk)
label.pack(side=LEFT , fill=BOTH , expand=YES)#in ghori mire vasat
app.mainloop()
#ezafe kardan aaks
from tkinter import *
app = Tk()
label = Label(app, text='hello')
entry = Entry(app)
btn = Button(text='hello')
label.grid(row=0 , column=0)
entry.grid(row=0 , column=1)
btn.grid(row=50 , column=0 , sticky="ew")
'''radif = row va column = soton'''
'''dar sticky bayad begim shomal ghonob shargh gharb va W = chap va n = bala va s = paiin e = rast'''
'''to mitoni ba ((columspan=)) begi andazeye chand ta harf ghadval gha begire'''
app.mainloop()
#grid ya ghadval ha 
from tkinter import *
app = Tk()
btn = Button(
    app,
    text='hello',
    width=10,
    height=2,
    background='red',
    foreground='green',
    activebackground='light blue',
    activeforeground='black',
)
'''activeforeground va activebackground baraye in hastand ke
vaghti dokme ra zadim backgroundeshon va forgroundeshon che rangi shavad'''
entry = Entry(app , width=10 , background='red' , foreground='green' , selectbackground='light blue' , selectforeground='black')
'''selectbackground va selectforeground baraye in hastand ke 
vaghti toye entry entekhab kardim on entekhabemon backgroundeshon va forgroundeshon che rangi shavad'''
btn.pack()
entry.pack()
app.mainloop()
#selectbackground va selectforeground va activeforeground va activebackground
from tkinter import *
app = Tk()
def namea(eventa):
    print('y:', eventa.y , 'x:' , eventa.x)
app.bind("<Motion>" , namea)
'''inghori mogheiiyat mous ra neshan midhad(roye safheye tkinter)'''
'''va mitoni to ye print bezani((event.x)) ya ((event.y)) inghori
in hara ghoda mithe ya agar yekisho bedi ono mide va digar matn poshtash ra nemiavarad'''
def nameb(eventb):
    print(eventb.char)
    if eventb.char == 'q':
        app.quit()
app.bind("<KeyPress>" , nameb)
'''baraye ine ke betoni dokmeii ke korbar entekhab kard ra neshan midahad
va agar benevisi kenere event ya harchizi ((.char)) faghat on harf ro mifge'''
'''va mitoni benevisi vaghti q masalan click shod barneme ra bebande mesle if tabee (neamb)'''
app.mainloop()
#ertebat mous ba karbar
from tkinter import *
from time import *
app = Tk()
app.geometry("800x800")
label = Label(app , text='click ((n)) and go to the next widow!!!' , background='red', foreground='blue')
label.pack()
def K(event):
    if event.char == 'n':
        for i in range(100):
            Toplevel(app)
        '''baraye sakhte safheye ghadidva harchi ziresh biyad be onvan metod Toplevel hesab mishe'''
        '''va chon zir maghmoee ye app hast agar app baste shavad hame baste khohand shod'''
app.bind("<KeyPress>" , K)
app.mainloop()
#Toplevel ha
from tkinter import *
from webbrowser import *
app =Tk()
def click():
    open(entry.get() , new=0 , autoraise=True)
app.geometry('800x800')
label = Label(app , text='Enter the URL:' , font=("arial" , 20))
label.grid(row=0 , column=0)
entry = Entry(app, font=("Arial" , 20))
entry.grid(row=0 , column=1)
btn = Button(
    text="goooooo",
    font=("Arail" , 20),
    background='red',
    foreground='blue',
    activebackground='blue',
    activeforeground='red',
    command=click
)
btn.grid(row=1 , column=0 , sticky="ew" , columnspan=2 )
app.mainloop()
#braye in ke betoni beri to site dade shode
from tkinter import *
import csv
from tkinter import Message
app = Tk()
app.title('Excel')
app.iconbitmap('logo.ico')
app.geometry('500x300')
def btn_click():
    file = open('data.csv' , 'a' , newline='')
    w = csv.DictWriter(file, fieldnames=['fname' , 'iname' , 'gender'])
    with open('data.csv' , 'r' , newline='') as fr:
        if len(list(csv.DictReader(fr))) == 0:
            w.writeheader()
    w.writerow({'fname':fname.get() , 'iname':iname.get() , 'gender':gender.get()})
    file.close()
    get_data()
def get_data():
    file = open('data.csv' , 'r' , newline='')
    r = csv.DictReader(file)
    data = ''
    for row in r:
        data += f"{row['fname']} , {row['iname']} , {row['gender']}\n"
        mesagebox.config(text=data)
    file.close()
fnamelabel = Label(app , text="First name:", font=("Arial" , 20))
inamelabel = Label(app , text="last name:", font=("Arial" , 20))
fname = Entry(app, font=("Arial" , 20))
iname = Entry(app, font=("Arial" , 20))
gender = StringVar()
woman = Radiobutton(app , value='woman' , variable=gender , text='Woman')
man = Radiobutton(app , value='man' , variable=gender , text='Man')
'''in akhari ha beraye in bodend ke vaghti taghir kard biyad dakhel gender zakhire she'''
btn = Button(
    app,
    text='Register',
    background='red',
    command=btn_click
)
btn2 = Button(
    app,
    text='Get Data',
    background='red',
    command=get_data
)
mesagebox = Message(app, text='' , width=100)
fnamelabel.grid(row=0 , column=0)
fname.grid(row=0 , column=1)
inamelabel.grid(row=1 , column=0)
iname.grid(row=1 , column=1)
woman.grid(row=2 , column=0)
man.grid(row=2 , column=1)
btn.grid(row=3 , column=0 , columnspan=2 , sticky='ew')
btn2.grid(row=4 , column=0 , columnspan=2 , sticky='ew')
mesagebox.grid(row=5 , column=0 , columnspan=2 , sticky='ew')
app.mainloop()
#poroghe ye baadi
from bs4 import BeautifulSoup
'''bayad az ((bs4)) module ((Beautifulsoup4)) ra biavari'''
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
uy = '(in motoghayer baraye ghodaii va khana ii behtar ast tavaghoh nakonid)'
'''in gha code haye html ra miavarim'''
soup = BeautifulSoup(html_doc, 'html.parser')
'''ingha soup ra taarif mikoni'''
i = f"{soup.title.string}" , f"{soup.a}"
'''ingha migim ke chi ya print shavad masalan az soup (haman code haye html) titel va string yaani chiz haii ke dakhelesh hast ra biavar'''
print(i)
'''ingha ham print mikonim'''
#ashnaii ba beautifulsuop4
from bs4 import BeautifulSoup
import requests
amirhn = requests.get("https://google.com").content
'''in gha link ra midahim va vared an mishavim va bayad .content ra ham ezanim'''
soup = BeautifulSoup(amirhn, 'html.parser')
'''ingh code haye html ra az site migirim'''
i = soup.title.string
'''ingh migim chi mikhaym va dar khat baad printesh mikonim'''
print(i)
print(soup.find_all('a'))
'''ingha ye list miyare va hameye tag haye ((a)) ra miavarad'''
for link in soup.find_all('a'):
    print(link) 
'''ingha ye halghe tarif kardim ke khat be khat miyad hershoi toye tag ((a)) dakhel site googl.com bod ra miavarad va khat be khat neshan midahad'''
#rafan be site vagheii
from bs4 import BeautifulSoup
import requests
amirhn = requests.get("https://naei.ir/python/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A7%D8%B2-%D8%B5%D9%81%D8%B1-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86").content
'''link site ra midahim'''
soup = BeautifulSoup(amirhn, 'html.parser')
'''baraye in ke begim chi ro mikhaym bayad ro ye on chizi ke mikhaym rast
click bokonim va baad an class ya code html ra dar code hayeman gharar dahin'''
print(soup.find_all('del' , {'class':'price-toman'})[0].string)
'''ingha migi onhaii ke del hastan va classeshon (prce-toman) ast
ra biavard va in ham begam del ra be sorat dic miavarad pas bayad begi ke item 0 ra mikham'''
#gereftan an chiz haii ke mikhaihm
from bs4 import BeautifulSoup
import requests
amirhn = requests.get("https://amirhn.ir/products").content
soup = BeautifulSoup(amirhn, 'html.parser')
for t in soup.find_all('h3' , {'class':'course-title'}):
    '''ingha migim ke on tag haaii ke in vighegi ro daran bere
    printteshon bokone va chon dar halghe ast hamashon ro miavarad'''
    print(t.string)
from bs4 import BeautifulSoup
import requests
amirhn = requests.get("https://amirhn.ir/products").content
soup = BeautifulSoup(amirhn, 'html.parser')
print(soup.find('a').parent.parent.parent)
'''ingha migim ke bere maasalan on a dokhel tag d ast in gha migim ke bere on
tag div ro biyare va mitovan in ra ta vaghti digar to dar to nabashe ham edame dad'''
from bs4 import BeautifulSoup
import requests
amirhn = requests.get("https://amirhn.ir/products").content
soup = BeautifulSoup(amirhn, 'html.parser')
'''mitoni dar find find benevisi ta betoni toy on code ke html on
site ra gerefte dobare dar on begardi [find baraye gashtane!!]'''
streain = soup.find(string='مشاوره رایگان').parent
'''ingha mige ke boro on tagi ke tosh neveshte moshavere ye raygan ro peyda kon'''
print(streain)
'''ingha ham mige begard donball on tag h3 iee ke on neveshte dakheleshe va mige printesh kon'''
#bardashtan tag ha bedone id ya class
from selenium import webdriver
import time
wb = webdriver.Chrome()
'''ingha miyad ba mororgar bazesh mikone'''
wb.get('https://amirhn.ir/')
time.sleep(3)
wb.close()
'''va in gha mibandatehsh'''
#baz kardan web ba python
from selenium import webdriver
from bs4 import BeautifulSoup
wb = webdriver.Chrome()
wb.get('https://amirhn.ir/')
htmlcode = wb.page_source
print(wb.page_source)
'''ingha age eshtebah nakonam code hasho gerefte'''
wb.close()
soup = BeautifulSoup(htmlcode , 'html.parser')
print('.................................................................................................................................................................................')
'''ingha htmlcode robehesh dadim va dar paiin title ra gereftim'''
print(soup.title.string)
#gereftan code html ba in module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('https://naei.ir//products')
e = driver.find_element(By.CSS_SELECTOR , 'h3.cours-title')
print(e)
action = ActionChains(driver)
action.move_to_element(e).perform
driver.close()
#click kardan roye site(moshkel darad)
pass
pass
#ghesmat haye 44 ta gheyre ham bebin(age khasti)