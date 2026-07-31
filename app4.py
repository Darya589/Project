"""def sheep(x):
    for i in range(1, x + 1):
        if i == 1:
           print(f"{i} овца")
        elif i in [2, 3, 4]:
           print(f"{i} овцы")
        else:
            print(f"{i} овец")
print(sheep(int(input())))
   """           

def str(x):
    k = []
    for i in x:
      if i == "ф":
         k.append("b")
      elif i == "л":
         k.append("j")
      else:
         k.append(i)

    return "".join(k)
   
        
print(str(input()))
a = str("100")
