f1=open("DomainEntities_topic1","r")
f2=open("DomainEntities_topic2","r")
fw=open("CommonEntities","w")
D1=[]
for i in f1:
	i=i.strip()
	D1.append(i)
D2=[]
for i in f2:
	i=i.strip()
	D2.append(i)

#print(FreqEntities[0:5])
for entity in D1:
	if entity in D2:
		if(len(entity)!=1):
			fw.write(entity+"\n")
