def matching_words(words):
    ctr=0
    lst=[]
    for word in words:
        if (len(word)>1 and word[0]==word[-1]):
            ctr=ctr+1
            lst.append(word)
    print(lst)
    return ctr
lst=["aba","fav","std","kask","dasd","asda"]
print(matching_words(lst))
    
    