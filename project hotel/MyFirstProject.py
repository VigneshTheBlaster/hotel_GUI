from tkinter import *
from datetime import date,datetime
import string
import time
import calendar
import mysql.connector as mysqli
import smtplib
from pygame import mixer
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
global sc,con,t1,t2,t3,t4,t5,t6,t7,t8
mixer.init()
sc=Tk()
sc.config(bg="red")
sc.iconbitmap(r"C:\Users\vignesh\icon.ico")
sc.title("MY First Project")
sc.attributes("-fullscreen",True)
sc.attributes("-transparentcolor","blue")
sc.attributes("-alpha","0.8")
imgg=Image.open(r"C:\Users\vignesh\Downloads\backward.png")
resi=imgg.resize((50,50))
pi=ImageTk.PhotoImage(resi)
imgg1=Image.open(r"C:\Users\vignesh\Downloads\play-button.png")
resi1=imgg1.resize((50,50))
pi1=ImageTk.PhotoImage(resi1)
imgg2=Image.open(r"C:\Users\vignesh\Downloads\forward.png")
resi2=imgg2.resize((50,50))
pi2=ImageTk.PhotoImage(resi2)
imgg3=Image.open(r"C:\Users\vignesh\Downloads\pause.png")
resi3=imgg3.resize((50,50))
pi3=ImageTk.PhotoImage(resi3)
igm=Image.open(r"C:\Users\vignesh\Downloads\ganesh.png")
igm1=igm.resize((300,300))
igm2=ImageTk.PhotoImage(igm1)
igm8=Image.open(r"C:\Users\vignesh\Downloads\hotel.png")
igm9=igm8.resize((600,150))
igm10=ImageTk.PhotoImage(igm9)
t1=False
t2=False
t3=False
t4=False
t5=False
t6=False
t7=False
t8=False
global stru,tot,weeks
to=date.today()
con=mysqli.connect(host="localhost",user="root",password="",database="test")
to=date.today()
weeks=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
tot=str(to.day)+"-"+str(to.month)+"-"+str(to.year)+"("+weeks[to.weekday()]+")"
strp=time.strftime('%I %M %S %p',time.localtime())
stru=str(strp[0])+str(strp[1])+":"+str(strp[3])+str(strp[4])+":"+str(strp[6])+str(strp[7])+" "+str(strp[9])+str(strp[10])
n=0
nn=0
yy=0
xx=0
mm=0
hmm=0
kkk=0
uuu=0
ttt=0
pr=StringVar()
pr1=StringVar()
def pending():
   delforsearch()
   delforbill()
   global ttt,con,stru,tot,vt,pr,t8,pr1
   if ttt==0:
      delforsearch()
      delforbill()
      global vt,r1,r2,tad,etry1,etry2,lb11,t5,r4,con
      t5=True
      def dell():
         if r1.get()!="" and r2.get()!="":
               xxx=con.cursor()
               xxx.execute("SELECT * FROM pendingit")
               otp=xxx.fetchall()
               if any(i[1]==r1.get() for i in otp):
                  xxx.execute("DELETE FROM pendingit WHERE names='%s'"%r1.get())
                  con.commit()
                  cl()
                  udt()
                  clr()
               else:
                  messagebox.showinfo("INSERT","CUSTOMER NOT EXITS")
      def cl():
         tree=vt.get_children()
         for x in tree:
            vt.delete(x)
      def clr():
         etry1.delete(0,END)
         etry2.delete(0,END)
         etry3.delete(0,END)
      def up():
          if r1.get()!="" and r2.get()!="":
               xxx=con.cursor()
               xxx.execute("SELECT * FROM pendingit")
               otp=xxx.fetchall()
               if any(i[1]==r1.get() for i in otp):
                  xxx.execute("UPDATE pendingit SET names=%s,price=%s,items=%s WHERE names=%s",(r1.get(),r2.get(),r4.get(),r1.get()))
                  con.commit()
                  cl()
                  udt()
                  clr()
               else:
                  messagebox.showinfo("UPDATE","CUSTOMER NOT EXITS")
      def godata(event):
         global itms,r4
         itms=vt.item(vt.focus())
         if itms['tags']!='':
            r1.set(itms['values'][0])
            r2.set(itms['values'][2])
            r4.set(itms['values'][1])
      def new():
         vv1=list(r1.get())
         vv2=list(r2.get())
         vv3=r4.get()
         if (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1) or any(ii=="-" for ii in vv1)) or (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1)) and r1.get()!="" and r2.get()!="":
            if any(j in string.ascii_lowercase or j in string.ascii_uppercase for j in vv2) or r1.get()=="" or r2.get()=="":
               messagebox.showinfo("warning","ENTER CORRECTLY")
            else:
               g1=list(r1.get())
               g1[0]=g1[0].upper()
               g11=""
               for i in range(len(g1)):
                  if i==0:
                     g1[0]=g1[0].upper()
                  else:
                     g1[i]=g1[i].lower()
                  g11+=g1[i]
               g2=int(r2.get())
               xxx=con.cursor()
               xxx.execute("SELECT * FROM pendingit")
               otp=xxx.fetchall()
               if not any(i[1]==g11 for i in otp):
                  du=con.cursor()
                  du.execute("""INSERT INTO pendingit (names,items,price,date,time) VALUES(%s,%s,%s,%s,%s)""",(g11,vv3,g2,tot,stru))
                  con.commit()
                  cl()
                  udt()
               else:
                  messagebox.showinfo("INSERT","CUSTOMER ALREADY EXITS")
               clr()
         else:
            messagebox.showinfo("warning","ENTER CORRECTLY")
      sty=ttk.Style()
      sty.configure("vicky.Treeview.Heading",font=("Times 20"))
      sty.configure("vicky.Treeview",font=("Times 15"))
      lb11=LabelFrame(sc,text="PENDING_SECTION",width=1260,height=600,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
      lb11.place(x=10,y=100)
      vt=ttk.Treeview(lb11,columns=(0,1,2,3,4),style="vicky.Treeview",show="headings",height=11)
      vt.bind("<Double 1>",godata)
      tadd=con.cursor()
      tadd.execute("SELECT * FROM pendingit")
      tad=tadd.fetchall()
      vt.column(0,width=255,anchor="center")
      vt.column(1,width=450,anchor="w")
      vt.column(2,width=210,anchor="center")
      vt.column(3,width=170,anchor="w")
      vt.column(4,width=150,anchor="w")
      vt.heading(0,text="CUSTOMER-NAMES",anchor="center")
      vt.heading(1,text="ITEMS",anchor="center")
      vt.heading(2,text="PENDING-PRICE",anchor="w")
      vt.heading(3,text="DATE",anchor="center")
      vt.heading(4,text="TIME",anchor="center")
      def udt():
         global udd,ud
         ud=con.cursor()
         ud.execute("""SELECT names,items,price,date,time FROM pendingit ORDER BY names""")
         udd=ud.fetchall()
         po=0
         for i in udd:
            if po%2==0:
               vt.insert("",END,values=[""])
               vt.insert("",END,values=i,tags=('even'))
               po+=1
            else:
               vt.insert("",END,values=[""])
               vt.insert("",END,values=i,tags=('odd'))
               po+=1
            vt.tag_configure('even',background="#ECECEC")
            vt.tag_configure('odd',background="white")
      udt()
      vt.tag_configure('even',background="#EEEEEE")
      vt.tag_configure('odd',background="white")
      vt.place(x=6,y=0)
      yscrol=Scrollbar(lb11,orient="vertical",command=vt.yview)
      vt.config(yscroll=yscrol.set)
      yscrol.place(x=1227,y=12,height=230)
      ln1=Label(lb11,text="CUSTOMER-NAME:",font="Times 18 bold",bg="red")
      ln1.place(x=50,y=290)
      r1=StringVar()
      r2=StringVar()
      r4=StringVar()
      etry1=Entry(lb11,textvariable=r1,font="Times 23 bold",bg="pink",fg="brown",width=10,bd=6,justify="center")
      etry1.place(x=290,y=280)
      ln3=Label(lb11,text="ITEMS:",font="Times 20 bold",bg="red")
      ln3.place(x=520,y=290)
      etry3=Entry(lb11,textvariable=r4,font="Times 23 bold",bg="pink",fg="brown",width=10,bd=6,justify="center")
      etry3.place(x=630,y=280)
      ln2=Label(lb11,text="PENDING-MONEY:",font="Times 18 bold",bg="red")
      ln2.place(x=866,y=290)
      etry2=Entry(lb11,textvariable=r2,font="Times 23 bold",bg="pink",fg="brown",width=5,bd=6,justify="center")
      etry2.place(x=1100,y=280)
      Button(lb11,text="UPDATE",font="Times 15 bold",bg="pink",bd=8,width=9,activebackground="blue",command=up).place(x=100,y=390)
      Button(lb11,text="ADD-NEW",font="Times 15 bold",bg="pink",bd=8,width=9,activebackground="blue",command=new).place(x=530,y=390)
      Button(lb11,text="DELETE",font="Times 15 bold",bg="pink",bd=8,width=9,activebackground="blue",command=dell).place(x=900,y=390)
      uuu=1
      if pr.get()!='0' and t8==True and pr.get()!='':
         r2.set(pr.get())
         r4.set(pr1.get())
         pr.set("")
         pr1.set("")
         t8=False
   else:
      pass
def update():
   global uuu,con,r3,r6
   if uuu==0:
      delforsearch()
      delforbill()
      global vt,r1,r2,tad,etry1,etry2,lb11,t5,udd,ud,r3
      t5=True
      def clr():
         etry1.delete(0,END)
         etry2.delete(0,END)
         r6.set("")
      def dell():
         global r3
         if r1.get()!="" and r2.get()!="" and r3!=0 and r6!="":
             duds=con.cursor()
             duds.execute("DELETE FROM ngkmass WHERE id="+r3)
             con.commit()
             cl()
             udt()
             clr()
      def up():
         global r3
         vv1=list(r1.get())
         vv2=list(r2.get())
         r11=""
         r12=r2.get()
         if (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1) or any(ii=="-" for ii in vv1)) or (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1)) and r1.get()!="" and r2.get()!="":
            if any(j in string.ascii_lowercase or j in string.ascii_uppercase for j in vv2) or r1.get()=="" or r2.get()=="" or r6.get()=="":
               messagebox.showinfo("warning","ENTER CORRECTLY")
            else:
               for i in range(len(vv1)):
                  if i==0:
                     vv1[0]=vv1[0].upper()
                  else:
                     vv1[i]=vv1[i].lower()
                  r11+=vv1[i]
               dud=con.cursor()
               if r3!=0:
                  dud.execute("""UPDATE ngkmass SET items=%s , price=%s , category=%s WHERE id=%s""",(r11,r12,r6.get(),r3))
                  con.commit()
                  cl()
                  udt()
         else:
             messagebox.showinfo("warning","ENTER CORRECTLY")
         clr()
      def godata(event):
         global itms,r3,r6
         r3=0
         itms=vt.item(vt.focus())
         if itms['tags']!='':
            r1.set(itms['values'][1])
            r2.set(itms['values'][2])
            r3=str(itms['values'][0])
            r6.set(itms['values'][3])
      def new():
         vv1=list(r1.get())
         vv2=list(r2.get())
         if (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1) or any(ii=="-" for ii in vv1)) or (all(i in string.ascii_lowercase or i in string.ascii_uppercase for i in vv1)) and r1.get()!="" and r2.get()!="":
            if any(j in string.ascii_lowercase or j in string.ascii_uppercase for j in vv2) or r1.get()=="" or r2.get()=="" or r6.get()=="":
               messagebox.showinfo("warning","ENTER CORRECTLY")
            else:
               g1=list(r1.get())
               g1[0]=g1[0].upper()
               g11=""
               for i in range(len(g1)):
                  if i==0:
                     g1[0]=g1[0].upper()
                  else:
                     g1[i]=g1[i].lower()
                  g11+=g1[i]
               g2=int(r2.get())
               if not any(i[1]==g11 for i in udd):
                  du=con.cursor()
                  du.execute("""INSERT INTO ngkmass (id,items,category,price) VALUES(NULL,%s,%s,%s)""",(g11,r6.get(),g2))
                  con.commit()
                  cl()
                  udt()
               else:
                  messagebox.showinfo("INSERT","ITEM ALREADY EXITS")
               clr()
         else:
            messagebox.showinfo("warning","ENTER CORRECTLY")
      sty=ttk.Style()
      sty.configure("vicky.Treeview.Heading",font=("Times 20"))
      sty.configure("vicky.Treeview",font=("Times 15"))
      lb11=LabelFrame(sc,text="UPDATE_SECTION",width=837,height=600,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
      lb11.place(x=200,y=100)
      vt=ttk.Treeview(lb11,columns=(0,1,2),style="vicky.Treeview",show="headings",height=11)
      vt.bind("<Double 1>",godata)
      vt.column(0,width=80,anchor="center")
      vt.column(1,width=520,anchor="center")
      vt.column(2,anchor="center")
      vt.heading(0,text="ID-NO",anchor="center")
      vt.heading(1,text="ITEMS",anchor="center")
      vt.heading(2,text="PRICE",anchor="center")
      def udt():
         global udd,ud
         ud=con.cursor()
         ud.execute("""SELECT id,items,price,category FROM ngkmass ORDER BY items""")
         udd=ud.fetchall()
         po=0
         for i in udd:
            if po%2==0:
               vt.insert("",END,values=[""])
               vt.insert("",END,values=i,tags=('even'))
               po+=1
            else:
               vt.insert("",END,values=[""])
               vt.insert("",END,values=i,tags=('odd'))
               po+=1
            vt.tag_configure('even',background="#ECECEC")
            vt.tag_configure('odd',background="white")
      udt()
      def cl():
         tree=vt.get_children()
         for x in tree:
            vt.delete(x)
      vt.place(x=12,y=0)
      yscrol=Scrollbar(lb11,orient="vertical",command=vt.yview)
      vt.config(yscroll=yscrol.set)
      yscrol.place(x=798,y=12,height=230)
      ln1=Label(lb11,text="ITEM-NAME:",font="Times 18 bold",bg="red")
      ln1.place(x=20,y=290)
      r1=StringVar()
      r2=StringVar()
      etry1=Entry(lb11,textvariable=r1,font="Times 23 bold",bg="pink",fg="brown",width=10,bd=6,justify="center")
      etry1.place(x=190,y=280)
      ln2=Label(lb11,text="PRICE:",font="Times 18 bold",bg="red")
      ln2.place(x=420,y=290)
      etry2=Entry(lb11,textvariable=r2,font="Times 23 bold",bg="pink",fg="brown",width=5,bd=6,justify="center")
      etry2.place(x=520,y=280)
      r6=StringVar()
      cb1=ttk.Combobox(lb11,textvariable=r6,font="Times 20 bold",width=9,justify="center",state="readonly")
      cb1.place(x=665,y=285,height=40)
      val24=["VEG","NON-VEG","OTHERS"]
      cb1['values']=val24
      Button(lb11,text="UPDATE",font="Times 15 bold",bg="yellow",bd=8,width=9,activebackground="pink",command=up).place(x=70,y=390)
      Button(lb11,text="ADD-NEW",font="Times 15 bold",bg="yellow",bd=8,width=9,activebackground="pink",command=new).place(x=350,y=390)
      Button(lb11,text="DELETE",font="Times 15 bold",bg="yellow",bd=8,width=9,activebackground="pink",command=dell).place(x=620,y=390)
      uuu=1
   else:
      pass
def getdata():
    global lb9,xx,t3,t4,lb10,hmm,kkk,uy,idd,con,weeks,strrr,strrr1,strrr2
    vv1=list(ts.get())
    styu=ttk.Style()
    styu.configure("vick.Treeview.Heading",font=("Times 20"),highlightthickness=30)
    styu.configure("vick.Treeview",borderwidth=10,font=("Times 15"),highlightthickness=30,background="black",foreground="white")
    idd=ts.get()
    if xx==1:
        f=st.get()
        f22=list(mon.get())
        f2=""
        for i in f22:
           if (not i in string.ascii_lowercase) and (not i in string.ascii_uppercase) and i!='-':
              f2+=i
        f3=era.get()
        if f!="DATE" and mon.get()!="MONTH" and f3!="YEAR":
            if kkk==1:
                if t3==True:
                   lb9.destroy()
                t3=True
                ltu=list(mon.get())
                gf=""
                for i in ltu:
                   if i=='-':
                      break
                   else:
                      gf+=i
                dta=f+' '+gf+' '+f3
                bor=datetime.strptime(dta,'%d %m %Y').weekday()
                dtaa=f+'-'+gf+'-'+f3+'('+weeks[bor]+')'
                strr2=con.cursor()
                strr2.execute(""" SELECT id,items,price,date,time FROM custome WHERE date='%s' """%dtaa)
                strrr2=strr2.fetchall()
                lb9=LabelFrame(sc,text=f+"/"+f2+"/"+f3,width=1200,height=300,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb9.place(x=32,y=200)
                tv=ttk.Treeview(lb9,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=11)
                tv.column(1,width=480,anchor="w")
                tv.column(0,width=100,anchor="w")
                tv.column(2,anchor="n")
                tv.heading(0,text="ID-NO",anchor="center")
                tv.heading(1,text="ITEMS",anchor="center")
                tv.heading(2,text="PRICE",anchor="center")
                tv.heading(3,text="DATE",anchor="center")
                tv.heading(4,text="TIME",anchor="center")
                ht=['','','','','']
                tyt=0
                for i in strrr2:
                   tv.insert("",END,values=i)
                   tv.insert("",END,values=ht,tags=('even'))
                   tyt+=int(i[2])
                tyt1=["","TOTAL:"+str(tyt),"","",""]
                tv.insert("",END,values=tyt1)
                tv.tag_configure('even',background="white")
                tv.place(x=4,y=0)
                yscrol=Scrollbar(lb9,orient="vertical",command=tv.yview)
                tv.config(yscroll=yscrol.set)
                yscrol.place(x=1170,y=12,height=230)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                t3=True
            else:
                if t3==True:
                   lb9.destroy()
                t3=True
                ltu=list(mon.get())
                gf=""
                for i in ltu:
                   if i=='-':
                      break
                   else:
                      gf+=i
                dta=f+' '+gf+' '+f3
                bor=datetime.strptime(dta,'%d %m %Y').weekday()
                dtaa=f+'-'+gf+'-'+f3+'('+weeks[bor]+')'
                strr3=con.cursor()
                strr3.execute(""" SELECT id,items,price,date,time FROM custome WHERE date='%s' """%dtaa)
                strrr3=strr3.fetchall()
                lb9=LabelFrame(sc,text=f+"/"+f2+"/"+f3,width=1200,height=300,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb9.place(x=32,y=200)
                tv=ttk.Treeview(lb9,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=11)
                tv.column(1,width=480,anchor="w")
                tv.column(0,width=100,anchor="w")
                tv.column(2,anchor="n")
                tv.heading(0,text="ID-NO",anchor="center")
                tv.heading(1,text="ITEMS",anchor="center")
                tv.heading(2,text="PRICE",anchor="center")
                tv.heading(3,text="DATE",anchor="center")
                tv.heading(4,text="TIME",anchor="center")
                ht=['','','','','']
                tyt=0
                for i in strrr3:
                   tv.insert("",END,values=i)
                   tv.insert("",END,values=ht,tags=('even'))
                   tyt+=int(i[2])
                tyt1=["","TOTAL:"+str(tyt),"","",""]
                tv.insert("",END,values=tyt1)
                tv.tag_configure('even',background="white")
                tv.place(x=4,y=0)
                yscrol=Scrollbar(lb9,orient="vertical",command=tv.yview)
                tv.config(yscroll=yscrol.set)
                yscrol.place(x=1170,y=12,height=230)
                kkk=1
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
        elif idd=="" and (f=="DATE" or mon.get()=="MONTH" or era.get()=="YEAR"):
           if f=="DATE":
              messagebox.showinfo("ENTER","PLEASE ENTER DATE")
           elif mon.get()=="MONTH":
              messagebox.showinfo("ENTER","PLEASE ENTER MONTH")
           else:
              messagebox.showinfo("ENTER","PLEASE ENTER YEAR")
        else:
           pass
        if idd!="" and not any(i in string.ascii_lowercase or i in string.ascii_uppercase or i in string.punctuation for i in vv1):
            if hmm==1:
                lb10.destroy()
                lb10=LabelFrame(sc,text="ID.NO:"+str(idd),width=1200,height=200,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb10.place(x=32,y=500)
                tv2=ttk.Treeview(lb10,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=6)
                viip=con.cursor()
                viip.execute(""" SELECT id,items,price,date,time FROM custome WHERE id='%s' """%idd)
                vip6=viip.fetchall()
                tv2.column(1,width=480,anchor="w")
                tv2.column(0,width=100,anchor="w")
                tv2.column(2,anchor="n")
                tv2.heading(0,text="ID-NO",anchor="center")
                tv2.heading(1,text="ITEMS",anchor="center")
                tv2.heading(2,text="PRICE",anchor="center")
                tv2.heading(3,text="DATE",anchor="center")
                tv2.heading(4,text="TIME",anchor="center")
                if len(vip6)==1:
                   tv2.insert("",END,values=vip6[0])
                else:
                   tv2.insert("",END,values=["","NO ID MATCHED","","","",""])
                tv2.place(x=4,y=0)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                t4=True
            else:
                lb10=LabelFrame(sc,text="ID.NO:"+str(idd),width=1200,height=200,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb10.place(x=32,y=500)
                tv2=ttk.Treeview(lb10,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=6)
                vvip=con.cursor()
                vvip.execute(""" SELECT id,items,price,date,time FROM custome WHERE id='%s' """%idd)
                vip4=vvip.fetchall()
                tv2.column(1,width=480,anchor="w")
                tv2.column(0,width=100,anchor="w")
                tv2.column(2,anchor="n")
                tv2.heading(0,text="ID-NO",anchor="center")
                tv2.heading(1,text="ITEMS",anchor="center")
                tv2.heading(2,text="PRICE",anchor="center")
                tv2.heading(3,text="DATE",anchor="center")
                tv2.heading(4,text="TIME",anchor="center")
                if len(vip4)==1:
                   tv2.insert("",END,values=vip4[0])
                else:
                   tv2.insert("",END,values=["","NO ID MATCHED","","","",""])
                tv2.place(x=4,y=0)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                hmm=1
                t4=True
       
        else:
           if idd!="":
              messagebox.showinfo("warning","ID NUMBER SHOULD BE ENTER INTEGER")
    else:
        f=st.get()
        f22=list(mon.get())
        f2=""
        for i in f22:
           if (not i in string.ascii_lowercase) and (not i in string.ascii_uppercase) and i!='-':
              f2+=i
        f3=era.get()
        if f!="DATE" and mon.get()!="MONTH" and f3!="YEAR":
            if kkk==1:
                if t3==True:
                   lb9.destroy()
                t3=True
                ltu=list(mon.get())
                gf=""
                for i in ltu:
                   if i=='-':
                      break
                   else:
                      gf+=i
                dta=f+' '+gf+' '+f3
                bor=datetime.strptime(dta,'%d %m %Y').weekday()
                dtaa=f+'-'+gf+'-'+f3+'('+weeks[bor]+')'
                strr1=con.cursor()
                strr1.execute(""" SELECT id,items,price,date,time FROM custome WHERE date='%s' """%dtaa)
                strrr1=strr1.fetchall()
                lb9=LabelFrame(sc,text=f+"/"+f2+"/"+f3,width=1200,height=300,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb9.place(x=32,y=200)
                lb9=LabelFrame(sc,text=f+"/"+f2+"/"+f3,width=1200,height=300,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb9.place(x=32,y=200)
                tv=ttk.Treeview(lb9,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=11)
                tv.column(1,width=480,anchor="w")
                tv.column(0,width=100,anchor="w")
                tv.column(2,anchor="n")
                tv.heading(0,text="ID-NO",anchor="center")
                tv.heading(1,text="ITEMS",anchor="center")
                tv.heading(2,text="PRICE",anchor="center")
                tv.heading(3,text="DATE",anchor="center")
                tv.heading(4,text="TIME",anchor="center")
                ht=['','','','','']
                tyt=0
                for i in strrr1:
                   tv.insert("",END,values=i)
                   tv.insert("",END,values=ht,tags=('even'))
                   tyt+=int(i[2])
                tyt1=["","TOTAL:"+str(tyt),"","",""]
                tv.insert("",END,values=tyt1)
                tv.tag_configure('even',background="white")
                tv.place(x=4,y=0)
                yscrol=Scrollbar(lb9,orient="vertical",command=tv.yview)
                tv.config(yscroll=yscrol.set)
                yscrol.place(x=1170,y=12,height=230)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                xx=1
            else:
                if t3==True:
                   lb9.destroy()
                t3=True
                ltu=list(mon.get())
                gf=""
                for i in ltu:
                   if i=='-':
                      break
                   else:
                      gf+=i
                dta=f+' '+gf+' '+f3
                bor=datetime.strptime(dta,'%d %m %Y').weekday()
                dtaa=f+'-'+gf+'-'+f3+'('+weeks[bor]+')'
                strr=con.cursor()
                strr.execute(""" SELECT id,items,price,date,time FROM custome WHERE date='%s' """%dtaa)
                strrr=strr.fetchall()
                lb9=LabelFrame(sc,text=f+"/"+f2+"/"+f3,width=1200,height=300,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb9.place(x=32,y=200)
                tv=ttk.Treeview(lb9,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=11)
                tv.column(1,width=480,anchor="w")
                tv.column(2,anchor="n")
                tv.column(0,width=100,anchor="w")
                tv.heading(0,text="ID-NO",anchor="center")
                tv.heading(1,text="ITEMS",anchor="center")
                tv.heading(2,text="PRICE",anchor="center")
                tv.heading(3,text="DATE",anchor="center")
                tv.heading(4,text="TIME",anchor="center")
                ht=["","","","",""]
                tyt=0
                for i in strrr:
                   tv.insert("",END,values=i)
                   tv.insert("",END,values=ht,tags=('even'))
                   tyt+=int(i[2])
                tyt1=["","TOTAL:"+str(tyt),"","",""]
                tv.insert("",END,values=tyt1)
                tv.tag_configure('even',background="white")
                tv.place(x=4,y=0)
                yscrol=Scrollbar(lb9,orient="vertical",command=tv.yview)
                tv.config(yscroll=yscrol.set)
                yscrol.place(x=1170,y=12,height=230)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                xx=1
                kkk=1
        elif idd=="" and (f=="DATE" or mon.get()=="MONTH" or era.get()=="YEAR"):
           if f=="DATE":
              messagebox.showinfo("ENTER","PLEASE ENTER DATE")
           elif mon.get()=="MONTH":
              messagebox.showinfo("ENTER","PLEASE ENTER MONTH")
           else:
              messagebox.showinfo("ENTER","PLEASE ENTER YEAR")
        else:
           pass
        if idd!="" and not any(i in string.ascii_lowercase or i in string.ascii_uppercase or i in string.punctuation for i in vv1):
            if hmm==1:
                lb10.destroy()
                vipp=con.cursor()
                vipp.execute(""" SELECT id,items,price,date,time FROM custome WHERE id='%s' """%idd)
                vip2=vipp.fetchall()
                lb10=LabelFrame(sc,text="ID.NO:"+str(idd),width=1200,height=200,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb10.place(x=32,y=500)
                tv2=ttk.Treeview(lb10,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=6)
                tv2.column(1,width=480,anchor="w")
                tv2.column(0,width=100,anchor="w")
                tv2.column(2,anchor="n")
                tv2.heading(0,text="ID-NO",anchor="center")
                tv2.heading(1,text="ITEMS",anchor="center")
                tv2.heading(2,text="PRICE",anchor="center")
                tv2.heading(3,text="DATE",anchor="center")
                tv2.heading(4,text="TIME",anchor="center")
                if len(vip2)==1:
                   tv2.insert("",END,values=vip2[0])
                else:
                   tv2.insert("",END,values=["","NO ID MATCHED","","","",""])
                tv2.place(x=4,y=0)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                xx=1
                t4=True
            else:
                vip=con.cursor()
                vip.execute(""" SELECT id,items,price,date,time FROM custome WHERE id='%s' """%idd)
                vip1=vip.fetchall()
                lb10=LabelFrame(sc,text="ID.NO:"+str(idd),width=1200,height=200,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
                lb10.place(x=32,y=500)
                tv2=ttk.Treeview(lb10,columns=(0,1,2,3,4),style="vick.Treeview",show="headings",height=6)
                tv2.column(1,width=480,anchor="w")
                tv2.column(0,width=100,anchor="w")
                tv2.column(2,anchor="n")
                tv2.heading(0,text="ID-NO",anchor="center")
                tv2.heading(1,text="ITEMS",anchor="center")
                tv2.heading(2,text="PRICE",anchor="center")
                tv2.heading(3,text="DATE",anchor="center")
                tv2.heading(4,text="TIME",anchor="center")
                if len(vip1)==1:
                   tv2.insert("",END,values=vip1[0])
                else:
                   tv2.insert("",END,values=["","NO ID MATCHED","","","",""])
                tv2.place(x=4,y=0)
                st.set("DATE")
                mon.set("MONTH")
                era.set("YEAR")
                hmm=1
                xx=1
                t4=True
        else:
           if idd!="":
              messagebox.showinfo("warning","ID NUMBER SHOULD BE ENTER INTEGER")
    ts.set("")
    g=list(str(iden.get()))
    ar=list(range(0,10))
    for j in range(10):
        ar[j]=str(ar[j])
    if all(i in ar for i in g):
            jo=""
            for j in g:
                jo+=j
def delforsearch():
    global nn,t5,uuu,t4,uy
    nn=0
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    bl1.destroy()
    if t5==True:
       lb11.destroy()
       t5=False
       uuu=0
    if(t4==True):
        lb10.destroy()
        t4=False
def delforbill():
    global t3,mm,t4,t2,t5,uuu,uy,lb9
    mm=0
    if t2==True:
        srf.destroy()
        t2=False
    if(t3==True):
        lb9.destroy()
        t3=False
    if(t4==True):
        lb10.destroy()
        t4=False
    if t5==True:
       lb11.destroy()
       t5=False
       uuu=0

def me1():
   global t8,pending
   t8=True
   pending()
def billing():
    global nn,lb1,lb2,lb3,yy,t1,bl1,sc,fa,pi,pi1,pi2,pi3,btt,t7,pay,itrid,st1,et1,price1,intall,pending,pr,me1,items1,con,tot,stru,uyy,uyy1,jk
    t1=True
    ytt=[]
    jk=[]
    def pay(event):
          global jk
          jk.clear()
          uyy=[]
          uyy1=[]
          for i in range(len(itrid)):
             if(itrid[i].get()!=''):
                kk=int(itrid[i].get())
                uyy.append(kk*int(price1[i]))
                oi=str(items1[i]+'-'+str(kk))
                uyy1.append(oi)
                jk.append(oi)
             else:
                uyy.append(0)
          intall.set(sum(uyy))
          pr.set(str(intall.get()))
          uri=""
          for i in range(len(uyy1)):
             if i<len(uyy1)-1:
                uri=uri+uyy1[i]+','
             else:
                uri+=uyy1[i]
          pr1.set(uri)
    def pay2():
          global uyy1,jk
          jk.clear()
          uyy=[]
          uyy1=[]
          for i in range(len(itrid)):
             if(itrid[i].get()!=''):
                kk=int(itrid[i].get())
                uyy.append(kk*int(price1[i]))
                oi=str(items1[i]+'-'+str(kk))
                uyy1.append(oi)
                jk.append(oi)
             else:
                uyy.append(0)
          intall.set(sum(uyy))
          pr.set(str(intall.get()))
          uri=""
          for i in range(len(uyy1)):
             if i<len(uyy1)-1:
                uri=uri+uyy1[i]+','
             else:
                uri+=uyy1[i]
          pr1.set(uri)
    def pay1():
       global itrid,uyy1,jk
       if intall.get()!="" and intall.get()!='0' :
          if not intall.get() in string.ascii_lowercase and not intall.get() in string.ascii_uppercase and not intall.get() in string.punctuation:
             uri=""
             for i in range(len(jk)):
                if i<len(jk)-1:
                   uri=uri+jk[i]+','
                else:
                   uri+=jk[i]
             tre=con.cursor()
             tre.execute("""INSERT INTO custome(items,price,date,time) VALUES(%s,%s,%s,%s) """,(uri,intall.get(),tot,stru))
             con.commit()
             jk.clear()
             for i in range(len(itrid)):
                itrid[i].set("")
             intall.set("")
          else:
             messagebox.showinfo("AMOUNT","INCORRECT AMOUNT")
       else:
             pay2()
             if intall.get()!="" and intall.get()!='0':
                if not intall.get() in string.ascii_lowercase and not intall.get() in string.ascii_uppercase and not intall.get() in string.punctuation:
                   return True
             else:
                messagebox.showinfo("AMOUNT","EMPTY AMOUNT")
    if nn==0:
        ud=con.cursor()
        ud.execute("""SELECT items,price FROM ngkmass WHERE category='%s' """%'VEG')
        udd=ud.fetchall()
        udi=con.cursor()
        udi.execute("""SELECT id FROM ngkmass""")
        uddi=udi.fetchall()
        ud1=con.cursor()
        ud1.execute("""SELECT items,price FROM ngkmass WHERE category='%s' """%'NON-VEG')
        udd1=ud1.fetchall()
        ud2=con.cursor()
        ud2.execute("""SELECT items,price FROM ngkmass WHERE category='%s' """%'OTHERS')
        udd2=ud2.fetchall()
        bl1=LabelFrame(sc,width=1250,height=73,bg="red",bd=6,font="Times 25 bold")
        bl1.place(x=20,y=100)
        Label(bl1,text="DATE:"+tot,font="Times 22 bold",bg="red").place(x=5,y=12)
        LabelFrame(bl1,width=6,height=61,bg="red",bd=6,font="Times 25 bold").place(x=385,y=0)
        Button(bl1,image=pi,bg='red',relief='flat',activebackground='red').place(x=440,y=3)
        def play():
           global bg,btt,t7
           if t7==False:
               mixer.music.load(r"C:\Users\vignesh\Downloads\kannu.mp3")
               mixer.music.play()
               btt['image']=pi3
               t7=True
           else:
              btt['image']=pi1
              mixer.music.stop()
              t7=False
        if t7==False:
           btt=Button(bl1,image=pi1,bg='red',relief='flat',activebackground='red',command=play)
           btt.place(x=540,y=3)
        else:
           btt=Button(bl1,image=pi3,bg='red',relief='flat',activebackground='red',command=play)
           btt.place(x=540,y=3)
        Button(bl1,image=pi2,bg='red',relief='flat',activebackground='red').place(x=630,y=3)
        LabelFrame(bl1,width=6,height=61,bg="red",bd=6,font="Times 25 bold").place(x=750,y=0)
        Label(bl1,text="TOTAL:",font="Times 22 bold",bg="red").place(x=760,y=12)
        intall=StringVar()
        ty=Entry(bl1,font="Times 22 bold",bg="pink",width=5,textvariable=intall,justify="center")
        ty.place(x=876,y=12)
        gt=Button(bl1,text="PRINT_BILL",font="Times 14 bold",bg="red",activebackground="pink",bd=5,width=10,command=pay1)
        gt.place(x=968,y=8)
        Button(bl1,text="PENDING",font="Times 14 bold",bg="red",bd=5,activebackground="pink",width=10,command=me1).place(x=1105,y=8)
        lb1=LabelFrame(sc,text="VEG",width=400,height=600,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
        lb1.place(x=10,y=180)
        mycan=Canvas(lb1,bg="red",bd=4,height=422,width=370)
        mycan.pack(side=LEFT,fill="both",expand="yes")
        srll=Scrollbar(lb1,orient='vertical',command=mycan.yview)
        srll.pack(side=RIGHT,fill="y")
        mycan.config(yscrollcommand=srll.set)
        mycan.bind('<Configure>',lambda e:mycan.config(scrollregion=mycan.bbox('all')))
        fat=Frame(mycan)
        mycan.create_window((5,0),window=fat,width=290)
        fat1=Frame(mycan)
        mycan.create_window((195,0),window=fat1)
        itr=['']
        itrid=[]
        price1=[]
        items1=[]
        for i in uddi:
           itrid.append(StringVar())
        for i in udd:
           if len(i[0])<13:
              tr=list(i[0])
              tr1=""
              for j in tr:
                 if j in list(string.ascii_lowercase) or j in list(string.ascii_uppercase) :
                    tr1+=tr[tr.index(j)].lower()
                 else:
                    tr1+=tr[tr.index(j)]
              itr.append(tr1)
              tr1=""
              price1.append(i[1])
              items1.append(i[0])
           else:
              tr=list(i[0])
              tr1=""
              for j in tr:
                 if not j in list(string.ascii_lowercase) and not j in list(string.ascii_uppercase) :
                    tr1+=tr[tr.index(j)+1].lower()
                    del tr[tr.index(j)]
                 else:
                    tr1+=j.lower()
              itr.append(tr1)
              tr1=""
              price1.append(i[1])
              items1.append(i[0])
        klm=0
        for i in itr:
           if i!='':
              hb1=Label(fat1,bg="red",width=10,height=1)
              hb1.pack()
              it1=Label(fat,text=i,font="Times 35 bold",bg="red",width=12)
              it1.pack()
              st1=StringVar()
              et1=Entry(fat1,textvariable=itrid[klm],font="Times 25 bold",bg="pink",width=4,justify="center")
              et1.bind("<Return>",pay)
              et1.pack()
              klm+=1
           else:
              hb1=Label(fat1,bg="red",width=10,height=1)
              hb1.pack()
              it1=Label(fat,text=i,font="Times 35 bold",bg="red",width=12)
              it1.pack()
              et1=Entry(fat1,font="Times 26 bold",relief="flat",bg="red",width=4,justify="center")
              et1.pack()
        Label(sc,bg='red',width=53).place(x=18,y=219)
        Label(sc,bg='red',width=53).place(x=18,y=650)
        Label(sc,bg='red',width=53).place(x=18,y=219)
        Label(sc,bg='red',height=29).place(x=15,y=213)
        lb2=LabelFrame(sc,text="NON-VEG",width=400,height=476,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
        lb2.place(x=450,y=180)
        mycaan1=Canvas(lb2,bd=4,bg="red",height=422,width=420)
        mycaan1.pack(side=LEFT,fill="both",expand="yes")
        sroll=Scrollbar(lb2,orient="vertical",command=mycaan1.yview)
        sroll.pack(side=RIGHT,fill="y")
        mycaan1.config(yscrollcommand=sroll.set)
        mycaan1.bind("<Configure>",lambda e:mycaan1.config(scrollregion=mycaan1.bbox('all')))
        fat2=Frame(mycaan1)
        mycaan1.create_window((90,0),window=fat2,width=310)
        fat3=Frame(mycaan1)
        mycaan1.create_window((290,0),window=fat3)
        itr1=['']
        for i in udd1:
           tr=list(i[0])
           tr1=""
           for j in tr:
              if j in list(string.ascii_lowercase) or j in list(string.ascii_uppercase) :
                 tr1+=tr[tr.index(j)].lower()
              else:
                 tr1+=tr[tr.index(j)]
           itr1.append(tr1)
           tr1=""
           price1.append(i[1])
           items1.append(i[0])
        itr1.append('')
        itr1.append('')
        for i in itr1:
           if i!='':
              hb2=Label(fat3,bg="red",width=10,height=1)
              hb2.pack()
              it2=Label(fat2,text=i,font="Times 35 bold",bg="red",width=50)
              it2.pack()
              et2=Entry(fat3,textvariable=itrid[klm],font="Times 25 bold",bg="pink",width=4,justify="center")
              et2.bind("<Return>",pay)
              et2.pack()
              klm+=1
           else:
              hb2=Label(fat3,bg="red",width=10,height=1)
              hb2.pack()
              it2=Label(fat2,text=i,font="Times 35 bold",bg="red",width=25)
              it2.pack()
              st2=StringVar()
              et2=Entry(fat3,textvariable=st2,font="Times 26 bold",relief="flat",bg="red",width=4,justify="center")
              et2.pack()
        Label(sc,bg='red',width=60,height=0).place(x=460,y=219)
        Label(sc,bg='red',width=60).place(x=460,y=633)
        Label(sc,bg='red',height=29).place(x=455,y=213)
        lb3=LabelFrame(sc,text="OTHERS",width=460,height=476,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
        lb3.place(x=930,y=180)
        itr2=['']
        for i in udd2:
           tr=list(i[0])
           tr1=""
           for j in tr:
              if not j in list(string.ascii_lowercase) and not j in list(string.ascii_uppercase) :
                 tr1+=tr[tr.index(j)+1].lower()
                 del tr[tr.index(j)]
              else:
                 tr1+=j.lower()
           itr2.append(tr1)
           tr1=""
           price1.append(i[1])
           items1.append(i[0])
        itr2.append('')
        itr2.append('')
        mycaan2=Canvas(lb3,bd=4,height=422,width=310,bg="red")
        mycaan2.pack(side=LEFT,fill="both",expand="yes")
        sroll1=Scrollbar(lb3,orient="vertical",command=mycaan2.yview)
        sroll1.pack(side=RIGHT,fill="y")
        mycaan2.config(yscrollcommand=sroll1.set)
        mycaan2.bind("<Configure>",lambda e:mycaan2.config(scrollregion=mycaan2.bbox('all')))
        fat4=Frame(mycaan2)
        mycaan2.create_window((115,0),window=fat4,width=260)
        fat5=Frame(mycaan2)
        mycaan2.create_window((280,0),window=fat5)
        for i in itr2:
           if i!='':
              hb3=Label(fat5,bg="red",width=10,height=1)
              hb3.pack()
              it3=Label(fat4,text=i,font="Times 35 bold",bg="red",width=50)
              it3.pack()
              st3=StringVar()
              et3=Entry(fat5,textvariable=itrid[klm],font="Times 25 bold",bg="pink",width=4,justify="center")
              et3.bind("<Return>",pay)
              et3.pack()
              klm+=1
           else:
              hb3=Label(fat5,bg="red",width=10,height=1)
              hb3.pack()
              it3=Label(fat4,text=i,font="Times 35 bold",bg="red",width=30)
              it3.pack()
              st3=StringVar()
              et3=Entry(fat5,textvariable=st3,font="Times 26 bold",relief="flat",bg="red",width=4,justify="center")
              et3.pack()
        Label(sc,bg='red',width=45).place(x=936,y=219)
        Label(sc,bg='red',width=45).place(x=936,y=227)
        Label(sc,bg='red',width=45,height=2).place(x=936,y=617)
        nn=1
        delforbill()
    if yy==1:
        delforbill()
        yy=0
def search():
    delforsearch()
    global srf,st,era,iden,yy,t2,mm,ts,mon
    if mm==0:
        t2=True
        yy=1
        srf=LabelFrame(sc,text="SREACH",width=1270,height=100,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
        srf.place(x=2,y=90)
        st=StringVar()
        cb1=ttk.Combobox(srf,state="readonly",textvariable=st,width=6,height=15,font="Times 20 bold")
        val1=["DATE"]
        for i in range(1,32):
            val1.append(str(i))
        cb1['values']=val1
        st.set(val1[0])
        cb1.place(x=10,y=1)
        mon=StringVar()
        cb2=ttk.Combobox(srf,state="readonly",textvariable=mon,width=11,height=15,font="Times 20 bold")
        val2=["MONTH"]
        for i in range(1,13):
            ca=calendar.month(2019,i)
            cc=ca[0:ca.index("2"):]
            jj=str(i)+"-"
            for j in cc:
                if j!=' ':
                    jj+=j
            val2.append(jj)
        cb2['values']=val2
        mon.set(val2[0])
        cb2.place(x=120,y=1)
        era=StringVar()
        cb3=ttk.Combobox(srf,state="readonly",textvariable=era,width=8,height=15,font="Times 20 bold")
        val3=["YEAR","2019"]
        xz=str(to.year)
        sas="2019"
        while sas!=xz:
           sas=str(int(sas)+1)
           val3.append(sas)
        cb3['values']=val3
        era.set(val3[0])
        cb3.place(x=300,y=1)
        Label(srf,text="=>",font="Times 30 bold",bg="red").place(x=445,y=0)
        idla=Label(srf,text="ID.NO:",font="Times 25 bold",bg="red")
        idla.place(x=500,y=1)
        ts=StringVar()
        iden=Entry(srf,textvariable=ts,font="Times 25 bold",width=5,bg="pink",justify="center")
        iden.place(x=630,y=1)
        Label(srf,text="=>",font="Times 30 bold",bg="red").place(x=800,y=0)
        fri=Button(srf,text="submit",font="Times 15 bold",bg="green",bd=8,width=9,activebackground="pink",command=getdata)
        fri.place(x=980,y=-5)
        mm=1
def email():
    global t1,t2,t3,t4,t5,nn,con,t7,lb9
    if messagebox.askyesno("ShutDown","Are You Sure To Log_out??"):
        mixer.music.stop()
        con.close()
        t7=False
        fr2.destroy()
        if t1==True:
            lb1.destroy()
            lb2.destroy()
            lb3.destroy()
            bl1.destroy()
            nn=0
            t1=False
        if t2==True:
            srf.destroy()
            t2=False
        if t3==True:
            lb9.destroy()
            t3=False
        if t4==True:
            lb10.destroy()
            t4=False
        if t5==True:
           lb11.destroy()
           t5=False
        login()
        """s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login("vigneshvicky8337@gmail.com","9035637356")
        s.sendmail("vigneshvicky8337@gmail.com","vignesh.v2019b@vitstudent.ac.in","hi da")
        print("send...")
        s.quit()"""
    else:
        pass
def small():
    global n
    if n==0:
        sc.attributes("-fullscreen",False)
        sc.geometry("1300x650+0+0")
        bt1.config(text="Full_screen")
        n=1
    else:
        sc.attributes("-fullscreen",True)
        bt1.config(text="Small_screen")
        n=0
def login():
    global usertxt,pastxt,userentry,passentry,fr1,bt1,igm2,lkk,igm10,lkk1
    bt1=Button(sc,text="Small_screen",font="Times 12 bold",bg="red",bd=7,width=10,command=small)
    bt1.place(x=1165,y=5)
    lkk=Label(sc,image=igm2,bg="red")
    lkk.place(x=100,y=-30)
    lkk1=Label(sc,image=igm10,bg="red")
    lkk1.place(x=370,y=80)
    fr1=LabelFrame(sc,text="LOG_IN",width=550,height=350,font="Times 25 bold",labelanchor=N,bg="red",bd=6)
    fr1.place(relx=0.5,rely=0.6,anchor=CENTER)
    userlb=Label(fr1,text="User_Name:",font="Times 24 bold",bg="red").place(x=25,y=35)
    usertxt=StringVar()
    pastxt=StringVar()
    userentry=Entry(fr1,textvariable=usertxt,width =25,fg="white",bg="red",bd="5",font="Times 25 bold")
    userentry.place(x=210,y=34)
    passlb=Label(fr1,text="Pass_Word:",font="Times 24 bold",bg="red").place(x=25,y=100)
    passentry=Entry(fr1,textvariable=pastxt,width =25,fg="white",bg="red",bd="5",font="Times 25 bold",show="*")
    passentry.place(x=210,y=100)
    def main():
        global bt1,fr2,btb,con
        con=mysqli.connect(host="localhost",user="root",password="",database="test")
        fr2=LabelFrame(sc,width=1200,height=68,bg="red",bd=6)
        fr2.place(x=20,y=20)
        Button(fr2,text="Billing_Section",font="Times 15 bold",bg="orange",bd=6,width=13,command=billing).place(x=4,y=4)
        billing()
        Frame(fr2,bg="brown",width=5,height=55).place(x=185,y=1)
        Button(fr2,text="Update_Section",font="Times 15 bold",bg="orange",bd=6,width=13,command=update).place(x=200,y=4)
        Frame(fr2,bg="brown",width=5,height=55).place(x=380,y=1)
        Button(fr2,text="Search_Section",font="Times 15 bold",bg="orange",bd=6,width=13,command=search).place(x=395,y=4)
        Frame(fr2,bg="brown",width=5,height=55).place(x=580,y=1)
        Button(fr2,text="Pending_Section",font="Times 15 bold",bg="orange",bd=6,width=13,command=pending).place(x=596,y=4)
        Frame(fr2,bg="brown",width=5,height=55).place(x=780,y=1)
        bt1.destroy()
        bt1=Button(fr2,text="Small_screen",font="Times 15 bold",bg="orange",bd=6,width=13,command=small)
        bt1.place(x=795,y=4)
        Frame(fr2,bg="brown",width=5,height=55).place(x=978,y=1)
        Button(fr2,text="LOG_OUT",font="Times 15 bold",bg="orange",bd=6,width=13,command=email).place(x=1000,y=4)
    def letsgo():
        if usertxt.get()=="Yadav" and pastxt.get()=="123456789":
            lkk1.destroy()
            lkk.destroy()
            fr1.destroy()
            main()
        else:
            userentry.delete(0,END)
            passentry.delete(0,END)
            messagebox.showwarning("warning","Wrong UserName or PassWord")
    Button(fr1,text="Lets_Go...",font="Times 18 bold",bg="red",bd=5,activebackground="pink",command=letsgo).place(x=100,y=200)
    Button(fr1,text="Exit",font="Times 18 bold",bg="red",bd=5,width=8,activebackground="pink",command=sc.destroy).place(x=350,y=200)
login()
sc.mainloop()


"""pyinstaller.exe --onefile -w --icon=app.ico app.py"""
