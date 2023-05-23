# Function: Calculate differential between start date and end date
# Company: Formosa Chemistry
# Developer: Cheng Kai, Cheng
# Develop date: 2023-05-19
# Change date: 2023-05-19
# Description: Calculate differential between start date and end date
 


from datetime import datetime

def calculate_period(start_datetime, end_datetime, period_minutes, period_days):
    date_format_str = '%Y-%m-%d %H:%M:%S'
    fmt_start_datetime = datetime.strptime(start_datetime, date_format_str)
    fmt_end_datetime = datetime.strptime(end_datetime, date_format_str)
    final_time = fmt_end_datetime - fmt_start_datetime 
    period_days = final_time.days
    period_minutes = final_time.days * 24 * 60

    return period_days, period_minutes