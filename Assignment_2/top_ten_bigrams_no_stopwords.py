from nltk.corpus import stopwords
import sys
stop_words = set(stopwords.words('english'))
punct = ('.', ',', '``', '\'\'', '!', '?', '\'', '`', ':', ';', '\'s', '’', '“ ', '”', '“')
file_name = sys.argv[1]
file = open(file_name, 'r', encoding='utf8')
bigram_lst = []
for line in file:
    if len(bigram_lst) == 10: break
    line_lst = line.split()
    word_1 = line_lst[0]
    word_2 = line_lst[1]
    if word_1 not in stop_words and word_2 not in stop_words and word_1 not in punct and word_2 not in punct:
        bigram_lst.append(line)
file.close()
for bigram in bigram_lst:
    print(bigram.strip("\n"))