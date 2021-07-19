import tkinter
from tkinter import *
from tkinter import ttk
import time
import os

from tkinter.messagebox import askyesno

if os.path.exists("./account.txt")==False:
    f=open("account.txt","x")

if os.path.exists("./cash.txt")==False:
    f=open("cash.txt","a")
    f.write("0 0 0")

s=open("cash.txt","r")
d=list(map(int,s.read().split()))
if d==[]:
    s=open("cash.txt","w")
    s.write("0 0 0")
    d=[0,0,0]
root=Tk()
p1 = PhotoImage(file = 'money.png')
 
# Setting icon of master window
root.iconphoto(False, p1)
mainbg="#DCDBD9"
root.title("Personal-Money-Tracker")
df=Frame(root,bg=mainbg,borderwidth=3,relief="solid")
to=Label(df,text="TOTAL AMOUNT $$",font=("arial",30),bg=mainbg,fg="blue")
to.grid(row=0,column=0,padx=10,pady=10)
ams=[5993,1093,0]
to1=Label(df,text=str(d[0]+d[1]),font=("arial",30),bg=mainbg,fg="blue")
to1.grid(row=1,column=0,padx=10,pady=5)
to2=Label(df,text="MY BALANCE $$",font=("arial",30),bg=mainbg,fg="green")
to2.grid(row=2,column=0,padx=10,pady=10)
to3=Label(df,text=str(d[0]),font=("arial",30),bg=mainbg,fg="green")
to3.grid(row=3,column=0,padx=10,pady=5)
to4=Label(df,text="SHOP MONEY $$",font=("arial",30),bg=mainbg,fg="black")
to4.grid(row=4,column=0,padx=10,pady=10)
to5=Label(df,text=str(d[1]),font=("arial",30),bg=mainbg,fg="black")
to5.grid(row=5,column=0,padx=10,pady=5)
to6=Label(df,text="SPENDS $$",font=("arial",30),bg=mainbg,fg="red")
to6.grid(row=6,column=0,padx=10,pady=10)
to7=Label(df,text=str(d[2]),font=("arial",30),bg=mainbg,fg="red")
to7.grid(row=7,column=0,padx=10,pady=5)
sd=Frame(root)

ty=Label(sd,text="Type",font=("arial",20)).grid(row=0,column=0,pady=5)

what = ttk.Combobox(sd, width =27,height=20,font=15)


    
# Adding combobox drop down list
what['values'] = ('ACCOUNT',
                          'SHOP',
                          'SPENT')

what.grid(row=1,column=0)

def entr():
    global en,what,lis,to1,to3,to5,to7
    if os.path.exists("./cash.txt")==False:
        s=open("cash.txt","a")
        s.write("0 0 0")

    s=open("cash.txt","r")
    d=list(map(int,s.read().split()))
    if d==[]:
        s=open("cash.txt","w")
        s.write("0 0 0")
        d=[0,0,0]

    
    

    if en.get()!="":
        
        fs=open("account.txt","a")
        fs.write(en.get()+" "+what.get()+" "+str(time.asctime( time.localtime(time.time()) ))+ " \n")
        lis.insert(END,en.get()+" "+what.get()+" "+str(time.asctime( time.localtime(time.time()) ))+ " \n")
        if what.get()=="ACCOUNT":
            d[0]=int(d[0])+int(en.get())
        elif what.get()=="SHOP":
            d[1]=int(d[1])+int(en.get())
        elif what.get()=="SPENT":
            d[2]=int(d[2])+int(en.get())
            d[0]=d[0]-int(en.get())

        to1.config(text=str(d[0]+d[1]))
        to3.config(text=str(d[0]))
        to5.config(text=str(d[1]))
        to7.config(text=str(d[2]))
        g=open("cash.txt","w")
        g.write(str(d[0])+" "+str(d[1])+" "+str(d[2]))
    print(d)
        


ty=Label(sd,text="Amount",font=("arial",20)).grid(row=2,column=0,pady=5)
en=Entry(sd,width=29,font=20)
en.grid(row=3,column=0,pady=10)
fg=Button(sd,text="Enter",width=20,font=("arial",15),bg="#218B82",command=entr)
fg.grid(row=4,column=0,pady=5)
sd.grid(row=0,column=1,padx=10)
df.grid(row=0,column=0,padx=10)

sdf=open("account.txt","r")
def details():
    global jk,lis,dfs,Am1,Am2,Am3
    dfs.grid_forget()
    sds=lis.get(ANCHOR).split()
    dfs.config(borderwidth=5,relief="solid")
    times=" ".join(sds[2:])
    Am1.config(text="Amount: "+sds[0],font=15)
    Am2.config(text="On what: "+sds[1],font=15)
    Am3.config(text="When: "+times,font=15)
    dfs.grid(row=4,column=0,pady=10)

def dele():
    global jk,lis,dfs,Am1,Am2,Am3,to1,to3,to5,to7
    dfs.grid_forget()
    sds=lis.get(ANCHOR).split()
    
    times=" ".join(sds[2:])
    fgd=open("account.txt","r")
    dff=fgd.read().split("\n")
    nds=open("asd.txt","a")
    l=[]

    answer = askyesno(title='confirmation',message='Are you sure that you want to delete the entry?')
    flag=0
    if answer:
        flag=1

    if flag==0:
        return

    lis.delete(ANCHOR)
        
    if os.path.exists("./cash.txt")==False:
        s=open("cash.txt","a")
        s.write("0 0 0")

    s=open("cash.txt","r")
    d=list(map(int,s.read().split()))
    if d==[]:
        s=open("cash.txt","w")
        s.write("0 0 0")
        d=[0,0,0]
    if sds[1]=="ACCOUNT":
        d[0]-=int(sds[0])
    if sds[1]=="SHOP":
        d[1]-=int(sds[0])
    if sds[1]=="SPENT":
        d[0]+=int(sds[0])
        d[2]-=int(sds[0])

    to1.config(text=str(d[0]+d[1]))
    to3.config(text=str(d[0]))
    to5.config(text=str(d[1]))
    to7.config(text=str(d[2]))
    g=open("cash.txt","w")
    g.write(str(d[0])+" "+str(d[1])+" "+str(d[2]))
    

    fdx=open("account.txt","w")
    for i in dff:
        if i.split()[2:]!=sds[2:] and i.split()!=[]:
            fdx.write(i+"\n")
    fgd.close()
   
        

    
    
notes=sdf.read().split("\n")
jk=Frame(root,borderwidth=2,relief="solid")
ty=Label(jk,text="ENTRIES ",font=("arial",20)).grid(row=0,column=0,pady=5)
lis=Listbox(jk,height=8,width=40,font=10)
de=Button(jk,text="Details",width=20,font=("arial",15),bg="green",command=details)
de.grid(row=2,column=0,pady=5)
de=Button(jk,text="Delete",width=20,font=("arial",15),bg="red",command=dele)
de.grid(row=3,column=0,pady=5)
dfs=Frame(jk)
Am1=Label(dfs,text="")
Am1.grid(row=0,column=0)
Am2=Label(dfs,text="")
Am2.grid(row=1,column=0)
Am3=Label(dfs,text="")
Am3.grid(row=2,column=0)
dfs.grid(row=4,column=0)
for i in notes:
    if i!="":
        lis.insert(END,i)
lis.grid(row=1,column=0,pady=5,padx=10)
jk.grid(row=0,column=2)
root.mainloop()

