# desafio 013 - Calculo de porcentagem
n = float(input("Digite o preço atual:"))
pc = n*5
pc2 = pc/100
t = n - pc2
print("O desconto de 5% aplicado ao preço {} é R${}.".format (n,pc2))
print("O valor final, com desconto aplicado é R$",t)
#finalizado
