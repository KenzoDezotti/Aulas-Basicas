h = float(input('qual a altura da parede?'))
d = float(input('qual a largura da parede?'))
a=h*d
print('sua parede possui as medidas {} x {} resultando em uma area de {:.2f} metros² e será necessário {:.1f} litros de tinta para pintá-la'.format(h,d,a,a/2))