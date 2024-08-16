import tkinter as tk
def clk(value):
    crnt=entry.get('1.0',tk.END).strip()
    # crnt=entry.get()
    entry.delete('1.0',tk.END)
    # entry.delete(0,tk.END)
    entry.insert(tk.END,crnt + str(value))
def clr():
    entry.delete('1.0',tk.END)
def eqls():
    try:
        result=str(eval(entry.get('1.0',tk.END).strip()))
        entry.delete('2.0',tk.END)
        entry.insert(tk.END,f"\n={result}")
    except:
        entry.insert(tk.END,f"\nERROR")
root= tk.Tk()
# root.geometry('400x400')
root.title('calculator')
# entry=tk.Entry(root)
entry=tk.Text(root,width=30,height=3,font=10)
entry.grid(row=0,column=0,columnspan=4)
buttons=[
    ('9',2,0),('8',2,1),('9',2,2),('C',0,3),
    ('4',3,0),('5',3,1),('6',3,2),('=',2,3),
    ('1',4,0),('2',4,1),('3',4,2),('*',3,3),
    ('0',5,0),('.',5,1),('/',5,2),('-',4,3),
    ('+',5,3)
]
for (text,row,col) in buttons:
    if text =="C":
        btn=tk.Button(root,text=text,fg='white',bg='red',font=5,padx=8,pady=10,command=clr)
    elif text=="=":
        btn=tk.Button(root,text=text,fg='white',bg='green',font=('Arial',15,'bold'),padx=8,pady=10,command=eqls)
    else:    
        btn=tk.Button(root,text=text,font=5,padx=8,pady=10,bg='grey',fg='white',command=lambda t=text:clk(t))
    btn.grid(row=row,column=col,sticky='nsew')
root.mainloop()
# def bttn_clk(value):
#     crrnt=entry
