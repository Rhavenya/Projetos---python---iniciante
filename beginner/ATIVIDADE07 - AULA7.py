n1 = int(input('Um valor:'))
n2 = int(input('Um outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, a multiplicação é {} a divisão é {:.2f}'. format(s, m, d), end=' ')
print ('Divisão inteira:{}, Potência: {}'. format(di, e))