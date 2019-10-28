import sys
from math import log

file = sys.argv[1]
unigram_file_name =  file + "_1_frequency.txt"
bigram_file_name = file + "_2_frequency.txt"
word_1 = sys.argv[2]
word_2 = sys.argv[3]
bigram = word_1 + " " + word_2
unigram_dict = {}
unigram_file = open(unigram_file_name, 'r', encoding='utf8')
for line in unigram_file:
    line_lst = line.split()
    unigram_dict[line_lst[0]] = int(line_lst[1])
bigram_dict = {}
bigram_file = open(bigram_file_name, 'r', encoding='utf8')
for line in bigram_file:
    line_lst = line.split()
    bigram_dict[line_lst[0] + " " + line_lst[1]] = int(line_lst[2])
total_tokens = 0
for unigram in unigram_dict:
    total_tokens += unigram_dict[unigram]
def log_likelyhood():
    total_tags = len(unigram_dict)
    freq_x = unigram_dict[word_1]/total_tokens
    freq_y = unigram_dict[word_2]/total_tokens
    freq_xy = bigram_dict[bigram]/unigram_dict[word_1]
    return -2 * log(freq_x*freq_y/freq_xy)
print("log-likelyhood: " + str(log_likelyhood()))

def mutual_information():
    A = bigram_dict[bigram]
    B = unigram_dict[word_1] - A
    C = unigram_dict[word_2] - A
    N = total_tokens
    return log(A * N /((A + C)*(A + B)))
print("mutual_information: " + str(mutual_information()))
def mutual_information_2():
    total_tags = len(unigram_dict)
    p_t = unigram_dict[word_1]/total_tags
    p_c = unigram_dict[word_2]/total_tags
    p_tc = bigram_dict[bigram]/unigram_dict[word_1]
    return log(p_tc/(p_c * p_t))
print("mutual_information_2: " + str(mutual_information_2()))
def X2():
    N = total_tokens
    total_t = unigram_dict[word_1]
    total_c = unigram_dict[word_2]
    obs_A = bigram_dict[bigram]
    obs_B = total_t - obs_A
    obs_C = total_c - obs_A 
    obs_D = (N - total_t) - obs_C
    exp_A = total_t * total_c /N
    exp_B = total_t * (N - total_c)/N
    exp_C = (N - total_t) * total_c/N
    exp_D = (N - total_t) * (N - total_c)/N
    obs_exp_tuple_lst = [(obs_A, exp_A), (obs_B, exp_B), (obs_C, exp_C), (obs_D, exp_D)]
    x2 = 0
    for obs_exp_tuple in obs_exp_tuple_lst:
        x2 += (obs_exp_tuple[0] - obs_exp_tuple[1])**2/obs_exp_tuple[1]
    return x2
print ("X2: ", X2())
