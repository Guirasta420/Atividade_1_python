import statistics

print('Bem-vindo ao sistema de notas da Escola')

notas = [10,9,8,7,10,7,8,9,10,10,9,8,7,10]

def media(notas):
    med = statistics.median(notas)
    return med

def moda(notas):
    mod = statistics.mode(notas)
    return mod

def desvio(notas):
    dev = statistics.stdev(notas)
    return dev

maximo = max(notas)
print('Maior nota:', maximo)
minimo = min(notas)
print('Menor nota:' , minimo)
med = media(notas)
print('media:',med)
mod = moda(notas)
print('moda:', mod)
des = desvio(notas)
print('desvio padrão:', des)
