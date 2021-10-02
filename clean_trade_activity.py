import csv
import pandas as pd

def find_line_number():
    the_file = open('TradeActivity.csv','r')
    reader = csv.reader(the_file)

    a = 'Filled Orders'
    b = 'Cancelled Orders'
    i = 0

    read_file = list(reader)
    the_file.close()

    # finds when var 'a' matches the data in csv, breaks
    for i, row in enumerate(read_file):
        if a in row:
            break
        x = i
    # print(i, row)

    for i, row in enumerate(read_file):
        if b in row:
            break
        y = i
    # print(i, row)
    
    x = x + 2
    data_cap = read_file[x:y]
    # print(data_cap)
    df = pd.DataFrame(data_cap)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    return df


# ----------------------------------------------------------------
# from csv import reader

# opened_file = open(‘AppleStore.csv’)
# read_file = reader(opened_file)
# apps_data = list(read_file)
# opened_file.close()

# print(apps_data[1:3])