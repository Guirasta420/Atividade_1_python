import statistics

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

def calcular_metricas(dados):
    media = statistics.mean(dados)
    mediana = statistics.median(dados)
    moda = statistics.mode(dados)
    desvio_padrao = statistics.stdev(dados) 
    return media, mediana, moda, desvio_padrao
    
metricas_empresa1 = calcular_metricas(empresa1)
metricas_empresa2 = calcular_metricas(empresa2)
metricas_empresa3 = calcular_metricas(empresa3)
metricas_empresa4 = calcular_metricas(empresa4)


print(f"Empresa 1: Média = {metricas_empresa1[0]}, Mediana = {metricas_empresa1[1]}, Moda = {metricas_empresa1[2]}, Desvio Padrão = {metricas_empresa1[3]:.2f}")
print(f"Empresa 2: Média = {metricas_empresa2[0]}, Mediana = {metricas_empresa2[1]}, Moda = {metricas_empresa2[2]}, Desvio Padrão = {metricas_empresa2[3]:.2f}")
print(f"Empresa 3: Média = {metricas_empresa3[0]}, Mediana = {metricas_empresa3[1]}, Moda = {metricas_empresa3[2]}, Desvio Padrão = {metricas_empresa3[3]:.2f}")
print(f"Empresa 4: Média = {metricas_empresa4[0]}, Mediana = {metricas_empresa4[1]}, Moda = {metricas_empresa4[2]}, Desvio Padrão = {metricas_empresa4[3]:.2f}")
# med = media(empresa1)
# med2 = media(empresa2)
# print('Média empresa1:', med)
# print('Média empresa2:', med)

# def moda(empresa1):
#     mod = statistics.mode(empresa1)
#     return mod

# mod = moda(empresa1)
# print('Moda empresa1:', mod)
   
# def mediana(empresa1):
#     medi = statistics.median(empresa1)
#     return medi

# medi = mediana(empresa1)
# print('Mediana empresa1:', medi)

# def desvio(empresa1):
#     des = statistics.stdev(empresa1)
#     return des

# des = desvio(empresa1)
# print('Desvio padrão empresa1:', des)   