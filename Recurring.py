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
color = PhotoImage(file="images/font_color.png")

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
photo11 = PhotoImage(file = "images/export excel.png")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
recurring_main=Frame(tab4, relief=GROOVE, bg="#f8f8f2")
recurring_main.pack(side="top", fill=BOTH)

recurringframe=Frame(recurring_main, bg="#f8f8f2", height=60)
recurringframe.pack(side="top", fill=X)


cus_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=(5, 2))
cus_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=(0, 5))

ad_rcr = PIL.Image.open("images/video1.png")
cus_rcr_Icon=ImageTk.PhotoImage(ad_rcr)

rcr_gen_recr = Button(recurringframe,compound="top", text="Genarate Recurring\nInvoice",relief=RAISED,  command="lambda:cus_add_customer()",          image=cus_rcr_Icon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=90)
rcr_gen_recr.pack(side="left", pady=3, ipadx=4)

rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

rcr_edit = PIL.Image.open("images/edit.png")
rir_edit_Icon=ImageTk.PhotoImage(rcr_edit)
rir_Label = Button(recurringframe,compound="top", text="View/Edit\nInvoice",relief=RAISED,command="lambda:cus_edit_customer()", image=rir_edit_Icon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
rir_Label.pack(side="left")
rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

rir_pr = PIL.Image.open("images/priewok.png")
rir_pry_Icon=ImageTk.PhotoImage(rir_pr)
rir_pry_Label = Button(recurringframe,compound="top", text="Print Preview",relief=RAISED, command="lambda:cus_delete_customer()",image=rir_pry_Icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
rir_pry_Label.pack(side="left")


rir_pri = PIL.Image.open("images/printer.png")
rir_pry_icon=ImageTk.PhotoImage(rir_pri)
rir_pri_Label = Button(recurringframe,compound="top",command="lambda:cus_previewinvoice_customer()", text="Preview\nInvoice",relief=RAISED,               image=rir_pry_icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
rir_pri_Label.pack(side="left")

rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

rir_eml = PIL.Image.open("images/gmail.png")
rir_eml_Icon=ImageTk.PhotoImage(rir_eml)
cus_eml_Label = Button(recurringframe,compound="top", text="Email Invoice",relief=RAISED,  command="lambda:cus_printinvoice_customer()", image=rir_eml_Icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
cus_eml_Label.pack(side="left")

rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

rir_srh = PIL.Image.open("images/search-icon.png")
cus_srh_Icon=ImageTk.PhotoImage(rir_srh)
cus_srh_Label = Button(recurringframe,compound="top",command="lambda:cus_addemail_order()", text="Search\nInvoice",relief=RAISED,               image=cus_srh_Icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
cus_srh_Label.pack(side="left")

rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

rir_rfh = PIL.Image.open("images/refresh.png")
rir_rfh_Icon=ImageTk.PhotoImage(rir_rfh)
rir_rfhLabel = Button(recurringframe,compound="top", text="Refresh\nInvoice List",command="lambda:cus_customersms()", relief=RAISED, image=rir_rfh_Icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
rir_rfhLabel.pack(side="left")

rir_pn = Canvas(recurringframe, width=1, height=65, bg="#b3b3b3", bd=0)
rir_pn.pack(side="left", padx=5)

clcu = PIL.Image.open("images/sum.png")
rir_clcu_Icon=ImageTk.PhotoImage(clcu)
rir_clcu_Label = Button(recurringframe,compound="top", text="Hide Total\nSum",command="lambda:import_customer_check()",relief=RAISED, image=rir_clcu_Icon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=65)
rir_clcu_Label.pack(side="left")

cus_pn = Canvas(tab4, width=1370, height=350, bg="#f8f8f2", bd=0)
cus_pn.pack(side="top")

cus_invoi1label = Label(tab4, text="Recurring Invoice", font=("arial", 18), bg="#f8f8f2")
cus_invoi1label.place(x=0,y=65)


#***************************************************************************************Functions
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$((Top Button Functions))
#---------------------------------------------------------------------------------Mail
def cus_send_mails():
      
      cus_sender_email = "saijuinfox@gmail.com"    
      cus_sender_password = "8848937577" 

      cus_server = smtplib.SMTP('smtp.gmail.com', 587)
    
      cus_server.starttls()

      cus_server.login(cus_sender_email, cus_sender_password)

    
      cus_carbcopy_info = cus_carcopyem_address.get()
      

    
      cus_msg = MIMEMultipart()
      cus_msg['Subject'] = cus_email_subject.get() 
    
      cus_mail_content  = cus_mframe.get('1.0','end-1c') 
      cus_msg['From'] = cus_email_from.get()
      cus_msg['To'] = cus_email_address.get()
    
        
      cus_gettingimg=cus_lstfrm.get()
      cus_lst_data = cus_gettingimg[1:-1].split(',')


      cus_msg.attach(MIMEText(cus_mail_content, 'plain'))

      for i in cus_lst_data:
          if len(i.strip()[1:-1])>1:

              with open('images/'+ i.strip()[1:-1], "rb") as attachment:
    
                  cus_part = MIMEBase("application", "octet-stream")
                  cus_part.set_payload(attachment.read())

                  encoders.encode_base64(cus_part)
                  cus_part.add_header('Content-Disposition', "attachment; filename= %s" % 'images/'+ i.strip()[1:-1]) 

      
                  cus_msg.attach(cus_part)
        

      cus_server.sendmail(cus_email_from.get(),cus_email_address.get(),cus_msg.as_string())
      cus_server.sendmail(cus_email_from.get(), cus_carbcopy_info,cus_msg.as_string()) 
def cus_empsfile_image(event):
            global cus_yawn
            for i in cus_htcodeframe.curselection():
              print("hloo",cus_htcodeframe.get(i))
              cus_yawn=cus_htcodeframe.get(i)        
              edit_window_img = Toplevel()
              edit_window_img.title("View Image")
              edit_window_img.geometry("700x500")
              image = Image.open("images/"+cus_yawn)
              resize_image = image.resize((700, 500))
              image = ImageTk.PhotoImage(resize_image)
              cus_psimage = Label(edit_window_img,image=image)
              cus_psimage.photo = image
              cus_psimage.pack()
def cus_file(event):
      try:
        all_items = cus_htcodeframe.get(0, tk.END) # tuple with text of all items in Listbox
        sel_idx = cus_htcodeframe.curselection() # tuple with indexes of selected items
        sel_list = [all_items[item] for item in sel_idx]
        
        if sel_list[0]=='CInvoice.pdf':
          win32api.ShellExecute(0,"",cus_filenamezrrr,None,".",0)
        else:
          win32api.ShellExecute(0,"",cus_filenamez,None,".",0)
      except:
        pass
def cus_UploadAction(event=None):
        global cus_filenamez
        cus_filenamez = askopenfilename(filetypes=(('PDF', '*.pdf',),("png file ",'.png'),("jpg file", ".jpg"),  ("All files", "*.*"),))
        
        shutil.copyfile(cus_filenamez, os.getcwd()+'/images/'+cus_filenamez.split('/')[-1])
        cus_htcodeframe.insert(0, cus_filenamez.split('/')[-1]) 
def cus_addemail_order():

          cus_mailDetail=Toplevel()
          cus_mailDetail.title("Send E-mail")
          cus_mailDetail.geometry("1080x550")
          cus_mailDetail.resizable(False, False)

          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", padding=5)
          cus_email_Notebook = ttk.Notebook(cus_mailDetail)
          cus_email_Frame = Frame(cus_email_Notebook, height=500, width=1080)
          cus_account_Frame = Frame(cus_email_Notebook, height=550, width=1080)
          cus_email_Notebook.add(cus_email_Frame, text="E-mail")
          cus_email_Notebook.add(cus_account_Frame, text="Account")
          cus_email_Notebook.place(x=0, y=0)

          cus_messagelbframe=LabelFrame(cus_email_Frame,text="Message", height=500, width=730)
          cus_messagelbframe.place(x=5, y=5)
          global cus_email_address, cus_email_subject, cus_email_from,cus_email_pswrd,cus_carcopyem_address,cus_mframe,cus_htcodeframe,cus_lstfrm,cus_langs
          cus_email_address = StringVar() 
          cus_email_subject = StringVar()

          cus_email_from = StringVar()
          cus_email_pswrd = StringVar()
          cus_carcopyem_address = StringVar()
          
          
          cus_lbl_emailtoaddr=Label(cus_messagelbframe, text="Email to address").place(x=5, y=5)
          cus_emailtoent=Entry(cus_messagelbframe, width=50,textvariable=cus_email_address)
          cus_emailtoent.place(x=120, y=5)
          cus_id=cus_main_tree.item(cus_main_tree.focus())["values"][1]
          
          if cus_id is None:
            pass
          else:
            sqrty="select cpemail from customer where customerno=%s"
            sqrty_val=(cus_id,)
            fbcursor.execute(sqrty,sqrty_val)
            dtre=fbcursor.fetchone()
            cus_emailtoent.insert(0,dtre[0])
        
          cus_sendemail_btn=Button(cus_messagelbframe, text="Send Email", width=10, height=1, command=cus_send_mails).place(x=600, y=10)

          cus_lbl_carcopyto=Label(cus_messagelbframe, text="Carbon copy to").place(x=5, y=32)
          cus_carcopyent=Entry(cus_messagelbframe, width=50,textvariable=cus_carcopyem_address)
          cus_carcopyent.place(x=120, y=32)

          cus_lbl_subject=Label(cus_messagelbframe, text="Subject").place(x=5, y=59)
          cus_subent=Entry(cus_messagelbframe, width=50, textvariable=cus_email_subject)
          cus_subent.place(x=120, y=59)
          cus_subjectinsrt='ORD_'+str("")
          cus_subent.delete(0,'end')
          cus_subent.insert(0, cus_subjectinsrt)

          
          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
          cus_mess_Notebook = ttk.Notebook(cus_messagelbframe)
          cus_emailmessage_Frame =Frame(cus_mess_Notebook, height=350, width=710)
          cus_htmlsourse_Frame = Frame(cus_mess_Notebook, height=350, width=710)
          cus_mess_Notebook.add(cus_emailmessage_Frame, text="E-mail message")

          cus_mess_Notebook.add(cus_htmlsourse_Frame, )
          cus_mess_Notebook.place(x=5, y=90)
          

          

          from tkinter import font,colorchooser
          fontSize=16
          fontStyle='Arial'
          
          def cus_font_style(event):
              global fontStyle
              fontStyle=font_family_variable.get()
              cus_mframe.config(font=(fontStyle,fontSize))

          def cus_font_size(event):
              global fontSize
              
              fontSize=size_variable.get()
              
              
              cus_mframe.config(font=(fontStyle,fontSize))

          def cus_bold_text():
              bold_font = font.Font(cus_mframe, cus_mframe.cget("font"))
              bold_font.configure(weight="bold")

              cus_mframe.tag_configure("bold", font=bold_font)

              current_tags = cus_mframe.tag_names("sel.first")

              if "bold" in current_tags:
                cus_mframe.tag_remove("bold", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("bold", "sel.first", "sel.last")    
          
          def cus_italic_text():
              italic_font = font.Font(cus_mframe, cus_mframe.cget("font"))
              italic_font.configure(slant="italic")

              cus_mframe.tag_configure("italic", font=italic_font)

              current_tags = cus_mframe.tag_names("sel.first")

              if "italic" in current_tags:
                cus_mframe.tag_remove("italic", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("italic", "sel.first", "sel.last")

          def cus_underline_text():
            try:
                if cus_mframe.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
                    cus_mframe.tag_remove('underline_selection', 'sel.first', 'sel.last')
                else:
                    cus_mframe.tag_add('underline_selection', 'sel.first', 'sel.last')
                    cus_mframe.tag_configure('underline_selection', underline=True)
            except TclError:
                pass

          def cus_color_select():
              color=colorchooser.askcolor()[1]
              if color:
            # if color:

                color_font = font.Font(cus_mframe, cus_mframe.cget("font"))

                cus_mframe.tag_configure("colored", font=color_font, foreground=color)

                current_tags = cus_mframe.tag_names("sel.first")

              if "colored" in current_tags:
                cus_mframe.tag_remove("colored", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("colored", "sel.first", "sel.last")

          def cus_align_right():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('right',justify=RIGHT)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'right')

          def cus_align_left():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('left',justify=LEFT)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'left')

          def cus_align_center():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('center',justify=CENTER)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'center')

          def add_link():
              # from tkHyperLinkManager import HyperlinkManager
              # import webbrowser
              # from functools import partial
              
              hghf=cus_mframe.selection_get()
              content=hghf
              
              
            #   content.configure(foreground="red")
              cus_mframe.insert(END, " "+content)
              
              # cus_mframe.delete(1.0,END)
              
              
              
          def callback(url):
              webbrowser.open_new_tab_url(url)

          def addlinkbox():
              global top
              top = Toplevel()
              top.title('Hyperlink')
              top.geometry("400x100")
              hyp_lbl = LabelFrame(top,text="Hyperlink Information", height=80, width=300)
              hyp_lbl.place(x=10, y=5)

              hyp_lbl1 = Label(top,text="Type:")
              hyp_lbl1.place(x=18, y=24)
              
              def comb_select(event):
                  hyper = cb_comb.get()
                  if hyper == "(other)":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "(other)")
                  elif hyper == "file://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "file://")
                  elif hyper == "ftp://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "ftp://") 
                  elif hyper == "http://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "http://") 
                  elif hyper == "https://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "https://") 
                  elif hyper == "mailto:":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "mailto:") 
                  elif hyper == "telnet:":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "telnet:")


              cb_comb = StringVar()
              cb1=ttk.Combobox(top,textvariable=cb_comb,width=15)
              cb1.grid(row=1,column=1,padx=90,pady=30)
              cb1['values']=('(other)','file://','ftp://','http://','https://','mailto:','news:','telnet:')
              cb1.current(0)
              cb1.bind('<<ComboboxSelected>>',comb_select)


              hyp_lbl2 = Label(top,text="URL:")
              hyp_lbl2.place(x=18, y=55)
              global cus_hyper
              cus_hyper = StringVar()
              
              hyp= Entry(top,textvariable=cus_hyper,width=35)
              hyp.place(x=90,y=55)

              

              hypbtn1 = Button(top,text="OK",width=10, command=add_link)
              hypbtn1.place(x=315,y=8)

              hypbtn2 = Button(top,text="Cancel",width=10)
              hypbtn2.place(x=315,y=35)

         

          cus_mframe=Text(cus_emailmessage_Frame,undo=True,width=84, bg="white", height=20)
          cus_mframe.pack(padx=0,pady=28,expand=False)


          cus_scrollbar1 = Scrollbar(cus_emailmessage_Frame,orient=VERTICAL,command=cus_mframe.yview)
          cus_scrollbar3= Scrollbar(cus_emailmessage_Frame,orient=HORIZONTAL,command=cus_mframe.xview, width=0)
          cus_scrollbar3.place(x=0, y=340, height=20,width=690)
          cus_scrollbar2= Scrollbar(cus_mframe,orient=HORIZONTAL,command=cus_mframe.xview, width=0)
          cus_scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=310,pady=155)
        #   cus_scrollbar2.place(x=0, y=310, height=20,width=670)
          cus_mframe.config(xscrollcommand=cus_scrollbar2.set)
          cus_mframe.config(yscrollcommand=cus_scrollbar1.set)
          cus_scrollbar1.config(command=cus_mframe.yview)
          cus_scrollbar1.place(x =690, y=0, height=360)
          cus_scrollbar2.config(command=cus_mframe.xview)


          cus_btn1=Button(cus_emailmessage_Frame,width=20,height=20,compound = LEFT,image=selectall,command=lambda :cus_mframe.event_generate('<Control a>'))
          cus_btn1.place(x=0, y=1)

                  
          cus_btn2=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :cus_mframe.event_generate('<Control x>'))
          cus_btn2.place(x=36, y=1)

          cus_btn3=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :cus_mframe.event_generate('<Control c>'))
          cus_btn3.place(x=73, y=1)

          cus_btn4=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :cus_mframe.event_generate('<Control v>'))
          cus_btn4.place(x=105, y=1)
          cus_btn5=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo, command=lambda:cus_mframe.event_generate("<<Undo>>")).place(x=140, y=1)

          cus_btn6=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo, command=lambda:cus_mframe.event_generate("<<Redo>>")).place(x=175, y=1)

          cus_btn7=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold,command=cus_bold_text)
          cus_btn7.place(x=210, y=1)

          cus_btn8=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics,command=cus_italic_text)
          cus_btn8.place(x=245, y=1)

          cus_btn9=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline,command=cus_underline_text)
          cus_btn9.place(x=280, y=1)

          cus_btn10=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=left,command=cus_align_left)
          cus_btn10.place(x=315, y=1)

          cus_btn11=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=right,command=cus_align_right)
          cus_btn11.place(x=350, y=1)

          cus_btn12=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=center,command=cus_align_center)
          cus_btn12.place(x=385, y=1)

          cus_btn14=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :cus_mframe.delete(0.0,END))
          cus_btn14.place(x=455, y=1)
          
          cus_btn15=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=cus_color_select)
          cus_btn15.place(x=420, y=1)
          cus_btn16=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink, command="addlinkbox")
          cus_btn16.place(x=491, y=1)
          global size_variable
          size_variable=IntVar()

          cus_dropcomp11 = ttk.Combobox(cus_emailmessage_Frame, width=6, textvariable=size_variable, values=tuple(range(8,17)))
          
          cus_dropcomp11.place(x=530, y=5)
        #   cus_dropcomp11.bind('<<ComboboxSelected>>',frmar)
          
          font_family_variable=StringVar()
          font_familyes=font.families()
          # dropcompo147 = ttk.Combobox(cus_emailmessage_Frame, width=10, textvariable=font_family_variable, values=font_familyes)
          # dropcompo147.place(x=600, y=5)
          # dropcompo147.current(font_familyes.index('Arial'))
          # dropcompo147.bind('<<ComboboxSelected>>', cus_font_style)
          cus_dropcomp11.bind('<<ComboboxSelected>>', cus_font_size)
          
          cus_attachlbframe=LabelFrame(cus_email_Frame,text="Attachment(s)", height=350, width=280)
          cus_attachlbframe.place(x=740, y=5)
          ##########################################################print()
          from reportlab.pdfgen import canvas
          # from tkdocviewer import *
          from reportlab.lib import colors
          from reportlab.pdfbase.ttfonts import TTFont
          from reportlab.pdfbase import pdfmetrics
          from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
          from reportlab.lib.pagesizes import letter, inch
          try:
              pdf = canvas.Canvas("customer_Reports/CInvoice.pdf", pagesize=letter)
              cus_id=cus_main_tree.item(cus_main_tree.focus())["values"][3]
              sqlt= 'select * from customer where businessname=%s'
              sqlt_val=(cus_id,)
              fbcursor.execute(sqlt,sqlt_val)
              cus_ft=fbcursor.fetchone()

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
              pdf.drawString(35,700, "Sales tax reg No:"+company[4])
              pdf.drawString(490,760, "Invoice Report")

              pdf.drawString(460,700,"Customer ID:"+str(cus_ft[0]))
              pdf.drawString(28,695,"__________________________________________________________________________________")
              pdf.drawString(31,680,"Bill To:")
              pdf.drawString(31,668,cus_ft[4])
              text=cus_ft[5]
              wraped_text="\n".join(wrap(text,30))
              htg=wraped_text.split('\n')
                  
              vg=len(htg)
              if vg>0:
                      pdf.drawString(30,654,htg[0])
                      print("1")
                      if vg>1:
                        pdf.drawString(30,640,htg[1])
                        print("2")
                        if vg>2:
                            pdf.drawString(30,626,htg[2])
                            print("3")
                            if vg>3:
                                pdf.drawString(30,612,htg[3])
                                print("4")
                            else:
                                pass
                        else:
                            pass
                      else:
                          pass
                      
              else:
                      pass

              pdf.drawString(400,680,"Ship To:")
              pdf.drawString(400,668,cus_ft[6])
              text=cus_ft[7]
              wraped_text="\n".join(wrap(text,30))
              htg=wraped_text.split('\n')
                  
              vg=len(htg)
              if vg>0:
                      pdf.drawString(400,654,htg[0])
                      print("1")
                      if vg>1:
                        pdf.drawString(400,640,htg[1])
                        print("2")
                        if vg>2:
                            pdf.drawString(400,626,htg[2])
                            print("3")
                            if vg>3:
                                pdf.drawString(400,612,htg[3])
                                print("4")
                            else:
                                pass
                        else:
                            pass
                      else:
                          pass
                      
              else:
                      pass

              pdf.drawString(28,606,"__________________________________________________________________________________")


              pdf.drawString(28,591,"__________________________________________________________________________________")
              pdf.drawString(28,591,"Invoice No           Date        Due Date     Recurring      Status        Invoice Total    Total Paid   Balance      ")
              
              
              sqlr= 'select currencysign from company'
              fbcursor.execute(sqlr)
              crncy=fbcursor.fetchone()
                
              crc=crncy[0]
              sqlrt= 'select currsignplace from company'
              fbcursor.execute(sqlrt)
              post_rp=fbcursor.fetchone()
              ps_cr=post_rp[0]
              count=0
              sql_inv_dt='SELECT * FROM invoice where businessname=%s'
              inv_valuz=(cus_id,)
              fbcursor.execute(sql_inv_dt,inv_valuz)
              tre=fbcursor.fetchall()
              x=571

              for i in tre:
                            if x==38 or x==50:
                                pdf.showPage()
                                x=750
                            else:
                                if i[24] is None:
                                    dfh="No"
                                else:
                                    dfh="Yes"
                                if ps_cr=="before amount":
                                    pdf.drawString(28,x,str(i[1]))
                              
                                    pdf.drawString(100,x,str(i[2]))
                                    pdf.drawString(168,x,str(i[3]))
                                    pdf.drawString(250,x,dfh)
                                    pdf.drawString(315,x,str(i[5])) 
                                    pdf.drawString(380,x,str(crc)+str(i[8]))
                                    pdf.drawString(460,x,str(crc)+str(i[9]))
                                    pdf.drawString(522,x,str(crc)+str(i[10]))
                                    
                                elif ps_cr=="after amount":
                                    pdf.drawString(28,x,str(i[1]))
                                    pdf.drawString(100,x,str(i[2]))
                                    pdf.drawString(168,x,str(i[3]))
                                    pdf.drawString(250,x,str(dfh))
                                    pdf.drawString(315,x,str(i[5])) 
                                    pdf.drawString(380,x,str(i[8])+str(crc))
                                    pdf.drawString(460,x,str(i[9])+str(crc))
                                    pdf.drawString(522,x,str(i[10])+str(crc))
                                    
                                elif ps_cr=="before amount with space":
                                    pdf.drawString(28,x,str(i[1]))
                              
                                    pdf.drawString(100,x,str(i[2]))
                                    pdf.drawString(168,x,str(i[3]))
                                    pdf.drawString(250,x,str(dfh))
                                    pdf.drawString(315,x,str(i[5])) 
                                    pdf.drawString(380,x,str(crc)+" "+str(i[8]))
                                    pdf.drawString(460,x,str(crc)+" "+str(i[9]))
                                    pdf.drawString(522,x,str(crc)+" "+str(i[10]))
                                    
                                    
                                elif ps_cr=="after amount with space":
                                    pdf.drawString(28,x,str(i[1]))
                                    pdf.drawString(100,x,str(i[2]))
                                    pdf.drawString(168,x,str(i[3]))
                                    pdf.drawString(250,x,str(dfh))
                                    pdf.drawString(315,x,str(i[5])) 
                                    pdf.drawString(380,x,str(i[8])+" "+str(crc))
                                    pdf.drawString(460,x,str(i[9])+" "+str(crc))
                                    pdf.drawString(522,x,str(i[10])+" "+str(crc))
                                
                                else:
                                    pass
                              
                            count += 1
                          
                            x-=15
              sql_inv_t="select sum(invoicetot),sum(totpaid), sum(balance) from invoice where businessname=%s"
              sql_inv_t_val=(cus_id,)
              fbcursor.execute(sql_inv_t,sql_inv_t_val)
              inv_ttt=fbcursor.fetchone() 
              pdf.drawString(28,x,"__________________________________________________________________________________")
              if ps_cr=="before amount":
                                    
                                    pdf.drawString(28,x-13,"")
                              
                                    pdf.drawString(100,x-13,"")
                                    pdf.drawString(168,x-13,"")
                                    pdf.drawString(250,x-13,"-Summary-")
                                    pdf.drawString(315,x-13,"") 
                                    pdf.drawString(380,x-13,str(crc)+str(inv_ttt[0]))
                                    pdf.drawString(460,x-13,str(crc)+str(inv_ttt[1]))
                                    pdf.drawString(522,x-13,str(crc)+str(inv_ttt[2]))
              elif ps_cr=="after amount":
                                  
                                    pdf.drawString(28,x-13,"")
                                    pdf.drawString(100,x-13,"")
                                    pdf.drawString(168,x-13,"-Summary-")
                                    pdf.drawString(250,x-13,"")
                                    pdf.drawString(315,x-13,"") 
                                    pdf.drawString(380,x-13,str(inv_ttt[0])+str(crc))
                                    pdf.drawString(460,x-13,str(inv_ttt[1])+str(crc))
                                    pdf.drawString(522,x-13,str(inv_ttt[2])+str(crc))
              elif ps_cr=="before amount with space":
                                    pdf.drawString(28,x-13,"")
                              
                                    pdf.drawString(100,x-13,"")
                                    pdf.drawString(168,x-13,"-Summary-")
                                    pdf.drawString(250,x-13,"")
                                    pdf.drawString(315,x-13,"") 
                                    pdf.drawString(380,x-13,str(crc)+" "+str(inv_ttt[0]))
                                    pdf.drawString(460,x-13,str(crc)+" "+str(inv_ttt[1]))
                                    pdf.drawString(522,x-13,str(crc)+" "+str(inv_ttt[2]))
              elif ps_cr=="after amount with space":
                                    pdf.drawString(28,x-13,"")
                                    pdf.drawString(100,x-13,"")
                                    pdf.drawString(168,x-13,"-Summary-")
                                    pdf.drawString(250,x-13,"")
                                    pdf.drawString(315,x-13,"") 
                                    pdf.drawString(380,x-13,str(inv_ttt[0])+" "+str(crc))
                                    pdf.drawString(460,x-13,str(inv_ttt[1])+" "+str(crc))
                                    pdf.drawString(522,x-13,str(inv_ttt[2])+" "+str(crc))
              else:
                              pass


              pdf.save()
              # win32api.ShellExecute(0,"","customer_Reports\Recurring_Invoice_Report.pdf",None,".",0)
          except:
            pass

          cus_lstfrm=StringVar()  
          cus_htcodeframe=Listbox(cus_attachlbframe, height=13, width=43,listvariable=cus_lstfrm, bg="white")
          global cus_filenamezrrr
          cus_filenamezrrr ="customer_Reports\CInvoice.pdf"
          wraped_text="/".join(wrap(cus_filenamezrrr,17))
          hrt=wraped_text.split('/')
          cus_htcodeframe.insert(0,hrt[1])

          cus_htcodeframe.place(x=5, y=5)
          cus_htcodeframe.bind('<Double-Button-1>' , cus_file)

          def cus_deslist():
              cus_laa=cus_htcodeframe.curselection()
              print("hloo",cus_htcodeframe.get(cus_laa))
              cus_yawn=cus_htcodeframe.get(cus_laa)        
              cus_htcodeframe.delete(ACTIVE)

          cus_lbl_btn_info=Label(cus_attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
          cus_btn17=Button(cus_attachlbframe, width=20, text="Add attachment file...", command=cus_UploadAction).place(x=60, y=260)
          cus_btn18=Button(cus_attachlbframe, width=20, text="Remove attachment",command=cus_deslist).place(x=60, y=295)
          cus_lbl_tt_info=Label(cus_email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
          cus_lbl_tt_info.place(x=740, y=370)

          cus_ready_frame=Frame(cus_mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
          
          cus_sendatalbframe=LabelFrame(cus_account_Frame,text="E-Mail(Sender data)",height=140, width=600)
          cus_sendatalbframe.place(x=240, y=165 )
          cus_lbl_sendermail=Label(cus_sendatalbframe, text="Company email address").place(x=5, y=10)
          cus_sentent=Entry(cus_sendatalbframe, width=40, textvariable=cus_email_from)
          cus_sentent.place(x=195, y=10)

          cus_lbl_sendecusswrd=Label(cus_sendatalbframe, text="Email Password").place(x=5, y=40)
          cus_pswrdent=Entry(cus_sendatalbframe, width=40, textvariable=cus_email_pswrd,show="*")
          cus_pswrdent.place(x=195, y=40)


#-----------------------------------------------------------------------------------Preview Invoice Customer
def cus_previewinvoice_customer():
  cus_in_preview = Toplevel()
  cus_in_preview.title("F-Billing Revolution Invoice Report ")
  cus_in_p2= PhotoImage(file = "images/fbicon.png")
  cus_in_preview.iconphoto(False, cus_in_p2)
  cus_in_preview.geometry("1800x1800+0+0")
  cus_in_frame = Frame(cus_in_preview,width=1500,height=1800,bg="red")
  cus_in_frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
  cus_in_frame.place(x=0,y=30)
  cus_in_canvas=Canvas(cus_in_frame,bg='grey',width=1400,height=1200,scrollregion=(0,0,1500, 1200))


  cus_in_vertibar=Scrollbar(cus_in_frame,orient=VERTICAL)
  cus_in_vertibar.pack(side=RIGHT,fill=Y)
  cus_in_vertibar.config(command=cus_in_canvas.yview)
  cus_in_canvas.config(width=1338,height=710)

  cus_in_canvas.config(yscrollcommand=cus_in_vertibar.set)
  cus_in_canvas.pack(expand=True,side=LEFT,fill=BOTH)
  # canvas.create_rectangle(235,10,1025,1430,  outline='yellow',fill='White')
  # canvas = Canvas(preview)
  # canvas.place(relwidth=1, relheight=1,x=250,y=10) 
  cus_in_paperheigth = cus_in_preview.winfo_fpixels('1m') * 297
  cus_in_paperwidth = cus_in_preview.winfo_fpixels('1m') * 210
  cus_in_canvas.create_rectangle(265, 20, 265+cus_in_paperwidth, 20+cus_in_paperheigth, outline='orange', fill='white')
  cus_company = "SELECT * from company"
  fbcursor.execute(cus_company)
  cus_company= fbcursor.fetchone()

  try:
    cus_id=cus_main_tree.item(cus_main_tree.focus())["values"][3]

    cus_main_table_sql="select * from orders where businessname=%s"
    cus_main_table_sql_val=(cus_id,)
    fbcursor.execute(cus_main_table_sql,cus_main_table_sql_val)
    main_tb_val=fbcursor.fetchone()

    sqlr= 'select currencysign from company'
    fbcursor.execute(sqlr)
    crncy=fbcursor.fetchone()
    crc=crncy[0]
    sqlrt= 'select currsignplace from company'
    fbcursor.execute(sqlrt)
    post_rp=fbcursor.fetchone()
    ps_cr=post_rp[0]
    
    #-------------------------------------------------------------------------------------------------Heder data--------
    labelcmp=Label(cus_in_canvas,text=cus_company[1], bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=2)
    window = cus_in_canvas.create_window(300,80, anchor="nw", window=labelcmp)

    labelcmpl=Label(cus_in_canvas,text=cus_company[2], bg="white",font=("Helvetica", 9),anchor="nw", width=50,justify=LEFT, height=6)
    windowl = cus_in_canvas.create_window(300,120, anchor="nw", window=labelcmpl)
    cus_in_canvas.create_text(950,100, text="Invoices List",font=("Helvetica", 16), justify='right')
    cus_in_canvas.create_text(350,228,text=cus_company[4],fill='black',font=("Helvetica", 8), justify='left')
    cus_in_canvas.create_text(953,220,text="Customer ID:"+str(main_tb_val[0]),fill='black',font=("Helvetica", 12), justify='right')

    cus_sql5="select * from customer where businessname=%s"
    cus_sql5_vals=(cus_id,)
    fbcursor.execute(cus_sql5,cus_sql5_vals)
    cus_det=fbcursor.fetchone()
    cus_in_canvas.create_line(1038,235,280,235,fill="black", width=2)
    
    cus_in_canvas.create_text(330,260,text="Bill To:",fill='black',font=("Helvetica", 12), justify='right')
    labelcmp=Label(cus_in_canvas,text=cus_det[4] , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=1)
    window = cus_in_canvas.create_window(305,275, anchor="nw", window=labelcmp)
    text=cus_det[5]
    wraped_text="\n".join(wrap(text,30))
    labelcmp=Label(cus_in_canvas,text=wraped_text , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=4)
    window = cus_in_canvas.create_window(305,295, anchor="nw", window=labelcmp)

    cus_in_canvas.create_text(720,260,text="Ship To:",fill='black',font=("Helvetica", 12), justify='right')
    labelcmp=Label(cus_in_canvas,text=cus_det[6] , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=1)
    window = cus_in_canvas.create_window(690,275, anchor="nw", window=labelcmp)
    text=cus_det[7]
    wraped_text="\n".join(wrap(text,30))
    labelcmp=Label(cus_in_canvas,text=wraped_text , bg="white",anchor="nw",font=("Helvetica", 10), width=40, height=4)
    window = cus_in_canvas.create_window(690,295, anchor="nw", window=labelcmp)
    #---------------------------------------------------------------------------------------------------Table Data

    style=ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13), background='white') # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    # Add a Treeview widge
                        
    cus_prv_tree=ttk.Treeview(cus_in_canvas, column=("c1", "c2","c3", "c4", "c5", "c6", "c7","c8"), show='headings', height=30, style='mystyle.Treeview')
    cus_prv_tree.column("# 1", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 1", text="Invoice No")
    cus_prv_tree.column("# 2", anchor=E, stretch=NO, width=80)
    cus_prv_tree.heading("# 2", text="Date")
    cus_prv_tree.column("# 3", anchor=E, stretch=NO, width=80)
    cus_prv_tree.heading("# 3", text="Due Date")
    cus_prv_tree.column("# 4", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 4", text="Recurring")
    cus_prv_tree.column("# 5", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 5", text="Status")
    cus_prv_tree.column("# 6", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 6", text="Invoice Total")
    cus_prv_tree.column("# 7", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 7", text="Total Paid")
    cus_prv_tree.column("# 8", anchor=E, stretch=NO, width=100)
    cus_prv_tree.heading("# 8", text="Balance")

    sql_qry="select * from invoice where businessname=%s"
    sql_qryvlz=(cus_id,)
    fbcursor.execute(sql_qry,sql_qryvlz)
    tre=fbcursor.fetchall() 
    for record in cus_prv_tree.get_children():
      cus_prv_tree.delete(record)
        

    count=0
    for i in tre:
      if i[24] is None:
        dfh="No"
      else:
        dfh="Yes"
      if ps_cr=="before amount":
        cus_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], crc+str(i[8]), crc+str(i[9]), crc+str(i[10])))
                      
      elif ps_cr=="after amount":
        cus_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], str(i[8])+crc, str(i[9])+crc,str(i[10])+crc))
                        
      elif ps_cr=="before amount with space":
        cus_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5], crc+" "+str(i[8]), crc+" "+str(i[9]), crc+" "+str(i[10])))
                        
      elif ps_cr=="after amount with space":
        cus_prv_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[1], i[2], i[3],dfh,i[5],  str(i[8])+" "+crc, str(i[9])+" "+crc,str(i[10])+" "+crc))
                        
                    
      else:
        pass
      count += 1
    cus_prv_tree.insert('', 'end',text="1",values=('','','','','','','',''))
    cus_prv_tree.insert('', 'end',text="1",values=('','','-End List-','','','Invoice Total','Total Paid','Balance'))
    sql_inv_t="select sum(invoicetot),sum(totpaid), sum(balance) from invoice where businessname=%s"
    sql_inv_t_val=(cus_id,)
    fbcursor.execute(sql_inv_t,sql_inv_t_val)
    inv_ttt=fbcursor.fetchone() 
    
    if ps_cr=="before amount":
      cus_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',crc+str(inv_ttt[0]),crc+str(inv_ttt[1]),crc+str(inv_ttt[2])))
    elif ps_cr=="after amount":
      cus_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',str(inv_ttt[0])+crc,str(inv_ttt[1])+crc,str(inv_ttt[2])+crc))
    elif ps_cr=="before amount with space":
      cus_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',crc+" "+str(inv_ttt[0]),crc+" "+str(inv_ttt[1]),crc+" "+str(inv_ttt[2])))
    elif ps_cr=="after amount with space":
      cus_prv_tree.insert('', 'end',text="1",values=('-Summary-','','','','',str(inv_ttt[0])+" "+crc,str(inv_ttt[1])+" "+crc,str(inv_ttt[2])+" "+crc))
    else:
      pass
    


    window = cus_in_canvas.create_window(280, 320, anchor="nw", window=cus_prv_tree)
  except:
    pass

              
