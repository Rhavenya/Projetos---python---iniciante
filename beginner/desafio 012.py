valor1 = float(input('Insira o valor do produto: '))
desc1 = float(input('Insira o valor do desconto: '))
calc1 = desc1 / 100
calc2 = calc1 * valor1
calc3 = valor1 - calc2
print('Com o desconto de {} o novo valor do seu produto será de {}. Boas compras!'.format (calc2, calc3 ), end=(''))