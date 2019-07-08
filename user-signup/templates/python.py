import re

input_username =username
if  re.match(" ", input_username):
    return(s)
    sys.exit()
elif len(input_username) > 20 or len(input_username) <3:
    print "Error! Only 15 characters allowed!"
    sys.exit()

print "Your input was:", input_username

-->

input_password = password
if  re.match(" ", input_password):
    print "Error! Only letters a-z allowed!"
    sys.exit()
elif len(input_password) > 20 or len(input_password) <3:
    print "Error! Only 15 characters allowed!"
    sys.exit()

print "Your input was:", input_password

-->

input_email = email
if not re.match("^[A-Z][a-z]@.", input_email):
    print "Error! Only letters a-z allowed!"
    sys.exit()
elif re.match(" "):
        print "error"
elif len(input_email) > 20 or len(input_email) <3:
    print "Error! Only 15 characters allowed!"
    sys.exit()

print "Your input was:", input_email