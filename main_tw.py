from tkinter import *
from tkcalendar import Calendar
from datetime import datetime, timedelta
import time 
import openpyxl
from tkcalendar import DateEntry
from tkinter import ttk
import tkinter as tk
import openpyxl, time
from pkg.parameter.mggh_parameter import mggh_parameter
from pkg.parameter.tagnumber_pi import tagnumber_pi
from pkg.control_excel import fill_in_excel_with_tag_value, fill_in_excel_with_stamp, fill_in_excel_with_parameter
from pkg.calculate_time import calculate_period
from pkg.validation.validate_date import validate_date

from PIL import Image, ImageTk
import io
import webbrowser

lan_arr1_tw = [
    '繁體中文',
    '說明: Digger 是一個軟體，用來下載 PI 資料庫的資料到 Excel',
    '感謝你的支持!',
    '版權所有: 台化 2023',
    '開發者: 鄭丞凱',
    '開始日期',
    '終點日期',
    "版本 1.0.0",
    "下載"

]
lan_arr1_en = [
    'english',
    'Decription: Digger is a software, which is able to organize data from PI system.',
    'Thank your support!',
    "Copyright: Formosa Chemistry Since 2023",
    "Developed by: Nicholas, Cheng",
    "Start Date",
    "End Date",
    "Version 1.0.0",
    "Download"
]



# from tkinter import tk
# Function: Operation in PI system
# Company: Formosa Chemistry
# Developer: Cheng Kai, Cheng
# Develop date: 2023-05-19
# Change date: 2023-05-19
# Description: Operation in PI system


# Language
lan = lan_arr1_tw[0]
descrip = lan_arr1_tw[1]
thx = lan_arr1_tw[2]
Copyright = lan_arr1_tw[3]
developer = lan_arr1_tw[4]
stdate = lan_arr1_tw[5]       
eddate = lan_arr1_tw[6]
version = lan_arr1_tw[7]
download = lan_arr1_tw[8]


def open_url(event):
    webbrowser.open("https://nicholascheng.netlify.app/", new=0)

def exec():
        dt = str(datetime.today())
        today_format = dt[0:10] + dt[10:13] +" "+ dt[14:16] +" " + dt[17:19] + "_"
        excel_name = today_format + 'LT3_MGGH_merge.xlsx'

        sdate = str(pick_start_datetime.get_date())
        edate = str(pick_end_datetime.get_date())
        #--------------------------------------- 
        # Initialization
        #---------------------------------------
        sdate = sdate + " 00:00:00"
        edate = edate + " 00:00:00"
        start_datetime = sdate 
        end_datetime = edate
        period_minutes = 0
        period_days = 0

        # show(a, bar,val)
        #--------------------------------------- 
        # Main Procedure
        #---------------------------------------
        period_days, period_minutes = calculate_period(start_datetime, end_datetime, period_minutes, period_days)
        # Open excel
        workbook = openpyxl.Workbook()
        # Read excel file
        try:
            workbook = openpyxl.load_workbook(excel_name)
        except IOError:
            pass
        # Pick the first sheet
        sheet = workbook.worksheets[0]


        fill_in_excel_with_stamp(mggh_parameter,sheet)
        fill_in_excel_with_parameter(start_datetime,period_minutes, sheet)
        for item in range(len(tagnumber_pi)):
            fill_in_excel_with_tag_value(tagnumber_pi[item], item + 1, start_datetime, end_datetime, period_minutes, sheet)
            # time.sleep(1)
        try:
            workbook.save(excel_name)
            date.config( text="Download complete!", width=600)
        except IOError:
            print("Please close Excel and rerun this program!")


# Create Object
root = tk.Tk()
root.title('Digger.exe')
# Set geometry
root.geometry("600x410")
header = Label(
        root,
        text= version,
        width=600,
        justify=LEFT,
        bg='green')
header.pack()


G_gif = PhotoImage(file="logo.png")
label = Label(root, text="Digger", image = G_gif,width=600,height=100, bg='white', compound='left', font=("simsun", 40))
label.pack()

# descrip = lan_arr1_en[1]
# thx = lan_arr1_en[2]

dev_info = Label(
        root,
        text= descrip + "\n" + thx,
        width=600,
        justify=LEFT,
        bg='white')
dev_info.pack()

# lan = lan_arr1_tw[0]


start_label = Label(root,text =  '\n' + stdate)
start_label.pack()

# Add Calendar
# start_datetime = Calendar(root, selectmode = 'day',
#                year = 2020, month = 5,
#                day = 22,date_pattern='yyyy-MM-dd')
# start_datetime.pack()
pick_start_datetime = DateEntry(root, selectmode = 'day',
               year = 2023, month = 5,
               day = 22,date_pattern='yyyy-MM-dd')
pick_start_datetime.pack()

end_label = Label(root,text = eddate)
end_label.pack()

# Add Calendar
pick_end_datetime = DateEntry(root, selectmode = 'day',
               year = 2023, month = 5,
               day = 22,date_pattern='yyyy-MM-dd')

pick_end_datetime.pack()

# Add Button and Label
Button(root, text = download,
       command = exec).pack(pady = 20)
 
date = Label(root, text = "")
date.pack()

# Copyright = lan_arr1_en[3]

footer = Label(
        root,
        text=  '\n'+ Copyright ,
        width=600,
        justify=LEFT,
        bg='green')
footer.pack()

# developer = lan_arr1_en[4]

link = Label(root, text= developer + "\n",bg='green',width=600)
# link.place(x=540, y=430)

link.bind("<Button-1>",open_url)

link.pack()

# Execute Tkinter
root.mainloop()


# def resize(w,h, w_box, h_box, pil_image):
#     f1 = 1.0*w_box/W
#     f2 = 1.0*h_box/h
#     factor = min([f1,f2])

#     width = int(w*factor)
#     height = int(h*factor)
#     return pil_image.resize((width, height), Image.ANTIALTAS)


