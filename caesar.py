import string 

def ceasar(word,n):
    
    punctuation = string.punctuation
    #print(10*"*",punctuation)
    result = ""    
    for i in word:        
        if i.isupper():
            ceasar = chr((ord(i)+n -65)%26 + 65)
            result = result + ceasar

        elif i.islower():
            ceasar = chr((ord(i)+n -97)%26 + 97)
            result = result + ceasar
        else:
            result = result + i

    return result        

print(ceasar("ABC CZ& aB xyZ",4))
