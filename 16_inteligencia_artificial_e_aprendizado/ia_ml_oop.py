# Importação das bibliotecas
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Classe para representar o Modelo de Machine Learning
class ModeloRegressaoLinear:
    def __init__(self, dados):
        """
        Inicializa o modelo de regressão linear com os dados.
        :param dados: DataFrame com as colunas 'Área' e 'Preço'.
        """
        self.dados = dados
        self.modelo = LinearRegression()

    def preparar_dados(self):
        """
        Prepara os dados separando as variáveis independentes (X) e dependentes (y).
        """
        # Seleciona a coluna 'Área' como X (independente) e 'Preço' como y (dependente)
        self.X = self.dados[['Área']].values
        self.y = self.dados['Preço'].values

    def treinar_modelo(self):
        """
        Treina o modelo de regressão linear com os dados.
        """
        self.modelo.fit(self.X, self.y)

    def prever_preco(self, area_nova):
        """
        Faz a previsão do preço baseado em uma área fornecida.
        :param area_nova: Área da casa a ser prevista.
        :return: Preço previsto.
        """
        return self.modelo.predict([[area_nova]])[0]

    def plotar_regressao(self):
        """
        Plota os dados e a linha de regressão.
        """
        plt.scatter(self.X, self.y, color='blue')  # Dados reais
        plt.plot(self.X, self.modelo.predict(self.X), color='red')  # Linha de regressão
        plt.xlabel('Área (m²)')
        plt.ylabel('Preço (R$)')
        plt.title('Regressão Linear: Preço vs. Área')
        plt.show()

# Classe para manipulação dos dados de entrada
class ManipuladorDeDados:
    def __init__(self, arquivo_csv):
        """
        Inicializa com o arquivo CSV que contém os dados.
        :param arquivo_csv: Caminho do arquivo CSV com os dados.
        """
        self.dados = pd.read_csv(arquivo_csv)

    def visualizar_dados(self):
        """
        Exibe as primeiras linhas do DataFrame para inspeção.
        """
        print(self.dados.head())

    def limpar_dados(self):
        """
        Realiza a limpeza básica de dados (remover valores nulos ou incorretos).
        """
        self.dados.dropna(inplace=True)

# Exemplo de uso das classes
if __name__ == "__main__":
    # Criando uma instância para manipular os dados
    dados = ManipuladorDeDados('dados_imoveis.csv')
    dados.visualizar_dados()
    dados.limpar_dados()

    # Criando e treinando o modelo de regressão
    modelo = ModeloRegressaoLinear(dados.dados)
    modelo.preparar_dados()
    modelo.treinar_modelo()

    # Fazendo uma previsão para uma casa de 110m²
    preco_previsto = modelo.prever_preco(110)
    print(f"Preço previsto para uma casa de 110m²: R${preco_previsto:.2f}")

    # Plotando os dados e a linha de regressão
    modelo.plotar_regressao()
