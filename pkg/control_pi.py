import sys
import clr

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')
clr.AddReference('OSIsoft.AFSDK')
from OSIsoft.AF.PI import *
from OSIsoft.AF.UnitsOfMeasure import *
import datetime

from datetime import datetime

import pandas as pd
import numpy as np
from pandas import *
from OSIsoft.AF import *
from OSIsoft.AF.Search import *
from OSIsoft.AF.Asset import *
from OSIsoft.AF.Data import *
from OSIsoft.AF.Time import *


class PISystemCRUD(object):
    L = []
    # 功能: 初始化數據
    # 隸屬單位: 台化龍德廠
    # 開發者: 鄭丞凱
    # 開發日期: 2023-05-19
    # 變更日期: 2023-05-19
    # 功能說明: 初始化數據
    # def __init__:
    #     serverName = "ldrtpmsPI"
    #     tagname = "lt3_mggh_smoke3"
    #     initdate = "2023-05-10 00:00:00" 
    #     enddate = "2023-05-11 00:00:00"
    #     current_dateTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    # 功能: connect_to_Server
    # 隸屬單位: 台化龍德廠
    # 開發者: 鄭丞凱
    # 變更者: -----
    # 開發日期: 2023-05-19
    # 變更日期: -----
    # 功能說明: 連線伺服器
    # 參數: 
    #    1:伺服器(serverName)
    #    Ex: connect_to_Server('2023-05-10 20:34:00', 999)
    def connect_to_Server(serverName):
        piServers = PIServers()
        global piServer
        piServer = piServers[serverName]  # Write PI Server Name
        piServer.Connect(False)  # Connect to PI Server
        print('Connected to server: ' + serverName)


    # 功能: extract_tag_from_pi
    # 隸屬單位: 台化龍德廠
    # 開發者: 鄭丞凱
    # 變更者: -----
    # 開發日期: 2023-05-19
    # 變更日期: -----
    # 功能說明: 蒐集起訖時間內 tagname 的數據，
    # 參數: 
    #    1:伺服器(piServer)
    #    2:錶點(tagname)
    #    3:起始日期(initdate)
    #    4:結束日期(enddate)
    #    5:數據陣列(L)
    #    Ex: extract_tag_from_pi('lt3_smoke_''2023-05-10 20:34:00', 999)
    def extract_tag_from_pi(tagname, initdate, enddate, L):
        current_dateTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # points = PIPoint.FindPIPoints(piServer, None, None, None)
        tag = PIPoint.FindPIPoint(piServer, tagname)
        timerange = AFTimeRange(initdate, enddate)

        sampled = tag.RecordedValues(
            timerange, AFBoundaryType.Inside, "", False)
        for event in sampled:
            f = event.Timestamp.ToString("yyyy-MM-dd HH:mm:ss")
            t = tagname
            v = event.Value
            L.append([f, t, v])
        # print(L)
        return L
            # 整理成 pd 可視化格式
            # df = pd.DataFrame(L, columns=['Timestamp', 'Tag', 'Value'])
            # print(df)

    # 功能: get_if_record
    # 隸屬單位: 台化龍德廠
    # 開發者: 鄭丞凱
    # 變更者: -----
    # 開發日期: 2023-05-19
    # 變更日期: -----
    # 功能說明: 取得 lt3 smoke tag
    # 參數: 
    #    1:時間(period)
    #    2:註記是否有煙(value)，尚未傳值前為 999
    #    Ex: get_if_record('2023-05-10 20:34:00', 999)
    def get_if_record(period, value, L):
        for i in range(len(L)):
            if L[i][0][1:16] == period[1:16]:
                # print(L[i][2])
                value = L[i][2]
                return value

## 實用範例 2023-05-19
# from crud_pi_system_test import PISystemCRUD
# # 建立 PISystemCRUD 物件
# PISystemCRUD()
# # 連結伺服器
# PISystemCRUD.connect_to_Server('ldrtpmsPI')
# # 蒐集錶點 lt3_mggh_smoke3，日期區間從 2023-05-10 00:00:00 到 2023-05-11 00:00:00
# doSmokeArray = PISystemCRUD.extract_tag_from_pi('lt3_mggh_smoke3', '2023-05-10 00:00:00', '2023-05-11 00:00:00', [])
# # 查詢 2023-05-10 03:41:00 是否有煙? 
# print(PISystemCRUD.get_if_smoke('2023-05-10 03:41:00', 999, doSmokeArray))




#print(i.get_Name()) for i in points  # Print coincidences

# Select PI Server and Tag name
# tag = PIPoint.FindPIPoint(piServer, tagname)
# # Select Time Range (Osisoft PI format)
# timerange = AFTimeRange(initdate, enddate)
# # Get Recorded Values in Time Range
# recorded = tag.RecordedValues(
#     timerange, AFBoundaryType.Inside, "", False)
# record_dict = {}
# for event in recorded:
#     temp_datetime = event.Timestamp.LocalTime.ToString().replace("上午", "AM").replace("下午", "PM")
#     temp_datetime = datetime.datetime.strptime(temp_datetime, '%Y/%m/%d %p %I:%M:%S')
#     temp_datetime = temp_datetime.strftime("%Y/%m/%d %H:%M:%S'")
#     record_dict.update({temp_datetime: event.Value})
#     print('{0} value: {1}'.format(
#         event.Timestamp.LocalTime, event.Value))

# print(len(record_dict))


# tag = PIPoint.FindPIPoint(piServer, tagname)
# lastData = tag.Snapshot()  # Get Snapshot
# print ('Last Value in PI Tag ' + tagname + ' = ' + str(lastData))                   #Print Tag Value
# print(lastData.Value, lastData.Timestamp.ToString("yyyy-MM-dd HH:mm:ss"))