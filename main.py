import pandas as pd
import matplotlib.pyplot as plt

# Dados exemplo
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [23, 17, 35, 29]
}
df = pd.DataFrame(data)

# Gera gráfico
plt.bar(df['Categoria'], df['Valores'])
plt.title('Gráfico de Exemplo')
plt.xlabel('Categoria')
plt.ylabel('Valores')
plt.savefig('output/grafico.png')
print('Gráfico salvo em output/grafico.png')
