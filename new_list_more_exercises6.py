string_list = ["Rishabh", "Rishabh", "Abhishek","Rishabh", "Divyashish", "Divyashish"]
new_list = []
index = 0
while index<len(string_list):
    string = string_list[index]
    if string == string_list[index]:
        if string_list[index] not in new_list:
            new_list.append(string_list[index])
    index = index+1
print new_list
