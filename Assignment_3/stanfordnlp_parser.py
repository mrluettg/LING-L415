import stanfordnlp
import sys
from nltk import sent_tokenize
file_name = sys.argv[1]
file = open(file_name, 'r', encoding='utf8')
text = ""
for line in file:
    text += line
file.close()
sentence_lst = sent_tokenize(text)
nlp = stanfordnlp.Pipeline()
for i in range(0, len(sentence_lst)):
    doc = nlp(sentence_lst[i])
    print(doc.conll_file.conll_as_string())