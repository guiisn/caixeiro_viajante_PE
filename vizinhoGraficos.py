import matplotlib.pyplot as plt
from vizinhoCalculos import media, media50, media102, desvio, desvio50, desvio102, intervalo20, intervalo50, intervalo102

label = ["20 Cidades", "50 Cidades", '102 Cidades']

mediaValores = [media, media50, media102]
plt.plot(label, mediaValores)
plt.show()

desvioValores = [desvio, desvio50, desvio102]
plt.plot(label, desvioValores)
plt.title('Desvio padrão das amostras - Vizinho mais Próximo')
plt.show()


desvioValores = [intervalo20, intervalo50, intervalo102]
plt.plot(label, desvioValores)
plt.title('Intervalo de confiança - Vizinho mais Próximo')
plt.show()
