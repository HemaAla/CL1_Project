#f=open("pos_tags")
import nltk
f=open("sent","r")
fw=open("NounsExtracted","w")
for i in f:
	tokens=nltk.word_tokenize(i)
	tags=nltk.pos_tag(tokens)
	for (word,tag) in tags:
		if(tag=='NN' or tag=='NNP'):
			fw.write(word+"\n")
	
