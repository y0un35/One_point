def add_it_up():
    print(" Enter an integer")
    n = input()
    result = 0
    try:
        x = int(n)
        result = x*(x+1)/2
        return result
    except:
        return 0
    
test = add_it_up()     
print(test)

