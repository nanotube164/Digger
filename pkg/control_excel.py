# Function: Control excel
# Company: Formosa Chemistry
# Developer: Cheng Kai, Cheng
# Develop date: 2023-05-19
# Change date: 2023-05-19
# Description: Control excel

from pkg.parameter.english_code import english_code
from datetime import datetime, timedelta
from pkg.control_pi import PISystemCRUD


def fill_in_excel_with_tag_value(tagname, excel_column, start_datetime, end_datetime, period_minutes, sheet):
    PISystemCRUD.connect_to_Server('ldrtpmsPI')
    # 蒐集錶點 LT3-DCS-FQ3K1108.PV，日期區間從 2023-05-10 00:00:00 到 2023-05-11 00:00:00
    doSmokeArray = PISystemCRUD.extract_tag_from_pi(tagname, start_datetime, end_datetime, [])
    # print(doSmokeArray)
    # 查詢 2023-05-10 03:41:00 是否有煙? 
    # print(PISystemCRUD.get_if_record('2023-05-10 03:42:00', 999, doSmokeArray))
    # 第二列開始記錄
    var_row = 2
    record_datetime = start_datetime
    date_format_str = '%Y-%m-%d %H:%M:%S'
    per_min_period = 1
    for period in range(period_minutes):
        first_varible = english_code[excel_column] + str(var_row)
        fmt_record_datetime = datetime.strptime(record_datetime, date_format_str)
        fmt_record_datetime_to_string = str(fmt_record_datetime)
        isRecorded = PISystemCRUD.get_if_record(fmt_record_datetime_to_string, 999, doSmokeArray)
        sheet[first_varible] = isRecorded
        record_datetime = str(fmt_record_datetime + timedelta(minutes=per_min_period))
        var_row = var_row + per_min_period
    

def fill_in_excel_with_parameter(start_datetime, period_minutes, sheet):
    # 變數值(第二列)
    var_row = 2
    record_datetime = start_datetime
    date_format_str = '%Y-%m-%d %H:%M:%S'
    per_min_period = 1
    # 紀錄起訖日期所有的分鐘數當標籤，作為第一個參數
    for period in range(int(period_minutes)):
        first_varible = english_code[0] + str(var_row)
        sheet[first_varible] = record_datetime
        fmt_record_datetime = datetime.strptime(record_datetime, date_format_str)
        record_datetime = str(fmt_record_datetime + timedelta(minutes=per_min_period))
        var_row = var_row + per_min_period


def fill_in_excel_with_stamp(mggh_parameter, sheet):
    # 變數名稱(第一列)
    para_first_row = "1"
    for para_column in range(1,len(mggh_parameter)+1):
        first_parameter = english_code[para_column] + para_first_row
        sheet[first_parameter] = mggh_parameter[para_column-1]