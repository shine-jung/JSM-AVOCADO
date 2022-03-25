import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

HEIGHT=720
WIDTH=1280
font=(40)

def onClick():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    df=pd.read_csv(root.filename)
    label=tk.Label(head, text=root.filename, fg='black', font=font)
    label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.5)
    
    tv1.delete(*tv1.get_children())
    tv1["column"]=list(df.columns)
    combo['values']=list(df.columns)
    combo3['values']=list(df.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows=df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
        
def onClick2():
    df=pd.read_csv(root.filename)
    if combo2.get()=='Search words':
        df1=df[df[combo.get()].str.contains(entry1.get())]
    if combo2.get()=='>':
        df1=df[df[combo.get()]>float(entry1.get())]
    if combo2.get()=='>=':
        df1=df[df[combo.get()]>=float(entry1.get())]
    if combo2.get()=='<':
        df1=df[df[combo.get()]<float(entry1.get())]
    if combo2.get()=='<=':
        df1=df[df[combo.get()]<=float(entry1.get())]
    if combo2.get()=='==':
        df1=df[df[combo.get()]==float(entry1.get())]
    if combo2.get()=='!=':
        df1=df[df[combo.get()]!=float(entry1.get())]
        
    label2=tk.Label(body, text=(combo.get()+" 열에서\n"+entry1.get()+"을(를) 필터링하였습니다."), fg='black', font=font)
    label2.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
    
    tv1.delete(*tv1.get_children())

    tv1["column"]=list(df1.columns)
    combo['values']=list(df1.columns)
    combo3['values']=list(df1.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows=df1.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
    
def onClick3():
    df=pd.read_csv(root.filename)
    label2=tk.Label(body, text="console", fg='black', font=font)
    label2.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
    tv1.delete(*tv1.get_children())
    tv1["column"]=list(df.columns)
    combo['values']=list(df.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows=df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
        
def onClick4():
    df=pd.read_csv(root.filename)
    if combo2.get()=='검색할 기능을 선택하세요.':
        df1=df
    if combo2.get()=='Search words':
        df1=df[df[combo.get()].str.contains(entry1.get())]
    if combo2.get()=='>':
        df1=df[df[combo.get()]>float(entry1.get())]
    if combo2.get()=='>=':
        df1=df[df[combo.get()]>=float(entry1.get())]
    if combo2.get()=='<':
        df1=df[df[combo.get()]<float(entry1.get())]
    if combo2.get()=='<=':
        df1=df[df[combo.get()]<=float(entry1.get())]
    if combo2.get()=='==':
        df1=df[df[combo.get()]==float(entry1.get())]
    if combo2.get()=='!=':
        df1=df[df[combo.get()]!=float(entry1.get())]
        
    label2=tk.Label(body, text=(combo3.get()+"을(를) 분석한 결과 입니다.\n\n"+str(df1[combo3.get()].describe())), fg='black', font=font)
    label2.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
    
    tv1.delete(*tv1.get_children())

    tv1["column"]=list(df1.columns)
    combo['values']=list(df1.columns)
    combo3['values']=list(df1.columns)
    tv1["show"]="headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows=df1.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)

root=tk.Tk()
root.wm_title("AVOCADO")

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

head=tk.Frame(root, bg='#558203', bd=10)
head.place(relx=0.5, rely=0.05, relwidth=0.95, relheight=0.2, anchor='n')

body=tk.Frame(root, bg='#f6df5b', bd=10)
body.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.65, anchor='n')

button1=tk.Button(head, text="csv 파일을 첨부하세요!", fg='gray', font=font, command=onClick)
button1.place(relx=0, rely=0, relwidth=0.2, relheight=0.5)

label=tk.Label(head, text="", fg='black', font=font)
label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.5)

reset_button=tk.Button(head, text="RESET", fg='gray', font=font, command=onClick3)
reset_button.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.5)

combo=ttk.Combobox(head, width=20, textvariable=str)
combo.place(relx=0, rely=0.5, relwidth=0.2, relheight=0.5)
combo['values'] = ('검색할 열을 선택하세요.', '')
combo.current(0)

combo2=ttk.Combobox(head, width=20, textvariable=str)
combo2.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.5)
combo2['values'] = ('검색할 기능을 선택하세요.','Search words', '>', '>=', '<', '<=', '==', '!=')
combo2.current(0)

entry1=tk.Entry(head, text="검색할 기능을 입력하세요.", fg='black', font=font)
entry1.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.5)

button2=tk.Button(head, text="Search", fg='gray', font=font, command=onClick2)
button2.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.5)

combo3=ttk.Combobox(head, width=20, textvariable=str)
combo3.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.5)
combo3['values'] = ('분석할 열을 선택하세요.', '')
combo3.current(0)

button3=tk.Button(head, text="분석", fg='gray', font=font, command=onClick4)
button3.place(relx=0.9, rely=0.5, relwidth=0.1, relheight=0.5)

tv1=ttk.Treeview(body)
tv1.place(relx=0, rely=0, relwidth=0.8, relheight=1)

label2=tk.Label(body, text="console", fg='black', font=font)
label2.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

treescrolly=tk.Scrollbar(tv1, orient="vertical", command=tv1.yview)
treescrollx=tk.Scrollbar(tv1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

root.mainloop()
