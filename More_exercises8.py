list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3=list1+list2

index1=0
new_list = []
while index1<len(list3):
    if list3[index1] not in new_list:
            new_list.append(list3[index1])
    index1 = index1+1
new_list.sort()
print new_list
