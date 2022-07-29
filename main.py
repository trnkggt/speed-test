import datetime
import random
from tkinter import *
from tkinter import ttk

times = []

## evrytime user writes anything in the main entry
## times list is appended with corresponding datetime
def create(event,*args):
    times.append(datetime.datetime.now())


### when user clicks enter, the text will be submitted
## accuracy, wpm will be calculated
## and corresponding labels will be updated
def print_time(event):
    finish = datetime.datetime.now()
    start = times[0]
    count = 0
    print((finish-start).total_seconds())

    for i, c in enumerate(sample_text.cget('text')):
        try:
            if c == vari.get()[i]:
                count += 1
        except:
            pass
    accuracy = (count*100)/len(sample_text.cget('text'))
    wpm = len(vari.get())*60/(5*((finish-start).total_seconds()))

    accuracy_label.config(text=f'Your accuracy is {round(accuracy)}',background='white')
    wpm_label.config(text=f'you can write {round(wpm)} words per minute',background='white')
###


## restart every info and label
def restart():
    global times
    times = []
    user_entry.delete(0,END)
    accuracy_label.config(text='')
    wpm_label.config(text='')
###

# get a new sentence from sentences.txt
def get_sentence():
    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    sample_text.config(text=sentence)
###


window = Tk()
window.title('Typing Test')
window.configure(background='blue',pady=15,padx=15)


welcome = ttk.Label(window,text='Welcome to the Typing Test',font='Bold 35')
welcome.grid(row=0,column=1,pady=15)


get_text = ttk.Button(window,text='Get Text',command=get_sentence)
get_text.grid(row=1,column=0,pady=15)

sample_text = ttk.Label(window,text='Hello my name is Tornike and i live in Tbilisi\n'
                                    'I am seventeen years old',font='Bold')
sample_text.grid(row=1,column=1,pady=15)


vari = StringVar()
user_entry = ttk.Entry(window,width=100,textvariable=vari)
user_entry.grid(row=3,column=1,pady=15)
vari.trace_add('write',create)

window.bind('<Return>',print_time)

accuracy_label = ttk.Label(window,text='',background='blue',font='Bold')
accuracy_label.grid(row=4,column=0,pady=15)

wpm_label = ttk.Label(window,text='',background='blue',font='Bold')
wpm_label.grid(row=5,column=0,pady=15)

restart = ttk.Button(window,text='restart',command=restart)
restart.grid(row=5,column=1,pady=15)


window.mainloop()