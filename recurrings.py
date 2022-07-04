from cProfile import label
from cgitb import text
import csv
from enum import auto
import tkinter as tk
from itertools import count
from pydoc import describe
import shutil
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from turtle import clear, color, width
from unittest.util import _count_diff_all_purpose
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser

from setuptools import Command
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date,datetime, timedelta
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
from tkPDFViewer import tkPDFViewer as pdf# For pdf view

#saiju
import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel
from matplotlib.widgets import Cursor
from dateutil.relativedelta import relativedelta
import pendulum

from pathlib import Path
import pandas as pd
from tkinter import messagebox
from tkinter import *
from docx import Document
from fpdf import FPDF
import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import pdfkit
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders

import win32api
import win32print
from tkinter import filedialog
from pyautogui import alert
import os
import tempfile
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from textwrap import wrap
import re


# ##########################################################################################################
fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbilling", port="3306"
)
fbcursor = fbilldb.cursor(buffered=True)
##########################################################################################################
def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1360x730")

root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
# recalc = PhotoImage(file="images/recalculate.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")




selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")


##################################################################################################FILES

#--------------------TAB-4  RECURRING-ASHBY---------------------


 #---------------------------------------------------------------------------------generate recurring invoice popups
def gn_inv_rir_in(): 
  #  if result=='ok': 
   messagebox.showinfo("F-Billing Revolution 2022", "No recurring invoices are ready today")

def gn_inv_sucss():  
   messagebox.showinfo("F-Billing Revolution 2022", "1 new invoice successfully created.")
#------------------------------------------------------------------------------------------------refrsh
def rfh_rir():
    rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL"
    fbcursor.execute(rir_main_table_sql)
    main_rir_val=fbcursor.fetchall()
    count_rir=0
    for record in rir_tree.get_children():
          rir_tree.delete(record)
    for i in main_rir_val:
        rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
        count_rir +=1

#----------------------------------------------------------------------------------------------------print invoice
  
def rir_prnt_inv_rir():

        from reportlab.pdfgen import canvas
            # from tkdocviewer import *
        from reportlab.lib import colors
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
        from reportlab.lib.pagesizes import letter, inch
    # try:
        pdf = canvas.Canvas("recurring_reports/CInvoice.pdf", pagesize=letter)
        # cus_id=cus_main_tree.item(cus_main_tree.focus())["values"][3]
        # sqlt= 'select * from customer where businessname=%s'
        # sqlt_val=(cus_id,)
        # fbcursor.execute(sqlt,sqlt_val)
        # cus_ft=fbcursor.fetchone()

        sql_company = "SELECT * from company"
        fbcursor.execute(sql_company)
        company= fbcursor.fetchone()
        
        pdf.setFont('Helvetica',12)
        pdf.drawString(27,768, company[1])
        text=company[2]
        wraped_text="\n".join(wrap(text,30))
        htg=wraped_text.split('\n')
            
        vg=len(htg)
        if vg>0:
                pdf.drawString(30,752,htg[0])
                print("1")
                if vg>1:
                  pdf.drawString(30,738,htg[1])
                  print("2")
                  if vg>2:
                      pdf.drawString(30,725,htg[2])
                      print("3")
                      if vg>3:
                          pdf.drawString(30,712,htg[3])
                          print("4")
                      else:
                          pass
                  else:
                      pass
                else:
                    pass
                
        else:
                pass
        pdf.drawString(35,700,company[4])
        pdf.drawString(490,760, "Invoice Report")

        # pdf.drawString(460,700,"Customer ID:"+str(cus_ft[0]))
        # pdf.drawString(28,695,"__________________________________________________________________________________")
        # pdf.drawString(31,680,"Bill To:")
        # pdf.drawString(31,668,cus_ft[4])
        # text=cus_ft[5]
        # wraped_text="\n".join(wrap(text,30))
        # htg=wraped_text.split('\n')
            
        # vg=len(htg)
        # if vg>0:
        #         pdf.drawString(30,654,htg[0])
        #         print("1")
        #         if vg>1:
        #           pdf.drawString(30,640,htg[1])
        #           print("2")
        #           if vg>2:
        #               pdf.drawString(30,626,htg[2])
        #               print("3")
        #               if vg>3:
        #                   pdf.drawString(30,612,htg[3])
        #                   print("4")
        #               else:
        #                   pass
        #           else:
        #               pass
        #         else:
        #             pass
                
        # else:
        #         pass

        # pdf.drawString(400,680,"Ship To:")
        # pdf.drawString(400,668,cus_ft[6])
        # text=cus_ft[7]
        # wraped_text="\n".join(wrap(text,30))
        # htg=wraped_text.split('\n')
            
        # vg=len(htg)
        # if vg>0:
        #         pdf.drawString(400,654,htg[0])
        #         print("1")
        #         if vg>1:
        #           pdf.drawString(400,640,htg[1])
        #           print("2")
        #           if vg>2:
        #               pdf.drawString(400,626,htg[2])
        #               print("3")
        #               if vg>3:
        #                   pdf.drawString(400,612,htg[3])
        #                   print("4")
        #               else:
        #                   pass
        #           else:
        #               pass
        #         else:
        #             pass
                
        # else:
        #         pass

        # pdf.drawString(28,606,"__________________________________________________________________________________")


        # pdf.drawString(28,591,"__________________________________________________________________________________")
        # pdf.drawString(28,591,"Invoice No           Date        Due Date     Recurring      Status        Invoice Total    Total Paid   Balance      ")
        
        
        # sqlr= 'select currencysign from company'
        # fbcursor.execute(sqlr)
        # crncy=fbcursor.fetchone()
          
        # crc=crncy[0]
        # sqlrt= 'select currsignplace from company'
        # fbcursor.execute(sqlrt)
        # post_rp=fbcursor.fetchone()
        # ps_cr=post_rp[0]
        # count=0
        # sql_inv_dt='SELECT * FROM invoice where businessname=%s'
        # inv_valuz=(cus_id,)
        # fbcursor.execute(sql_inv_dt,inv_valuz)
        # tre=fbcursor.fetchall()
        # x=571

        # for i in tre:
        #               if x==38 or x==50:
        #                   pdf.showPage()
        #                   x=750
        #               else:
        #                   if i[24] is None:
        #                       dfh="No"
        #                   else:
        #                       dfh="Yes"
        #                   if ps_cr=="before amount":
        #                       pdf.drawString(28,x,str(i[1]))
                        
        #                       pdf.drawString(100,x,str(i[2]))
        #                       pdf.drawString(168,x,str(i[3]))
        #                       pdf.drawString(250,x,dfh)
        #                       pdf.drawString(315,x,str(i[5])) 
        #                       pdf.drawString(380,x,str(crc)+str(i[8]))
        #                       pdf.drawString(460,x,str(crc)+str(i[9]))
        #                       pdf.drawString(522,x,str(crc)+str(i[10]))
                              
        #                   elif ps_cr=="after amount":
        #                       pdf.drawString(28,x,str(i[1]))
        #                       pdf.drawString(100,x,str(i[2]))
        #                       pdf.drawString(168,x,str(i[3]))
        #                       pdf.drawString(250,x,str(dfh))
        #                       pdf.drawString(315,x,str(i[5])) 
        #                       pdf.drawString(380,x,str(i[8])+str(crc))
        #                       pdf.drawString(460,x,str(i[9])+str(crc))
        #                       pdf.drawString(522,x,str(i[10])+str(crc))
                              
        #                   elif ps_cr=="before amount with space":
        #                       pdf.drawString(28,x,str(i[1]))
                        
        #                       pdf.drawString(100,x,str(i[2]))
        #                       pdf.drawString(168,x,str(i[3]))
        #                       pdf.drawString(250,x,str(dfh))
        #                       pdf.drawString(315,x,str(i[5])) 
        #                       pdf.drawString(380,x,str(crc)+" "+str(i[8]))
        #                       pdf.drawString(460,x,str(crc)+" "+str(i[9]))
        #                       pdf.drawString(522,x,str(crc)+" "+str(i[10]))
                              
                              
        #                   elif ps_cr=="after amount with space":
        #                       pdf.drawString(28,x,str(i[1]))
        #                       pdf.drawString(100,x,str(i[2]))
        #                       pdf.drawString(168,x,str(i[3]))
        #                       pdf.drawString(250,x,str(dfh))
        #                       pdf.drawString(315,x,str(i[5])) 
        #                       pdf.drawString(380,x,str(i[8])+" "+str(crc))
        #                       pdf.drawString(460,x,str(i[9])+" "+str(crc))
        #                       pdf.drawString(522,x,str(i[10])+" "+str(crc))
                          
        #                   else:
        #                       pass
                        
        #               count += 1
                    
        #               x-=15
        # sql_inv_t="select sum(invoicetot),sum(totpaid), sum(balance) from invoice where businessname=%s"
        # sql_inv_t_val=(cus_id,)
        # fbcursor.execute(sql_inv_t,sql_inv_t_val)
        # inv_ttt=fbcursor.fetchone() 
        # pdf.drawString(28,x,"__________________________________________________________________________________")
        # if ps_cr=="before amount":
                              
        #                       pdf.drawString(28,x-13,"")
                        
        #                       pdf.drawString(100,x-13,"")
        #                       pdf.drawString(168,x-13,"")
        #                       pdf.drawString(250,x-13,"-Summary-")
        #                       pdf.drawString(315,x-13,"") 
        #                       pdf.drawString(380,x-13,str(crc)+str(inv_ttt[0]))
        #                       pdf.drawString(460,x-13,str(crc)+str(inv_ttt[1]))
        #                       pdf.drawString(522,x-13,str(crc)+str(inv_ttt[2]))
        # elif ps_cr=="after amount":
                            
        #                       pdf.drawString(28,x-13,"")
        #                       pdf.drawString(100,x-13,"")
        #                       pdf.drawString(168,x-13,"-Summary-")
        #                       pdf.drawString(250,x-13,"")
        #                       pdf.drawString(315,x-13,"") 
        #                       pdf.drawString(380,x-13,str(inv_ttt[0])+str(crc))
        #                       pdf.drawString(460,x-13,str(inv_ttt[1])+str(crc))
        #                       pdf.drawString(522,x-13,str(inv_ttt[2])+str(crc))
        # elif ps_cr=="before amount with space":
        #                       pdf.drawString(28,x-13,"")
                        
        #                       pdf.drawString(100,x-13,"")
        #                       pdf.drawString(168,x-13,"-Summary-")
        #                       pdf.drawString(250,x-13,"")
        #                       pdf.drawString(315,x-13,"") 
        #                       pdf.drawString(380,x-13,str(crc)+" "+str(inv_ttt[0]))
        #                       pdf.drawString(460,x-13,str(crc)+" "+str(inv_ttt[1]))
        #                       pdf.drawString(522,x-13,str(crc)+" "+str(inv_ttt[2]))
        # elif ps_cr=="after amount with space":
        #                       pdf.drawString(28,x-13,"")
        #                       pdf.drawString(100,x-13,"")
        #                       pdf.drawString(168,x-13,"-Summary-")
        #                       pdf.drawString(250,x-13,"")
        #                       pdf.drawString(315,x-13,"") 
        #                       pdf.drawString(380,x-13,str(inv_ttt[0])+" "+str(crc))
        #                       pdf.drawString(460,x-13,str(inv_ttt[1])+" "+str(crc))
        #                       pdf.drawString(522,x-13,str(inv_ttt[2])+" "+str(crc))
        # else:
        #                 pass


        pdf.save()
        win32api.ShellExecute(0,"","recurring_reports\CInvoice.pdf",None,".",0)
    # except:
    #   pass
#----------------------------------------------------------------------------------------------------------email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)


def addacnt():  
   messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

def savesettings():  
   messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")


