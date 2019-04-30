# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
f=open("links.txt","w")
for i in range(1,5):
	#link="https://www.imdb.com/title/"+i+"/reviews"
	link="https://nptel.ac.in/srt/101106031/lec-0"+str(i)+".srt"
	f.write(link)
	f.write("\n")
