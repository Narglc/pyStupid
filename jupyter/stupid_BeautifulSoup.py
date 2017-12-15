#coding:utf-8
from bs4 import BeautifulSoup
html_sample = '\
<html> \
  <body> \
    <h1 id="title">Hello World</h1> \
    <a href="#" class="link">This is link1</a> \
    <a href="# link2" class="link">This is link2</a>\
  <body>\
<html>'

soup = BeautifulSoup(html_sample,"html5lib")
print soup.text                     #不含tab的内容
# print '====='
# print soup.contents                 #全部内容
print soup.select('a')[0]
print soup.select('.link')            #class  :   .link
# print soup.select('#title')           #id :   #title
# print ""
