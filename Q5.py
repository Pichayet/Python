def AND(a,b):
    if a == 1 and b == 1 :
        return True
    else :
        return False
def OR(a,b):
    if a == 1 :
        return True
    elif b == 1 :
        return True
    else:
        return False
def NOT(a):
    if a == 1:
        return False 
    elif a == 0:
        return True


a = 1
b = 1

print(OR(AND(a, NOT(b)), AND(NOT(a), b)))
