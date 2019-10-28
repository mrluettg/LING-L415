import sys
compare_file_name = sys.argv[1]
i = 1
file_name_lst = []
while i < 100:
    try:
        file_name_lst.append(sys.argv[i])
    except:
        break
    i += 1
compare_file = open(compare_file_name, 'r', encoding="utf8")
compare_file_tag_num = 0
for line in compare_file:
    compare_file_tag_num += 1
uniq_tag_lst = []
compare_file.close()
for file_name in file_name_lst:
    file = open(file_name, 'r', encoding="utf8")
    for line in file:
        line_lst = line.split()
        tag = line_lst[0]
        if tag not in uniq_tag_lst:
            uniq_tag_lst.append(tag)
    file.close()
print("Tags in document: " + str(compare_file_tag_num))
print("Tags in corpus: " + str(len(uniq_tag_lst)))
print("Generality: " + str(compare_file_tag_num/len(uniq_tag_lst)))
    
