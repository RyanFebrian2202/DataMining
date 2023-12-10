# imports and load spacy english language package
import spacy
from spacy import displacy
from spacy import tokenizer
nlp = spacy.load('en_core_web_sm')
 
#Load the text and process it
# I copied the text from python wiki
text =("Python is an interpreted, high-level and general-purpose programming language"
       "Pythons design philosophy emphasizes code readability with"
       "its notable use of significant indentation."
       "Its language constructs and object-oriented approach aim to"
       "help programmers write clear and"
       "logical code for small and large-scale projects")
# text2 = # copy the paragraphs from  https://www.python.org/doc/essays/ 
doc = nlp(text)
#doc2 = nlp(text2)
sentences = list(doc.sents)
print(sentences)
# tokenization
for token in doc:
    print(token.text)
# print entities
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)
# now we use displaycy function on doc2
displacy.render(doc, style='ent', jupyter=True)