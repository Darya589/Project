
with open("file3.txt", "w", encoding= "utf-8") as f:
    f.write("Hello World \n")
    f.write("Привет мир \n")
    
with open("file3.txt", "r", encoding= "utf-8") as d:
    n = d.readlines()
    print(len(n))
print(type(n))
print(range(9))

for i in n:
    print(f"{i} !")