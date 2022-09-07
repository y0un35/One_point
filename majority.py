def majority(liste):
    floor = len(liste)/2
    my_dict = {}
    if len(liste)==0:
        return "List is empty"
    for i in liste:
        my_dict[i]=my_dict.get(i,0)+1
    val = max(my_dict,key=my_dict.get)
    if my_dict[i]>floor:
        return val    
    else:
        return "Majority element doesn't exist"

print(majority([1,2,2,3,3,3,3]))
print(majority([]))