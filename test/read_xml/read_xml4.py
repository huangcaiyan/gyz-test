# -*- coding: UTF-8 -*-

from xml.dom import minidom
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 获得标签对之间的数据
# open xml file
file_dir = '/Users/doghome/work/guanplus-test/test/read_xml/info.xml'
dom = minidom.parse(file_dir)

# get xml file parameter
root = dom.documentElement

provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')

# get the second tag pair's value
p2 = provinces[1].firstChild.data 
print(p2) 

# get the first city tag pair's value
c1 = citys[0].firstChild.data
print(c1)

# get the second city tag pair's value
c2 = citys[1].firstChild.data
print(c2)