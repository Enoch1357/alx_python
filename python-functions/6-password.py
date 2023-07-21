
password = str()
def validate_password(password):
    if (len(password) >= 8):
        l, u, p, d = 0, 0, 0, 0
        for i in password:
            
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
 
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
 
            # counting digits
            if (i.isdigit()):
                d+=1           
 
            # counting the mentioned special characters
            if(i==' '):
                p+=1 
    else:
        return False       
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        return False
    elif (l>=1 and u>=1 and d>=1 and l+u+d==len(password)):
        return True
    return False