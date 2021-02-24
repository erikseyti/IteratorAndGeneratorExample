# Enumerar uma lista ao iterar ela, com o indice presente na hora da iteracao da lista.
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
print('')
print('_____________________________________________________')
print('')
# caso voce queria que o indice comece com 1 ao inves de 0, passa passar um argumento opcional
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)