def prview_rir_inv():
      
    if not rir_tree.selection():
        messagebox.showwarning("F-Billing Revolution","No line selected.\nSelect a line before printing.")
    else:
      prev_invo = Toplevel()
      prev_invo.title("Preview Invoice")
      p2 = PhotoImage(file = "images/fbicon.png")
      prev_invo.iconphoto(False, p2)
      prev_invo.geometry("1360x730+0+0")
      rir_tree_prev = rir_tree.item(rir_tree.focus())["values"][1]
      prev_sql = "SELECT * FROM invoice WHERE invoice_number=%s"
      prev_val = (rir_tree_prev,)
      fbcursor.execute(prev_sql,prev_val)
      prev_data = fbcursor.fetchone()

      pri_sql = "SELECT * FROM company"
      fbcursor.execute(pri_sql)
      comp_data = fbcursor.fetchone()


      if prev_data[13] == 'Professional 1 (logo on left side)':
        frame = Frame(prev_invo, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=5,y=30)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        
        canvas.config(width=1315,height=640)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235, 25, 1035, 1430 , outline='yellow',fill='white')
        inv_title_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_title_canvas.config(text=prev_data[39],anchor="center",bg="white")
        canvas.create_window(637, 50,window=inv_title_canvas)

        try:
          image = Image.open("images/"+comp_data[13])
          resize_image = image.resize((250, 125))
          logo_img = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=logo_img, height=125, width=250,)
          b2.photo = logo_img
          canvas.create_window(410, 155,window=b2)
        except:
          pass
        inv_pr_sql = "SELECT * FROM invoice_settings"

        fbcursor.execute(inv_pr_sql)
        inv_st = fbcursor.fetchone()

        lb_inv1=Label(canvas,text=inv_st[4], bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Invoice#
        win_inv1 = canvas.create_window(290, 240, anchor="nw", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[5], bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Invoicedate
        win_inv1 = canvas.create_window(290, 260, anchor="nw", window=lb_inv1)
          
        lb_inv1=Label(canvas,text="Due Date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
        win_inv1 = canvas.create_window(290, 280, anchor="nw", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[7], bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
        win_inv1 = canvas.create_window(290, 300, anchor="nw", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[6], bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
        win_inv1 = canvas.create_window(290, 320, anchor="nw", window=lb_inv1)

        lb_inv1=Label(canvas,text=str(inv_st[0])+str(prev_data[1]), bg="white",anchor="nw",font=("Helvetica", ),height=1)
        win_inv1 = canvas.create_window(425, 240, anchor="nw", window=lb_inv1)
        
        lb_inv1=Label(canvas,text=inv_st[3], bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
        win_inv1 = canvas.create_window(990, 240, anchor="ne", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[24], bg="white",anchor="ne",font=("Helvetica 10" ),height=2)#TAX EXEMPTED
        win_inv1 = canvas.create_window(990, 268, anchor="ne", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[8], bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
        win_inv1 = canvas.create_window(298, 350, anchor="nw", window=lb_inv1)

        lb_inv1=Label(canvas,text=inv_st[9], bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
        win_inv1 = canvas.create_window(625, 350, anchor="nw", window=lb_inv1)

        canvas.create_text(465, 270, text=prev_data[2], fill="black", font=('Helvetica 11'))
        canvas.create_text(465, 290, text=prev_data[3], fill="black", font=('Helvetica 11'))
        inv_terms_canvas = Label(canvas,font=('Helvetica 10'),width=30,bg='white')
        inv_terms_canvas.config(text=prev_data[42],anchor="w")
        canvas.create_window(548, 330,window=inv_terms_canvas)
        inv_ref_canvas = Label(canvas,font=('Helvetica 10'),width=30,bg='white')
        inv_ref_canvas.config(text=prev_data[43],anchor="w")
        canvas.create_window(548, 330,window=inv_ref_canvas) 
        
        canvas.create_text(896, 110, text=comp_data[1], fill="black", font=('Helvetica 12 bold'))
        comp_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",bg="white",cursor="arrow",bd=0,)
        comp_addr_canvas.insert("1.0",comp_data[2])
        comp_addr_canvas.tag_configure("tag_name", justify='right')
        comp_addr_canvas.tag_add("tag_name", "1.0", "end")
        comp_addr_canvas.config(state=DISABLED)
        canvas.create_window(882, 165,window=comp_addr_canvas)
        inv_stax_canvas = Label(canvas, font=('Helvetica 10 '),width=30,bg="white")
        inv_stax_canvas.config(text=comp_data[4],anchor="e")
        canvas.create_window(865, 220,window=inv_stax_canvas)
     
        inv_canv_name = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_canv_name.config(text=prev_data[18],anchor="w",bg="white")
        canvas.create_window(419, 380,window=inv_canv_name)
        inv_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_addr_canvas.insert("1.0",prev_data[19])
        inv_addr_canvas.config(state=DISABLED)
        canvas.create_window(405, 425, window=inv_addr_canvas)
        
        inv_ship_canv_lbl = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_ship_canv_lbl.config(text=prev_data[20],anchor="w",bg="white")
        canvas.create_window(751, 380, window=inv_ship_canv_lbl)
        inv_ship_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_ship_addr_canvas.insert("1.0",prev_data[21])
        inv_ship_addr_canvas.config(state=DISABLED)
        canvas.create_window(736, 425,window=inv_ship_addr_canvas)

        inv_header_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_header_canvas.config(text=prev_data[40],anchor="center",bg="white")
        canvas.create_window(637, 452,window=inv_header_canvas)
        
        s = ttk.Style()
        s.configure('mystyles.Treeview.Heading', background=''+inv_st[2],State='DISABLE')
        inv_prev_tree = ttk.Treeview(canvas,height=12,style='mystyles.Treeview')
        inv_prev_tree["columns"] = ["1","2","3","4","5"]
        inv_prev_tree.column("#0",width=1)
        inv_prev_tree.column("1",width=100,anchor=CENTER)
        inv_prev_tree.column("2",width=343,anchor=CENTER)
        inv_prev_tree.column("3",width=80,anchor=CENTER)
        inv_prev_tree.column("4",width=90,anchor=CENTER)
        inv_prev_tree.column("5",width=80,anchor=CENTER)
        inv_prev_tree.heading("#0",text="")
        inv_prev_tree.heading("1",text=inv_st[10])
        inv_prev_tree.heading("2",text=inv_st[11])
        inv_prev_tree.heading("3",text=inv_st[12])
        inv_prev_tree.heading("4",text=inv_st[14])
        inv_prev_tree.heading("5",text=inv_st[15])
        window = canvas.create_window(285, 462, anchor="nw", window=inv_prev_tree)

        currency_sql = "SELECT currencysign,currsignplace FROM company"
        fbcursor.execute(currency_sql,)
        currency_symb = fbcursor.fetchone()

        storing_sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
        storing_val = (prev_data[1],)
        fbcursor.execute(storing_sql,storing_val)
        storing_data = fbcursor.fetchall()
        
        for record in storing_data:
          inv_prev_tree.insert(parent='', index='end',text='', values=(record[5],record[6] + "  -  " + record[7],record[9],record[8],record[13]))
        

        if not comp_data:
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          
          if currency_symb[1] == "before amount":

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,737,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,737,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,786,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,786,window=inv_tot1_canvas)

          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            
        elif comp_data[12] == "1":
          canvas.create_line(980, 723, 980, 773 )
          canvas.create_line(720, 723, 720, 773 )
          canvas.create_line(860, 723, 860, 773 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          # canvas.create_line(980, 798, 720, 798 )
          # canvas.create_line(980, 823, 720, 823 )
          # canvas.create_line(980, 848, 720, 848 )
          # canvas.create_line(980, 873, 720, 873 )

          if currency_symb[1] == "before amount":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white', height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)


            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,761,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,761,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "before amount with space":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,761,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,761,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

           

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,761,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount with space":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,37,window=inv_sub1_canvas)

            

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,761,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tot1_canvas)

            
        elif comp_data[12] == "2":
          canvas.create_line(980, 723, 980, 798 )
          canvas.create_line(720, 723, 720, 798 )
          canvas.create_line(860, 723, 860, 798 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          # canvas.create_line(980, 823, 720, 823 )
          # canvas.create_line(980, 848, 720, 848 )
          # canvas.create_line(980, 873, 720, 873 )
          # canvas.create_line(980, 898, 720, 898 )

          if currency_symb[1] == "before amount":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)


            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,786,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,786,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "before amount with space":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white',height=1)
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount":
       

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,786,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount with space":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)


            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,786,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tot1_canvas)

            
        elif comp_data[12] == "3":
          canvas.create_line(980, 723, 980, 823 )
          canvas.create_line(720, 723, 720, 823 )
          canvas.create_line(860, 723, 860, 823 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
       
          if currency_symb[1] == "before amount":
           

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX2_canvas.config(text="TAX2",anchor="n")
            canvas.create_window(790,786,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white',height=1)
            inv_tax_2_canvas.config(text=currency_symb[0]+str(prev_data[36]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_2_canvas)


            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "before amount with space":

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX2_canvas.config(text="TAX2",anchor="n")
            canvas.create_window(790,786,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0] + " " + str(prev_data[36]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_excname_canvas.config(text=prev_data[11],anchor="n")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX2_canvas.config(text="TAX2",anchor="n")
            canvas.create_window(790,761,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_excname_canvas.config(text=prev_data[11],anchor="n")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            
          elif currency_symb[1] == "after amount with space":
            

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_sub_canvas.config(text=inv_st[16],anchor="n")
            canvas.create_window(790,737,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX1_canvas.config(text=inv_st[19],anchor="n")
            canvas.create_window(790,761,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_TAX2_canvas.config(text="TAX2",anchor="n")
            canvas.create_window(790,786,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white',height=1)
            inv_excname_canvas.config(text=prev_data[11],anchor="n")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white',height=1)
            inv_tot_canvas.config(text="Invoice Total",anchor="n")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            

        inv_prev_comments = Text(canvas,font=('Helvetica 10'),width=100,height=6,fg= "black",
        bg="white",cursor="arrow",bd=0)
        inv_prev_comments.insert("1.0",prev_data[44])
        inv_prev_comments.config(state=DISABLED)
        canvas.create_window(635, 980,window=inv_prev_comments)
        
        lbx_inv=Label(canvas,text=inv_st[23], bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
        win_inv2 = canvas.create_window(560, 1055, anchor="nw", window=lbx_inv)
        canvas.create_line(290, 1090, 982, 1090)

        inv_prev_terms = Text(canvas,font=('Helvetica 10'),width=100,height=4,fg= "black",bg="white",cursor="arrow",bd=0)
        inv_prev_terms.insert("1.0",prev_data[35])
        inv_prev_terms.tag_configure("tag_name", justify='left')
        inv_prev_terms.tag_add("tag_name", "1.0", "end")
        inv_prev_terms.config(state=DISABLED)
        canvas.create_window(642, 1125,window=inv_prev_terms)
        canvas.create_text(330, 1165, text="Sale Person:", fill="black", font=('Helvetica 10'))
        inv_prev_salesp = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_prev_salesp.config(text=prev_data[14],anchor="w",bg="white")
        canvas.create_window(502, 1165, window = inv_prev_salesp)
        inv_footer_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_footer_canvas.config(text=prev_data[41],anchor="w",bg="white")
        canvas.create_window(413, 1185,window=inv_footer_canvas)
    #----------------Professional 2 (logo on right side)------------------
      elif prev_data[13] == 'Professional 2 (logo on right side)':
        frame = Frame(prev_invo, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=5,y=30)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        
        canvas.config(width=1315,height=640)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235, 25, 1035, 1430 , outline='yellow',fill='white')
        inv_title_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_title_canvas.config(text=prev_data[39],anchor="center",bg="white")
        canvas.create_window(637, 50,window=inv_title_canvas)

        try:
          image = Image.open("images/"+comp_data[13])
          resize_image = image.resize((250, 125))
          logo_img = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=logo_img, height=125, width=250,)
          b2.photo = logo_img
          canvas.create_window(860, 155,window=b2)
        except:
          pass
        
        canvas.create_text(715, 250, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(725, 270, text="Invoicedate", fill="black", font=('Helvetica 11'))
        canvas.create_text(718, 290, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(710, 310, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(728, 330, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_num_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_num_canvas.config(text=prev_data[1],anchor="w")
        canvas.create_window(918, 250,window=inv_num_canvas)
        canvas.create_text(856, 270, text=prev_data[2], fill="black", font=('Helvetica 11'))
        canvas.create_text(856, 290, text=prev_data[3], fill="black", font=('Helvetica 11'))
        inv_terms_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_terms_canvas.config(text=prev_data[42],anchor="w")
        canvas.create_window(918, 310,window=inv_terms_canvas)
        inv_ref_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_ref_canvas.config(text=prev_data[43],anchor="w")
        canvas.create_window(918, 330,window=inv_ref_canvas)
        
        canvas.create_text(379, 110, text=comp_data[1], fill="black", font=('Helvetica 12 bold'))
        comp_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",bg="white",cursor="arrow",bd=0,)
        comp_addr_canvas.insert("1.0",comp_data[2])
        comp_addr_canvas.tag_configure("tag_name", justify='left')
        comp_addr_canvas.tag_add("tag_name", "1.0", "end")
        comp_addr_canvas.config(state=DISABLED)
        canvas.create_window(392, 165,window=comp_addr_canvas)
        inv_stax_canvas = Label(canvas, font=('Helvetica 10 '),width=30,bg='white')
        inv_stax_canvas.config(text=comp_data[4],anchor="w")
        canvas.create_window(405, 220,window=inv_stax_canvas)
        canvas.create_text(320, 255, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(335, 285, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        canvas.create_text(315, 350, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_canv_name = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_canv_name.config(text=prev_data[18],anchor="w",bg="white")
        canvas.create_window(409, 370,window=inv_canv_name)
        inv_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_addr_canvas.insert("1.0",prev_data[19])
        inv_addr_canvas.config(state=DISABLED)
        canvas.create_window(395, 415, window=inv_addr_canvas)
        canvas.create_text(650, 350, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_ship_canv_lbl = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_ship_canv_lbl.config(text=prev_data[20],anchor="w",bg="white")
        canvas.create_window(751, 370, window=inv_ship_canv_lbl)
        inv_ship_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_ship_addr_canvas.insert("1.0",prev_data[21])
        inv_ship_addr_canvas.config(state=DISABLED)
        canvas.create_window(736, 415,window=inv_ship_addr_canvas)

        inv_header_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_header_canvas.config(text=prev_data[40],anchor="center",bg="white")
        canvas.create_window(637, 452,window=inv_header_canvas)
        
        s = ttk.Style()
        s.configure('Treeview.Heading', background='',State='DISABLE')
        inv_prev_tree = ttk.Treeview(canvas,height=12,style='mystyle.Treeview')
        inv_prev_tree["columns"] = ["1","2","3","4","5"]
        inv_prev_tree.column("#0",width=1)
        inv_prev_tree.column("1",width=100,anchor=CENTER)
        inv_prev_tree.column("2",width=343,anchor=CENTER)
        inv_prev_tree.column("3",width=80,anchor=CENTER)
        inv_prev_tree.column("4",width=90,anchor=CENTER)
        inv_prev_tree.column("5",width=80,anchor=CENTER)
        inv_prev_tree.heading("#0",text="")
        inv_prev_tree.heading("1",text="ID/SKU")
        inv_prev_tree.heading("2",text="Product/Service - Description")
        inv_prev_tree.heading("3",text="Quantity")
        inv_prev_tree.heading("4",text="Unit Price")
        inv_prev_tree.heading("5",text="Price")
        window = canvas.create_window(285, 462, anchor="nw", window=inv_prev_tree)

        currency_sql = "SELECT currencysign,currsignplace FROM company"
        fbcursor.execute(currency_sql,)
        currency_symb = fbcursor.fetchone()
        
        storing_sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
        storing_val = (prev_data[1],)
        fbcursor.execute(storing_sql,storing_val)
        storing_data = fbcursor.fetchall()
        
        for record in storing_data:
          inv_prev_tree.insert(parent='', index='end',text='', values=(record[5],record[6] + "  -  " + record[7],record[9],record[8],record[13]))
        

        if not comp_data:
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          
          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "1":
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "2":
          canvas.create_line(980, 723, 980, 898 )
          canvas.create_line(720, 723, 720, 898 )
          canvas.create_line(860, 723, 860, 898 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
        elif comp_data[12] == "3":
          canvas.create_line(980, 723, 980, 923 )
          canvas.create_line(720, 723, 720, 923 )
          canvas.create_line(860, 723, 860, 923 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )
          canvas.create_line(980, 923, 720, 923 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0]+str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0] + " " + str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)

        inv_prev_comments = Text(canvas,font=('Helvetica 10'),width=100,height=6,fg= "black",
        bg="white",cursor="arrow",bd=0)
        inv_prev_comments.insert("1.0",prev_data[44])
        inv_prev_comments.config(state=DISABLED)
        canvas.create_window(635, 980,window=inv_prev_comments)
        
        canvas.create_text(635, 1075, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(290, 1090, 982, 1090)
        
        inv_prev_terms = Text(canvas,font=('Helvetica 10'),width=100,height=4,fg= "black",bg="white",cursor="arrow",bd=0)
        inv_prev_terms.insert("1.0",prev_data[35])
        inv_prev_terms.tag_configure("tag_name", justify='left')
        inv_prev_terms.tag_add("tag_name", "1.0", "end")
        inv_prev_terms.config(state=DISABLED)
        canvas.create_window(642, 1125,window=inv_prev_terms)
        canvas.create_text(330, 1165, text="Sale Person:", fill="black", font=('Helvetica 10'))
        inv_prev_salesp = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_prev_salesp.config(text=prev_data[14],anchor="w",bg="white")
        canvas.create_window(502, 1165, window = inv_prev_salesp)
        inv_footer_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_footer_canvas.config(text=prev_data[41],anchor="w",bg="white")
        canvas.create_window(413, 1185,window=inv_footer_canvas)
    #----------------Simplified 1 (logo on left side)------------------ 
      elif prev_data[13] == 'Simplified 1 (logo on left side)':
        frame = Frame(prev_invo, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=5,y=30)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        
        canvas.config(width=1315,height=640)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235, 25, 1035, 1430 , outline='yellow',fill='white')
        inv_title_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_title_canvas.config(text=prev_data[39],anchor="center",bg="white")
        canvas.create_window(637, 50,window=inv_title_canvas)

        try:
          image = Image.open("images/"+comp_data[13])
          resize_image = image.resize((250, 125))
          logo_img = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=logo_img, height=125, width=250,)
          b2.photo = logo_img
          canvas.create_window(410, 155,window=b2)
        except:
          pass
        
        canvas.create_text(310, 250, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(320, 270, text="Invoicedate", fill="black", font=('Helvetica 11'))
        canvas.create_text(313, 290, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(304, 310, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(323, 330, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_num_canvas = Label(canvas,font=('Helvetica 10'),width=30,bg='white')
        inv_num_canvas.config(text=prev_data[1],anchor="w")
        canvas.create_window(548, 250,window=inv_num_canvas)
        canvas.create_text(465, 270, text=prev_data[2], fill="black", font=('Helvetica 11'))
        canvas.create_text(465, 290, text=prev_data[3], fill="black", font=('Helvetica 11'))
        inv_terms_canvas = Label(canvas,font=('Helvetica 10'),width=30,bg='white')
        inv_terms_canvas.config(text=prev_data[42],anchor="w")
        canvas.create_window(548, 310,window=inv_terms_canvas)
        inv_ref_canvas = Label(canvas,font=('Helvetica 10'),width=30,bg='white')
        inv_ref_canvas.config(text=prev_data[43],anchor="w")
        canvas.create_window(548, 330,window=inv_ref_canvas)   
        
        canvas.create_text(896, 110, text=comp_data[1], fill="black", font=('Helvetica 12 bold'))
        comp_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",bg="white",cursor="arrow",bd=0,)
        comp_addr_canvas.insert("1.0",comp_data[2])
        comp_addr_canvas.tag_configure("tag_name", justify='right')
        comp_addr_canvas.tag_add("tag_name", "1.0", "end")
        comp_addr_canvas.config(state=DISABLED)
        canvas.create_window(882, 165,window=comp_addr_canvas)
        inv_stax_canvas = Label(canvas, font=('Helvetica 10 '),width=30,bg="white")
        inv_stax_canvas.config(text=comp_data[4],anchor="e")
        canvas.create_window(865, 220,window=inv_stax_canvas)
        canvas.create_text(951, 255, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(935, 285, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        canvas.create_text(325, 360, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_canv_name = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_canv_name.config(text=prev_data[18],anchor="w",bg="white")
        canvas.create_window(419, 380,window=inv_canv_name)
        inv_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_addr_canvas.insert("1.0",prev_data[19])
        inv_addr_canvas.config(state=DISABLED)
        canvas.create_window(405, 425, window=inv_addr_canvas)
        canvas.create_text(650, 360, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_ship_canv_lbl = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_ship_canv_lbl.config(text=prev_data[20],anchor="w",bg="white")
        canvas.create_window(751, 380, window=inv_ship_canv_lbl)
        inv_ship_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_ship_addr_canvas.insert("1.0",prev_data[21])
        inv_ship_addr_canvas.config(state=DISABLED)
        canvas.create_window(736, 425,window=inv_ship_addr_canvas)

        inv_header_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_header_canvas.config(text=prev_data[40],anchor="center",bg="white")
        canvas.create_window(637, 452,window=inv_header_canvas)
        
        s = ttk.Style()
        s.configure('Treeview.Heading', background='',State='DISABLE')
        inv_prev_tree = ttk.Treeview(canvas,height=12,style='mystyle.Treeview')
        inv_prev_tree["columns"] = ["1","2","3"]
        inv_prev_tree.column("#0",width=1)
        inv_prev_tree.column("1",width=394,anchor=CENTER)
        inv_prev_tree.column("2",width=150,anchor=CENTER)
        inv_prev_tree.column("3",width=150,anchor=CENTER)
        inv_prev_tree.heading("#0",text="")
        inv_prev_tree.heading("1",text="Product/Service - Description")
        inv_prev_tree.heading("2",text="Quantity")
        inv_prev_tree.heading("3",text="Price")
        window = canvas.create_window(285, 462, anchor="nw", window=inv_prev_tree)

        currency_sql = "SELECT currencysign,currsignplace FROM company"
        fbcursor.execute(currency_sql,)
        currency_symb = fbcursor.fetchone()
    
        storing_sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
        storing_val = (prev_data[1],)
        fbcursor.execute(storing_sql,storing_val)
        storing_data = fbcursor.fetchall()
        
        for record in storing_data:
          inv_prev_tree.insert(parent='', index='end',text='', values=(record[6] + "  -  " + record[7],record[9],record[13]))

        if not comp_data:
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          
          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "1":
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "2":
          canvas.create_line(980, 723, 980, 898 )
          canvas.create_line(720, 723, 720, 898 )
          canvas.create_line(860, 723, 860, 898 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
        elif comp_data[12] == "3":
          canvas.create_line(980, 723, 980, 923 )
          canvas.create_line(720, 723, 720, 923 )
          canvas.create_line(860, 723, 860, 923 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )
          canvas.create_line(980, 923, 720, 923 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0]+str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0] + " " + str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)

        inv_prev_comments = Text(canvas,font=('Helvetica 10'),width=100,height=6,fg= "black",
        bg="white",cursor="arrow",bd=0)
        inv_prev_comments.insert("1.0",prev_data[44])
        inv_prev_comments.config(state=DISABLED)
        canvas.create_window(635, 980,window=inv_prev_comments)
        
        canvas.create_text(635, 1075, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(290, 1090, 982, 1090)
        
        inv_prev_terms = Text(canvas,font=('Helvetica 10'),width=100,height=4,fg= "black",bg="white",cursor="arrow",bd=0)
        inv_prev_terms.insert("1.0",prev_data[35])
        inv_prev_terms.tag_configure("tag_name", justify='left')
        inv_prev_terms.tag_add("tag_name", "1.0", "end")
        inv_prev_terms.config(state=DISABLED)
        canvas.create_window(642, 1125,window=inv_prev_terms)
        canvas.create_text(330, 1165, text="Sale Person:", fill="black", font=('Helvetica 10'))
        inv_prev_salesp = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_prev_salesp.config(text=prev_data[14],anchor="w",bg="white")
        canvas.create_window(502, 1165, window = inv_prev_salesp)
        inv_footer_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_footer_canvas.config(text=prev_data[41],anchor="w",bg="white")
        canvas.create_window(413, 1185,window=inv_footer_canvas)
    #----------------Simplified 2 (logo on right side)------------------ 
      elif prev_data[13] == 'Simplified 2 (logo on right side)':
        frame = Frame(prev_invo, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=5,y=30)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        
        canvas.config(width=1315,height=640)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235, 25, 1035, 1430 , outline='yellow',fill='white')
        inv_title_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_title_canvas.config(text=prev_data[39],anchor="center",bg="white")
        canvas.create_window(637, 50,window=inv_title_canvas)

        try:
          image = Image.open("images/"+comp_data[13])
          resize_image = image.resize((250, 125))
          logo_img = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=logo_img, height=125, width=250,)
          b2.photo = logo_img
          canvas.create_window(860, 155,window=b2)
        except:
          pass
        
        canvas.create_text(715, 250, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(725, 270, text="Invoicedate", fill="black", font=('Helvetica 11'))
        canvas.create_text(718, 290, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(710, 310, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(728, 330, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_num_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_num_canvas.config(text=prev_data[1],anchor="w")
        canvas.create_window(918, 250,window=inv_num_canvas)
        canvas.create_text(856, 270, text=prev_data[2], fill="black", font=('Helvetica 11'))
        canvas.create_text(856, 290, text=prev_data[3], fill="black", font=('Helvetica 11'))
        inv_terms_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_terms_canvas.config(text=prev_data[42],anchor="w")
        canvas.create_window(918, 310,window=inv_terms_canvas)
        inv_ref_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_ref_canvas.config(text=prev_data[43],anchor="w")
        canvas.create_window(918, 330,window=inv_ref_canvas)   
        
        canvas.create_text(379, 110, text=comp_data[1], fill="black", font=('Helvetica 12 bold'))
        comp_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",bg="white",cursor="arrow",bd=0,)
        comp_addr_canvas.insert("1.0",comp_data[2])
        comp_addr_canvas.tag_configure("tag_name", justify='left')
        comp_addr_canvas.tag_add("tag_name", "1.0", "end")
        comp_addr_canvas.config(state=DISABLED)
        canvas.create_window(392, 165,window=comp_addr_canvas)
        inv_stax_canvas = Label(canvas, font=('Helvetica 10 '),width=30,bg="white")
        inv_stax_canvas.config(text=comp_data[4],anchor="w")
        canvas.create_window(405, 220,window=inv_stax_canvas)
        canvas.create_text(320, 255, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(335, 285, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        canvas.create_text(315, 350, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_canv_name = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_canv_name.config(text=prev_data[18],anchor="w",bg="white")
        canvas.create_window(409, 370,window=inv_canv_name)
        inv_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_addr_canvas.insert("1.0",prev_data[19])
        inv_addr_canvas.config(state=DISABLED)
        canvas.create_window(395, 415, window=inv_addr_canvas)
        canvas.create_text(650, 350, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_ship_canv_lbl = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_ship_canv_lbl.config(text=prev_data[20],anchor="w",bg="white")
        canvas.create_window(751, 370, window=inv_ship_canv_lbl)
        inv_ship_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_ship_addr_canvas.insert("1.0",prev_data[21])
        inv_ship_addr_canvas.config(state=DISABLED)
        canvas.create_window(736, 415,window=inv_ship_addr_canvas)

        inv_header_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_header_canvas.config(text=prev_data[40],anchor="center",bg="white")
        canvas.create_window(637, 452,window=inv_header_canvas)
        
        s = ttk.Style()
        s.configure('Treeview.Heading', background='',State='DISABLE')
        inv_prev_tree = ttk.Treeview(canvas,height=12,style='mystyle.Treeview')
        inv_prev_tree["columns"] = ["1","2","3"]
        inv_prev_tree.column("#0",width=1)
        inv_prev_tree.column("1",width=394,anchor=CENTER)
        inv_prev_tree.column("2",width=150,anchor=CENTER)
        inv_prev_tree.column("3",width=150,anchor=CENTER)
        inv_prev_tree.heading("#0",text="")
        inv_prev_tree.heading("1",text="Product/Service - Description")
        inv_prev_tree.heading("2",text="Quantity")
        inv_prev_tree.heading("3",text="Price")
        window = canvas.create_window(285, 462, anchor="nw", window=inv_prev_tree)

        currency_sql = "SELECT currencysign,currsignplace FROM company"
        fbcursor.execute(currency_sql,)
        currency_symb = fbcursor.fetchone()

        storing_sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
        storing_val = (prev_data[1],)
        fbcursor.execute(storing_sql,storing_val)
        storing_data = fbcursor.fetchall()

        for record in storing_data:
          inv_prev_tree.insert(parent='', index='end',text='', values=(record[6] + "  -  " + record[7],record[9],record[13]))

        if not comp_data:
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          
          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "1":
          canvas.create_line(980, 723, 980, 873 )
          canvas.create_line(720, 723, 720, 873 )
          canvas.create_line(860, 723, 860, 873 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,786,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,811,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,836,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,861,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_bal1_canvas)
        elif comp_data[12] == "2":
          canvas.create_line(980, 723, 980, 898 )
          canvas.create_line(720, 723, 720, 898 )
          canvas.create_line(860, 723, 860, 898 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,811,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,836,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,861,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,886,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_bal1_canvas)
        elif comp_data[12] == "3":
          canvas.create_line(980, 723, 980, 923 )
          canvas.create_line(720, 723, 720, 923 )
          canvas.create_line(860, 723, 860, 923 )#1st
          canvas.create_line(980, 723, 720, 723 )
          canvas.create_line(980, 748, 720, 748 )
          canvas.create_line(980, 773, 720, 773 ) 
          canvas.create_line(980, 798, 720, 798 )
          canvas.create_line(980, 823, 720, 823 )
          canvas.create_line(980, 848, 720, 848 )
          canvas.create_line(980, 873, 720, 873 )
          canvas.create_line(980, 898, 720, 898 )
          canvas.create_line(980, 923, 720, 923 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0]+str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0] + " " + str(prev_data[36]),anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="center")
            canvas.create_window(790,737,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,737,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="center")
            canvas.create_window(790,761,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,761,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="center")
            canvas.create_window(790,786,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,786,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="center")
            canvas.create_window(790,811,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,811,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="center")
            canvas.create_window(790,836,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,836,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="center")
            canvas.create_window(790,861,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,861,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="center")
            canvas.create_window(790,886,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,886,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="center")
            canvas.create_window(790,911,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(925,911,window=inv_bal1_canvas)

        inv_prev_comments = Text(canvas,font=('Helvetica 10'),width=100,height=6,fg= "black",
        bg="white",cursor="arrow",bd=0)
        inv_prev_comments.insert("1.0",prev_data[44])
        inv_prev_comments.config(state=DISABLED)
        canvas.create_window(635, 980,window=inv_prev_comments)
        
        canvas.create_text(635, 1075, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(290, 1090, 982, 1090)
        
        inv_prev_terms = Text(canvas,font=('Helvetica 10'),width=100,height=4,fg= "black",bg="white",cursor="arrow",bd=0)
        inv_prev_terms.insert("1.0",prev_data[35])
        inv_prev_terms.tag_configure("tag_name", justify='left')
        inv_prev_terms.tag_add("tag_name", "1.0", "end")
        inv_prev_terms.config(state=DISABLED)
        canvas.create_window(642, 1125,window=inv_prev_terms)
        canvas.create_text(330, 1165, text="Sale Person:", fill="black", font=('Helvetica 10'))
        inv_prev_salesp = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_prev_salesp.config(text=prev_data[14],anchor="w",bg="white")
        canvas.create_window(502, 1165, window = inv_prev_salesp)
        inv_footer_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_footer_canvas.config(text=prev_data[41],anchor="w",bg="white")
        canvas.create_window(413, 1185,window=inv_footer_canvas)
    #----------------Business Classic------------------ 
      elif prev_data[13] == 'Business Classic':
        frame = Frame(prev_invo, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=5,y=30)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
        
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        
        canvas.config(width=1315,height=640)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235, 25, 1080, 1430 , outline='yellow',fill='white')
        inv_title_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_title_canvas.config(text=prev_data[39],anchor="center",bg="white")
        canvas.create_window(657, 50,window=inv_title_canvas)
        canvas.create_line(290, 70, 1025, 70, fill='orange')
        try:
          image = Image.open("images/"+comp_data[13])
          resize_image = image.resize((250, 125))
          logo_img = ImageTk.PhotoImage(resize_image)
          b2 = Label(canvas,image=logo_img, height=125, width=250,)
          b2.photo = logo_img
          canvas.create_window(417, 155,window=b2)
        except:
          pass
        canvas.create_text(629, 110, text=comp_data[1], fill="black", font=('Helvetica 10 bold'))
        comp_addr_canvas = Text(canvas,font=('Helvetica 10'),width=21,height=5,fg= "black",bg="white",cursor="arrow",bd=0,)
        comp_addr_canvas.insert("1.0",comp_data[2])
        comp_addr_canvas.tag_configure("tag_name", justify='left')
        comp_addr_canvas.tag_add("tag_name", "1.0", "end")
        comp_addr_canvas.config(state=DISABLED)
        canvas.create_window(628, 165,window=comp_addr_canvas)
        inv_stax_canvas = Label(canvas, font=('Helvetica 10 '),width=21,bg="white")
        inv_stax_canvas.config(text=comp_data[4],anchor="w")
        canvas.create_window(638, 220,window=inv_stax_canvas)
        

        inv_canv_name = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_canv_name.config(text=prev_data[18],anchor="w",bg="white")
        canvas.create_window(868, 110,window=inv_canv_name)
        inv_addr_canvas = Text(canvas,font=('Helvetica 10'),width=30,height=3,bd=0,fg= "black",
        bg="white",cursor="arrow")
        inv_addr_canvas.insert("1.0",prev_data[19])
        inv_addr_canvas.config(state=DISABLED)
        canvas.create_window(853, 157, window=inv_addr_canvas)
        
        canvas.create_text(765, 190, text="Invoice", fill="black", font=('Helvetica 10'))
        canvas.create_text(780, 210, text="Invoice date", fill="black", font=('Helvetica 10'))
        canvas.create_text(772, 230, text="Due date", fill="black", font=('Helvetica 10'))
        canvas.create_text(763, 250, text="Terms", fill="black", font=('Helvetica 10'))
        canvas.create_text(779, 270, text="Invoice ref.#", fill="black", font=('Helvetica 10'))
        inv_num_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_num_canvas.config(text=prev_data[1],anchor="w")
        canvas.create_window(963, 190,window=inv_num_canvas)
        canvas.create_text(900, 210, text=prev_data[2], fill="black", font=('Helvetica 11'))
        canvas.create_text(900, 230, text=prev_data[3], fill="black", font=('Helvetica 11'))
        inv_terms_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_terms_canvas.config(text=prev_data[42],anchor="w")
        canvas.create_window(963, 250,window=inv_terms_canvas)
        inv_ref_canvas = Label(canvas,font=('Helvetica 10'),width=25,bg='white')
        inv_ref_canvas.config(text=prev_data[43],anchor="w")
        canvas.create_window(963, 270,window=inv_ref_canvas) 

        inv_header_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_header_canvas.config(text=prev_data[40],anchor="center",bg="white")
        canvas.create_window(657, 290,window=inv_header_canvas)


        s = ttk.Style()
        s.configure('Treeview.Heading', background='',State='DISABLE')
        inv_prev_tree = ttk.Treeview(canvas,height=12,style='mystyle.Treeview')
        inv_prev_tree["columns"] = ["1","2","3","4","5"]
        inv_prev_tree.column("#0",width=1)
        inv_prev_tree.column("1",width=240,anchor=CENTER)
        inv_prev_tree.column("2",width=220,anchor=CENTER)
        inv_prev_tree.column("3",width=90,anchor=CENTER)
        inv_prev_tree.column("4",width=100,anchor=CENTER)
        inv_prev_tree.column("5",width=90,anchor=CENTER)
        inv_prev_tree.heading("#0",text="")
        inv_prev_tree.heading("1",text="Product/Service")
        inv_prev_tree.heading("2",text="Description")
        inv_prev_tree.heading("3",text="Quantity")
        inv_prev_tree.heading("4",text="Unit Price")
        inv_prev_tree.heading("5",text="Price")
        window = canvas.create_window(285, 300, anchor="nw", window=inv_prev_tree)
        
        
        currency_sql = "SELECT currencysign,currsignplace FROM company"
        fbcursor.execute(currency_sql,)
        currency_symb = fbcursor.fetchone()

        storing_sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
        storing_val = (prev_data[1],)
        fbcursor.execute(storing_sql,storing_val)
        storing_data = fbcursor.fetchall()

        for record in storing_data:
          inv_prev_tree.insert(parent='', index='end',text='', values=(record[6],record[7],record[8],record[9],record[13]))
        
        if not comp_data:
          canvas.create_line(1027, 560, 1027, 710 )
          canvas.create_line(720, 560, 720, 710 )
          canvas.create_line(1027, 560, 720, 560 )
          canvas.create_line(1027, 585, 720, 585 )
          canvas.create_line(1027, 610, 720, 610 ) 
          canvas.create_line(1027, 635, 720, 635 )
          canvas.create_line(1027, 660, 720, 660 )
          canvas.create_line(1027, 685, 720, 685 )
          canvas.create_line(1027, 710, 720, 710 )
          
          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
        elif comp_data[12] == "1":
          canvas.create_line(1027, 560, 1027, 710 )
          canvas.create_line(720, 560, 720, 710 )
          canvas.create_line(1027, 560, 720, 560 )
          canvas.create_line(1027, 585, 720, 585 )
          canvas.create_line(1027, 610, 720, 610 ) 
          canvas.create_line(1027, 635, 720, 635 )
          canvas.create_line(1027, 660, 720, 660 )
          canvas.create_line(1027, 685, 720, 685 )
          canvas.create_line(1027, 710, 720, 710 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,624,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,649,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,674,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,699,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_bal1_canvas)
        elif comp_data[12] == "2":
          canvas.create_line(1027, 560, 1027, 735 )
          canvas.create_line(720, 560, 720, 735 )
          canvas.create_line(1027, 560, 720, 560 )
          canvas.create_line(1027, 585, 720, 585 )
          canvas.create_line(1027, 610, 720, 610 ) 
          canvas.create_line(1027, 635, 720, 635 )
          canvas.create_line(1027, 660, 720, 660 )
          canvas.create_line(1027, 685, 720, 685 )
          canvas.create_line(1027, 710, 720, 710 )
          canvas.create_line(1027, 735, 720, 735 )

          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,649,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(971,649,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,674,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(971,674,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,699,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(971,699,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,724,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(971,724,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,649,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(971,649,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,674,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(971,674,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,699,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(971,699,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,724,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(971,724,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,649,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,674,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,699,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,724,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(971,724,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,649,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,674,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,699,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,724,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,724,window=inv_bal1_canvas)
        elif comp_data[12] == "3":
          canvas.create_line(1027, 560, 1027, 760 )
          canvas.create_line(720, 560, 720, 760 )
          canvas.create_line(1027, 560, 720, 560 )
          canvas.create_line(1027, 585, 720, 585 )
          canvas.create_line(1027, 610, 720, 610 ) 
          canvas.create_line(1027, 635, 720, 635 )
          canvas.create_line(1027, 660, 720, 660 )
          canvas.create_line(1027, 685, 720, 685 )
          canvas.create_line(1027, 710, 720, 710 )
          canvas.create_line(1027, 735, 720, 735 )
          canvas.create_line(1027, 760, 720, 760)
            
          if currency_symb[1] == "before amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0]+str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0]+str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0]+str(prev_data[16]),anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="w")
            canvas.create_window(784,649,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0]+str(prev_data[36]),anchor="e")
            canvas.create_window(971,649,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,674,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0]+str(prev_data[12]),anchor="e")
            canvas.create_window(971,674,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,699,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0]+str(prev_data[8]),anchor="e")
            canvas.create_window(971,699,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,724,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0]+str(prev_data[9]),anchor="e")
            canvas.create_window(971,724,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,749,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0]+str(prev_data[10]),anchor="e")
            canvas.create_window(971,749,window=inv_bal1_canvas)
          elif currency_symb[1] == "before amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=currency_symb[0] + " " + str(prev_data[31]),anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=currency_symb[0] + " " + str(prev_data[49]),anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=currency_symb[0] + " " + str(prev_data[16]),anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="w")
            canvas.create_window(784,649,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=currency_symb[0] + " " + str(prev_data[36]),anchor="e")
            canvas.create_window(971,649,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,674,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=currency_symb[0] + " " + str(prev_data[12]),anchor="e")
            canvas.create_window(984,674,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,699,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=currency_symb[0] + " " + str(prev_data[8]),anchor="e")
            canvas.create_window(971,699,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,724,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=currency_symb[0] + " " + str(prev_data[9]),anchor="e")
            canvas.create_window(971,724,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,749,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=currency_symb[0] + " " + str(prev_data[10]),anchor="e")
            canvas.create_window(971,749,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="w")
            canvas.create_window(784,649,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,674,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,699,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,724,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+currency_symb[0],anchor="e")
            canvas.create_window(971,724,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,749,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+currency_symb[0],anchor="e")
            canvas.create_window(971,749,window=inv_bal1_canvas)
          elif currency_symb[1] == "after amount with space":
            inv_dis_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_dis_canvas.config(text=str(prev_data[15]) + "" + "% Discount",anchor="w")
            canvas.create_window(784,574,window=inv_dis_canvas)
            inv_dis1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_dis1_canvas.config(text=str(prev_data[31])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,574,window=inv_dis1_canvas)

            inv_sub_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_sub_canvas.config(text="Subtotal",anchor="w")
            canvas.create_window(784,599,window=inv_sub_canvas)
            inv_sub1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_sub1_canvas.config(text=str(prev_data[49])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,599,window=inv_sub1_canvas)

            inv_TAX1_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX1_canvas.config(text="TAX1",anchor="w")
            canvas.create_window(784,624,window=inv_TAX1_canvas)
            inv_tax_1_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_1_canvas.config(text=str(prev_data[16])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,624,window=inv_tax_1_canvas)

            inv_TAX2_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_TAX2_canvas.config(text="TAX2",anchor="w")
            canvas.create_window(784,649,window=inv_TAX2_canvas)
            inv_tax_2_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_tax_2_canvas.config(text=str(prev_data[36])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,649,window=inv_tax_2_canvas)

            inv_excname_canvas = Label(canvas,font=('Helvetica 10'),width=15,bg='white')
            inv_excname_canvas.config(text=prev_data[11],anchor="w")
            canvas.create_window(784,674,window=inv_excname_canvas)
            inv_excost_canvas = Label(canvas,font=('Helvetica 10'),width=13,bg='white')
            inv_excost_canvas.config(text=str(prev_data[12])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,674,window=inv_excost_canvas)

            inv_tot_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_tot_canvas.config(text="Invoice Total",anchor="w")
            canvas.create_window(784,699,window=inv_tot_canvas)
            inv_tot1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_tot1_canvas.config(text=str(prev_data[8])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,699,window=inv_tot1_canvas)

            inv_totp_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_totp_canvas.config(text="Total Paid",anchor="w")
            canvas.create_window(784,724,window=inv_totp_canvas)
            inv_totp1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_totp1_canvas.config(text=str(prev_data[9])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,724,window=inv_totp1_canvas)

            inv_bal_canvas = Label(canvas,font=('Helvetica 10 bold'),width=15,bg='white')
            inv_bal_canvas.config(text="Balance",anchor="w")
            canvas.create_window(784,749,window=inv_bal_canvas)
            inv_bal1_canvas = Label(canvas,font=('Helvetica 10 bold'),width=13,bg='white')
            inv_bal1_canvas.config(text=str(prev_data[10])+ " " +currency_symb[0],anchor="e")
            canvas.create_window(971,749,window=inv_bal1_canvas)

        canvas.create_line(290, 810, 1030, 810, fill='orange')
        inv_prev_comments = Text(canvas,font=('Helvetica 10'),width=106,height=6,fg= "black",
        bg="white",cursor="arrow",bd=0)
        inv_prev_comments.insert("1.0",prev_data[44])
        inv_prev_comments.config(state=DISABLED)
        canvas.create_window(661, 860,window=inv_prev_comments)

        canvas.create_text(635, 1075, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(290, 1090, 1030, 1090, fill='orange')
        
        inv_prev_terms = Text(canvas,font=('Helvetica 10'),width=106,height=4,fg= "black",bg="white",cursor="arrow",bd=0)
        inv_prev_terms.insert("1.0",prev_data[35])
        inv_prev_terms.tag_configure("tag_name", justify='left')
        inv_prev_terms.tag_add("tag_name", "1.0", "end")
        inv_prev_terms.config(state=DISABLED)
        canvas.create_window(661, 1125,window=inv_prev_terms)
        canvas.create_text(330, 1165, text="Sale Person:", fill="black", font=('Helvetica 10'))
        inv_prev_salesp = Label(canvas, font=('Helvetica 10 '),width=30)
        inv_prev_salesp.config(text=prev_data[14],anchor="w",bg="white")
        canvas.create_window(502, 1165, window = inv_prev_salesp)
        inv_footer_canvas = Label(canvas,font=('Helvetica 10 '),width=30)
        inv_footer_canvas.config(text=prev_data[41],anchor="w",bg="white")
        canvas.create_window(413, 1185,window=inv_footer_canvas)
      else:
          pass

  

#------------------------------------------------------------------------------------------------convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
#--------------------------------------------------------------------------------------------------search in invoice 
def srh_rir():  
    def find_cus_row():
  
      if find_txt_var.get()=="Invoice#":
        
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and invoice_number=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="Next Invoice":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and next_invoice=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="Recurring Period":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and recurring_period=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="Stop After":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and stop_recurring=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="Customer Name":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and 	businessname=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="Invoice Total":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL and invoicetot=%s"
        rir_main_table_sql_qry=(fnd_srh_txt.get(),)
        fbcursor.execute(rir_main_table_sql,rir_main_table_sql_qry)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
      elif find_txt_var.get()=="<<All>>":
        for record in rir_tree.get_children():
          rir_tree.delete(record)
        rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL "
  
        fbcursor.execute(rir_main_table_sql)
        main_rir_val=fbcursor.fetchall()
        count_rir=0

        for i in main_rir_val:
            rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
            count_rir +=1

        top.destroy()
    def fnd_dist():
      top.destroy()

    top = Toplevel()  
    top.title("Find Text")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("520x150+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    fnd_srh_txt = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = fnd_srh_txt )
    findwhat.place(x=85,y=15,height=23) 
    findButton = Button(top, text ="Find next",width=10, command=lambda:find_cus_row())
    findButton.place(x=420,y=15)
    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    find_txt_var = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable =find_txt_var )
    findIN['values'] = ('Invoice#',  
                              'Next Invoice', 
                              'Recurring Period', 
                              'Stop After', 
                              'Customer Name', 
                              'Invoice Total',
                              '<<All>>')    
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)
    closeButton = Button(top, text ="Close",width=10, command=lambda:fnd_dist())
    closeButton.place(x=420,y=45)
   
    up_var = StringVar() 
    checkvarStatus4=IntVar()
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button4.select()
    Button4.place(x=60,y=80)
    checkvarStatus5=IntVar()  
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button5.select()
    Button5.place(x=270,y=80)
    top.mainloop()

#--------------------------calculator-recurring----------------------

def clcu_rcrir():
  subprocess.Popen('C:\\Windows\\System32\\calc.exe')


#edit/view invoice in recurring 

def view_invs_rir():
  pop=Toplevel(rirmidFrame)
  pop.title("Invoice")
  pop.geometry("950x690+150+0")
  
  #select customer
  def customer_invoice_recurring():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)
    ##------------------------------------------------------------------------------------------customer Filter
    def cus_filter_rir(event):
      selected_indices = cus_listbox.curselection()
      selected_font = ",".join([cus_listbox.get(i) for i in selected_indices])
 
      if selected_font== "             View all records":
        for record in cusventtree.get_children():
          cusventtree.delete(record)
        cus_main_table_sql="select * from customer"
        fbcursor.execute(cus_main_table_sql)
        main_tb_val=fbcursor.fetchall()
        
        count_cus=0

        for i in main_tb_val:
          cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
          
          count_cus +=1
      elif selected_font== "             View only Client/Vendor Type":
        for record in cusventtree.get_children():
          cusventtree.delete(record)
        cus_main_table_sql="select * from customer where customertype='Both(Client/Vender)'"
        fbcursor.execute(cus_main_table_sql)
        main_tb_val=fbcursor.fetchall()
        
        count_cus=0

        for i in main_tb_val:
          cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
          
          count_cus +=1
      elif selected_font=="             View only Client Type":
    
        for record in cusventtree.get_children():
          cusventtree.delete(record)
        cus_main_table_sql="select * from customer where customertype='Client'"
        fbcursor.execute(cus_main_table_sql)
        main_tb_val=fbcursor.fetchall()
        
        count_cus=0

        for i in main_tb_val:
          cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
          
          count_cus +=1
      elif selected_font=="             View only Vendor Type":
        for record in cusventtree.get_children():
          cusventtree.delete(record)
        cus_main_table_sql="select * from customer where customertype='Vender'"
        fbcursor.execute(cus_main_table_sql)
        main_tb_val=fbcursor.fetchall()
        
        count_cus=0

        for i in main_tb_val:
          cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
          
          count_cus +=1
      else:
        pass
    #add new customer
    def create_newcustomer_recurring():
      def cancel_add():
     
        add_customer.destroy()
      def cus_add_cst():
        cst_id=b1sd.get()#id
        cus_bs_nm=bnm_cus.get()
        if cst_id=="" or cus_bs_nm=="" :
              
          messagebox.showerror("Empty Field", "Customer ID field and Business Name field is Required!")

        else:
          
          #bs name
          # cmp_id=
          cus_bs_ad_cus=bdfdsfsd2.get("1.0",END)#bs ad name
          
          cus_bs_cnt=bs_cnt.get()#Contact person
          cus_bs_em=bs_em.get()#email bs
          cus_bs_tel=bs_tel.get()#bs tel
          cus_bs_fax=bs_fax.get()#bs fax
          cus_bs_mob=bs_mobi.get()#bs mob
          cus_bs_pymcheck=cus_ds_chk.get()# discount checkboc
          cus_bs_spc_tax=blsr.get()# specific tax
          cus_bs_spc_tax2=bdsfd14.get()# specific tax
          cus_bs_dis=b1f2.get()# discount
          cus_bs_ctr=bs_cus_ct.get()# customer category

          # ship 
          cus_shp_cat=cus_catg.get()# category
          cus_shp_st=cus_st.get()# status Checkbox
          cus_shp_cnt_pr=cus_sh_nam.get()#contact person
          cus_shp_adr=b2sds1.get("1.0",END)#contact address
          cus_shp_cnt=bs_sh_cnt.get()#Contact person
          cus_shp_em=bs_sh_em.get()#email bs
          cus_shp_tel=bs_sh_tel.get()#bs tel
          cus_shp_fax=bs_sh_fax.get()#bs fax
          cus_shp_cntry=cus_sh_coun.get()#contry
          cus_shp_city=cus_sh_cty.get()#city
          cus_shp_nte=scll.get("1.0", END)

          cus_ed_tbles="select customerno from customer where customerno=%s"
          cus_ed_tbles_valuz=(cst_id,)
          fbcursor.execute(cus_ed_tbles,cus_ed_tbles_valuz)
          cus_ins_val=fbcursor.fetchone()

          cus_ed_tbless="select businessname from customer where businessname=%s"
          cus_ed_tbless_valuz=(cus_bs_nm,)
          fbcursor.execute(cus_ed_tbless,cus_ed_tbless_valuz)
          cus_ins_valse=fbcursor.fetchone()
      
          if cus_ins_val is None:
            if cus_ins_valse is None:
              cus_tbl_add="INSERT INTO customer(customerno,category,status,businessname,businessaddress,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,specifictax1,discount,country,city,customertype,notes,specifictax2)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
              cus_tbl_add_val=(cst_id,cus_shp_cat,cus_shp_st,cus_bs_nm,cus_bs_ad_cus,cus_shp_cnt_pr,cus_shp_adr,cus_bs_cnt,cus_bs_em,cus_bs_tel,cus_bs_fax,cus_bs_mob,cus_shp_cnt,cus_shp_em,cus_shp_tel,cus_shp_fax,cus_bs_pymcheck,cus_bs_spc_tax,cus_bs_dis,cus_shp_cntry,cus_shp_city,cus_bs_ctr,cus_shp_nte,cus_bs_spc_tax2)
              fbcursor.execute(cus_tbl_add,cus_tbl_add_val)
              fbilldb.commit()
              for record in cusventtree.get_children():
                cusventtree.delete(record)
              cus_main_table_sql="select * from customer"
              fbcursor.execute(cus_main_table_sql)
              main_tb_val=fbcursor.fetchall()
              count_cus=0

              for i in main_tb_val:
                cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
                count_cus +=1
              
              add_customer.destroy()
            else:
              messagebox.showerror("Already Exists", "Customer ID value already exists. Duplicate value not allowed")
          else:
              messagebox.showerror("Already Exists", "Business name is already exists. Duplicate value not allowed")
      
      def top_btn():
          cus_bs_nm=bnm_cus.get()
          cus_bs_ad_cus=bdfdsfsd2.get("1.0",END)#bs ad name
          b1fr1.delete(0,'end')
          b1fr1.insert(0,cus_bs_nm)
          b2sds1.delete(1.0,'end')
          b2sds1.insert(1.0,cus_bs_ad_cus)

      def btm_btn():
          cus_bs_cnt=bs_cnt.get()#Contact person
          cus_bs_em=bs_em.get()#email bs
          cus_bs_tel=bs_tel.get()#bs tel
          cus_bs_fax=bs_fax.get()#bs fax
          b141sd.insert(0,cus_bs_cnt)
          b21vcvc1.delete(0,'end')
          b21vcvc1.insert(0,cus_bs_em)
          b3zx1.delete(0,'end')
          b3zx1.insert(0,cus_bs_tel)
          b4x141.delete(0,'end')
          b4x141.insert(0,cus_bs_fax)



      add_customer = Toplevel()  
      add_customer.title("Add new Customer ")
      p2 = PhotoImage(file = "images/fbicon.png")
      add_customer.iconphoto(False, p2)
      add_customer.geometry("775x580+300+100")
      Labelframe1=LabelFrame(add_customer,text="Customer")
      Labelframe1.place(x=10,y=10,width=755,height=525)
      a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
      a2=Label(Labelframe1,text="Category:")
      a3=Label(Labelframe1,text="Status :")
      a3.place(x=620,y=7)
      cu_idr=IntVar() 
      b1sd=Entry(Labelframe1)
      cus_catg=StringVar() 
      b2=ttk.Combobox(Labelframe1,textvariable = cus_catg)    
      sql_cust_dt='SELECT DISTINCT category from customer'
      fbcursor.execute(sql_cust_dt)
      catgry=fbcursor.fetchall()
      b2['values'] = catgry 
      b2.place(x=390,y=220) 
      b2.current(0)
      a1.place(x=10,y=7)
      a2.place(x=330,y=7)   
      b1sd.place(x=120,y=7,width=200)
      b2.place(x=390,y=7,width=220)
      cus_st = IntVar()
      chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = cus_st, onvalue = 1, offvalue = 0)
      chkbtn1.select()
      chkbtn1.place(x=670,y=6)


      Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
      Labelframe2.place(x=10,y=35,width=340,height=125)
      a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
      a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
      bnm_cus=StringVar()
      bs_adr_cus=StringVar()
      
      

      b1=Entry(Labelframe2, textvariable=bnm_cus)
      # b1.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
      b1.place(x=110,y=10,width=210)

      bdfdsfsd2=scrolledtext.ScrolledText(Labelframe2)
      bdfdsfsd2.place(x=110,y=35,width=210,height=63)  
      btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:top_btn()).place(x=359,y=85,height=20)


      Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
      Labelframe3.place(x=400,y=35,width=340,height=125)
      a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
      a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
      cus_sh_nam=StringVar()
      cus_sh_adr=StringVar()
      b1fr1=Entry(Labelframe3, textvariable=cus_sh_nam)
      b1fr1.place(x=110,y=10,width=210)
      b2sds1=scrolledtext.ScrolledText(Labelframe3)
      b2sds1.place(x=110,y=35,width=210,height=63)


      Labelframe4=LabelFrame(Labelframe1,text="Contact")
      Labelframe4.place(x=10,y=170,width=340,height=137)
      a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
      a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
      a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
      a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
      a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
      bs_cnt=StringVar()
      bs_em=StringVar()
      bs_tel=StringVar()
      bs_fax=StringVar()
      bs_mobi=StringVar()
      b11=Entry(Labelframe4, textvariable=bs_cnt).place(x=110,y=10,width=210)

      #-------------------------------------------------------------------------------------------Email Validation
      b21=Entry(Labelframe4,textvariable=bs_em)
      

      def validate(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern, value) is None:
                
                return False

            b21.config(fg="black")
            return True

      def on_invalid():
            b21.config(fg="red")
            
      vcmd = (Labelframe2.register(validate), '%P')
      ivcmd = (Labelframe2.register(on_invalid),)

      b21.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
      
      b21.place(x=110,y=35,width=210)

      b311=Entry(Labelframe4,textvariable=bs_tel)
      def validate_tel(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'^[0-9]\d{9,10}$'
            if re.fullmatch(pattern, value) is None:
                
                return False
            b311.config(fg="black")
            return True

      def on_invalid_tel():
            b311.config(fg="red")
            
      v_tel_cmd = (Labelframe2.register(validate_tel), '%P')
      iv_tel_cmd = (Labelframe2.register(on_invalid_tel),)
      
      
      b311.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
      b311.place(x=110,y=60,width=90)

      b4126=Entry(Labelframe4,textvariable=bs_fax)
      def validate_telb4126(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
            if re.fullmatch(pattern, value) is None:
                
                return False
            b4126.config(fg="black")
            return True

      def on_invalid_telb4126():
            b4126.config(fg="red")
            
      v_tel_cmdb4126 = (Labelframe2.register(validate_telb4126), '%P')
      iv_tel_cmdb4126 = (Labelframe2.register(on_invalid_telb4126),)
      b4126.config(validate='focusout', validatecommand=v_tel_cmdb4126, invalidcommand=iv_tel_cmdb4126)
      b4126.place(x=230,y=60,width=90)
      
      b51=Entry(Labelframe4,textvariable=bs_mobi)
      def validate_telb51(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'^[0-9]\d{9}$'
            if re.fullmatch(pattern, value) is None:
                
                return False
            b51.config(fg="black")
            return True

      def on_invalid_telb51():
            b51.config(fg="red")
            
      v_tel_cmdb51 = (Labelframe2.register(validate_telb51), '%P')
      iv_tel_cmdb51 = (Labelframe2.register(on_invalid_telb51),)
      b51.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)
      b51.place(x=215,y=85,width=105)
      btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:btm_btn()).place(x=359,y=220,height=20)

      bs_sh_cnt=StringVar()
      bs_sh_em=StringVar()
      bs_sh_tel=StringVar()
      bs_sh_fax=StringVar()

      Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
      Labelframe5.place(x=400,y=170,width=340,height=108)
      a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
      a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
      a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
      a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
    
      b141sd=Entry(Labelframe5, textvariable=bs_sh_cnt)
      b141sd.place(x=110,y=10,width=210)
      
      b21vcvc1=Entry(Labelframe5,textvariable=bs_sh_em)
      def validateb211(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern, value) is None:
                
                return False

            b21vcvc1.config(fg="black")
            return True

      def on_invalidb211():
            b21vcvc1.config(fg="red")
            
      vcmdb211 = (Labelframe2.register(validateb211), '%P')
      ivcmdb211 = (Labelframe2.register(on_invalidb211),)

      b21vcvc1.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
      b21vcvc1.place(x=110,y=35,width=210)
      
      b3zx1=Entry(Labelframe5,textvariable=bs_sh_tel)
      def validate_telb31(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'^[0-9]\d{9,10}$'
            if re.fullmatch(pattern, value) is None:
                
                return False
            b3zx1.config(fg="black")
            return True

      def on_invalid_telb31():
            b3zx1.config(fg="red")
            
      v_tel_cmdb31 = (Labelframe2.register(validate_telb31), '%P')
      iv_tel_cmdb31 = (Labelframe2.register(on_invalid_telb31),)
      b3zx1.config(validate='focusout', validatecommand=v_tel_cmdb31, invalidcommand=iv_tel_cmdb31)
      b3zx1.place(x=110,y=60,width=90)

      b4x141=Entry(Labelframe5,textvariable=bs_sh_fax)
      def validate_telb4141(value):
            
            """
            Validat the email entry
            :param value:
            :return:
            """
            pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
            if re.fullmatch(pattern, value) is None:
                
                return False
            b4x141.config(fg="black")
            return True

      def on_invalid_telb4141():
            b4x141.config(fg="red")
            
      v_tel_cmdb4141 = (Labelframe2.register(validate_telb4141), '%P')
      iv_tel_cmdb4141 = (Labelframe2.register(on_invalid_telb4141),)
      b4x141.config(validate='focusout', validatecommand=v_tel_cmdb4141, invalidcommand=iv_tel_cmdb4141)
      b4x141.place(x=230,y=60,width=90)


      Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
      Labelframe6.place(x=10,y=317,width=340,height=80)
      cus_ds_chk = StringVar()
      cus_sp_tx=IntVar()
      cus_sp_tx2=IntVar()
      cus_sp_disc=IntVar()
      chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = cus_ds_chk, onvalue = 1, offvalue = 0, font=("arial", 8))
      chkbtn1.place(x=10,y=6)
      chkbtn1.select()

      
      a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
      
      cus_sp_disc = IntVar(Labelframe6)
      
      
      #-----------------------------------------------------------------------------------------------tax2
      swt='select taxtype from company'
      fbcursor.execute(swt)
      fdt=fbcursor.fetchone()
      def tax_frt(S,d):
          if d=='1':
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
            
          if d.isdigit():
            return True


      edt_lty=(Labelframe6.register(tax_frt), '%S','%d')
      blsr=Entry(Labelframe6, textvariable=cus_sp_tx)
      bdsfd14=Entry(Labelframe6)
      if fdt[0]=='3':
        a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
        blsr=Entry(Labelframe6, )
        
        # edt_ltyr=(Labelframe6.register(tax_frtinv),)
        blsr.config(validate='key',validatecommand=(edt_lty))
        blsr.place(x=250,y=7,width=70)
        
        bdsfd14.config(validate='key',validatecommand=(edt_lty))
        bdsfd14.place(x=250,y=30,width=70)
        a16=Label(Labelframe6,text="Specific Tax2%::").place(x=150,y=30)
      elif fdt[0]=='2':
        a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
        
        blsr.config(validate='key',validatecommand=(edt_lty))
        blsr.place(x=250,y=7,width=70)
      elif fdt[0]=='1':
        pass
      b1f2=Entry(Labelframe6)
      b1f2.config(validate='key',validatecommand=(edt_lty))
      b1f2.place(x=80,y=30,width=70)

      Labelframe7=LabelFrame(Labelframe1,text="Customer type")
      Labelframe7.place(x=10,y=405,width=340,height=90)
      bs_cus_ct=StringVar()
      r1=Radiobutton(Labelframe7, text = "Client", variable = bs_cus_ct, value ="Client")
      r1.select()
      r1.place(x=5,y=15)
      
      r2=Radiobutton(Labelframe7, text = "Vender", variable = bs_cus_ct, value = "Vender")
      r2.deselect()
      r2.place(x=90,y=15)
      r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = bs_cus_ct, value = "Both(Client/Vender)")
      r3.deselect()
      r3.place(x=180,y=15)


      Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
      Labelframe8.place(x=400,y=288,width=340,height=80)
      a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
      a12=Label(Labelframe8,text="City:").place(x=10,y=30)
      cus_sh_coun=StringVar() 
      cus_sh_cty=StringVar() 

      b11=ttk.Combobox(Labelframe8,textvariable=cus_sh_coun)
      b11.place(x=110,y=5,width=210)
      b11['values'] = ('India','America')    
      
      b11.place(x=110,y=5) 
      b12=Entry(Labelframe8,textvariable=cus_sh_cty).place(x=110,y=30,width=210)
      Labelframe9=LabelFrame(Labelframe1,text="Notes")
      Labelframe9.place(x=400,y=380,width=340,height=115)
      '''scrollbar = Scrollbar(Labelframe9)
            scrollbar.place(x=300,y=10)
            b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
            yscrollcommand.config(command=b12.yview)'''
      cus_nt=StringVar()
      global scll
      scll=scrolledtext.ScrolledText(Labelframe9)
      scll.place(x=20,y=10,width=295,height=70)
      # scrollbar_cus_nt = Scrollbar(Labelframe9)
      # scrollbar_cus_nt.place(x=295,y=10)

      btn1=Button(add_customer,width=50,compound = LEFT,image=tick ,command=lambda:cus_add_cst(),text="  OK").place(x=20, y=545)
      btn2=Button(add_customer,width=80,compound = LEFT,image=cancel,text="  Cancel",command=cancel_add).place(x=665, y=545)
      add_customer.mainloop()
    def edit_sltd_cust_rir():
      # try:
      
        cus_id=cusventtree.item(cusventtree.focus())["values"][0]
        cus_ed_tbles="select * from customer where customerno=%s"
        cus_ed_tbles_valuz=(cus_id,)
        fbcursor.execute(cus_ed_tbles,cus_ed_tbles_valuz)
        cus_ins_val=fbcursor.fetchone()

        def cancel_edt():
          edit_customer.destroy()

        def cus_edit_cst():
          
                cst_id=b1s.get()#id
              
                cus_bs_nm=bnm_cus.get()#bs name

                cus_bs_ad_cus=bnjh2.get('1.0',END)#bs ad name
                cus_bs_cnt=bs_cnt.get()#Contact person
                cus_bs_em=bs_em.get()#email bs
                cus_bs_tel=bs_tel.get()#bs tel
                cus_bs_fax=bs_fax.get()#bs fax
                cus_bs_mob=bs_mobi.get()#bs mob
                cus_bs_pymcheck=cus_ds_chk.get()# discount checkboc
                cus_bs_spc_tax=cus_sp_tx.get()# specific tax
                cus_bs_spc_tax2=cus_sp_tx2.get()
                cus_bs_dis=cus_sp_disc.get()# discount
                cus_bs_ctr=bs_cus_ct.get()# customer category

                # ship 
                cus_shp_cat=cus_catg.get()# category
                cus_shp_st=cus_st.get()# status Checkbox
                cus_shp_cnt_pr=cus_sh_nam.get()#contact person
                cus_shp_adr=b2vxcvcxbc1.get("1.0",END)#contact address
                cus_shp_cnt=bs_sh_cnt.get()#Contact person
                cus_shp_em=bs_sh_em.get()#email bs
                cus_shp_tel=bs_sh_tel.get()#bs tel
                cus_shp_fax=bs_sh_fax.get()#bs fax
                cus_shp_cntry=cus_sh_coun.get()#contry
                cus_shp_city=cus_sh_cty.get()#city
                cus_shp_ntre=cfgd.get("1.0", END) 
                
                cus_ed_tbless="select businessname from customer where businessname=%s"
                cus_ed_tbless_valuz=(cus_bs_nm,)
                fbcursor.execute(cus_ed_tbless,cus_ed_tbless_valuz)
                cus_ins_valse=fbcursor.fetchone()
              
                cus_tbl_edit="update customer set customerno=%s,category=%s,status=%s,businessname=%s,businessaddress=%s,shipname=%s,shipaddress=%s,contactperson=%s,cpemail=%s,cptelno=%s,cpfax=%s,cpmobileforsms=%s,shipcontactperson=%s,shipcpemail=%s,shipcptelno=%s,shipcpfax=%s,taxexempt=%s,specifictax1=%s,discount=%s,country=%s,city=%s,customertype=%s,notes=%s, specifictax2=%s where customerno = %s" #adding values into db
                cus_tbl_edit_val=(cst_id,cus_shp_cat,cus_shp_st,cus_bs_nm,cus_bs_ad_cus,cus_shp_cnt_pr,cus_shp_adr,cus_bs_cnt,cus_bs_em,cus_bs_tel,cus_bs_fax,cus_bs_mob,cus_shp_cnt,cus_shp_em,cus_shp_tel,cus_shp_fax,cus_bs_pymcheck,cus_bs_spc_tax,cus_bs_dis,cus_shp_cntry,cus_shp_city,cus_bs_ctr,cus_shp_ntre,cus_bs_spc_tax2,cus_id,)
                fbcursor.execute(cus_tbl_edit,cus_tbl_edit_val)
                fbilldb.commit()
                cus_main_s=ttk.Style()
                for record in cusventtree.get_children():
                  cusventtree.delete(record)
                cus_main_table_sql="select * from customer"
                fbcursor.execute(cus_main_table_sql)
                main_tb_val=fbcursor.fetchall()
                count_cus=0

                for i in main_tb_val:
                  cusventtree.insert(parent='', index='end', iid=count_cus, values=(i[24],i[4],i[10],i[8]))
                  count_cus +=1
                edit_customer.destroy()
                  

        def top_SHP_btn():
          cus_bs_nm=bnm_cus.get()#bs name
          # cmp_id=
          cus_bs_ad_cus=bnjh2.get("1.0",END)#bs ad name
          b1fdgfg1.delete(0,'end')
          b1fdgfg1.insert(0,cus_bs_nm)
          b2vxcvcxbc1.delete(1.0,'end')
          b2vxcvcxbc1.insert(1.0,cus_bs_ad_cus)

        def btm_shp_btn():
            
            cus_bs_cnt=bs_cnt.get()#Contact person
            cus_bs_em=bs_em.get()#email bs
            cus_bs_tel=bs_tel.get()#bs tel
            cus_bs_fax=bs_fax.get()#bs fax
            b1dsf1.delete(0,'end')
            b1dsf1.insert(0,cus_bs_cnt)
            b21cd1.delete(0,'end')
            b21cd1.insert(0,cus_bs_em)
            b311.delete(0,'end')
            b311.insert(0,cus_bs_tel)
            b414.delete(0,'end')
            b414.insert(0,cus_bs_fax)
        edit_customer = Toplevel()  
        edit_customer.title("Add new Customer ")
        p2 = PhotoImage(file = "images/fbicon.png")
        edit_customer.iconphoto(False, p2)
        edit_customer.geometry("775x580+300+100")
        Labelframe1=LabelFrame(edit_customer,text="Customer")
        Labelframe1.place(x=10,y=10,width=755,height=525)
        a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
        a2=Label(Labelframe1,text="Category:")
        a3=Label(Labelframe1,text="Status :")
        a3.place(x=620,y=7)
      
        b1s=Entry(Labelframe1)
        
        b1s.insert(0,cus_ins_val[24])
        b1s.config(state=DISABLED,disabledbackground="white",disabledforeground="black")
        cus_catg=StringVar() 
        b2=ttk.Combobox(Labelframe1,textvariable = cus_catg) 
        sql_cust_dt='SELECT DISTINCT category from customer'
        fbcursor.execute(sql_cust_dt)
        catgry=fbcursor.fetchall()    
        b2['values'] = catgry  
        b2.place(x=390,y=220) 
        b2.current(cus_ins_val[3])
        a1.place(x=10,y=7)
        a2.place(x=330,y=7)   
        b1s.place(x=120,y=7,width=200)
        b2.place(x=390,y=7,width=220)
        cus_st = IntVar()
        chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = cus_st, onvalue = 1, offvalue = 0)
        if cus_ins_val[3]=="0":
          chkbtn1.deselect()
        else:
          chkbtn1.select()
        chkbtn1.place(x=670,y=6)

        Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
        Labelframe2.place(x=10,y=35,width=340,height=125)
        a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
        a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
        bnm_cus=StringVar()
        bs_adr_cus=StringVar()
        b1=Entry(Labelframe2, textvariable=bnm_cus)
        b1.insert(0,cus_ins_val[4])
        b1.place(x=110,y=10,width=210)
        bnjh2=scrolledtext.ScrolledText(Labelframe2) 
        
        bnjh2.insert(1.0,cus_ins_val[5])
        bnjh2.place(x=110,y=35,width=210,height=63) 
        # b1.place(x=359,y=85,height=20)
        btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:top_SHP_btn()).place(x=359,y=85,height=20)


        Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
        Labelframe3.place(x=400,y=35,width=340,height=125)
        a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
        a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
        cus_sh_nam=StringVar()
        cus_sh_adr=StringVar()
        b1fdgfg1=Entry(Labelframe3, textvariable=cus_sh_nam)
        b1fdgfg1.insert(0,str(cus_ins_val[6]))
        b1fdgfg1.place(x=110,y=10,width=210)
        b2vxcvcxbc1=scrolledtext.ScrolledText(Labelframe3)
        b2vxcvcxbc1.delete(1.0,'end')
        b2vxcvcxbc1.insert(1.0,str(cus_ins_val[7]))
        b2vxcvcxbc1.place(x=110,y=35,width=210,height=63)
        


        Labelframe4=LabelFrame(Labelframe1,text="Contact")
        Labelframe4.place(x=10,y=170,width=340,height=137)
        a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
        
        a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
        a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
        a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
        a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
        
        bs_cnt=StringVar()
        bs_em=StringVar()
        bs_tel=StringVar()
        bs_fax=StringVar()
        
        b11=Entry(Labelframe4, textvariable=bs_cnt)
        b11.insert(0,str(cus_ins_val[8]))
        b11.place(x=110,y=10,width=210)
        
        b21=Entry(Labelframe4,textvariable=bs_em)
        def validate(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b21.config(fg="black")
              return True

        def on_invalid():
              b21.config(fg="red")
              
        vcmd = (Labelframe4.register(validate), '%P')
        ivcmd = (Labelframe4.register(on_invalid),)

        
        
        b21.insert(0,str(cus_ins_val[9]))
        b21.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        b21.place(x=110,y=35,width=210)
        
        def validate_tel(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9,10}$'
              if re.fullmatch(pattern, value) is None:
                  return False
                  
              b31.config(fg="black")
              return True

        def on_invalid_tel():
            b31.config(fg="red")
        
            
        v_tel_cmd = (Labelframe4.register(validate_tel), '%P')
        iv_tel_cmd = (Labelframe4.register(on_invalid_tel),)

        b31=Entry(Labelframe4,textvariable=bs_tel)
        b31.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
        b31.insert(0,str(cus_ins_val[10]))

        b31.place(x=110,y=60,width=90)
        b4126=Entry(Labelframe4,textvariable=bs_fax)
        def validate_telb4126(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b4126.config(fg="black")
              return True

        def on_invalid_telb4126():
              b4126.config(fg="red")
              
        v_tel_cmdb4126 = (Labelframe4.register(validate_telb4126), '%P')
        iv_tel_cmdb4126 = (Labelframe4.register(on_invalid_telb4126),)
        b4126.config(validate='focusout', validatecommand=v_tel_cmdb4126, invalidcommand=iv_tel_cmdb4126)
        b4126.insert(0,str(cus_ins_val[11]))
        b4126.place(x=230,y=60,width=90)
        bs_mobi=StringVar()
        b5fd1=Entry(Labelframe4,textvariable=bs_mobi)
        def validate_tel3(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9}$'
              if re.fullmatch(pattern, value) is None:
                  return False
                  
              b5fd1.config(fg="black")
              return True

        def on_invalid_tel3():
            b5fd1.config(fg="red")
        
        v_tel_cmd3 = (Labelframe4.register(validate_tel3), '%P')
        iv_tel_cmd3 = (Labelframe4.register(on_invalid_tel3),)
        b5fd1.insert(0,str(cus_ins_val[12]))
        b5fd1.config(validate='focusout', validatecommand=v_tel_cmd3, invalidcommand=iv_tel_cmd3)
      
        b5fd1.place(x=215,y=85,width=105)
        btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>",command=lambda:btm_shp_btn())
        btn111.place(x=359,y=220,height=20)
      
        bs_sh_cnt=StringVar()
        bs_sh_em=StringVar()
        bs_sh_tel=StringVar()
        bs_sh_fax=StringVar()
    
        Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
        Labelframe5.place(x=400,y=170,width=340,height=108)
        a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
        a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
        a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
        a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
        
        b1dsf1=Entry(Labelframe5, textvariable=bs_sh_cnt)
        b1dsf1.insert(0,str(cus_ins_val[13]))
        b1dsf1.place(x=110,y=10,width=210)
        b21cd1=Entry(Labelframe5,textvariable=bs_sh_em)
        

        def validateb21(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
              if re.fullmatch(pattern, value) is None:
                  
                  return False

            
              b21cd1.config(fg="black")
              return True

        def on_invalidb21():
              b21cd1.config(fg="red")
              
        vcmdb21 = (Labelframe5.register(validateb21), '%P')
        ivcmdb21 = (Labelframe5.register(on_invalidb21),)
        
        b21cd1.config(validate='focusout', validatecommand=vcmdb21, invalidcommand=ivcmdb21)
        b21cd1.insert(0,str(cus_ins_val[14]))
        b21cd1.place(x=110,y=35,width=210)
        b311=Entry(Labelframe5,textvariable=bs_sh_tel)
        def validate_telb311(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9,10}$'
              if re.fullmatch(pattern, value) is None:
                  return False
                  
              b311.config(fg="black")
              return True

        def on_invalid_telb311():
            b311.config(fg="red")
        v_tel_cmdb311 = (Labelframe5.register(validate_telb311), '%P')
        iv_tel_cmdb311 = (Labelframe5.register(on_invalid_telb311),)

        b311.insert(0,str(cus_ins_val[15]))
        b311.config(validate='focusout', validatecommand=v_tel_cmdb311, invalidcommand=iv_tel_cmdb311)
        b311.place(x=110,y=60,width=90)

        b414=Entry(Labelframe5,textvariable=bs_sh_fax)
        def validate_telb414(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b414.config(fg="black")
              return True

        def on_invalid_telb414():
              b414.config(fg="red")
              
        v_tel_cmdb414 = (Labelframe5.register(validate_telb414), '%P')
        iv_tel_cmdb414 = (Labelframe5.register(on_invalid_telb414),)
        b414.config(validate='focusout', validatecommand=v_tel_cmdb414, invalidcommand=iv_tel_cmdb414)

        b414.insert(0,str(cus_ins_val[16]))
        b414.place(x=230,y=60,width=90)


        Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
        Labelframe6.place(x=10,y=317,width=340,height=80)
        cus_ds_chk = StringVar()
        cus_sp_tx=IntVar()
        cus_sp_tx2=IntVar()
        cus_sp_disc=IntVar()
        chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = cus_ds_chk, onvalue = 1, offvalue = 0, font=("arial", 8))
        if cus_ins_val[17]=="0":
          chkbtn1.deselect()
        else:
          chkbtn1.select()
        chkbtn1.place(x=10,y=6)

        
        a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
        cus_sp_disc = IntVar(Labelframe6)

        cus_sp_disc=Entry(Labelframe6)
        
          # edt_ltyr=(Labelframe6.register(tax_frtinv),)
        def tax_frt(S,d):
            if d=='1':
              if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
                return False
              return True
              
            if d.isdigit():
              return True


        edt_lty=(Labelframe6.register(tax_frt), '%S','%d')

        cus_sp_disc.insert(0,str(cus_ins_val[19]))
        cus_sp_disc.config(validate='key',validatecommand=(edt_lty))
        cus_sp_disc.place(x=80,y=30,width=70)

        swt='select taxtype from company'
        fbcursor.execute(swt)
        fdt=fbcursor.fetchone()
        print(fdt[0])
        cus_sp_tx=Entry(Labelframe6)
        cus_sp_tx2=Entry(Labelframe6)
        cus_sp_tx=Entry(Labelframe6)
        if fdt[0]=='3':

          a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
          
          cus_sp_tx.insert(0,str(cus_ins_val[18]))
          cus_sp_tx.config(validate='key',validatecommand=(edt_lty))
          cus_sp_tx.place(x=250,y=7,width=70)
          
          cus_sp_tx2.insert(0,str(cus_ins_val[25]))
          cus_sp_tx2.config(validate='key',validatecommand=(edt_lty))
          cus_sp_tx2.place(x=250,y=30,width=70)
          
          a16=Label(Labelframe6,text="Specific Tax2%::").place(x=150,y=30)
        elif fdt[0]=='2':
          a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
          
          cus_sp_tx.insert(0,str(cus_ins_val[18]))
          cus_sp_tx.config(validate='key',validatecommand=(edt_lty))
          cus_sp_tx.place(x=250,y=7,width=70)
        elif fdt[0]=='1':
          pass

        Labelframe7=LabelFrame(Labelframe1,text="Customer type")
        Labelframe7.place(x=10,y=405,width=340,height=90)
        bs_cus_ct=StringVar()
        r1=Radiobutton(Labelframe7, text = "Client", variable = bs_cus_ct, value ="Client")
        r2=Radiobutton(Labelframe7, text = "Vender", variable = bs_cus_ct, value = "Vender")
        r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = bs_cus_ct, value = "Both(Client/Vender)")
        if cus_ins_val[22]=="Client":
          r1.select()
          r2.deselect()
          r3.deselect()
        elif cus_ins_val[22]=="Vender":
          r1.deselect()
          r2.select()
          r3.deselect()
        else:
          r1.deselect()
          r2.deselect()
          r3.select()
        r1.place(x=5,y=15)
        r2.place(x=90,y=15)
        r3.place(x=180,y=15)

        Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
        Labelframe8.place(x=400,y=288,width=340,height=80)
        a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
        a12=Label(Labelframe8,text="City:").place(x=10,y=30)
        cus_sh_coun=StringVar() 
        cus_sh_cty=StringVar() 

        b11=ttk.Combobox(Labelframe8,textvariable=cus_sh_coun)
        b11.place(x=110,y=5,width=210)
        b11['values'] = ('India','America')  
        b11.insert(0,str(cus_ins_val[20]))  
        b11.place(x=110,y=5) 
        b12=Entry(Labelframe8,textvariable=cus_sh_cty)
        b12.insert(0,str(cus_ins_val[21]))  
        b12.place(x=110,y=30,width=210)
        Labelframe9=LabelFrame(Labelframe1,text="Notes")
        Labelframe9.place(x=400,y=380,width=340,height=115)
        '''scrollbar = Scrollbar(Labelframe9)
              scrollbar.place(x=300,y=10)
              b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
              yscrollcommand.config(command=b12.yview)'''
        cus_nt=StringVar()
        global cfgd
        cfgd=scrolledtext.ScrolledText(Labelframe9)
        cfgd.insert(1.0,str(str(cus_ins_val[23])))
        cfgd.place(x=20,y=10,width=295,height=70)
        # scrollbar_cus_nt = Scrollbar(Labelframe9)
        # scrollbar_cus_nt.place(x=295,y=10)

        btn1=Button(edit_customer,width=50,compound = LEFT,image=tick ,command=lambda:cus_edit_cst(),text="  OK").place(x=20, y=545)
        btn2=Button(edit_customer,width=80,compound = LEFT,image=cancel,text="  Cancel", command=cancel_edt).place(x=665, y=545)
        edit_customer.mainloop()
      # except:
      #   pass    
    def cncl_cuselection():
      cuselection.destroy()


    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)

    cus_vnt_try="select * from customer"
    fbcursor.execute(cus_vnt_try)
    cus_vnty=fbcursor.fetchall()
    count_vnty=0

    for i in cus_vnty:
        cusventtree.insert(parent='', index='end', iid=count_vnty, values=(i[24],i[4],i[10],i[8]))
        count_vnty +=1


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    cus_listbox = Listbox(cuselection,height =34,  
                      width = 40)  
    cus_listbox.insert(0, "             View all records")
    cus_listbox.insert(1, "             View only Client/Vendor Type")
    cus_listbox.insert(2, "             View only Client Type")
    cus_listbox.insert(3, "             View only Vendor Type")

    cus_listbox.place(x=660,y=63)
    cus_listbox.bind('<<ListboxSelect>>', cus_filter_rir)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=ctegorytree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=edit_sltd_cust_rir)
    btn1.place(x=250, y=610)
    btn2=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create_newcustomer_recurring)
    btn2.place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", command=cncl_cuselection, width=60).place(x=740, y=610)   
 
  #add new line item
  #add new line item
  def recurring_New_newline():
      # businessname = recur_combo_name1.get()
      # sql='SELECT * FROM estimate WHERE businessname=%s'
      # val=(businessname,)
      # fbcursor.execute(sql,val)
      
      recur_newselection=Toplevel()
      recur_newselection.title("Select Product")
      recur_newselection.geometry("930x650+240+10")
      recur_newselection.resizable(False, False)


      #add new product
      def recur_product():  
        recur_top = Toplevel()  
        recur_top.title("Add a new Product/Service")
        recur_p2 = PhotoImage(file = 'images/fbicon.png')
        recur_top.iconphoto(False, recur_p2)
      
        recur_top.geometry("600x550+390+15")
        recur_tabControl = ttk.Notebook(recur_top)
        recur_s = ttk.Style()
        recur_s.theme_use('default')
        recur_s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        recur_tab1 = ttk.Frame(recur_tabControl)
        recur_tab2 = ttk.Frame(recur_tabControl)
      
        recur_tabControl.add(recur_tab1,compound = LEFT, text ='Product/Service')
        recur_tabControl.add(recur_tab2,compound = LEFT, text ='Product Image')
      
        recur_tabControl.pack(expand = 1, fill ="both")

        global filename
        filename = ""

        def este_upload_file():
          global filename,img, b2
          f_types =[('Png files','.png'),('Jpg Files', '.jpg'),('PDF', '*.pdf',)]
          filename = filedialog.askopenfilename(filetypes=f_types)
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          image = Image.open(filename)
          resize_image = image.resize((350, 350))
          img = ImageTk.PhotoImage(resize_image)
          b2 = Button(recur_imageFrame,image=img)
          b2.place(x=130, y=80)

        
        def est_addproducts():
          global img , filename 
          sku = recur_codeentry.get()
          status = recur_checkvarStatus.get()
          catgory = recur_n.get()
          name = recur_nameentry.get()
          description = recur_desentry.get()
          unitprice = recur_uval.get()
          peices = recur_pcsentry.get()
          cost = recur_costval.get()
          price_cost = recur_priceval.get()
          taxable = recur_checkvarStatus2.get()
          tax2 = recur_checkvarStatus_2.get()
          nostockcontrol = recur_checkvarStatus3.get()
          stock = recur_stockentry.get()
          lowstock = recur_lowentry.get()
          warehouse = recur_wareentry.get()
          pnotes = recur_txt.get("1.0",'end-1c')
          entries = [sku,name, unitprice, cost]
          entri = []
          for i in entries:
            if i == '':
              entri.append(i)
          if len(entri) == 0:
            sql = 'select * from Productservice where sku = %s or name = %s'
            val  = (sku, name)
            fbcursor.execute(sql, val)
            fbcursor.fetchall()
            row_count = fbcursor.rowcount
            if row_count == 0:
              if filename == "":
                sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
                val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2)
                fbcursor.execute(sql, val)
                fbilldb.commit()
              else:
                file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
                sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, image, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
                val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, filename.split('/')[-1], pnotes,tax2)
                fbcursor.execute(sql, val)
                fbilldb.commit()
            else:
              messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
              recur_top.destroy()

            for record in recur_cusventtree1.get_children():
              recur_cusventtree1.delete(record)
            fbcursor.execute("select *  from Productservice")
            est_pandsdata = fbcursor.fetchall()
            countp = 0
            for i in est_pandsdata:
              if i[12] == '1':
                servi = '🗹'
              else:
                servi = ''
              sql = "select currencysign,currsignplace from company"
              fbcursor.execute(sql)
              estcurrsymb = fbcursor.fetchone()
              if not estcurrsymb: 
                if i[13] > i[14]:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                  countp += 1              
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                  countp += 1
                        
              elif estcurrsymb[1] == "before amount":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "before amount with space":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "after amount":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "after amount with space":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1

            recur_top.destroy()
  
    
        recur_innerFrame = Frame(recur_tab1,bg="#f5f3f2", relief=GROOVE)
        recur_innerFrame.pack(side="top",fill=BOTH)

        recur_Customerlabelframe = LabelFrame(recur_innerFrame,text="Product/Service",width=580,height=455)
        recur_Customerlabelframe.pack(side="top",fill=BOTH,padx=10,pady=(10,45))

        fbcursor.execute("SELECT * FROM Productservice ORDER BY sku DESC LIMIT 1")
        skuin = fbcursor.fetchone()

        recur_code1=Label(recur_Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        recur_code1.place(x=20,y=0)
        recur_codeentry = Entry(recur_Customerlabelframe,width=35)
        recur_codeentry.place(x=120,y=8)

        recur_checkvarStatus=IntVar()
        recur_status1=Label(recur_Customerlabelframe,text="Status:")
        recur_status1.place(x=400,y=8)
        recur_Button1 = Checkbutton(recur_Customerlabelframe,
                          variable = recur_checkvarStatus,text="Active",compound="right",
                          onvalue =1,
                          offvalue = 0,
                        
                          width = 10)

        recur_Button1.place(x=450,y=5)

        recur_category1=Label(recur_Customerlabelframe,text="Category:",pady=5,padx=10)
        recur_category1.place(x=20,y=40)
        recur_n = StringVar()
        recur_country0 = ttk.Combobox(recur_Customerlabelframe, width = 40, textvariable = recur_n )
        recur_country0['values'] = ('Default')
        recur_country0.place(x=120,y=45)
        recur_country0.insert(0, 'Default')


        recur_name81=Label(recur_Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        recur_name81.place(x=20,y=70)
        recur_nameentry = Entry(recur_Customerlabelframe,width=60)
        recur_nameentry.place(x=120,y=75)

        recur_des1=Label(recur_Customerlabelframe,text="Description :",pady=5,padx=10)
        recur_des1.place(x=20,y=100)
        recur_desentry = Entry(recur_Customerlabelframe,width=60)
        recur_desentry.place(x=120,y=105)
        def est_prdoucts_cal(S,d):
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
          if d.isdigit():
            return True


        recur_uval = StringVar(value="0")
        recur_unit1=Label(recur_Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        recur_unit1.place(x=20,y=130)
        recur_unitentry = Entry(recur_Customerlabelframe,width=20,textvariable=recur_uval)
        recur_unitentry.place(x=120,y=135)
        est_cal_unit = (recur_Customerlabelframe.register(est_prdoucts_cal),'%S','%d')
        recur_unitentry.config(validate='key',validatecommand=(est_cal_unit),justify='right')

        # recur_pcsval = IntVar(recur_Customerlabelframe, value='$0.00')
        recur_pcs1=Label(recur_Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        recur_pcs1.place(x=330,y=135)
        recur_pcsentry = Entry(recur_Customerlabelframe,width=20)
        recur_pcsentry.place(x=420,y=140)

        recur_costval = StringVar(value="0")
        recur_cost1=Label(recur_Customerlabelframe,text="Cost:",pady=5,padx=10)
        recur_cost1.place(x=20,y=160)
        recur_costentry = Entry(recur_Customerlabelframe,width=20,textvariable=recur_costval)
        recur_costentry.place(x=120,y=165)
        est_cal_cost = (recur_Customerlabelframe.register(est_prdoucts_cal),'%S','%d')
        recur_costentry.config(validate='key',validatecommand=(est_cal_cost),justify='right')


        def est_set_label(name, index, mode):
          est_copr = float(recur_uval.get()) - float(recur_costval.get())
          recur_priceval.set(str(est_copr))


        recur_priceval = StringVar()
        recur_price1=Label(recur_Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        recur_price1.place(x=20,y=190)
        recur_priceentry = Entry(recur_Customerlabelframe,width=20,textvariable=recur_priceval,state=DISABLED,disabledbackground="white",disabledforeground="black")
        recur_priceentry.config(justify="right")
        recur_priceentry.place(x=120,y=195)


        recur_uval.trace('w', est_set_label)
        recur_costval.trace('w', est_set_label)

        sql = "select taxtype from company"
        fbcursor.execute(sql)
        est_taxchoose = fbcursor.fetchone()

        recur_checkvarStatus2=IntVar()
      
        recur_Button92 = Checkbutton(recur_Customerlabelframe,variable = recur_checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =1 ,
                          offvalue = 0,
                          height=2,
                          width = 12)

        #recur_Button92.place(x=415,y=170)

        recur_checkvarStatus_2=IntVar()
      
        recur_Button_92 = Checkbutton(recur_Customerlabelframe,variable = recur_checkvarStatus_2,
                          text="Taxable Tax2rate",compound="right",
                          onvalue =1,
                          offvalue =0,
                          height=2,
                          width = 12)

        #recurrecur_Button_92.place(x=415,y=210)
        if not est_taxchoose:
          pass
        elif est_taxchoose[0] == '1':
          recur_Button92.place_forget()
          recur_Button_92.place_forget()
        elif est_taxchoose[0] == '2':
          recur_Button92.place(x=415,y=170)
          recur_Button_92.place_forget()
        elif est_taxchoose[0] == '3':
          recur_Button92.place(x=415,y=170)
          recur_Button_92.place(x=415,y=210)

        def est_switch():
          if recur_checkvarStatus3.get():
            recur_stockentry["state"] = DISABLED
            recur_lowentry["state"] = DISABLED
            recur_wareentry["state"] = DISABLED
          else:
            recur_stockentry["state"] = NORMAL
            recur_lowentry["state"] = NORMAL
            recur_wareentry["state"] = NORMAL
        
        recur_checkvarStatus3=BooleanVar()
        recur_Button93 = Checkbutton(recur_Customerlabelframe,variable = recur_checkvarStatus3,command=est_switch, 
                          text="This is a service(no stock control)",
                          onvalue =1 ,
                          offvalue =0,
                          height=3)
        recur_Button93.place(x=40,y=220)

        def est_stocknum(input):
          if input.isdigit():
            return True
          elif input is "":
            return True
          else:
            return False


        
        recur_stock1=Label(recur_Customerlabelframe,text="Stock:",pady=5,padx=10)
        recur_stock1.place(x=90,y=260)
        recur_stockentry = Entry(recur_Customerlabelframe,width=15)
        recur_stockentry.place(x=150,y=265)
        est_sto = recur_Customerlabelframe.register(est_stocknum)
        recur_stockentry.config(validate="key",validatecommand=(est_sto, '%S'))

        
        recur_low1=Label(recur_Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        recur_low1.place(x=270,y=260)
        recur_lowentry = Entry(recur_Customerlabelframe,width=10)
        recur_lowentry.place(x=432,y=265)
        est_lowsto = recur_Customerlabelframe.register(est_stocknum)
        recur_lowentry.config(validate="key",validatecommand=(est_lowsto, '%S'))

      
        recur_ware1=Label(recur_Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        recur_ware1.place(x=60,y=290)
        recur_wareentry = Entry(recur_Customerlabelframe,width=50)
        recur_wareentry.place(x=150,y=295)

        recur_text10=Label(recur_Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        recur_text10.place(x=20,y=330)

        recur_txt = scrolledtext.ScrolledText(recur_Customerlabelframe, undo=True,width=62,height=4)
        recur_txt.place(x=32,y=358)




        recur_okButton = Button(recur_innerFrame,compound = LEFT,image=tick , text ="Ok",width=60,command=est_addproducts)
        recur_okButton.place(x=10,y=475)

        def est_closetab():
          recur_top.destroy()


        recur_cancelButton = Button(recur_innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60,command=est_closetab)
        recur_cancelButton.place(x=519,y=475)

        recur_imageFrame = Frame(recur_tab2, relief=GROOVE,height=580)
        recur_imageFrame.pack(side="top",fill=BOTH)
        

        recur_browseimg=Label(recur_imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        recur_browseimg.place(x=15,y=35)

        recur_browsebutton=Button(recur_imageFrame,text = 'Browse',command=este_upload_file)
        recur_browsebutton.place(x=520,y=30,height=30,width=50)
        
        recur_removeButton = Button(recur_imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150, command=lambda: b2.destroy())
        recur_removeButton.place(x=400,y=450)
      
      # ###---------------Edit product-----------------###    
      def est_edit_product(): 
        edit_est_itemid = recur_cusventtree1.item(recur_cusventtree1.focus())["values"][0]  
        global filename
        filename = ""
      
        def edit_estupload_file():
          global filename,img, b2
          f_types =[('Png files','.png'),('Jpg Files', '.jpg')]
          filename = filedialog.askopenfilename(filetypes=f_types)
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          image = Image.open(filename)
          resize_image = image.resize((350, 350))
          img = ImageTk.PhotoImage(resize_image)
          edit_est_b2 = Button(edit_est_imageFrame,image=img)
          edit_est_b2.place(x=130, y=80)
        
        def edit_est_updateproducts():
          global img , filename,sku,name,description,unitprice,peices,price_cost,taxable,tax2
          sku = edit_est_codeentry.get()
          status = edit_est_checkvarStatus.get()
          catgory = edit_est_n.get()
          name = edit_est_nameentry.get()
          description = edit_est_desentry.get()
          unitprice = edit_est_uval.get()
          peices = edit_est_pcsentry.get()
          cost = edit_est_costval.get()
          price_cost = edit_est_priceval.get()
          taxable = edit_est_checkvarStatus2.get()
          tax2 = edit_est_checkvarStatustax2.get()
          nostockcontrol = edit_est_checkvarStatus3.get()
          stock = edit_est_stockval.get()
          lowstock = edit_est_lowval.get()
          warehouse = edit_est_wareentry.get()
          pnotes = edit_est_sctxt.get("1.0", 'end-1c')
          entries = [sku, name, unitprice, cost]
          entri = []
          for i in entries:
            if i == '':
              entri.append(i)
          if len(entri) == 0:
            if filename == "":
              print("hello")
              sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, privatenote=%s,tax2=%s where sku = %s"
              val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2, edit_est_itemid)
              fbcursor.execute(sql, val)
              fbilldb.commit()
            else:
              print("hai")
              file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
              sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s, privatenote=%s,tax2=%s where sku = %s"
              val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse,filename.split('/')[-1], pnotes,tax2, edit_est_itemid)
              fbcursor.execute(sql, val)
              fbilldb.commit()
            for record in recur_cusventtree1.get_children():
              recur_cusventtree1.delete(record)
            fbcursor.execute("select *  from Productservice")
            edit_est_pandsdata = fbcursor.fetchall()
            countp = 0
            for i in edit_est_pandsdata:
              if i[12] == '1':
                servi = '🗹'
              else:
                servi = ''
              sql = "select currencysign,currsignplace from company"
              fbcursor.execute(sql)
              estcurrsymb = fbcursor.fetchone()
              if not estcurrsymb: 
                if i[13] > i[14]:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                  countp += 1              
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                  countp += 1
                        
              elif estcurrsymb[1] == "before amount":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "before amount with space":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "after amount":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1

              elif estcurrsymb[1] == "after amount with space":
                if (i[13]) > (i[14]):
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
                  countp += 1
                else:
                  recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
                  countp += 1
            edit_est_top.destroy()
          else:
            messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
            edit_est_top.destroy()
            

        sql = "select * from Productservice where sku = %s"
        val = (edit_est_itemid, )
        fbcursor.execute(sql, val)
        edit_est_psdata = fbcursor.fetchone()
        
        edit_est_top = Toplevel()  
        edit_est_top.title("Edit Product/Service details")
        p3 = PhotoImage(file = 'images/fbicon.png')
        edit_est_top.iconphoto(False, p3)
        edit_est_top.geometry("600x550+350+15")
        tabControl = ttk.Notebook(edit_est_top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)

        edit_est_taba = ttk.Frame(tabControl)
        edit_est_tabb = ttk.Frame(tabControl)
        
        tabControl.add(edit_est_taba,compound = LEFT, text ='Product/Service')
        tabControl.add(edit_est_tabb,compound = LEFT, text ='Product Image')
        
        tabControl.pack(expand = 1, fill ="both")
        
        edit_est_innerFrame = Frame(edit_est_taba,bg="#f5f3f2", relief=GROOVE)
        edit_est_innerFrame.pack(side="top",fill=BOTH)

        edit_est_updateframe = LabelFrame(edit_est_innerFrame,text="Product/Service",width=580,height=455)
        edit_est_updateframe.pack(side="top",fill=BOTH,padx=10,pady=(10,45))

        edit_est_code1=Label(edit_est_updateframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        edit_est_code1.place(x=20,y=0)
        edit_est_codeentry = Entry(edit_est_updateframe,width=35)
        edit_est_codeentry.place(x=120,y=8)
        edit_est_codeentry.insert(0, edit_est_psdata[2])

        edit_est_checkvarStatus=IntVar()
        edit_est_status1=Label(edit_est_updateframe,text="Status:")
        edit_est_status1.place(x=400,y=8)
        edit_est_Button1 = Checkbutton(edit_est_updateframe, 
                          variable = edit_est_checkvarStatus,text="Active",compound="right",
                          onvalue =1,
                          offvalue =0,
                          width = 10)
        edit_est_Button1.place(x=450,y=5)
        edit_est_sta = edit_est_psdata[6]
        if edit_est_sta == '1':
          edit_est_Button1.select()
        else:
          edit_est_Button1.deselect()



        edit_est_category1=Label(edit_est_updateframe,text="Category:",pady=5,padx=10)
        edit_est_category1.place(x=20,y=40)
        edit_est_n = StringVar() 
        edit_est_category = Entry(edit_est_updateframe,width=40,textvariable=edit_est_n) 
        edit_est_category.insert(0, edit_est_psdata[3])
        edit_est_category = ttk.Combobox(edit_est_updateframe, width = 40, textvariable = edit_est_n )
        edit_est_category['values'] = ('Default')
        edit_est_category.place(x=120,y=45)
        #edit_est_category.insert(0, 'Default')



        edit_est_name1=Label(edit_est_updateframe,text="Name :",fg="blue",pady=5,padx=10)
        edit_est_name1.place(x=20,y=70)
        edit_est_nameentry = Entry(edit_est_updateframe,width=70)
        edit_est_nameentry.place(x=120,y=75)
        edit_est_nameentry.insert(0, edit_est_psdata[4])

        edit_est_des1=Label(edit_est_updateframe,text="Description :",pady=5,padx=10)
        edit_est_des1.place(x=20,y=100)
        edit_est_desentry = Entry(edit_est_updateframe,width=70)
        edit_est_desentry.place(x=120,y=105)
        edit_est_desentry.insert(0, edit_est_psdata[5])

        def edit_est_set_label(name, index, mode):
          edit_est_priceval.set(float(edit_est_uval.get()) - float(edit_est_costval.get()))

        def edit_est_prdoucts_cal(S,d):
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
          if d.isdigit():
            return True
        
        edit_est_unit1=Label(edit_est_updateframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        edit_est_unit1.place(x=20,y=130)
        
        edit_est_uval = StringVar()
        edit_est_unitentry = Entry(edit_est_updateframe,width=20,textvariable=edit_est_uval)
        edit_est_unitentry.place(x=120,y=135)
        edit_est_unitentry.delete(0,'end')
        edit_est_unitentry.insert(0, edit_est_psdata[7])
        edit_est_cal_unit = (edit_est_updateframe.register(edit_est_prdoucts_cal),'%S','%d')
        edit_est_unitentry.config(validate='key',validatecommand=(edit_est_cal_unit),justify='right')
        

        edit_est_pcsval = IntVar()
        edit_est_pcs1=Label(edit_est_updateframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        edit_est_pcs1.place(x=330,y=135)
        edit_est_pcsentry = Entry(edit_est_updateframe,width=20,textvariable=edit_est_pcsval)
        edit_est_pcsentry.place(x=420,y=140)
        edit_est_pcsentry.delete(0,'end')
        edit_est_pcsentry.insert(0, edit_est_psdata[8])
        

        edit_est_costval = StringVar()
        edit_est_cost1=Label(edit_est_updateframe,text="Cost:",pady=5,padx=10)
        edit_est_cost1.place(x=20,y=160)
        edit_est_costentry = Entry(edit_est_updateframe,width=20,textvariable=edit_est_costval)
        edit_est_costentry.place(x=120,y=165)
        edit_est_costentry.delete(0, END)
        edit_est_costentry.insert(0, edit_est_psdata[9])
        edit_est_cal_cost = (edit_est_updateframe.register(edit_est_prdoucts_cal),'%S','%d')
        edit_est_costentry.config(validate='key',validatecommand=(edit_est_cal_cost),justify='right')
        

        edit_est_priceval = StringVar()
        edit_est_price1=Label(edit_est_updateframe,text="(Price-Cost):",pady=5,padx=10)
        edit_est_price1.place(x=20,y=190)
        edit_est_priceentry = Entry(edit_est_updateframe,width=20,textvariable=edit_est_priceval,state=DISABLED,disabledbackground="white",disabledforeground="black")
        edit_est_priceentry.config(justify="right")
        edit_est_priceentry.place(x=120,y=195)
        edit_est_priceentry.delete(0,'end')
        edit_est_priceentry.insert(0, edit_est_psdata[11])

        edit_est_uval.trace('w', edit_est_set_label)
        edit_est_costval.trace('w', edit_est_set_label)
        

        edit_est_checkvarStatus2=IntVar()
      
        edit_est_Button2 = Checkbutton(edit_est_updateframe,variable = edit_est_checkvarStatus2, 
                          text="Taxable Tax1rate",compound="right",
                          onvalue =1 ,
                          offvalue =0,
                          height=2,
                          width = 12)
        
        edit_est_checkvarStatustax2=IntVar()
        edit_est_Buttontax2 = Checkbutton(edit_est_updateframe,variable = edit_est_checkvarStatustax2, 
                        text="Taxable Tax2rate",compound="right",
                        onvalue =1 ,
                        offvalue = 0,
                        height=2,
                        width = 12)
        
        sql = "select taxtype from company"
        fbcursor.execute(sql)
        edit_est_taxchoose = fbcursor.fetchone()
        if not edit_est_taxchoose:
          pass
        elif edit_est_taxchoose[0] == '1':
          edit_est_Button2.place_forget()
          edit_est_Buttontax2.place_forget()
        elif edit_est_taxchoose[0] == '2':
          edit_est_Button2.place(x=415,y=170)
          edit_est_Buttontax2.place_forget()
        elif edit_est_taxchoose[0] == '3':
          edit_est_Button2.place(x=415,y=170)
          edit_est_Buttontax2.place(x=415,y=210)

    
        edit_est_tax = edit_est_psdata[10]
        if edit_est_tax == '1':
          edit_est_Button2.select()
        else:
          edit_est_Button2.deselect()

        if edit_est_psdata[19] == '1':
          edit_est_Buttontax2.select()
        else:
          edit_est_Buttontax2.deselect()

        def edit_est_switch():
          if edit_est_checkvarStatus3.get():
            edit_est_stockentry["state"] = DISABLED
            edit_est_lowentry["state"] = DISABLED
            edit_est_wareentry["state"] = DISABLED
          else:
            edit_est_stockentry["state"] = NORMAL
            edit_est_lowentry["state"] = NORMAL
            edit_est_wareentry["state"] = NORMAL
        edit_est_checkvarStatus3=BooleanVar()
      
        edit_est_Button3 = Checkbutton(edit_est_updateframe,variable = edit_est_checkvarStatus3,command=edit_est_switch, 
                          text="This is a service(no stock control)", 
                          onvalue =1 ,
                          offvalue = 0,
                          height=3)

        edit_est_Button3.place(x=40,y=220)

        

        def edit_est_stocknum(input):
          if input.isdigit():
            return True
          elif input is "":
            return True
          else:
            return False
        edit_est_stockval = IntVar(edit_est_updateframe)
        edit_est_stock1=Label(edit_est_updateframe,text="Stock:",pady=5,padx=10)
        edit_est_stock1.place(x=90,y=260)
        edit_est_stockentry = Entry(edit_est_updateframe,width=15,textvariable=edit_est_stockval)
        edit_est_stockentry.place(x=150,y=265)
        edit_est_stockentry.delete(0,'end')
        edit_est_stockentry.insert(0, edit_est_psdata[13])
        edit_est_sto = edit_est_updateframe.register(edit_est_stocknum)
        edit_est_stockentry.config(validate="key",validatecommand=(edit_est_sto, '%S'))
        

        edit_est_lowval = IntVar(edit_est_updateframe)
        edit_est_low1=Label(edit_est_updateframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        edit_est_low1.place(x=270,y=260)
        edit_est_lowentry = Entry(edit_est_updateframe,width=15,textvariable=edit_est_lowval)
        edit_est_lowentry.place(x=432,y=265)
        edit_est_lowentry.delete(0,'end')
        edit_est_lowentry.insert(0, edit_est_psdata[14])
        edit_est_lowsto = edit_est_updateframe.register(edit_est_stocknum)
        edit_est_lowentry.config(validate="key",validatecommand=(edit_est_lowsto, '%S'))
        

      
        edit_est_ware1=Label(edit_est_updateframe,text="Warehouse:",pady=5,padx=10)
        edit_est_ware1.place(x=60,y=290)
        edit_est_wareentry = Entry(edit_est_updateframe,width=64)
        edit_est_wareentry.place(x=150,y=295)
        edit_est_wareentry.insert(0, edit_est_psdata[15])

        edit_est_scr = edit_est_psdata[12]
        if edit_est_scr == '1':
          edit_est_Button3.select()
          edit_est_stockentry["state"] = DISABLED
          edit_est_lowentry["state"] = DISABLED
          edit_est_wareentry["state"] = DISABLED
        else:
          edit_est_Button3.deselect()
          edit_est_stockentry["state"] = NORMAL
          edit_est_lowentry["state"] = NORMAL
          edit_est_wareentry["state"] = NORMAL
        
        

        

        edit_est_text1=Label(edit_est_updateframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        edit_est_text1.place(x=20,y=330)
        edit_est_sctxt = scrolledtext.ScrolledText(edit_est_updateframe, undo=True,width=62,height=4)
        edit_est_sctxt.place(x=32,y=358)
        try:
          edit_est_sctxt.insert("1.0", edit_est_psdata[16])
        except:
          pass

        edit_est_okButton = Button(edit_est_innerFrame, text ="Ok",image=tick,width=70,compound = LEFT,command=edit_est_updateproducts)
        edit_est_okButton.place(x=10, y=475)

        edit_est_cancelButton = Button(edit_est_innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=lambda : edit_est_top.destroy())
        edit_est_cancelButton.place(x=519, y=475)
        
        
        edit_est_imageFrame = Frame(edit_est_tabb, relief=GROOVE,height=580)
        edit_est_imageFrame.pack(side="top",fill=BOTH)
        # for record in recur_cusventtree1.get_children():
        #   recur_cusventtree1.delete(record)
        # doc_sql1 = "SELECT * FROM productservice WHERE sku=%s"
        # doc_val1 = (edit_est_itemid,)
        # fbcursor.execute(doc_sql1,doc_val1)
        # doc_details1 = fbcursor.fetchall()
        # print(doc_details1)
        # countdocc = 0
        # for doc1 in doc_details1:
        #   file_size_31 = est_check_convertion(os.path.getsize("images/"+doc1[17]))
        #   recurrecur_cusventtree1.insert(parent='',index='end',iid=doc1,text='',values=('',doc1[17],file_size_31))
        # countdocc += 1

        edit_est_browseimg=Label(edit_est_imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        edit_est_browseimg.place(x=15,y=35)

        edit_est_browsebutton=Button(edit_est_imageFrame,text = 'Browse',command=edit_estupload_file)
        edit_est_browsebutton.place(x=530,y=30,height=30,width=50)

        try:
          image = Image.open("images/"+edit_est_psdata[17])
          resize_image = image.resize((350, 350))
          image = ImageTk.PhotoImage(resize_image)
          edit_est_b2 = Label(edit_est_imageFrame,image=image,width=350,height=350)
          edit_est_b2.photo = image
          edit_est_b2.place(x=130, y=80)
        except:
          pass

        edit_est_removeButton = Button(edit_est_imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT,command=lambda: edit_est_b2 .destroy())
        edit_est_removeButton.place(x=410,y=460)
      
      def cncl_prd():
        recur_newselection.destroy()
      recur_enter10=Label(recur_newselection, text="Enter filter text").place(x=5, y=10)
      recur_e10=Entry(recur_newselection, width=20)
      recur_e10.place(x=110, y=10)
      # recur_text10=Label(recur_newselection, text="Filtered column").place(x=340, y=10)
      # recur_e20=Entry(recur_newselection, width=20).place(x=450, y=10)
      recur_pro_filter_button=Button(recur_newselection, text='Click Here')
      recur_pro_filter_button.place(x=240, y=9,height=20,width=60)

      
      
      global recur_cusventtree1
      recur_cusventtree1=ttk.Treeview(recur_newselection, height=25)
      recur_cusventtree1["columns"]=["1","2","3", "4","5"]
      recur_cusventtree1.column("#0", width=35)
      recur_cusventtree1.column("1", width=160)
      recur_cusventtree1.column("2", width=160)
      recur_cusventtree1.column("3", width=140)
      recur_cusventtree1.column("4", width=70)
      recur_cusventtree1.column("5", width=70)
      recur_cusventtree1.heading("#0",text="")
      recur_cusventtree1.heading("1",text="ID/SKU")
      recur_cusventtree1.heading("2",text="Product/Service Name")
      recur_cusventtree1.heading("3",text="Unit price")
      recur_cusventtree1.heading("4",text="Service")
      recur_cusventtree1.heading("5",text="Stock")
      recur_cusventtree1.tag_configure('green', foreground='green')
      recur_cusventtree1.tag_configure('red', foreground='red')
      recur_cusventtree1.tag_configure('blue', foreground='blue')
      
    
      countp = 0
      sql = 'select * from Productservice'
      fbcursor.execute(sql)
      estprodata = fbcursor.fetchall()
      for i in estprodata:
        if i[12] == '1':
          servi = '🗹'
        else:
          servi = ''
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        estcurrsymb = fbcursor.fetchone()
        if not estcurrsymb: 
          if i[13] > i[14]:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
            countp += 1
                  
        elif estcurrsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
            countp += 1

        elif estcurrsymb[1] == "before amount with space":
          if (i[13]) > (i[14]):
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
            countp += 1

        elif estcurrsymb[1] == "after amount":
          if (i[13]) > (i[14]):
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
            countp += 1

        elif estcurrsymb[1] == "after amount with space":
          if (i[13]) > (i[14]):
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
            countp += 1
          else:
            recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
            countp += 1
      recur_cusventtree1.place(x=5, y=45)
      

      recur_ctegorytree1=ttk.Treeview(recur_newselection, height=25)
      recur_ctegorytree1["columns"]=["1"]
      recur_ctegorytree1.column("#0", width=35, minwidth=20)
      recur_ctegorytree1.column("1", width=205, minwidth=25, anchor=CENTER)    
      recur_ctegorytree1.heading("#0",text="", anchor=W)
      recur_ctegorytree1.heading("1",text="View filter by category", anchor=CENTER)
      recur_ctegorytree1.place(x=660, y=45)
      def est_items_selected(event):
        selected_indices = est_fil_cat_list.curselection()
        selected_filter = ",".join([est_fil_cat_list.get(i) for i in selected_indices])

        sql = 'select * from Productservice'
        fbcursor.execute(sql)
        pandsdata = fbcursor.fetchall()
        psql = "select * from Productservice where serviceornot=%s"
        val = ('0', )
        fbcursor.execute(psql, val)
        pdata = fbcursor.fetchall()

        ssql = "select * from Productservice where serviceornot=%s"
        val = ('1', )
        fbcursor.execute(ssql, val)
        sdata = fbcursor.fetchall()

        if selected_filter == "View all records":
          for record in recur_cusventtree1.get_children():
            recur_cusventtree1.delete(record)
          countp = 0
          for i in pandsdata:
            if i[12] == '1':
              servi = '🗹'                     #'Active'
            else:
              servi = ' '                         #'Inactive'
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            estcurrsymb = fbcursor.fetchone()
            if not estcurrsymb: 
              if i[13] > i[14]:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                countp += 1
                      
            elif estcurrsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "before amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

        elif selected_filter == "View all products":
          for record in recur_cusventtree1.get_children():
            recur_cusventtree1.delete(record)
          countp = 0
          for i in pdata:
            if i[12] == '1':
              servi = '🗹'                   #'Active'
            else:
              servi = ' '                    #'Inactive'
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            estcurrsymb = fbcursor.fetchone()
            if not estcurrsymb: 
              if i[13] > i[14]:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                countp += 1
                      
            elif estcurrsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "before amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1
        elif selected_filter == "View all services":
          for record in recur_cusventtree1.get_children():
            recur_cusventtree1.delete(record)
          countp = 0
          for i in sdata:
            if i[12] == '1':
              servi = '🗹'             #'Active'
            else:
              servi = ' '              #'Inactive'
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            estcurrsymb = fbcursor.fetchone()
            if not estcurrsymb: 
              if i[13] > i[14]:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                countp += 1
                      
            elif estcurrsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0]+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "before amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],estcurrsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

            elif estcurrsymb[1] == "after amount with space":
              if (i[13]) > (i[14]):
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('blue',))
                countp += 1
              else:
                recur_cusventtree1.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+" "+estcurrsymb[0],servi,i[13]),tags=('red',))
                countp += 1

      est_fil_cat_list = Listbox(recur_newselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      est_fil_cat_list.insert(0,"View all records")
      est_fil_cat_list.insert(1,"View all products")
      est_fil_cat_list.insert(2,"View all services")
      est_fil_cat_list.place(x=660,y=63)
      est_fil_cat_list.bind('<<ListboxSelect>>',est_items_selected)
      est_stockok = Label(recur_newselection,text="Green: Stock is Ok",foreground="green").place(x =15,y =580)
      est_stocko = Label(recur_newselection,text="Red: Limit <= Low Stock Limit",foreground="red").place(x =136,y=580)
      est_stock = Label(recur_newselection,text="Blue: Service,no Stock Control",foreground="blue").place(x =335,y =580)


      recur_scrollbar10 = Scrollbar(recur_newselection)
      recur_scrollbar10.place(x=640, y=45, height=520)
      recur_scrollbar10.config( command=recur_cusventtree1.yview )

      def estselepro():
        global estpriceview
        estpriceview = Label(prd_tree,bg="#f5f3f2")
        estpriceview.place(x=850,y=200,width=78,height=18)
        proskuid = recur_cusventtree1.item(recur_cusventtree1.focus())["values"][0]
        sql = "select * from Productservice where sku = %s"
        val = (proskuid,)
        fbcursor.execute(sql,val)
        prosele = fbcursor.fetchone()
        sql = "select * from company"
        fbcursor.execute(sql)
        create_maintree_insert = fbcursor.fetchone()
        if prosele[10] == '1':
          tax1 = 'yes'
        else:
          tax1 = ''
        if prosele[19] == '1':
          tax2 = 'yes'
        else:
          tax2 = ''
        
        if not create_maintree_insert:
           
          if estcurrsymb[1]=="before amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+str(prosele[7]),1,prosele[8],str(estcurrsymb[1])+str(prosele[7]*1)))
          elif estcurrsymb[1]=="after amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+str(estcurrsymb[1]),1,prosele[8],str(prosele[7]*1)+str(estcurrsymb[1])))
          elif estcurrsymb[1]=="before amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+" "+str(prosele[7]),1,prosele[8],str(estcurrsymb[1])+" "+str(prosele[7]*1)))

          elif estcurrsymb[1]=="after amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+" "+str(estcurrsymb[1]),1,prosele[8],str(prosele[7]*1)+" "+str(estcurrsymb[1]))) 

        elif create_maintree_insert[12] == "1":
          
          if estcurrsymb[1]=="before amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+str(prosele[7]),1,prosele[8],str(estcurrsymb[1])+str(prosele[7]*1)))
          elif estcurrsymb[1]=="after amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+str(estcurrsymb[1]),1,prosele[8],str(prosele[7]*1)+str(estcurrsymb[1])))
          elif estcurrsymb[1]=="before amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+" "+str(prosele[7]),1,prosele[8],str(estcurrsymb[1])+" "+str(prosele[7]*1)))

          elif estcurrsymb[1]=="after amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+" "+str(estcurrsymb[1]),1,prosele[8],str(prosele[7]*1)+" "+str(estcurrsymb[1]))) 
        
          
        elif create_maintree_insert[12] == "2":
          if estcurrsymb[1]=="before amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+str(prosele[7]),1,prosele[8],tax1,str(estcurrsymb[1])+str(prosele[7]*1)))
          elif estcurrsymb[1]=="after amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+str(estcurrsymb[1]),1,prosele[8],tax1,str(prosele[7]*1)+str(estcurrsymb[1])))
          elif estcurrsymb[1]=="before amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+" "+str(prosele[7]),1,prosele[8],tax1,str(estcurrsymb[1])+" "+str(prosele[7]*1)))

          elif estcurrsymb[1]=="after amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+" "+str(estcurrsymb[1]),1,prosele[8],tax1,str(prosele[7]*1)+" "+str(estcurrsymb[1]))) 
          
            
        elif create_maintree_insert[12] == "3":
          if estcurrsymb[1]=="before amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+str(prosele[7]),1,prosele[8],tax1,tax2,str(estcurrsymb[1])+str(prosele[7]*1)))
          elif estcurrsymb[1]=="after amount": 
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+str(estcurrsymb[1]),1,prosele[8],tax1,tax2,str(prosele[7]*1)+str(estcurrsymb[1])))
          elif estcurrsymb[1]=="before amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(estcurrsymb[1])+" "+str(prosele[7]),1,prosele[8],tax1,tax2,str(estcurrsymb[1])+" "+str(prosele[7]*1)))

          elif estcurrsymb[1]=="after amount with space":
            prd_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],str(prosele[7])+" "+str(estcurrsymb[1]),1,prosele[8],tax1,tax2,str(prosele[7]*1)+" "+str(estcurrsymb[1]))) 
        else:
          pass
          
          
     
        slt_prd="select * from productservice where sku=%s"
        slt_prd_val=(proskuid,)
        fbcursor.execute(slt_prd,slt_prd_val)
        dtl_prd=fbcursor.fetchone()
        
        cus_tbl_add="INSERT INTO storingproduct(invoice_number,sku,name,description,unitprice,quantity,peices,tax1,tax2,price)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        cus_tbl_add_val=(inv_nmb_rir.get(),dtl_prd[2],dtl_prd[4],dtl_prd[5],dtl_prd[7],1,dtl_prd[9],dtl_prd[10],dtl_prd[19],dtl_prd[7])
        fbcursor.execute(cus_tbl_add,cus_tbl_add_val)
        fbilldb.commit()
        #--------------------------------------------------------------------------------------------------- Summary Refresh
        sm_qry="select sum(price) from storingproduct where invoice_number=%s"
        sm_qry_val=(inv_nmb_rir.get(),)
        fbcursor.execute(sm_qry,sm_qry_val)
        smry_value=fbcursor.fetchone()
        
        sqlr= 'select currencysign from company'
        fbcursor.execute(sqlr)
        crncy=fbcursor.fetchone()
        crcy_tp=crncy[0]
        sqlrt= 'select currsignplace from company'
        fbcursor.execute(sqlrt)
        post_rp=fbcursor.fetchone()
        crcy_tp_ps=post_rp[0]

        smr_discount=float(smry_value[0])*float(dsc_rt.get())/100
        smr_tax1=float(smry_value[0])*float(tax1_rir.get())/100
        smr_tax2=float(smry_value[0])*float(tax2_rir.get())/100
        smr_ext_cst=rir_cost3.get()
        smr_iv_ttl=(float(smry_value[0])+float(rir_cost3.get())+float(smr_tax1)+float(smr_tax2))-float(smr_discount)

        in_tt_qry="select sum(totpaid),sum(balance) from invoice where invoice_number=%s"
        in_tt_qry_val=(inv_nmb_rir.get(),)
        fbcursor.execute(in_tt_qry,in_tt_qry_val)
        inv_value=fbcursor.fetchone()
        if int(taxtype[0])==2:
          fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
          fir4Frame.place(x=740,y=520)
          summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
          summaryfrme.place(x=0,y=0,width=200,height=170)
          discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
          sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
          tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
          cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
          order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
          total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
          balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
          if crcy_tp_ps=="before amount": 
            discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21)
            tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=42)  
            cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
          elif cency_pos=="after amount":
            discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
            tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=42)  
            cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
          elif cency_pos=="before amount with space":
            discount1=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+" "+str(smry_value[0])).place(x=130 ,y=21)
            tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=42)  
            cost=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_ext_cst)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_iv_ttl)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(crcy_tp)+" "+str(inv_value[0])).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(crcy_tp)+" "+str(inv_value[1])).place(x=130 ,y=126)
          elif cency_pos=="after amount with space":
            discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
            tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=42)  
            cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
          else:
            pass
        elif int(taxtype[0])==3:
          fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
          fir4Frame.place(x=740,y=520)
          summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
          summaryfrme.place(x=0,y=0,width=200,height=170)
          discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
          sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=15)
          tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=30)
          tax=Label(summaryfrme, text="Tax2").place(x=0 ,y=45)
          cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
          order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
          total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
          balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
          if crcy_tp_ps=="before amount": 
            discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=15)
            tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=30)  
            ta2=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax2)).place(x=130 ,y=45) 
            cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
          elif cency_pos=="after amount":
            discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=15)
            tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=30)
            ta2=Label(summaryfrme, text=str(smr_tax2)+str(crcy_tp)).place(x=130 ,y=45)   
            cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
          elif cency_pos=="before amount with space":
            discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=15)
            tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=30) 
            ta2=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_tax2)).place(x=130 ,y=45)  
            cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
          elif cency_pos=="after amount with space":
            discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=15)
            tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=30)  
            ta2=Label(summaryfrme, text=str(smr_tax2)+" "+str(crcy_tp)).place(x=130 ,y=45) 
            cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
            total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
            balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
          else:
            pass
        else:
            fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
            fir4Frame.place(x=740,y=520)
            summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
            summaryfrme.place(x=0,y=0,width=200,height=170)
            discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
            sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
            cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=42)
            order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=63)
            total=Label(summaryfrme, text="Total paid").place(x=0 ,y=84)
            balance=Label(summaryfrme, text="Balance").place(x=0 ,y=105)
            if crcy_tp_ps=="before amount": 
              discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
              sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21) 
              cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=42) 
              order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=63)
              total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=84)
              balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=105)
            elif cency_pos=="after amount":
              discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
              sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
          
              cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=42) 
              order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=63)
              total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=84)
              balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=105)
            elif cency_pos=="before amount with space":
              discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
              sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
        
              cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=42) 
              order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=63)
              total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=84)
              balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=105)
            elif cency_pos=="after amount with space":
              discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
              sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
        
              cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=42) 
              order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=63)
              total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=84)
              balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=105)
            else:
              pass

        recur_newselection.destroy()

      recur_btn11=Button(recur_newselection,compound = LEFT,image=tick ,text="ok", width=60, command=estselepro).place(x=15, y=610)
      recur_btn11=Button(recur_newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=est_edit_product).place(x=250, y=610)
      recur_btnadd=Button(recur_newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=recur_product)
      recur_btnadd.place(x=435, y=610)
      recur_btn11=Button(recur_newselection,compound = LEFT,image=cancel ,text="Cancel",command=cncl_prd, width=60).place(x=740, y=610)
  
  #sms notification
  def sms_recurring():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

  #mark invoice
  def markinvoice_recurring():
    mark_inv=Toplevel()
    mark_inv.geometry("700x480+240+150")
    mark_inv.title("Record Payement for Invoice")
    checkvar=IntVar()
    checkvar1=IntVar()
    checkvar2=IntVar()

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    mark_Notebook = ttk.Notebook(mark_inv)
    Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
    mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
    mark_Notebook.place(x=0, y=0)

    involbel=Label(Mark_Invoice, text="Invoice Balance")
    involbel.place(x=10, y=10)
    numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

    labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
    labelframe5.place(x=10,y=60,width=670,height=250)
    e1 = Entry(labelframe5,width=28).place(x=30,y=45)
    pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
    e2 = Entry(labelframe5,width=28).place(x=220,y=45)
    payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
    drop = ttk.Combobox(labelframe5, value="Hello")
    drop.place(x=450,y=45)
    involbel=Label(labelframe5, text="Description")
    involbel.place(x=30, y=80)
    numentry=Entry(labelframe5, width=100).place(x=30, y=120)
    Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
    pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
    pl.place(x=300,y=145)
    Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
    Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

    okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
    canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    
  #voidinvoice
  def voidinvoice_recurring():
    messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
  
  #delete line item  
  def rir_delete():
    try:
      proskuid = prd_tree.item(prd_tree.focus())["values"][0]
      sql_qr="DELETE FROM storingproduct WHERE sku=%s"
      sql_qr_val=(proskuid,)
      fbcursor.execute(sql_qr,sql_qr_val)
      fbilldb.commit()
      

      sqlr= 'select currencysign from company'
      fbcursor.execute(sqlr)
      crncy=fbcursor.fetchone()
      crcy_tp=crncy[0]
      sqlrt= 'select currsignplace from company'
      fbcursor.execute(sqlrt)
      post_rp=fbcursor.fetchone()
      crcy_tp_ps=post_rp[0]
      
      if int(taxtype[0])==2:
          rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
          rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
          fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
          main_prd_val=fbcursor.fetchall()
          count_prd=0
          for record in prd_tree.get_children():
            prd_tree.delete(record)
          for i in main_prd_val:
                if i[11] is not None:
                  dgt="Yes"
                else:
                  dgt="No"
                  if crcy_tp_ps=="before amount":
                    prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+str(i[13])))
                    count_prd +=1
                  elif crcy_tp_ps=="after amount":
                    prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,str(i[13])+str(crcy_tp)))
                    count_prd +=1
                  elif crcy_tp_ps=="before amount with space":
                    prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+" "+str(i[13])))
                  elif crcy_tp_ps=="after amount with space":
                    prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,str(i[13])+" "+str(crcy_tp)))
                    count_prd +=1
                  else:
                    pass

      elif int(taxtype[0])==3:
              rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
              rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
              fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
              main_prd_val=fbcursor.fetchall()
              count_prd=0
              for record in prd_tree.get_children():
                prd_tree.delete(record)

              for i in main_prd_val:
                    if i[11] is not None:
                      dgt="Yes"
                    else:
                      dgt="No"
                    if i[12] is not None:
                      dlt="Yes"
                    else:
                      dlt="No"
                    if crcy_tp_ps=="before amount":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+str(i[13])))
                        count_prd +=1
                    elif crcy_tp_ps=="after amount":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,dlt,str(i[13])+str(crcy_tp)))
                        count_prd +=1
                    elif crcy_tp_ps=="before amount with space":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+" "+str(i[13])))
                    elif crcy_tp_ps=="after amount with space":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,dlt,str(i[13])+" "+str(crcy_tp)))
                        count_prd +=1
                    else:
                        pass

      else:
              
              rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
              rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
              fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
              main_prd_val=fbcursor.fetchall()
              count_prd=0
              
              for record in prd_tree.get_children():
                prd_tree.delete(record)
              for i in main_prd_val:
                      if crcy_tp_ps=="before amount":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],str(crcy_tp)+str(i[13])))
                        count_prd +=1
                      elif crcy_tp_ps=="after amount":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],str(i[13])+str(crcy_tp)))
                        count_prd +=1
                      elif crcy_tp_ps=="before amount with space":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],str(crcy_tp)+" "+str(i[13])))
                      elif crcy_tp_ps=="after amount with space":
                        prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],str(i[13])+" "+str(crcy_tp)))
                        count_prd +=1
                      else:
                        pass
          
      sm_qry="select sum(price) from storingproduct where invoice_number=%s"
      sm_qry_val=(inv_nmb_rir.get(),)
      fbcursor.execute(sm_qry,sm_qry_val)
      smry_value=fbcursor.fetchone()
      #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Summary Calculations
      smr_discount=float(smry_value[0])*float(dsc_rt.get())/100
      smr_tax1=float(smry_value[0])*float(tax1_rir.get())/100
      smr_tax2=float(smry_value[0])*float(tax2_rir.get())/100
      smr_ext_cst=rir_cost3.get()
      smr_iv_ttl=(float(smry_value[0])+float(rir_cost3.get())+float(smr_tax1)+float(smr_tax2))-float(smr_discount)
      
      in_tt_qry="select sum(totpaid),sum(balance) from invoice where invoice_number=%s"
      in_tt_qry_val=(inv_nmb_rir.get(),)
      fbcursor.execute(in_tt_qry,in_tt_qry_val)
      inv_value=fbcursor.fetchone()
      if int(taxtype[0])==2:
        fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
        fir4Frame.place(x=740,y=520)
        summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
        summaryfrme.place(x=0,y=0,width=200,height=170)
        discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
        sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
        tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
        cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
        order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
        total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
        balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
        if crcy_tp_ps=="before amount": 
          discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21)
          tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=42)  
          cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
        elif cency_pos=="after amount":
          discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
          tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=42)  
          cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
        elif cency_pos=="before amount with space":
          discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
          tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=42)  
          cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
        elif cency_pos=="after amount with space":
          discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
          tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=42)  
          cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
        else:
          pass
      elif int(taxtype[0])==3:
        fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
        fir4Frame.place(x=740,y=520)
        summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
        summaryfrme.place(x=0,y=0,width=200,height=170)
        discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
        sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=15)
        tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=30)
        tax=Label(summaryfrme, text="Tax2").place(x=0 ,y=45)
        cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
        order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
        total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
        balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
        if crcy_tp_ps=="before amount": 
          discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=15)
          tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=30)  
          ta2=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax2)).place(x=130 ,y=45) 
          cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
        elif cency_pos=="after amount":
          discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=15)
          tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=30)
          ta2=Label(summaryfrme, text=str(smr_tax2)+str(crcy_tp)).place(x=130 ,y=45)   
          cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
        elif cency_pos=="before amount with space":
          discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=15)
          tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=30) 
          ta2=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_tax2)).place(x=130 ,y=45)  
          cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
        elif cency_pos=="after amount with space":
          discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=15)
          tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=30)  
          ta2=Label(summaryfrme, text=str(smr_tax2)+" "+str(crcy_tp)).place(x=130 ,y=45) 
          cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
          total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
          balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
        else:
          pass
      else:
          fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
          fir4Frame.place(x=740,y=520)
          summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
          summaryfrme.place(x=0,y=0,width=200,height=170)
          discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
          sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
          cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=42)
          order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=63)
          total=Label(summaryfrme, text="Total paid").place(x=0 ,y=84)
          balance=Label(summaryfrme, text="Balance").place(x=0 ,y=105)
          if crcy_tp_ps=="before amount": 
            discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21) 
            cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=42) 
            order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=63)
            total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=84)
            balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=105)
          elif cency_pos=="after amount":
            discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
        
            cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=42) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=63)
            total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=84)
            balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=105)
          elif cency_pos=="before amount with space":
            discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
      
            cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=42) 
            order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=63)
            total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=84)
            balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=105)
          elif cency_pos=="after amount with space":
            discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
            sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
      
            cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=42) 
            order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=63)
            total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=84)
            balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=105)
          else:
            pass
    except:
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")       
#------------------------------------------------------------------------------------save edit
  def sv_edit():
    sm_qry="select sum(price) from storingproduct where invoice_number=%s"
    sm_qry_val=(inv_nmb_rir.get(),)
    fbcursor.execute(sm_qry,sm_qry_val)
    smry_value=fbcursor.fetchone()

    invoice_number=inv_nmb_rir.get()
    invodate=inv_dt_rir.get_date()
    duedate=due_dt_rir.get_date()
    invoicetot=smr_iv_ttl
    extracostname=ext_dt.get()
    extracost=rir_cost3.get()
    template=tmpl_dt.get()
    salesper=sl_prsn.get()
    discourate=dsc_rt.get()
    tax1=tax1_rir.get()
    category=ct_rir.get()
    businessname=cust_selction_nm.get()
    businessaddress=address_rir.get(1.0,END)
    shipname=shp_to_rir.get()
    shipaddress=shp_to_adr_rir.get(1.0,END)
    cpemail=emil_rir.get()
    cpmobileforsms=sms_shpto_rir.get()
    recurring_check=chk_sts.get()
    recurring_period=rir_spn_bx.get()
    next_invoice=dt_nxt_inv.get_date()
    stop_recurring=dt_stp_inv.get_date()
    discount=smr_discount
    terms=trms.get(1.0,END)
    term_of_payment=cmb_trms.get()
    tax2=tax2_rir.get()
    quantity=1
    title_text=ttl_inv.get()
    header_text=hd_inv.get()
    footer_text=fd_inv.get()
    comments=cmm.get(1.0,END)
    privatenotes=prv_nt.get(1.0,END)
    subtotal=smry_value[0]
    stop_recurring_check=stp_chk.get()
    
    rir_tbl_edit="update invoice set invoice_number=%s,invodate=%s,duedate=%s,invoicetot=%s,extracostname=%s,extracost=%s,template=%s,salesper=%s,discourate=%s,tax1=%s,category=%s,businessname=%s,businessaddress=%s,shipname=%s,shipaddress=%s,cpemail=%s,cpmobileforsms=%s,recurring_check=%s,recurring_period=%s,next_invoice=%s,stop_recurring=%s,discount=%s,terms=%s,term_of_payment=%s,tax2=%s,quantity=%s,title_text=%s,header_text=%s,footer_text=%s,comments=%s,privatenotes=%s,subtotal=%s,stop_recurring_check=%s where invoice_number=%s"
    rir_tbl_edit_val=(invoice_number,invodate,duedate,invoicetot,extracostname,extracost,template,salesper,discourate,tax1,category,businessname,businessaddress,shipname,shipaddress,cpemail,cpmobileforsms,recurring_check,recurring_period,next_invoice,stop_recurring,discount,terms,term_of_payment,tax2,quantity,title_text,header_text,footer_text,comments,privatenotes,subtotal,stop_recurring_check,invoice_number,)
    fbcursor.execute(rir_tbl_edit,rir_tbl_edit_val)
    fbilldb.commit()

    for record in rir_tree.get_children():
          rir_tree.delete(record)
    rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL"
  
    fbcursor.execute(rir_main_table_sql)
    main_rir_val=fbcursor.fetchall()
    count_rir=0

    for i in main_rir_val:
      rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
      count_rir +=1
    
    
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=customer_invoice_recurring)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=addnew,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=recurring_New_newline)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=delete,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=rir_delete)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=prview_rir_inv)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=rir_prnt_inv_rir)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms_recurring)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mark= Button(firFrame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=57,command=markinvoice_recurring)
  mark.pack(side="left", pady=3, ipadx=4)

  void= Button(firFrame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=56,command=voidinvoice_recurring)
  void.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=clcu_rcrir)
  calc.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Save",relief=RAISED, image=saves,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sv_edit)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)
  #---------------------------------------------------------------------------------------------Customer Selection Functiopn
  def name_sltd(event):
    
   
    sdrt_qsy='select * from customer where businessname=%s'
    sdrt_qry_qtr=(cust_selction_nm.get(),)
    fbcursor.execute(sdrt_qsy,sdrt_qry_qtr)
    dtl_rir_cus=fbcursor.fetchone()

    sdou_qsy='select * from invoice where businessname=%s'
    sdou_qsy_qry=(cust_selction_nm.get(),)
    fbcursor.execute(sdou_qsy,sdou_qsy_qry)
    dtl_inv=fbcursor.fetchone()
  
    address_rir.delete(1.0,END)
    address_rir.insert(1.0,dtl_inv[5])
    shp_to_rir.delete(0,END)
    shp_to_rir.insert(0,dtl_inv[6])
    shp_to_adr_rir.delete(1.0,END)
    shp_to_adr_rir.insert(1.0,dtl_inv[7])
    emil_rir.delete(0,END)
    emil_rir.insert(0,dtl_inv[9])
    sms_shpto_rir.delete(0,END)
    sms_shpto_rir.insert(0,dtl_inv[12])
    # inv_nmb_rir.delete(0,END)
    # inv_nmb_rir.insert(0,dtl_inv[1])
    # inv_dt_rir.delete(1,END)
    # inv_dt_rir.insert(0,dtl_inv[2])
    # due_dt_rir.delete(0,END)
    # due_dt_rir.insert(0,dtl_inv[2])
    # trms_cmb.delete(0,END)
    # trms_cmb.insert(0,dtl_inv[35])

    cmb_ext_nm.delete(0,END)
    cmb_ext_nm.insert(0,dtl_inv[11])
    dsc_rt.delete(0,END)
    dsc_rt.insert(0,dtl_inv[15])
    rir_cost3.delete(0,END)
    rir_cost3.insert(0,dtl_inv[12])
    sql_yty='select taxtype from company'
    fbcursor.execute(sql_yty)
    taxtype=fbcursor.fetchone()
    if int(taxtype[0])==3:
      tax1_rir.delete(0,END)
      tax1_rir.insert(0,dtl_inv[16])
      tax2_rir.delete(0,END)
      tax2_rir.insert(0,dtl_inv[36])
    elif int(taxtype[0])==2:
      tax1_rir.delete(0,END)
      tax1_rir.insert(0,dtl_inv[16])
    else:
      pass
    tmp_rir.delete(0,END)
    tmp_rir.insert(0,dtl_inv[13])
    sl_prsn.delete(0,END)
    sl_prsn.insert(0,"Administrator")
    ct_rir.delete(0,END)
    ct_rir.insert(0,dtl_inv[17])

    #-------------------------------------------------------------------------------Insert Summary
    

    sqlr= 'select currencysign from company'
    fbcursor.execute(sqlr)
    crncy=fbcursor.fetchone()
    crcy_tp=crncy[0]
    sqlrt= 'select currsignplace from company'
    fbcursor.execute(sqlrt)
    post_rp=fbcursor.fetchone()
    crcy_tp_ps=post_rp[0]
    
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Summary Calculations
    sm_qry="select sum(price) from storingproduct where invoice_number=%s"
    sm_qry_val=(inv_nmb_rir.get(),)
    fbcursor.execute(sm_qry,sm_qry_val)
    smry_value=fbcursor.fetchone()
    
    smr_discount=float(smry_value[0])*float(dsc_rt.get())/100
    smr_tax1=float(smry_value[0])*float(tax1_rir.get())/100
    smr_tax2=float(smry_value[0])*float(tax2_rir.get())/100
    smr_ext_cst=rir_cost3.get()
    smr_iv_ttl=(float(smry_value[0])+float(rir_cost3.get())+float(smr_tax1)+float(smr_tax2))-float(smr_discount)

    in_tt_qry="select sum(totpaid),sum(balance) from invoice where invoice_number=%s"
    in_tt_qry_val=(inv_nmb_rir.get(),)
    fbcursor.execute(in_tt_qry,in_tt_qry_val)
    inv_value=fbcursor.fetchone()
    if int(taxtype[0])==2:
      fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
      fir4Frame.place(x=740,y=520)
      summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
      summaryfrme.place(x=0,y=0,width=200,height=170)
      discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
      sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
      tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
      cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
      order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
      total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
      balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
      if crcy_tp_ps=="before amount": 
        discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21)
        tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=42)  
        cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
      elif cency_pos=="after amount":
        discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
        tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=42)  
        cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
      elif cency_pos=="before amount with space":
        discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
        tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=42)  
        cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
      elif cency_pos=="after amount with space":
        discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
        tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=42)  
        cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
      else:
        pass
    elif int(taxtype[0])==3:
      fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
      fir4Frame.place(x=740,y=520)
      summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
      summaryfrme.place(x=0,y=0,width=200,height=170)
      discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
      sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=15)
      tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=30)
      tax=Label(summaryfrme, text="Tax2").place(x=0 ,y=45)
      cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
      order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
      total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
      balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
      if crcy_tp_ps=="before amount": 
        discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=15)
        tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=30)  
        ta2=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax2)).place(x=130 ,y=45) 
        cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
      elif cency_pos=="after amount":
        discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=15)
        tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=30)
        ta2=Label(summaryfrme, text=str(smr_tax2)+str(crcy_tp)).place(x=130 ,y=45)   
        cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
      elif cency_pos=="before amount with space":
        discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=15)
        tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=30) 
        ta2=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_tax2)).place(x=130 ,y=45)  
        cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
      elif cency_pos=="after amount with space":
        discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=15)
        tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=30)  
        ta2=Label(summaryfrme, text=str(smr_tax2)+" "+str(crcy_tp)).place(x=130 ,y=45) 
        cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
        total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
        balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
      else:
        pass
    else:
        fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
        fir4Frame.place(x=740,y=520)
        summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
        summaryfrme.place(x=0,y=0,width=200,height=170)
        discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
        sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
        cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=42)
        order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=63)
        total=Label(summaryfrme, text="Total paid").place(x=0 ,y=84)
        balance=Label(summaryfrme, text="Balance").place(x=0 ,y=105)
        if crcy_tp_ps=="before amount": 
          discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21) 
          cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=42) 
          order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=63)
          total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=84)
          balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=105)
        elif cency_pos=="after amount":
          discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
      
          cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=42) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=63)
          total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=84)
          balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=105)
        elif cency_pos=="before amount with space":
          discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
    
          cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=42) 
          order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=63)
          total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=84)
          balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=105)
        elif cency_pos=="after amount with space":
          discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
          sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
    
          cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=42) 
          order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=63)
          total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=84)
          balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=105)
        else:
          pass


    #=---------------------------------------------------------------------------------------Table
    # sql_yty='select taxtype from company'
    # fbcursor.execute(sql_yty)
    # taxtype=fbcursor.fetchone()
    # if int(taxtype[0])==3:
    #   rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
    #   rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
    #   fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
    #   main_prd_val=fbcursor.fetchall()
    #   count_prd=0
    #   for record in prd_tree.get_children():
    #     prd_tree.delete(record)

    #   for i in main_prd_val:
    #         if i[11] is not None:
    #           dgt="Yes"
    #         else:
    #           dgt="No"
    #         if i[12] is not None:
    #           dlt="Yes"
    #         else:
    #           dlt="No"
    #         if crcy_tp_ps=="before amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+str(i[13])))
    #             count_prd +=1
    #         elif crcy_tp_ps=="after amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,dlt,str(i[13])+str(crcy_tp)))
    #             count_prd +=1
    #         elif crcy_tp_ps=="before amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+" "+str(i[13])))
    #         elif crcy_tp_ps=="after amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,dlt,str(i[13])+" "+str(crcy_tp)))
    #             count_prd +=1
    #         else:
    #             pass

    # elif int(taxtype[0])==2:
      
    #   rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
    #   rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
    #   fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
    #   main_prd_val=fbcursor.fetchall()
    #   count_prd=0
    #   for record in prd_tree.get_children():
    #     prd_tree.delete(record)
    #   for i in main_prd_val:
    #         if i[11] is not None:
    #           dgt="Yes"
    #         else:
    #           dgt="No"
    #         if crcy_tp_ps=="before amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+str(i[13])))
    #             count_prd +=1
    #         elif crcy_tp_ps=="after amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,str(i[13])+str(crcy_tp)))
    #             count_prd +=1
    #         elif crcy_tp_ps=="before amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+" "+str(i[13])))
    #         elif crcy_tp_ps=="after amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,str(i[13])+" "+str(crcy_tp)))
    #             count_prd +=1
    #         else:
    #             pass
    # else:
    #   rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
    #   rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
    #   fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
    #   main_prd_val=fbcursor.fetchall()
    #   count_prd=0
    #   for record in prd_tree.get_children():
    #     prd_tree.delete(record)
    #   for i in main_prd_val:
    #         if crcy_tp_ps=="before amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],str(crcy_tp)+str(i[13])))
    #             count_prd +=1
    #         elif crcy_tp_ps=="after amount":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],str(i[13])+str(crcy_tp)))
    #             count_prd +=1
    #         elif crcy_tp_ps=="before amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],str(crcy_tp)+" "+str(i[13])))
    #         elif crcy_tp_ps=="after amount with space":
    #             prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],str(i[13])+" "+str(crcy_tp)))
    #             count_prd +=1
    #         else:
    #             pass
    
    #--------------------------------------------------------------------------------------recurring
    if dtl_inv[24] is not None:
      stp_rir.select()
    else:
      stp_rir.deselect()
    if dtl_inv[27] is not None:
      stp_rir2.select()
    else:
      stp_rir2.deselect()

    dt_nxt_inv.delete(0,END)
    dt_nxt_inv.insert(0,dtl_inv[26])
    dt_stp_inv.delete(0,END)
    dt_stp_inv.insert(0,dtl_inv[27])

    #-------------------------------------------------------------------------------------Header Fotter
    cmp_ttl.delete(0,END)
    cmp_ttl.insert(0,dtl_inv[39])
    cmp_ht.delete(0,END)
    cmp_ht.insert(0,dtl_inv[40])
    cmp_ft.delete(0,END)
    cmp_ft.insert(0,dtl_inv[41])
    #=======================================================================private note
    prv_nt.delete(1.0,END)
    prv_nt.insert(1.0,dtl_inv[45])
    #=======================================================================terms
    trms.delete(1.0,END)
    trms.insert(1.0,dtl_inv[35])
    #=======================================================================comments
    cmm.delete(1.0,END)
    cmm.insert(1.0,dtl_inv[44])


  cusr_selct=rir_tree.item(rir_tree.focus())["values"][5]#---------------------------------values Insertion edit
    
  sdrt_qsy='select businessname from customer'
  fbcursor.execute(sdrt_qsy)
  dtl_rir=fbcursor.fetchall()

  sdrts_qsy='select * from customer where businessname=%s'
  sdrt_qry_qtr=(cusr_selct,)
  fbcursor.execute(sdrts_qsy,sdrt_qry_qtr)
  dtl_rissr_cus=fbcursor.fetchone()

  sdou_qsy='select * from invoice where businessname=%s'
  sdou_qsy_qry=(cusr_selct,)
  fbcursor.execute(sdou_qsy,sdou_qsy_qry)
  dtl_inv=fbcursor.fetchone()
  #-----------------------------------------------------------------------------------button >>
  def cpy_dts():
    
    shp_to_rir.delete(0,END)
    shp_to_rir.insert(0,cust_selction_nm.get())
    shp_to_adr_rir.delete(1.0,END)
    shp_to_adr_rir.insert(1.0,address_rir.get(1.0,END))
    pass
  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Order to").place(x=10,y=5)
  
  cust_selction_nm=StringVar()
  cmb_main_bx = ttk.Combobox(labelframe1,width=28, textvariable=cust_selction_nm)
  cmb_main_bx.insert(0,dtl_inv[18])

  rir_dt_cst=[]
  for i in dtl_rir:
    rir_dt_cst.append(i[0])
    
  cmb_main_bx['values']=rir_dt_cst
  
  cmb_main_bx.bind('<<ComboboxSelected>>',name_sltd)
  cmb_main_bx.place(x=80,y=5)

  
  sdrt_qsy='select * from customer where businessname=%s'
  sdrt_qry_qtr=(cusr_selct,)
  fbcursor.execute(sdrt_qsy,sdrt_qry_qtr)
  dtl_rir_cus=fbcursor.fetchone()

    

  

  

  sdous_qsy='select distinct term_of_payment from invoice'
  fbcursor.execute(sdous_qsy)
  dtl_inv_all=fbcursor.fetchall()


  address=Label(labelframe1,text="Address").place(x=10,y=30)
  address_rir=scrolledtext.ScrolledText(labelframe1,width=23,)
  address_rir.delete(1.0,END)
  address_rir.insert(1.0,dtl_inv[19])
  address_rir.place(x=80,y=30,height=70)

  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  shp_to_rir=Entry(labelframe1,width=30)
  shp_to_rir.delete(0,END)
  shp_to_rir.insert(0,dtl_inv[20])
  shp_to_rir.place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  shp_to_adr_rir=scrolledtext.ScrolledText(labelframe1,width=23)
  shp_to_adr_rir.delete(1.0,END)
  shp_to_adr_rir.insert(1.0,dtl_inv[21])
  shp_to_adr_rir.place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=cpy_dts).place(x=280, y=50)
    
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  emil_rir=Entry(labelframe2,width=30)
  emil_rir.delete(0,END)
  emil_rir.insert(0,dtl_inv[22])

  emil_rir.place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  sms_shpto_rir=Entry(labelframe2,width=30)
  sms_shpto_rir.delete(0,END)
  sms_shpto_rir.insert(0,dtl_inv[23])
  sms_shpto_rir.place(x=402,y=5)
      
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  inv_nmb_rir=Entry(labelframe,width=25)
  inv_nmb_rir.delete(0,END)
  inv_nmb_rir.insert(0,dtl_inv[1])
  inv_nmb_rir.place(x=100,y=5,)
  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  inv_dt_rir=DateEntry(labelframe,width=20)
  inv_dt_rir.delete(1,END)
  inv_dt_rir.insert(0,dtl_inv[2])
  inv_dt_rir.place(x=150,y=33)
  chk_dur=IntVar()
  duedate=Checkbutton(labelframe,variable = chk_dur,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  due_dt_rir=DateEntry(labelframe,width=20)
  due_dt_rir.delete(0,END)
  due_dt_rir.insert(0,dtl_inv[2])
  due_dt_rir.place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  cmb_trms=StringVar()
  trms_cmb=ttk.Combobox(labelframe,width=25,textvariable=cmb_trms)

  dtl_trm=[]
  for i in dtl_inv_all:
    dtl_trm.append(i[0])

  trms_cmb['values']=dtl_trm
  trms_cmb.delete(0,END)
  trms_cmb.insert(0,dtl_inv[35])
  trms_cmb.place(x=100,y=92)

  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e11=Entry(labelframe,width=27)
    # e11.insert(1,)
  e11.place(x=100,y=118)

    
  #----------------------------------------------------------------------------------------------product Table
  sql_yty='select taxtype from company'
  fbcursor.execute(sql_yty)
  taxtype=fbcursor.fetchone()
  sqlr= 'select currencysign from company'
  fbcursor.execute(sqlr)
  crncy=fbcursor.fetchone()
  crcy_tp=crncy[0]
  sqlrt= 'select currsignplace from company'
  fbcursor.execute(sqlrt)
  post_rp=fbcursor.fetchone()
  crcy_tp_ps=post_rp[0]
    
  if int(taxtype[0])==2:
      fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
      fir2Frame.pack(side="top", fill=X)
      listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
      prd_tree=ttk.Treeview(listFrame)
      prd_tree["columns"]=["1","2","3","4","5","6","7","8"]

      prd_tree.column("#0", width=40)
      prd_tree.column("1", width=80)
      prd_tree.column("2", width=190)
      prd_tree.column("3", width=190)
      prd_tree.column("4", width=80)
      prd_tree.column("5", width=60)
      prd_tree.column("6", width=60)
      prd_tree.column("7", width=60)
      prd_tree.column("8", width=80)
      
      prd_tree.heading("#0")
      prd_tree.heading("1",text="ID/SKU")
      prd_tree.heading("2",text="Product/Service")
      prd_tree.heading("3",text="Description")
      prd_tree.heading("4",text="Unit Price")
      prd_tree.heading("5",text="Quality")
      prd_tree.heading("6",text="Pcs/Weight")
      prd_tree.heading("7",text="Tax1")
      prd_tree.heading("8",text="Price")
      
      
    
      rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
      rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
      fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
      main_prd_val=fbcursor.fetchall()
      count_prd=0
      for record in prd_tree.get_children():
        prd_tree.delete(record)
      for i in main_prd_val:
            if i[11] is not None:
              dgt="Yes"
            else:
              dgt="No"
              if crcy_tp_ps=="before amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+str(i[13])))
                count_prd +=1
              elif crcy_tp_ps=="after amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,str(i[13])+str(crcy_tp)))
                count_prd +=1
              elif crcy_tp_ps=="before amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,str(crcy_tp)+" "+str(i[13])))
              elif crcy_tp_ps=="after amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,str(i[13])+" "+str(crcy_tp)))
                count_prd +=1
              else:
                pass
            
      
      prd_tree.pack(fill="both", expand=1)

  elif int(taxtype[0])==3:
      
      fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
      fir2Frame.pack(side="top", fill=X)
      listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
      prd_tree=ttk.Treeview(listFrame)
      prd_tree["columns"]=["1","2","3","4","5","6","7","8","9"]

      prd_tree.column("#0", width=20)
      prd_tree.column("1", width=80)
      prd_tree.column("2", width=170)
      prd_tree.column("3", width=170)
      prd_tree.column("4", width=80)
      prd_tree.column("5", width=60)
      prd_tree.column("6", width=60)
      prd_tree.column("7", width=60)
      prd_tree.column("8", width=60)
      prd_tree.column("9", width=80)
      
      prd_tree.heading("#0")
      prd_tree.heading("1",text="ID/SKU")
      prd_tree.heading("2",text="Product/Service")
      prd_tree.heading("3",text="Description")
      prd_tree.heading("4",text="Unit Price")
      prd_tree.heading("5",text="Quality")
      prd_tree.heading("6",text="Pcs/Weight")
      prd_tree.heading("7",text="Tax1")
      prd_tree.heading("8",text="Tax2")
      prd_tree.heading("9",text="Price")
      rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
      rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
      fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
      main_prd_val=fbcursor.fetchall()
      count_prd=0
      for record in prd_tree.get_children():
        prd_tree.delete(record)

      for i in main_prd_val:
            if i[11] is not None:
              dgt="Yes"
            else:
              dgt="No"
            if i[12] is not None:
              dlt="Yes"
            else:
              dlt="No"
            if crcy_tp_ps=="before amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+str(i[13])))
                count_prd +=1
            elif crcy_tp_ps=="after amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],dgt,dlt,str(i[13])+str(crcy_tp)))
                count_prd +=1
            elif crcy_tp_ps=="before amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],dgt,dlt,str(crcy_tp)+" "+str(i[13])))
            elif crcy_tp_ps=="after amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],dgt,dlt,str(i[13])+" "+str(crcy_tp)))
                count_prd +=1
            else:
                pass

      prd_tree.pack(fill="both", expand=1)
      

  else:
      fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
      fir2Frame.pack(side="top", fill=X)
      listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
      prd_tree=ttk.Treeview(listFrame)
      prd_tree["columns"]=["1","2","3","4","5","6","7","8"]

      prd_tree.column("#0", width=40)
      prd_tree.column("1", width=110)
      prd_tree.column("2", width=220)
      prd_tree.column("3", width=220)
      prd_tree.column("4", width=80)
      prd_tree.column("5", width=80)
      prd_tree.column("6", width=80)
      prd_tree.column("7", width=100)
      
      prd_tree.heading("#0")
      prd_tree.heading("1",text="ID/SKU")
      prd_tree.heading("2",text="Product/Service")
      prd_tree.heading("3",text="Description")
      prd_tree.heading("4",text="Unit Price")
      prd_tree.heading("5",text="Quality")
      prd_tree.heading("6",text="Pcs/Weight")
      prd_tree.heading("7",text="Price")


      rir_prd_table_sql="select * from storingproduct where invoice_number=%s"
      rir_prd_table_sql_qry=(inv_nmb_rir.get(),)
      fbcursor.execute(rir_prd_table_sql,rir_prd_table_sql_qry)
      main_prd_val=fbcursor.fetchall()
      count_prd=0
      for record in prd_tree.get_children():
        prd_tree.delete(record)
      for i in main_prd_val:
              if crcy_tp_ps=="before amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+str(i[8]),i[9],i[10],str(crcy_tp)+str(i[13])))
                count_prd +=1
              elif crcy_tp_ps=="after amount":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+str(str(crcy_tp)),i[9],i[10],str(i[13])+str(crcy_tp)))
                count_prd +=1
              elif crcy_tp_ps=="before amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(crcy_tp)+" "+str(i[8]),i[9],i[10],str(crcy_tp)+" "+str(i[13])))
              elif crcy_tp_ps=="after amount with space":
                prd_tree.insert(parent='', index='end', iid=count_prd, values=(i[5],i[6],i[7],str(i[8])+" "+str(crcy_tp),i[9],i[10],str(i[13])+" "+str(crcy_tp)))
                count_prd +=1
              else:
                pass
      
      prd_tree.pack(fill="both", expand=1)
    

  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
    
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  
  # --------------------------------------------------------------------------------------Invoice in edit



  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  sql_ytyf='select distinct extracostname,template from invoice'
  fbcursor.execute(sql_ytyf)
  dt_tmp=fbcursor.fetchall()
  dtl_nm_ext=[]
  for i in dt_tmp:
    dtl_nm_ext.append(i[0])
  ext_dt=StringVar()
  cmb_ext_nm=ttk.Combobox(labelframe1, value=dtl_nm_ext,width=20, textvariable=ext_dt)
  cmb_ext_nm.delete(0,END)
  cmb_ext_nm.insert(0,dtl_inv[11])
  cmb_ext_nm.place(x=115,y=5)

  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  dsc_rt=Entry(labelframe1,width=6)
  dsc_rt.delete(0,END)
  dsc_rt.insert(0,dtl_inv[15])
  dsc_rt.place(x=460,y=5)

  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  global rir_cost3
  rir_cost3=Entry(labelframe1,width=10)
  rir_cost3.delete(0,END)
  rir_cost3.insert(0,dtl_inv[12])
  rir_cost3.place(x=115,y=35)

  if int(taxtype[0])==3:
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    tax1_rir=Entry(labelframe1,width=7)
    tax1_rir.delete(0,END)
    tax1_rir.insert(0,dtl_inv[16])
    tax1_rir.place(x=460,y=35)

    tax=Label(labelframe1,text="Tax2").place(x=420,y=60)
    tax2_rir=Entry(labelframe1,width=7)
    tax2_rir.delete(0,END)
    tax2_rir.insert(0,dtl_inv[36])
    tax2_rir.place(x=460,y=60)
  elif int(taxtype[0])==2:
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    tax1_rir=Entry(labelframe1,width=7)
    tax1_rir.delete(0,END)
    tax1_rir.insert(0,dtl_inv[16])
    tax1_rir.place(x=460,y=35)
  else:
    pass

  template=Label(labelframe1,text="Template").place(x=37,y=70)
  dtl_tmpl=[]
  for i in dt_tmp:
    dtl_tmpl.append(i[1])
  tmpl_dt=StringVar()
  tmp_rir=ttk.Combobox(labelframe1, value=dtl_tmpl,width=30, textvariable=tmpl_dt)
  tmp_rir.delete(0,END)
  tmp_rir.insert(0,dtl_inv[13])
  tmp_rir['value']=("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  tmp_rir.place(x=115,y=70)

  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  sl_prsn=Entry(labelframe1,width=18)
  sl_prsn.delete(0,END)
  sl_prsn.insert(0,"Administrator")
  sl_prsn.place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  ct_rir=Entry(labelframe1,width=22)
  ct_rir.delete(0,END)
  ct_rir.insert(0,dtl_inv[17])
  ct_rir.place(x=370,y=100)
 
    
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  emon=StringVar()
  pron=StringVar()
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never")
  nev1.place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never")
  nev2.place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)

  sdous_qsy='select distinct title_text from invoice'
  fbcursor.execute(sdous_qsy)
  inf_ttl=fbcursor.fetchall()

  sdous_qsy='select distinct header_text from invoice'
  fbcursor.execute(sdous_qsy)
  inv_ht=fbcursor.fetchall()

  sdous_qsy='select distinct footer_text from invoice'
  fbcursor.execute(sdous_qsy)
  inv_ft=fbcursor.fetchall()
  ttl_inv=StringVar()
  hd_inv=StringVar()
  fd_inv=StringVar()
  cmp_ttl=ttk.Combobox(headerFrame,width=60, textvariable=ttl_inv)
  cmp_ttl.delete(0,END)
  cmp_ttl.insert(0,dtl_inv[39])
  dtl_hd=[]
  for i in inf_ttl:
    dtl_hd.append(i[0])
  cmp_ttl['value']=dtl_hd
  
  cmp_ttl.place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  cmp_ht=ttk.Combobox(headerFrame,width=60,textvariable=hd_inv)
  cmp_ht.delete(0,END)
  cmp_ht.insert(0,dtl_inv[40])
  dtl_ht=[]
  for i in inv_ht:
      dtl_ht.append(i[0])
  cmp_ht['value']=dtl_ht
  cmp_ht.place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  cmp_ft=ttk.Combobox(headerFrame,width=60,textvariable=fd_inv)
  cmp_ft.delete(0,END)
  cmp_ft.insert(0,dtl_inv[41])
  dtl_ft=[]
  for i in inv_ft:
    dtl_ft.append(i[0])
  cmp_ft['value']=dtl_ft
  cmp_ft.place(x=125,y=85)

  

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)")
  text.place(x=10,y=10)
  prv_nt=Text(noteFrame,width=100,height=7)
  prv_nt.delete(1.0,END)
  prv_nt.insert(1.0,dtl_inv[45])
  prv_nt.place(x=10,y=32)

  trms=Text(termsFrame,width=100,height=9)
  trms.delete(1.0,END)
  trms.insert(1.0,dtl_inv[35])
  trms.place(x=10,y=10)

  cmm=Text(commentFrame,width=100,height=9)
  cmm.delete(1.0,END)
  cmm.insert(1.0,dtl_inv[44])
  cmm.place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
    
  
  sqlr= 'select currencysign from company'
  fbcursor.execute(sqlr)
  crncy=fbcursor.fetchone()
  crcy_tp=crncy[0]
  sqlrt= 'select currsignplace from company'
  fbcursor.execute(sqlrt)
  post_rp=fbcursor.fetchone()
  crcy_tp_ps=post_rp[0]
  
  

  sm_qry="select sum(price) from storingproduct where invoice_number=%s"
  sm_qry_val=(inv_nmb_rir.get(),)
  fbcursor.execute(sm_qry,sm_qry_val)
  smry_value=fbcursor.fetchone()
  #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Summary Calculations
  smr_discount=float(smry_value[0])*float(dsc_rt.get())/100
  smr_tax1=float(smry_value[0])*float(tax1_rir.get())/100
  smr_tax2=float(smry_value[0])*float(tax2_rir.get())/100
  smr_ext_cst=rir_cost3.get()
  smr_iv_ttl=(float(smry_value[0])+float(rir_cost3.get())+float(smr_tax1)+float(smr_tax2))-float(smr_discount)
  sum1=0.0
  
  
  in_tt_qry="select sum(totpaid),sum(balance) from invoice where invoice_number=%s"
  in_tt_qry_val=(inv_nmb_rir.get(),)
  fbcursor.execute(in_tt_qry,in_tt_qry_val)
  inv_value=fbcursor.fetchone()
  if int(taxtype[0])==2:
    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
    total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
    balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
    if crcy_tp_ps=="before amount": 
      discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21)
      tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=42)  
      cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
    elif cency_pos=="after amount":
      discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
      tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=42)  
      cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
    elif cency_pos=="before amount with space":
      discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
      tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=42)  
      cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
    elif cency_pos=="after amount with space":
      discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
      tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=42)  
      cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
    else:
      pass
  elif int(taxtype[0])==3:
    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=15)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=30)
    tax=Label(summaryfrme, text="Tax2").place(x=0 ,y=45)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
    total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
    balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
    if crcy_tp_ps=="before amount": 
      discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=15)
      tax1=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax1)).place(x=130 ,y=30)  
      ta2=Label(summaryfrme, text=str(crcy_tp)+str(smr_tax2)).place(x=130 ,y=45) 
      cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=126)
    elif cency_pos=="after amount":
      discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=15)
      tax1=Label(summaryfrme, text=str(smr_tax1)+str(crcy_tp)).place(x=130 ,y=30)
      ta2=Label(summaryfrme, text=str(smr_tax2)+str(crcy_tp)).place(x=130 ,y=45)   
      cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=126)
    elif cency_pos=="before amount with space":
      discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=15)
      tax1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_tax1)).place(x=130 ,y=30) 
      ta2=Label(summaryfrme, text=str(crcy_tp)+" "+str(smr_tax2)).place(x=130 ,y=45)  
      cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=126)
    elif cency_pos=="after amount with space":
      discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
      sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=15)
      tax1=Label(summaryfrme, text=str(smr_tax1)+" "+str(crcy_tp)).place(x=130 ,y=30)  
      ta2=Label(summaryfrme, text=str(smr_tax2)+" "+str(crcy_tp)).place(x=130 ,y=45) 
      cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=63) 
      order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=84)
      total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=105)
      balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=126)
    else:
      pass
  else:
      fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
      fir4Frame.place(x=740,y=520)
      summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
      summaryfrme.place(x=0,y=0,width=200,height=170)
      discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
      sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
      cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=42)
      order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=63)
      total=Label(summaryfrme, text="Total paid").place(x=0 ,y=84)
      balance=Label(summaryfrme, text="Balance").place(x=0 ,y=105)
      if crcy_tp_ps=="before amount": 
        discount1=Label(summaryfrme, text=str(crcy_tp)+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+str(smry_value[0])).place(x=130 ,y=21) 
        cost=Label(summaryfrme, text=str(crcy_tp)+str(smr_ext_cst)).place(x=130 ,y=42) 
        order1=Label(summaryfrme, text=str(crcy_tp)+str(smr_iv_ttl)).place(x=130 ,y=63)
        total1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[0])).place(x=130 ,y=84)
        balance1=Label(summaryfrme, text=str(crcy_tp)+str(inv_value[1])).place(x=130 ,y=105)
      elif cency_pos=="after amount":
        discount1=Label(summaryfrme, text=str(smr_discount)+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+str(crcy_tp)).place(x=130 ,y=21)
     
        cost=Label(summaryfrme, text=str(smr_ext_cst)+str(crcy_tp)).place(x=130 ,y=42) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+str(crcy_tp)).place(x=130 ,y=63)
        total1=Label(summaryfrme, text=str(inv_value[0])+str(crcy_tp)).place(x=130 ,y=84)
        balance1=Label(summaryfrme, text=str(inv_value[1])+str(crcy_tp)).place(x=130 ,y=105)
      elif cency_pos=="before amount with space":
        discount1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_discount)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(crcy_tp)+""+str(smry_value[0])).place(x=130 ,y=21)
  
        cost=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_ext_cst)).place(x=130 ,y=42) 
        order1=Label(summaryfrme, text=str(crcy_tp)+""+str(smr_iv_ttl)).place(x=130 ,y=63)
        total1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[0])).place(x=130 ,y=84)
        balance1=Label(summaryfrme, text=str(crcy_tp)+""+str(inv_value[1])).place(x=130 ,y=105)
      elif cency_pos=="after amount with space":
        discount1=Label(summaryfrme, text=str(smr_discount)+" "+str(crcy_tp)).place(x=130 ,y=0)
        sub1=Label(summaryfrme, text=str(smry_value[0])+" "+str(crcy_tp)).place(x=130 ,y=21)
  
        cost=Label(summaryfrme, text=str(smr_ext_cst)+" "+str(crcy_tp)).place(x=130 ,y=42) 
        order1=Label(summaryfrme, text=str(smr_iv_ttl)+" "+str(crcy_tp)).place(x=130 ,y=63)
        total1=Label(summaryfrme, text=str(inv_value[0])+" "+str(crcy_tp)).place(x=130 ,y=84)
        balance1=Label(summaryfrme, text=str(inv_value[1])+" "+str(crcy_tp)).place(x=130 ,y=105)
      else:
        pass

  #---------------------------------------------------------------------------------------recuring frame
  def reir_chk():
      if chk_sts.get() == 0:
        rir_spn_bx['state'] = DISABLED
        e1['state'] = DISABLED
        dt_nxt_inv['state'] = DISABLED
        stp_rir2['state'] = DISABLED
        dt_stp_inv['state'] = DISABLED
        rir_recalc_1['state'] = DISABLED
        
      else:
        rir_spn_bx['state'] = NORMAL
        e1['state'] = NORMAL
        dt_nxt_inv['state'] = NORMAL
        stp_rir2['state'] = NORMAL
        dt_stp_inv['state'] = NORMAL
        rir_recalc_1['state'] = NORMAL
  def recalc_rir():
      sql_rec='select * from company '
      fbcursor.execute(sql_rec)
      cmp_dtl=fbcursor.fetchone()
      rir_spn_val = rir_spn_bx.get()
      recur_stop = dt_nxt_inv.get_date()
      print(type(recur_stop))
      print(recur_stop)
      if main_cus_rir.get() == "month(s)":
        if cmp_dtl[10] == "mm-dd-yyyy":
          stop_date = datetime.strftime(recur_stop,"%m-%d-%Y")
          stop_d = datetime.strptime(stop_date,"%m-%d-%Y")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%m-%d-%Y")

        elif cmp_dtl[10] == "dd-mm-yyyy":
          stop_date = datetime.strftime(recur_stop,"%d-%m-%Y")
          print(stop_date)
          stop_d = datetime.strptime(stop_date,"%d-%m-%Y")
          print(stop_d)
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%d-%m-%Y")
          print(nxt_inv)
        elif cmp_dtl[10] == "yyyy.mm.dd":
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_date = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(months=+int(rir_spn_valrir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0}.{1:02}.{2:02}'.format(nxt.year,nxt.month,nxt.day)
        elif cmp_dtl[10] == "mm/dd/yyyy":
          stop_date = datetime.strftime(recur_stop,"%m/%d/%Y")
          stop_d = datetime.strptime(stop_date,"%m/%d/%Y")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%m/%d/%Y")
        elif cmp_dtl[10] == "dd/mm/yyyy":
          stop_date = datetime.strftime(recur_stop,"%d/%m/%Y")
          stop_d = datetime.strptime(stop_date,"%d/%m/%Y")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%d/%m/%Y")
        elif cmp_dtl[10] == "dd.mm.yyyy":
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_d = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0:02}.{1:02}.{2:02}'.format(nxt.day,nxt.month,nxt.year)
        elif cmp_dtl[10] == "yyyy/mm/dd":
          stop_date = datetime.strftime(recur_stop,"%Y/%m/%d")
          stop_d = datetime.strptime(stop_date,"%Y/%m/%d")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%Y/%m/%d")
        else:
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_d = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(months=+int(rir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0}/{1}/{2:02}'.format(nxt.month,nxt.day,nxt.year % 100)
        dt_nxt_inv.delete(0,END)
        dt_nxt_inv.insert(0,nxt_inv)
      else:
        if cmp_dtl[10] == "mm-dd-yyyy":
          stop_date = datetime.strftime(recur_stop,"%m-%d-%Y")
          stop_d = datetime.strptime(stop_date,"%m-%d-%Y")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%m-%d-%Y")
        elif cmp_dtl[10] == "dd-mm-yyyy":
          stop_date = datetime.strftime(recur_stop,"%d-%m-%Y")
          stop_d = datetime.strptime(stop_date,"%d-%m-%Y")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%d-%m-%Y")
        elif cmp_dtl[10] == "yyyy.mm.dd":
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_date = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0}.{1:02}.{2:02}'.format(nxt.year,nxt.month,nxt.day)
        elif cmp_dtl[10] == "mm/dd/yyyy":
          stop_date = datetime.strftime(recur_stop,"%m/%d/%Y")
          stop_d = datetime.strptime(stop_date,"%m/%d/%Y")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%m/%d/%Y")
        elif cmp_dtl[10] == "dd/mm/yyyy":
          stop_date = datetime.strftime(recur_stop,"%d/%m/%Y")
          stop_d = datetime.strptime(stop_date,"%d/%m/%Y")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%d/%m/%Y")
        elif cmp_dtl[10] == "dd.mm.yyyy":
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_d = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0:02}.{1:02}.{2:02}'.format(nxt.day,nxt.month,nxt.year)
        elif cmp_dtl[10] == "yyyy/mm/dd":
          stop_date = datetime.strftime(recur_stop,"%Y/%m/%d")
          stop_d = datetime.strptime(stop_date,"%Y/%m/%d")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt_inv = datetime.strftime(n,"%Y/%m/%d")
        else:
          stop_date = datetime.strftime(recur_stop,"%Y-%m-%d")
          stop_d = datetime.strptime(stop_date,"%Y-%m-%d")
          n = stop_d + relativedelta(days=+int(rir_spn_val))
          nxt = datetime.strptime(str(n.date()),"%Y-%m-%d")
          nxt_inv = '{0}/{1}/{2:02}'.format(nxt.month,nxt.day,nxt.year % 100)
        dt_nxt_inv.delete(0,END)
        dt_nxt_inv.insert(0,nxt_inv)

  labelframe2 = LabelFrame(recurFrame,text="",font=("arial",15))
  labelframe2.place(x=1,y=1,width=730,height=170)

  chk_sts=IntVar()

  stp_rir=Checkbutton(labelframe2,variable = chk_sts,text="Recurring",onvalue =1 ,offvalue = 0, command=reir_chk)
  if int(dtl_inv[50])==1:
    stp_rir.select()
  else:
    stp_rir.deselect()
  
  

  stp_rir.place(x=40,y=5)

  text1=Label(labelframe2,text="Recurring Period(Interval)").place(x=130,y=30)
  rir_spn_bx = Spinbox(labelframe2,from_=1,to=10,width=15,justify=RIGHT)
  
  rir_spn_bx.place(x=270,y=30)

  main_cus_rir=StringVar()
  e1 = ttk.Combobox(labelframe2,width=15, textvariable=main_cus_rir)
  e1['values']=('month(s)',"day(s)")
  e1.place(x=380,y=30)
  e1.current(0)

  por_sql_st='select * from company'
  fbcursor.execute(por_sql_st)
  cmpy_dtl=fbcursor.fetchone()

  sql='select dateformat from company'
  fbcursor.execute(sql)
  date_frmat=fbcursor.fetchone()
          
  # nxt =0
  # stp=0
  # if date_frmat[0] == "mm-dd-yyyy":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="mm-dd-yyyy")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="mm-dd-yyyy")
  #     stop_date = datetime.strftime(stp,"%m-%d-%Y")
  #     nxt_inv = datetime.strftime(nxt,"%m-%d-%Y")
  # elif date_frmat[0] == "dd-mm-yyyy":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="dd-mm-yyyy")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="dd-mm-yyyy")
  #     stop_date = datetime.strftime(stp,"%d-%m-%Y")
  #     nxt_inv = datetime.strftime(nxt,"%d-%m-%Y")
  # elif date_frmat[0] == "yyyy.mm.dd":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="yyyy.mm.dd")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="yyyy.mm.dd")
  #     s = datetime.strftime(stp,"%Y-%m-%d")
  #     v= datetime.strftime(nxt,"%Y-%m-%d")
  #     stop_d = datetime.strptime(s,"%Y-%m-%d")
  #     stop_date = '{0}.{1:02}.{2:02}'.format(stop_d.year,stop_d.month,stop_d.day)
  #     nxt = datetime.strptime(v,"%Y-%m-%d")
  #     nxt_inv = '{0}.{1:02}.{2:02}'.format(nxt.year,nxt.month,nxt.day)
  # elif date_frmat[0] == "mm/dd/yyyy":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="mm/dd/yyyy")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="mm/dd/yyyy")
  #     stop_date = datetime.strftime(stp,"%m/%d/%Y")
  #     nxt_inv = datetime.strftime(nxt,"%m/%d/%Y")
  # elif date_frmat[0] == "dd/mm/yyyy":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="dd/mm/yyyy")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="dd/mm/yyyy")
  #     stop_date = datetime.strftime(stp,"%d/%m/%Y")
  #     nxt_inv = datetime.strftime(nxt,"%d/%m/%Y")
  # elif date_frmat[0] == "dd.mm.yyyy":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="dd.mm.yyyy")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="dd.mm.yyyy")
  #     s = datetime.strftime(stp,"%Y-%m-%d")
  #     v= datetime.strftime(nxt,"%Y-%m-%d")
      
  #     stop_d = datetime.strptime(s,"%Y-%m-%d")
  #     stop_date = '{0:02}.{1:02}.{2:02}'.format(stop_d.day,stop_d.month,stop_d.year)
  #     nxt = datetime.strptime(v,"%Y-%m-%d")
  #     nxt_inv = '{0:02}.{1:02}.{2:02}'.format(nxt.day,nxt.month,nxt.year)
  # elif date_frmat[0] == "yyyy/mm/dd":
  #     dt_nxt_inv = DateEntry(labelframe2,width=20,date_pattern="yyyy/mm/dd")
  #     dt_stp_inv = DateEntry(labelframe2,width=20,date_pattern="yyyy/mm/dd")
  #     stop_date = datetime.strftime(stp,"%Y/%m/%d")
  #     nxt_inv = datetime.strftime(nxt,"%Y/%m/%d")
  # else:
  #     dt_nxt_inv = DateEntry(labelframe2,width=20)
  #     dt_stp_inv = DateEntry(labelframe2,width=20)
  #     s = datetime.strftime(stp,"%Y-%m-%d")
  #     v= datetime.strftime(nxt,"%Y-%m-%d")
  #     stop_d = datetime.strptime(s,"%Y-%m-%d")
  #     stop_date = '{0}/{1}/{2:02}'.format(stop_d.month,stop_d.day,stop_d.year % 100)
  #     nxt = datetime.strptime(v,"%Y-%m-%d")
  #     nxt_inv = '{0}/{1}/{2:02}'.format(nxt.month,nxt.day,nxt.year % 100)
  
  dt_nxt=Label(labelframe2,text="Next Invoice").place(x=300,y=60)
  dt_nxt_inv=DateEntry(labelframe2,width=15)
  dt_nxt_inv.delete(0,END)
  dt_nxt_inv.insert(0,dtl_inv[26])
  dt_nxt_inv.place(x=380,y=60)

  def stp_dt():
    if stp_chk.get()==0:
      dt_stp_inv["state"] =DISABLED
    else:
      dt_stp_inv["state"] =NORMAL
  stp_chk=IntVar()
  stp_rir2=Checkbutton(labelframe2,variable = stp_chk,text="Stop Recurring After",onvalue =1 ,offvalue = 0, command=stp_dt)
  if int(dtl_inv[50])==1:
      stp_rir2.select()
  else:
      stp_rir2.deselect()
  stp_rir2.place(x=240,y=85)
  dt_stp_inv=DateEntry(labelframe2,width=15)
  dt_stp_inv.delete(0,END)
  dt_stp_inv.insert(0,dtl_inv[27])
  dt_stp_inv.place(x=380,y=90)

  rir_recalc_1 = Button(labelframe2,image="",text="Recalculate",width=15,command=recalc_rir)
  # recur_recalc_1 = Button(labelframe2,compound=LEFT,image="",text="Recalculate",width=80,height=12,state=DISABLED,command="")
  # recur_recalc_1.place(x=480,y=70)
  rir_recalc_1.place(x=540,y=60)

  if chk_sts.get() == 0:
        rir_spn_bx['state'] = DISABLED
        e1['state'] = DISABLED
        dt_nxt_inv['state'] = DISABLED
        stp_rir2['state'] = DISABLED
        dt_stp_inv['state'] = DISABLED
        rir_recalc_1['state'] = DISABLED
  else:
        rir_spn_bx['state'] = NORMAL
        e1['state'] = NORMAL
        dt_nxt_inv['state'] = NORMAL
        stp_rir2['state'] = NORMAL
        dt_stp_inv['state'] = NORMAL
        rir_recalc_1['state'] = NORMAL

  
