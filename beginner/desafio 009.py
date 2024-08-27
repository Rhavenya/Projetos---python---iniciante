num1 = int(input('Coloque o número que você deseja ver a tabuada: '))
calc = num1 * 1
calc2 = num1 * 2
calc3 = num1 * 3
calc4 = num1 * 4
calc5 = num1 * 5
calc6 = num1 * 6
calc7 = num1 * 7
calc8 = num1 * 8
calc9 = num1 * 9
calc10 = num1 * 10

print('O seu resultado será:'.format())
print('_'*12)
print('{:2} x 1  =  {:2}'
      '\n{:2} x 2  =  {:1}'
      '\n{:2} x 3  =  {:1}'
      '\n{:2} x 4  =  {:1}'
      '\n{:2} x 5  =  {:1}'
      '\n{:2} x 6  =  {:1}'
      '\n{:2} x 7  =  {:1}'
      '\n{:2} x 8  =  {:1}'
      '\n{:2} x 9  =  {:1}'
      '\n{:2} x 10 =  {:1}'
      . format(num1,calc, num1, calc2,num1, calc3, num1, calc4, num1, calc5, num1, calc6, num1, calc7, num1, calc8,num1, calc9, num1,  calc10))
print('_'*12,end=(''))