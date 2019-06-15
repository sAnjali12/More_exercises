list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
index = 0
new_list = []
while index<len(list1):
    if list1[index] in list2:
        new_list.append(list1[index])
    index = index+1
print new_list
