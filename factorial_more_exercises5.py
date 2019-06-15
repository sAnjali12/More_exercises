user_input = int(raw_input("Take a one number"))
index = 0
fact = 1
while index<=user_input:
    fact = fact*user_input
    print fact
    user_input = user_input-1
    index = index+1
print fact