#-------------------------------------------------------------------------------------------payment frame
  labelframe3 = LabelFrame(payementFrame,text="",font=("arial",15))
  labelframe3.place(x=1,y=1,width=730,height=170)

  pym_rir_tr=ttk.Treeview(labelframe3, height=7)
  pym_rir_tr["columns"]=["1","2","3","4","5"]
  pym_rir_tr.column("#0", width=20)
  pym_rir_tr.column("1", width=200)
  pym_rir_tr.column("2", width=100)
  pym_rir_tr.column("3", width=100)
  pym_rir_tr.column("4", width=200)
  pym_rir_tr.column("5", width=100)
  pym_rir_tr.heading("#0",text="", anchor=W)
  pym_rir_tr.heading("1",text="Payment ID")
  pym_rir_tr.heading("2",text="Payement Date")
  pym_rir_tr.heading("3",text="Paid By")  
  pym_rir_tr.heading("4",text="Description")
  pym_rir_tr.heading("5",text="Amount")

  pym_rir_tr.place(x=0, y=0)
  

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)



#--------------------------------------------------------------------------------------Top Buttons

rirmainframe=Frame(tab4, relief=GROOVE, bg="#f8f8f2")
rirmainframe.pack(side="top", fill=BOTH)

rirmidFrame=Frame(rirmainframe, bg="#f5f3f2", height=60)
rirmidFrame.pack(side="top", fill=X)

