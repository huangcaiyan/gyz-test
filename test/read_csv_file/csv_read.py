# import csv
# import os

# # read local csv file
# file_dir = '/Users/doghome/work/guanplus-test/test/read_csv_file/info.csv'
# date= open(file_dir,'rU')
# date = csv.reader(date)

# # print dates
# for user in date:
#     print(user)


import csv

# read local csv file
file_dir = '/Users/doghome/work/guanplus-test/test/read_csv_file/info.csv'
date= open(file_dir,'rU')
date = csv.reader(date)

# print dates
for user in date:
    print(user[1])


