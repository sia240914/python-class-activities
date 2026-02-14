def palindrome(tuple):
    s=0
    e=len(tuple)-1
    while(s<e):
        if tuple[s]!= tuple[e]:
            return False
        s=s+1
        e=e-1
    return True


tuple=(1,5,2,3,2,1)
if(palindrome(tuple)):
    print("palindrome")
else:
    print("not a palindrome")