w = Canvas(rirmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(rirmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

rir_gen = Button(rirmidFrame,compound="top", text="Generate recurring\n invoices",relief=RAISED, image=video,bg="#f8f8f2", fg="black", height=55, bd=1, width=95,command=gn_inv_sucss)
rir_gen.pack(side="left", pady=3, ipadx=4)


w = Canvas(rirmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

rir_edit_lbl = Button(rirmidFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=view_invs_rir) 
rir_edit_lbl.pack(side="left")


w = Canvas(rirmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

rirpreviewLabel = Button(rirmidFrame,compound="top", text="Print Preview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command= prview_rir_inv)
rirpreviewLabel.pack(side="left")

rir_pr_label = Button(rirmidFrame,compound="top", text="Print Invoice",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=rir_prnt_inv_rir)
rir_pr_label.pack(side="left")

w = Canvas(rirmidFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

rir_email_label = Button(rirmidFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=email_invoice_recurring)
rir_email_label.pack(side="left")


w = Canvas(rirmidFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

rir_srh_lbl = Button(rirmidFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=srh_rir)
rir_srh_lbl.pack(side="left")

w = Canvas(rirmidFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

rir_refresh_lbl = Button(rirmidFrame,compound="top", text="Refresh\nInvoices list",relief=RAISED, image=photo8,bg="#f8f8f2",fg="black", height=55, bd=1, width=75, command=rfh_rir)
rir_refresh_lbl.pack(side="left")

w = Canvas(rirmidFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)
def sum_lbl():
  labessl = Label(left_frame,bg="red",text = "$500")
show_ttl_sum = Button(rirmidFrame,compound="top", text="Show totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=sum_lbl)
show_ttl_sum.pack(side="left")

rir_hd_lbl = Button(rirmidFrame,compound="top", text="Hide totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: labessl.place_forget())
rir_hd_lbl.pack(side="left")



invoilabel = Label(rirmainframe, text="Recurring invoices", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))

#-----------------------------------------------------------------------------Recurring invoice table and scrollbars
def slt_main_sub(event):
  rir_id=rir_tree.item(rir_tree.focus())["values"][1]
  rir_main_table_sql="select * from storingproduct where invoice_number=%s"
  rir_main_table_sql_vals=(rir_id,)
  fbcursor.execute(rir_main_table_sql,rir_main_table_sql_vals)
  main_tb_rir=fbcursor.fetchall()
  count_cus=0
  sql_yty='select taxtype from company'
  fbcursor.execute(sql_yty)
  taxtype=fbcursor.fetchone()
  if int(taxtype[0])==2:
    for record in rir_tble.get_children():
          rir_tble.delete(record)
    for i in main_tb_rir:
        if i[11] is not None:
          dty="Yes"
        else:
          dty="No"
        rir_tble.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[0],i[6],i[7],i[13],i[9],dty,i[14]))
        count_cus +=1
  elif int(taxtype[0])==3:
    for record in rir_tble.get_children():
          rir_tble.delete(record)
    for i in main_tb_rir:
        if i[11] is not None:
          dty="Yes"
        else:
          dty="No"
        if i[12] is not None:
          dtst="Yes"
        else:
          dtst="No"
        rir_tble.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[0],i[6],i[7],i[13],i[9],dty,dtst,i[14]))
        count_cus +=1

  else:
    for record in rir_tble.get_children():
          rir_tble.delete(record)
    for i in main_tb_rir:
        rir_tble.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[0],i[6],i[7],i[13],i[9],i[14]))
        count_cus +=1

    


class RirMyApp1:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    global rir_tree
    rir_tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
    rir_tree.pack(side = 'top')
    rir_tree.heading(1)
    rir_tree.heading(2, text="Invoice#")
    rir_tree.heading(3, text="Next Invoice")
    rir_tree.heading(4, text="Recurring Period")
    rir_tree.heading(5, text="Stop After")
    rir_tree.heading(6, text="Customer Name")
    rir_tree.heading(7, text="Invoice Total")  
    rir_tree.column(1, width = 40)
    rir_tree.column(2, width = 200)
    rir_tree.column(3, width = 200,anchor='c')
    rir_tree.column(4, width = 200,anchor='c')
    rir_tree.column(5, width = 200,anchor='c')
    rir_tree.column(6, width = 340)
    rir_tree.column(7, width = 190,anchor='n')

    rir_tree.bind('<<TreeviewSelect>>',slt_main_sub)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1008+300+25, y=0, height=300+20)
    scrollbar.config( command=rir_tree.yview )

    rir_main_table_sql="select * from invoice where recurring_period IS NOT NULL"
    fbcursor.execute(rir_main_table_sql)
    main_rir_val=fbcursor.fetchall()
    count_rir=0

    for i in main_rir_val:
        rir_tree.insert(parent='', index='end', iid=count_rir, text='hello', values=("",i[1],i[26],i[24],i[27],i[18],i[8]))
        count_rir +=1


    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items')
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    global rir_tble
    sql_yty='select taxtype from company'
    fbcursor.execute(sql_yty)
    taxtype=fbcursor.fetchone()
    if int(taxtype[0])==2:
      rir_tble = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
      rir_tble.pack(side = 'top')
      rir_tble.heading(1)
      rir_tble.heading(2, text="Product/Service ID",)
      rir_tble.heading(3, text="Name")
      rir_tble.heading(4, text="Description")
      rir_tble.heading(5, text="Price")
      rir_tble.heading(6, text="QTY")
      rir_tble.heading(7, text="Tax1")
      rir_tble.heading(8, text="Line Total")   
      rir_tble.column(1, width = 40)
      rir_tble.column(2, width = 250)
      rir_tble.column(3, width = 270)
      rir_tble.column(4, width = 300)
      rir_tble.column(5, width = 130)
      rir_tble.column(6, width = 100)
      rir_tble.column(7, width = 100)
      rir_tble.column(8, width = 190)
    elif  int(taxtype[0])==3:
      rir_tble = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,9), height = 15, show = "headings")
      rir_tble.pack(side = 'top')
      rir_tble.heading(1)
      rir_tble.heading(2, text="Product/Service ID",)
      rir_tble.heading(3, text="Name")
      rir_tble.heading(4, text="Description")
      rir_tble.heading(5, text="Price")
      rir_tble.heading(6, text="QTY")
      rir_tble.heading(7, text="Tax1")
      rir_tble.heading(8, text="Tax1")
      rir_tble.heading(9, text="Line Total")   
      rir_tble.column(1, width = 20)
      rir_tble.column(2, width = 250)
      rir_tble.column(3, width = 200)
      rir_tble.column(4, width = 300)
      rir_tble.column(5, width = 120)
      rir_tble.column(6, width = 100)
      rir_tble.column(7, width = 100)
      rir_tble.column(8, width = 100)
      rir_tble.column(9, width = 190)
    else:
      rir_tble = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,), height = 15, show = "headings")
      rir_tble.pack(side = 'top')
      rir_tble.heading(1)
      rir_tble.heading(2, text="Product/Service ID",)
      rir_tble.heading(3, text="Name")
      rir_tble.heading(4, text="Description")
      rir_tble.heading(5, text="Price")
      rir_tble.heading(6, text="QTY")
      rir_tble.heading(7, text="Line Total")   
      rir_tble.column(1, width = 40)
      rir_tble.column(2, width = 300)
      rir_tble.column(3, width = 300)
      rir_tble.column(4, width = 300)
      rir_tble.column(5, width = 130)
      rir_tble.column(6, width = 120)
      
      rir_tble.column(7, width = 190)

    note1=Text(tab2, width=170,height=10).place(x=10, y=10)

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    rirs_tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    rirs_tree.pack(side = 'top')
    rirs_tree.heading(1)
    rirs_tree.heading(2, text="Attach to Email",)
    rirs_tree.heading(3, text="Filename")
    rirs_tree.column(1, width = 30)
    rirs_tree.column(2, width = 310)
    rirs_tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1004+300+25, y=360, height=195)
    scrollbar.config( command=rirs_tree.yview )
       
myapp = RirMyApp1(tab4)



root.mainloop()