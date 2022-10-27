import tkinter as tk
from tkinter import ttk
import datetime
import random

letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
'''
boy name	girl name	last name	place	shop or business	food	animal	adjective	total
'''

w = tk.Tk()
w['bg'] = '#ffffff'
w.minsize(width=200, height=50)
w.resizable = False
w.title('categories')

t = tk.StringVar()
t.set('Time')

cats = [1, 2, 3, 4, 5, 6, 7, 8]
ents = []

time_finish = False

def start():
    global start_time, spb
    for x in ents:
        x.delete(0, tk.END)
    start_time = datetime.datetime.today()
    ll['text']=letter

    spb = ttk.Button(tf, text='Stop', command=stop)
    spb.grid(padx=3, pady=3, column=3, row=0, sticky='e')

    sb.grid_remove()

    w.update_idletasks()
    w.after(100,update_time)

def start2():
    global start_time2, t1
    start_time2 = datetime.datetime.today()
    ll['text'] = letter
    t1=te.get()
    te.grid_remove()
    w.update_idletasks()
    w.after(100, time_left)

def update_time():
    global end_time, time_taken
    if not time_finish:
        now = datetime.datetime.today()
        t.set(str(now - start_time).split('.')[0])
        w.update_idletasks()
        w.after(100,update_time)
    else:
        end_time = datetime.datetime.today()
        time_taken = end_time - start_time


def time_left():
    now = datetime.datetime.today()
    a = str(time_taken-(now - start_time2)).split('.')[0]
    t.set(a)
    w.update_idletasks()
    if a == '0:00:00':
        stop2()
    else:
        w.after(100, time_left)

def mkte():
    global te
    te = tk.Entry(total)
    te.grid(padx=0, pady=0, column=0, row=2, sticky='ew')

def stop():
    global time_finish, sb2
    time_finish = True
    t.set('Time')
    ll['text'] = 'Letter'
    for x in ents:
        x.delete(0, tk.END)
    spb.grid_remove()
    sb2 = ttk.Button(tf, text='Start', command=start2)
    sb2.grid(padx=3, pady=3, column=2, row=0, sticky='e')
    mkte()
    w.update_idletasks()

def stop2():
    for x in ents:
        x['state'] = tk.DISABLED
    ttl = ttk.Label(total, text=str(t1), relief=tk.SOLID, borderwidth=1, background='#ffffff', width=10, anchor=tk.CENTER)
    ttl.grid(padx=3, pady=3, column=0, row=1, sticky='ew')
    te.grid()

tf = tk.Frame(w, padx=0, pady=0, bg='#ffffff')
#tf.grid(column=0, row=1, padx=0, pady=0, sticky='nsew')



ll = ttk.Label(tf, text='Letter', relief=tk.SOLID, borderwidth=1, background='#ffffff', width=6, anchor=tk.CENTER)
ll.grid(padx=3, pady=3, column=1, row=0, sticky='e')

tl = ttk.Label(tf, textvariable=t, relief=tk.SOLID, borderwidth=1, background='#ffffff', width=10, anchor=tk.CENTER)
tl.grid(padx=3, pady=3, column=0, row=0, sticky='e')

sb = ttk.Button(tf, text='Start', command=start)
sb.grid(padx=3, pady=3, column=2, row=0, sticky='e')

f = tk.Frame(w, relief=tk.SOLID, padx=0, pady=0, bg='#ffffff', bd=1)
f.grid(column=0, row=2, padx=0, pady=0, sticky='nsew')

cats[0] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[0].grid(column=0, row=0, padx=0, pady=0, sticky='nsew')
l0 = tk.Label(cats[0], text='Boy Name', bg='#ffffff')
l0.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[1] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[1].grid(column=1, row=0, padx=0, pady=0, sticky='nsew')
l1 = tk.Label(cats[1], text='Girl Name', bg='#ffffff')
l1.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[2] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[2].grid(column=2, row=0, padx=0, pady=0, sticky='nsew')
l2 = tk.Label(cats[2], text='Last Name', bg='#ffffff')
l2.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[3] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[3].grid(column=3, row=0, padx=0, pady=0, sticky='nsew')
l3 = tk.Label(cats[3], text='Place', bg='#ffffff')
l3.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[4] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[4].grid(column=4, row=0, padx=0, pady=0, sticky='nsew')
l4 = tk.Label(cats[4], text='Shop/Business', bg='#ffffff')
l4.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[5] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[5].grid(column=5, row=0, padx=0, pady=0, sticky='nsew')
l5 = tk.Label(cats[5], text='Food', bg='#ffffff')
l5.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[6] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[6].grid(column=6, row=0, padx=0, pady=0, sticky='nsew')
l6 = tk.Label(cats[6], text='Animal', bg='#ffffff')
l6.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

cats[7] = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
cats[7].grid(column=7, row=0, padx=0, pady=0, sticky='nsew')
l7 = tk.Label(cats[7], text='Adjective', bg='#ffffff')
l7.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

total = tk.Frame(f, relief=tk.SOLID, padx=3, pady=3, bg='#ffffff', bd=1)
total.grid(column=8, row=0, padx=0, pady=0, sticky='nsew')
l8 = tk.Label(total, text='Total', bg='#ffffff')
l8.grid(padx=0, pady=0, column=0, row=0, sticky='nsew')

mkte()

for x, item in enumerate(cats):
    ents.append(tk.Entry(item))
    ents[x].grid(padx=0, pady=0, column=0, row=1, sticky='ew')

w.mainloop()
