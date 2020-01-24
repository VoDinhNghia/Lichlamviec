import sqlite3
import os
import numpy as np
import pickle
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import xlwt
from datetime import datetime
from datetime import date

root = Tk()
root.geometry("1000x400")
img1=ImageTk.PhotoImage(Image.open('nen.jpg'))
panel = Label(root, image = img1)
panel.image = img1
panel.place(x = 0, y = 0)

def btn_thu2():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 2"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 2"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 2"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 2", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()

def btn_thu3():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 3"
    cursor = conn.execute(cmd)
    cvthu3=[]
    for row in cursor:
        row = row[0]
        cvthu3.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 3"
    cursor_ngay = conn.execute(cmd)
    ngaythu3=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu3.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 3"
    cursor_gio = conn.execute(cmd)
    giothu3=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu3.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 3", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu3[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu3[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu3[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu3[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu3[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu3[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu3[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu3[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu3[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()

def btn_thu4():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 4"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 4"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 4"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 4", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)
    
    conn.commit()
    conn.close()

def btn_thu5():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 5"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 5"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 5"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 5", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()   

def btn_thu6():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 6"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 6"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 6"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 6", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()

def btn_thu7():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 7"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 7"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 7"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc thứ 7", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()

def btn_chunhat():
    tk=Tk()
    tk.geometry("1000x500")
    conn = sqlite3.connect("LichCV.db")
    cmd = "SELECT Congviec FROM BangCV WHERE Thu == 8"
    cursor = conn.execute(cmd)
    cvthu2=[]
    for row in cursor:
        row = row[0]
        cvthu2.append(row)
    cmd = "SELECT Ngay FROM BangCV WHERE Thu == 8"
    cursor_ngay = conn.execute(cmd)
    ngaythu2=[]
    for row_ngay in cursor_ngay:
        row_ngay = row_ngay[0]
        ngaythu2.append(row_ngay)
    cmd = "SELECT Gio FROM BangCV WHERE Thu == 8"
    cursor_gio = conn.execute(cmd)
    giothu2=[]
    for row_gio in cursor_gio:
        row_gio = row_gio[0]
        giothu2.append(row_gio)
    
    lblt_t2 = Label(tk, text="Danh sách công việc chủ nhật", font=("Times New Roman", 18), fg='blue')
    lblt_t2.place(x=350, y=10)
    
    lbl2 = Label(tk, text="Công việc", font=("Times New Roman", 15), fg='red')
    lbl2.place(x=15, y=60)
    lbl2n = Label(tk, text="Ngày thực hiện", font=("Times New Roman", 15), fg='red')
    lbl2n.place(x=800, y=60)
    lbl2g = Label(tk, text="Giờ", font=("Times New Roman", 15), fg='red')
    lbl2g.place(x=700, y=60)

    lblt_t20 = Label(tk, text=cvthu2[0], font=("Times New Roman", 15), fg='blue')
    lblt_t20.place(x=15, y=90)
    lbltn_t20 = Label(tk, text=ngaythu2[0], font=("Times New Roman", 15), fg='blue')
    lbltn_t20.place(x=800, y=90)
    lbltg_t20 = Label(tk, text=giothu2[0], font=("Times New Roman", 15), fg='blue')
    lbltg_t20.place(x=700, y=90)

    lblt_t21 = Label(tk, text=cvthu2[1], font=("Times New Roman", 15), fg='blue')
    lblt_t21.place(x=15, y=120)
    lbltn_t21 = Label(tk, text=ngaythu2[1], font=("Times New Roman", 15), fg='blue')
    lbltn_t21.place(x=800, y=120)
    lbltg_t21 = Label(tk, text=giothu2[1], font=("Times New Roman", 15), fg='blue')
    lbltg_t21.place(x=700, y=120)

    lblt_t22 = Label(tk, text=cvthu2[2], font=("Times New Roman", 15), fg='blue')
    lblt_t22.place(x=15, y=150)
    lbltn_t22 = Label(tk, text=ngaythu2[2], font=("Times New Roman", 15), fg='blue')
    lbltn_t22.place(x=800, y=150)
    lbltg_t22 = Label(tk, text=giothu2[2], font=("Times New Roman", 15), fg='blue')
    lbltg_t22.place(x=700, y=150)

    conn.commit()
    conn.close()

