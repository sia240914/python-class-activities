sentence=input("enter your sentence: ")
alphabet=input("enter your alphabet") 
count=0
sent_leng=len(sentence)
for i in range (0,sent_leng):
    if(alphabet==sentence[i]):
        count=count+1

print("occurence of",alphabet," is ",count)