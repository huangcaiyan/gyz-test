
# -*- encoding:utf-8 -*-
from xml.dom import minidom

# 获得标签的属性值
# open xml file
file_dir = '/Users/doghome/work/guanplus-test/test/read_xml/info.xml'
dom = minidom.parse(file_dir)

# get xml file parameter
root = dom.documentElement

logins = root.getElementsByTagName('login')

# get login tag's username value
username = logins[0].getAttribute('username')
print 'username1=>',username

# get login tag's password value
password = logins[0].getAttribute('password')
print 'password1=>',password

# get the second login tag's username value
username = logins[1].getAttribute('username')
print 'username2=>',username

# get the second login tag's username value
password =logins[1].getAttribute('password')
print 'password2=>',password