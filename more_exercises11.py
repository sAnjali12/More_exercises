sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
count = 0
new_list = []
while count<len(sentence):
	new_index = count
	str_count = " "
	while new_index<len(sentence):
		if sentence[new_index] == " ":
		     break
		else:
		     str_count = str_count+sentence[new_index]
		new_index = new_index+1
	new_list.append(str_count)
	count = new_index+1
print new_list
