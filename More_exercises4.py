user_input1 = int(raw_input("enter your number"))
user_input2 = int(raw_input("enter your second number"))
user_input3 = int(raw_input("enter your third number"))
if user_input1<user_input2 and user_input3<user_input2:
    print user_input2
elif user_input3>user_input1 and user_input3>user_input2:
    print user_input3
else:
    print user_input1
