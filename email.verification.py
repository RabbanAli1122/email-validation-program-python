def Wrong_Email_Errors(error_number):
    print("Email incorrect!\nError number:", error_number)
    int(input("Enter 1 for error detail and enter 0 to exit the email checking:"))
    if error_number == 1:
        print("Error number:1\n"
              "Which means that your email address is smaller than the minimum email syntax\n"
              "Which is not valid.")
    elif error_number == 2:
        print("Error number:2\n"
              "Which means that your email address' first letter is a non-alphabatic or it is a space\n"
              "Which is not valid.")
    elif error_number == 3:
        print("Error number:3\n"
              "Which means that your email address contains zero, two or more \"@\" signs.\n"
              "Which is not valid.")
    elif error_number == 4:
        print("Error number:4\n"
              "Which means that your email address doesn't contains \".com\"\n"
              "Which is not valid.")
    elif error_number == 5:
        print("Error number:5\n"
              "Which means that your email address contains a space or it contains a capital alphabate.\n"
              "Which is not valid.")
    return ""


d, k, j = 0, 0, 0
email = input("Only \".com\" top-level domain is allowed to enter.\nEnter your Email:\n")
"""the minimum length of an email address is 6 characters
for exaple:g@g.in"""
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace() == True:
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
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