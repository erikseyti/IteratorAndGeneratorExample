
# podemos iterar por meio de mais de uma lista ao mesmo tempo utilizando o funcao zip()
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)
print('')
print('_____________________________________________________')
print('')
# por se tratar de 2 listas serem iteradas ao mesmo tempo,
# caso uma delas acabe, a iteracao da outra tambem sera interrompida
# retornasse uma tupla, se n for definido na inicializacao os parametros de cada uma delas
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)
print('')
print('_____________________________________________________')
print('')

# para mitigar esse problema temos outra funcao chamada zip_longest.
# por padrao ela ira adicionar um None para caso o valor n seja informado, porem pode se passar um parametro opcional.
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

print('')
print('_____________________________________________________')
print('')


# zip, normalmente é utilizado para quando queremos juntar as listas e depois convertelos normalmente para dicionario
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers,values))
print(s)

print('')
print('_____________________________________________________')
print('')


# podemos utilza-lo tambem para exibir informacoes relacionadas de 2 listas juntas
for name, val in zip(headers, values):
    print(name, '=', val)

print('')
print('_____________________________________________________')
print('')

# podemos passar mais de 2 parametros para o metodo zip(), porem normalmente é utilizado e aconselhavel apenas 2.
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']
for i in zip(a, b, c):
    print(i)

print('')
print('_____________________________________________________')
print('')

# e por fim se quisermos podemos converter as tuplas geradas pela funcao zip em uma lista de tuplas.
zip(a, b)
list(zip(a, b))