#-----------------------------------------------------------------------------------print Invoice Customer
def cus_printinvoice_customer():
    from reportlab.pdfgen import canvas
        # from tkdocviewer import *
    from reportlab.lib import colors
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    from reportlab.lib.pagesizes import letter, inch
    try:
        pdf = canvas.Canvas("customer_Reports/CInvoice.pdf", pagesize=letter)
        cus_id=cus_main_tree.item(cus_main_tree.focus())["values"][3]
        sqlt= 'select * from customer where businessname=%s'
        sqlt_val=(cus_id,)
        fbcursor.execute(sqlt,sqlt_val)
        cus_ft=fbcursor.fetchone()

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
        pdf.drawString(35,700, "Sales tax reg No:"+company[4])
        pdf.drawString(490,760, "Invoice Report")

        pdf.drawString(460,700,"Customer ID:"+str(cus_ft[0]))
        pdf.drawString(28,695,"__________________________________________________________________________________")
        pdf.drawString(31,680,"Bill To:")
        pdf.drawString(31,668,cus_ft[4])
        text=cus_ft[5]
        wraped_text="\n".join(wrap(text,30))
        htg=wraped_text.split('\n')
            
        vg=len(htg)
        if vg>0:
                pdf.drawString(30,654,htg[0])
                print("1")
                if vg>1:
                  pdf.drawString(30,640,htg[1])
                  print("2")
                  if vg>2:
                      pdf.drawString(30,626,htg[2])
                      print("3")
                      if vg>3:
                          pdf.drawString(30,612,htg[3])
                          print("4")
                      else:
                          pass
                  else:
                      pass
                else:
                    pass
                
        else:
                pass

        pdf.drawString(400,680,"Ship To:")
        pdf.drawString(400,668,cus_ft[6])
        text=cus_ft[7]
        wraped_text="\n".join(wrap(text,30))
        htg=wraped_text.split('\n')
            
        vg=len(htg)
        if vg>0:
                pdf.drawString(400,654,htg[0])
                print("1")
                if vg>1:
                  pdf.drawString(400,640,htg[1])
                  print("2")
                  if vg>2:
                      pdf.drawString(400,626,htg[2])
                      print("3")
                      if vg>3:
                          pdf.drawString(400,612,htg[3])
                          print("4")
                      else:
                          pass
                  else:
                      pass
                else:
                    pass
                
        else:
                pass

        pdf.drawString(28,606,"__________________________________________________________________________________")


        pdf.drawString(28,591,"__________________________________________________________________________________")
        pdf.drawString(28,591,"Invoice No           Date        Due Date     Recurring      Status        Invoice Total    Total Paid   Balance      ")
        
        
        sqlr= 'select currencysign from company'
        fbcursor.execute(sqlr)
        crncy=fbcursor.fetchone()
          
        crc=crncy[0]
        sqlrt= 'select currsignplace from company'
        fbcursor.execute(sqlrt)
        post_rp=fbcursor.fetchone()
        ps_cr=post_rp[0]
        count=0
        sql_inv_dt='SELECT * FROM invoice where businessname=%s'
        inv_valuz=(cus_id,)
        fbcursor.execute(sql_inv_dt,inv_valuz)
        tre=fbcursor.fetchall()
        x=571

        for i in tre:
                      if x==38 or x==50:
                          pdf.showPage()
                          x=750
                      else:
                          if i[24] is None:
                              dfh="No"
                          else:
                              dfh="Yes"
                          if ps_cr=="before amount":
                              pdf.drawString(28,x,str(i[1]))
                        
                              pdf.drawString(100,x,str(i[2]))
                              pdf.drawString(168,x,str(i[3]))
                              pdf.drawString(250,x,dfh)
                              pdf.drawString(315,x,str(i[5])) 
                              pdf.drawString(380,x,str(crc)+str(i[8]))
                              pdf.drawString(460,x,str(crc)+str(i[9]))
                              pdf.drawString(522,x,str(crc)+str(i[10]))
                              
                          elif ps_cr=="after amount":
                              pdf.drawString(28,x,str(i[1]))
                              pdf.drawString(100,x,str(i[2]))
                              pdf.drawString(168,x,str(i[3]))
                              pdf.drawString(250,x,str(dfh))
                              pdf.drawString(315,x,str(i[5])) 
                              pdf.drawString(380,x,str(i[8])+str(crc))
                              pdf.drawString(460,x,str(i[9])+str(crc))
                              pdf.drawString(522,x,str(i[10])+str(crc))
                              
                          elif ps_cr=="before amount with space":
                              pdf.drawString(28,x,str(i[1]))
                        
                              pdf.drawString(100,x,str(i[2]))
                              pdf.drawString(168,x,str(i[3]))
                              pdf.drawString(250,x,str(dfh))
                              pdf.drawString(315,x,str(i[5])) 
                              pdf.drawString(380,x,str(crc)+" "+str(i[8]))
                              pdf.drawString(460,x,str(crc)+" "+str(i[9]))
                              pdf.drawString(522,x,str(crc)+" "+str(i[10]))
                              
                              
                          elif ps_cr=="after amount with space":
                              pdf.drawString(28,x,str(i[1]))
                              pdf.drawString(100,x,str(i[2]))
                              pdf.drawString(168,x,str(i[3]))
                              pdf.drawString(250,x,str(dfh))
                              pdf.drawString(315,x,str(i[5])) 
                              pdf.drawString(380,x,str(i[8])+" "+str(crc))
                              pdf.drawString(460,x,str(i[9])+" "+str(crc))
                              pdf.drawString(522,x,str(i[10])+" "+str(crc))
                          
                          else:
                              pass
                        
                      count += 1
                    
                      x-=15
        sql_inv_t="select sum(invoicetot),sum(totpaid), sum(balance) from invoice where businessname=%s"
        sql_inv_t_val=(cus_id,)
        fbcursor.execute(sql_inv_t,sql_inv_t_val)
        inv_ttt=fbcursor.fetchone() 
        pdf.drawString(28,x,"__________________________________________________________________________________")
        if ps_cr=="before amount":
                              
                              pdf.drawString(28,x-13,"")
                        
                              pdf.drawString(100,x-13,"")
                              pdf.drawString(168,x-13,"")
                              pdf.drawString(250,x-13,"-Summary-")
                              pdf.drawString(315,x-13,"") 
                              pdf.drawString(380,x-13,str(crc)+str(inv_ttt[0]))
                              pdf.drawString(460,x-13,str(crc)+str(inv_ttt[1]))
                              pdf.drawString(522,x-13,str(crc)+str(inv_ttt[2]))
        elif ps_cr=="after amount":
                            
                              pdf.drawString(28,x-13,"")
                              pdf.drawString(100,x-13,"")
                              pdf.drawString(168,x-13,"-Summary-")
                              pdf.drawString(250,x-13,"")
                              pdf.drawString(315,x-13,"") 
                              pdf.drawString(380,x-13,str(inv_ttt[0])+str(crc))
                              pdf.drawString(460,x-13,str(inv_ttt[1])+str(crc))
                              pdf.drawString(522,x-13,str(inv_ttt[2])+str(crc))
        elif ps_cr=="before amount with space":
                              pdf.drawString(28,x-13,"")
                        
                              pdf.drawString(100,x-13,"")
                              pdf.drawString(168,x-13,"-Summary-")
                              pdf.drawString(250,x-13,"")
                              pdf.drawString(315,x-13,"") 
                              pdf.drawString(380,x-13,str(crc)+" "+str(inv_ttt[0]))
                              pdf.drawString(460,x-13,str(crc)+" "+str(inv_ttt[1]))
                              pdf.drawString(522,x-13,str(crc)+" "+str(inv_ttt[2]))
        elif ps_cr=="after amount with space":
                              pdf.drawString(28,x-13,"")
                              pdf.drawString(100,x-13,"")
                              pdf.drawString(168,x-13,"-Summary-")
                              pdf.drawString(250,x-13,"")
                              pdf.drawString(315,x-13,"") 
                              pdf.drawString(380,x-13,str(inv_ttt[0])+" "+str(crc))
                              pdf.drawString(460,x-13,str(inv_ttt[1])+" "+str(crc))
                              pdf.drawString(522,x-13,str(inv_ttt[2])+" "+str(crc))
        else:
                        pass


        pdf.save()
        win32api.ShellExecute(0,"","customer_Reports\CInvoice.pdf",None,".",0)
    except:
      pass


