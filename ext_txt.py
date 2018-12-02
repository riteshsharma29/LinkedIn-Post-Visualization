#!/usr/bin/python
# coding: utf-8 -*-

import codecs
import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from textwrap import wrap
pid = sys.argv[1]

tv = []
l_1 = []
l_2 = []
l_3 = []
l_4 = []
l_5 = []
l_6 = []
t = []

#function for company list
def read_text(filename):

    lines = codecs.open(filename,"rb", encoding='utf-8')
    line = lines.read().encode('utf-8')
    l = line.split(chr(10))
    Title = l[0].decode('utf-8')
    views = l[2]
    tv.append(Title)
    tv.append(views)	
    num = str(l[4]).split()
    company = str(l[4]).replace('people',"").replace('from',"").replace(str(num[0]),"").strip()
    l_1.append(int(num[0]))
    l_2.append(company)	
    for i in range(0,len(l)):
        if len(l[i]) > 0:
           m = re.search(r'\d+$', l[i])
           # if the string ends in digits m will be a Match object, or None otherwise.
           if m is not None:
              #print str(l[i]).replace(m.group(),""),m.group()
              var = str(l[i]).replace(m.group(),"")
              l_1.append(int(m.group()))
              l_2.append(var.decode('utf-8'))
			  
#function for Title/Location	
def read_text_2(filename):

    lines = codecs.open(filename,"rb", encoding='utf-8')
    line = lines.read().encode('utf-8')
    l = line.split(chr(10))
    c = str(l[4]).split()
    str_1 = l[4] + l[5]
    str_1 = str(str_1).replace(str(c[0]),"").replace('people viewed your postfrom',"").replace('people who have the title',"").replace('people viewed your videofrom',"").replace('viewed',"").strip()	
    if filename == '2.txt':
	    l_3.append(int(c[0]))
	    l_4.append(str_1)	
    if filename == '3.txt':
	    l_5.append(int(c[0]))
	    t.append(0) 
	    l_6.append(str_1)
    #print c[0],str_1
    for i in range(0,len(l)):
        if len(l[i]) > 0:
           m = re.search(r'\d+$', l[i])
           # if the string ends in digits m will be a Match object, or None otherwise.
           if m is not None:
              var = str(l[i]).replace(m.group(),"")
              #print str(l[i]).replace(m.group(),""),m.group()
              if filename == '2.txt':
                  l_3.append(int(m.group()))
                  l_4.append(var.decode('utf-8'))
              if filename == '3.txt':				  
                  l_5.append(int(m.group()))              
                  l_6.append(var.decode('utf-8'))
                  t.append(0)	


	
read_text('1.txt')
read_text_2('2.txt')
read_text_2('3.txt')

########################################################## Visulaization - company ##############################################

def company():

    #1. For viewers by company
    df_1 = pd.DataFrame({'Company':l_2,'Number of Viewers':l_1})
    y = df_1['Number of Viewers'].values
    df_1.plot(kind='barh',color='g')
	
    #Post link is the Maintitle
    maint = "https://www.linkedin.com/in/ritesh-sharma29/detail/recent" + chr(45) + "activity/shares/ca/share" + chr(45) + "analytics/urn:li:activity:" + pid + "/"
    maint = '\n'.join(wrap(maint))	
	
    plt.xlabel('Number of Viewers')
    plt.ylabel('Company')
	
    #Wraping Long company name
    labels = [ '\n'.join(wrap(l, 20)) for l in df_1['Company'].values ]

    # range(Number of categories)
    plt.yticks(range(len(df_1['Company'].values)),labels)

    plt.title(maint + " : " + tv[1])
    for i, v in enumerate(y):
        plt.text(v,i ,str(v), color='blue', fontweight='light')
    plt.show()
    #plt.savefig('company.png')


######################################################## Visulaization - Title #######################################################

def designation():

    #2. For viewers by Title
    df_2 = pd.DataFrame({'Title':l_4,'Number of Viewers':l_3})

    y = df_2['Number of Viewers'].values
    df_2.plot(kind='barh',color='orange')
	
	#Post link is the Maintitle
    maint = "https://www.linkedin.com/in/ritesh-sharma29/detail/recent" + chr(45) + "activity/shares/ca/share" + chr(45) + "analytics/urn:li:activity:" + pid + "/"
    maint = '\n'.join(wrap(maint))
	
    plt.xlabel('Number of Viewers')
    plt.ylabel('Title')

    #Wraping Long company name
    label = [ '\n'.join(wrap(l, 20)) for l in df_2['Title'].values ]

    # range(Number of categories - len(df_2['Title'].values))
    plt.yticks(range(len(df_2['Title'].values)),label)
    plt.title(maint + " : " + tv[1])

    for i, v in enumerate(y):
        plt.text(v,i ,str(v), color='blue', fontweight='light')
    plt.show()
    #plt.savefig('title.png')


######################################################## Visulaization - Location #######################################################


def location():

    #3. For viewers by Location
	#Location list
    pielabel = [ '\n'.join(wrap(p, 20)) for p in l_6 ]

    cols = ['r','m','c','b','g','w','navy','khaki','pink']
    plt.pie(l_5,
        labels=l_6,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=t, #0.1 is used to explote the slice-share use 0.0 instead if this feature is not required.
        autopct='%1.1f%%'
    )
	
    maint = "https://www.linkedin.com/in/ritesh-sharma29/detail/recent" + chr(45) + "activity/shares/ca/share" + chr(45) + "analytics/urn:li:activity:" + pid + "/" + " : Viewers By Location"
    maint = '\n'.join(wrap(maint))

    plt.title(maint)
    plt.show()
    #plt.savefig('location.png')


company()
designation()
#passing tuple for explode parameter
t = tuple(t)
location()