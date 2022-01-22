# Using 'while' write a Python program to print the multiplication table of n, 2<=n<=10. Replace the 'while' statement with an equivalent 'for'  statement to get the same output
x=int(input())
i=0
while(i<11):
  print(x,"*",i,"=",x*i)
  i=i+1

for i in range(0,11):
  print(x,"*",i,"=",x*i)
  