#-----------------------------------------------------------------------------------Refresh
def cus_refresh_customers(): 
      for record in cus_main_tree.get_children():
        cus_main_tree.delete(record)
      cus_main_table_sql="select * from customer"
      fbcursor.execute(cus_main_table_sql)
      main_tb_val=fbcursor.fetchall()
      count_cus=0

      for i in main_tb_val:
        cus_main_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=("",i[24],i[2],i[4],i[8],i[10],i[12],i[22]))
        count_cus +=1

#----------------------------------------------------------------------------------------------bottom Button
rir_btn=Button(tab4, text="Invoice Items(0)",image=invoices,compound = LEFT, width=130, command="lambda:cus_inv_btm1()")
rir_btn.place(x=7, y=430)
rir_btn=Button(tab4, text="Invoice Private Notes", image=orders,compound = LEFT, width=130, command="lambda:cus_ord_btm()")
rir_btn.place(x=150, y=430)
rir_btn=Button(tab4, text="SMS Log", image=estimates,compound = LEFT, width=130, command="lambda:cus_est_btm()")
rir_btn.place(x=295, y=430)
rir_btn=Button(tab4, text="Document(0)", image=invoices,compound = LEFT, width=130, command="lambda:cus_stm_btm()")
rir_btn.place(x=440, y=430)