def btn_themcongviec():
    tk = Tk()
    tk.geometry("600x280")
    def btn_themcv():
        thu = lbl_getthu.get()
        cv = lbl_getcv.get()
        ngay = lbl_getngay.get()
        gio = lbl_getgio.get()
        conn=sqlite3.connect("LichCV.db")
        cmd="INSERT INTO BangCV(Thu,Congviec,Ngay,Gio) Values("+str(thu)+","+str(cv)+","+str(ngay)+","+str(gio)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()
        messagebox.showinfo("Thông báo", "Thêm công việc thành công")

    lbl_thu = Label(tk,text="Thứ", font=("Time New Roman", 14), fg="green")
    lbl_thu.place(x=15, y=15)
    lbl_getthu = Entry(tk, width=35, font=("Time New Roman", 14))
    lbl_getthu.place(x=150, y=15)
    lbl_congviec = Label(tk,text="Công việc", font=("Time New Roman", 14), fg="green")
    lbl_congviec.place(x=15, y=65)
    lbl_getcv = Entry(tk, width=35, font=("Time New Roman", 14))
    lbl_getcv.place(x=150, y=65)
    lbl_ngay = Label(tk,text="Ngày", font=("Time New Roman", 14), fg="green")
    lbl_ngay.place(x=15, y=115)
    lbl_getngay = Entry(tk, width=35, font=("Time New Roman", 14))
    lbl_getngay.place(x=150, y=115)
    lbl_gio = Label(tk,text="Giờ", font=("Time New Roman", 14), fg="green")
    lbl_gio.place(x=15, y=165)
    lbl_getgio = Entry(tk, width=35, font=("Time New Roman", 14))
    lbl_getgio.place(x=150, y=165)
    btn_themcv = Button(tk, text="Thêm công việc", font=("Times New Roman", 14), fg="white", bg="green",
        width=12, height=1, command=btn_themcv)
    btn_themcv.place(x=250, y=220)

def btn_huongdan():
    print("haha")

def btn_dong():
    root.destroy()

btn_thu2 = Button(root, text="Thứ hai", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu2)
btn_thu2.place(x=15, y=70)
btn_thu3 = Button(root, text="Thứ ba", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu3)
btn_thu3.place(x=155, y=70)
btn_thu4 = Button(root, text="Thứ tư", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu4)
btn_thu4.place(x=295, y=70)
btn_thu5 = Button(root, text="Thứ năm", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu5)
btn_thu5.place(x=435, y=70)
btn_thu6 = Button(root, text="Thứ sáu", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu6)
btn_thu6.place(x=575, y=70)
btn_thu7 = Button(root, text="Thứ bảy", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_thu7)
btn_thu7.place(x=715, y=70)
btn_chunhat = Button(root, text="Chủ nhật", font=("Times New Roman", 14), fg="white", bg="green",
    width=12, height=1, command=btn_chunhat)
btn_chunhat.place(x=855, y=70)

btn_themcongviec = Button(root, text="Thêm công việc", font=("Times New Roman", 14), fg="white", bg="red",
    width=15, height=1, command=btn_themcongviec)
btn_themcongviec.place(x=800, y=200)
btn_dn = Button(root, text="Hướng dẫn", font=("Times New Roman", 14), fg="white", bg="red",
    width=15, height=1, command=btn_huongdan)
btn_dn.place(x=800, y=250)
btn1 = Button(root, text="Đóng", font=("Times New Roman", 14), fg="white", bg="red",
    width=15, height=1, command=btn_dong)
btn1.place(x=800, y=350)
lbl_title = Label(root, text= "LỊCH LÀM VIỆC THEO TUẦN", font=("Times New Roman", 20), fg="red")
lbl_title.place(x=350, y =10)

lbl_now = Label(root, text= "Công việc hôm nay", font=("Times New Roman", 21), fg="red")
lbl_now.place(x=150, y =250)
lbl_now1 = Label(root, text= " ", font=("Times New Roman", 14), fg="red")
lbl_now1.place(x=150, y =310)
lbl_now2 = Label(root, text= " ", font=("Times New Roman", 14), fg="red")
lbl_now2.place(x=150, y =350)

conn = sqlite3.connect("LichCV.db")
cmd = "SELECT * FROM BangCV"
cursor_cvhn = conn.execute(cmd)

cvhomnay=[]
for rowcv in cursor_cvhn:
    if(rowcv[2] == str(date.today())):
        rowcv=rowcv[1]
        cvhomnay.append(rowcv)

lbl_now2.configure(text =cvhomnay[0])
lbl_now1.configure(text =cvhomnay[1])
conn.commit()
conn.close()            

root.mainloop()