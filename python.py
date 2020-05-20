sentence=input("enter a sentence")
p=0
k=0
for a in sentence:
  if a.isdigit():
     p=p+1
  elif a.isalpha():
     k=k+1
  else:
      pass
print("letters", p)
print("digits", k)
     
 