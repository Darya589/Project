"""n = input() # 8 11 -2 9
def tekst(n):
   m = n.split(" ")
   k = 0
   for i in m:
      if int(i) % 2 != 0:
         k += int(i)
   return k
print(tekst(n))"""


h = "Москва Уфа Тверь"
def tekst(h):
   
   return [len(i) for i in h.split(" ")]
print(tekst(h))   