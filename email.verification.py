def Wrong_Email_Errors(error_number):

    print("Email incorrect!\nError number:", error_number)
    while True:
        code=int(input("Enter 1 for error detail and enter 0 to exit the email checking:"))
        if code == 1:

                if error_number == 1:
                    return ("Error number:1\n"
                          "Which means that your email address is smaller than the minimum email syntax\n"
                          "Which is not valid.")
                    break
                elif error_number == 2:
                    return ("Error number:2\n"
                          "Which means that your email address' first letter is a non-alphabatic or it is a space\n"
                          "Which is not valid.")
                    break
                elif error_number == 3:
                    return ("Error number:3\n"
                          "Which means that your email address contains zero, two or more \"@\" signs.\n"
                          "Which is not valid.")
                    break
                elif error_number == 4:
                    return ("Error number:4\n"
                          "Which means that your email address doesn't contains \".com\" or it contains a \"space\" at the end of the email \n"
                          "Which is not valid.")
                    break
                elif error_number == 5:
                    return ("Error number:5\n"
                          "Which means that your email address contains a space or it contains a capital alphabate.\n"
                          "Which is not valid.")
                    break
        elif code ==0:
            return ("Good bye")
            break
        else:
            continue


invalid_symbols, space, j = 0, 0, 0
email = input("Only \".com\" top-level domain is allowed to enter.\nEnter your Email:\n")
"""the minimum length of an email address is 6 characters
for exaple:g@g.in"""
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace() == True:
                        space = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        invalid_symbols = 1
                if invalid_symbols == 1 or j == 1 or space == 1:
                 print(Wrong_Email_Errors(error_number=5))
                else:
                    print("Right Email!")
            else:
                print(Wrong_Email_Errors(error_number=4))
        else:
            print(Wrong_Email_Errors(error_number=3))
    else:
        print(Wrong_Email_Errors(error_number=2))
else:
    print(Wrong_Email_Errors(error_number=1))
"""
'^'operator means that if there is two different statements then the
result is true e.g True ^ False = True and if there is two same 
statements then the result is False e.g True ^ True = False
"""
