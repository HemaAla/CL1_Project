import nltk
'''f=open("content","r")
fw=open("sentences","w")
lines=f.readlines()
sent=nltk.sent_tokenize(lines[0])
fw.writelines(sent)
print(nltk.pos_tag(sent))
print(sent[0])'''
f=open("sent","r")
fw=open("pos_tags","w")
for i in f:
	tokens=nltk.word_tokenize(i)
	tags=nltk.pos_tag(tokens)
	fw.writelines(str(tags))
	fw.write("\n")

