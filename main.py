import tkinter as tk
#from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
#import webbrowser
from tkinter import messagebox
#import string
#import random
import smtplib
from email.mime.text import MIMEText
from tkVideoPlayer import TkinterVideo
#from tkvideo import tkvideo
#import json
#import pandas as pd
#import numpy as np
#import oauth2client as oauth2client
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
from tkinter import filedialog
from PIL import Image
import pandas as pd
#import pytesseract


def model():

    df1 = pd.read_csv('./Server/Database/insurance.csv')
    df2 = pd.read_csv('./Server/Database/customer.csv')
    global features
    features = ['serum creatinine', 'glyco hb', 'culture and senstivity', 'aerobic urine routine',
                'tsh ultrasensitive thyroid', 'stimulating kub plain', 'ct uroflowmetry']
    global serum1, serum
    if df1['serum creatinine'][0] >= df2['serum creatinine'][0]:
        serum1 = True
        serum = df1['serum creatinine'][0]
    else:
        serum1 = False
        serum = 0

    global glyco1, glyco
    if df1['glyco hb'][0] >= df2['glyco hb'][0]:
        glyco1 = True
        glyco = df1['glyco hb'][0]
    else:
        glyco1 = False
        glyco = 0

    global culture1, culture
    if df1['culture and senstivity'][0] >= df2['culture and senstivity'][0]:
        culture1 = True
        culture = df1['culture and senstivity'][0]
    else:
        culture1 = False
        culture = 0

    global aerobic1, aerobic
    if df1['aerobic urine routine'][0] >= df2['aerobic urine routine'][0]:
        aerobic1 = True
        aerobic = df1['serum creatinine'][0]
    else:
        aerobic1 = False
        aerobic = 0

    global tsh1, tsh
    if df1['tsh ultrasensitive thyroid'][0] >= df2['tsh ultrasensitive thyroid'][0]:
        tsh1 = True
        tsh = df1['tsh ultrasensitive thyroid'][0]
    else:
        tsh1 = False
        tsh = 0

    global stimulating1, stimulating
    if df1['stimulating kub plain'][0] >= df2['stimulating kub plain'][0]:
        stimulating1 = True
        stimulating = df1['stimulating kub plain'][0]
    else:
        stimulating1 = False
        stimulating = 0

    global ct1, ct
    if df1['ct uroflowmetry'][0] >= df2['ct uroflowmetry'][0]:
        ct1 = True
        ct = df1['ct uroflowmetry'][0]
    else:
        ct1 = False
        ct = 0

    total = serum + glyco + culture + aerobic + tsh + stimulating + ct
    global claim
    claim = int(total)

    global list1
    list1 = [serum, glyco, culture, aerobic, tsh, stimulating, ct]
    count = -1
    global index
    for i in list1:
        count += 1
        if i == 0:
            index = count
    global not_covered_name
    global not_covered_value
    not_covered_name = features[index]
    not_covered_value = df2[not_covered_name][0]

    print(claim)
    print(not_covered_name)
    print(not_covered_value)
    print(pat_name)
    print(pat_email)

def generate_mail():
    #Delete the below line, dont forget it
    #pat_email = 'vashishthaharishankar@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
    server.login('dropmymail.otp@gmail.com','*******API_SECRET_KEY*******')
    global msg
    msg = 'Dear '+str(pat_name)+',\n\n' \
          'Welcome to ENIGMA,\n\n' \
          "We're thrilled to have you on board as a new user of ENIGMA.\n" \
            "Detailed break down of your claim is:\n\n" \
            "Amount claimed in serum creatinine is: " + str(list1[0]) + '\n' \
            "Amount claimed in glyco hb is: " + str(list1[1]) + '\n' \
            "Amount claimed in culture and senstivity is: " + str(list1[2]) + '\n' \
            "Amount claimed in aerobic urine routine is: " + str(list1[3]) + '\n' \
            "Amount claimed in tsh ultrasensitive thyroid is: " + str(list1[4]) + '\n' \
            "Amount claimed in stimulating kub plain is: " + str(list1[5]) + '\n' \
            "Amount claimed in ct uroflowmetry is: " + str(list1[6]) + '\n' \
            "We're confident that our application will provide you with a unique and enjoyable experience.\n\n" \
            "Category not covered in claim is : "+str(not_covered_name)+".\nThe Amount which you have to pay is "+str(not_covered_value)+'.\n' \
            "Amount which you can claim from insurer is "+str(claim)+'.\n' \
          'At ENIGMA, our goal is to help you to \n' \
          'broadcast your message/mail to your friend,colleague,team or group by hiding your identity. \n' \
          'Our platform is designed to make it easy and convenient for you to Drop Your Mail to your Target.\n\n' \
          'If you have any questions or need help getting started, our support team is always available to assist you.\n' \
          'You can reach us by email at: dropmymail.otp@gmail.com or through our website: www.vashishthahari.weebly.com\n\n' \
          '\n' \
          "We're looking forward to helping you achieve your goals with ENIGMA.\n" \
          '\n' \
          '\n' \
          '\n' \
          'Best regards,\n' \
          '\n' \
          'The ENIGMA Team,\n' \
          'Harishankar Vashishtha, Developer & Designer\n' \
          'Contact: www.vashishthahari.weebly.com\n' \
          'Email: dropmymail.otp@gmail.com\n' \
          '\n' \
          '\n' \
          'Follow us & spread the word:\n' \
          'Twitter: www.twitter.com/vashishthahari\n' \
          'Facebook: www.facebook.com/vashishthahari\n' \
          'Intagram: www.instagram.com/vashishthahari\n'

    msg1 = MIMEText(msg)
    sub_str = 'Revised Amount for Your Insurance Claim is '+ str(claim)
    msg1['Subject'] = sub_str
    server.sendmail('dropmymail.otp@gmail.com',str(pat_email),msg1.as_string())
    server.quit()
    #label5.destroy()
    messagebox.showinfo("Report",msg)

