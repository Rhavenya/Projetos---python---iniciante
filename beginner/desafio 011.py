alt = float(input('Insira aqui a altura do local em metros: '))
larg = float(input('Insira aqui a largura do local em metros: '))
area = alt * larg
tinta = area / 2
print('O local tem {} de área e você precisará de {} baldes de tinta para pinta-la. '.format(area, tinta), end=(''))
