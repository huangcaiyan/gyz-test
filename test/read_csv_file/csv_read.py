import csv
import os

# read local csv file
info_file = open('/Users/huangcaiyan/work/guanplus-test/test/read_csv_file/info.csv','rU')
date = csv.reader(info_file)

# print dates
for user in date:
    print(user)