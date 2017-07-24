# -*- encoding:utf-8 -*-

from xml.dom import minidom

# 获得任意表亲名
# open xml file
file_dir = '/Users/doghome/work/guanplus-test/test/read_xml/info.xml'
dom = minidom.parse(file_dir)

# get xml file parameter
root = dom.documentElement

# get tagname
tagname = root.getElementsByTagName('browser')
print 'tagname[0]=>',tagname[0].tagName

tagname = root.getElementsByTagName('login')
print 'tagname[1]=>',tagname[1].tagName

tagname = root.getElementsByTagName('province')
print 'tagname[2]=>',tagname[2].tagName 


