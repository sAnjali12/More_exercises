user_input =(raw_input("enter your password"))
if len(user_input)<=16:
	if "$" in user_input:
		if "2"or"8" in user_input:
			if "A"or"Z"in user_input:
				print "Strong Password"
else:
	print "Weak Password"
