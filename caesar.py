import string 

def ceasar(word,value):
    
    punctuation = string.punctuation
    #print(10*"*",punctuation)

    result = ""
    
        
    
    for i in word:
        if i == " " or i in punctuation:
            result = result + i
            print(result,end = '')
        else:
            # i need to the mathematical formula to avoid ASCII after Z
            print(chr(ord(i)+value),end = '')
            
ceasar("ABCD OPQ",4)            