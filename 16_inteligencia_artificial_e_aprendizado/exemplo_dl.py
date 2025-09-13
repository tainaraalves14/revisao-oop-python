import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Carregando o dataset Iris
data = load_iris()
X = data.data
y = data.target

# Transformando as classes em variáveis one-hot
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y.reshape(-1, 1))

# Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Construindo a rede neural
model = Sequential([
    Dense(10, input_dim=4, activation='relu'),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax')  # 3 classes no dataset Iris
])

# Compilando o modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
model.fit(X_train, y_train, epochs=100, batch_size=10)

# Avaliando o modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acurácia no conjunto de testes: {accuracy * 100:.2f}%')
