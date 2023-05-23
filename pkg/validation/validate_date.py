# Function: Validation for user's keyin
# Company: Formosa Chemistry
# Developer: Cheng Kai, Cheng
# Develop date: 2023-05-19
# Change date: 2023-05-19
# Description: Validation for user's keyin
#       Correct validation
#       valid == 1 : valid 
#       valid == 0 : invalid 

def validate_date(sdate, edate, valid):
    valid = 1

    if sdate[4] != "-" or sdate[7] != "-":
        valid = 0
    elif edate[4] != "-" or edate[7] != "-":
        valid = 0
    elif (isinstance(sdate[0:3], int) != True or isinstance(edate[0:3], int) != True or isinstance(sdate[5:6], int) != True or 
        isinstance(sdate[8:9], int) != True or isinstance(edate[5:6], int) != True or isinstance(sdate[8:9], int) != True):
        valid = 0
    elif sdate[0:3] != edate[0:3]:
        valid = 0
    elif (sdate[5:6] == edate[5:6] and sdate[8:9] > edate[8:9]):
        valid = 0
    elif sdate[5:6] > edate[5:6]:
        valid = 0
    elif sdate == None or edate == None:
        valid = 0
    
    return valid
    