cus_pn = Canvas(tab4, width=1370, height=230, bg="#f8f8f2", bd=0)
cus_pn.pack(side="top",pady=(32,0))

global cus_main_tree
cus_main_s=ttk.Style()
cus_main_s.configure('Treeview.Heading',background='white')
cus_main_tree=ttk.Treeview(tab4,selectmode='browse')

cus_main_vertical_bar=ttk.Scrollbar(tab4,orient="vertical")
cus_main_vertical_bar.config(command=cus_main_tree.yview)
cus_main_vertical_bar.place(x=1343,y=95,height=330)
cus_main_tree.place(x=0,y=95,height=330)
cus_main_tree["columns"]=("1","2","3","4","5","6","7")
cus_main_tree["show"]='headings'
cus_main_tree.column("1",width=30,anchor='c')
cus_main_tree.column("2",width=200,anchor='c')
cus_main_tree.column("3",width=190,anchor='c')
cus_main_tree.column("4",width=176,anchor='c')
cus_main_tree.column("5",width=196,anchor='c')
cus_main_tree.column("6",width=400,anchor='c')
cus_main_tree.column("7",width=150,anchor='c')

cus_main_tree.heading("1",text="")
cus_main_tree.heading("2",text="Invoice#")
cus_main_tree.heading("3",text="Next Invoice")
cus_main_tree.heading("4",text="Recurring Period")
cus_main_tree.heading("5",text="Stop After")
cus_main_tree.heading("6",text="Customer Name")
cus_main_tree.heading("7",text="Invoice Total")

