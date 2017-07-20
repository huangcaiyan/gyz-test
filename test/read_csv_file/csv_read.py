import csv

# read local csv file
info_file = open('../read_csv_file/info.csv','r')
date = csv.reader(info_file)

# print dates
for user in date:
    print(user)