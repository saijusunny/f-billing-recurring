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
fbcursor = fbilldb.cursor()
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
    rir_in_preview = Toplevel()
    rir_in_preview.title("F-Billing Revolution Invoice Report ")
    rir_in_p2= PhotoImage(file = "images/fbicon.png")
    rir_in_preview.iconphoto(False, rir_in_p2)
    rir_in_preview.geometry("1800x1800+0+0")
    rir_in_frame = Frame(rir_in_preview,width=1500,height=1800,bg="red")
    rir_in_frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    rir_in_frame.place(x=0,y=30)
    rir_in_canvas=Canvas(rir_in_frame,bg='grey',width=1400,height=1200,scrollregion=(0,0,1500, 1200))


    rir_in_vertibar=Scrollbar(rir_in_frame,orient=VERTICAL)
    rir_in_vertibar.pack(side=RIGHT,fill=Y)
    rir_in_vertibar.config(command=rir_in_canvas.yview)
    rir_in_canvas.config(width=1338,height=710)

    rir_in_canvas.config(yscrollcommand=rir_in_vertibar.set)
    rir_in_canvas.pack(expand=True,side=LEFT,fill=BOTH)

    rir_in_paperheigth = rir_in_preview.winfo_fpixels('1m') * 297
    rir_in_paperwidth = rir_in_preview.winfo_fpixels('1m') * 210
    rir_in_canvas.create_rectangle(265, 20, 265+rir_in_paperwidth, 20+rir_in_paperheigth, outline='orange', fill='white')
    rir_company = "SELECT * from company"
    fbcursor.execute(rir_company)
    rir_company= fbcursor.fetchone()

  # try:
    # rir_id=rir_main_tree.item(rir_main_tree.focus())["values"][3]

    # rir_main_table_sql="select * from orders where businessname=%s"
    # rir_main_table_sql_val=(rir_id,)
    # fbcursor.execute(rir_main_table_sql,rirrir_main_table_sql_val)
    # main_tb_val=fbcursor.fetchone()

    sqlr= 'select currencysign from company'
    fbcursor.execute(sqlr)
    crncy=fbcursor.fetchone()
    crc=crncy[0]
    sqlrt= 'select currsignplace from company'
    fbcursor.execute(sqlrt)
    post_rp=fbcursor.fetchone()
    ps_cr=post_rp[0]
    
    #-------------------------------------------------------------------------------------------------Heder data--------
    labelcmp=Label(rir_in_canvas,text=rir_company[1], bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=2)
    window = rir_in_canvas.create_window(300,80, anchor="nw", window=labelcmp)

    labelcmpl=Label(rir_in_canvas,text=rir_company[2], bg="white",font=("Helvetica", 9),anchor="nw", width=50,justify=LEFT, height=6)
    windowl = rir_in_canvas.create_window(300,120, anchor="nw", window=labelcmpl)
    rir_in_canvas.create_text(950,100, text="Invoices List",font=("Helvetica", 16), justify='right')
    rir_in_canvas.create_text(350,228,text=rir_company[4],fill='black',font=("Helvetica", 8), justify='left')
    # rir_in_canvas.create_text(953,220,text="Customer ID:"+str(main_tb_val[0]),fill='black',font=("Helvetica", 12), justify='right')

    # rir_sql5="select * from customer where businessname=%s"
    # rir_sql5_vals=(rir_id,)
    # fbcursor.execute(rir_sql5,rir_sql5_vals)
    # rir_det=fbcursor.fetchone()
    # rir_in_canvas.create_line(1038,235,280,235,fill="black", width=2)
    
    # rir_in_canvas.create_text(330,260,text="Bill To:",fill='black',font=("Helvetica", 12), justify='right')
    # labelcmp=Label(rir_in_canvas,text=rir_det[4] , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=1)
    # window = rir_in_canvas.create_window(305,275, anchor="nw", window=labelcmp)
    # text=rir_det[5]
    # wraped_text="\n".join(wrap(text,30))
    # labelcmp=Label(rir_in_canvas,text=wraped_text , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=4)
    # window = rir_in_canvas.create_window(305,295, anchor="nw", window=labelcmp)

    # rir_in_canvas.create_text(720,260,text="Ship To:",fill='black',font=("Helvetica", 12), justify='right')
    # labelcmp=Label(rir_in_canvas,text=rir_det[6] , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=1)
    # window = rir_in_canvas.create_window(690,275, anchor="nw", window=labelcmp)
    # text=rir_det[7]
    # wraped_text="\n".join(wrap(text,30))
    # labelcmp=Label(rirrir_in_canvas,text=wraped_text , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=4)
    # window = rir_in_canvas.create_window(690,295, anchor="nw", window=labelcmp)
    # #---------------------------------------------------------------------------------------------------Table Data

    # style=ttk.Style()
    # style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
    # style.configure("mystyle.Treeview.Heading", font=('Calibri', 13), background='white') # Modify the font of the headings
    # style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    # # Add a Treeview widge
                        
    # rir_prv_tree=ttk.Treeview(rir_in_canvas, column=("c1", "c2","c3", "c4", "c5", "c6", "c7","c8"), show='headings', height=30, style='mystyle.Treeview')
    # rir_prv_tree.column("# 1", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 1", text="Invoice No")
    # rir_prv_tree.column("# 2", anchor=E, stretch=NO, width=80)
    # rir_prv_tree.heading("# 2", text="Date")
    # rir_prv_tree.column("# 3", anchor=E, stretch=NO, width=80)
    # rir_prv_tree.heading("# 3", text="Due Date")
    # rir_prv_tree.column("# 4", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 4", text="Recurring")
    # rir_prv_tree.column("# 5", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 5", text="Status")
    # rir_prv_tree.column("# 6", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 6", text="Invoice Total")
    # rir_prv_tree.column("# 7", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 7", text="Total Paid")
    # rir_prv_tree.column("# 8", anchor=E, stretch=NO, width=100)
    # rir_prv_tree.heading("# 8", text="Balance")

    # sql_qry="select * from invoice where businessname=%s"
    # sql_qryvlz=(rir_id,)
    # fbcursor.execute(sql_qry,sql_qryvlz)
    # tre=fbcursor.fetchall() 
    # for record in rir_prv_tree.get_children():
    #   rir_prv_tree.delete(record)
        

    # count=0
    # for i in tre:
    #   if i[24] is None:
    #     dfh="No"
    #   else:
    #     dfh="Yes"
    #   if ps_cr=="before amount":
    #     rir_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], crc+str(i[8]), crc+str(i[9]), crc+str(i[10])))
                      
    #   elif ps_cr=="after amount":
    #     rir_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], str(i[8])+crc, str(i[9])+crc,str(i[10])+crc))
                        
    #   elif ps_cr=="before amount with space":
    #     rir_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], crc+" "+str(i[8]), crc+" "+str(i[9]), crc+" "+str(i[10])))
                        
    #   elif ps_cr=="after amount with space":
    #     rir_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5],  str(i[8])+" "+crc, str(i[9])+" "+crc,str(i[10])+" "+crc))
                        
                    
    #   else:
    #     pass
    #   count += 1
    # rir_prv_tree.insert('', 'end',text="1",values=('','','','','','','',''))
    # rir_prv_tree.insert('', 'end',text="1",values=('','','-End List-','','','Invoice Total','Total Paid','Balance'))
    # sql_inv_t="select sum(invoicetot),sum(totpaid), sum(balance) from invoice where businessname=%s"
    # sql_inv_t_val=(rir_id,)
    # fbcursor.execute(sql_inv_t,sql_inv_t_val)
    # inv_ttt=fbcursor.fetchone() 
    
    # if ps_cr=="before amount":
    #   rir_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',crc+str(inv_ttt[0]),crc+str(inv_ttt[1]),crc+str(inv_ttt[2])))
    # elif ps_cr=="after amount":
    #   rir_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',str(inv_ttt[0])+crc,str(inv_ttt[1])+crc,str(inv_ttt[2])+crc))
    # elif ps_cr=="before amount with space":
    #   rir_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',crc+" "+str(inv_ttt[0]),crc+" "+str(inv_ttt[1]),crc+" "+str(inv_ttt[2])))
    # elif ps_cr=="after amount with space":
    #   rir_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',str(inv_ttt[0])+" "+crc,str(inv_ttt[1])+" "+crc,str(inv_ttt[2])+" "+crc))
    # else:
    #   pass
    


    # window = rir_in_canvas.create_window(280, 320, anchor="nw", window=rir_prv_tree)
  # except:
  #   pass 

