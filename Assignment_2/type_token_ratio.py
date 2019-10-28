import sys
#takes in a frequency file created by n_gram_frequency.py and prints the type-token ratio
file_name = sys.argv[1]
file = open(file_name, 'r', encoding="utf8")
total_types = 0
total_tokens = 0
for line in file:
    total_types += 1
    line_lst = line.split()
    total_tokens += int(line_lst[1])

print(total_types/total_tokens)