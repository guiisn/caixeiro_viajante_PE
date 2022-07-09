import numpy as np


cidades20 = [0.00015020370483398438, 0.0001289844512939453, 0.00012636184692382812, 9.584426879882812e-05, 0.00011014938354492188,
             0.0001308917999267578, 0.00013780593872070312, 0.0001518726348876953, 0.00011801719665527344, 0.00013303756713867188]

media = sum(cidades20) / len(cidades20)
desvio = np.std(cidades20)
tam = np.sqrt(len(cidades20))
intervalo20 = (media + (1.96 * (desvio / tam)))
print(f'\nMédia de tempo para 20 cidades: {media:.6f}')
print(f'Desvio padrão para 20 cidades: {desvio:.6f}')
print(f'Intervalo de confiança para 20 cidades: {intervalo20:.6f}')


cidades50 = [0.0022482872009277344, 0.00022673606872558594, 0.00019621849060058594, 0.00021338462829589844, 0.00023794174194335938,
             0.002806425094604492, 0.00023317337036132812, 0.00020694732666015625, 0.0002129077911376953, 0.0002079010009765625]

media50 = sum(cidades50) / len(cidades50)
desvio50 = np.std(cidades50)
tam50 = np.sqrt(len(cidades50))
intervalo50 = (media50 + (1.96 * (desvio50 / tam50)))
print(f'\nMédia de tempo para 50 cidades: {media50:.6f}')
print(f'Desvio padrão para 50 cidades: {desvio50:.6f}')
print(f'Intervalo de confiança para 50 cidades: {intervalo50:.6f}')


cidades102 = [0.008902788162231445, 0.008126020431518555, 0.00796961784362793, 0.010588645935058594, 0.008170366287231445,
              0.008376598358154297, 0.008214473724365234, 0.008818626403808594, 0.008293390274047852, 0.009701728820800781]

media102 = sum(cidades102) / len(cidades102)
desvio102 = np.std(cidades102)
tam102 = np.sqrt(len(cidades102))
intervalo102 = (media102 + (1.96 * (desvio102 / tam102)))
print(f'\nMédia de tempo para 102 cidades: {media102:.6f}')
print(f'Desvio padrão para 20 cidades: {desvio102:.6f}')
print(f'Intervalo de confiança para 50 cidades: {intervalo102:.6f}')