#---------------------------------------------------------------------------------------------Bottom Table:
cus_inv_s=ttk.Style()
cus_inv_s.configure('Treeview.Heading',background='white')
cus_inv_tree=ttk.Treeview(tab4,selectmode='browse')
cus_inv_tree.place(x=0,y=455,height=230)
cus_inv_vertical_bar=ttk.Scrollbar(tab4,orient="vertical")
cus_inv_vertical_bar.config(command=cus_inv_tree.yview)
cus_inv_vertical_bar.place(x=1343,y=455,height=230)
cus_inv_tree["columns"]=("1","2","3","4","5","6","7","8","9")
cus_inv_tree["show"]='headings'

sql_rir_qry='select * from company'
fbcursor.execute(sql_rir_qry) 
tax_des=fbcursor.fetchone()
if tax_des[12]=='3':
  cus_inv_tree.column("1",width=20,anchor='c')
  cus_inv_tree.column("2",width=160,anchor='c')
  cus_inv_tree.column("3",width=300,anchor='c')
  cus_inv_tree.column("4",width=150,anchor='c')
  cus_inv_tree.column("5",width=150,anchor='c')
  cus_inv_tree.column("6",width=120,anchor='c')
  cus_inv_tree.column("7",width=150,anchor='c')
  cus_inv_tree.column("8",width=150,anchor='c')
  cus_inv_tree.column("9",width=140,anchor='c')
  cus_inv_tree.heading("1",text="")
  cus_inv_tree.heading("2",text="Product/Service ID")
  cus_inv_tree.heading("3",text="Name")
  cus_inv_tree.heading("4",text="Description")
  cus_inv_tree.heading("5",text="Price")
  cus_inv_tree.heading("6",text="QTY")
  cus_inv_tree.heading("7",text="Tax1")
  cus_inv_tree.heading("8",text="Tax2")
  cus_inv_tree.heading("9",text="Line Total")
