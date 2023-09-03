def check(c):
    if(c.isalpha()):
        if(c=='a'or c=='e'or c=='i' or c=='o' or c=='u'):
            print("Given character is vowel")
        else:
            print("Given character is consonant")
    elif(c.isdigit()):
        print("Given number is digit")


check('20')