#------------------------------------------------------------------------------------------------convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
#--------------------------------------------------------------------------------------------------search in invoice 
def srh_rir():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                    
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)

#-------------------------view/edit invoice---------------------------

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


    #add new customer
    def create_newcustomer_recurring():
      ven=Toplevel(rirmidFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

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


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create_newcustomer_recurring).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create_newcustomer_recurring).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   
 
  #add new line item
  def newline_recurring():
    newselection=Toplevel()
    newselection.title("Product/Services")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)


    #add new product
    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe, value='0')
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe, value='0')
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)




      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=ctegorytree.yview )
   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)
  
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
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=customer_invoice_recurring)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=addnew,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline_recurring)
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

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  cusr_selct=rir_tree.item(rir_tree.focus())["values"][5]#---------------------------------values Insertion edit
  
  sdrt_qsy='select businessname from customer'
  fbcursor.execute(sdrt_qsy)
  dtl_rir=fbcursor.fetchall()

  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Order to").place(x=10,y=5)

  cust_selction_nm=StringVar()
  e1 = ttk.Combobox(labelframe1,width=28, textvariable=cust_selction_nm)
  e1['values']=dtl_rir
  e1.place(x=80,y=5)
  e1.insert(0,cusr_selct)


  sdrt_qsy='select * from customer where businessname=%s'
  sdrt_qry_qtr=(cust_selction_nm.get(),)
  fbcursor.execute(sdrt_qsy,sdrt_qry_qtr)
  dtl_rir_cus=fbcursor.fetchone()

  
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23)
  e2.insert(1.0,str(dtl_rir_cus[5]))
  e2.place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30)
  e3.insert(0,str(dtl_rir_cus[6]))
  e3.place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23)
  e4.insert(1.0,str(dtl_rir_cus[7]))
  e4.place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30)
  e5.insert(0,str(dtl_rir_cus[9]))
  e5.place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  e6=Entry(labelframe2,width=30)
  e6.insert(0,str(dtl_rir_cus[12]))
  e6.place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  e1=Entry(labelframe,width=25).place(x=100,y=5,)
  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
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
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

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
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)
#---------------------------------------------------------------------------------------recuring frame
  labelframe2 = LabelFrame(recurFrame,text="",font=("arial",15))
  labelframe2.place(x=1,y=1,width=730,height=170)
  checkvarStatus5=IntVar()
  stp_rir=Checkbutton(labelframe2,variable = checkvarStatus5,text="Recurring",onvalue =0 ,offvalue = 1)
  stp_rir.place(x=40,y=5)

  text1=Label(labelframe2,text="Recurring Period(Interval)").place(x=130,y=30)
  rir_spn_bx = Spinbox(labelframe2,from_=1,to=1000000,width=15,justify=RIGHT)
  rir_spn_bx.place(x=270,y=30)

  cust_selction_nm=StringVar()
  e1 = ttk.Combobox(labelframe2,width=15, textvariable=cust_selction_nm)
  e1['values']=('month(s)',"day(s)")
  e1.place(x=380,y=30)
  e1.insert(0,cusr_selct)

  dt_nxt=Label(labelframe2,text="Next Invoice").place(x=300,y=60)
  dt_nxt_inv=DateEntry(labelframe2,width=15)
  dt_nxt_inv.place(x=380,y=60)

  checkvarStatus5=IntVar()
  stp_rir=Checkbutton(labelframe2,variable = checkvarStatus5,text="Stop Recurring After",onvalue =0 ,offvalue = 1)
  stp_rir.place(x=240,y=85)
  dt_stp_inv=DateEntry(labelframe2,width=15)
  dt_stp_inv.place(x=380,y=90)


  
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

rir_refresh_lbl = Button(rirmidFrame,compound="top", text="Refresh\nInvoices list",relief=RAISED, image=photo8,bg="#f8f8f2",fg="black", height=55, bd=1, width=75)
rir_refresh_lbl.pack(side="left")

w = Canvas(rirmidFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

show_ttl_sum = Button(rirmidFrame,compound="top", text="Show totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place())
show_ttl_sum.pack(side="left")

rir_hd_lbl = Button(rirmidFrame,compound="top", text="Hide totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place_forget())
rir_hd_lbl.pack(side="left")

label = Label(rirmainframe, text = "$500")
label.place(x= 100 , y=120)


invoilabel = Label(rirmainframe, text="Recurring invoices", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))

#-----------------------------------------------------------------------------Recurring invoice table and scrollbars

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

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1008+300+25, y=0, height=300+20)
    scrollbar.config( command=rir_tree.yview )

    rir_main_table_sql="select * from invoice"
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