def loopVideo(event):
    videoplayer.play()
def pausevideo():
    videoplayer.pause()
def video():
    global videoplayer
    videoplayer = TkinterVideo(master=win1, scaled=True)
    videoplayer.load(r"./Server/Images/Squares.mp4")
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    videoplayer.bind('<<Ended>>', loopVideo)
    #win1.mainloop()
def destroyreport():
    label1.destroy()
    label3.destroy()
    label4.destroy()
def pass1():
    model()
    destroyreport()
    generate_mail()
    global label5
    # img5 = Image.open('./Server/Images/submit.png')
    # resize5 = img5.resize((220, 80))
    # img_5 = ImageTk.PhotoImage(resize5)
    # label5 = Button(win1, image=img_5, relief=FLAT, bg='#00FA9A', bd=0, activebackground='#00FA9A',command = generate_mail)
    # label5.place(x=535, y=350)
    win1.mainloop()


def destroyupload():
    upload_button.destroy()
    label21.destroy()
    label22.destroy()
    text1.destroy()
    text2.destroy()
def report():
    global label4
    img4 = Image.open('./Server/Images/report1.png')
    resize4 = img4.resize((220, 80))
    img_4 = ImageTk.PhotoImage(resize4)
    label4 = Button(win1, image=img_4, relief=FLAT, bg='#00FA9A', bd=0, activebackground='#00FA9A',command = pass1)
    label4.place(x=535, y=350)
    win1.mainloop()
def tick1():
    destroyupload()
    global label3
    img3 = Image.open('./Server/Images/tick1.png')
    resize3 = img3.resize((140, 140))
    img_3 = ImageTk.PhotoImage(resize3)
    label3 = Label(win1, image=img_3, relief=FLAT, bg='#00FA9A', bd=0, activebackground='#00FA9A')
    label3.place(x=570, y=180)
    report()
    win1.mainloop()
def upload_file():
    global pat_name
    global pat_email
    pat_name = str(text1.get())
    pat_email = str(text2.get())
    if len(pat_name) == 0 or len(pat_email) == 0:
        messagebox.showerror("Error!","Name and E-Mail is mandatory.")
    else:
        global file_path
        file_path = filedialog.askopenfilename()
        # Use the file_path as needed, such as printing it
        print("Selected File:", file_path)
        tick1()




def win1():
    global win1
    win1 = tk.Tk()
    win1.iconbitmap("./Server/Images/ww.ico")
    win1.title('DropMyMail')
    win1.geometry('1279x650')
    video()
    global label1
    img1 = Image.open('./Server/Images/bc.jpg')
    resize1 = img1.resize((100, 80))
    img_1 = ImageTk.PhotoImage(resize1)
    label1 = Label(win1, image=img_1, relief=FLAT, bg='#00FA9A', bd=0, activebackground='#00FA9A')
    label1.place(x=10, y=10)
    global upload_button
    img2 = Image.open('./Server/Images/upload1.png')
    resize2 = img2.resize((350, 100))
    img_2 = ImageTk.PhotoImage(resize2)

    global label21
    label21 = Label(win1, text='Name*', bg='#00FA9A')
    label21.config(font=('georgia', 15, 'bold'))
    label21.place(x=470, y=80)

    global label22
    label22 = Label(win1, text='E-Mail*', bg='#00FA9A')
    label22.config(font=('georgia', 15, 'bold'))
    label22.place(x=470, y=170)

    global text1
    text1 = tk.Entry(master=win1, width=25, relief=RIDGE, borderwidth=5)
    text1.config(font=('times new roman', 17))
    text1.place(x=470, y=122)
    text1.focus_set()
    global text2
    text2 = tk.Entry(master=win1, width=25, relief=RIDGE, borderwidth=5)
    text2.config(font=('times new roman', 17))
    text2.place(x=470, y=210)


    upload_button = tk.Button(win1, image=img_2, command=upload_file)
    upload_button.place(x=470,y=270)
    #tick1()


    win1.mainloop()
win1()
