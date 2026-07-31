"""def sq(r):
    p = 3.14
    try:
       s = p * r**2 
       return s
    except TypeError:
        return type(r), " Неправильный тип данных" 




print(sq("4"))"""

def sq(r, h):
    p = 3.14
    try:
        r = int(r)
        
    except ValueError:
        
        return type(r), " Неправильный тип r данных"

    try:
        h = int(h)
        
    except ValueError:
        
        return type(h), " Неправильный тип данных h"

    s = p * (r**2) * h
    return s
print(sq("Hello", "World"))