elif tax_des[12]=='2':
  cus_inv_s=ttk.Style()
  cus_inv_s.configure('Treeview.Heading',background='white')
  cus_inv_tree=ttk.Treeview(tab4,selectmode='browse')
  cus_inv_tree.place(x=0,y=455,height=230)
  cus_inv_tree["columns"]=("1","2","3","4","5","6","7","8")
  cus_inv_tree["show"]='headings'
  cus_inv_vertical_bar=ttk.Scrollbar(tab4,orient="vertical")
  cus_inv_vertical_bar.config(command=cus_inv_tree.yview)
  cus_inv_vertical_bar.place(x=1343,y=455,height=230)
  cus_inv_tree.column("1",width=20,anchor='c')
  cus_inv_tree.column("2",width=160,anchor='c')
  cus_inv_tree.column("3",width=300,anchor='c')
  cus_inv_tree.column("4",width=210,anchor='c')
  cus_inv_tree.column("5",width=150,anchor='c')
  cus_inv_tree.column("6",width=150,anchor='c')
  cus_inv_tree.column("7",width=150,anchor='c')
  cus_inv_tree.column("8",width=200,anchor='c')

  cus_inv_tree.heading("1",text="")
  cus_inv_tree.heading("2",text="Product/Service ID")
  cus_inv_tree.heading("3",text="Name")
  cus_inv_tree.heading("4",text="Description")
  cus_inv_tree.heading("5",text="Price")
  cus_inv_tree.heading("6",text="QTY")
  cus_inv_tree.heading("7",text="Tax1")
 
  cus_inv_tree.heading("8",text="Line Total")
