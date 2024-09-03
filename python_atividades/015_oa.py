# Exercício 008 - Conversão m, cm e mm
n = float(input("Digite um valor em metros:"))
cm = n*100
mm = n*1000
print("Voce digitou",n, "metros.")
print("Há {0} centímetros em {1} metros".format(cm, n))
print("Há {0} milímetros em {1} metros".format(mm, n))
#feito