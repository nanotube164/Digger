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

# from tkinter import tk
# Function: Operation in PI system
# Company: Formosa Chemistry
# Developer: Cheng Kai, Cheng
# Develop date: 2023-05-19
# Change date: 2023-05-19
# Description: Operation in PI system

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
root.title('Pi System Catcher.exe')
# Set geometry
root.geometry("600x330")
header = Label(
        root,
        text= '\n' +'Pi System Catcher' + '\n',
        width=600,
        justify=LEFT,
        bg='green')
header.pack()

dev_info = Label(
        root,
        text='Business Unit: Formosa Chemistry' + '\n'+ 'Developer: Cheng Kai, Cheng' + '\n' 'Dev. date: 2023-05-20',
        width=600,
        justify=LEFT,
        bg='white')
dev_info.pack()

start_label = Label(root,text =  '\n' + 'Start date:')
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

end_label = Label(root,text = 'End date:')
end_label.pack()

# Add Calendar
pick_end_datetime = DateEntry(root, selectmode = 'day',
               year = 2023, month = 5,
               day = 22,date_pattern='yyyy-MM-dd')

pick_end_datetime.pack()

# Add Button and Label
Button(root, text = "Execution",
       command = exec).pack(pady = 20)
 
date = Label(root, text = "")
date.pack()


footer = Label(
        root,
        text=  '\n'+'Copyright: Formosa Chemistry Since 2023' + '\n' ,
        width=600,
        justify=LEFT,
        bg='green')
footer.pack()

# Execute Tkinter
root.mainloop()