CHUNKSIZE = 8192
# podemos trocar um while com apenas uma chamada de uma funcao iter
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)

print('')
print('_____________________________________________________')
print('')

# exemplo de iter com uma expressao lambda
import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
