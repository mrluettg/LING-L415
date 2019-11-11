#This is based on
import sys
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import chunk
file_name = sys.argv[1]
file = open(file_name, 'r', encoding='utf8')
text = ""
for line in file:
    text += line
file.close()
sentence_lst = sent_tokenize(text)
tagged_sentences = []
for sentence in sentence_lst:
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    tagged_sentences.append(tagged)
for tagged_sentence in tagged_sentences:
    tree = chunk.ne_chunk(tagged_sentence)
    print(tree)