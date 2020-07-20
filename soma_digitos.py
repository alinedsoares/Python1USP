N = (int(input("Digite um número inteiro:")))
s = 0
while N > 0:
 r = N % 10
 N = N // 10
 s = s + r
print (s)
