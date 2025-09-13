from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
# Vamos prever o preço de uma casa com base na área
X = np.array([[50], [60], [70], [80], [90], [100]])  # Área em metros quadrados
y = np.array([100000, 120000, 140000, 160000, 180000, 200000])  # Preço

# Criando o modelo
modelo = LinearRegression()

# Treinando o modelo com os dados
modelo.fit(X, y)

# Fazendo previsões
area_nova = np.array([[110]])
preco_previsto = modelo.predict(area_nova)

print(f"Preço previsto para uma casa de 110m²: R${preco_previsto[0]:.2f}")

# Plotando os dados e a linha de regressão
plt.scatter(X, y, color='blue')
plt.plot(X, modelo.predict(X), color='red')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.title('Regressão Linear: Preço vs. Área')
plt.show()
