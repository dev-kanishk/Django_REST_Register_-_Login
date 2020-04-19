import gspread
import pandas as pd
from pprint import pprint
import operator
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/codermeter/Django_REST_Register_-_Login/task/task_app/json_data.json")
client = gspread.authorize(creds)

def get_nameIndex(data):
    name_index = {}
    for i in range(len(data[0])):
        if data[0][i] != "":
            name_index[data[0][i].title()] = i
    return name_index

def counter(data,this):
    count = 0

    for i in range(5,len(data[0])):
        if data[i][this+1] != "" and data[i][this+1] != "no" and data[i][this+1] != "No" and data[i][this+1] != "NO":
            count += 1;
    return count


# sheet1 = client.open("this")

def final_list():
    sheets = []
    sheets.append("this")
    sheets.append("Copy of Target 2021 Team-2A")

    subsheets = 'Easy Problems','Medium Problems','Hard Problems'

    # page = sheet.worksheet("Easy Problems")

    topper = {}

    for sheet in sheets:
        sheet1 = client.open(sheet)

        for subsheet in subsheets:
            page = sheet1.worksheet(subsheet)
            data = page.get_all_values()
            name_index = get_nameIndex(data)
    #         print(name_index)
            k = 0
            for i in name_index:
                k+=1
                if name_index[i] > 4:
                    ths = counter(data,name_index[i])
                    coder = i
                    if i in topper:
                        topper[coder] += ths
                    else:
                        topper[coder] = ths
    # listofTuples = dict(sorted(topper.items() , reverse=True, key=lambda x: x[1]))
    # sorted_d = sorted(topper.items(), key=operator.itemgetter(1),reverse=True)
    # print(listofTupels)
    return topper



