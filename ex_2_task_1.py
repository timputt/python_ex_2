# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    # Tim's code here

    #confirm there's only one @ symbol
    if s.count("@") != 1:
        return 1, "Looks like you must have only one @ symbol"

    l = s.split("@")
    A , post = l[0], l[1]
    print(A, post) #Debug - confirm pulling A and post correctly

    #Confirm that A is between 3 and 16 characters
    if len(A) <3 or len(A) > 16:
        print("A length is:",len(A)) #Debug - confirm length of A
        return 2, "The email must be between 3 and 16 character long."

    #Confirm count of . is only 1
    if post.count(".") != 1:
        return 3, "The email address must have 1 dot in it."

    #Split apart post @ symbol
    l2 = post.split(".")
    B, C = l2[0], l2[1]

    #Confirm that A and B only contains alpha and numbers
    if A.isalnum() == False or B.isalnum() == False:
        return 4, "You can only use letters and numbers in the email address"

    #Confirm the part after the @ and before part C can only be 2-8 characters
    if len(B) <2 or len(B) >8:
        return 5, "Sorry, but after the @ symbol and before the domain suffix must be between 2 and 8 characters."

    #THIS IS THE ONE SECTION I DIDN'T RECALL.
    #the domain suffix is com, edu, org, gov
    if C not in ["com", "edu", "org", "gov"]:
        print("Your domain site is:", C)
        return 6, "Sorry, your email domain must end in com, edu, org or gov."

    #if everything looks good then print that there aren't any error codes and it's a valid email    
    else:
        return None, "Valid Email"

print (is_valid_email_address("chris.edu"))