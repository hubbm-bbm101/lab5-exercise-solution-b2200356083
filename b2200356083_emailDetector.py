def emailCheck(userMail):
    if "@" in userMail:
        if " " in userMail: 
            print ("The e-mail address you entered is not valid, please try again")
        elif "." in userMail:
            print ("You entered a valid e-mail address")
        else: 
            print ("The e-mail address you entered is not valid, please try again")
    else: print ("The e-mail address you entered is not valid, please try again")

userMail = input ("Please enter your e-Mail address: ")    

while [ ("@" in userMail) == False and ("." in userMail) == False]:
    emailCheck(userMail)
    if "@" in userMail and "." in userMail and " " not in userMail:
        break
    else:
        userMail = input ("Please enter your e-mail address: ")
 
       


 


    

