n1 = int(input("digite um valor por gentileza:"))
n2 = int(input("digite um outro valor:"))
s = n1 + n2 
m = n1 * n2 
d = n1 + n2 
di = n1 // n2 
e = n1 ** n2 
print('A soma é {}, \n o produto é {}, \n e a divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira é {} e potência {}'.format(di, e))
