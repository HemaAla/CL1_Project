f1=open("FrequentEntities.txt","r")
f2=open("NounsExtracted","r")
fw=open("DomainEntities","w")
Nouns=[]
for i in f2:
	i=i.strip()
	Nouns.append(i)
FreqEntities=[]
for i in f1:
	i=i.strip()
	FreqEntities.append(i)

#print(FreqEntities[0:5])
for entity in FreqEntities:
	if entity in Nouns:
		if(len(entity)!=1):
			fw.write(entity+"\n")
		
