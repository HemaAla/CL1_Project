Implementing Domain Entity Identifiaction by scraping data from online NPTEL videos transcipts, for different subjects like Chemistry Aerospace Engineering etc.<br?
AerospaceEng & Chemistry_topic1 &Chemistry_topic2 <br>
  get_link.py----> In this formed url links by using lecture id for example aerospace engeneering the lecture id will be " 101106031" from this we have formed 'link="https://nptel.ac.in/srt/101106031/lec-0"+str(i)+".srt"' <br><br>
  The created links are there in links.txt<br><br>
  data_scrapping.py----> In this using beatifulsoup and urllib we extracted content form the urls.<br><br>
  ngram_frequency.py----> calculated unigram,bigram and trigram frequencies from the content, stored the words which occur more than 4 words in frequently occuring entities file.
  get_sentences.py -----> Got sentences from the content<br><br>
  pos_tag.py -------> Using NLTK pos tagger tagged the data<br><br>
  Extracting_Entities.py ------> Extracted entities whose pos tag is NNP or NNS or NN.<br><br>
  GetDomainEntities.py--------->In the above step we extracted nouns, and we have frequent entities with us, so in this we extracted which are nouns and occuring frequently.....Identifying frequently occuring entities. Which are stored in DomainEntities File.<br><br>
  
  Common_entities-------> In this we checked whether there are common  DomainEntities present in Chemistry topic1 (like introduction to materials) and topic2(coordination Chemistry).
  
 
  
  
  
  
