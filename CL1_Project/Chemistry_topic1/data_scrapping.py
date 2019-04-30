# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib2
import urllib
import warnings
import nltk
import re


def TextCleaner(text):   
	text=re.sub(r'(\d+)',r'',text)
	text=text.replace(u'%','')
	text=text.replace(u',','')
	text=text.replace(u'"','')
	text=text.replace(u'(','')
	text=text.replace(u')','')
	text=text.replace(u'"','')
	text=text.replace(u':','')
	text=text.replace(u"'",'')
	text=text.replace(u"‘‘",'')
	text=text.replace(u"’’",'')
	text=text.replace(u"''",'')
	text=text.replace(u"-",'')
	text=text.replace(u'>','')
	text=text.replace(u'\n\n\n  ','')
	text=text.replace(u".",'')
	text=text.replace(u"\n  \n",'')
	text=text.replace(u"\n",' . ')
	#text=text.replace(u"u'",'.')

	return text


f=open("links.txt","r")
fw=open("content","w")
# Connect to the URL
for i in f:
	#opening the url
	f = urllib.urlopen(i)
	#reading the content in the url
	myfile = f.read()
	#print(myfile)
	#parsing
	#soup = BeautifulSoup(myfile)
	soup=BeautifulSoup(myfile, "html5lib")
	content=[]
	#taking review from this perticular class
	for p in soup.find_all('body'):
		text=TextCleaner(p.text)
		content.append(text)
		#mwtokenizer = nltk.MWETokenizer(separator='.')
		#review=mwtokenizer.tokenize(review)
		fw.write(str(content))
		
