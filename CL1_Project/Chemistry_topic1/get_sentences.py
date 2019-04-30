import nltk
f=open("content","r")
fw=open("sent","w")
for i in f:
	sen=nltk.word_tokenize(i)
	#print(sen)
	#print("hema")
	st=""
	for j in sen:
		if(j=='.'):
			fw.write(st)
			fw.write("\n")
			st=""
		else:
			st=st+j+" "
