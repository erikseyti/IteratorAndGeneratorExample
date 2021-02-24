# gera todos os possiveis valores de permutacao de um grupo de valores de 3 valores
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

# exibe em lista todos os valores gerados pela permutacao de 3 valores
print(list(permutations(items)))
print('_____________________________________________________')

# gera as todas as possiveis permutacoes de uma quantidade x de elementos (nesse caso 2).
# todas as permutacoes de 2 elementos
for p in permutations(items, 2):
    print(p)

# exibe em lista os valores da permutacao contendo apenas 2 elementos.
print(list(permutations(items,2)))
print('_____________________________________________________')

# gera uma sequencia de combinacoes dos elementos, onde a ordem dos elementos nao é considerada no total
from itertools import combinations
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)
print('_____________________________________________________')

# por padrao o combination nao permite escolhe utilizar o mesmo elemento novamente,
# para isso utilize a funcao combinations_with_replacement
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)