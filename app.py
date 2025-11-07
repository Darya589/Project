def tekst(n):
    return [i for i in n if i.lower() == i]
    




a = tekst("Hello World")
print(a)

def uniq(a):
    return list(set(a))

print(uniq(a))