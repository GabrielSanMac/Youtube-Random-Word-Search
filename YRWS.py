import os
import random
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk

#Get Words From Link
response = requests.get('https://www.dicio.com.br/lista-de-palavras/')
soup = BeautifulSoup(response.text, 'lxml')
subject = []
tags = soup.find_all('a')
for tag in tags:
	subject.append(tag.text)

#Atributes
color_bg = '#121212'
font_ = 'calibri 11'
element_fg = '#BB86FC'
color_fg = '#e1e1e6'

#Screen
root = Tk()
root.geometry('600x300')
root.resizable(height=False, width=False)
root.title('Web Random')
root.config(bg=color_bg)

#vars
URL = ''
WORD = ''

#Functions
def GetWord():
	global WORD
	word = random.choice(subject)
	WORD = word
	GetUrl(word)

def GetUrl(word):
	global URL
	#plataform = combo.get()
	#if plataform == 'Youtube':
	URL = f'https://www.youtube.com/results?search_query={word}'

def Search():
	os.system(f'start {URL}')

def Reflesh():
	GetWord()
	print_Word.config(text=WORD)
	print_url.config(text=URL)

#Objects
label_Word = Label(root, text='WORD', fg=color_fg, bg=color_bg, font=font_)
print_Word = Label(root, text=WORD, fg=element_fg, bg=color_bg, font=font_)
label_url = Label(root, text='URL', fg=color_fg, bg=color_bg, font=font_)
print_url = Label(root, text=URL, fg=element_fg, bg=color_bg, font=font_)
btnSearch = Button(root, text='Search', command=Search, fg=color_fg, bg=color_bg, font=font_, bd=0)
btnReflesh = Button(root, text='reflesh', command=Reflesh, fg=color_fg, bg=color_bg, font=font_, bd=0)
#combo = ttk.Combobox(root, value=['Youtube'])
#combo.current(0)

#render
label_Word.place(x=10,y=10)
print_Word.place(x=60,y=10)
label_url.place(x=10,y=40)
print_url.place(x=60,y=40)
btnSearch.place(x=540,y=260)
btnReflesh.place(x=10,y=260)
#combo.place(x=10,y=10)

#runtime
GetWord()
Reflesh()

root.mainloop()