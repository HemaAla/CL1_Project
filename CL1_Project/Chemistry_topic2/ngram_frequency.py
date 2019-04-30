import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

'''text = "I need to write a program in NLTK that breaks a corpus (a large collection of \
txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams.\  I need to write a program in NLTK that breaks a corpus"'''
f=open("content","r")
lines=f.readlines()
#for i in f:
token = nltk.word_tokenize(str(lines))
unigram=ngrams(token,1)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

print("***************unigram frequency***************")
#print(Counter(unigram))
fw=open("FrequentEntities.txt","w")
fdist = nltk.FreqDist(unigram)
for k,v in fdist.items():
    #print (k,v)
    if(v>=4):
    	fw.write(k[0]+"\n")
    
#print(fdist[('increase',)])
#print(fdist[('PDE',)])

'''print("***************bigram frequency***************")
print Counter(bigrams)'''