else:
  cus_inv_s=ttk.Style()
  cus_inv_s.configure('Treeview.Heading',background='white')
  cus_inv_tree=ttk.Treeview(tab4,selectmode='browse')
  cus_inv_tree.place(x=0,y=455,height=230)
  cus_inv_tree["columns"]=("1","2","3","4","5","6","7")
  cus_inv_tree["show"]='headings'
  cus_inv_vertical_bar=ttk.Scrollbar(tab4,orient="vertical")
  cus_inv_vertical_bar.config(command=cus_inv_tree.yview)
  cus_inv_vertical_bar.place(x=1343,y=455,height=230)
  cus_inv_tree.column("1",width=20,anchor='c')
  cus_inv_tree.column("2",width=230,anchor='c')
  cus_inv_tree.column("3",width=300,anchor='c')
  cus_inv_tree.column("4",width=200,anchor='c')
  cus_inv_tree.column("5",width=200,anchor='c')
  cus_inv_tree.column("6",width=200,anchor='c')
  cus_inv_tree.column("7",width=190,anchor='c')
  cus_inv_tree.heading("1",text="")
  cus_inv_tree.heading("2",text="Product/Service ID")
  cus_inv_tree.heading("3",text="Name")
  cus_inv_tree.heading("4",text="Description")
  cus_inv_tree.heading("5",text="Price")
  cus_inv_tree.heading("6",text="QTY")
  cus_inv_tree.heading("7",text="Line Total")


root.mainloop()