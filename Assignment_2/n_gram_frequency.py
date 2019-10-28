#how to use:
import sys
import re
from nltk import word_tokenize
def n_gram_frequency(file_name, n):
    #generate dictionary from file.
    file = open(file_name, 'r', encoding="utf8")
    freq_dict = ""
    word_lst = []
    for line in file:
        if line.strip("\n") == "": continue
        line_lst = word_tokenize(line)
        for word in line_lst:
            lower_word = word.lower()
            word_lst.append(lower_word)
    token_lst = []
    #if necessary do n-grams. 
    if n > 1: 
        for i in range(len(word_lst) - (n - 1)):
            token = ""
            for j in range(n):
                num = i + j
                token += word_lst[num] + " "
            token_lst.append(token[:-1])
    else: token_lst = word_lst
    token_dict = {}
    for word in token_lst:
        if word in token_dict:
            token_dict[word] += 1
        else:
            token_dict[word] = 1
    listOfTuples = sorted(token_dict.items(), key = lambda x : x[1])
    i = len(listOfTuples) - 1
    new_file = open(file_name[:-4] + "_" + str(n) + "_frequency.txt", 'w', encoding="utf8")
    while i > -1:
        new_file.write(listOfTuples[i][0] + " " + str(listOfTuples[i][1]) + "\n")
        i -= 1

if __name__ == "__main__":
    file_name = sys.argv[1]
    n = int(sys.argv[2])
    n_gram_frequency(file_name, n)
